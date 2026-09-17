#!/usr/bin/env python3
"""风起玲珑骨 V2 — 交付包格式质检器 (lint_prompt.py)

把 Preflight 里可机械判定的部分从模型注意力搬到程序上。

用法:
    python scripts/lint_prompt.py <file>            # 检查一个交付包
    python scripts/lint_prompt.py --stdin           # 从标准输入读
    python scripts/lint_prompt.py --skill-check     # 检查 skill 自身健康度
    python scripts/lint_prompt.py <file> --json     # 机器可读输出

退出码: 0 = 无 ERROR, 1 = 有 ERROR, 2 = 用法错误

Windows 提示: 脚本会主动把标准输出与错误输出切换为 UTF-8；
旧环境也可使用 ``python -X utf8 scripts/lint_prompt.py ...``。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def configure_utf8_stdio() -> None:
    """Keep Chinese diagnostics and status icons stable on Windows hosts."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="replace")


configure_utf8_stdio()

# ---------------------------------------------------------------- 规范常量

OUTER_SECTIONS = [
    "【镜头与素材状态】",
    "【参考素材角色表】",
    "【镜头设计摘要】",
    "【完整可复制提示词】",
    "【生成前质检】",
    "【下一轮只建议调】",
]

INNER_HEADINGS = [
    "参考图角色分工：",
    "全局视觉 / 材质 / 光影母版：",
    "全局摄影 / 镜头母版：",
    "开场可见状态与空间调度：",
    "事件 / 表演节拍：",
    "动作物理与材质响应：",
    "声音 / 对白：",
    "连续性锁：",
    "负面限制：",
]

HEADER_FIELDS = ["景别", "焦距", "光源", "机位/运动", "焦点/景深"]

# 长匹配优先，避免 大远景 被切成 远景、中近景 被切成 中景
SHOT_SIZES = [
    "过肩中近景", "过肩近景", "大远景", "大全景", "大特写",
    "中近景", "远景", "全景", "中景", "近景", "特写", "插入",
]

# 必须写 85mm+ 的景别
TIGHT_SIZES = {"中景", "中近景", "近景", "特写", "大特写", "插入",
               "过肩中近景", "过肩近景"}
# 可用广角 24-35mm 的景别
WIDE_SIZES = {"大远景", "远景", "大全景"}

# 必须含近景细节固定句的景别
CLOSE_CLAUSE_SIZES = {"中近景", "近景", "特写", "大特写",
                      "过肩中近景", "过肩近景"}
CLOSE_CLAUSE = "角色毛孔真实细腻，双眼保持清晰眼神光"

CHAR_CEILING = 5000
MAX_NEGATIVES = 5

VISUAL_FAMILIES = ["高调灵境", "青蓝暗域", "暖木人间", "临界大战"]
BASELINE_HEAD = "高规格真人东方玄幻电视剧质感"
EFFECT_ACTIVE = "术法融合："
EFFECT_NONE = "现实变化来源："
EFFECT_NOUNS = ["术法", "粒子", "光环", "能量雾", "法阵", "结界"]

# 禁止出现在围栏内的运营元数据
FENCE_FORBIDDEN_META = [
    "生成模式与有效参考", "目标模型=", "平台画幅=", "构图目标=",
    "同步音频=", "摄影参数仅作创作意图",
]
# 禁止出现在围栏内的会话依赖简写
FENCE_FORBIDDEN_REF = ["同上", "承接前文", "沿用上一版", "同外层", "参考上图"]
# 禁止出现在围栏内的溯源信息
FENCE_FORBIDDEN_PROVENANCE = [
    (r"E\d{2}-S\d{3}", "场景ID"),
    (r"episode-\d+\.txt", "语料文件名"),
    (r"\.pdf", "源PDF文件名"),
    (r"第\s*\d+\s*集", "集数"),
    (r"\b[0-9A-F]{64}\b", "SHA-256 哈希"),
    (r"FQ-EFTV-01", "后台版本号"),
]
# 禁止当风格标签用的片名
FENCE_FORBIDDEN_TITLES = ["逐玉", "苍兰诀"]

# 无控制接口的技术参数 / 拍摄元数据 —— 一律不得进围栏
# 保留焦距 mm，因为它在训练字幕里高频出现且强制配可见透视短语；
# 以下这些只是拍摄设置，Seedance 无对应接口，进围栏即无效 token
NO_INTERFACE_PARAMS = [
    (r"\d+\s*fps", "帧率"),
    (r"\d+\s*帧率", "帧率"),
    (r"\d+\s*[-–]?\s*\d*\s*[xX×]\s*升格", "升格倍率"),
    (r"\bISO\s*\d+", "ISO"),
    (r"\d+(\.\d+)?\s*°", "快门角度"),
    (r"\b4K\b|\b8K\b|\b1080[pP]\b", "分辨率"),
    (r"\bT\d+(\.\d+)?\b", "T光圈"),
    (r"\bf/\d+(\.\d+)?", "f光圈"),
    (r"\d{3,5}\s*K\b", "白平衡开尔文值"),
    (r"ARRI|ALEXA|Sony\s+VENICE|RED\s+KOMODO|Sony\s+FX\d|VENICE|KOMODO",
     "摄影机机身型号"),
    (r"BT\.?709|BT\.?2020|Rec\.?709|sRGB|LogC|S-Log", "色彩空间/输出目标"),
]


class Finding:
    __slots__ = ("level", "rule", "message", "line")

    def __init__(self, level: str, rule: str, message: str, line: int | None = None):
        self.level = level
        self.rule = rule
        self.message = message
        self.line = line

    def as_dict(self) -> dict:
        return {"level": self.level, "rule": self.rule,
                "message": self.message, "line": self.line}


class Linter:
    def __init__(self, text: str):
        self.text = text.replace("\r\n", "\n")
        self.findings: list[Finding] = []
        self.fence = ""
        self.fence_offset = 0

    # -------------------------------------------------------- 报告工具

    def err(self, rule: str, msg: str, line: int | None = None) -> None:
        self.findings.append(Finding("ERROR", rule, msg, line))

    def warn(self, rule: str, msg: str, line: int | None = None) -> None:
        self.findings.append(Finding("WARN", rule, msg, line))

    def _line_of(self, index: int) -> int:
        return self.text.count("\n", 0, index) + 1

    def _fence_line(self, index_in_fence: int) -> int:
        return self._line_of(self.fence_offset + index_in_fence)

    # -------------------------------------------------------- 主流程

    def run(self) -> list[Finding]:
        self.check_outer_sections()
        self.extract_fence()
        if self.fence:
            self.check_inner_headings()
            self.check_char_ceiling()
            self.check_shot_headers()
            self.check_time_format()
            self.check_reference_handles()
            self.check_visual_master()
            self.check_forbidden_in_fence()
            self.check_negatives()
        self.check_role_table_mirror()
        return self.findings

    # -------------------------------------------------------- 各项检查

    def check_outer_sections(self) -> None:
        positions = []
        for name in OUTER_SECTIONS:
            idx = self.text.find(name)
            if idx < 0:
                self.err("outer-sections", f"缺少外层区块 {name}")
            else:
                positions.append((name, idx))
                if self.text.count(name) > 1:
                    self.err("outer-sections",
                             f"外层区块 {name} 出现 {self.text.count(name)} 次，必须只出现一次")
        ordered = [n for n, _ in sorted(positions, key=lambda p: p[1])]
        expected = [n for n in OUTER_SECTIONS if n in ordered]
        if ordered != expected:
            self.err("outer-sections",
                     f"外层区块顺序错误。实际 {' → '.join(ordered)}；应为 {' → '.join(expected)}")

        m = re.search(r"【镜头与素材状态】\s*(.*)", self.text)
        if m and m.group(1).strip() != "直接生成；按已提供素材与文字约束":
            self.err("outer-sections",
                     "【镜头与素材状态】的值必须为「直接生成；按已提供素材与文字约束」，"
                     f"实际为「{m.group(1).strip()[:40]}」")

    def extract_fence(self) -> None:
        anchor = self.text.find("【完整可复制提示词】")
        if anchor < 0:
            self.err("fence", "找不到【完整可复制提示词】，无法检查围栏内容")
            return
        m = re.search(r"```+\s*\w*\s*\n(.*?)\n```+", self.text[anchor:], re.S)
        if not m:
            self.err("fence", "【完整可复制提示词】下方没有找到代码围栏（```）")
            return
        self.fence = m.group(1)
        self.fence_offset = anchor + m.start(1)

    def check_inner_headings(self) -> None:
        positions = []
        for h in INNER_HEADINGS:
            idx = self.fence.find(h)
            if idx < 0:
                self.err("inner-headings", f"围栏内缺少标题 {h}")
            else:
                positions.append((h, idx))
                count = self.fence.count(h)
                if count > 1:
                    self.err("inner-headings",
                             f"围栏内标题 {h} 出现 {count} 次，必须只出现一次")
        ordered = [h for h, _ in sorted(positions, key=lambda p: p[1])]
        expected = [h for h in INNER_HEADINGS if h in ordered]
        if ordered != expected:
            self.err("inner-headings",
                     f"围栏内九标题顺序错误。实际 {' → '.join(ordered)}")
        if positions and not self.fence.lstrip().startswith(INNER_HEADINGS[0]):
            self.err("inner-headings",
                     f"围栏必须直接以「{INNER_HEADINGS[0]}」开头，不得有前导行")

    def check_char_ceiling(self) -> None:
        n = len(self.fence)
        if n > CHAR_CEILING:
            self.err("char-ceiling",
                     f"围栏文字 {n} 字，超过 {CHAR_CEILING} 上限 {n - CHAR_CEILING} 字，需原位压缩")
        else:
            self.findings.append(Finding(
                "INFO", "char-ceiling",
                f"围栏文字 {n} 字（上限 {CHAR_CEILING}，余量 {CHAR_CEILING - n}）"))

    def _shot_blocks(self) -> list[tuple[int, str, str, int]]:
        """返回 [(镜号, 头部行, 表演块, 头部在围栏内的偏移)]"""
        pattern = re.compile(r"^镜头\s*(\d+)\s*｜(.*)$", re.M)
        matches = list(pattern.finditer(self.fence))
        blocks = []
        for i, m in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(self.fence)
            body = self.fence[m.end():end]
            blocks.append((int(m.group(1)), m.group(0), body, m.start()))
        return blocks

    def check_shot_headers(self) -> None:
        blocks = self._shot_blocks()
        if not blocks:
            self.err("shot-headers",
                     "围栏内没有找到 `镜头N｜` 规范头部；单镜也必须使用一个完整镜头头部")
            return

        numbers = [b[0] for b in blocks]
        if numbers != list(range(1, len(numbers) + 1)):
            self.err("shot-headers",
                     f"镜号必须从 1 连续编号。实际为 {numbers}")

        # 疑似遗漏头部：出现 表演 / 动作 / 承接 但前面没有头部
        perf_count = len(re.findall(r"表演\s*/\s*动作\s*/\s*承接", self.fence))
        if perf_count != len(blocks):
            self.err("shot-headers",
                     f"镜头头部 {len(blocks)} 个，`表演 / 动作 / 承接` {perf_count} 个，"
                     "两者必须相等（每镜一个头部一段表演）")

        for num, header, body, off in blocks:
            line = self._fence_line(off)

            # 字段齐全与顺序
            found = [f for f in HEADER_FIELDS if f + "：" in header]
            missing = [f for f in HEADER_FIELDS if f not in found]
            if missing:
                self.err("header-fields",
                         f"镜头{num} 头部缺字段：{'、'.join(missing)}", line)
            idxs = [header.find(f + "：") for f in found]
            if idxs != sorted(idxs):
                self.err("header-fields",
                         f"镜头{num} 头部字段顺序错误，必须为 "
                         f"{'→'.join(HEADER_FIELDS)}", line)

            # 表演必须在头部之后，不得有旧式摄影尾注
            if re.search(r"摄影参数\s*[:：]", body):
                self.err("camera-tail",
                         f"镜头{num} 表演之后追加了旧式摄影尾注，应删除", line)

            # 景别与焦距绑定
            size = next((s for s in SHOT_SIZES if s in header), None)
            focal = re.search(r"(\d+)\s*mm", header)
            if size and focal:
                mm = int(focal.group(1))
                if size in TIGHT_SIZES and mm < 85:
                    self.err("focal-rule",
                             f"镜头{num} 景别「{size}」使用 {mm}mm，"
                             "中景及以下必须 85mm 以上", line)
                if size == "全景" and mm > 65:
                    self.warn("focal-rule",
                              f"镜头{num} 全景使用 {mm}mm，全景只在需要身体关系时用 65mm", line)
                if size in WIDE_SIZES and mm > 35:
                    self.warn("focal-rule",
                              f"镜头{num} 景别「{size}」使用 {mm}mm，"
                              "大远景/远景/大全景通常为 24-35mm", line)
            elif size and not focal:
                self.err("focal-rule", f"镜头{num} 焦距字段没有具体毫米值", line)

            # 焦距必须带可见透视结果，不能只有毫米数
            if focal:
                mm = int(focal.group(1))
                fseg = re.search(r"焦距：([^｜]*)", header)
                fseg_text = fseg.group(1) if fseg else ""
                if mm >= 85 and "压缩" not in fseg_text:
                    self.err("focal-phrase",
                             f"镜头{num} 85mm+ 必须补「摄影机远离主体，背景拉近，压缩前后景」"
                             "类可见结果，不能只写毫米数", line)
                if mm <= 35 and "近大远小" not in fseg_text and "纵向展开" not in fseg_text:
                    self.err("focal-phrase",
                             f"镜头{num} 广角必须补「摄影机靠近主体，近大远小，空间纵向展开」"
                             "类可见结果", line)
                if 40 <= mm <= 65 and "中等机距" not in fseg_text:
                    self.err("focal-phrase",
                             f"镜头{num} 40-65mm 必须补「中等机距，人物比例自然，空间轻压缩」"
                             "类可见结果", line)

            # 单值，不得留备选
            for fname in HEADER_FIELDS:
                seg = re.search(rf"{re.escape(fname)}：([^｜\n]*)", header)
                if seg and re.search(r"[/或~]|～|、\s*备选", seg.group(1)):
                    if fname != "机位/运动":  # 该字段名自带斜杠
                        self.warn("single-value",
                                  f"镜头{num} 字段「{fname}」疑似留了备选值："
                                  f"{seg.group(1).strip()[:30]}", line)

            # 近景细节固定句
            if size in CLOSE_CLAUSE_SIZES:
                cnt = body.count(CLOSE_CLAUSE)
                if cnt == 0:
                    self.err("close-clause",
                             f"镜头{num} 景别「{size}」缺少固定句「{CLOSE_CLAUSE}」"
                             "（仅无可读面部的道具/肢体插入可豁免）", line)
                elif cnt > 1:
                    self.err("close-clause",
                             f"镜头{num} 固定句出现 {cnt} 次，应恰好一次", line)

            # 表演篇幅底线
            hlen, blen = len(header), len(body.strip())
            if blen < hlen:
                self.err("performance-floor",
                         f"镜头{num} 表演段 {blen} 字 < 头部 {hlen} 字，"
                         "表演篇幅必须不少于该镜一半", line)

            # 抽象标签
            for tag in ["神情复杂", "眼神一冷", "情绪崩溃", "若有所思",
                        "表演细腻", "情绪复杂"]:
                if tag in body:
                    self.err("abstract-label",
                             f"镜头{num} 出现抽象标签「{tag}」，"
                             "必须落到眼睑/视线/咬肌/喉结/呼吸/指尖/重心", line)

            # 面部崩坏词
            for bad in ["面部扭曲", "面部形变"]:
                if bad in body:
                    self.err("face-breakdown",
                             f"镜头{num} 出现「{bad}」，与身份锁定指令打架，必须改写", line)

            # 下一镜承接
            if num < len(blocks) and not re.search(r"承接|镜末|交接|下一镜", body):
                self.warn("handoff",
                          f"镜头{num} 未见镜末状态或下一镜承接描述", line)

    def check_time_format(self) -> None:
        for m in re.finditer(r"\d+\.\d+\s*s\b", self.fence):
            self.err("time-format", f"围栏内出现小数秒「{m.group(0)}」，必须用整数秒",
                     self._fence_line(m.start()))
        for m in re.finditer(r"\d{1,2}:\d{2}", self.fence):
            self.err("time-format", f"围栏内出现冒号时间码「{m.group(0)}」，"
                     "诊断时间码必须留在围栏外", self._fence_line(m.start()))
        for m in re.finditer(r"\d+\s*[~～–—]\s*\d+\s*s", self.fence):
            self.err("time-format", f"时间范围「{m.group(0)}」分隔符必须是 ASCII 连字符 -",
                     self._fence_line(m.start()))
        for m in re.finditer(r"\d+\s*[-至到]\s*\d+\s*秒", self.fence):
            self.err("time-format", f"时间范围「{m.group(0)}」不得用中文「秒」后缀，应写 N-Ns",
                     self._fence_line(m.start()))
        for m in re.finditer(r"(\d+)-(\d+)s", self.fence):
            a, b = int(m.group(1)), int(m.group(2))
            if a >= b:
                self.err("time-format",
                         f"时间范围「{m.group(0)}」起点不小于终点",
                         self._fence_line(m.start()))

    def check_reference_handles(self) -> None:
        if "无上传素材；使用文本锁定。" in self.fence:
            stray = re.search(r"@(图片|视频|音频)\s*\d+", self.fence)
            if stray:
                self.err("handles",
                         f"已声明无上传素材，却仍出现句柄「{stray.group(0)}」")
            return

        for modality in ["图片", "视频", "音频"]:
            nums = sorted({int(m.group(1)) for m in
                           re.finditer(rf"@{modality}\s*(\d+)", self.fence)})
            if not nums:
                continue
            if nums != list(range(1, len(nums) + 1)):
                self.err("handles",
                         f"@{modality} 编号必须从 1 连续。实际为 {nums}")
            for n in nums:
                pat = re.compile(rf"^.*@{modality}\s*{n}\D.*$", re.M)
                lines = [l for l in pat.findall(self.fence) if "只锁定" in l]
                if not lines:
                    self.err("handles",
                             f"@{modality} {n} 缺少完整的「只锁定……，不复制……。」说明句")
                elif not any("不复制" in l for l in lines):
                    self.err("handles",
                             f"@{modality} {n} 的说明句缺少「不复制」拒绝边界")

        for bad in re.finditer(r"@(Image|Video|Audio|image|video|audio)\s*\d+",
                               self.fence):
            self.err("handles",
                     f"出现英文句柄「{bad.group(0)}」，必须用 @图片 N / @视频 N / @音频 N")

    def check_visual_master(self) -> None:
        seg = self._section("全局视觉 / 材质 / 光影母版：")
        if seg is None:
            return
        if BASELINE_HEAD not in seg:
            self.err("visual-master",
                     f"全局视觉母版缺少固定质量基线（应以「{BASELINE_HEAD}」开头的整段）")
        if seg.count(BASELINE_HEAD) > 1:
            self.err("visual-master", "固定质量基线重复出现，应只写一次，不得逐镜重复")

        fams = [f for f in VISUAL_FAMILIES if f in seg]
        if len(fams) == 0:
            self.err("visual-master",
                     f"缺少已解析的视觉家族句，必须从 {'/'.join(VISUAL_FAMILIES)} 选恰好一个")
        elif len(fams) > 1:
            self.err("visual-master",
                     f"视觉家族必须恰好一个，实际出现 {len(fams)} 个：{'、'.join(fams)}")

        active, none_ = EFFECT_ACTIVE in seg, EFFECT_NONE in seg
        if active and none_:
            self.err("effect-branch", "术法状态分支必须二选一，不得同时写 active 和 none")
        elif not active and not none_:
            self.err("effect-branch",
                     f"缺少术法状态分支，必须写「{EFFECT_ACTIVE}」或「{EFFECT_NONE}」之一")
        elif none_:
            leaked = [w for w in EFFECT_NOUNS if w in self.fence]
            if leaked:
                self.err("effect-branch",
                         f"已声明 effect=none，围栏内却出现效果名词：{'、'.join(leaked)}。"
                         "无术法分支不得出现这些词，负向关键词会反向预激活装饰特效")

    def _section(self, heading: str) -> str | None:
        start = self.fence.find(heading)
        if start < 0:
            return None
        start += len(heading)
        ends = [self.fence.find(h, start) for h in INNER_HEADINGS]
        ends = [e for e in ends if e > 0]
        return self.fence[start:min(ends)] if ends else self.fence[start:]

    def check_forbidden_in_fence(self) -> None:
        for token in FENCE_FORBIDDEN_META:
            if token in self.fence:
                self.err("fence-metadata",
                         f"围栏内出现运营元数据「{token}」，应移到【镜头设计摘要】或后台记录")
        for token in FENCE_FORBIDDEN_REF:
            if token in self.fence:
                self.err("fence-shorthand",
                         f"围栏内出现会话依赖简写「{token}」，每镜必须自足")
        for pat, label in FENCE_FORBIDDEN_PROVENANCE:
            m = re.search(pat, self.fence)
            if m:
                self.err("fence-provenance",
                         f"围栏内出现{label}「{m.group(0)}」，溯源信息必须留在围栏外",
                         self._fence_line(m.start()))
        for title in FENCE_FORBIDDEN_TITLES:
            if title in self.fence:
                self.err("style-label",
                         f"围栏内出现片名「{title}」，不得当风格标签，"
                         "必须翻译成可见的光位/构图/材质控制")
        for pat, label in NO_INTERFACE_PARAMS:
            m = re.search(pat, self.fence)
            if m:
                self.err("capture-metadata",
                         f"围栏内出现拍摄元数据{label}「{m.group(0).strip()}」。"
                         "Seedance 无对应控制接口，应留在后台记录或【镜头设计摘要】，"
                         "围栏内只写它造成的可见结果",
                         self._fence_line(m.start()))

    def check_negatives(self) -> None:
        seg = self._section("负面限制：")
        if seg is None:
            return
        items = [s for s in re.split(r"[；;\n]|(?<=[^0-9])、", seg) if s.strip()]
        if len(items) > MAX_NEGATIVES:
            self.err("negatives",
                     f"负面限制 {len(items)} 条，上限 {MAX_NEGATIVES} 条，"
                     "只保留有实据的真实风险")
        for lock in ["不得出现", "禁止出现", "画面中只能有", "人数固定"]:
            if lock in seg:
                self.warn("negatives",
                          f"负面限制里出现锁定式写法「{lock}」，"
                          "站位/人数/道具身份应由正面描写解决")

    def check_role_table_mirror(self) -> None:
        if not self.fence:
            return
        outer_start = self.text.find("【参考素材角色表】")
        outer_end = self.text.find("【镜头设计摘要】")
        if outer_start < 0 or outer_end < 0:
            return
        outer = self.text[outer_start:outer_end]
        if "参考图角色分工：" not in outer:
            self.err("role-mirror",
                     "外层【参考素材角色表】必须同样以「参考图角色分工：」开头")
            return

        def sentences(block: str) -> set[str]:
            return {re.sub(r"\s+", "", s) for s in
                    re.findall(r"[^\n]*只锁定[^\n]*不复制[^\n]*", block)}

        o, i = sentences(outer), sentences(self.fence)
        for miss in o - i:
            self.err("role-mirror",
                     f"外层角色表有、围栏内缺的说明句：{miss[:50]}…")
        for miss in i - o:
            self.err("role-mirror",
                     f"围栏内有、外层角色表缺的说明句：{miss[:50]}…")


def lint_document(text: str) -> list[Finding]:
    """Validate every complete delivery package in one response."""
    normalized = text.replace("\r\n", "\n")
    package_head = OUTER_SECTIONS[0]
    starts = [m.start() for m in re.finditer(re.escape(package_head), normalized)]
    prompt_blocks = normalized.count("【完整可复制提示词】")

    if len(starts) <= 1:
        return Linter(normalized).run()

    findings: list[Finding] = []
    if prompt_blocks != len(starts):
        findings.append(Finding(
            "ERROR",
            "document-packages",
            f"检测到 {len(starts)} 个交付包起点，但有 {prompt_blocks} 个完整提示词区块；"
            "每个交付包必须各有一个完整提示词区块",
        ))

    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(normalized)
        package_text = normalized[start:end].strip()
        line_offset = normalized.count("\n", 0, start)
        package_findings = Linter(package_text).run()
        for finding in package_findings:
            finding.message = f"交付包{index + 1}：{finding.message}"
            if finding.line is not None:
                finding.line += line_offset
        findings.extend(package_findings)

    return findings


# ---------------------------------------------------------------- skill 自检

def skill_check(root: Path) -> list[Finding]:
    out: list[Finding] = []
    skill = root / "SKILL.md"
    if not skill.exists():
        out.append(Finding("ERROR", "skill", f"找不到 {skill}"))
        return out

    text = skill.read_text(encoding="utf-8")
    refs = root / "references"

    # 悬空外部依赖
    deps = sorted({m.group(0) for f in [skill] + sorted(refs.glob("*.md"))
                   for m in re.finditer(r"\$[a-z][a-z0-9-]{5,}",
                                        f.read_text(encoding="utf-8"))})
    for d in deps:
        out.append(Finding("ERROR", "dangling-dep",
                           f"仍引用外部 skill「{d}」，本 skill 必须自足"))

    # 链接的 reference 是否都存在
    for m in re.finditer(r"\(references/([a-z0-9.-]+\.md)\)", text):
        if not (refs / m.group(1)).exists():
            out.append(Finding("ERROR", "broken-link",
                               f"SKILL.md 链接了不存在的 {m.group(1)}"))

    # references 是否都被 SKILL.md 链接
    linked = {m.group(1) for m in re.finditer(r"\(references/([a-z0-9.-]+\.md)\)", text)}
    for f in sorted(refs.glob("*.md")):
        if f.name not in linked:
            out.append(Finding("WARN", "orphan-ref",
                               f"{f.name} 存在但 SKILL.md 未链接，不会被路由到"))

    # 哈希漂移
    checklist = refs / "capability-regression-checklist.md"
    if checklist.exists():
        import hashlib
        ctext = checklist.read_text(encoding="utf-8")
        for f in sorted(refs.glob("*.md")):
            if f.name == checklist.name:
                continue
            digest = hashlib.sha256(f.read_bytes()).hexdigest().upper()
            if f"`{f.name}`" in ctext and digest not in ctext:
                out.append(Finding("ERROR", "hash-drift",
                                   f"{f.name} 内容已变但回归清单里的哈希未更新 → {digest}"))

    # 行数目标
    n = len(text.splitlines())
    if n > 500:
        out.append(Finding("WARN", "skill-size",
                           f"SKILL.md {n} 行，超过回归清单的 500 行目标 {n - 500} 行"))

    if not any(f.level == "ERROR" for f in out):
        out.append(Finding("INFO", "skill", "skill 结构自检通过"))
    return out


# ---------------------------------------------------------------- 入口

def main() -> int:
    p = argparse.ArgumentParser(
        description="风起玲珑骨 V2 交付包格式质检器")
    p.add_argument("file", nargs="?", type=Path, help="待检查的交付包文本文件")
    p.add_argument("--stdin", action="store_true", help="从标准输入读取")
    p.add_argument("--skill-check", action="store_true", help="检查 skill 自身健康度")
    p.add_argument("--json", action="store_true", help="输出 JSON")
    args = p.parse_args()

    if args.skill_check:
        findings = skill_check(Path(__file__).resolve().parent.parent)
    elif args.stdin:
        findings = lint_document(sys.stdin.read())
    elif args.file:
        if not args.file.exists():
            print(f"找不到文件: {args.file}", file=sys.stderr)
            return 2
        findings = lint_document(args.file.read_text(encoding="utf-8"))
    else:
        p.print_help()
        return 2

    errors = [f for f in findings if f.level == "ERROR"]
    warns = [f for f in findings if f.level == "WARN"]

    if args.json:
        print(json.dumps(
            {"status": "FAIL" if errors else "PASS",
             "errors": len(errors), "warnings": len(warns),
             "findings": [f.as_dict() for f in findings]},
            ensure_ascii=False, indent=2))
        return 1 if errors else 0

    icon = {"ERROR": "✗", "WARN": "!", "INFO": "·"}
    for f in findings:
        loc = f" (第{f.line}行)" if f.line else ""
        print(f"{icon[f.level]} [{f.rule}]{loc} {f.message}")
    print()
    print(f"{'FAIL' if errors else 'PASS'} — {len(errors)} 个错误, {len(warns)} 个提醒")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
