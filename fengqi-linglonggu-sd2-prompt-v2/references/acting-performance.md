# Acting Performance Layer

Use this layer after current story facts and any supplied reference roles are resolved. Its job is to make character behavior playable, observable, and appropriate for the shot size and duration while proceeding directly to the complete video prompt.

## Table of contents

1. Core model
2. Character master profile
3. Scene adaptation
4. Framing-aware performance
5. Eye life, listening, and voice
6. Duration budget
7. Ensemble and quality control

## 1. Core model

Acting is behavior under pressure, not an emotion label.

For each visible character, define:

- `objective`: what the character wants from a specific partner now;
- `obstacle`: what prevents it;
- `stakes`: the cost of failure;
- `tactic`: the current playable method—press, charm, shame, plead, provoke, bargain, threaten, stall;
- `beat change`: new information, failed tactic, achieved objective, or power shift;
- `subtext`: what the body and timing reveal beneath the spoken text.

Never ask the model merely to show anger, sadness, fear, or confidence. Translate the state into breath, gaze, posture, tempo, distance, touch, hand business, interruption, or refusal.

## 2. Character master profile

Create a persistent profile for recurring characters and store it outside individual video prompts. Include:

- age, build, posture, center of gravity, and physical history;
- one psychological engine that explains the physicality;
- vocal identity and pressure behavior;
- signature habit with its trigger;
- stress habit with its trigger;
- concealment behavior and the exact mask-breaking condition;
- gait and movement economy;
- one optional softening target;
- eye-life baseline.

Do not place wardrobe, camera, color, or lighting in the acting master. Those belong to other layers.

The master is identity, not paste-ready scene text.

## 3. Scene adaptation

Rewrite the master for each shot:

1. Include only characters visible or audibly active.
2. Preserve the core engine, vocal identity, signature triggers, and eye-life baseline.
3. Convert impossible behaviors instead of deleting their energy. A pacer forced to sit may shift into micro-sway, wrist motion, paper tearing, or toe pressure.
4. Give the character physical business: count, clean, fold, repair, hold, sort, pour, or manipulate an action-relevant object.
5. Use the interruption of that business as punctuation when appropriate.
6. Tie every visible reaction to a stimulus or failed tactic.
7. Keep only behavior the camera can see and the duration can support.

## 4. Framing-aware performance

### Extreme wide / wide

Prioritize silhouette, center of gravity, gait, distance, entrances/exits, status, group rhythm, and visible action path. Do not spend prompt budget on tiny eye or lip detail.

### Medium wide / medium

Prioritize torso orientation, hands, object business, breath, partner distance, listening, one tactic shift, and interruption of action.

### Medium close-up / close-up

Prioritize thought-before-word, breath containment, jaw, swallow, eyelid tension, blink quality, micro-saccades, focus shifts, minimal head movement, and the mask cracking. Reduce gestures as framing tightens.

### Extreme close-up

Use one dominant thought change, one eye target, one breath or muscle event, and one consequence. Avoid a chain of large expressions.

If a supplied scene reference does not show the framing or partner eyeline needed by the performance, limit that reference to the environment, palette, material, or other dimensions it actually supplies, then state the required framing, eyeline, partner position, and performance space directly in text. Continue to the complete video prompt; do not require a replacement image or stop delivery.

## 5. Eye life, listening, and voice

### Eye life

- Eyes reach the target slightly before the head.
- Use natural micro-saccades and state-dependent blinks.
- Controlled stillness is deliberate, not frozen.
- Maintain live catchlights only when the shot's light physically supports them.
- Macro gaze target follows the blocking plan; micro gaze behavior follows thought and listening.

### Listening

- A reaction may start before the partner finishes speaking.
- Use a short assessment moment before difficult answers.
- Let tempo, volume, energy, and posture respond to the partner.
- Do not leave an empty neutral face while another character speaks.

### Voice

Keep one stable vocal identity per character: age impression, origin/accent when relevant, timbre, register, pace, and baseline delivery. Scene acting may change volume, breath, rhythm, or pressure behavior without replacing the identity.

If injury, aging, intoxication, disguise, or transformation materially changes the sound, create a clearly named stage variant instead of pretending the voice never changes.

## 6. Duration budget

Scale acting beats to usable screen time:

- `3–5 seconds`: one tactic or action state plus one reaction/consequence;
- `6–10 seconds`: up to two clear beats;
- `10–15 seconds`: two to three clear beats when action and camera remain readable;
- longer scenes: add beats only when each change is visible and motivated.

Do not force two to four beat changes into every short clip. A close-up may be strongest with one thought, one refusal, and one delayed answer.

## 7. Ensemble and quality control

- Stagger group reactions; do not synchronize everyone unless choreography requires it.
- Let status appear through timing, stillness, space, permission, and object handling.
- Preserve emotional inertia across cuts; do not reset after a strong event.
- The stronger character is not always still or quiet; treat that as an option, not a universal law.
- Do not make every character use the same mask, tic, or softening structure.

Before handoff, check:

- objective is a verb aimed at a partner;
- obstacle and stakes affect behavior;
- tactic changes only when motivated;
- body and breath fit the physical action;
- gaze target agrees with blocking;
- close performance is small enough for the frame;
- reaction begins from a real stimulus;
- voice and lips match the scripted dialogue;
- no camera, wardrobe, or color instructions leaked into the acting paragraph.

Scene-performance handoff schema:

```text
shot_id:
objective / obstacle / stakes:
current tactic:
visible business:
opening behavior:
beat change and trigger:
reaction / consequence:
macro gaze target:
micro eye-life behavior:
breath / voice behavior:
end state:
```
