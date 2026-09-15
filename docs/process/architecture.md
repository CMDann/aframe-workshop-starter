# Architecture

What's in this repo, how the pieces relate, and why the constraints are what they are.

## Layout

```
/
├── index.html              Landing site (GitHub Pages root)
├── slides/                 Facilitator deck (reveal.js)
├── site/                   Shared CSS for the site and deck
├── starter-template/       The scene participants fork and edit
├── example-scene/          Finished demo, shown at minute zero
├── asset-kit/              Curated CC0 models and skyboxes + manifest
├── docs/                   All documentation (this folder included)
├── tools/                  Maintenance scripts
├── CLAUDE.md               The build specification
└── .nojekyll               Tells Pages to serve files verbatim
```

## The three audiences

Almost every file serves exactly one of them, and knowing which keeps the writing honest:

| Audience | Reads | Assumes |
|---|---|---|
| **Participant** | `starter-template/`, `docs/student-cheatsheet.md`, `docs/assignment.md`, the landing site | Nothing. No coding, no 3D, no WebXR. |
| **Facilitator** | `docs/facilitator-guide.md`, `slides/`, `example-scene/README.md` | Can run a session; not necessarily any A-Frame. |
| **Contributor** | `CONTRIBUTING.md`, `docs/process/`, `CLAUDE.md` | Comfortable in a repo. |

A document that tries to serve two of these at once usually serves neither.

## Why GitHub Pages serves from the root

Publishing the repository root does two jobs at once:

1. The presentation is at `/` and the deck at `/slides/`.
2. **The scenes and the asset kit end up on HTTPS.** `/starter-template/` is a live, VR-capable URL, and `/asset-kit/models/…` can be referenced from a student's Glitch project.

That second point is the load-bearing one. WebXR's VR entry requires a secure context, so a hosted HTTPS copy isn't a convenience — it's the difference between a working VR button and a missing one.

The cost is a root `index.html`, which the original specification's layout didn't include.

## The constraints, and what they're protecting

These are in [`CONTRIBUTING.md`](../../CONTRIBUTING.md) as rules. Here's the reasoning:

**A-Frame, not Three.js or raw WebXR.** The declarative entity-component syntax is the pedagogical point — describing a scene and coding it become the same act. Three.js is more capable and completely unteachable in two hours to people who've never written code.

**Zero install.** Every minute spent on npm, Node versions, or a build tool is a minute not spent building a scene — and it's the point where a fraction of any room drops out for environmental reasons nobody can debug live. A CDN script tag has no such failure mode.

**Single-file scenes.** A participant can read the whole thing top to bottom. Splitting it into partials would be better engineering and worse teaching.

**HTTPS by default.** See above. This is why Glitch and Pages are documented ahead of local files, and why a contributor "simplifying" to a `file://` workflow has to flag the tradeoff.

**Pinned versions, never `latest`.** A-Frame is pinned at 1.8.0 and reveal.js at 5.1.0. An upstream release mid-session is a failure no facilitator can diagnose in front of a room. Bumping a pin is a deliberate act with a re-test attached.

**Finished in the room.** Every scoping decision resolves toward "participant has a working, personalised, shareable scene by minute 120" rather than "participant has seen more A-Frame features."

## How the presentation and the code stay connected

The deck and landing page link into specific line ranges of `starter-template/index.html` on GitHub, so a facilitator can jump from a slide to the real source.

Line-range links rot the moment the file is edited. [`tools/check-links.py`](../../tools/check-links.py) exists for exactly this: it resolves every relative markdown link, and checks that each GitHub line range still spans the content it's supposed to. Run it before pushing.

## Documentation layout

`docs/` has one front door ([README.md](../README.md)) and two subfolders:

- **`docs/aframe/`** — teaching material about A-Frame itself, useful independently of this workshop.
- **`docs/process/`** — how the repo was built and how to work on it.

Workshop-delivery docs stay at `docs/` root, because that's what a facilitator reaches for first.

---

See also: [how this was built](how-this-was-built.md) · [contributing workflow](contributing-workflow.md)
