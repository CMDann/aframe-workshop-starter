# 6. Interactivity

Everything so far has been a scene you look at. This is how it starts responding.

## The cursor

The small ring in the centre of your view is `<a-cursor>`, and it's the reason interaction works the same with a mouse and in a headset. It sits inside the camera:

```html
<a-entity camera look-controls wasd-controls>
  <a-cursor></a-cursor>
</a-entity>
```

It casts a ray straight ahead. Whatever that ray hits is what you're pointing at — with a mouse, you click; in a headset with no controller, you look at something and it activates. Same code either way.

## Click events

Any entity can respond to being clicked:

```html
<a-box id="lamp" position="0 1 -3" color="#333"></a-box>

<script>
  document.querySelector('#lamp').addEventListener('click', function () {
    this.setAttribute('color', '#FFD700');
  });
</script>
```

`click` fires from a mouse click *and* from a cursor activation in VR. `mouseenter` and `mouseleave` also fire when the cursor moves on and off an entity, which is how you build hover states.

## Making a whole scene respond

Attach to many entities at once rather than one at a time:

```html
<script>
  document.querySelectorAll('.clickable').forEach(function (el) {
    el.addEventListener('click', function () {
      this.setAttribute('visible', false);
    });
  });
</script>
```

```html
<a-box class="clickable" ...></a-box>
<a-sphere class="clickable" ...></a-sphere>
```

If you have many entities, tell the cursor which ones matter — it's a real performance win, and it silences a console warning you'll otherwise see:

```html
<a-cursor raycaster="objects: .clickable"></a-cursor>
```

## Animation

The built-in `animation` component needs no JavaScript at all:

```html
<a-box animation="property: rotation; to: 0 360 0; loop: true; dur: 4000"></a-box>
```

- **`property`** — what to animate (`position`, `rotation`, `scale`, `material.color`…)
- **`to`** — the target value
- **`dur`** — duration in milliseconds
- **`loop`** — `true`, or a number of repeats
- **`dir`** — `alternate` to ping-pong back and forth
- **`easing`** — `easeInOutQuad` and friends

Animate on an event instead of immediately with `startEvents`:

```html
<a-box
  class="clickable"
  animation="property: scale; to: 1.4 1.4 1.4; dur: 200; startEvents: click"></a-box>
```

Multiple animations on one entity need distinct names — `animation__spin`, `animation__float`:

```html
<a-sphere
  animation__float="property: position; to: 0 2 -4; dir: alternate; loop: true; dur: 2000"
  animation__spin="property: rotation; to: 0 360 0; loop: true; dur: 6000"></a-sphere>
```

A slow float or drift is one of the cheapest ways to make a static scene feel alive — well within reach as a workshop stretch goal.

## Sound

```html
<a-scene>
  <a-assets>
    <audio id="hum" src="sounds/hum.mp3" preload="auto"></audio>
  </a-assets>

  <a-entity sound="src: #hum; autoplay: true; loop: true; positional: true"
            position="2 1 -3"></a-entity>
</a-scene>
```

`positional: true` is the interesting part: the sound gets quieter as you walk away and shifts between your ears as you turn. It's a strong atmosphere tool for very little code.

Browsers block autoplaying audio until the user interacts with the page — so a sound set to autoplay often starts only after the first click. That's a browser policy, not a bug in the scene.

## Writing your own component

When you want behaviour that doesn't exist, register a component. It then works as an attribute like any built-in:

```html
<script>
  AFRAME.registerComponent('spin-on-click', {
    init: function () {
      this.el.addEventListener('click', () => {
        this.el.setAttribute('animation', {
          property: 'rotation', to: '0 360 0', dur: 800
        });
      });
    }
  });
</script>

<a-box spin-on-click></a-box>
```

This is the doorway from "using A-Frame" to "extending it," and the point where the entity-component model from [Concepts](01-concepts.md) starts paying off properly.

---

Next: [VR & devices →](07-vr-and-devices.md)
