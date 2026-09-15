# Deployment

> **Provisional.** The full version — CodeSandbox, GitHub Pages, and venue-network troubleshooting — lands in Phase 5. The two paths below are written out because they've been tested and you may need them now.

## Why hosting matters here

WebXR's VR-mode entry point requires a **secure context**: HTTPS, or `localhost`. On a plain `file://` page the scene still renders and you can still look around with the mouse, but the **VR button will not appear** and models may fail to load on CORS restrictions.

That's the whole reason this workshop defaults to a hosted editor rather than "just open the file." It's a browser security rule, not a preference.

## Glitch (primary path)

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
