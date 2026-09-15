# Asset Kit

*Not populated yet — this lands in Phase 2.*

A small, curated set of CC0 models and skyboxes participants choose from during the **Discernment** step. The point of a curated kit is that the skill being practiced is judgment about what serves the scene's mood — not open-web asset search, which will eat the entire build window if left unbounded.

Participants may also source their own assets, under the rules in [../docs/assignment.md](../docs/assignment.md): free-to-use only (CC0, or CC-BY with credit), an actual downloadable `.glb`/`.gltf` file rather than a viewer page, and a hard 10-minute cap before falling back to this kit.

## What will be here

| Path | Contents |
|---|---|
| `manifest.json` | Machine-readable index of every asset: id, name, file path, source URL, license, and mood/category tags. |
| `models/` | `.glb` props, roughly 8-12 across a couple of mood categories. |
| `skyboxes/` | Equirectangular JPGs for `<a-sky>`, roughly 4-6, sized 2048x1024 to stay fast on venue wifi. |
| `ATTRIBUTION.md` | Source, license, and required credit text for **every** bundled asset. No exceptions. |

## Planned sources

- **Skyboxes** — [Poly Haven](https://polyhaven.com) (CC0). Their tonemapped JPG exports are full-resolution and far too heavy to ship as-is, so they get downscaled before being committed.
- **Models** — [Khronos glTF-Sample-Assets](https://github.com/KhronosGroup/glTF-Sample-Assets), which carries a per-model license file, plus other CC0 sources as verified.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the bar an asset has to clear to be added here.
