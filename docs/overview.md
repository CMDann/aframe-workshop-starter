# Workshop Overview

## Spatial Storytelling: Designing Your First WebXR Scene

A 2-hour, hands-on workshop where participants design and publish their own interactive 3D scene using WebXR — no prior coding or 3D experience required. Everyone leaves with a real, shareable scene they built themselves, viewable in any browser (or in VR, if a headset's on hand).

---

## Who this is for

No prior coding, 3D, or game-dev background assumed. Some HTML familiarity helps but isn't required — the starter template is designed to be readable and editable by someone seeing A-Frame for the first time. Works for classroom-sized groups (one laptop per participant, facilitator plus roughly 20-25 people).

## Learning outcomes

By the end, participants will be able to:

- Apply basic spatial design principles — composition, lighting, mood — to a 3D scene, not just place objects at random.
- Read and edit declarative A-Frame markup to position, scale, color, and light objects in 3D space.
- Curate deliberately — whether from the supplied asset kit or assets they source themselves — rather than defaulting to whatever's fastest to grab.
- Publish a working WebXR experience and share it with a live link.

## Format at a glance

| | |
|---|---|
| **Duration** | 2 hours |
| **Group size** | Classroom-sized (facilitator + ~20-25) |
| **Tools** | A-Frame (loaded via CDN, no install) + Glitch (hosted, HTTPS, live preview) |
| **Fallback** | GitHub Pages / local server, documented in `docs/deployment.md` |
| **Output** | A personal, shareable WebXR scene live at a public URL |

## The pedagogical model: the 4 Ds

The session is structured around four moments, in order, rather than a feature-by-feature software tutorial:

- **Direction** — participants pick a mood, theme, or concept for their scene before writing anything. Intent comes first.
- **Description** — writing the A-Frame entity tags that describe what they want in the scene. This maps unusually literally onto A-Frame's declarative syntax: describing a scene *is* the code.
- **Discernment** — choosing deliberately from the supplied asset kit or sourcing your own (models, skybox images), with the skill being judgment about what serves the mood, not how much stuff you can find.
- **Delegation** — A-Frame's default components (camera rig, look-controls, cursor, lighting defaults) handle the underlying complexity, so participants never touch raw WebXR API code and can spend their time on composition instead.

## What participants leave with

- A live, shareable URL to the scene they built.
- A one-page cheat sheet of the A-Frame syntax they used (`docs/student-cheatsheet.md`).
- A path to keep building: the starter template and asset kit stay forkable after the session ends.

## Related documents

- `docs/assignment.md` — the student-facing task brief and requirements
- `docs/facilitator-guide.md` — run of show, pre-session checklist, common failure points
- `docs/student-cheatsheet.md` — one-page A-Frame quick reference
- `docs/deployment.md` — Glitch / CodeSandbox / GitHub Pages / local fallback instructions
- `asset-kit/` — curated models and skyboxes, with license attribution
- `starter-template/` — the fork-ready scene participants build from
