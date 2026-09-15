# CLAUDE.md — WebXR Scene-Building Workshop Framework

## Instructions for the executing agent

You (Claude Code) are building an open-source repository from this spec. Work through the **Build Phases** in order. Each phase has acceptance criteria — do not move to the next phase until the current one satisfies them. If a phase requires a judgment call not covered here, make the simplest choice that keeps the workshop runnable end-to-end in a single 2-hour session with zero local installation, and note the decision in `docs/decisions.md`.

This repo will be published publicly on GitHub. Write everything — code, comments, docs — as if a stranger with no context will read it first.

---

## What this project is

A ready-to-fork framework for running a **2-hour, hands-on WebXR scene-design workshop** using A-Frame. Participants start from a working scene template, learn the primitives, and leave with a finished, shareable 3D scene they built themselves — viewable in any browser, no VR headset required (though it works in one if available).

It is designed to be picked up and run by *any* facilitator, not just the original author — that's the point of open-sourcing it.

## Who this is for

- **Facilitators**: educators or workshop leads running a short, no-prior-coding-experience session for students (originally built for a ~2-hour college-level workshop, but should read as reusable for any similar audience — don't hardcode any specific institution's name into the framework itself).
- **Participants**: assume zero WebXR/3D experience. Some may have basic HTML familiarity; none should be required.

## Non-negotiable constraints

These decisions are load-bearing for the whole design — do not silently change them:

1. **A-Frame, not Three.js/raw WebXR API.** Declarative HTML entity-component syntax is the point — it's what makes this approachable in 2 hours.
2. **Zero local install.** The default path is forking a hosted, browser-based editor (Glitch is the reference target; CodeSandbox should work as a documented alternative). A GitHub Pages / local-file fallback must also exist for venues with restrictive networks.
3. **HTTPS-servable by default.** WebXR's VR-mode entry point requires a secure or localhost context — this is *why* Glitch/Pages is the default, not an incidental choice. Don't let a later contributor "simplify" this into a plain `file://`-only setup without flagging the tradeoff in the docs.
4. **Single-file scene, CDN-loaded A-Frame.** No build step, no npm install, no bundler. `<script src="https://aframe.io/releases/.../aframe.min.js">` in the `<head>`, everything else in one `index.html` participants can read top to bottom.
5. **Finished in the room.** Every design decision (asset kit, template scope, cheat sheet) should optimize for "participant has a working, personalized, shareable scene by minute 120" — not for teaching the most A-Frame features.

## Core pedagogical model: the 4 Ds

The workshop structure (and the facilitator guide you'll write in Phase 3) is built around four moments, in order:

- **Direction** — participant picks a mood/theme/concept for their scene *before* touching code.
- **Description** — writing the A-Frame entity tags that describe what they want in the scene (this maps unusually literally onto A-Frame's declarative syntax — call that out in the docs, it's a genuinely good hook).
- **Discernment** — choosing deliberately from a curated asset kit (models, skybox images), or self-sourcing under a hard 10-minute cap and a CC0/CC-BY-only rule; the skill being taught is judgment about what serves the scene's mood, not asset-search. (See `docs/decisions.md` — this supersedes an earlier kit-only framing.)
- **Delegation** — A-Frame's default components (camera rig, look-controls, cursor, lighting defaults) handle the underlying complexity so participants never touch raw WebXR API code. Name this explicitly in the docs as "what the framework is doing for you and why."

---

## Repository structure

Build exactly this layout:

```
/
├── README.md
├── LICENSE                       (MIT)
├── CONTRIBUTING.md
├── CLAUDE.md                     (this file, kept in the repo root)
├── starter-template/
│   ├── index.html                (the fork-ready A-Frame scene)
│   └── README.md                 (how to fork it — Glitch, CodeSandbox, GitHub Pages, local)
├── example-scene/
│   ├── index.html                (a finished scene built FROM the starter template, used as the opening demo)
│   └── README.md                 (what's demonstrated and why, for facilitators prepping the hook)
├── asset-kit/
│   ├── manifest.json             (schema below)
│   ├── models/                   (a small default set of CC0 .glb props, or documented download links if binaries can't be fetched)
│   ├── skyboxes/                 (a small default set of CC0 equirectangular images for a-sky)
│   └── ATTRIBUTION.md            (source + license for every asset, no exceptions)
├── docs/
│   ├── facilitator-guide.md      (run-of-show, timing, pre-session checklist)
│   ├── student-cheatsheet.md     (A-Frame primitives/attributes quick reference)
│   ├── deployment.md             (Glitch / CodeSandbox / GitHub Pages / local-fallback instructions)
│   └── decisions.md              (any judgment calls made while executing this spec)
└── .gitignore
```

---

## Build phases

### Phase 0 — Repo scaffold
Create `README.md`, `LICENSE` (MIT), `CONTRIBUTING.md`, `.gitignore` (standard web project ignores), and the empty folder structure above.

`README.md` should cover, in this order: one-paragraph pitch, a screenshot/GIF placeholder (note in a comment that a real one should replace it before launch), quick-start ("fork this on Glitch and you have a working scene in 30 seconds" — the actual link goes in once `starter-template` exists), what's in the repo (link to each doc), license, and a "built around the 4 Ds framework" callout with a one-line explanation of each D.

**Acceptance criteria**: a first-time visitor can tell what this is and how to try it within 30 seconds of landing on the README.

### Phase 1 — Starter template
Build `starter-template/index.html`: a complete, well-commented A-Frame scene containing —
- `<a-scene>` with a `<a-sky>` (default color, swappable via comment instructions)
- one `<a-light>` (type="ambient" or "directional" — pick one and comment why)
- a ground `<a-plane>`
- a camera rig entity with `look-controls` and `wasd-controls`, plus a `cursor` for interaction
- 2-3 placeholder primitives (`a-box`, `a-sphere`) with obvious, commented position/rotation/scale/color attributes as an editing example
- an HTML comment block at the top explaining what each section does, written for someone who has never seen A-Frame before

Every attribute a participant is expected to touch in the workshop should have an inline comment. This file doubles as the in-session reference, so over-comment rather than under-comment.

**Acceptance criteria**: opening this file in a browser (via Glitch preview or local server) renders a scene with visible geometry, working camera look/move controls, and a VR-mode button. A participant with zero A-Frame experience can change a color or position value and understand why the scene changed just from the comments.

### Phase 2 — Asset kit
Build `asset-kit/manifest.json` with this schema:

```json
{
  "models": [
    { "id": "string", "name": "string", "file": "models/....glb", "source_url": "string", "license": "CC0 | CC-BY (name attribution requirement)", "tags": ["prop","furniture", "..."] }
  ],
  "skyboxes": [
    { "id": "string", "name": "string", "file": "skyboxes/....jpg", "source_url": "string", "license": "string", "mood_tags": ["noir","dream","..."] }
  ]
}
```

Populate it with a small default set (aim for 8-12 models across a couple of mood categories, 4-6 skyboxes) sourced only from CC0 or clearly-licensed repositories (e.g. Poly Pizza, glTF sample repo, ambientCG, Poly Haven HDRIs re-exported as equirectangular JPGs). If you have live network/fetch access, download the actual files into `models/` and `skyboxes/`; if you don't, populate the manifest with direct source URLs and leave a clear `docs/decisions.md` note that a human needs to download and drop in the binaries before the repo is workshop-ready — do not fabricate placeholder binaries.

Every single asset must have a corresponding line in `asset-kit/ATTRIBUTION.md` — source, license, and any required credit text. This is non-negotiable for an open-source repo; an unattributed asset is a legal problem waiting to surface.

**Acceptance criteria**: manifest.json validates as JSON, every entry has a matching attribution line, and the mood_tags/tags give a facilitator enough to say "if your theme is X, look at these assets" without opening every file.

### Phase 3 — Facilitator guide
Write `docs/facilitator-guide.md` structured as:

1. **Pre-session checklist** — test the venue wifi against Glitch (or whichever host you're using) at least a day ahead; confirm the local-fallback path works if wifi fails; if a headset will be passed around, test it against the starter template beforehand; print or link the student cheat sheet.
2. **Run of show** (2 hours, with clock times) —
   - 0:00–0:10 Hook: open the example-scene, view-source it live, make the point that the whole thing is ~15-30 lines of HTML.
   - 0:10–0:25 Fork the starter template together; tour the primitives; live-edit one attribute as a group.
   - 0:25–0:35 Direction: a 5-minute individual prompt to pick a mood/theme before writing more code.
   - 0:35–1:35 Build time, framed explicitly through Description / Discernment / Delegation (see 4 Ds section above) — this is the bulk of the session.
   - 1:35–1:50 Peer-test: everyone already has a live URL from their fork; view 2-3 classmates' scenes.
   - 1:50–2:00 Gallery walk + "one thing you'd add with more time."
3. **Common failure points and fixes** — things like: scene not rendering (check script tag/typo), VR button missing (check HTTPS context), model not loading (check CORS/asset path), participant runs out of time mid-build (have a "minimum viable scene" fallback — just primitives, no custom models).
4. **Explaining the 4 Ds to participants** — a short script/framing facilitators can use verbatim or adapt.

**Acceptance criteria**: a facilitator who has never run this workshop before could execute it start-to-finish using only this document.

### Phase 4 — Student cheat sheet
Write `docs/student-cheatsheet.md`: a single-page (print-friendly) quick reference covering the primitives and attributes actually used in the starter template — `a-box`, `a-sphere`, `a-plane`, `a-sky`, `a-light`, `a-entity` with `gltf-model`, and the `position` / `rotation` / `scale` / `color` attribute syntax with one example line each. Keep it to what's needed for this workshop, not a full A-Frame reference — link to the official A-Frame docs for anything beyond that.

**Acceptance criteria**: fits on one printed page; every entry has a copy-pasteable example line.

### Phase 5 — Deployment guide
Write `docs/deployment.md` covering, in order of preference: forking on Glitch (primary path — include exact steps and why it satisfies the HTTPS requirement for free), CodeSandbox as an alternative, GitHub Pages as a "publish your finished scene permanently" option post-workshop, and a local-fallback path (e.g. a one-line `npx serve` or Python `http.server` instruction) for venues where hosted editors are blocked — with an explicit note that VR mode may not work over plain `http://` on `file://`, only over `localhost` or HTTPS.

**Acceptance criteria**: someone with no deployment experience can get the starter template live and shareable using only this doc, via at least two of the documented paths.

### Phase 6 — Example finished scene
Build `example-scene/index.html`: a small, polished scene built from the starter template plus 3-5 asset-kit items, demonstrating a clear mood/theme. This is what facilitators show at minute zero as "here's what you'll build toward." Write `example-scene/README.md` explaining which primitives/assets it uses and why, so a facilitator can narrate it live.

**Acceptance criteria**: visibly more polished than the bare starter template, but built entirely from documented asset-kit items and starter-template primitives — nothing a participant couldn't also do in the build-time window.

### Phase 7 — QA pass and README polish
Verify: every internal link in every doc resolves; `manifest.json` entries match actual files in `models/`/`skyboxes/` (or are clearly flagged as pending downloads); the starter template and example scene both render and enter VR mode correctly when served over HTTPS; README's quick-start link points at the real forkable project. Fill in any placeholder text left from earlier phases. Record any open issues in `docs/decisions.md` rather than leaving them silently unresolved.

---

## Licensing & attribution rules

- Repo license: MIT.
- Every third-party asset (model, texture, skybox image) requires a corresponding entry in `asset-kit/ATTRIBUTION.md` with source URL and license. CC0 preferred; CC-BY acceptable only if the required credit text is captured verbatim.
- Never bundle an asset whose license is unclear or unverifiable — document it as a pending decision instead of guessing.

## Definition of done

A contributor with no prior context can: clone the repo, read the README, fork `starter-template` on Glitch, and have a working, VR-mode-capable A-Frame scene live in under a minute — with `docs/facilitator-guide.md` sufficient to run the full 2-hour workshop unassisted.

## Future / stretch phases (do not build now — record as issues instead)

- AI-assisted asset generation as an optional "Delegation" extension for longer workshop formats.
- Multiplayer/shared-scene support for group builds.
- A branded/skinnable version of the example scene for institutional demos.

Flag these as GitHub issues in Phase 0 rather than building them — keep the initial repo scoped to the 2-hour single-participant workshop.
