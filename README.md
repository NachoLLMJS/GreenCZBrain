# ZBRAIN — local editable project

The untouched source reference is preserved in `reference-original.html`.

## Open locally

Run from this folder:

```bash
python serve.py
```

Then open:

http://127.0.0.1:4175/

## Files

- `index.html` — active ZBRAIN experience with inline CSS, JavaScript and the Three.js scene.
- `assets/brand/` — generated ZBRAIN character logo, web icon and favicon.
- `reference-original.html` — untouched downloaded reference; keep it for exact comparisons.
- `editable/overrides.css` — safest place for initial visual changes.
- `assets/vendor/` — local copies of Three.js, GSAP, and the web fonts, so the visual experience does not depend on those CDNs.
- `serve.py` — local static server with explicit JavaScript/CSS/font MIME types.

## Important

This is a preserved public compiled/static frontend, not the original component repository. It is nevertheless directly editable because the whole deployed experience is contained in `index.html`.
