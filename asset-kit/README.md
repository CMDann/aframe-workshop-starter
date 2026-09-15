# Asset Kit

Original **PIZZA.EXE** assets for the workshop's **Discernment** step — a curated set with a point of view, rather than a bag of unrelated props. The skill being practised is judgment about what serves your scene's mood, not open-web asset search, which will eat the entire build window if left unbounded.

Art direction lives in [pizza_exe_characters_and_world_bible.md](pizza_exe_characters_and_world_bible.md) and the 32 sheets in [concept/](concept/).

## Licence — read this first

These are **original works, © 2026 Dann Blair**, not third-party CC0 downloads.

**You may** use them in a scene you build during or after a workshop, publish that scene anywhere, and keep it online. Facilitators may fork this repo and teach with them.

**You may not** redistribute the assets on their own, use them in another product or game, or make derivative models for use outside a workshop scene.

Full terms: **[LICENSE-ASSETS.md](LICENSE-ASSETS.md)**. The repository's framework code and docs remain [MIT](../LICENSE) — the licences are deliberately separate.

## What's here

| Path | Contents |
|---|---|
| [`manifest.json`](manifest.json) | Machine-readable index: id, file, dimensions, triangle count, tags, licence. |
| [`preview.html`](preview.html) | Inspection harness — loads any model beside a 1 m grid and a 1.8 m human reference. |
| `models/` | `.glb` assets. |
| `concept/` | Concept art, renders, source textures, and `.blend` sources. |
| [`ATTRIBUTION.md`](ATTRIBUTION.md) | Author and licence for every asset. No exceptions. |
| `skyboxes/` | Equirectangular JPGs for `<a-sky>`. Empty for now. |

## Inspecting an asset

Every model should be checked through the preview harness before it's considered done:

```
preview.html?model=PIZZA_EXE_CRT_diorama.glb
```

[Open it live →](https://cmdann.github.io/aframe-workshop-starter/asset-kit/preview.html?model=PIZZA_EXE_CRT_diorama.glb)

It reads out real dimensions, mesh and material counts, and triangles. Wrong scale is the most common glTF export fault (see [../docs/aframe/05-models.md](../docs/aframe/05-models.md)) and is near-impossible to eyeball without something known-sized standing beside it.

Useful params: `&scale=0.5`, `&spin=0`, `&bg=222233`.

## Using a model in your scene

```html
<a-entity gltf-model="../asset-kit/models/PIZZA_EXE_CRT_diorama.glb"
          position="0 0 -4"></a-entity>
```

The kit is also served over HTTPS with permissive CORS headers, so you can reference it by absolute URL from a Glitch project without re-uploading anything:

```html
<a-entity gltf-model="https://cmdann.github.io/aframe-workshop-starter/asset-kit/models/PIZZA_EXE_CRT_diorama.glb"></a-entity>
```

## Sourcing your own assets instead

Entirely allowed, under the rules in [../docs/assignment.md](../docs/assignment.md): free-to-use only (CC0, or CC-BY with credit), an actual downloadable `.glb`/`.gltf` rather than a viewer page, and a hard 10-minute cap before falling back to this kit.

Third-party assets contributed *into* this kit face a stricter bar — see [../CONTRIBUTING.md](../CONTRIBUTING.md).
