# Decisions

Judgment calls made while building this repo, and open items that still need a human. Recorded here rather than left implicit, so a future maintainer can tell what was deliberate from what was accident.

---

## Resolved

### A-Frame is pinned to 1.8.0, not `latest`

The starter template loads `https://aframe.io/releases/1.8.0/aframe.min.js` — an exact version, verified live at time of writing (1.8.0 released 2026-06-24). A floating `latest` URL would mean an upstream release could change behavior mid-workshop, producing a failure no facilitator can diagnose in the room. Bumping the pin is a deliberate maintenance action, with a re-test, not something that should happen by itself.

### Discernment allows self-sourced assets, not kit-only

`CLAUDE.md` originally framed Discernment as choosing from a curated kit *rather than* hunting the open web. The student-facing docs (`assignment.md`, `facilitator-guide.md`) had already evolved past this: they permit self-sourcing under a hard 10-minute cap and a CC0/CC-BY-only rule.

The docs win, and `CLAUDE.md` has been amended to match. Rationale: banning self-sourcing outright is unenforceable and slightly patronizing — students will look anyway. The cap plus the license rule handles the actual risk (asset-hunting eating the build window, and unlicensed assets ending up in a publicly-published scene) while keeping the real lesson intact, which is judgment about what serves the mood. The facilitator guide lists both as named failure points with fixes.

### `docs/overview.md` and `docs/assignment.md` are kept

Neither appears in the repo layout `CLAUDE.md` specifies, but both existed already and are good. `overview.md` serves the "what is this" need for someone evaluating whether to run the workshop; `assignment.md` is the student-facing brief the facilitator guide's pre-session checklist explicitly depends on. Both are linked from the README's contents table.

### The asset kit will bundle real files, downscaled

Decided for Phase 2, not yet executed. Binaries get committed rather than left as download links, so the repo is workshop-ready with no manual prep step and no live-network dependency during the session. Expected weight is 10-15 MB, which is acceptable for a public repo.

Sourcing constraints found while verifying feasibility:

- **Poly Haven** (CC0) serves skies via a public API, but the `tonemapped` JPG exports are full-resolution — roughly 17 MB each. They must be downscaled to 2048x1024 before committing. macOS `sips` is sufficient for this; Pillow is not installed on the build machine.
- **Poly Pizza's API requires a key**, so its catalog can't be fetched programmatically here. It stays a recommended source for *students* sourcing their own assets, but can't be bulk-pulled into the kit.
- **Khronos glTF-Sample-Assets** is the reliable model source: 150 models, each with its own license file, downloadable directly over HTTPS with no key.

### The starter template ships two lights, not one

`CLAUDE.md` Phase 1 asks for "one `<a-light>` (type="ambient" or "directional" — pick one and comment why)". The template ships both, and the deviation is deliberate.

Tested visually during the build. A-Frame disables its default lighting as soon as a scene declares any `<a-light>`, so a single light really is the only light. Ambient-only renders every face of every object identically: the example cube reads as a flat hexagon and the cylinder as a flat rectangle, with no cue that anything is solid. Directional-only has the opposite failure — unlit faces go to near-black.

The ambient (0.4) plus directional (0.8) pairing is what actually makes geometry legible, and it costs one extra line. Since the opening hook depends on the scene looking good on a projector, and the Phase 1 acceptance criterion is that a participant "can change a color or position value and understand why the scene changed," flat shading worked directly against both.

Knock-on change: `assignment.md`'s stretch goal used to read "layer in a second light" — already true in the starter now — so it was rewritten to push on lighting *mood* (killing the ambient, tinting key against fill, adding a practical point light) instead.

### The repo lives on an exFAT volume

The working volume is exFAT, which doesn't preserve permission bits and causes macOS to scatter `._*` AppleDouble files. `.gitignore` covers `._*`, and the repo sets `core.fileMode false`. Worth knowing if a contributor sees spurious mode-change diffs.

---

## Open items

These block "definition of done" and need a human:

### The Glitch quick-start link imports the whole repo

The README points at `https://glitch.com/edit/#!/import/github/CMDann/aframe-workshop-starter`, which works but imports the entire repository. Because Glitch serves from the project root, the scene ends up at `/starter-template/` on the preview URL rather than at the root — so the quick start is a few clicks longer than the ideal "fork and it's live."

The better pre-launch move is a purpose-made Glitch project containing only the starter template's contents at root, shared as a remix URL. That needs a Glitch account and can't be created from here. Until it exists, the README documents the extra navigation step honestly rather than overpromising.

### README screenshot is a placeholder

A real screenshot or GIF can't be captured until the example scene exists (Phase 6). The placeholder carries an HTML comment marking it as a pre-launch blocker.

### LICENSE copyright holder

Set to `Dann Blair` from the local git config. Confirm this is the right attribution for a public repo before launch — particularly if the workshop is being run under an institutional banner.

---

## Deferred to GitHub issues at publish time

`CLAUDE.md` asks for the stretch items to be filed as issues during Phase 0. The repo had no remote at that point and the GitHub connector is unauthenticated in this environment, so they're parked here. File them as real issues once the repo is published:

1. **AI-assisted asset generation** as an optional "Delegation" extension for longer workshop formats.
2. **Multiplayer / shared-scene support** for group builds.
3. **A branded, skinnable version of the example scene** for institutional demos.

All three are explicitly out of scope for the 2-hour single-participant workshop.
