# 4. Lighting & materials

Lighting is the highest-leverage thing you can change for mood, and it contains the one piece of A-Frame behaviour that surprises nearly everybody.

## The surprise: your defaults disappear

A-Frame gives every scene default lighting for free — an ambient light plus a directional one. That's why a brand-new scene with no `<a-light>` in it looks fine.

**The moment you add a single `<a-light>` of your own, those defaults switch off.** Your light becomes the only light in the scene.

So the classic first move — "I'll add one light to brighten things up" — very often makes the scene *darker* or flatter than it was before. Nothing is broken; you've just replaced two lights with one.

The fix is to think in pairs.

## The pairing that works

```html
<a-light type="ambient"     color="#FFFFFF" intensity="0.4"></a-light>
<a-light type="directional" color="#FFFFFF" intensity="0.8" position="-1 2 1"></a-light>
```

This is what the [starter template](../../starter-template/index.html) ships with, and it's a good default for almost any scene.

**Ambient** is soft light arriving from every direction at once. It's the safety net: it guarantees nothing is lost in total blackness. On its own it looks completely flat, because every face of every object receives exactly the same light — a cube lit only by ambient light reads as a plain hexagon.

**Directional** acts like the sun: parallel rays from one direction, so objects get a lit side and a shadowed side. This is what makes geometry look solid.

Try it yourself: set the directional light's `intensity` to `0` and reload. Everything flattens. That difference is the whole argument for using two.

## Light types

| Type | Behaves like | Use for |
|---|---|---|
| `ambient` | Light from everywhere | Base fill so nothing goes black |
| `directional` | The sun | Main light, shape and shadow |
| `point` | A bare bulb | Lamps, fires, anything glowing in place |
| `spot` | A torch or stage light | Pools of light, drama, focus |
| `hemisphere` | Sky above, ground below | Soft outdoor light with colour from both |

`ambient` and `hemisphere` ignore `position` — they have no location. The others use it.

## Intensity and colour set the mood

Two dials do most of the work:

```html
intensity="0.2"  <!-- barely there -->
intensity="1.0"  <!-- normal -->
intensity="2.0"  <!-- blown out, harsh -->
```

Colour tints everything the light touches, which is the fastest route to atmosphere:

| Feeling | Ambient | Directional |
|---|---|---|
| Overcast afternoon | `#FFFFFF` @ 0.8 | `#FFFFFF` @ 0.4 |
| Warm sunset | `#FFD9B3` @ 0.4 | `#FF9E5E` @ 0.9 |
| Moonlight | `#8FA9D9` @ 0.2 | `#C5D4FF` @ 0.6 |
| Underwater | `#2E6B7A` @ 0.5 | `#7FD4E8` @ 0.5 |
| Something wrong | `#3A1F3D` @ 0.15 | `#FF3B3B` @ 0.7 |

A warm key light against a cool ambient — or the reverse — reads as far more considered than a single white light, and costs nothing.

## Materials

`color` is the shorthand you'll use most, but it's really the `material` component underneath:

```html
<a-box color="#4CC3D9"></a-box>
<a-box material="color: #4CC3D9; roughness: 0.2; metalness: 0.8"></a-box>
```

Useful properties:

- **`roughness`** (0–1) — 0 is mirror-smooth, 1 is completely matte. Default 0.5.
- **`metalness`** (0–1) — how metallic the surface reads. Default 0.
- **`opacity`** (0–1) — needs `transparent: true` to take effect.
- **`src`** — a texture image instead of a flat colour.
- **`side`** — `front` (default), `back`, or `double`. A plane viewed from behind is invisible until this is `double`.

```html
<a-plane material="src: wood.jpg; repeat: 4 4"></a-plane>
```

`repeat` tiles the texture, which keeps a small image sharp across a large floor.

## `flat` shading

Sometimes you want something to ignore lighting entirely — a UI panel, a sky, a stylised object that should always read the same:

```html
<a-box material="shader: flat; color: #FF00AA"></a-box>
```

Flat-shaded objects are unaffected by every light in the scene. Handy, and occasionally the explanation for "why won't this thing get darker."

---

Next: [Models →](05-models.md)
