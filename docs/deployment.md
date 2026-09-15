# Deployment

> **Partial.** CodeSandbox and venue-network troubleshooting still land in Phase 5. Everything below has been tested and is safe to rely on.

## Why hosting matters here

WebXR's VR-mode entry point requires a **secure context**: HTTPS, or `localhost`. On a plain `file://` page the scene still renders and you can still look around with the mouse, but the **VR button will not appear** and models may fail to load on CORS restrictions.

That's the whole reason this workshop defaults to a hosted editor rather than "just open the file." It's a browser security rule, not a preference.

## GitHub Pages (already live)

This repository publishes itself. Pages serves from the root of `main`, so everything in it is available over HTTPS with no setup at all:

| What | URL |
|---|---|
| Workshop site | <https://cmdann.github.io/aframe-workshop-starter/> |
| Starter scene | <https://cmdann.github.io/aframe-workshop-starter/starter-template/> |
| Facilitator slides | <https://cmdann.github.io/aframe-workshop-starter/slides/> |
| Asset kit | `https://cmdann.github.io/aframe-workshop-starter/asset-kit/…` |

Two things this gives you:

- **A demo link that always works**, including the VR button, for showing the workshop to someone before running it.
- **Assets over HTTPS.** Participants can reference kit models and skyboxes by absolute URL from their own Glitch projects rather than re-uploading them. GitHub Pages sends permissive CORS headers, so cross-origin loading works.

**To publish a finished scene this way**, fork this repo (or push your own), then enable Pages under *Settings → Pages* with source `main` / `/ (root)`. Add an empty `.nojekyll` file at the root so your files are served verbatim.

Pages is for *publishing*, not editing — there's no live preview and each change needs a commit. Use Glitch during the session and Pages to make a scene permanent afterwards.

## Glitch (primary path for editing)

1. Open <https://glitch.com/edit/#!/import/github/CMDann/aframe-workshop-starter>. This imports the repo into a fresh Glitch project.
2. Click **Preview** → **Preview in a new window**.
3. Navigate to `/starter-template/` on that preview URL.

You now have a live HTTPS URL that you can share, that reloads as you edit, and that works in a headset's browser. Glitch projects stay live and editable after the session ends.

> **Note:** because this imports the whole repo, the scene sits at `/starter-template/` rather than at the root. See the open item in [decisions.md](decisions.md) — a purpose-built Glitch remix project serving the template at root is a pre-launch improvement.

## Local server (fallback for restrictive networks)

From the repository root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/starter-template/`. `localhost` is a secure context, so the VR button works.

If you have a working Node install, `npx serve` is equivalent — but Python's built-in server has no install step at all, which is what you want when a venue's network is already the problem.

## Still to be written (Phase 5)

- CodeSandbox as a hosted alternative
- GitHub Pages for publishing a finished scene permanently after the workshop
- Getting a headset onto the same network as a local server
