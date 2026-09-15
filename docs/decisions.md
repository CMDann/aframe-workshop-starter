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

### GitHub Pages serves from the repository root

The presentation needed hosting, and serving Pages from the root of `main` does considerably more than host it. It also publishes `starter-template/`, `example-scene/` and `asset-kit/` over **HTTPS** — which is what makes the VR button work, and gives the asset kit stable URLs a student can reference from a Glitch project.

Live at <https://cmdann.github.io/aframe-workshop-starter/>.

The cost is a root `index.html`, which the layout in `CLAUDE.md` doesn't include, plus a `.nojekyll` file so Pages serves everything verbatim instead of running Jekyll over it. Both are deliberate deviations in service of the HTTPS win. Markdown in `docs/` stays markdown and is read on github.com, which renders it properly.

### reveal.js is pinned to 5.1.0, not 6.0.2

The facilitator deck needs speaker notes (presenter view with a timer, for a session timed to the minute) and syntax highlighting (its whole job is showing A-Frame markup).

Verified against cdnjs: **6.0.2 serves core and themes but not plugins** — `plugin/notes/notes.js` and `plugin/highlight/highlight.js` both 404 there. 5.1.0 serves all of them. So the deck pins the older version on purpose, and this is the reason not to "helpfully" bump it.

### Kit assets are original IP under a workshop-use licence, not CC0

The asset kit was originally specced as curated third-party CC0 downloads. It became original PIZZA.EXE work instead — simpler licensing, and a coherent visual identity rather than a bag of unrelated props.

The terms are **© 2026 Dann Blair, all rights reserved, licensed for workshop use only** ([asset-kit/LICENSE-ASSETS.md](../asset-kit/LICENSE-ASSETS.md)). Use them in a workshop scene and publish it anywhere; don't redistribute them standalone or ship them in other products.

Two constraints shaped the wording, because a literal "no reproduction" would have broken the workshop:

1. **Participants must publish.** `assignment.md` makes a live shareable link the deliverable. A scene containing a kit model reproduces that model the moment it goes online, so the licence has to permit exactly that.
2. **Public GitHub repos can be forked by anyone.** GitHub's Terms of Service grant that right for every public repository, and it overrides repo-level licence text for as long as the repo is public. Going private is the only way to prevent copying. The licence still governs what someone may lawfully *do* with a fork, but it cannot prevent the fork.

Knock-on changes: `CONTRIBUTING.md`'s "CC0 preferred, CC-BY acceptable" rule now applies only to *third-party* contributions and names the first-party assets separately; the root `LICENSE` carves assets out of MIT explicitly; `asset-kit/README.md` and `ATTRIBUTION.md` were rewritten, having previously described a third-party CC0 kit.

### The repo lives on an exFAT volume

The working volume is exFAT, which doesn't preserve permission bits and causes macOS to scatter `._*` AppleDouble files. `.gitignore` covers `._*`, and the repo sets `core.fileMode false`. Worth knowing if a contributor sees spurious mode-change diffs.

---

## Open items

These block "definition of done" and need a human:

### The Glitch quick start needs an extra navigation step

Largely defused, not fully closed. The canonical live demo is now the GitHub Pages URL, which serves the scene directly with no navigation:

<https://cmdann.github.io/aframe-workshop-starter/starter-template/>

The Glitch path remains the recommended route for *editing*, because participants need a fork they can change. `https://glitch.com/edit/#!/import/github/CMDann/aframe-workshop-starter` imports the whole repository, and since Glitch serves from the project root the scene lands at `/starter-template/` rather than at the root.

A purpose-made Glitch project containing only the template's contents at root, shared as a remix URL, would remove that step. It needs a Glitch account and can't be created from here. The docs describe the extra step honestly in the meantime.

### README screenshot is a placeholder

A real screenshot or GIF can't be captured until the example scene exists (Phase 6). The placeholder carries an HTML comment marking it as a pre-launch blocker.

### LICENSE copyright holder

Set to `Dann Blair` from the local git config. Confirm this is the right attribution for a public repo before launch — particularly if the workshop is being run under an institutional banner.

---

## Stretch items — now filed as issues

`CLAUDE.md` asked for these to be filed during Phase 0. There was no remote at that point, so they were parked here and have since been filed:

1. [AI-assisted asset generation as a "Delegation" extension](https://github.com/CMDann/aframe-workshop-starter/issues/1)
2. [Multiplayer / shared-scene support for group builds](https://github.com/CMDann/aframe-workshop-starter/issues/2)
3. [A branded / skinnable example scene for institutional demos](https://github.com/CMDann/aframe-workshop-starter/issues/3)

All three are explicitly out of scope for the 2-hour single-participant workshop.
