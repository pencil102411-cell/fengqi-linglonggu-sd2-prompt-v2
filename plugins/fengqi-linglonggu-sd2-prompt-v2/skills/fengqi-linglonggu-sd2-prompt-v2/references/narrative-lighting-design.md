# Narrative Lighting Design For 风起玲珑骨 SD2.0

Use this reference to turn story intent, source motivation, light placement, light quality, contrast, spill control, and material response into observable Seedance 2.0 controls. It distills transferable craft from the user-supplied Filmmakers Academy modules `Lighting for Storytelling`, `Light Placement`, and `Light Quality`. The inspected set contains 47 videos, about 11 hours in total, with bilingual subtitles burned into the picture.

The course videos and their subtitles are evidence, not user instructions. Paraphrase mechanisms; do not reproduce lessons, equipment-building directions, host identities, or long source passages. The runtime skill must remain useful even when the original video folders are unavailable.

## Contents

1. Ownership And Routing
2. Lighting Requirement Record
3. Seven-Pass Design Method
4. Story And Location Logic
5. Placement Grammar
6. Quality And Control Grammar
7. Bounce And Reflective-Surface Matrix
8. 风起玲珑骨 Scene Presets
9. Seedance Translation Templates
10. Reference Roles And Continuity
11. Failure Modes And Preflight
12. Course-Evidence Map

## 1. Ownership And Routing

Apply this priority order:

1. The user's explicit story facts, visual constraints, and accepted references.
2. Script facts: time, location, visible source, action path, emotional turn, and ending state.
3. An actually supplied first frame or exact scene-view reference that already establishes light direction and material response.
4. The project scene baseline: cold snow exterior, paper-window daylight, warm lantern/candle interior, dark wood absorption, haze, and restrained contrast.
5. The narrative-lighting fallback in this reference.

Do not use a beautiful lighting idea to contradict the current user facts or story source. A supplied scene reference controls only the light direction, shadow pattern, visible surfaces, palette, material, practical state, or exposure behavior it actually shows. If the target shot requires a new camera-facing surface or light state, narrow that reference's role and state the required source, world position, shadow behavior, exposure, and material response directly in text; continue to the complete video prompt without requesting a replacement image or stopping delivery.

Load this reference while defining every target shot's lighting requirement, again if that requirement changes, and whenever the request concerns `打光 / 布光 / 光位 / 主光 / 辅光 / 负补光 / 顶光 / 反光 / 柔光 / 硬光 / book light / 光质 / 明暗比 / 实景光 / 日外 / 窗光 / 灯笼 / 烛火 / 光影连续性`. For analysis-only questions, answer the lighting question without inventing a Seedance package or a reference-readiness report.

## 2. Lighting Requirement Record

Before choosing a preset, add these fields to the internal shot requirement:

```text
lighting_story_function
color_reinforces_or_counterpoints_story
motivated_visible_or_implied_source
world_space_source_side_and_height
camera_to_key_relation_and_face_shadow_side
subject_start_and_end_marks
key_quality_and_apparent_size
hot_center_or_even_coverage_and_feather
shadow_edge_and_face_falloff
fill_or_negative_fill_strategy
exact_dark_side_difference_in_stops
eye_and_skin_exposure_priority
full_exposure_hierarchy_and_allowed_loss
catchlight_position_and_story_state
one_to_three_relevant_spill_boundaries_or_none
separation_or_effect_source
background_light_layers
atmosphere_and_beam_visibility
material_and_color_response
practical_position_and_brightness
continuity_dependencies
```

Choose one dominant lighting idea per shot. A second source may separate, motivate, or mark a story change; it must not become an accidental second key.

## 3. Seven-Pass Design Method

### Pass 1: Story Function

State what the light makes legible: safety, intimacy, secrecy, threat, isolation, authority, injury, revelation, transition, or temporal change. Describe a visible result, not a mood adjective alone.

Color does not have to translate emotion literally. A tragic beat may sit inside warm, living light to create counter-tension; a cold palette is not an automatic synonym for sadness. State whether color reinforces or deliberately opposes the story state.

Examples:

- `权力压迫：上方暖光只形成一小块可行动区域，人物跨出灯池后眼窝迅速沉入阴影。`
- `迟疑亲近：纸窗侧光保留双眼与手部，暗面不完全填平，让靠近动作比表情先泄露。`

### Pass 2: Motivation

Name one visible or implied source: sun, bright sky, snow bounce, paper window, doorway, lantern, candle, fire, moonlit opening, or reflected water. Every key, rim, shaft, or warm patch must trace back to that source family.

Do not add an unmotivated rim merely to make the frame look cinematic. If a source is off-screen, its direction and color must still agree with visible windows, doors, flames, and cast shadows.

### Pass 3: Placement

Lock the key in world space: subject-left or subject-right, front/side/back, high/eye-level/low, and the surface or opening it comes through. Use the set axis rather than vague `left/right` when reverse angles are involved.

Examples:

- `纸窗位于床榻东侧，冷光从人物右后上方进入。`
- `灯笼固定在桌面南端，暖光从人物左前下方抬起指节与下颌。`

### Pass 4: Quality

Resolve all of these as visible properties:

- apparent source size relative to the face or body;
- hard, semi-hard, soft, or very soft transition;
- directional versus wrapping behavior;
- shadow-edge width and nose/cheek shadow definition;
- near-to-far falloff and whether the source isolates a mark or covers a movement zone;
- specular response on skin, silk, embroidery, metal, snow, wet stone, and dark wood.

Soft light is not automatically flat. Preserve a source side, a readable dark side, and controlled spill.

### Pass 5: Contrast And Subtraction

Choose either fill or negative fill as the primary dark-side strategy:

- `1 stop below key`: bright, open, comic, gentle, or explicitly hopeful.
- `1.5 stops below key`: the readable project default for restrained faces.
- `2 stops below key`: secrecy, conflicted intimacy, or contained anger.
- `2.5 stops below key`: a dramatic starting point with shaped but readable eyes and skin.
- `3.5 stops below key`: an emotional moonlit or deeply isolated state; protect only the information the beat needs.
- `4-5 stops below key`: thriller, horror, silhouette, or graphic concealment only; do not use for dialogue information unless hiding the face is the point.

These are selection bands. Resolve the final shot to one exact value; never leave a range in the generator-facing block.

Negative fill means removing ambient return from a named side or zone. Describe the visible darkening and edge control, not grip equipment. Fill is not a second key; it opens selected information without erasing source direction.

### Pass 6: Separation And Layers

Choose one concrete separator: window edge, lantern rim, fire flicker, snow backlight, haze-visible shaft, wet-floor reflection, or a brighter/darker background patch. Then build unequal background layers rather than illuminating every surface equally.

Recommended layer logic:

```text
foreground obstruction or darkness
-> subject key and controlled dark side
-> one practical or architectural brightness cue
-> background falloff or atmospheric separation
```

### Pass 7: Exposure, Material, And Continuity

Name the exposure hierarchy: eyes and skin, window/exterior detail, snow texture, flame core, white costume embroidery, dark-fabric folds, or a required landmark. State what may clip or fall near black and why; purposeful overexposure may hide irrelevant modern detail but must never erase story geography. Describe how the source recolors face, fabric, jewelry, hair, props, and nearby surfaces. Lock source side, contrast, practical position, white balance, haze, and material response across adjacent shots.

Higher ISO or brighter global exposure can reveal darkness but cannot create direction, edge separation, hotspots, or layered depth. Never use exposure gain as a substitute for lighting structure.

## 4. Story And Location Logic

### Find A Location That Lights The Scene

Prefer architecture that already supplies an intelligible source and shadow side: doorway, paper window, eave, corridor opening, courtyard, tree line, snow bank, or fire-lit alcove. Block the actors where the source naturally creates depth rather than lighting them independently of the set.

For generated scenes, describe the self-lighting geometry:

```text
门洞形成唯一冷色开口，人物停在门内半步，脸部靠近开口的一侧可读，背后的暗木走廊逐层衰减。
```

### Day Exterior

Fix sun direction before camera direction. Backlight or side-backlight usually preserves face control and gives hair, breath, snow, haze, or dust a readable edge. Use sky, snow, pale ground, or a controlled reflected source to open the eyes; use dark architecture, trees, costume, or an explicit negative-fill side to stop ambient light from flattening the face. In an open exterior, 2 to 2.5 stops below key is a naturalistic dark-side starting band; resolve one exact value for the shot.

Do not write generic `natural daylight`. State sun altitude and side, sky softness, ground return, face contrast, and background depth. Prioritize emotion-bearing close-ups while the sun is low and the eyes are readable; if the sun rises into a skull-eye angle, change schedule, blocking, or controlled coverage instead of accepting black eye sockets. When matching artificial sunlight to real sun, match direction, color family, hardness, shadow direction, and falloff so the frame reads as one sun rather than two.

### Interior And Practicals

Let paper windows, doors, lanterns, candles, braziers, and fire motivate the lighting. A visible practical may justify warmth and position, but its apparent brightness must agree with the light it seems to produce. Extend its effect only within a believable zone; keep distant wood, corners, and ceiling darker.

Use haze only when it reveals direction, separation, or depth. Lock haze density and drift direction across shots. Uniform haze plus uncontrolled soft light creates a flat gray wash.

For near-darkness without a visible key, use only a very weak high rear or top-rear ambient source to reveal forehead, shoulder, movement volume, and one distant depth layer after visual adaptation. Do not lift the whole room, create a heroic rim, or leave a readable head floating against absolute black.

### Actor Movement Through Light

For a moving subject, define lighting marks rather than asking one perfect portrait light to follow invisibly:

```text
起点处于纸窗冷侧光，向桌边迈两步后进入灯笼暖光，停下时冷暖交界落在双眼与握碗的手之间；背景光位不移动。
```

The lighting transition may express a beat change, but it must follow the actor's route and the fixed sources.

## 5. Placement Grammar

### Key Light

Choose the key side by story, blocking, and the supplied identity reference. Do not mechanically assign every actor the same flattering side. A broad side key can remain soft while preserving direction. A near-frontal key makes information easy but can flatten shape; reserve it for deliberate openness, vulnerability, comedy, fashion-like presentation, or a character-specific reason. A far-side key across the face often strengthens depth and relationship tension, provided the eyes remain readable.

Derive `key direction -> camera side -> face shadow side -> background separation` as one system. Over-shoulder coverage normally observes from the subject's dark side (`downside key`) to retain modeling. Break that relationship only for a named power, identity, or subjectivity change, then state the new state and continuity boundary.

Place the source high enough to feel natural for sun/window/top light but not so high that both eyes die unless concealment is the intent. A low lantern or fire source may lift the lower face, but keep the effect localized and motivated.

### Fill Light

Fill controls what the audience is allowed to read. Treat catchlight, eye socket, jaw, costume folds, and hand detail as separate information priorities. Open only the needed channel. Removing or lowering fill can turn reassurance into uncertainty without changing the key. If the fill or eye reflection changes during a shot, tie it to an actor mark or story trigger so it never flickers randomly.

When only an eye reflection is needed, specify one small, stable catchlight on the key-consistent side; do not raise the whole dark side or create multiple drifting reflections.

### Negative Fill

Use negative fill when broad sky, snow, pale walls, haze, or a large soft source washes out the dark side. A broad soft source normally also needs visible top/side/bottom spill boundaries. Name the side and result:

```text
人物远离纸窗的一侧以负补光压暗至低主光2档，保留颧骨下方与下颌边缘，不把暗面压成无细节黑块。
```

### Top Light

Top light creates a pool, separates standing figures from dark space, and can support authority, danger, ritual, or a morally enclosed world. Define the pool boundary and protect the story channel: one eye reflection, cheek plane, hands, weapon, or table surface. Avoid dead black eye sockets by adding only the smallest motivated return the shot needs.

### Flags And Spill Control

Translate flags, toppers, side cutters, bottom cutters, skirts, and black solids into visible limits:

- keep soft key off the background;
- prevent bounce from hitting the top of the head or doorway;
- preserve a black strip beside the face;
- keep the lantern pool on the table and hands;
- stop haze or pale walls from filling every shadow.

For a low skip-bounce, write the whole believable path: `hard sun or artificial source -> stone/earth/wood/water surface -> face or costume`. State the reflected direction, softness, landing zone, and direct-light cut. Do not let the original hard beam also hit the face or lens.

Do not put stand, clamp, flag, or rig instructions in the final Seedance prompt unless the user is requesting a real production diagram.

## 6. Quality And Control Grammar

### Apparent Size

A larger apparent source produces a broader transition and more wrap; a smaller apparent source produces a narrower edge and more defined shadows. State the facial result. `柔光` alone is incomplete.

### Distance And Falloff

A source close to the subject creates faster near-to-far falloff and can isolate one actor or mark. A distant source covers a wider movement zone more evenly. In a two-person shot, decide whether equal exposure or selective emphasis serves the beat.

Also state whether the source has a hot center, even coverage, or a feathered edge. Light an actor's playable zone rather than one dead point; define the gradual change as the actor enters or leaves it.

### Book-Light Behavior

The transferable result of bounce followed by diffusion is a broad, wrapping source with softened facial shadows. Treat it as a causal chain: the original light strikes the bounce at an oblique angle; the bounce becomes the source; after sufficient separation, the diffusion becomes the final visible source. The whole diffusion surface must illuminate evenly. A bright patch behind a large cloth is still a small effective source and will produce hard spots or uneven falloff.

Greater bounce-to-diffusion separation and heavier diffusion can soften more, but they reduce output and increase spill. Choose the bounce response for color, direction, and efficiency; choose diffusion density for edge softness; then restore contrast with controlled spill and negative fill. Do not demand the original exposure after a heavy diffusion step unless a credible compensating source change is stated. In a model prompt, prefer the result:

```text
大面积定向包裹柔光从纸窗侧进入，鼻影边缘宽而柔，脸部从亮侧平滑衰减到暗侧；溢光被限制在人物和床榻，暗木背景保持低照度。
```

Mention `book light` only as a secondary craft label, never as a substitute for the full light path, evenly filled final surface, visible quality, direction, falloff, output loss, and spill.

### Hard And Semi-Hard Light

Hard light gives a defined shadow edge, focused intensity, crisp shafts, and stronger texture or specular response. Use it for sun, revelation, threat, fire edge, or a graphic transition. Control facial hot spots and do not combine hard nose shadows with a contradictory shadowless beauty instruction.

### Source Shape

Round versus square bounce chiefly matters when the source shape is motivated or visible in catchlight, reflection, or shadow behavior. A square source can support window motivation; a round source can support sun, moon, lantern, or a neutral face reflection. Do not claim that shape alone changes softness when apparent size and distance stay the same.

### Practical And Background Brightness

Assign every visible lamp, candle, fire, window, or distant source one job: motivation, rim/separation, background bokeh, or color contrast. Keep edge-of-frame lamps and architecture below the subject's visual priority unless the story intentionally transfers attention. The visible practical brightness must be credible for the exposure it appears to motivate.

Night does not require saturated blue. Choose neutral gray, slightly cool gray, or an explicitly stylized blue. Set the white balance backstage to achieve it, but lock it in the prompt by naming the visible colour of the shadows and highlights, not a Kelvin value. The project default rejects electric-blue moonlight unless the user requests that stylization.

## 7. Bounce And Reflective-Surface Matrix

Use the following as response families, not mandatory equipment names:

| Surface family | Visible response | Best use | Main risk |
|---|---|---|---|
| Beadboard | soft return with useful output and a rounded catchlight; added diffusion progressively softens the nose shadow | directional portrait softness, eye/face return | heavy diffusion can erase facial modeling, dull the catchlight, and lose substantial output |
| Bleached muslin | very matte, neutral, extremely soft, almost no kick angle | intimate faces, quiet vulnerability, low-sheen skin | direct transmission may expose a lamp hotspot; low output |
| UltraBounce white | broad, matte, very soft, and stable over a large zone | moving actors, wind-exposed exterior fill | too large/close plus no subtraction produces flat ambient light |
| White showcard / foam | coveable, localizable, slightly harder when the apparent area is small | doorway, hidden bounce, hand or face zone | hard edge, broken source shape, or background spill if undersized/unshaped |
| White Griffolyn | shinier and more directional than matte white, with a stronger kick angle | greater throw with a white-family response | wind-driven exposure fluctuation and unwanted sheen |
| Soft silver / dull silver | higher output, more direction, slightly crisper and often cooler than matte white | strong backlit exterior, dawn/twilight sky return, longer throw | brow/forehead sheen, bright patch, obvious artificial kick |
| Silver lamé | powerful, focused, textured silver return; diffusion can retain shape with high efficiency | directional book-light backing or special moving-water texture | wind-driven pulsing, mottled sparkle, hard eye reflection |
| Hard silver / mirror-like silver | narrow, intense, hard, specular reflection | extreme backlight fill, sun skip, metal edge, book-light backing | squinting, hard nose shadow, vertical hot bands, double-image reflections |
| Soft gold / warm matte | warm, soft, and localizable | lantern, gaslight, candle or warm practical extension | orange skin and costume contamination if it spreads globally |
| Hard gold | focused, intense, very warm specular reflection | controlled fire/sunset accent or high-efficiency diffused backing | metallic copper faces, sharp nose shadow, clipped highlights |
| Silver-gold checker lamé | restrained warm return compared with pure gold, with pearly direction after light diffusion | warm foliage/sun ambience entering a window | grid-like sparkle, unstable glints, or over-orange substitution |
| Unbleached muslin | matte, diffuse, naturally brown-warm response | candle, gaslight, old warm practicals | muddy brown skin and lost color separation if oversized |
| Butcher-paper family | very matte red-yellow-brown warm return | strongly localized flame/gas/practical matching | cheap global yellow filter look and collapsed skin dimension |
| True black solid / UltraBounce black | absorbs ground, wall, and camera-side ambient return without adding color | negative fill and stable face shape | dead-black cheek, blocked actor path, or theatrical contrast when overused |
| Black Griffolyn | limited subtraction but retains some reflectivity | temporary soft-environment subtraction | hard light can bounce from it and create a strange secondary mark |
| Diffusion cloth | makes its evenly filled surface the final source; denser grades widen edges and reduce output | book light, close-up softening, sun-edge control | a narrow grid or uneven fill shrinks the effective source and makes it unexpectedly hard |

Select the response needed by the story, then write the visible behavior. Do not inventory multiple surfaces in one prompt. A final shot should normally resolve to one key-quality family and one fill/subtraction strategy. Treat any measured Kelvin or stop change from the course as a setup-specific observation, never a universal material constant; lock the intended relative warmth and visible skin/material result instead.

## 8. 风起玲珑骨 Scene Presets

These extend rather than replace the project's original six lighting presets. User/script facts always override them.

### Snow Exterior Day

Cold high-key environment, sun fixed behind or to the side-back of the actors, blue-gray shadow, snow as broad cool return, one controlled warm rim when motivated, and negative fill from dark costume/tree/building side when face shape is lost. Protect snow texture from clipping; use breath or drifting snow only when it serves depth or weather.

### Early-Morning Exterior

Low sun remains at side-back through trees, eaves, or thin mist; a high, large matte return lightly opens the eyes without casting a moving camera shadow; stable thin haze reveals only a few beams and gives black levels a gradual slope. Do not replace the missed morning window with white overhead noon light or erase required landmarks through blanket overexposure.

### Paper-Window Interior Day

Large directional soft source through the paper window, readable source side, gentle wrap with a 1.5- or 2-stop dark side chosen by the beat, dark wood absorbing spill, one warm practical or object highlight, and slight haze only where it reveals the window direction.

### Lantern Or Candle Interior Night

Warm practical pool on face, hands, prop, or table; blue-black or neutral-dark background falloff; localized low-source behavior; one cooler doorway/window edge only if the geography supports it. Keep flame cores controlled and prevent the whole room from sharing the same amber exposure.

### Near-Dark Interior Or Night Forest

Use an extremely weak high rear/top-rear environment source to retain forehead, shoulder, and movement volume, plus one low-brightness distant layer or haze-revealed shaft. Keep the front at low exposure and let the audience adapt. Reject global ISO-like lift, low-angle moonlight, repeated shadows, floating heads, and changing haze density.

### Restrained Male Close-Up

Preserve the V1 half-shadow and eye-line control: far-side or side-back key, one readable eye, jaw and shoulder tension, low mouth emphasis, shallow focus, and a concrete background/practical separator. Story state outranks gender; do not force this look onto an openly vulnerable beat.

### Restrained Female Close-Up

Preserve the V1 softer fill and eye catchlight while maintaining a directional source and dark-side shape. Let warmth touch skin against a cooler background when motivated. Do not turn the result into flat beauty light or erase injury, fatigue, fear, or authority required by the scene.

### Shadow Play Or Story-Within-Story

Warm backlit screen, high-contrast silhouettes, minimal facial fill, audience heads as dark foreground mass, and graphic negative space. Keep screen brightness and silhouette edges stable.

### Interrogation Or Concealed Anger

One motivated side or top-side key, dark side exactly 2 stops below key, spill removed from the pressure side, one eye or hand retained as the active channel, and a practical/background layer that fixes geography. Avoid a decorative rim on both characters.

### Injury Or Vulnerability

Broad but directional soft source, quick falloff beyond the face and hands, dark-side detail retained at 1.5 stops below key, restrained catchlight, and material response on sweat, blood, bandage, or damp hair without glossy beauty highlights.

### Revelation Or Threshold Transition

Let the actor cross a fixed light boundary from shadow to window/door/fire light. Define the start mark, crossing beat, and end mark; keep the source stationary. The transition must reveal new story information rather than merely brighten the image.

### Top-Lit Group Or 360-Degree Move

Choose exactly one mode: a bounded practical pool, an even but directional soft top zone, or a top-back separator. State the pool boundary, playable area, table/ground return that protects the eyes, and the darker space beyond it. The camera may move around the group while world-space light direction, contrast, practical positions, and background brightness remain fixed.

## 9. Seedance Translation Templates

### Global Lighting Master

Use this order inside the generator-facing prompt:

```text
灯光母版：本段以{叙事功能}为唯一主导，色彩对情绪采取{强化或反向张力}；{可见或可推断光源}固定在场景{世界坐标方位与高度}，摄影机位于人物{亮侧或暗侧}，从人物{受光侧}形成{主光软硬、包裹度、热点/覆盖、阴影边缘与衰减}；{辅光或负补光策略}使暗面精确低主光{单一档位}，优先保留{眼睛/皮肤/手/道具}；仅从{本镜相关的一至三个边界}切断{具体溢光，无风险则明确无需额外控溢光}；{具体分离光或实景光}建立{前中后景层次}；曝光优先保护{人物/窗外/雪/火焰/地标}并允许{明确可牺牲信息}；{雾/雪/烟/湿地反射}只用于{可见作用}；人物皮肤、发丝、服装、刺绣、首饰和道具共同接受{色温与材质响应}，禁止无动机轮廓光、双主光、平光和环境贴片感。
```

### Global Lighting Master And Per-Shot Source Field

For each named scene segment, put the complete lighting system once in `全局视觉 / 材质 / 光影母版`: story function, motivated source, apparent size, world-space placement, camera-to-key relation, quality/coverage/falloff, exact dark-side difference, protected information, relevant spill boundaries, separator/practical position and relative brightness, exposure hierarchy, material response, catchlight state, and continuity. When the prompt contains multiple scenes, give each scene a short submaster inside that same heading.

Every declared shot then begins with the canonical camera header from [camera-parameter-presets.md](camera-parameter-presets.md). Its `光源` field says `本场景母版，无变化` when the named scene master is inherited unchanged; with multiple named scene segments, use the matching compact scene label. If a relationship, light-zone, practical, or effect-light state changes, write only that real per-shot delta. Do not restate the shared source/direction, repeat the expanded master per shot, use conversation-only `同上`, or append the retired lighting/camera tail after performance. The following `表演 / 动作 / 承接` prose shows the event-light response. `shot count = shot-header count` remains mandatory.

### Moving-Light Beat

```text
灯光变化：光源位置不动；人物从{起点光区}沿{动作路径}进入{终点光区}，在{剧情触发动作}时{眼睛/脸/手/道具}由{起始明暗与色温}过渡为{终止明暗与色温}，背景实景光与阴影方向全程稳定。
```

### Compact Direct-Mode Sentence

```text
参考场景的光向只控制环境；人物进入场景后由同一{窗/日光/灯笼/火光}重新染色，亮侧、暗面环境反射、接触影、服装高光与背景层次一致，拒绝沿用人设图棚拍光和抠图边缘光。
```

## 10. Reference Roles And Continuity

A supplied scene reference may control `environment/palette-material-light` even when it does not show the target camera-side lighting. Bind it only to the camera position, visible surfaces, source direction, shadow side, practical placement, subject mark, contrast, palette, and material response it actually provides. Do not treat it as permission or refusal to write the shot: the current user facts, story, and written storyboard own the target view and final lighting state, and any unsupported dimension is supplied as explicit observable text.

Use direct textual specification rather than requesting a repaired or new image when:

- the target camera crosses to an unseen side with recognizable geometry or light interaction;
- a close or telephoto shot needs material detail or cast-shadow behavior absent from a panorama;
- the actor must touch a table, doorway, wall, bed, or prop whose light/contact state is not visible;
- the shot changes day/night, practical state, fire state, weather, damage, or dominant source direction;
- a moving actor needs multiple light zones that the supplied scene reference contradicts;
- relighting would erase the reference's defining cast shadows or create a second sun.

In every such case, retain the reference only for compatible roles and write the new camera-facing geometry, contact surface, source position, shadow state, practical state, actor light zones, exposure hierarchy, and material response directly into the same complete prompt. Do not generate a scene image or require a replacement reference; deliver the text prompt directly.

For dialogue reverses, preserve the same world-space source. The key may appear on opposite screen sides after the camera reverses; forcing it to stay on the same screen side creates a continuity error. Match key height, shadow direction, exact dark-side difference, practical position, white balance, haze, and background-layer logic.

For adjacent shots, track:

```text
source_world_position | camera_to_key_relation | key_side | shadow_side |
dark_side_stops | negative_fill_and_relevant_spill_cut_zones | catchlight_state |
practical_position_and_brightness | WB | haze | material_response |
actor_start_mark | actor_end_mark
```

## 11. Failure Modes And Preflight

Reject or repair:

- `电影感打光 / 高级光影 / 柔和灯光` without source, side, quality, contrast, and visible result;
- two unrelated keys, two suns, or a rim with no source;
- frontal or overhead exterior sun that causes squinting, hard forehead/nose patches, or skull-eye sockets;
- frontal fill that erases cheek, jaw, costume, and set depth;
- a camera/key relationship that changes randomly or makes every reverse front-lit;
- soft light described as shadowless while also requesting strong side modeling;
- top light with dead eyes when dialogue or recognition depends on eye information;
- negative fill that crushes hair, cheek, costume, and prop into one black shape;
- book-light softness that spills onto every wall and turns haze gray;
- a book light whose final diffusion is not evenly filled, or a grid so narrow that the effective source becomes hard;
- white wall, low white ceiling, pale floor, or reflective rig contamination that secretly fills the dark side;
- hard silver/gold behavior that produces clipped skin, metallic faces, or unstable glints;
- warm bounce that makes all skin, white fabric, wood, and flame the same orange;
- a visible lantern or candle too dim to motivate the claimed exposure;
- bright edge lamps or architecture that steal attention from the subject;
- character light that ignores the supplied scene reference's source and creates a pasted-on portrait;
- artificial and natural sun that create double shadows or mismatched height, color, hardness, or falloff;
- matched reverses that copy screen-side light instead of world-space light;
- catchlights that multiply, switch sides, or disappear without a story/position trigger;
- saturated electric-blue moonlight without an explicit stylization request;
- a moving actor whose face remains identically lit through incompatible zones;
- every background plane at equal brightness;
- global ISO-like shadow lift with no edge, hotspot, or depth structure;
- an otherwise readable head floating against absolute black with no shoulder or distant layer;
- window/snow overexposure that erases a required landmark or spatial relation;
- haze density or direction that changes between matched shots;
- color that mechanically equates tragedy with cold desaturation when the intended counter-tension is warm or alive;
- final blocks that leave a ratio range, material alternatives, or multiple light plans.

Before delivery confirm:

- one story function and one dominant source are legible;
- source direction is physically tied to the set;
- camera side, face shadow side, and background separation follow the chosen key relationship;
- key quality includes apparent-size result, direction, shadow edge, and falloff;
- any book-light final surface is evenly filled and its output loss/spill are acknowledged;
- fill or negative fill uses one exact dark-side difference;
- eyes/skin/hands/props expose according to story priority;
- one concrete separation/effect source builds depth;
- spill and background brightness are controlled;
- any bounce states its original source, reflecting surface, landing zone, and direct-light cut;
- skin, fabric, metal, snow, wood, haze, and wet surfaces respond consistently;
- the exposure hierarchy states which detail is protected and which may intentionally fall away;
- actors have defined lighting marks when they move;
- every reverse and adjacent shot preserves world-space continuity;
- every changed lighting state or required view has an updated reference-role boundary and a complete textual lock for the new source, world position, shadow state, exposure, material response, and continuity;
- every declared shot has one canonical front-loaded camera header whose `光源` field says `本场景母版，无变化` when unchanged or only the real per-shot delta when changed, followed by complete performance/action/handoff prose; the shared source/direction and expanded same-scene lighting system appear once in the global master rather than once per shot.

## 12. Course-Evidence Map

The applied craft was derived from these inspected topic groups:

- `Lighting for Storytelling`: day-exterior timing and sun orientation, self-lighting locations, natural-light control, early-morning replication, interviews with available light, large-source shaping, and the use of light to create depth, mood, and emotional information.
- `Light Placement`: key and fill as separate story decisions, top-light pools, matching artificial and natural sunlight, bounce placement, source containment, and subtraction of unwanted spill.
- `Light Quality`: apparent source size, round versus square motivation, white/muslin/silver/gold/black surface behavior, book-light diffusion, negative fill, exterior shaping, layered setup design, and practical-light color matching.

Use this evidence map for provenance only. The operational sections above are the runtime contract.
