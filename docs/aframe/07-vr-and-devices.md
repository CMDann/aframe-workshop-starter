# 7. VR & devices

## The secure-context rule

**WebXR only enters VR from a secure context: HTTPS, or `localhost`.**

On a plain `file://` page — double-clicking the HTML — the scene still renders and you can still look around with the mouse, but the **VR button will not appear**, and models may fail to load on CORS restrictions.

This is a browser security rule. No scene can opt out of it, and no amount of debugging the markup will bring the button back. It's the single most common "why is this broken" moment, and the answer is always the URL, not the code.

It's also the entire reason this workshop defaults to a hosted editor instead of "just open the file." See [deployment](../deployment.md) for the paths that satisfy it:

| Path | Secure context? | VR button? |
|---|---|---|
| `file:///…/index.html` | No | **No** |
| `http://localhost:8000/` | Yes (localhost exception) | Yes |
| Glitch preview URL | Yes (HTTPS) | Yes |
| GitHub Pages | Yes (HTTPS) | Yes |

## The VR button

`<a-scene>` adds it automatically, bottom-right. If it's missing, work through:

1. **Is the URL HTTPS or localhost?** Almost always this.
2. **Does the browser support WebXR?** Chrome, Edge, and headset browsers do. Safari's support is partial.
3. **Any console errors?** A scene that failed to initialise won't offer VR.

You do not need a headset to build. Everything except actually entering VR works on a laptop, which is why the workshop doesn't require one.

## Devices

**Desktop, no headset.** Drag to look, WASD to move. This is what most people build with.

**Phone.** Look around by physically moving the phone — `look-controls` reads the gyroscope. Dropping a phone into a cardboard viewer gives a genuine stereo VR view.

**Standalone headsets** (Quest and similar). Open the URL in the headset's own browser and press the VR button. Because everything is a URL, sharing a scene with someone in a headset needs no installation at all — arguably WebXR's best trick.

**Tethered headsets.** Work through a desktop browser with WebXR enabled.

## Testing in a headset

If a headset is going round the room:

- Test it against the starter template **before** the session, not during.
- The headset needs to reach the URL — same wifi, or a public URL like Glitch or Pages.
- Type as little as possible in a headset. QR codes or very short links are worth the setup.
- Expect to clean the lenses between people, and expect each person to take a minute to orient.

## Comfort

Motion sickness in VR is real, and it comes mostly from the scene moving in ways the person's body didn't ask for:

- **Never move the camera without user input.** Animating the camera along a path is the fastest way to make someone ill.
- **Keep the horizon level.** Tilting the world is strongly disorienting.
- **Keep the floor at Y=0** and the camera near 1.6m so scale feels right.
- **Nothing should rush at the viewer's face.** Sudden close motion reads as a threat.

## Performance

A headset renders the whole scene twice, once per eye, at 72–90fps. That budget is much tighter than a flat screen:

- Low-poly models, and few of them.
- Textures no larger than needed — 1024×1024 is plenty for a prop.
- Reuse assets via `<a-assets>` rather than loading variants.
- Fewer, simpler lights. Real-time shadows are expensive; leave them off unless they earn their place.
- Test on the weakest device you expect anyone to use.

A scene that runs at 30fps on a laptop will be unpleasant in a headset. If it stutters flat, fix that before putting anyone in VR.

## Where to go next

- [A-Frame documentation](https://aframe.io/docs/1.8.0/introduction/) — the full reference
- [A-Frame examples](https://aframe.io/examples/) — working scenes to pick apart
- [WebXR Device API](https://immersiveweb.dev/) — the standard underneath, for when you want to know what's being delegated on your behalf

---

Back to the [guide index](README.md).
