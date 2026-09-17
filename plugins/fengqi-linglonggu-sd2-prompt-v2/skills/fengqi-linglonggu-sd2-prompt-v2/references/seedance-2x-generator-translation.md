# CineVisible Compiler: Film Grammar To Seedance 2.0 / 2.5

Use this reference after project truth, character canon, supplied scene/character settings, plot or written storyboard, shot requirements, and actual reference roles are resolved. It directly converts that production intent into executable natural Chinese for Seedance 2.0 or Seedance 2.5 without a scene-asset gate or automatic image generation. The always-on visual quality baseline remains owned by [eastern-fantasy-tv-visual-master.md](eastern-fantasy-tv-visual-master.md); this compiler must carry it into the existing global visual field without abbreviation. It does not own story truth, character identity, final optics, the canonical global-master/per-shot-header camera schema, or the 瑞宝PRO outer package.

## 1. Verified Model Boundary

The maintained platform facts below come from the official Seed pages and launch notes. Treat every workflow rule derived from them as a conservative production inference, not as an undocumented platform guarantee.

| Profile | Verified single-pass duration | Verified single-pass reference capacity | Prompt consequences |
|---|---:|---:|---|
| `Seedance 2.0` | up to 15 seconds | up to 9 images, 3 videos, 3 audio references | Use a compact short-clip spine: one main event, two to three motivated dramatic beats, three to five small visible state changes, and one dominant camera behavior. |
| `Seedance 2.5` | up to 30 seconds | up to 30 images, 10 videos, 10 audio references | A 16-30 second request may use a timed narrative spine, explicit transition mechanisms, and time-scoped reference roles. A simple short request stays compact and is not inflated merely because the model is newer. |

Seedance 2.5 officially adds finer timestamp-level control, stronger long-form transition/continuity handling, reference-based editing, and broader image/video/audio capacity. It also supports motion, camera, green-screen, and clay/white-model references when those assets and product modes actually exist. The official materials still acknowledge limitations in complex physical motion and very dense multi-subject interaction. Never remove force, contact, continuity, or identity controls merely because the target is 2.5.

Official sources:

- Seedance 2.0: <https://seed.bytedance.com/zh/blog/official-launch-of-seedance-2-0> and <https://seed.bytedance.com/zh/seedance2_0>
- Seedance 2.5: <https://seed.bytedance.com/zh/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5> and <https://seed.bytedance.com/zh/seedance2_5>

Do not present the following project controls as universal Seedance API guarantees: exact camera body, focal length, T-stop, shutter angle, ISO, white balance, frame rate, color space, the 5000-character project contract, or the maximum number of extension rounds. They remain this skill's cinematic-intent controls or confirmed current-UI choices. Separate hard product settings from composition intent in the backstage target record and, when useful to the operator, `【镜头设计摘要】`: record the real platform-selectable ratio, the 2.39:1/2.40:1 active-picture target when used, one synchronous-audio choice, and that camera metadata is creative intent rather than a platform guarantee. Do not emit this operational metadata as the first line or any equivalent key-value preamble inside `【完整可复制提示词】`; the fenced copy begins with `参考图角色分工：`. When the active Seedance entry offers `21:9` rather than exact 2.39:1/2.40:1, select `21:9`, keep the requested safe composition, and state the post-crop outside the fence. Exact delivery frame rate likewise requires a confirmed product setting or post-conform step. Do not output `camera_fixed` as a required Seedance 2.0 API/UI parameter; express a locked camera through visible natural-language support and motion instructions such as `三脚架锁定，全程不移动`.

## 2. Target-Profile Router

Resolve one target profile before shot decomposition and preserve it through generation and repair:

1. An explicit `Seedance/SD 2.0` or `Seedance/SD 2.5` request wins.
2. When the user explicitly requests both versions, compile two independent, self-contained ready-state packages. Never put competing model names, durations, reference limits, or alternative instructions inside one fenced generator block.
3. A returned or extended video preserves the model version that generated the source unless the user explicitly requests migration. A retry never upgrades the model silently.
4. For a bare `SD2`, `Seedance`, or `即梦 SD` request that fits 15 seconds and the 2.0 reference limits, preserve backward compatibility and select `Seedance 2.0`.
5. For an otherwise unspecified request longer than 15 seconds but no longer than 30 seconds, or one that exceeds a 2.0 reference capacity but fits 2.5, select `Seedance 2.5` and state the resolved target in the backstage record and `【镜头设计摘要】`, not inside the fenced copy block.
6. When an explicit 2.0 request exceeds 15 seconds or its reference limits, split it into self-contained 2.0 invocations with concrete handoff states; do not silently relabel it 2.5. When an explicit 2.5 request exceeds 30 seconds, use extension/self-contained continuation packages.
7. If the requested model version or product mode is unknown, do not invent a capability profile. Stop at a separate target-profile incompatibility notice; do not invent a scene-asset status or automatic-image workaround.

The source-match route is orthogonal to the model route. Selecting 2.5 does not activate 25fps, BT.709, 2.40:1, `逐玉原片质感`, or `苍兰诀原片质感`. Resolve model, comparator craft, and technical source match as three separate decisions.

## 3. CineVisible Intermediate Record

Keep this record backstage. Do not paste it as JSON, YAML, analysis notes, or pseudo-code into the generator prompt.

```text
target: model version, generation mode, duration, platform-selectable ratio, active-picture composition target, synchronous-audio switch, product/UI constraints
assets: actual UI handle, modality, primary role, controlled attributes, forbidden overrides, priority, active time span
scene: place, time, weather, fixed geography, depth planes, materials
subjects: identity lock, screen position, facing, gaze, posture, action, prop/contact state
look: visual_master_version=FQ-EFTV-01, one resolved scene family, one resolved effect-state branch, exact compiled visual-master text, first visual read, palette, texture, material response, atmosphere
lighting: motivated source, world position, apparent size/quality, coverage, exact dark-side relation, spill, separation, exposure, catchlight
camera: support, position, height, side, angle, shot size/occupancy, optics, axis, movement trigger/path/stop/end framing
effect: active/none, function, source anchor, geometry, propagation, target/contact, occlusion, interaction light, physical response, decay/residue
state_chain: visible opening, trigger, action, response, visible end, next-beat handoff
audio: speaker, dialogue, ambience, foley, music/silence, timed trigger
continuity: persistent facts, permitted changes, forbidden resets
```

Every retained item must answer at least one of these questions: what can the camera see, what can the microphone hear, what supplied asset controls it, or what current UI value must be selected? Delete analytical labels that answer none of them.

## 4. Observation-To-Instruction Compiler

Translate analysis into visible proof instead of decorative adjectives:

| Analytical observation | Executable conversion |
|---|---|
| `高级 / 电影感 / 仙气 / 苍兰诀感` | Delete the label. State the first visual read, motivated light source and contrast, exact composition, material response, depth, action timing, and camera behavior. |
| `人物紧张` | State gaze target and interruption, breath change, jaw/hand tension, posture, delay before speech, and the final visible state. |
| `人物强大` | State stable base, force path, contact result, minimal recovery, partner/environment response, and whether the subject yields ground. |
| `压迫感` | State camera height/side, subject occupancy, foreground occlusion, headroom, spatial compression, shadow allocation, and the visible power distance. |
| `光影漂亮` | State source, world-space direction/height, apparent size and hardness, coverage/falloff, dark-side difference, spill control, separation, material/catchlight response. |
| `震撼特效` | State function, source anchor, geometry, path, contact, depth/occlusion, interaction light, body/environment response, decay, and residue. |
| `运镜有张力` | State support, opening frame, trigger, path/direction/speed, occluder or transition bridge when relevant, stop condition, end framing, and what change the move proves. |
| `节奏紧凑 / 舒缓` | Express it through the number and duration of beats, response delays, cut/transition triggers, action density, silence, and audio entrances/exits. |
| `真实质感` | State skin/fabric/metal/wood/water/snow roughness, contact shadow, deformation, inertia, reflections, stains, and light response relevant to the event. |

Use this minimum natural-language pattern:

```text
[时空与开场可见状态]。当[可见或可听触发]，[明确主体沿明确路径行动]；
[目标物、人物或环境产生可见响应]，最后停在[稳定终态/交接状态]。
镜头从[支撑、机位、起始景别]在[触发时刻]沿[路径]移动至[结束构图]，证明[关键变化]。
[动机光源]从[世界方位与高度]照到[具体人物/表面]，形成[阴影、反射、材质或眼神光结果]。
```

Do not make every sentence equally detailed. Give the most words to identity, opening/end state, event causality, contact, first visual read, and the one camera behavior that proves the event.

## 5. Five Visual Systems To Nine Prompt Fields

The five learned systems must survive into the existing nine inner headings:

| Learned system | Required model-facing destinations |
|---|---|
| Visual quality master | `全局视觉 / 材质 / 光影母版` begins with the exact `FQ-EFTV-01` baseline once, then exactly one resolved `本段视觉家族` sentence, exactly one resolved `effect=active/none` branch, and current-scene light/material facts. The no-effect branch contains no effect vocabulary. The version code stays backstage; the baseline is never repeated per shot or replaced by a source-drama title. |
| Lighting | `全局视觉 / 材质 / 光影母版` for the complete same-scene motivated master; each shot header's `光源` says `本场景母版，无变化` when unchanged or only the real shot delta when changed; `事件 / 表演节拍` for visible event-light response; `连续性锁` for world coordinates and exposure invariants. |
| VFX | `开场可见状态与空间调度` for the initial active/absent state and anchor; `事件 / 表演节拍` for cause/state chain; `动作物理与材质响应` for contact and response; `连续性锁` for residue/end state; `负面限制` only for the actual failure risks. |
| Camera position | `全局摄影 / 镜头母版` for the shared capture/axis setup; each front-loaded shot header for exact shot size, focal, camera relation, and focus/depth. |
| Camera movement / transition | `全局摄影 / 镜头母版` for the dominant support/movement policy; each shot header's `机位/运动` for its exact relation and permitted delta; the following performance/action prose for trigger/path/stop/end hold and transition bridge. |

The compiler may not create a second camera schema. `camera-parameter-presets.md` remains the sole canonical two-layer contract: shared capture/light facts in the global masters, then `镜头号→景别→焦距→光源→机位/运动→焦点/景深` before each shot's `表演 / 动作 / 承接`. The retired full camera tail must not be appended after performance.

## 6. Lighting Sentence Contract

Compile a light observation in this order:

```text
story function -> motivated source -> world side/height -> apparent size and quality
-> coverage/falloff -> camera-to-key relation -> exact dark-side difference
-> only relevant spill control -> one separator/practical/effect layer
-> exposure priority -> material response -> catchlight state
```

Example of executable phrasing:

```text
雪夜西北侧云后月光从人物右后上方斜入，脸宽三倍的定向冷柔光只覆盖双眼、右肩和掌前雪面；
摄影机位于暗侧，左脸低主光1.5档，南侧暗林压住雪地返光；同源轮廓只勾亮右肩衣缘与飞雪，双眼保留右上单一低亮眼神光。
```

For event light, state the exact surface and relative priority. Prefer `结界冷白折射低主光0.5档，只落在掌缘和近雪` over `蓝色能量照亮全场`. Do not let effect light erase the motivated world light unless the story explicitly performs that transition.

## 7. Effect Compiler

When `effect = active`, retain the minimum complete chain:

```text
opening absence/lock -> pre-cue -> birth at exact source -> geometry and propagation
-> depth/occlusion/parallax -> contact/target response -> peak and interaction light
-> body/fabric/prop/environment response -> decay -> residue/end state
```

The final Chinese prose must name the single story function, one dominant geometry, and one main color family. Use surface topology for corrosion, frost, cracks, liquid, or crawling marks; use clear volume and depth planes for clouds, waves, barriers, pressure fields, or projectiles.

Example:

```text
开场掌前无结界；来袭风压先把掌前雪粒推成一条弧线，掌心随即生出近无色半球薄膜。
薄膜从掌心向外展开，前景飞雪短暂遮住下沿，冲击接触后只在接触点压凹并沿弧面泄散；
掌缘和近雪被冷白折射提亮半档，袖口后掀半拍，结尾薄膜由边缘向掌心退散，雪面留下半环压痕。
```

When `effect = none`, do not leave an empty effect section or import fantasy decoration from a comparator. Drive change through acting, contact, existing light, cloth, weather, dust, water, sound, or props with physical causes. When a fantasy comparator is active and leakage risk is real, one concise sentence is enough: `画面变化只来自现有光源、人物动作和物体物理响应，不出现自发光图形、能量雾或环境异变。`

## 8. Camera Position, Movement, And Transition Compiler

Position must describe a relation, not only a lens:

```text
摄影机位于主体东南侧、略低于胸口、仰角5°；人物居画面右三分之一、占画高七成；
前景门框遮住左肩边缘，背景只见一层虚焦窗纸和暗木。
```

Every move uses `support -> opening frame -> trigger -> path/speed -> stop -> end framing/end hold -> narrative proof`:

```text
三脚架开场停留半拍；人物抬眼时才沿视线方向缓慢推近，双眼进入近景后停止并停留一拍，证明她已认出门外来人。
```

Every transition uses an executable bridge such as a motivated cut, foreground occluder, action handoff, sound bridge, gaze handoff, or light-state change. State the first visible condition after the transition. Delete `丝滑转场`, `震撼推进`, `镜头飞舞`, and movement that does not reveal a new fact.

For a complex effect, fight, contact, or multi-person interaction, prefer a locked camera or one short peak response. Camera energy never substitutes for readable action physics.

## 9. State-Chain And Continuity Contract

Every dramatic beat must create a visible or audible difference:

```text
S0 visible start -> trigger -> subject action -> object/partner/environment response
-> S1 visible end and next-beat handoff
```

`end(Sn)` must be usable as `start(Sn+1)`. Preserve screen side, gaze target, prop hand, open/closed doors, wetness, damage, costume state, wounds, effect residue, source-light coordinates, sound state, and partner distance unless the prompt visibly changes them.

`悲伤后振作` is not sufficient. Use visible proof such as `垂眼握紧纸条；听见名字后呼吸停半拍；抬眼时手指松开，纸条仍留在右手`.

## 10. Reference-Role Compiler

Use a canonical product-visible asset handle for every actual reference in the invocation; never assign a handle to an absent asset. For JiMeng/Seedance ready-state packages, use the visible Chinese handle syntax `@图片 1`, `@图片 2`, `@视频 1`, and `@音频 1`. For a 2.5-only clay/white-model or edit mode, preserve the exact handle exposed by the active product rather than inventing a token. Number from one in the declared upload order for each modality. When preparing the package before UI upload, the package itself establishes that upload order and the operator must upload in the same order; do not substitute English placeholders such as `@Image1`.

For every actual image, video, audio, clay/white-model, or edit reference supplied to the current generator invocation, preserve the parent V2 full-reference contract in both the outer `【参考素材角色表】` and the fenced first heading. Both locations use the exact legacy-compatible label `参考图角色分工：` and repeat the same complete natural-language sentence for every supplied asset. Use a human-readable label followed by its required handle; the handle never replaces the natural description.

Every reference sentence uses this complete semantic form:

```text
{参考素材标签}（@图片/视频/音频 N或当前产品实际句柄）只锁定{该素材全部有效控制项}，不复制{该素材全部拒绝项}；{仅在确有分段作用时写 N-Ns 适用时间}。
```

Do not output the backstage `首要职责 / 控制 / 不得覆盖` record, internal role codes, filename-only entries, slash-separated tags, `同外层`, or a short form such as `@图片 1只锁人物身份`. Do not merge separately supplied assets to save characters. Group them only when the user explicitly designated them as one reference set. The inner prompt is self-contained; the CineVisible compiler may translate film grammar but may not omit, summarize, or narrow any handle, reference lock list, or rejection boundary. Compress accidental repetition in other prose while preserving the same invocation.

Canonical image-reference format example; replace the facts only when the actual supplied images differ:

 ```text
参考图角色分工：
人物身份图（@图片 1）只锁定帝鸿和玲珑的脸型、发型、服装、气质，不复制棚拍背景和光感。
动作参考图（@图片 2）只锁定开场两人的抱扶动作、身体关系、低机位构图和洞窟正拍背景关系，不复制图中人物身份细节。
火焰材质参考图（@图片 3）只锁定金橙火焰材质、透明能量丝、粒子密度、流动层次和热浪感，不复制构图。
```

Active video, audio, clay/white-model, or edit references follow the same full-sentence principle and always include their actual invocation handle. Add a time span when it materially controls execution, for example: `动作参考视频（@视频 1）只锁定3-6s的低机位跟拍速度和停机节奏，不复制人物身份、服装和剧情。` and `声音参考（@音频 1）只锁定鼓点密度、环境低频和高潮进入时机，不复制原素材对白、旋律主题和人物声纹。` The fixed heading remains `参考图角色分工：` for compatibility with the parent ready-state package.

Capacity is not a recommendation to fill every slot. Use the actual supplied references needed for the requested generation. If two assets compete for identity, geometry, movement, light, style, or sound, apply an explicit user priority first; otherwise assign conservative non-overlapping roles and state the boundary instead of averaging them silently or requesting an automatically generated replacement.

## 11. Seedance 2.0 Short-Clip Profile

For a single 2.0 invocation:

- Keep duration at or below 15 seconds and within 9 image / 3 video / 3 audio references.
- Use one main event and one stable event space. Use two to three motivated dramatic beats and three to five small visible changes for a normal 10-15 second clip; scale down for shorter clips.
- Use one dominant camera support/movement policy. In a multi-shot 2.0 invocation, every shot inherits that policy; at most one shot executes the motivated move, while the remaining shots stay locked or use motivated cuts. One to four declared shots may share the same invocation when each cut is causally motivated and the complete fenced text remains at or below 5000 characters.
- Use one active effect system or the explicit no-effect branch. Simplify simultaneous effect, fight, dialogue, camera, and environment changes before prompting.
- Prefer `开场 / 随即 / 接触后 / 最后` when coarse causality is sufficient. Do not invent frame-level timing merely to look precise.
- If the first assembled prompt exceeds 5000 characters, compress it in place and recount while preserving identity, supplied dialogue, performance, action, geography, light, prop/injury/residue/audio state, all one-to-four shots, every inter-shot handoff, reference-role sentences, global capture/light masters, and every required camera-header field. Character count alone never authorizes another package. Split only for a verified hard duration limit, a verified hard reference-capacity limit, an explicit user request, or returned-video evidence of execution overload followed by user approval; any authorized next package restates its concrete opening state and never says only `承接上一段`.

The fenced prompt must begin with the reference-role heading. For text-only generation, use a truthful no-upload value instead of an operational metadata line:

```text
参考图角色分工：
无上传素材；使用文本锁定。
```

## 12. Seedance 2.5 Long-Form And Edit Profile

For a 2.5 invocation:

- Keep duration at or below 30 seconds and within 30 image / 10 video / 10 audio references.
- For a simple clip at or below 15 seconds, preserve the same compact physical, lighting, acting, and camera core used for 2.0. Do not add cuts, effects, dialogue, references, or subplots just to use 2.5 capacity.
- For 16-30 seconds, use three to five macro story beats such as `setup -> development -> turn -> payoff -> end`. Each beat states opening condition, one event/change, visible result, transition trigger when one exists, and a handoff state. These are not automatically five declared shots.
- Use explicit time ranges only when the total duration is fixed and timing materially controls the story. Every generator-visible range uses integer-second endpoints, one ASCII hyphen, and one final lowercase `s`, such as `1-3s` and `4-5s`. Never output decimal seconds, colon timecodes, `~ / ～ / – / — / 至 / 到`, or a Chinese `秒` suffix. Keep each range broad enough to perform the action; keep the chosen whole-second labeling convention consistent, and do not create missing, repeated, reset, or overlapping actions while converting the spine.
- Declare whether the invocation is `单镜到底` or `多镜头`. A one-to-four-shot sequence intended for one generation remains one ready-state package and one fenced block; four shots are never split merely because of shot count or prompt length. A longer sequence is split only for the same verified hard duration/reference-capacity conditions, an explicit user request, or returned-video evidence of execution overload followed by user approval.
- For every transition, specify trigger/bridge and the first visible state after it: foreground occlusion, action crossing, sound bridge, gaze handoff, light transition, or an explicit motivated cut.
- Use clay/white-model, green-screen, motion, camera, or edit references only when the user supplied the required source and the active UI supports the mode. State exactly which attributes they control and must not override.
- For an extension, treat the existing video as a continuity reference and restate the new segment's first visible frame, identities, geography, light, props, residue, audio, and motion state. Do not rely on `继续上一段`.
- For a targeted edit, use `source -> target time range -> preserve exactly -> change only -> post-edit continuity`. The source video and requested edit range are mandatory. Preserve every untargeted span; this profile does not override a stricter preservation-first lock.
- Continue to simplify complex contact, nonlinear cloth/hair/fluids, many simultaneous speakers, and dense multi-subject interaction while keeping causal action and continuity readable. A 2.5 label is not evidence that these risks disappeared. Split only after returned-video evidence identifies execution overload and the user approves, unless a verified hard duration/reference-capacity limit already requires it.

The fenced prompt must begin with the complete reference-role block:

```text
参考图角色分工：
人物身份图（@图片 1）只锁定人物脸型、发型、服装和气质，不复制原图背景、棚拍光感、动作和构图。
动作参考视频（@视频 1）只锁定有效时间段内的低机位运镜速度、路径和停机节奏，不复制人物身份、服装、剧情和场景材质。
```

Example of a 24-second timed spine inside `事件 / 表演节拍`:

```text
0-5s：她在暗室合上信匣，右手仍压住匣盖；远处第一声钟响触发抬眼。
5-12s：她携匣穿出门廊，摄影机从右后侧跟拍；前景柱面完全遮挡画面时转入雨院。
12-19s：柱面离开后第一帧已见她在雨院右侧，信匣仍在右手；她停在来人两步外，将匣递出但不松手。
19-24s：第二声钟响后她才松手，来人接稳信匣；镜头停在两人的手与一臂距离，作为下一段起点。
```

## 13. Ready-Prompt Surface Rules

Retain the established nine headings and write natural Chinese, not the intermediate record:

1. `参考图角色分工`: the exact heading `参考图角色分工：` followed by one complete handle-bound `只锁定……，不复制……。` natural-language sentence for every actual image/video/audio/clay/edit reference supplied to the invocation. Repeat the same full sentences from the outer role table; never use a shortened role summary or point back to the outer section. For text-only generation, write `无上传素材；使用文本锁定。`. Target model, generation mode, duration, platform ratio, active-picture composition/crop target, synchronous-audio choice, and the camera-intent disclaimer stay backstage and, when operator-facing, in `【镜头设计摘要】`, never in this fenced heading or a separate preamble.
2. `全局视觉 / 材质 / 光影母版`: the exact `FQ-EFTV-01` fixed baseline once; exactly one resolved scene-family sentence; exactly one resolved effect-state branch; then the current first visual read, motivated light, contrast, depth, exposure, integration, and material response. For `effect=none`, omit effect vocabulary instead of writing a dormant active-effect clause. Do not expose the version code or repeat the fixed baseline in shot prose.
3. `全局摄影 / 镜头母版`: per-scene shared **visible** color/grain result, axis, and support/movement policy; never repeat these values inside every shot. Camera body, fps, shutter angle, ISO, WB, and T-stop are resolved backstage and never compiled into the fence.
4. `开场可见状态与空间调度`: exact first frame, identities, count, screen side, facing, distance, props, effect baseline, geography.
5. `事件 / 表演节拍`: every declared shot first uses `镜头号｜景别｜焦距｜光源｜机位/运动｜焦点/景深`, then `表演 / 动作 / 承接` supplies the visible state chain, performance, event-light/effect response, movement trigger/path/stop, transition bridge, and timed spine when justified.
6. `动作物理与材质响应`: force/contact/weight/inertia/occlusion/deformation/material response and recovery.
7. `声音 / 对白`: speaker, supplied dialogue, mouth state, ambience/foley/music/silence and timing.
8. `连续性锁`: identity, geography, screen side, props, damage/residue, light world coordinates, exposure, audio and exact handoff state.
9. `负面限制`: no more than five short, evidenced risks; never a generic quality-word dump.

The generator-facing block must not contain source episode numbers, source paths, analysis confidence, evidence ranks, comparator character names, source drama names as style labels, capability commentary, official citations, UI help text, or unresolved alternatives. `玲珑`, `帝鸿`, and other requested project character names may remain as identity labels only when the active character router has resolved them.

## 14. Model-Facing Lint

Reject or repair the copy when any item is true:

- `TargetProfileMissing`: the backstage/outer ready-state package has no resolved target model or contains competing versions.
- `TargetBudgetOverflow`: the resolved duration or reference count exceeds the selected official profile without an explicit split/extension plan.
- `PromptCharacterOverflow`: the exact fenced text exceeds 5000 characters. Reject that draft internally, compress duplicated atmosphere, repeated global masters, workflow/meta prose, inactive physics/audio/negative channels, and verbose continuity wording in place, then recount. Preserve complete reference-role sentences, supplied dialogue, required performance/action, one-to-four-shot order, inter-shot handoffs, continuity values, the shared global capture/light facts, and every required camera-header field. Do not emit an over-limit prompt and do not split merely because of character count.
- `LegacyCameraTail`: a shot puts performance/action first and appends a full camera-parameter tail afterward, or repeats the visible color/grain result and the full light paragraph per shot. Rewrite it into the global-master/per-shot-header structure.
- `ShotHeaderOrder`: any declared shot lacks one of `镜头号→景别→焦距→光源→机位/运动→焦点/景深`, changes that order, merges fields across shots, or places performance before the header.
- `PlatformSettingMissing`: the backstage target record lacks the platform-selectable ratio, composition/crop target, synchronous-audio choice, or camera-intent classification; when an operator-facing summary is delivered, it must agree with that record.
- `AudioModeMismatch`: the backstage/UI synchronous-audio choice and outer summary conflict with requested dialogue/sound generation, explicit silence, or the fenced `声音 / 对白` field.
- `GeneratorMetadataLeak`: the fenced copy contains `生成模式与有效参考：`, a `目标模型= / 平台画幅= / 构图目标= / 同步音频=` key-value preamble, or the camera-intent disclaimer instead of beginning directly with `参考图角色分工：`.
- `AbstractOnly`: an important instruction is only `高级 / 仙气 / 震撼 / 电影感 / 有张力 / 克制` with no visible or audible proof.
- `VisualMasterMissing`: the global visual/material/light field omits or abbreviates the exact `FQ-EFTV-01` baseline, or the baseline appears more than once in the fenced block.
- `VisualFamilyUnresolved`: the global visual/material/light field contains no resolved family, contains more than one family, or leaves braces, slashes, alternatives, or family-choice instructions in generator-facing text.
- `VisualEffectBranchUnresolved`: the global visual/material/light field contains neither or both effect-state branches, or an `effect=none` prompt retains active-effect vocabulary.
- `SourceTitleStyleLeak`: `苍兰诀`, another source drama, actor, director, or protected work title appears as a generator-facing style shortcut instead of translated visible controls.
- `UnanchoredLight`: a light has no motivated source, world position, subject/surface, or material result.
- `UnanchoredVFX`: an effect lacks source, path/geometry, target/contact, response, decay, or end state.
- `NoVFXLeak`: the no-effect branch contains aura, particles, energy fog, spontaneous glow, environmental transformation, or shake.
- `DecorativeCameraMove`: a move lacks support, trigger, path, stop/end framing, or narrative proof.
- `MultiMoveOverload20`: one Seedance 2.0 invocation uses competing dominant support/movement policies, or more than one declared shot executes any non-locked camera move, even when those moves share a policy or each has a causal motivation. At most one declared shot may move; all others remain locked or enter through motivated cuts.
- `StateReset`: a beat begins from a state incompatible with the prior end state.
- `AssetRoleConflict`: two references control the same field without priority, or a handle is invented for an unattached asset.
- `ReferenceHandleMissing`: an actual supplied image/video/audio lacks its numbered `@图片 N / @视频 N / @音频 N` handle, uses an English placeholder such as `@Image1`, or its numbering disagrees with declared upload order; likewise, an active 2.5-only clay/white-model/edit reference lacks the exact handle exposed by the current product or uses an invented substitute.
- `ReferenceRoleAbbreviated`: an actual supplied reference is missing from either the outer or inner `参考图角色分工：` block, or its line lacks a complete positive lock list, complete `不复制` boundary, material time span when required, or has been shortened into a handle/tag/role code.
- `InvalidVisibleTimeRange`: a generator-visible range is not exactly integer-start + ASCII hyphen + integer-end + one lowercase `s`; it uses a decimal, colon timecode, `~ / ～ / – / — / 至 / 到`, or Chinese `秒`, exceeds the resolved duration, is zero/reversed, or causes a missing/repeated/reset action in a continuous spine. Frame-accurate evidence in the human-facing diagnosis is outside this lint, as is frozen text outside an authorized preservation-first edit span.
- `FalsePrecision`: an exact technical value is presented as measured/model-guaranteed without user, project, reference, or UI authority.
- `DenseInteractionRisk`: complex physical contact or very dense multi-subject interaction has not been simplified, assigned to truthful supplied-reference roles, or expressed as readable cause-and-effect; splitting remains limited to the authorized conditions above.
- `AnalysisLeak`: source names, pages, paths, evidence notes, rankings, citations, or workflow instructions remain in model-facing text.

## 15. Regression Examples

### A. No Effect, Abstract Terms Removed, SD2.0

Input intent: `10秒，暖木室内，两人隔桌试探；高级、克制、紧张；不运镜，不要特效。`

Required compile result: the abstract labels disappear; the prompt states north-window world light, exact left/right positions and social distance, gaze/breath/hand evidence, a fixed support, one opening and one changed end state, and no effect leakage. It stays within 15 seconds and the 2.0 reference limits.

### B. Active Effect And Contact Proof, SD2.0

Input intent: `8秒，帝鸿一掌截住左前方冲击；震撼、力量感。`

Required compile result: one pressure-wave geometry, left-front source/path, palm contact, force chain to the rear foot, snow/fabric response, one short peak camera response or locked camera, decay/residue, and a stable end pose. The two abstract labels do not survive as substitutes for those controls.

### C. Timed Narrative, SD2.5

Input intent: `24秒，玲珑从暗室携信匣穿过门廊，在雨院交给来人；需要铺垫、推进、转折、收尾。`

Required compile result: three to five broad time ranges, each with an opening state, event, result, transition trigger, and handoff; the right-hand prop state and light/geography survive every transition; any actual reference has one role and time span; no segment says only `承接上一段`.

### D. Same Short Core Across Both Versions

Input intent: `同一10秒双人对话分别输出2.0和2.5。`

Required compile result: two independent ready-state packages. Identity, story, physical action, light, camera position, no-effect state, continuity, global capture/light masters, and front-loaded shot headers are semantically identical. Only verified profile syntax or requested reference/timing differences may vary; 2.5 does not inflate the story.

### E. Targeted 2.5 Edit

Input intent: `只修改现有视频8-11秒的运镜，人物、动作、声音和其余时段保持不变。`

Required compile result: the source video is present; `8-11s` is the only generator-visible target range; the one permitted camera change is stated; every untargeted span and identity/action/audio/story fact is frozen; the post-edit framing reconnects to the unchanged next frame. Without the source video, do not claim the edit is executable.

### F. Complete Reference-Role Prose Across 2.0 And 2.5

Input intent: supplied 帝鸿/玲珑 identity image, opening embrace-support action image, and gold-orange flame-material image, with either Seedance 2.0 or 2.5 selected.

Required compile result: both the outer role table and the fenced first heading contain `参考图角色分工：` followed by the same three unabridged sentences beginning `人物身份图（@图片 1）`, `动作参考图（@图片 2）`, and `火焰材质参考图（@图片 3）`. The compiler does not replace them with `@Image1只锁人物身份`, internal role codes, or a shorter capacity-oriented summary.

### G. Platform Settings, Audio, And Camera Intent, SD2.0

Input intent: `Seedance 2.0，12秒，2.39:1构图，有环境音，无对白，三镜头。`

Required compile result: the backstage target record and `【镜头设计摘要】` state one real platform ratio such as `21:9`, a 2.39:1 safe-composition/post-crop target, synchronous audio on, and that camera metadata is creative intent rather than a platform guarantee. The fenced copy begins directly with `参考图角色分工：`, contains no operational metadata preamble, and its sound field contains only the requested environment audio. All three shots inherit one dominant support/movement policy; at most one performs the motivated move and the other shots remain locked or enter through motivated cuts.

### H. Always-On Eastern-Fantasy Television Visual Master

Input intent: `风起玲珑骨，Seedance 2.0，10秒，暖木室内双人对话，无术法，无视觉参考图。`

Required compile result: `全局视觉 / 材质 / 光影母版` contains the complete fixed quality baseline exactly once, followed by one resolved `暖木人间` sentence, only the reality-change `effect=none` branch, and the current motivated window/practical-light facts. The no-effect field contains no effect vocabulary; the backstage token `FQ-EFTV-01` and the title `苍兰诀` do not enter the fenced copy, and later shot prose does not repeat the baseline.

### I. Four-Shot Single-Invocation Budget

Input intent: `Seedance 2.0，15秒，四镜头连续动作，初稿约4200字符。`

Required compile result: one ready-state package and one fenced prompt contain all four shots in order, with one shared global capture/light master, four canonical front-loaded camera headers in the fixed field order, four complete performance/action/handoff lines, and explicit end-to-next-opening handoffs. The prompt remains valid anywhere up to 5000 characters. An over-5000 first draft is compressed in place without removing dialogue, performance, action, positions, scene transitions, reference roles, continuity, or header fields; it is never divided solely because it contains four shots or exceeded a retired lower character ceiling.
