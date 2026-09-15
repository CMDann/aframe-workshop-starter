# Contributing

Thanks for helping improve this workshop framework. It's built to be forked and adapted, so the most valuable contributions are usually the ones that make it easier for *someone else* to run the session cold.

## The constraints that are load-bearing

These aren't style preferences — the workshop stops working without them. Please don't change them without opening an issue first:

1. **A-Frame, not Three.js or the raw WebXR API.** The declarative HTML entity-component syntax is the pedagogical point. It's what makes this teachable in two hours to people who've never written code.
2. **Zero local install.** No build step, no npm install, no bundler. A-Frame loads from a CDN in `<head>`; everything else lives in one `index.html` a participant can read top to bottom.
3. **HTTPS-servable by default.** WebXR's VR-mode entry point requires a secure context or `localhost`. This is *why* Glitch and GitHub Pages are the documented paths — a `file://`-only setup silently loses the VR button. If you propose a simpler local flow, flag that tradeoff in the docs.
4. **Finished in the room.** Every change should optimize for "participant has a working, personalized, shareable scene by minute 120" — not for covering more A-Frame features.
5. **Pin the A-Frame version.** Use an exact release URL, never `latest`. An upstream release mid-workshop is a failure mode no facilitator can debug live.

## Contributing to the asset kit

Assets are the area most likely to cause legal problems, so the bar is strict.

**First-party assets.** The PIZZA.EXE models, concept art and world bible are original works under [`asset-kit/LICENSE-ASSETS.md`](asset-kit/LICENSE-ASSETS.md) — free for workshop use, all other rights reserved. They are not CC0 and must not be relicensed, redistributed standalone, or used in other projects.

**Third-party assets** you contribute must clear this bar:

- **CC0 preferred. CC-BY acceptable** only if the required credit text is captured verbatim.
- **Never add an asset whose license is unclear or unverifiable.** If you can't point at the license, document it as a pending decision in `docs/decisions.md` instead of guessing.
- **Every asset needs a line in `asset-kit/ATTRIBUTION.md`** — source URL, license, and any required credit. No exceptions.
- **Add a matching entry in `asset-kit/manifest.json`**, with `tags` (models) or `mood_tags` (skyboxes) meaningful enough that a facilitator can say "if your theme is X, look at these" without opening every file.
- **Keep files small.** Models should be `.glb`. Skyboxes should be equirectangular JPGs at 2048x1024 or smaller — a workshop runs on venue wifi, and a 17 MB sky is a dead scene.

## Testing a change

There's no test suite. Verify by actually loading the scene:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/starter-template/`. Check that:

- Geometry renders and the sky, ground, and primitives are all visible.
- The browser console is free of errors.
- Mouse-drag looks around and WASD moves the camera.
- The **VR-mode button appears bottom-right.** If it's missing, you're not on a secure context — this is exactly the failure the HTTPS constraint exists to prevent.

If you changed a doc — or edited `starter-template/index.html`, which the slides and landing page link into by line number — run the link checker:

```bash
python3 tools/check-links.py
```

It resolves every relative markdown link and verifies that each GitHub line-range link still spans the code it claims to. The second check matters: editing the template silently redirects those links without anything appearing broken.

More detail in [docs/process/contributing-workflow.md](docs/process/contributing-workflow.md).

## Documentation style

Write for a stranger with no context — that's who reads this first. Facilitator docs should be executable by someone who has never run the session; student-facing docs assume zero WebXR experience and should stay free of jargon that isn't defined on the spot.

## Reporting problems from a real session

The most useful issue you can file is "here's where my participants got stuck." Workshop failure modes are hard to predict from the outside, and `docs/facilitator-guide.md` has a "common failure points" section that grows from exactly this kind of report.
