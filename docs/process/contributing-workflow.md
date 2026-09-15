# Contributing workflow

Practical mechanics. The rules about *what* is acceptable to contribute are in [`CONTRIBUTING.md`](../../CONTRIBUTING.md); this is about how to work on the repo day to day.

## Commit cadence

Commit at each completed unit rather than batching a session's work into one change. A commit should leave the repo in a working state and carry a message explaining *why*, not just what — the diff already says what.

Messages that have earned their place here look like:

> Ships two lights rather than the one the spec called for. Tested both: ambient-only renders every face identically, so the example cube reads as a flat hexagon…

Someone reading that in a year knows why the file looks the way it does and what would have to change for the decision to be revisited.

## Before every push

```bash
python3 tools/check-links.py
```

It does two things:

1. Resolves every relative link in every markdown file.
2. Checks that each GitHub line-range link still spans the content it claims to.

The second is the one that matters. The slide deck and landing page link to specific lines of `starter-template/index.html` — edit that file and every one of those links quietly starts pointing somewhere else. Nothing visibly breaks, which is exactly why it needs a check.

If it reports a drifted anchor, update the line numbers in the offending file.

## Testing a scene change

There's no test suite; verify by running it.

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/starter-template/` and confirm:

- Geometry renders — sky, ground, and primitives all visible
- The console is free of errors
- Mouse-drag looks around; WASD moves
- **The VR button appears bottom-right**

That last one is the canary. If it's missing you're not on a secure context — which also means you're not testing what participants will actually experience.

Use a server rather than double-clicking the file. `file://` renders the scene but silently loses VR and may block model loading.

## Testing the site or deck

Same server, from the repo root:

- `http://localhost:8000/` — landing page. Check at a narrow width too; it must not scroll horizontally.
- `http://localhost:8000/slides/` — the deck. Press <kbd>S</kbd> for speaker view and confirm notes appear.

Both follow the viewer's colour scheme except the deck, which is always dark because it's projected.

## Changing the run of show

The schedule lives in two places: [`docs/facilitator-guide.md`](../facilitator-guide.md) and the clock chips in `slides/index.html`. **Change both.** A deck disagreeing with the guide about what happens at 0:35 is worse than either being slightly wrong.

## Adding to the asset kit

Covered in [`CONTRIBUTING.md`](../../CONTRIBUTING.md). The short version: CC0 or clearly-licensed CC-BY only, a row in `asset-kit/ATTRIBUTION.md` without exception, a matching entry in `manifest.json`, `.glb` for models, and skyboxes downscaled to 2048×1024 or smaller.

## Bumping a pinned version

A-Frame (1.8.0) and reveal.js (5.1.0) are both pinned deliberately. To bump either:

1. Change the version in one place and load the affected pages.
2. Run through the scene checks above in full.
3. For reveal, confirm the plugins still resolve on cdnjs at the new version — they were the reason 6.x was rejected.
4. Note the bump and the re-test in [`docs/decisions.md`](../decisions.md).

Never switch a pin to a floating `latest`.

## Filing what you can't fix

If something can't be resolved, write it into [`docs/decisions.md`](../decisions.md) as an open item, or open an issue. The one thing not to do is leave it silently unresolved — an undocumented gap costs the next person far more than an acknowledged one.

---

See also: [architecture](architecture.md) · [how this was built](how-this-was-built.md)
