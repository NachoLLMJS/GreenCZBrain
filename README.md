# GreenCZBrain — BNB $2,000 green-rush simulation

This project is a separate rebrand of the preserved ZBRAIN reference. The untouched source reference remains in `reference-original.html`.

## Open locally

Run from this folder:

```bash
python serve.py
```

Then open:

http://127.0.0.1:4175/

## Files

- `index.html` — active GreenCZBrain experience with the looping BNB chart and Three.js green-rush scene.
- `assets/brand/` — GreenCZBrain logo, web icon and favicon in a green/BNB-yellow palette.
- `reference-original.html` — untouched downloaded reference; keep it for exact comparisons.
- `editable/overrides.css` — safest place for initial visual changes.
- `assets/vendor/` — local copies of Three.js, GSAP, and the web fonts, so the visual experience does not depend on those CDNs.
- `serve.py` — local static server with explicit JavaScript/CSS/font MIME types.

## Important

The BNB chart is an explicit visual simulation, not a live price feed or price prediction. The loop rises to $2,000, turns the brain and background green for four seconds, and resets.
