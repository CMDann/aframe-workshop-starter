# How this was built

A record of the process, kept because the workshop is partly *about* delegation — and this repo was itself built by delegating to an agent working from a written specification. If you're forking this to run your own version, the useful takeaway is the verification habit, not the tooling.

## The shape of it

The repo was built from a specification ([`CLAUDE.md`](../../CLAUDE.md) in the root) that defines the pedagogical model, the non-negotiable constraints, and a sequence of numbered build phases with acceptance criteria. Each phase had to satisfy its criteria before the next one started.

| Phase | Output | Status |
|---|---|---|
| 0 | Repo scaffold — README, licence, contributing, structure | Done |
| 1 | Starter template | Done |
| 2 | Asset kit + attribution | Pending |
| 3 | Facilitator guide | Done |
| 4 | Student cheat sheet | Pending |
| 5 | Deployment guide | Partial |
| 6 | Example finished scene | Pending |
| 7 | QA pass and README polish | Pending |

Phases 3 and parts of 5 were written before the scaffold existed, which is why the numbering isn't strictly chronological.

## The specification came first, and then lost an argument

Writing the constraints down before building anything was what kept the result coherent — A-Frame over Three.js, zero install, HTTPS by default, single-file scenes, "finished in the room." Those are all decisions that are cheap up front and expensive to reverse halfway.

But a specification written in advance is a prediction, and predictions are sometimes wrong. Two were:

**Lighting.** The spec asked for exactly one `<a-light>` in the starter template. Built that way and looked at it, the scene was visibly flat — A-Frame switches off its default lighting the moment a scene declares any light of its own, so one ambient light really is the only light, and every face of every object receives identical illumination. The example cube rendered as a plain hexagon.

Testing it side by side settled it: the template ships an ambient **and** a directional light. That cost one line and made the difference between a scene that looks solid and one that doesn't — which matters, because the opening demo is projected in front of a room. The spec was amended to match rather than quietly ignored.

**Asset sourcing.** The spec framed the Discernment step as choosing from a curated kit *instead of* searching the open web. The student-facing docs had already moved past that, allowing self-sourced assets under a hard 10-minute cap and a CC0/CC-BY-only rule. The docs won: banning search outright is unenforceable and students will do it anyway, whereas a time cap plus a licence rule handles the actual risks — asset hunting eating the build hour, and unlicensed work ending up in a publicly-published scene.

Both are recorded in [decisions.md](../decisions.md) with the reasoning, which is the point: a deviation that's written down is a decision, and one that isn't is just drift.

## Verification, not assertion

The rule throughout was that nothing counts as done because it looks right in the source. The starter template was checked by actually running it:

- Served over a local HTTP server and loaded in a browser
- Confirmed A-Frame 1.8.0 loaded, the scene reported `hasLoaded`, and the console was free of errors
- Confirmed the VR button was present **and visible**, and that `isSecureContext` was true
- Drove `wasd-controls` and confirmed the camera moved forward; drove `look-controls` with a real drag and confirmed yaw and pitch changed to finite values
- Changed a colour value, reloaded, and confirmed the scene updated — the exact interaction the workshop's tour block depends on

That last one matters more than it sounds. The 0:10–0:25 block is built around live-editing a value in front of the room. If that loop were broken, the session's spine would break with it.

One detail worth recording: an early attempt to test the controls by calling `look-controls` handlers directly with hand-built event objects produced `NaN` rotations. That was the *test* being wrong, not the scene — synthetic events were missing fields the component needs to compute a delta. A real drag produced correct finite values. Worth knowing, because a bad test that looks like a real failure will send you rewriting working code.

## External facts were checked, not assumed

Version numbers and URLs rot, and guessing them produces documentation that's confidently wrong:

- A-Frame **1.8.0** confirmed current and its CDN URL confirmed reachable before pinning it
- reveal.js pinned to **5.1.0**, not the newer 6.0.2, because 6.x doesn't publish its plugins to cdnjs — `plugin/notes` and `plugin/highlight` both 404, and the deck needs speaker notes and syntax highlighting
- Poly Haven's API checked directly: their CC0 skies are available, but the tonemapped JPG exports run to roughly 17 MB each and need downscaling before they're usable on venue wifi
- Poly Pizza's API found to require a key, so it can't be bulk-fetched into the kit — it stays a recommendation for students sourcing their own

## Publishing

GitHub Pages serves from the repository root on `main`. That choice does more than host the presentation: it puts the starter template, the example scene, and the asset kit on **HTTPS**, which is what makes the VR button work. Before it, the only hosted path was Glitch.

The cost is a root `index.html`, which the spec's layout didn't include. Recorded in [decisions.md](../decisions.md).

## What's still open

Tracked in [decisions.md](../decisions.md) rather than left implicit — the asset kit binaries, the example scene, the cheat sheet, and a real screenshot for the README. Anything that couldn't be resolved was written down as an open item rather than quietly skipped.

---

See also: [architecture](architecture.md) · [contributing workflow](contributing-workflow.md)
