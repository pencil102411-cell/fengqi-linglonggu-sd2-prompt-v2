# Seedance Shot Assembly

Use this reference after project truth, character state, supplied scene/character/reference roles, and the intended shot sequence are resolved. Compile directly from the supplied character setting, scene setting, plot, or written storyboard into one coherent prompt; do not run a scene-asset gate, generate a replacement image, or paste specialist manuals as separate blocks.

## Table of contents

1. Layer ownership
2. Prompt architecture
3. References and first frame
4. Blocking and optics
5. Camera, action, physics, light, and audio
6. Continuity, density, and prompt budget
7. Final delivery

## 1. Layer ownership

- The orchestrator owns shot ID, script compression, supplied-reference inventory, and the return loop.
- The acting layer owns objective, obstacle, tactic, beat, listening, eye behavior, breath, and voice behavior.
- The narrative-lighting layer in [narrative-lighting-design.md](narrative-lighting-design.md) owns story function, source motivation, world-space placement, quality, fill/negative fill, contrast, spill, separation, material response, and light continuity.
- The visual-master layer in [eastern-fantasy-tv-visual-master.md](eastern-fantasy-tv-visual-master.md) owns the always-on `FQ-EFTV-01` live-action quality baseline, exactly one resolved scene family, and exactly one resolved effect-state branch inside the existing global visual field. It never replaces the current shot's concrete narrative light, scene geography, optics, or effect chain.
- This assembly layer owns first-frame occupancy, spatial blocking, optical character, camera, action timing, physics, audio, continuity, and compression of all approved light controls into the final prompt.
- Supplied images, videos, audio, clay/white-model assets, and edit sources are optional direct references, not permission gates. Use only assets the user actually supplied to the generator invocation; describe any missing scene/view detail with positive text rather than generating or demanding a replacement asset.
- This assembly reference owns the visible 瑞宝PRO outer package. A final packaging specialist may write and validate only the generator-facing content inside `【完整可复制提示词】`; it cannot introduce an asset gate, an automatic-image detour, or another outer shell.

## 2. Prompt architecture

Use this planning order:

```text
shot function -> reference roles -> global visual/material/light master
-> global camera/shot master -> first visible state and blocking
-> acting/action state chain -> physics -> sound
-> continuity locks -> targeted negatives
```

Required model-facing content order inside the fenced copy block:

```text
REFERENCE ROLES
GLOBAL VISUAL / MATERIAL / LIGHT MASTER
GLOBAL CAMERA / SHOT MASTER
OPENING VISIBLE STATE AND SPATIAL BLOCKING
EVENT / PERFORMANCE BEATS
PHYSICS AND MATERIAL RESPONSE
AUDIO / DIALOGUE
CONTINUITY LOCKS
NEGATIVE CONSTRAINTS
```

The six visible outer sections in `Final delivery` are fixed and must stay in that order. Keep all nine inner headings in the fenced copy block and keep their order; when a channel is legitimately absent, write a concise truthful `无` or `不适用` instead of deleting it. Prose values may be compressed to suit the target interface, but do not add competing outer sections.

The exact resolved text inside each fenced `【完整可复制提示词】` block has a hard ceiling of 5000 characters, including a non-patch preservation-first local repair that returns a complete generator prompt. Count Chinese and non-Chinese characters, punctuation, spaces, and line breaks; exclude the outer package and code fences. Do not pad a complete short prompt, and do not use an overflow tolerance above 5000. The budget applies per independent generator invocation. A one-to-four-shot sequence intended for one Seedance generation remains one invocation, one ready-state package, and one fenced block. A patch-only replacement span is not a complete generator prompt and remains governed by the exact local-repair span contract.

Build `GLOBAL VISUAL / MATERIAL / LIGHT MASTER` as one continuous field in this exact layer order: the literal `FQ-EFTV-01` baseline once, one resolved `本段视觉家族` sentence, one resolved `effect=active/none` branch, then the current shot's motivated source, world-space placement, dark-side relation, spill/separation, exposure, atmosphere, and material response. In a no-effect prompt, use only the reality-change branch and omit effect vocabulary. Do not add a tenth heading, repeat the fixed baseline per shot, expose its version code, or substitute `苍兰诀风格 / 高级电影感` for the visible controls.

`GLOBAL CAMERA / SHOT MASTER` records the shared **visible** baseline for each named scene segment: the color/grain result, the axis, and the dominant support/movement policy. The capture values that produced that look — camera body, frame rate, shutter angle, ISO, white balance, T-stop — are resolved at full fidelity in the backstage target record and summarized in `【镜头设计摘要】` when the operator needs them; they never appear inside the fence, because Seedance exposes no control interface for them and they only consume the character budget. Write what the frame looks like, not what the camera was set to. Treat numbered shots, titled shots, an unnumbered single shot, inserts, transitions, reactions, and spatial re-establishments as declared shots. Begin each such shot with the canonical header `镜头号 → 景别 → 焦距 → 光源 → 机位/运动 → 焦点/景深`, then write `表演 / 动作 / 承接`; before delivery, verify `declared shot count = canonical shot-header count`. Do not repeat the shared capture baseline per shot or append the retired full camera tail.

## 3. References and first frame

List every actual image, video, audio, clay/white-model, or edit reference supplied to the current generator invocation. Do not list unseen assets or task-level files that are not being supplied to that invocation, but never omit a supplied asset merely because another asset has the same role. For each reference, state:

- primary role;
- what it controls;
- priority when roles overlap;
- what it must not override;
- visible traits to preserve.

Bind every actual reference to its invocation handle. For JiMeng/Seedance ready-state packages, use `@图片 1`, `@图片 2`, `@视频 1`, and `@音频 1`, numbered from one in declared upload order for each modality. For a 2.5-only clay/white-model or edit mode, use the exact handle exposed by the active product. When the package is prepared before UI upload, the declared order becomes the required upload order. Never bind a handle to an absent asset and never replace the Chinese product syntax with English placeholders such as `@Image1`.

Every listed asset must be an actual supplied generator reference. Never invent a handle, claim that an absent image was generated or inspected, or turn a textual scene description into a fictitious upload. Count the selected Seedance profile's actual image/video/audio references before assembly. When the hard platform reference capacity is exceeded, use only a user-approved minimum sufficient set, or split only for that verified hard capacity reason; never drop a source silently or change model versions silently.

In both the outer `【参考素材角色表】` and the fenced first heading, use the exact legacy-compatible label `参考图角色分工：` and then write one complete Chinese natural-language sentence per supplied reference. Use the form `{参考素材标签}（@图片/视频/音频 N或当前产品实际句柄）只锁定{完整正向控制项}，不复制{完整拒绝项}。`; add a material time span for video/audio/edit references and overlap priority as another complete clause when needed. Any generator-visible span uses only integer endpoints in `N-Ns` form, such as `1-3s` and `4-5s`. Use human-readable labels such as `人物身份图`, `动作参考图`, `火焰材质参考图`, `动作参考视频`, and `声音参考`. Do not expose only internal role codes, use filename-only entries, collapse lines into slash-separated tags, write `同外层`, or merge separate assets merely to reduce length. Group references only when the user explicitly designated them as one set.

Canonical format example; replace the facts when the current assets differ:

 ```text
参考图角色分工：
人物身份图（@图片 1）只锁定帝鸿和玲珑的脸型、发型、服装、气质，不复制棚拍背景和光感。
动作参考图（@图片 2）只锁定开场两人的抱扶动作、身体关系、低机位构图和洞窟正拍背景关系，不复制图中人物身份细节。
火焰材质参考图（@图片 3）只锁定金橙火焰材质、透明能量丝、粒子密度、流动层次和热浪感，不复制构图。
```

Repeat the same complete handle-bound sentences in the outer and inner locations. This duplication is deliberate: the outer table supports review, while the fenced copy must remain self-contained for the generator. Reference-role prose is a required control and cannot be shortened for the prompt budget; compress accidental repetition in other fields while keeping the same invocation intact.

Embed the first visible state in the opening event:

```text
开场：第一帧已经包含[required subjects]，位于[positions]，处于[current physical and emotional state]；空间关系立即可读。
```

Avoid empty establishing frames unless requested. A geography reference may inform the location without dictating the final camera view.

## 4. Blocking and optics

### Blocking

For each important subject, define only what matters:

- screen-left / screen-right / center;
- foreground / midground / background;
- distance from partner or landmark;
- body facing direction and separate gaze target;
- movement path and destination;
- prop hand, contact surface, and long-axis direction;
- camera side and axis.

Use measurable physical anchors such as `within one meter`, `hand on the door handle`, `back against the wall`, or `boots inside the marked zone` when precision matters.

### Optics

Use full-frame-equivalent focal bands as shorthand, then describe observable results:

- `18–24mm`: strong spatial expansion, near foreground large, environment dominant;
- `28–35mm`: wide environmental action, camera near subject, readable geography;
- `40–50mm`: grounded normal perspective, balanced subject and environment;
- `65–85mm`: portrait compression, camera farther away, controlled background separation;
- `100mm+`: distant observation, strong compression, narrow field, foreground occlusion when motivated.

For this project, the V1 camera protocol overrides those generic bands: 65mm is allowed only for an explicit full-shot body-geography or relationship setup; every medium shot or tighter—including medium, medium close-up, close-up, extreme close-up, and insert—uses 85mm or longer with shallow/very shallow/extremely shallow depth of field, one clear focus plane, and only partial defocused background fill. Never widen the requested target shot merely to fit a supplied panorama; bind that panorama only to the environment/palette/material dimensions it can truthfully support and use text to specify the requested close view.

Do not rely on a focal number alone. State physical camera distance, subject occupancy, visible set surfaces, background compression/expansion, depth behavior, and what remains readable.

Do not mix incompatible content classes inside one beat. If the sequence needs environmental geography, facial close-up, and macro prop detail, use causally motivated cuts across one to four declared shots inside the same invocation. Create separate generated clips only for a verified hard duration/reference-capacity limit, an explicit user request, or returned-video evidence of execution overload followed by user approval.

## 5. Camera, action, physics, light, and audio

### Camera

Describe camera behavior physically:

- starting position and height;
- tracking owner;
- path—push, pull, side-track, arc, rise, descend, whip, recoil, handoff, or deliberate lock-off;
- motivation—what action, occlusion, gaze, contact, scale, or revelation causes the move;
- information proved by the move.

Use one dominant move per short beat. For a Seedance 2.0 multi-shot invocation, resolve one dominant support/movement policy for the whole block; at most one shot executes the motivated move, while the remaining shots stay locked or enter through motivated cuts. Avoid decorative orbiting, random roll, floating drone motion, or compound moves that obscure acting.

### Action and acting integration

Every beat should have:

```text
function -> visible state -> character tactic/behavior -> camera response
-> physical consequence -> changed end state
```

For every character-bearing shot labeled `中近景`, `近景`, `特写`, `大特写`, `过肩中近景`, or `过肩近景`, place the exact clause `角色毛孔真实细腻，双眼保持清晰眼神光` once inside that shot's own `表演 / 动作 / 承接` prose after its camera header. In an over-the-shoulder shot, this clause governs the in-focus face, not the defocused foreground shoulder. A global master, continuity lock, negative list, or camera header does not satisfy the rule. Do not inject it into a prop/body-part insert with no readable face; an explicit user/script requirement for closed or occluded eyes remains higher priority.

Do not write invisible psychology without behavior. Do not let camera energy replace contact, listening, or reaction.

#### Performance budget floor

**主体动作 = 动作 + 表演，表演层不是可选项。** The most common failure in this schema is spending the whole budget on the camera header and the light master, leaving the subject with one sentence such as `她神情复杂地看着他`. The model cannot execute that; those characters are wasted.

- **In every shot, the `表演 / 动作 / 承接` prose must occupy at least half of that shot's characters.** The camera header and its optics take roughly a third; environment and light changes take the rest. A shot whose performance line is shorter than its camera header is rejected and rewritten before delivery.
- **Abstract labels must resolve to physiology.** `神情复杂`, `眼神一冷`, `情绪崩溃`, `若有所思` are not acceptable output. Convert each into visible changes on eyelids, lashes, gaze landing point, masseter, throat/swallow, nostril, breath, fingertips, or weight shift. Draw the exact vocabulary from [microexpression-acting-grammar.md](microexpression-acting-grammar.md) and [body-action-and-contact-grammar.md](body-action-and-contact-grammar.md).
- **Emotion is written as a dynamic, not a state.** Each shot needs at least one visible expression change plus the trigger that causes it: `从什么状态 → 被什么触发 → 变成什么状态`. A single static emotion word never satisfies this.
- **Detail must match the framing.** A `特写` or `近景` that omits microexpression wastes the shot; a `远景` or `大全景` must not describe microexpression that cannot be resolved at that size.

This floor is a proportion requirement, not a licence to pad. Under the 5000-character ceiling, compress the camera and light prose first and keep the performance layer intact.

### Physics

When relevant, lock gravity, mass, support, inertia, friction, contact, weight transfer, follow-through, braking, cloth/hair delay, liquid behavior, particles, weapon load, and environmental response. Effects must originate from visible action and cannot substitute for body/object response.

### Light

Read [narrative-lighting-design.md](narrative-lighting-design.md) and resolve the light in this order:

```text
story function and color reinforcement/counterpoint
-> motivated visible/implied source -> world-space side and height
-> camera-to-key relation and face shadow side
-> apparent-size result, hotspot/coverage, softness, wrap, shadow edge, and falloff
-> one fill or negative-fill strategy with one exact dark-side difference
-> protected eye/skin/hand/prop information and only the relevant spill boundaries
-> one separation/practical/effect layer -> atmosphere and material response
-> exposure hierarchy and allowed loss -> cross-shot continuity
```

Use one dominant key. Do not use an equipment label, `cinematic lighting`, `soft light`, `book light`, or `negative fill` as a complete instruction. State the observable result. Preserve the supplied scene reference's visible source direction, cast shadows, practical state, and material response when those fields are assigned to that reference, unless the user's story or written storyboard explicitly establishes a new visible state.

Use [camera-parameter-presets.md](camera-parameter-presets.md) as the sole normative two-layer camera schema. Put the complete same-scene lighting system—story function and motivated source, apparent size, world-space placement, camera-to-key relation, visible quality/coverage/falloff, exact fill or negative-fill difference, protected information channel, relevant spill boundaries, separator/practical position and relative brightness, exposure hierarchy, material response, and catchlight state—once in the global visual/material/light master. Every shot header keeps `光源`: write `本场景母版，无变化` when unchanged or only the necessary relationship/state delta when changed, without restating shared source/direction. The following performance/action prose describes event-light response; the continuity lock preserves source coordinates and exposure invariants.

### Timing

Use exact macro ranges only when supported by reference footage, an animatic, dialogue/music synchronization, or a credible action budget. Inside the fenced generator text, every explicit range must use integer-second endpoints, one ASCII hyphen, and one final lowercase `s`, such as `1-3s` and `4-5s`; do not use decimals, colon timecodes, `~ / ～ / – / — / 至 / 到`, or a Chinese `秒` suffix. Otherwise use causal order or qualitative pacing rather than fabricating a range. Scale performance beats to duration. Sub-second acting knowledge is translated into `半拍 / 一拍 / 短暂停顿` and never copied as a decimal duration.

#### Dialogue time value

A shot carrying dialogue must have a duration the spoken line can actually fit. Estimate it before locking the shot duration or the macro range:

| 语速 | 换算 | 示例 |
|---|---|---|
| 慢速 | 1 秒 2 字（每字 0.5s） | `你在怕什么`（5 字）≈ 2.5 秒 |
| 中速 | 1 秒 3 字（每字 ≈0.33s） | `你到底想怎么样`（7 字）≈ 2.5 秒 |
| 快速 | 1 秒 4 字（每字 0.25s） | `让开别挡我的路`（7 字）≈ 1.8 秒 |

- **标点不计入字数。**
- Consecutive lines: total the characters, convert, then add 0.3-0.5s between sentences.
- Emotional pauses: add 1-2s of reaction time before a burst or after a release.
- Keep one 语速 per scene unless a character-motivated change is written into the performance line.
- A silent shot (pure action, reaction, or empty frame) is estimated from narrative need, normally 2-5s.

If the supplied dialogue cannot fit the requested clip duration, say so and either shorten the covered dialogue or split at a real beat boundary; never compress the line count silently or speed the delivery past the character's canonical rhythm.

### Audio and dialogue

- Resolve the platform audio switch backstage before writing this field. `同步音频=开启` is required when the requested result needs generated dialogue, ambience, foley, music, or another synchronized track; `同步音频=关闭` is required for an explicitly silent result. Keep the backstage/UI choice and the outer `【镜头设计摘要】` consistent with `声音 / 对白`, but do not copy the switch as an operational key-value line into the fenced prompt.
- Speak only the supplied dialogue unless improvisation is requested.
- **Supplied dialogue must be audibly spoken, with lip movement strictly matched to the line.** Excluding background music and on-screen subtitles never means the character stays silent — those are separate channels. Lip-sync accuracy is a hard requirement for short-form drama; write the spoken line explicitly in the performance prose as `{角色}说："{台词原文}"`.
- Keep non-speaking lips still.
- When delivery speed matters (急促 / 拖长 / 气声 / 压着嗓子), add one short clause after the line; otherwise write nothing about speed.
- Define voice behavior from the acting layer without changing vocal identity.
- State ambience, foley, sound focus, music, or deliberate silence when relevant.
- Do not add subtitles, captions, narration, or offscreen voices unless requested.

## 6. Continuity, density, and prompt budget

Across cuts, preserve:

- active character list and identity;
- location geography and camera axis;
- left/right and gaze relation;
- outfit, wounds, dirt, sweat, water, blood, smoke, and weather;
- prop state, hand state, and object orientation;
- world-space source position, key and shadow side, exact dark-side difference, negative-fill zone, practical state, visible color balance, haze, exposure priority, and material response;
- physical and emotional progression.

Do not restart action after a cut or teleport subjects.

Keep high detail for reference roles, first frame, blocking, interaction, performance trigger, optics, camera proof, physics, light, dialogue, and continuity. Keep generic beauty adjectives and non-active background detail short.

For close shots, do not repeat full-room geography in prose. Bind a supplied close-scene reference when one exists; otherwise retain only the visible landmark, material, light, and background evidence needed for continuity as direct text.

### 5000-character in-place compression protocol

Keep the nine headings, one-to-four-shot sequence, and all required controls. If the first assembled fenced block exceeds 5000 characters, compress it in place and recount the exact final text; do not create additional prompt packages merely to satisfy the character budget.

- Do not impose any lower sub-budget on shared prose or a fixed quota on any heading. Allocate space dynamically according to the current sequence; a four-shot prompt well above the retired lower ceiling remains valid when the final count is at or below 5000 characters.
- Keep each canonical per-shot camera header compact while preserving the fixed order `镜头号→景别→焦距→光源→机位/运动→焦点/景深` and every required value. Prefer compact noun phrases and visible results; never delete a header field or move a shot into another package merely because four headers take more space.
- Preserve the complete per-reference handle-bound sentences under the fenced first heading `参考图角色分工：` even though the outer role table repeats them. Remove only reference-role wording duplicated in other inner fields; never replace this dedicated block with short labels or a pointer to the outer table.
- Put shared visual, material, light, support, and visible color facts once in the global masters. Preserve the complete `FQ-EFTV-01` baseline, one resolved family, and one resolved effect-state branch in the visual master, and remove only their repetitions elsewhere. In each shot header, write the mandatory shot-defining values and only true deltas; in the following prose, write visible action, active performance change, blocking/contact, and handoff. Do not repeat camera body, fps, shutter, ISO, WB, color/grain, or the expanded same-scene light paragraph per shot.
- Write event beats as causal state chains—`起始状态→触发→动作/反应→结束状态`—rather than restating atmosphere or psychology. Keep only physics and sound channels that visibly operate in this clip.
- Reduce continuity to exact invariants and keep no more than five short, shot-specific negative constraints. Do not use the negative list to retell the desired image or prior failure history.
- One fenced block may hold one, two, three, or four declared shots when they belong to one intended generation. Four declared shots are not an overflow condition. Preserve their exact order, each shot's opening/ending state, and every inter-shot handoff inside the same block.

Compress in this order: remove duplicated atmosphere/quality adjectives; merge repeated global visual, material, light, support, and visible color facts into their one master; remove workflow explanation and backstage metadata; convert non-locked explanatory prose into short visible state chains; retain only physics, sound, and negative channels that actually operate; reduce continuity wording to exact invariants. Never compress away the exact `FQ-EFTV-01` baseline, its one resolved family, its one resolved effect-state branch, identity, complete reference handles/boundaries, supplied dialogue, required performance, causal actions, blocking/axis/contact, the first readable spatial state, each shot's end state, inter-shot handoff, exact continuity values, the required close-framing detail clause, any canonical camera-header field, or its following performance/action/handoff prose. Rebuild and recount until the ordinary complete prompt is at or below 5000 characters. Character count alone never authorizes splitting. Splitting is permitted only for a verified hard model-duration limit, a verified hard reference-capacity limit, an explicit user request, or returned-video evidence of execution overload followed by user approval. In preservation-first local repair, frozen text still cannot be globally compressed or split: if a non-patch complete baseline itself exceeds 5000 and the allowed span cannot lawfully reduce it, stop with `完整基线超过5000字；请授权扩大压缩范围或改为只返回替换段`.

## 7. Final delivery

Deliver the final Seedance block directly from the confirmed character setting, scene setting, plot, written storyboard, and any actually supplied references. Do not wait for a scene-asset status and do not generate a missing image first.

Visible package:

````text
 【镜头与素材状态】直接编译（文本生成 / 按已提供素材参考生成）
 【参考素材角色表】
参考图角色分工：
[每个实际参考素材各用一句带规范句柄的完整“只锁定……，不复制……”说明]
【镜头设计摘要】[目标模型、模式、时长、平台画幅、构图/裁切目标、同步音频状态、摄影参数仅作创作意图的说明，以及镜头设计摘要；这些操作信息不得复制进下方围栏]
【完整可复制提示词】
```text
参考图角色分工：
[逐素材重复外层带规范句柄的完整自然语言说明，不得缩写或省略]
全局视觉 / 材质 / 光影母版：[FQ-EFTV-01 固定质量基线逐字一次；一个已解析的本段视觉家族句；一个已解析的 effect=active/none 分支；按场景段集中写 story function, motivated source, apparent size, world-space placement, camera-to-key relation, quality/coverage/falloff, exact fill or negative-fill difference, spill/separation, atmosphere, exposure, material and catchlight continuity]
全局摄影 / 镜头母版：[按场景段集中写可见的 color/grain result, axis, dominant support/movement policy；不写 camera body / fps / shutter / ISO / WB / T-stop]
开场可见状态与空间调度：[first-frame occupancy, blocking, axis, gaze, props, and contact]
事件 / 表演节拍：
[如需时间段，只在对应节拍或镜头前写整数范围，例如1-3s、4-5s；无需精确时间时只写因果顺序]
镜头N｜景别：[shot size/occupancy]｜焦距：[exact focal+lens family+compact distance/space result]｜光源：[unchanged=`本场景母版，无变化`; changed=only the real shot delta]｜机位/运动：[camera relation+support/single move]｜焦点/景深：[depth class+focus plane+visible falloff; no T-stop]
表演 / 动作 / 承接：[opening state→trigger→performance/action/dialogue/response→end state/next-shot handoff；qualifying close-framing shots contain `角色毛孔真实细腻，双眼保持清晰眼神光` here]
动作物理与材质响应：[support, contact, inertia, cloth/hair, props, particles, and environment]
声音 / 对白：[supplied dialogue or explicit silence, ambience, and foley]
连续性锁：[identity, wardrobe, wounds, positions, axis, prop hand, source world position, key/shadow side, exact dark-side stops, negative-fill/spill zones, practical position/relative brightness, catchlight state when eyes are visible, WB, haze, material response, actor start/end light zones, and end state]
负面限制：[short, shot-specific constraints]
```
【生成前质检】
【下一轮只建议调】one variable
````

Keep the heading `【镜头与素材状态】` unchanged. Its truthful value is `直接编译（文本生成）` or `直接编译（按已提供素材参考生成）`; never imply that an absent asset was supplied, generated, or inspected.

Targeted negative constraints may cover identity drift, extra subjects, outfit/prop morphing, wrong layout, frozen eyes, camera chaos, weightless motion, flat light, subtitles, flicker, broken anatomy, or text artifacts. Do not name old unrelated failures.

**A negative constraint yields to the shot's intended effect.** A negative exists to stop the model from breaking down, not to stop the scene from happening. When a candidate negative contradicts a technique this shot actually requires, **delete that negative outright and note the deletion outside the fence** — do not write both.

**不要两条都写。** Two equally weighted contradictory instructions do not meet in the middle: either the effect is flattened or the frame falls apart. The test is one question — *is this constraint preventing model breakdown, or preventing the effect this shot is supposed to have?* Delete every instance of the latter.

Common yields in this project:

| Candidate negative | Yields to | Handling |
|---|---|---|
| 背景环境稳定不闪烁 | 空间异变、环境崩解、明暗剧变、破界 | Delete; the collapsing environment is the shot |
| 不扭曲 / 肢体比例自然 | 变身、兽化、鳞甲、人体解构（限幻觉/法术） | Delete these two clauses, keep `不换脸` |
| 动作流畅连贯无卡顿无瞬移 | 时间冻结段、身外化身、瞬移连招 | Delete for the frozen segment; a trajectory-visualized teleport usually needs no deletion |
| 画面左右关系保持一致 | 环绕运镜、群攻包围、长距离追逐、一镜到底 | Delete that clause only |
| 摄像机运动平滑无抖动 | 手持、环绕、FPV、变速 | Never write it in the first place |

Never add a per-shot lock line that forbids blocking, head count, prop identity, or elements that simply should not appear. Solve those in the positive description inside `开场可见状态与空间调度` and `事件 / 表演节拍`: stating what is in frame beats listing what is not.

Final check:

- direct compilation used the supplied character setting, scene setting, plot, or written storyboard without a scene-asset gate or automatic image-generation detour;
- every listed reference is an actual supplied generator input assigned to the declared upload order; no prompt draft, inferred image, or absent file has a handle;
- target-profile reference capacity was counted from the actual supplied inputs, with no silent reference deletion or model upgrade;
- current-shot context only;
- every actual image, video, audio, clay/white-model, or edit reference supplied to the invocation appears under `参考图角色分工：` in both outer and inner locations as the same complete handle-bound `只锁定……，不复制……。` sentence, with correct `@图片 N / @视频 N / @音频 N` upload-order numbering for those three modalities or the exact active-product handle for a 2.5-only special modality, and no invented placeholder, shorthand, merging, or omission;
- all nine inner headings retained in the required order, with truthful `无/不适用` values where needed;
- the global visual/material/light field contains the exact `FQ-EFTV-01` baseline once and only once, exactly one resolved scene family, exactly one resolved effect-state branch, and current-shot light/material facts; a no-effect branch contains no effect vocabulary, and the field contains neither the backstage version code nor a source drama title used as a style shortcut;
- exact fenced prompt measured at no more than 5000 characters; any over-limit draft was compressed in place and remeasured without dropping dialogue, performance, action, shot order, inter-shot handoffs, continuity, reference roles, global capture/light masters, or camera-header fields, and without character-count-driven splitting;
- every explicit generator-visible time range uses only `N-Ns` with integer endpoints, an ASCII hyphen, and one final `s`; decimal seconds, colon timecodes, alternative range separators, and Chinese `秒` suffixes are absent, while frame-accurate diagnosis timecodes stay outside the fenced copy and frozen local-repair text stays verbatim;
- first frame and spatial relation immediately readable;
- focal band, written scene facts, and each supplied scene reference's explicitly limited role are mutually consistent;
- acting visible at the chosen framing;
- every qualifying character-bearing close-framing shot contains `角色毛孔真实细腻，双眼保持清晰眼神光` exactly once in its own performance/action/handoff prose after the camera header, with over-the-shoulder focus assigned to the in-focus face;
- lighting has one story function and motivated dominant source, exact world-space placement and dark-side difference, visible quality/falloff, controlled spill, one separator, coherent material response, and continuity across reverses;
- physics, light, audio, and continuity agree;
- target version, mode, duration, platform ratio, composition/crop target, and synchronous-audio switch are resolved backstage and, when shown, explicit and consistent in `【镜头设计摘要】`; camera metadata is labeled there as creative intent rather than a platform guarantee; the fenced copy begins with `参考图角色分工：` and contains no `生成模式与有效参考` operational-metadata line or equivalent key-value preamble;
- a Seedance 2.0 multi-shot block has one dominant support/movement policy, with at most one motivated moving shot;
- every declared shot begins with one canonical exact-value camera header in the fixed order and then complete performance/action/handoff prose, shot count equals shot-header count, no shared capture/light baseline is duplicated per shot, and every one-to-four-shot invocation remains one package and one fenced block;
- prompt contains no internal QA notes or workflow instructions.
