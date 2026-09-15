# Learning A-Frame

A guide from zero, written for the same audience as the workshop: no prior 3D, game-dev, or WebXR experience assumed. Some HTML familiarity helps but isn't required.

This goes deeper than the [one-page cheat sheet](../student-cheatsheet.md), which is deliberately scoped to what the 2-hour session uses. Read this if you want to keep building after the workshop ends — or if you're a facilitator who wants to answer questions confidently rather than deflecting them.

## Reading order

| # | Page | What it covers |
|---|---|---|
| 1 | [Concepts](01-concepts.md) | The scene graph, entities and components, why declarative HTML |
| 2 | [Primitives](02-primitives.md) | `a-box`, `a-sphere`, `a-cylinder`, `a-plane`, `a-sky`, `a-entity` |
| 3 | [Transforms](03-transforms.md) | Position, rotation, scale — and the negative-Z gotcha |
| 4 | [Lighting & materials](04-lighting-materials.md) | Light types, why your defaults disappeared, colour for mood |
| 5 | [Models](05-models.md) | `gltf-model`, `.glb` files, scaling surprises, CORS |
| 6 | [Interactivity](06-interactivity.md) | Cursor, click and gaze events, animation |
| 7 | [VR & devices](07-vr-and-devices.md) | Entering VR, the secure-context rule, headsets, performance |

Chapters 1–4 cover everything the workshop itself needs. Chapters 5–7 are where to go next.

## Version

Everything here targets **A-Frame 1.8.0**, the version pinned in the [starter template](../../starter-template/index.html). A-Frame is stable across minor versions, but component syntax does occasionally change — if something here disagrees with the [official docs](https://aframe.io/docs/), trust the official docs and please open an issue.

## The single most useful habit

Keep the browser console open while you build. A-Frame reports missing files, malformed attribute values, and model-loading failures there, and almost every "nothing happened" moment has an explanation waiting in it.
