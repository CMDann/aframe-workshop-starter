# Facilitator Guide

## Spatial Storytelling: Designing Your First WebXR Scene

This guide is written so someone who has never run this workshop before can execute it start to finish. Read it fully once before the session, then keep the run-of-show table open during it.

---

## Before the session

Do these at least a day ahead, not the morning of:

- [ ] Test the venue wifi against Glitch (or your hosting platform) from a device on that network. Some campus/corporate networks block Glitch or throttle it — find out before you're in the room.
- [ ] Confirm the local-fallback path works (see `docs/deployment.md`) in case wifi fails entirely on the day.
- [ ] If a VR headset will be passed around, test it against the starter template beforehand — confirm the VR-mode button appears and the headset can reach the Glitch URL.
- [ ] Print or link the student cheat sheet (`docs/student-cheatsheet.md`) — have it visible or handed out before build time starts.
- [ ] Open and sanity-check every link in the asset kit (`asset-kit/manifest.json`) — a broken model link mid-session eats build time you don't have.
- [ ] Have `docs/assignment.md` printed or linked alongside the cheat sheet — participants need the requirements and the asset-sourcing rules in front of them before build time starts, not explained verbally once and forgotten.
- [ ] Pre-fork the starter template yourself and confirm it renders and enters VR mode over the URL participants will actually use.
- [ ] Have the example scene (`example-scene/`) loaded and ready for the opening hook.

## What you'll need in the room

- A projector/screen for the opening demo and group walkthrough.
- The starter template fork link, ready to share (QR code or short link works well).
- The asset kit link, shared before build time so no one is searching for it mid-session.
- The student cheat sheet, printed or linked.
- A stopwatch or visible clock — this session is tightly timed and the build block is where time gets lost if you're not watching it.

---

## Run of show (2 hours)

| Time | Block | What happens |
|---|---|---|
| 0:00–0:10 | **Hook** | Open the example scene, view-source it live on the projector. Make the point explicitly: "this whole thing is about 15-30 lines of HTML." The goal is to collapse the intimidation factor before anyone touches a keyboard. |
| 0:10–0:25 | **Tour** | Everyone forks the starter template. Walk through the primitives together (`a-box`, `a-sphere`, `a-plane`, `a-sky`, `a-light`) and the position/rotation/scale/color attributes. Live-edit one value as a group so everyone sees the instant reload before working solo. |
| 0:25–0:35 | **Direction** | Individual, quiet 5-minute prompt: pick a mood, theme, or one-sentence concept for your scene. Don't let this run long — the point is a decision, not a polished idea. |
| 0:35–1:35 | **Build time** | The bulk of the session. Participants work from their Direction, writing entity tags (Description), and sourcing assets (Discernment) — either from the supplied kit or their own find. State the rule up front: **10 minutes max hunting for your own asset**, then fall back to the kit — this is the single biggest time sink in the build block if left unbounded. A-Frame's defaults handle camera/lighting/interaction (Delegation). Circulate — this is where most one-on-one help happens. |
| 1:35–1:50 | **Peer test** | Everyone already has a live URL from their fork. Pair up or small-group and view 2-3 classmates' scenes in-browser (or in the headset, if one's in the room). |
| 1:50–2:00 | **Wrap** | Quick gallery walk or verbal share: "one thing you'd add with more time." Point people to the deployment doc if they want to keep the scene live permanently (GitHub Pages) beyond the workshop. |

**If you're running behind at 1:00 (halfway through build time):** cut scope, not the peer-test block. A scene with three primitives and one asset-kit model is a complete deliverable. The peer-test and wrap are what make it feel finished — don't sacrifice them to squeeze in more build time.

---

## Explaining the 4 Ds to participants

Use this verbatim or adapt it — it's meant to give the session a spine, not to be read robotically:

> "We're going to build this in four moves. First, **Direction** — you decide what mood or story this space has before you write anything. Then **Description** — in A-Frame, writing the code *is* describing the scene; that's not a metaphor, it's literally what the tags do. Then **Discernment** — you'll pick from a curated set of models and skyboxes, and the skill here is choosing what fits your scene, not finding the most stuff. And finally **Delegation** — A-Frame is already handling your camera, your lighting math, your controls. You don't need to write any of that. That's what frees you up to spend the next hour on the part that's actually yours: how the space feels."

---

## Common failure points and fixes

- **Scene renders blank / nothing shows up.** Almost always a typo in the A-Frame script tag or a missing closing tag on `<a-scene>`. Check the browser console first.
- **VR-mode button is missing.** The page isn't being served over HTTPS or localhost — check the URL. This is the #1 reason to stick with Glitch/Pages over a plain local file.
- **A model won't load.** If it's from the asset kit, usually a broken or CORS-blocked path. If it's a self-sourced asset, check the file format (must be `.glb`/`.gltf`) and hosting — a direct link to a page (like a Sketchfab viewer URL) isn't a usable asset link, they need the actual downloadable file, hosted somewhere reachable (uploaded into their Glitch project is easiest).
- **Participant is stuck searching for "the right" asset with 20 minutes of build time gone.** This is the main failure mode of allowing self-sourced assets — enforce the 10-minute cap from the run-of-show and redirect them to the kit. Don't let scene-building time become asset-hunting time.
- **Participant brings in an asset with an unclear or all-rights-reserved license.** Worth a quick heads-up during the tour: self-sourced assets must be free-to-use (CC0 or CC-BY with credit) — Poly Pizza, Sketchfab (filtered to downloadable + CC license), and Poly Haven are safe starting points. This matters more here than in a typical classroom exercise because scenes may get published publicly.
- **Participant is stuck mid-build with 20 minutes left.** Steer them to the "minimum viable scene" fallback: primitives only (box, sphere, plane, sky, light), no custom models. It's still a complete, shareable scene.
- **Glitch is slow or blocked on the venue network.** This is why you tested wifi ahead of time — switch to the local-fallback path documented in `docs/deployment.md` without losing session time to troubleshooting live.

---

## After the session

- Encourage participants to keep their Glitch project (it stays live and editable after the workshop ends) or publish it permanently via GitHub Pages.
- If you're collecting feedback, a two-question ask works well: "what would you add with more time?" and "where did you get stuck?" — the second one is what actually improves the next run of this workshop.
