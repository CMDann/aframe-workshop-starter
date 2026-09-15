# 2. Primitives

The building blocks. Everything here is a convenience wrapper around `<a-entity>` (see [Concepts](01-concepts.md)), so anything you learn about one applies to all of them.

## The shapes

### `<a-box>`

```html
<a-box position="-1 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
```

Sized with `width`, `height`, `depth` (all default `1`, in metres). A box sitting on the floor needs its position Y set to **half its height** — the position is the centre of the shape, not its base. A 1-metre box sits at `y="0.5"`.

### `<a-sphere>`

```html
<a-sphere position="0 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>
```

`radius` defaults to `1`. Same rule as the box: a sphere resting on the ground has its Y equal to its radius.

### `<a-cylinder>`

```html
<a-cylinder position="2 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>
```

Good for pillars, cans, tree trunks, and — with a large radius and small height — discs and platforms.

### `<a-plane>`

A flat rectangle. **It stands up like a wall by default**, so making a floor means rotating it flat:

```html
<a-plane rotation="-90 0 0" width="30" height="30" color="#7BC8A4"></a-plane>
```

That `-90` on the X axis is the single most copied line in A-Frame. A plane is one-sided by default — from underneath it's invisible. Add `material="side: double"` if you need to see it from both sides.

### Others worth knowing

`<a-circle>`, `<a-cone>`, `<a-ring>`, `<a-torus>`, and `<a-text>` all exist and follow the same patterns. The [official primitives reference](https://aframe.io/docs/1.8.0/introduction/html-and-primitives.html) has the full list.

## The environment

### `<a-sky>`

A giant sphere painted on the inside, surrounding everything. It does more for mood than anything else in a scene:

```html
<a-sky color="#0B0C1E"></a-sky>                    <!-- flat colour -->
<a-sky src="../asset-kit/skyboxes/dusk.jpg"></a-sky> <!-- panoramic image -->
```

Image skies must be **equirectangular** — a 2:1 panorama that wraps onto a sphere. A normal photo will smear badly. Poly Haven is a good CC0 source; their full-resolution exports are far too heavy for the web, so downscale to around 2048×1024 before using one.

Keep sky images small. A 17 MB sky on venue wifi is a scene that never loads.

### `<a-light>`

Covered properly in [Lighting & materials](04-lighting-materials.md), because there's one behaviour that catches everybody out.

## The generic entity

When no primitive fits — most often for 3D models — use `<a-entity>` and attach components directly:

```html
<a-entity gltf-model="models/lantern.glb" position="0 0 -4" scale="0.5 0.5 0.5"></a-entity>
```

See [Models](05-models.md).

## Grouping

An `<a-entity>` with no components is a perfectly good container, and moving it moves everything inside:

```html
<a-entity id="campsite" position="4 0 -6" rotation="0 30 0">
  <a-box ...></a-box>
  <a-cylinder ...></a-cylinder>
</a-entity>
```

Compose a cluster around the origin where the numbers are easy to reason about, then place the whole group once. Far easier than recalculating every child by hand.

---

Next: [Transforms →](03-transforms.md)
