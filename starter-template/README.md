# Starter Template

The scene participants build from. One file — [`index.html`](index.html) — with no build step, no install, and A-Frame loaded from a CDN. It's commented far more heavily than production code would be, on purpose: during the session this file doubles as the reference, so a participant should be able to answer most of their own questions by reading the file they're already editing.

## What's in it

- An `<a-sky>` (flat colour, with a commented example for swapping in a real panorama)
- Two lights — an ambient for safety and a directional for shape (see note below)
- A ground `<a-plane>`
- Three example primitives: `<a-box>`, `<a-sphere>`, `<a-cylinder>`
- A camera rig with `look-controls`, `wasd-controls`, and an `<a-cursor>`
- A commented-out `gltf-model` entity, ready to point at an asset-kit model

## Getting it running

### Just look at it

It's already live: <https://cmdann.github.io/aframe-workshop-starter/starter-template/>

Served over HTTPS, so the VR button works. Nothing to set up.

### Glitch (recommended for editing)

Import this repo at <https://glitch.com/edit/#!/import/github/CMDann/aframe-workshop-starter>, hit **Preview**, and navigate to `/starter-template/`.

Glitch is the reference path because it gives you free HTTPS. That matters more than it sounds: **the VR-mode button only appears on a secure context** (HTTPS or `localhost`). It's a browser security rule for WebXR, not something a scene can opt out of.

### Locally

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/starter-template/`.

Use a server rather than double-clicking the file. Opening it directly as `file://` will render the scene, but you'll get **no VR button** and models may fail to load on CORS restrictions. `localhost` counts as a secure context, so serving it this way keeps VR working.

Other paths — CodeSandbox, and GitHub Pages for publishing a finished scene permanently — are covered in [../docs/deployment.md](../docs/deployment.md).

## A note on the two lights

A-Frame provides default lighting, but it switches off the moment a scene defines its own `<a-light>`. This template defines two:

```html
<a-light type="ambient" color="#FFFFFF" intensity="0.4"></a-light>
<a-light type="directional" color="#FFFFFF" intensity="0.8" position="-1 2 1"></a-light>
```

Ambient alone renders everything perfectly evenly, which sounds fine but means a cube reads as a flat hexagon — there's no bright side and shadowed side to tell you it's solid. The directional light is what makes geometry look three-dimensional. Shipping only one light produced a visibly worse scene, so the template starts with both, and the comments explain what each is doing so participants can push them around deliberately.

Lighting is the highest-leverage thing a participant can change for mood. It's worth demonstrating during the tour block: set the directional intensity to `0` on the projector and let the room watch the scene go flat.

## Next steps for participants

The task brief, requirements, and asset-sourcing rules are in [../docs/assignment.md](../docs/assignment.md). The one-page syntax reference is [../docs/student-cheatsheet.md](../docs/student-cheatsheet.md).
