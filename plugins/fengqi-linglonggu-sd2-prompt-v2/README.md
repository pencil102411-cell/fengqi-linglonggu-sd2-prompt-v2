# 风起玲珑骨 · Seedance 2.0 / 2.5 影视提示词插件

《风起玲珑骨》专用的 Codex 插件，版本 **2.3.0**。从人物、场景、剧本或文字分镜直接编译横屏真人影视感视频提示词。

## 能做什么

- 反查 1—24 集定稿剧本，核验人物身份、关系、知情范围和当前状态。
- 设计微表情、视线、对白、动作接触与连续表演。
- 组织逐镜摄影参数、叙事灯光、仙侠特效和武打动作。
- 按 Seedance 2.0 或 2.5 目标输出瑞宝 PRO 六段交付包；完整可复制提示词不超过 5000 字。
- 分析生成结果并返修；指定局部修改时冻结其余原文。

本插件只适用于《风起玲珑骨》，不会把本剧正典套用到其他项目。它生成和检查提示词，不直接调用即梦或视频生成 API。

## 安装到 Codex

在支持插件的 Codex CLI 中执行：

```sh
codex plugin marketplace add pencil102411-cell/fengqi-linglonggu-sd2-prompt-v2
codex plugin add fengqi-linglonggu-sd2-prompt-v2@fengqi-linglonggu
```

安装后在 Codex 新建任务，明确调用本插件或 skill，并提供剧情、目标模型和实际参考素材。以上命令供使用者安装，本仓库的发布过程不要求在发布者电脑上安装插件。

也可以从 [Releases](https://github.com/pencil102411-cell/fengqi-linglonggu-sd2-prompt-v2/releases) 下载插件 ZIP。ZIP 根目录直接包含 `.codex-plugin/plugin.json` 与 `skills/`。

## 使用示例

```text
使用 fengqi-linglonggu-sd2-prompt-v2，为《风起玲珑骨》以下剧情生成 Seedance 2.5 提示词。
剧情：[粘贴剧情或文字分镜]
角色：[角色及当前状态]
参考素材：[说明实际提供的图片或视频]
要求：[时长、镜头、对白与需要保留的细节]
```

局部返修请提供上一版完整提示词，再指定允许修改的镜头或段落，例如“只修改镜头 2 的转身动作，其余逐字不变”。

## 包含的资料

- 原始 skill 与参考规则，保留原文。
- 4 份定稿剧本 PDF，共覆盖 24 集；24 份逐集文本、剧本索引与来源校验清单。
- 剧本检索、语料构建、提示词检查脚本及回归样例。

```text
.agents/plugins/marketplace.json
plugins/fengqi-linglonggu-sd2-prompt-v2/
  .codex-plugin/plugin.json
  skills/fengqi-linglonggu-sd2-prompt-v2/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
```

## 检查与维护

普通提示词使用无需额外 Python 依赖。检索与检查脚本使用 Python 3.10+；仅重新从 PDF 构建语料时需要 `pypdf`。

```sh
python -m unittest discover -s plugins/fengqi-linglonggu-sd2-prompt-v2/skills/fengqi-linglonggu-sd2-prompt-v2/scripts -p "test_*.py" -v
```

GitHub Actions 在云端完成目录整理、插件与资源完整性检查、PDF 哈希校验、回归测试及 ZIP 打包。发布任务可在 Actions 页面手动运行。已有版本的 Release 保持不变；更新发布需先修改插件版本。

## 开源许可

本仓库采用 [MIT License](LICENSE)。保留许可证和版权声明后，可以使用、修改和分发。影视作品名称用于说明参考分析来源，不代表与相关作品、Seedance 或 OpenAI 存在官方合作关系。
