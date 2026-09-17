# 风起玲珑骨 项目视觉与表演缺省语法

> **纯内容层，不是输出格式。** 本文件收纳项目级的视觉基调、双人调度、构图分层，以及**未命名角色**
> 的男女主表演回退语法。它不定义工作流、不定义交付模板、不定义镜头头部格式。
>
> **加载条件**：编译任何一条完整提示词时读取本文件。
>
> **所有权边界**
>
> | 归本文件 | 归别处 |
> |---|---|
> | 项目默认色温对照、框中框与前景遮挡、三层构图、道具插入的情绪铰链 | 具名角色的表演 → [character-performance-bible.md](character-performance-bible.md)，**优先级高于本文件的男女主回退语法** |
> | 双人对话的空间轴线与站位权力关系 | 微表情预设与泪态 → [microexpression-acting-grammar.md](microexpression-acting-grammar.md) |
> | 未命名角色的男女主表演回退 | 动作动力链与接触 → [body-action-and-contact-grammar.md](body-action-and-contact-grammar.md) |
> | 灯光设计的落笔顺序与母版句式 | 灯光的完整七道设计法 → [narrative-lighting-design.md](narrative-lighting-design.md) |
> | | 景别、焦距、机位、景深、镜头头部 → [camera-parameter-presets.md](camera-parameter-presets.md) |
> | | 九标题、字数预算、负面限制 → [seedance-assembly.md](seedance-assembly.md) |
>
> **本文件的男女主语法只是回退。** 任何一个具名的《风起玲珑骨》角色出现时，
> 人物表演圣经的档案覆盖本文件；不得把 帝鸿、崔珏/燕十三、司徒陌、庚辰、小奎
> 压成同一套"男主节奏"。

---

## Core Visual System

Use the following as project defaults only where the user, script, or approved scene asset does not establish a different physical condition. Confirmed scene light, geography, weather, and material response outrank a decorative cold-snow/warm-wood fallback.

- Use a 2.39:1 period-drama active-picture composition by default; when matching the inspected source texture, use a 2.40:1 / 1920x800 delivery target. Treat this as composition/delivery intent, not proof that the current Seedance product exposes those exact canvas ratios. When the active entry offers only a nearby platform ratio such as `21:9`, select that real value, preserve a 2.39:1 or 2.40:1 safe composition inside it, and state the required post-crop. Favor wide horizontal compositions, layered depth, architecture-driven blocking, and patient spatial reads.
- Build the main contrast as **cold snow exterior vs warm wood interior**.
- Exterior snow: cool white bounce from the ground, blue-gray shadows, warm low sun or rim light, visible snow particles, trees/fences/rooflines as depth layers.
- Interior: paper-window cool backlight plus lantern/candle/firelight warm foreground, dark wood background, soft haze, shallow depth of field, practical lights visible in frame.
- Use frame-within-frame and foreground obstruction: doors, window lattice, bed curtains, pillars, railings, fences, branches, lantern cages, hanging cloth, or blurred heads.
- Avoid a flat portrait-video feel. Characters should feel held by space, architecture, objects, and social distance.

## Female Lead Acting Grammar

Use this only as a fallback when no named profile applies. A named `风起玲珑骨` character always overrides it.

- Make her alert and fast-reading: eyes scan first, head turns second, hands act third.
- In public or light-comic scenes, use quick head turns, forward body lean, brisk hand movement, and slightly open facial expression.
- In danger or injury scenes, lower the body toward the ground; hands brace, search, or touch evidence before the face fully reacts.
- In concern scenes, use smaller performance: eyes lift before the head, lips part or tighten, breath pauses, then a practical action follows.
- Put emotion into hands and objects: bowl, spoon, cloth, written board, small token, medicine, lantern, snow, or sleeve.

Prompt pattern:

```text
女主表演：先用眼神读取局势，短暂停顿后低头处理手中的物件，再抬眼回应；情绪不靠夸张表情，而由眼神、呼吸、手部动作和身体前倾逐步推进。
```

## Male Lead Acting Grammar

Use this only as a fallback when no named profile applies. Do not flatten 帝鸿, 崔珏/燕十三, 司徒陌, 庚辰, 小奎, or another named role into one generic male-lead rhythm.

- Make him restrained, wounded, low-volume, and slow-reacting.
- Use stillness as status and injury: lowered torso, folded posture, leaning near a window, slow grip, controlled breath.
- Let the face be partially shadowed or side-lit. Use downward gaze, delayed eye lift, minimal mouth movement, and shoulder/neck tension.
- When he becomes decisive, keep the move small but deliberate: slow sit-up, one hand tightening, a measured turn, or a short response.
- Do not make him expressive through big gestures unless the user explicitly asks for melodrama.

Prompt pattern:

```text
男主表演：保留受伤后的低重心与克制感，脸部半侧逆光，目光先下压再缓慢抬起；他不大幅度动作，只通过呼吸停顿、手指轻握、肩颈紧张和短促回应释放情绪。
```

## Two-Person Dialogue Grammar

- Anchor the scene around a bed, table, threshold, window, or doorway.
- Use standing vs sitting vs kneeling to express power: standing applies pressure, sitting holds ground, bed-bound or lowered posture shows vulnerability, kneeling/crouching suggests care or secrecy.
- Start with a medium or wide shot to confirm geography; then use over-shoulder singles, close reactions, hand/prop inserts, and a return to medium shot.
- Keep a blurred shoulder, doorframe, curtain, or lattice in the foreground to preserve relationship pressure.
- Insert a practical hand action between emotional beats so the scene does not become flat shot-reverse-shot.

Prompt pattern:

```text
调度规则：以床榻、桌面、窗户或门槛作为固定空间轴线，先用中景确认人物距离，再用过肩近景压缩关系，中间插入手部或道具特写作为情绪转折，最后回到中景确认新的站位和结局状态。
```

## Narrative Lighting Grammar

Read [references/narrative-lighting-design.md](references/narrative-lighting-design.md) while defining every target shot before direct compilation. Design in this order: `story function + color reinforcement/counterpoint -> motivated source -> world-space placement -> camera-to-key relation -> apparent size + quality/coverage/falloff -> fill or negative fill with one exact dark-side difference -> only relevant spill boundaries -> one separator/practical layer with position/relative brightness -> exposure hierarchy + material/catchlight response -> continuity`.

Preserve all V1 scene families: cold high-key snow with blue-gray shadow and a motivated warm side/back edge; paper-window cool daylight with warm practical accents and dark-wood absorption; localized amber night practicals with blue-black falloff; male half-shadow close-ups; female softer-fill/catchlight close-ups; and warm backlit shadow-play silhouettes. Treat gender presets as fallbacks below story, character state, injury, authority, and user facts.

Translate equipment into visible results. Do not stop at `电影感打光`, `柔光`, `book light`, `反光板`, or `负补光`. State source, side, height, shadow edge, wrap, falloff, exact contrast, controlled dark zone, protected information channel, and material response. Use one dominant key and do not add an unmotivated rim or second sun.

```text
灯光母版：本段以{叙事功能}为主导；{可见或可推断光源}固定在{世界坐标方位与高度}，从人物{受光侧}形成{软硬、包裹、阴影边缘与衰减}；{辅光或负补光策略}使暗面精确低主光{单一档位}并保留{眼睛/皮肤/手/道具}；{具体分离或实景光}建立不均等的前中后景亮度，皮肤、服装、金属、木材、雪雾共同接受同一环境染色。
```

## Composition And Blocking Grammar

- Use three layers by default: foreground obstruction, midground characters, background window/light/architecture.
- Use diagonal movement in snow village scenes; let fences, trees, roofs, and paths guide screen direction.
- In interiors, keep the bed/window/table as a fixed axis and let characters circulate around it.
- Use prop inserts as emotional hinges: medicine bowl, spoon, written board, hand, cloth, token, lantern, weapon, or small keepsake.
- Use wide re-establishing shots after close-ups when AI continuity or spatial clarity matters.
- Use close-ups and inserts to hide minor position drift in generated clips.
- Let crowds become layered background texture unless one person has a clear story function.

Prompt pattern:

```text
构图：2.39:1 超宽画幅，前景有虚化门框、窗棂、床帐或柱子形成框中框，中景保留人物关系，背景有纸窗冷光和暗木结构；镜头从中景锁定站位，切到过肩近景和手部道具特写，再回到中景确认新的关系状态。
```

