# 3. Transforms

Three attributes place everything in the scene. They work identically on every entity, primitive or not.

```html
position="X Y Z"    where it is        (metres)
rotation="X Y Z"    how it's turned    (degrees)
scale="X Y Z"       how big            (1 = unchanged)
```

All three take three space-separated numbers. All three default to sensible values (`0 0 0`, `0 0 0`, `1 1 1`), so you only write the ones you're changing.

## The coordinate system

| Axis | Direction | Positive is |
|---|---|---|
| **X** | left ↔ right | right |
| **Y** | down ↕ up | up |
| **Z** | back ↔ forward | **towards you** |

Y being up is intuitive. X being right is intuitive. Z is where everyone stumbles.

## Negative Z is forward

You start at `0 0 0` looking down the **negative** Z axis. So anything you want to see goes at a negative Z:

```html
<a-box position="0 1 -3"></a-box>   <!-- 3 metres in front of you. Visible. -->
<a-box position="0 1 3"></a-box>    <!-- 3 metres BEHIND you. Turn around. -->
```

When someone says "I added a box and nothing happened," this is the reason about nine times out of ten. The box is there, perfectly fine, behind their head.

If a scene looks empty, turn around before you start debugging.

## Units are real

Positions and sizes are in **metres**, and A-Frame means it. The default camera sits at 1.6m — roughly human eye height. This is worth taking seriously, because a scene built at the wrong scale feels deeply wrong in a headset even when it looks fine on a monitor.

Useful reference points: a doorway is about 2m tall, a table about 0.75m, a coffee mug about 0.1m.

## Rotation is in degrees

Degrees, not radians — a small kindness A-Frame does you. Rotation is applied around each axis:

```html
rotation="0 45 0"     <!-- turned 45° to the left, standing upright -->
rotation="-90 0 0"    <!-- tipped face-up: the standard floor plane -->
rotation="0 0 45"     <!-- rolled 45° like a tilted picture frame -->
```

Y-axis rotation (turning on the spot) is the one you'll use most.

## Scale multiplies

Scale is a multiplier on whatever size the object already had:

```html
scale="1 2 1"     <!-- normal width, DOUBLE height, normal depth -->
scale="0.5 0.5 0.5" <!-- half size in every direction -->
```

For primitives you usually set real dimensions (`width`, `radius`, `height`) instead — it's clearer. Scale earns its place with **models**, where you have no control over the size the file was exported at. See [Models](05-models.md).

A scale of `0` makes something vanish, and negative scale mirrors it — occasionally useful, more often a typo.

## Positions are relative to the parent

A nested entity's position is measured from its parent, not from the world:

```html
<a-entity position="0 0 -5">          <!-- 5 metres away -->
  <a-box position="0 2 0"></a-box>    <!-- 2 metres above the PARENT -->
</a-entity>                            <!-- world position: 0 2 -5 -->
```

This is what makes grouping useful, and it's how the camera rig works in the starter template.

## Practical advice

- **Move one axis at a time** while you're learning. Change Y, reload, see it rise. Changing all three at once makes it hard to build intuition.
- **Round numbers first.** Place things at `-3`, `0`, `2`, then refine.
- **Sitting on the floor** means Y equals half the height (boxes) or the radius (spheres).
- **If you can't find it**, temporarily give it a `scale="5 5 5"` and a bright colour. Much faster than guessing.

---

Next: [Lighting & materials →](04-lighting-materials.md)
