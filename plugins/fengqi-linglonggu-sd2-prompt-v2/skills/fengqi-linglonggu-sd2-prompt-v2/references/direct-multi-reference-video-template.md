# Direct Multi-Reference Content Adapter For 瑞宝PRO Seedance Delivery

Use this reference when the user gives any one source or combination of sources—character settings, character reference images, scene/environment settings or images, plot content, or a written storyboard—and asks for a finished Seedance / Jimeng SD2 prompt directly. Do not require every source category to be present; map actual references to bounded roles and express the remaining visible requirements in text. Supply project-specific content controls only; let `seedance-assembly.md` own the visible 瑞宝PRO output package.

## Table of contents

1. Output goal
2. Required 瑞宝PRO delivery shape
3. Legacy-to-瑞宝 content mapping
4. Reference roles and character integration
5. Legacy content bank
6. Camera defaults and final checks

## Output Goal

Generate the self-contained model-facing content for a multi-reference video prompt. Preserve the user's character, scene, and plot facts, then translate them into visible controls: reference roles, action, facial performance, environmental relighting, camera focus, material realism, and camera metadata. Do not emit a separate legacy direct-template shell.

The default output is one complete prompt for the requested continuous clip. Keep all requested shots—including four or more declared shots—inside that one prompt whenever they belong to the same video and fit the selected model's real duration and reference-capacity limits. Never split solely because of shot count, character count, shot-header count, or the former prompt budget. Split only when the user explicitly requests separate clips, the selected model's hard duration/reference capacity requires it, or the material is explicitly several independent videos.

Before filling this adapter, define camera and narrative-lighting requirements, map every supplied reference to a precise control/rejection boundary, and resolve every known character through `character-performance-bible.md`. A character image locks appearance; the canonical role profile locks stable performance; the current plot, era, relationship, and injury state select the active variation. A scene reference controls only the environment, palette, material, light, geography, or viewpoint it actually provides; any required new angle, framing, interaction surface, blocking, or light state is stated directly in text and does not stop prompt delivery. An image caption such as `钟离玲珑` must not silently replace the current-line `玲珑` performance layer when the user's plot names current-line 玲珑. Conversely, a past-life scene must not inherit modern 玲珑's quick wit merely because the face matches.

## Required 瑞宝PRO Delivery Shape

Use the sole normative outer package and nine-field inner order in [seedance-assembly.md](seedance-assembly.md) directly after the current text facts and reference roles are resolved. Do not reproduce, shorten, or reorder that package here. Keep `负面限制` inside its fenced copy block, retain every inner heading with truthful `无/不适用` values when needed, and do not add the Jimeng workbench's parallel outer headings. Keep the exact fenced generator text at or below 5000 characters. If it exceeds 5000, compress it in place by removing analytical labels and repeated descriptions, merging shared visual/light/capture facts, and shortening sentence structure while preserving every requested shot, identity, supplied dialogue, action order, transition/handoff, continuity lock, complete reference-role sentence, the shared global masters, and every required camera-header field. Do not split merely to satisfy the character ceiling.

For every reference-bound delivery, preserve the complete per-reference role prose twice: once in the outer `【参考素材角色表】` and once under the fenced first heading `参考图角色分工：`. Both locations must use that exact legacy-compatible label followed by one full handle-bound natural-language `只锁定……，不复制……。` sentence for every actual image, video, audio, clay/white-model, or edit reference supplied to that generator invocation. Use `@图片 N / @视频 N / @音频 N` in declared upload order for those three modalities; for a 2.5-only special modality, preserve the exact handle exposed by the active product. When a reference needs a generator-visible active span, write it only as integer endpoints in `N-Ns` form, such as `1-3s` or `4-5s`. The inner prompt is self-contained and may not refer to the outer table. It begins directly with `参考图角色分工：` and does not carry an operational metadata preamble.

## Legacy-To-Ruibao Content Mapping

Preserve every legacy direct-template control, but relocate it:

- character identity/era -> `开场可见状态与空间调度` plus `连续性锁`; reference assignments -> the full `参考图角色分工：` prose repeated as the fenced first heading and in the outer `参考素材角色表`; media restrictions -> `声音 / 对白` and `负面限制` as applicable;
- visual core, art direction, skin light, garment light, narrative function, motivated source, apparent size, camera-to-key relation, key/fill or negative-fill state, relevant spill boundaries, practical/background hierarchy, exposure priority, spatial layers, and material realism -> `全局视觉 / 材质 / 光影母版`;
- shared camera metadata -> `全局摄影 / 镜头母版`; shot-defining optics/light/camera/focus values -> the front-loaded per-shot header before performance;
- plot/action chain -> `开场可见状态与空间调度` plus `事件 / 表演节拍`;
- contact, weight, cloth/hair, prop, liquid, particle, and environment response -> `动作物理与材质响应`;
- dialogue, silence, ambience, foley, and media restrictions -> `声音 / 对白`;
- identity/outfit/position/prop locks plus source world position, key/shadow side, exact dark-side stops, negative-fill/spill zones, practical position/brightness, catchlight state, WB, haze, material response, and actor light zones -> `连续性锁`;
- failure prevention -> the in-block `负面限制`.

## Reference Role Rules

- Character reference images lock only identity-relevant features: face shape, facial-feature ratio, temperament, age impression, hairstyle, hair ornament, costume shape/color, body proportion, and signature props.
- Character reference images must not donate source-image background, studio lighting, flat front fill, beauty-filter skin, portrait exposure, product-shot cleanliness, modern photo texture, or unwanted color cast.
- Scene reference images lock only environment: architecture, terrain, material, weather, color palette, light direction, atmosphere, spatial layers, foreground obstruction, and background depth.
- Scene reference images must not override character identity, face, costume, makeup, body proportion, or performance.
- If a reference image contains an undesirable element, name the rejection explicitly in the reference-role line.

Write the visible reference-role block in this complete prose form:

 ```text
参考图角色分工：
人物身份图（@图片 1）只锁定帝鸿和玲珑的脸型、发型、服装、气质，不复制棚拍背景和光感。
动作参考图（@图片 2）只锁定开场两人的抱扶动作、身体关系、低机位构图和洞窟正拍背景关系，不复制图中人物身份细节。
火焰材质参考图（@图片 3）只锁定金橙火焰材质、透明能量丝、粒子密度、流动层次和热浪感，不复制构图。
```

This is a format example, not a fixed asset inventory. Replace the labels, handles, characters, lock lists, and rejection boundaries with the actual current references and text facts. Keep one sentence per separately supplied reference; combine assets only when the user explicitly treats them as one reference set. Do not shorten the block to internal codes such as `identity/outfit`, filename-only labels, slash-separated tag lists, or fragments such as `身份图锁脸服饰`. Do not omit a repeated-role reference: describe its distinct controls and rejection boundary. Treat these sentences as required prompt content under the 5000-character budget; if the complete prompt is over budget, compress other prose in place without splitting the continuous shot sequence or shortening these sentences.

## Character Integration Rules

- The character must look physically present in the scene, not pasted over it.
- Recolor skin, makeup, hair, costume, embroidery, jewelry, and metal accessories with the actual scene light: low sunset, cold fog, stone bounce, snow bounce, paper-window light, wood shadow, lantern amber, water reflection, or other user-specified sources.
- Mention at least three integration mechanisms when relevant: shared shadow direction, environmental bounce on the dark side of the face, rim light on hair/fabric edge, color contamination on white fabric, haze between subject and background, foreground occlusion crossing the frame, or contact shadow near feet/hands/railing.

## Legacy Linglong Sunset Watchtower Content Bank

Use the detailed prose below only as an extraction bank when the user gives Linglong, a mountain watchtower / valley pavilion scene, and a sunset mood. Select only facts active in the current shot; do not copy whole paragraphs that repeat the global masters or continuity lock. Remap the selected information through the table above. Never reproduce its legacy section headings as the final output format; extract shared capture/light values once, then rebuild every declared shot through the sole normative front-loaded header in `camera-parameter-presets.md`.

```text
用多参考图生成视频，不含背景音乐，不含台词字幕，不含现代物件，不含录屏质感。

人物设定：
玲珑（当前线现代灵魂；人物图中的钟离玲珑只作脸与服装参考）：机灵、快反应、会用轻松神态掩饰紧张，眼神先扫后定，手会立即找一个实际动作承接情绪；少女感轻盈但不幼稚，不使用钟离玲珑的长期压抑、自毁式节奏。

参考图角色分工：
人物身份图（@图片 1）只锁定钟离玲珑的脸型、五官比例、少女感、发型、发饰、白色衣裙、身形比例和灵动气质，不复制图片里的灰色棚拍背景、正面柔光、亮白皮肤、证件照式曝光、白裙纯白高亮和干净棚拍质感。

剧情动作：
根据用户提供的剧情内容改写为 10-15s 内可见的动作链：玲珑刚刚听见或察觉身后动静，正在木栏旁微微停步，指尖轻触袖口或栏杆，衣袖被山风轻轻带起；她即将回眸，眼神先动，头部再缓慢转回三分之二侧脸，表情灵动、聪明、带一点克制的少女好奇，不说话，不出现字幕。动作重点放在眼神变化、回眸节奏、发丝和耳饰轻晃、袖口边缘受光、皮肤被夕阳擦亮的瞬间。

画面核心：
人物必须真实进入背景环境中，皮肤、妆容、发丝、白色衣料、刺绣、发饰和金属小配件都被低位橙金夕阳、山谷冷雾、青灰石墙反射、深木栏杆阴影和灯笼琥珀光重新染色，不能像抠图贴上去。镜头重点看玲珑的脸、眼神、回眸表情、发丝、耳饰、衣领、袖口和夕阳下的皮肤质感；背景山水和楼阁只作为虚化层次，不要展示过多大环境。

美术风格：
真人写实女频古装长剧质感，古东方山间望楼与山谷楼阁群，真实外景置景感，画面温暖、柔美、通透、克制，有傍晚落日仙气。场景包含青灰石墙、深木屋檐、木栏杆、观景楼、远处楼阁、山体、瀑布、水面、松树、紫灰山雾和橙金晚霞。近景可以有虚化屋檐、木柱、栏杆、松枝或灯笼形成遮挡，增强实拍层次。色彩以低饱和橙金夕阳、暖杏肤色、青灰紫棕暗面、深木色、青灰石墙、冷灰蓝远山、紫灰山雾为主。不要整屏金黄滤镜，暖色只落在人物亮面、发丝边缘、白纱边缘、栏杆高光和远处晚霞。

角色皮肤光影：
人物脸部不是纯逆光剪影，低位夕阳从画面左后偏侧前约45度方向斜扫过来。脸部形成明确明暗分区：暗面占脸部约60%-70%，亮面只占30%-40%。靠夕阳一侧的额头、鼻梁边缘、颧骨、上唇、下颌线、耳廓和指尖出现小面积暖杏金亮面，皮肤有真实皮下散射感，像光轻轻透过皮肤，带一点自然血色，不是白色硬高光。背光暗面保持柔和青灰紫棕、暖灰棕层次，不能糊成一整块黑影；眼窝、鼻翼、唇形、下颌和脸颊轮廓都要可读。脸部整体仍偏暗、克制、含蓄，不要把脸打成全亮；只让关键骨点和薄皮肤区域出现温润透光。眼睛有很小的自然眼神光，来自低位天空反射和石墙、栏杆、白衣反射；不要环形灯，不要现代棚拍补光。

服装光影：
服装款式和颜色保持 @图片 1 参考，但整体被山间夕阳环境重新染色。白色衣裙不能纯白发光，受光边缘偏淡金，暗部偏青灰、烟灰紫和暖灰棕。绸缎、轻纱、刺绣、腰封、发饰和金属配件要有古装剧精致感；纱衣边缘在逆光中微微透亮，金属饰品只出现小面积暖金高光。衣袖靠近脸部时，可以给下颌和脸颊暗面一点柔白反射，让皮肤更通透。衣料褶皱、刺绣和纱层不能糊成一片。

打光：
整场只有一个主光源：远处低位橙金夕阳。主光不是纯背后勾边，而是从人物后侧偏侧前方向柔扫人物半边脸，形成三层效果：第一层是发丝、肩线、白纱边缘的暖金轮廓光；第二层是脸部靠光侧的小面积透亮亮面；第三层是山谷薄雾里的低饱和橙金空气光晕。夕阳经过山谷水汽、薄云和屋檐边缘削弱后变得柔和，不是刺眼硬晒。太阳附近可以高亮，但人物脸和白衣必须保留细节。人物回眸时，脸部保持三分之二侧脸朝向夕阳，让夕阳擦过半边脸，不能完全背对太阳导致脸部只剩阴影。

辅光：
暗面由青灰石墙、木栏杆、白色衣袖、山谷冷雾和天空漫反射轻轻托起，辅光低于夕阳主光约1.5到2档。辅光只负责保留脸部暗面结构，不负责把整张脸打亮；暗面要柔、厚、有层次，但仍然比亮面面积更大。灯笼或远处暖光只能给耳坠、发饰、手指和衣褶暗面一点点琥珀反射，不能制造第二个明显主光。

空间与材质：
青灰石墙和石阶有真实粗糙度、边缘磨损、潮气和细小阴影；深木屋檐、栏杆和楼阁受光处有克制暖反光，暗部吸光但能看见木纹。远处瀑布、水面和山雾作为冷灰蓝空气层次，随距离降低对比并自然虚化。灯笼是小范围纸质琥珀光，只点亮局部木构，不能把整场染成橙色。整体像真实搭建在山谷楼阁中的古装剧外景，不要纯CG仙侠地图，不要游戏副本感，不要塑料材质，不要过度锐化。

全局摄影 / 镜头母版：望楼夕照场景为低饱和橙金亮面、青灰紫棕暗面、细腻真实颗粒；同一望楼轴线不越轴；滑轨极轻微慢推为唯一运动政策。
镜头1｜景别：近景，玲珑面部与上身占画七成｜焦距：100mm长焦定焦；远机位，背景拉近，前后景压缩｜光源：沿用望楼左后偏侧前45度低位橙金夕阳主光，无变化｜机位/运动：眼平三分之四侧面，滑轨极轻微慢推｜焦点/景深：浅景深，双眼、鼻梁、唇形、耳饰、衣领和近袖清晰，远山楼阁柔化成局部色块
表演 / 动作 / 承接：角色毛孔真实细腻，双眼保持清晰眼神光；玲珑先以眼神扫向身后，再缓慢回眸成三分之二侧脸，指尖仍触袖口；发丝、耳饰和袖缘随山风晚半拍轻晃，镜末目光准确停在声源方向。

负面限制：
不要身份漂移，不要服装变形，不要多余人物，不要背景音乐，不要台词字幕，不要现代物件，不要录屏质感，不要棚拍证件照感，不要抠图贴片感，不要纯CG仙侠地图，不要游戏副本感，不要塑料材质，不要过度锐化，不要整屏金黄滤镜，不要环形灯，不要现代美颜补光，不要把脸打成全亮，不要白裙纯白发光。
```

## Default Camera Choices

- Single-character emotional prompt: the fenced form is `100mm 长焦定焦；摄影机远离主体，背景相对放大并靠近主体，压缩前景与背景之间的空间｜滑轨极轻微慢推｜浅景深，双眼与近袖清晰，远景柔化｜低饱和暖高光与青灰阴影`; the matching `ARRI ALEXA Mini LF｜T2.8｜24fps｜172.8°｜ISO 800｜白平衡 5000K` creative-intent baseline stays backstage. Only when the user explicitly requests an inspected source match, switch to a `25fps cadence intent + BT.709 output target`; exact delivery requires a confirmed product setting or post-conform.
- Two-person medium dialogue: use 85mm+ and matched reverses unless a full-body relationship setup is explicitly needed.
- Detail insert or big close-up: use 100mm or 135mm with very shallow or extremely shallow depth of field.
- Background should be partial defocused fill for `中景` and tighter shots.
- Every focal-length entry must include the corresponding camera-distance and perspective phrase from the main skill: wide lenses use the close-camera / near-large-far-small expansion rule; 85mm+ lenses use the distant-camera / enlarged-background / spatial-compression rule.

## Final Checks

- Does the visible answer use exactly the 瑞宝PRO ready-state outer order: `镜头与素材状态 → 参考素材角色表 → 镜头设计摘要 → 完整可复制提示词 → 生成前质检 → 下一轮只建议调`?
- Are all nine inner headings retained in their required order, with truthful `无/不适用` values when a channel is absent?
- Is there exactly one self-contained fenced prompt block per requested continuous generator invocation, with all of that invocation's declared shots and `负面限制` inside it rather than one block per shot?
- Does every declared shot—including a numbered or titled shot, unnumbered single shot, insert, transition, reaction, or re-establishing shot—begin with `镜头号→景别→焦距→光源→机位/运动→焦点/景深`, followed by complete `表演 / 动作 / 承接`, with `shot count = shot-header count` and no old full camera tail appended?
- Were all legacy content controls remapped into the 瑞宝PRO inner order rather than emitted as competing outer headings?
- Did the prompt keep media restrictions: no background music, no dialogue subtitles, no modern objects, no screen-recording texture?
- Do both the outer `【参考素材角色表】` and fenced first heading contain the exact label `参考图角色分工：`, followed by one complete handle-bound `只锁定……，不复制……。` sentence for every actual supplied reference, with correct `@图片 N / @视频 N / @音频 N` upload-order numbering or the exact active-product handle for a 2.5-only special modality, and no shorthand, invented placeholder, merged assets, or omitted lock/rejection item?
- Does every explicit time span inside the fenced copy use integer endpoints in `N-Ns` form with one ASCII hyphen and one final `s`, with no decimal seconds, colon timecodes, alternative separators, or Chinese `秒` suffix?
- Do the backstage target record and `【镜头设计摘要】` state the real platform ratio, composition/crop target, synchronous-audio choice, and that camera metadata is creative intent rather than a hard platform parameter, while the fenced copy begins directly with `参考图角色分工：` and omits those operational key-value fields?
- Does the character integrate into the scene through environmental relighting, shared color, shadows, haze, and foreground layers?
- Does the action describe visible body/eye/hand/cloth movement rather than abstract emotion?
- Do the two global masters hold one exact visible color/grain result, shared light/material system, axis, and support policy, while each shot header holds one exact shot size, focal, light-master status/real delta, camera relation/movement, depth class, focus plane, and visible falloff without duplicating the global baseline? Is the fence free of camera body, frame rate, shutter angle, ISO, white balance, and T-stop?
- Does the focal-length field include lens family, camera-to-subject distance, and the visible perspective/space result rather than only `24mm` or `100mm`?
- Does the global light master state story function and motivated source, apparent size, world-space placement, camera-to-key relation, quality/coverage/falloff, exact dark-side difference, relevant spill boundaries, separator/practical position and relative brightness, exposure hierarchy, material response, and catchlight state when eyes are visible, while each shot's `光源` field says `本场景母版，无变化` when unchanged or only the real per-shot delta when changed?
