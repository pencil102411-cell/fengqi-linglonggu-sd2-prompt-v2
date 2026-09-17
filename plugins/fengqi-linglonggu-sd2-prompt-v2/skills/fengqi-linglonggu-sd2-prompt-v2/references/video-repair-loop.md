# Generated-Video Repair Loop

Use this reference when a draw operator returns the exact prompt used for a `风起玲珑骨` Seedance 2.0 or Seedance 2.5 attempt, the resulting video, and a description of what went wrong. Preserve that source model version unless the user explicitly requests a migration. This is a post-generation evidence and prompt-repair mode, not ordinary prompt creation.

## Ownership And Priority

- The user's failure report defines the intended result and inspection priority; the returned video establishes what visibly happened.
- Preserve the exact submitted prompt as an immutable attempt record. Diagnose that prompt, not an earlier draft or a reconstructed approximation. Record its complete `全局视觉 / 材质 / 光影母版`, backstage `visual_master_version`, resolved scene family, and resolved effect-state branch when present.
- Treat the returned video as `diagnostic evidence only`. Never bind a failed output as a new motion, camera, first-frame, last-frame, identity, or style reference unless the user explicitly assigns that role.
- Perform symptom classification and smallest-change reasoning inside this loop. In ordinary unrestricted project repair, return a complete rewritten prompt for every evidence-backed retry, including `MODEL_EXECUTION_VARIANCE`, rather than a patch-shaped fragment. An explicit preservation-first scope lock instead follows the higher-priority splice/patch-only contract in the parent V2 `SKILL.md`.
- Inspect the video directly and extract timestamped evidence frames with available local video tools. An unavailable review specialist does not block repair, and must never be claimed as executed.
- Preserve the source target route after diagnosis. For both Seedance 2.0 and Seedance 2.5, the parent V2 project's local CineVisible compiler writes and validates the complete generator-facing content inside `【完整可复制提示词】`. In both routes, keep the visible outer package owned by [seedance-assembly.md](seedance-assembly.md).
- Repair directly from the exact submitted prompt, returned video, supplied character/scene settings, plot/storyboard, and actual generator references. Do not run a scene-asset gate, generate a replacement image, or delay prompt repair until an asset receives a status. If a supplied reference cannot control the failed field, narrow its role sentence to what it truthfully supplies and express the corrected viewpoint, blocking, light, interaction, or continuity state in positive text. Never invent a new handle or claim that an absent reference was generated or inspected. An explicit preservation-first scope lock still forbids changing a role sentence outside the authorized span.

## Repair Readiness

The minimum evidence for a causal repair is:

1. the exact complete prompt submitted to the resolved Seedance 2.0 or Seedance 2.5 target;
2. the exact generated video produced from that prompt;
3. the user's description of the wrong result and the desired correction.

Also use the actual generation mode, duration, aspect ratio, reference assets, layout board, seed/settings, and intended storyboard when supplied. Do not invent missing assets or settings.

- If the video is missing or cannot be opened, do not claim to have watched it. Perform only a prompt-side risk audit and request a playable upload before causal attribution.
- If the exact submitted prompt is missing, visually describe the failure but do not claim that a specific clause caused it and do not reconstruct a definitive repair prompt from memory. Request the exact prompt.
- If reference-bound causality depends on an unavailable identity, scene, layout, prop, first-frame, or last-frame asset, mark that dimension `unverified` and avoid false certainty.
- Never fabricate a timestamp, frame, cut, gesture, screen side, camera move, or artifact that was not inspected.

## Evidence Inspection Protocol

1. Assign the failed attempt a stable revision label such as `R01`; preserve its prompt, video, settings, and reference-role map without overwriting them.
2. Watch the complete video once at normal speed with audio to understand rhythm, cut logic, dialogue, and the failure in context.
3. Reinspect every reported failure segment frame by frame. Record the first frame, representative failure frame, recovery or last frame, and exact visible timecode.
4. For multi-shot standing, continuity, cut, or axis problems, extract non-destructive first/key/last evidence frames and contact sheets in a temporary directory with available local video tools. Build a full contact-sheet deliverable only when the user explicitly asks for one; ordinary repair must not create or report that extra package.
5. Compare the returned video with the exact prompt, active reference roles, complete visual master, resolved family, resolved effect-state branch, first visible state, shot endings, next-shot openings, left/right positions, world-space axis, gaze, body facing, prop hand, contact surface, action chain, camera side, focal/shot rules, light continuity, audio, and duration budget. Also compare the current prompt against the accepted lineage root and the immediately preceding revision so a successful visual or narrative control cannot disappear unnoticed across multiple rewrites.
6. Build one backstage causal ledger:

```text
shot_id + timecode
observed visible failure
user's desired visible state
exact prompt clause, omission, contradiction, or overload linked to the failure
cause class and confidence
smallest positive correction
successful controls that must remain unchanged
visual_master_version + resolved family + resolved effect-state branch + exact protected visual-master text
```

Keep inspected frame-accurate timecodes and quoted old clauses in the human-facing diagnosis only. Do not place diagnostic metadata, old-failure narration, or revision language inside the generator-facing copy block. This does not ban a necessary story/reference/edit range inside the copy: such a range must be rewritten with integer endpoints in `N-Ns` form, such as `1-3s` or `4-5s`.

## Cause Classes

Assign every material failure one primary cause class:

- `PROMPT_DIRECT_CONFLICT`: two or more instructions demand incompatible positions, actions, emotions, optics, timing, light, or endings.
- `PROMPT_AMBIGUITY`: the prompt names a result but leaves subject ownership, screen side, world position, path, endpoint, contact, gaze, camera side, or timing open.
- `PROMPT_OMISSION`: a necessary first-frame, blocking, axis, action-chain, hand/prop, continuity, or camera proof is absent.
- `PROMPT_OVERLOAD`: too many actions, camera moves, emotional reversals, details, or cuts compete within the available duration.
- `ASSET_ROLE_OR_VIEW_MISMATCH`: the bound reference cannot supply the required identity, viewpoint, surface, layout, interaction, or continuity role.
- `MODEL_EXECUTION_VARIANCE`: the prompt and assets contain a clear, non-conflicting control, but the output still drifts stochastically.
- `UNVERIFIED`: missing or unreadable evidence prevents reliable attribution.

Name a prompt cause as definite only when the video evidence and exact prompt support it. Otherwise say `most likely` and retain the confidence level. Do not invent a bad clause merely to sound precise; an omission, asset weakness, or execution variance may be the real cause.

## Common Failure Root-Cause Map

| Failure | Inspect | Common prompt cause | Positive repair first |
|---|---|---|---|
| 人物站位错误、换边、距离漂移 | first frame, screen-left/right, foreground depth, world landmarks, facing, gaze, path and endpoint | missing dual screen/world anchors; unlabeled subject; no measurable distance; camera orbit silently changes sides; no stable end anchor | state each subject's screen side and world position, distance, body facing, gaze target, movement path and end mark; keep the camera in one half-space; bind a layout board when needed |
| 画面穿帮、穿模、道具或场景异常 | body/prop intersections, contact surfaces, clearance, occlusion, set surfaces, unwanted modern/text elements, identity/wardrobe/prop state | missing interaction surface or clearance; impossible path; overly aggressive camera; contaminated reference/background; too many simultaneous contacts | specify the visible contact surface, prop hand, clearance and occlusion; simplify the move; lock the period set and prop state; use a text-defined close insert or an actually supplied scene reference to hide unsupported geometry |
| 人物表演问题 | gaze order, listening, breath, hands, posture, intensity, tears, reaction delay and endpoint | adjective-only emotion; conflicting endpoints; too many reversals; no objective/tactic/counterforce; no listening or recovery | rewrite one dominant emotion plus one counterforce as 3-5 visible states, with an exact tear state, body channels, trigger and stable endpoint |
| 动作不连贯、动作重置、失重 | start anchor, preparation, support foot, weight transfer, contact, receiver response, follow-through, braking and recovery | missing kinetic chain; cut restarts action; overloaded beat; contact has no consequence; endpoint is undefined | restore the full action chain and one next-shot-ready end anchor; reduce competing actions; make the next shot open from the previous changed state |
| 镜头不衔接、跳切关系错误 | previous last frame versus next first frame, subject count, position, body/gaze direction, prop hand/state, camera side, light, WB and action phase | no handoff state; mismatched camera baseline; next shot restarts or teleports; prop/light continuity absent | make shot N's visible endpoint equal shot N+1's opening state; match axis, gaze, prop hand, world light and capture baseline; use a motivated insert, occlusion or re-establishing shot only when it solves a proven mismatch |
| 越轴、视线方向颠倒 | world-space interaction axis, camera position per shot, screen direction, reverse pair, any arc/orbit path | axis never declared; camera move crosses the line; reverses copy screen-side light/position rather than world coordinates; left/right labels change meaning | declare the fixed world axis and permitted camera half-space; lock each character's screen direction and gaze; keep reverse cameras on the same side; cross only through a visible neutral-axis or re-establishing transition when explicitly intended |

Do not repair these failures with style adjectives. Repair blocking, axis, temporal handoff, contact physics, performance behavior, reference roles, or shot density first.

## Prompt-Cause Audit And Rewrite

For each observed failure:

1. Quote only the smallest relevant original clause in the human-facing diagnosis, or state the exact missing control.
2. Classify the repair operation as `remove`, `rewrite`, `move earlier`, `add one lock`, `narrow/rebind a supplied reference role`, or—only under an authorized condition—`split the clip`.
3. Remove contradictions, duplicate wording, stale context, and duration overload before adding text, but preserve the complete handle-bound per-reference `参考图角色分工：` block required by the parent V2 contract and the exact `FQ-EFTV-01` visual baseline plus one resolved family and one resolved effect-state branch. Their required placement is not removable duplication; remove only accidental repeats elsewhere.
4. Preserve every visibly successful identity, costume, prop, composition, performance, camera, lighting, material, sound, continuity, visual-master, resolved-family, and effect-state control. A requested repair to another field does not authorize a visual-family swap, branch switch, or deletion.
5. Translate the correction into positive, visible facts. Prefer `玲珑始终位于画面左侧，沿桌案西边缘移动至门槛内侧停住` over a stack of `禁止站错 / 禁止换边 / 禁止漂移`.
6. Fix one primary root cause and at most two linked secondary causes per retry when the clip remains usable. If the result is unusable, repair all blocking causes but still group them by root cause instead of adding unrelated polish.
7. If the revised camera side, focal rule, viewpoint, blocking, interaction, light state, or required visible surface differs from a supplied reference, update that reference's controlling role and rejection boundary truthfully, then compile the requested result directly in text. Keep existing handles only for actual supplied inputs. Under an explicit local-repair span, stop for scope expansion if the required role-sentence change falls outside the authorized span rather than altering frozen text.

## Ordinary Full-Prompt Contract

Outside explicit preservation-first local repair, every ordinary repair response must contain the complete revised 瑞宝PRO ready-state package and the entire self-contained prompt, including retries classified as `MODEL_EXECUTION_VARIANCE`. In that ordinary mode, never return only a patch, changed paragraph, replacement sentence, diff, or instruction for the operator to merge manually.

When an explicit scope lock is active, this section yields to the parent V2 preservation-first contract: use the exact baseline, edit only the allowed span, and either splice the complete baseline or—when patch-only is requested—emit exactly the replacement span with no added wrapper or report.

- Retain the six outer headings and all nine ordered inner headings.
- Rewrite every declared shot in full. Start each shot with the canonical `镜头号→景别→焦距→光源→机位/运动→焦点/景深` header, then write complete `表演 / 动作 / 承接`; never append the retired full camera tail or write `同上`, `其余不变`, `沿用上一版`, `只替换以下内容`, or an ellipsis. `本场景母版，无变化` is allowed because it resolves inside the same complete prompt; if light changes, write only the real per-shot delta rather than restating the shared source/direction.
- Keep the repaired prompt stateless. Inside the copy block, describe only the desired current video; do not mention `上一次`, `原视频`, `错误`, `返修`, timestamps, confidence, or old unwanted objects.
- Inside the copy block, any necessary story, reference-active, or edit-target range uses integer-second endpoints, one ASCII hyphen, and one final lowercase `s`, such as `1-3s` or `4-5s`. Do not carry frame-accurate diagnosis timecodes, decimal seconds, colon timecodes, alternative separators, or a Chinese `秒` suffix into the generator copy. Under a scope lock, normalize only the authorized span and leave frozen time text verbatim.
- Put the revision label, timestamped evidence, exact prompt cause, correction strategy, and preserved successes inside `【镜头设计摘要】`, not in a new competing outer section.
- In `【参考素材角色表】`, mark the submitted prompt and returned output video as diagnostic evidence only. Under the exact legacy-compatible label `参考图角色分工：`, list every actual generator image/video/audio/clay/edit reference separately with its modality-appropriate handle—`@图片 N / @视频 N / @音频 N` in upload order, or the exact active-product handle for a 2.5-only special modality—and one complete natural-language `只锁定……，不复制……。` sentence. Repeat those same complete handle-bound sentences under the fenced first heading `参考图角色分工：`; diagnostic evidence never enters the fenced block. Do not shorten the generator references into invented placeholders, internal role codes, filename-only entries, table fragments, or pointers to the outer table.
- In ordinary unrestricted repair, preserve the source target version and rebuild only the complete fenced copy block after diagnosis; the parent V2 project's local CineVisible compiler writes that block for both Seedance 2.0 and Seedance 2.5. Under a preservation-first scope lock, the same compiler instead performs exact splicing or patch-only output. In both routes, V2 continues to own the outer package.
- Preserve the exact `FQ-EFTV-01` baseline once inside `全局视觉 / 材质 / 光影母版`, preserve the accepted resolved family and effect-state branch unless the user requests a visual/effect change or timestamped evidence proves it is causal, and append only the repaired current-scene light/material delta. A no-effect branch contains no effect vocabulary. Never expose the version code or use a source-drama title as the replacement.
- Preserve the project close-framing clause, character routing, action physics, `shot count = shot-header count`, fixed header order, global-master inheritance, narrative light, direct reference-role boundaries, one-to-four-shot continuity, and all other V2 invariants.
- Count the exact repaired fenced text, including punctuation, spaces, and line breaks, and keep it at or below 5000 characters. A one-to-four-shot sequence intended for one generation stays in one package and one fenced block. If the first repair draft exceeds 5000, compress duplicated atmosphere, repeated global masters, workflow/meta prose, inactive physics/audio/negative channels, and verbose continuity wording in place; never remove supplied dialogue, required performance/action, shot order, positions, scene transitions, end-to-next-opening handoffs, complete reference-role sentences, shared capture/light facts, or required camera-header fields. Character count alone never authorizes a split.

Use this repair population inside the existing package:

```text
【镜头与素材状态】[直接编译（文本生成 / 按已提供素材参考生成）]
 【参考素材角色表】
参考图角色分工：
[每个实际生成参考素材各用一句带规范句柄的完整“只锁定……，不复制……”说明]
诊断证据：[submitted prompt + returned video marked diagnostic-only]
【镜头设计摘要】
制作设置：[保留源模型版本、模式、时长、平台画幅、构图/裁切目标、同步音频状态；摄影参数仅作创作意图，不作为平台硬参数；不得复制进下方围栏]
返修版本：[R02]
视频证据：[shot/timecode + observed fact]
提示词根因：[cause class + exact clause/omission + confidence]
重写策略：[remove/rewrite/add/move/rebind；仅在获准时 split]
保留项：[successful controls left intact]
【完整可复制提示词】
参考图角色分工：
[逐素材重复外层带规范句柄的完整自然语言说明，不得缩写或省略]
全局视觉 / 材质 / 光影母版：[FQ-EFTV-01 固定质量基线逐字一次；保留或有证据地修改一个已解析家族；保留或有证据地切换一个已解析 effect=active/none 分支；当前镜头光线与材质结果]
[the remaining seven headings of the complete prompt]
【生成前质检】[root causes corrected; full package; direct-compilation, 5000-character, continuity, and camera checks pass]
【下一轮只建议调】[one controlled variable]
```

## Negative-Constraint Budget

Outside preservation-first local repair, repair positive controls first and keep `负面限制` to no more than five short, shot-specific constraints across the complete generated clip; two to four is preferred. Under a scope lock, apply this budget only to newly authored text inside the allowed span and never delete, consolidate, or rewrite frozen negatives. Retain only high-risk failure classes supported by the reviewed video or required for basic continuity/anatomy/text hygiene.

- This repair-specific five-total budget overrides every imported legacy rule, per-shot quota, example, or negative bank. Use legacy negatives only as candidate risks, then consolidate the entire clip to five or fewer.
- Do not repeat the same prohibition in global, per-shot, continuity, and negative sections.
- Do not narrate the old wrong result in the negative block or name stale objects merely to forbid them.
- Do not convert every positive blocking, action, acting, or camera instruction into a mirrored negative.
- When a precise positive lock makes a prohibition redundant, delete the prohibition.

## Iteration Loop And Stop Conditions

- When the next video returns, compare it with both the accepted lineage root and the immediately preceding revision plus its isolated primary change. Preserve newly successful layers and the original still-valid controls instead of restarting from scratch; flag any missing dialogue, performance beat, shot, transition, reference role, visual-master clause, global capture/light fact, camera-header field, or handoff before the candidate becomes the next baseline.
- If the same failure family repeats twice, stop adding text. Reinspect timestamped frames and actual references, reduce prompt density, strengthen positive layout/blocking text, or narrow a supplied reference role. Split the clip only when the returned-video evidence identifies execution overload and the user approves; character count, four-shot count, or risk speculation alone never authorizes splitting.
- Do not call a failure a model limitation until prompt conflict, omission, overload, asset mismatch, and workflow error have been checked.
- Stop the repair loop when the user accepts the result, the evidence shows no material failure, or the exact submitted prompt/video needed for causal repair remains unavailable. Missing optional scene imagery does not block direct prompt compilation from the supplied settings, plot, or storyboard.

## Repair Preflight

Before delivery, verify:

- the exact submitted prompt and returned video were both inspected;
- every diagnosed symptom has timestamped visible evidence and a cause class;
- definite prompt causes point to an exact clause, omission, conflict, or overload; uncertain causes are labeled `most likely`;
- successful controls are preserved and the rewrite does not introduce unrelated creative changes;
- the repaired global visual field contains the exact `FQ-EFTV-01` baseline once, one resolved scene family, one resolved effect-state branch, and the current light/material facts; the accepted family or branch changed only under explicit visual/effect scope or timestamped causal evidence, a no-effect branch contains no effect vocabulary, and neither the version code nor a source-drama title appears in generator-facing text;
- changed camera, blocking, light, interaction, or supplied-reference roles were rewritten directly and their controlling/rejection boundaries remain truthful;
- no scene-asset gate, automatic image generation, invented handle, or claim of inspecting an absent reference entered the repair;
- in ordinary unrestricted repair, the response contains a complete prompt rather than a patch or merge instruction; under a preservation-first scope lock, it instead follows exact splicing or explicit patch-only output;
- in ordinary unrestricted repair, all six outer and nine inner headings remain intact; under a scope lock, frozen structure remains verbatim and no current template is imposed on it;
- in ordinary unrestricted repair, every actual generator reference appears under `参考图角色分工：` in both the outer role table and the fenced first heading as the same complete handle-bound `只锁定……，不复制……。` sentence, with correct `@图片 N / @视频 N / @音频 N` upload-order numbering for those three modalities or the exact active-product handle for a 2.5-only special modality, while the submitted prompt and returned video remain outer diagnostic evidence only;
- in ordinary unrestricted repair, the backstage record and `【镜头设计摘要】` preserve the source model version and state the real platform ratio, composition/crop target, synchronous-audio choice, and camera-intent classification; the fenced copy begins directly with `参考图角色分工：` and does not reinsert the removed operational-metadata line or an equivalent key-value preamble;
- in ordinary unrestricted repair, every declared shot is fully written with one front-loaded camera header in fixed order followed by its performance/action/handoff prose; every one-to-four-shot invocation remains one package and one fenced block; under a scope lock, enforce this only inside the allowed span and do not normalize frozen shots;
- in ordinary unrestricted repair, every explicit generator-visible time range uses integer endpoints in `N-Ns` form and every inspected frame-accurate evidence timecode remains in the outer diagnosis; under a scope lock, the same check applies only to newly authored text and never rewrites frozen time text;
- in ordinary unrestricted repair, the close-framing skin/eye clause and all character/action/light/camera invariants pass; under a scope lock, validate only newly authored text and report no extra patch-only notes;
- in ordinary unrestricted repair, the exact fenced text is at most 5000 characters after any required in-place compression, with dialogue, performance, actions, shot order, positions, transitions, handoffs, complete reference roles, continuity, shared global capture/light facts, and camera headers preserved; under a scope lock, frozen text remains exact and an over-5000 complete baseline requires expanded compression scope or explicit patch-only output rather than splitting;
- in ordinary unrestricted repair, `负面限制` contains at most five short, evidenced constraints with no generic prohibition dump; under a scope lock, enforce the budget only inside the allowed span;
- in ordinary unrestricted repair, `【下一轮只建议调】` names one controlled variable; explicit patch-only output adds no such section.
