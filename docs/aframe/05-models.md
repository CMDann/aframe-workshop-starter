# 5. Models

Primitives get you a long way, but a real prop — a lantern, a chair, a tree — usually comes from a model file.

## Use `.glb`

glTF is the web's 3D format, and **`.glb`** is its single-file binary flavour: geometry, materials, and textures all in one file. That one-file property matters a lot in a workshop, because there's nothing to go missing.

```html
<a-entity gltf-model="models/lantern.glb" position="0 0 -4"></a-entity>
```

`.gltf` also works but usually arrives as a folder of separate files that all have to be uploaded together. Prefer `.glb` unless you have a reason not to.

Formats that are **not** directly usable: `.fbx`, `.obj`, `.blend`, `.max`, `.dae`. They need converting first — Blender will import most of them and export `.glb`.

## Where to get them

| Source | Licence | Notes |
|---|---|---|
| [Poly Pizza](https://poly.pizza) | Mostly CC0 | Large low-poly library, direct `.glb` downloads |
| [Khronos glTF Sample Assets](https://github.com/KhronosGroup/glTF-Sample-Assets) | Documented per model | Reliable, licence stated for each |
| [Sketchfab](https://sketchfab.com) | Varies — **filter carefully** | Filter to downloadable + CC licence |
| [Poly Haven](https://polyhaven.com) | CC0 | Excellent for skies and textures |

Two rules if you're sourcing your own:

1. **You need the actual file.** A link to a viewer page is not a model. If you can't download a `.glb`, you can't use it.
2. **The licence must be clear.** CC0 is safest. CC-BY is fine if you credit properly. Anything unclear — skip it. This matters more than usual because workshop scenes get published publicly.

## Scale is the first thing to fix

Models are almost never the size you expect. Exporters disagree about units, so a chair can arrive 100 metres tall or 2 centimetres wide. This is normal, not a mistake.

```html
<a-entity gltf-model="models/chair.glb" scale="0.01 0.01 0.01"></a-entity>
```

If a model doesn't appear at all, work through this order:

1. **It's enormous** and you're standing inside it. Try `scale="0.01 0.01 0.01"`.
2. **It's microscopic.** Try `scale="100 100 100"`.
3. **It's behind you.** Negative Z is forward — see [Transforms](03-transforms.md).
4. **It didn't load.** Check the console.

## Loading takes time

Models load asynchronously. For anything beyond a couple of small props, preload them in `<a-assets>` so the scene waits rather than popping things in mid-look:

```html
<a-scene>
  <a-assets>
    <a-asset-item id="lantern" src="models/lantern.glb"></a-asset-item>
  </a-assets>

  <a-entity gltf-model="#lantern" position="0 0 -4"></a-entity>
</a-scene>
```

The `#id` reference means the file is fetched once even if you place it twenty times.

## Paths and CORS

The most common loading failure is a path problem, and the second most common is CORS.

**Paths** are relative to the HTML file. From `starter-template/index.html`, a model in the shared kit is `../asset-kit/models/lantern.glb`.

**CORS** blocks a browser from loading a file from another domain unless that server explicitly allows it. In practice:

- **Same project** (uploaded into your Glitch project, or sitting next to your HTML) — always works. Easiest path by far.
- **GitHub Pages** — works; it sends permissive headers. The asset kit in this repo is served this way.
- **Random image or model URL found on the web** — usually blocked. A link that opens fine in a browser tab can still fail to load into a scene.

If the console says something about CORS or `Access-Control-Allow-Origin`, the fix is to host a copy yourself, not to keep retrying the link.

## Performance

A workshop scene runs on laptops and phones, and a headset has to render everything twice at 72–90fps. Rough guidance:

- Prefer low-poly. Stylised reads better than detailed at this scale anyway.
- Watch total download size. Ten 5 MB models is a scene nobody waits for.
- Reuse the same model rather than loading ten similar ones.
- Large textures cost more than polygons. 1024×1024 is plenty for a prop.

## Animated models

glTF can carry animations. A-Frame doesn't play them by default — that needs the `animation-mixer` component, which ships separately as part of [aframe-extras](https://github.com/c-frame/aframe-extras). Beyond the scope of the workshop, but worth knowing it exists.

---

Next: [Interactivity →](06-interactivity.md)
