# UV Filter Atlas

A comprehensive reference compendium of **36 sunscreen UV filters and visible-light photoprotectants**, with absorption spectra, photodegradation kinetics, regulatory status across five major markets, and a Spectrum Builder that estimates SPF / UVA-PF / HEV blockade for arbitrary filter combinations.

Built end-to-end by AI agents (Claude Code) over ~24 commits as a worked example of how a structured multi-agent research pipeline can produce a verifiable, calibrated, factually-grounded artifact — and document its own limits along the way.

## What's in it

The webapp at `webapp/index.html` has 9 sections:

1. **Main Things You Need to Know** — eight FAQ-style cards (sun-band physics, UV biological effects, what SPF measures, chart units, real-world application gap, "physical vs chemical" myth, iron oxides for HEV, photodegradation reality) with expandable long-form for each. Includes an SVG diagram of solar irradiance × erythema action spectrum.
2. **Spectral Coverage Map** — every filter's absorption band as a Gaussian-gradient bar on a piecewise wavelength axis (UV gets 72% width, visible compressed). Iron oxides separated below the UV filters with a note that they're regulated as colorants, not UV filters.
3. **λmax × Photostability Scatter** — log-scale half-life vs peak wavelength. Hover any point for the full spectrum smear bar + uncertainty bracket; corner toggle reveals all 36 spectra at once.
4. **Spectrum Builder** — pick filters via presets (UVMune 400, Skin Aqua, EU broad, US classic, Mineral, Tinted mineral, All-UVB) or manually; concentration sliders per filter; live SPF / UVA-PF / critical-λ / HEV-blockade metrics; switch between cuvette / lab-test / real-world film modes. Source-doc 📄 icons next to UVMune 400 and Skin Aqua presets link to the verified ingredient lists.
5. **Filter Directory** — 36 filter cards with search and category/photostability/region chip filters. Click any card for the detail modal (SVG spectrum, half-life with uncertainty, regulatory grid, literature references with paper + figure links).
6. **Photodegradation Kinetics** — quantitative loss data with primary peer-reviewed citations.
7. **Photostabilization Mechanisms** — eight mechanism cards covering avobenzone-octinoxate incompatibility, octocrylene → benzophenone, Tinosorb S/M, DEHN, Polycrylene, DESM, vehicle effects.
8. **Cross-Cutting Findings** — seven synthesis insights including the avobenzone–octocrylene–benzophenone trilemma and ESIPT as the dominant photostability mechanism.
9. **Methodology & Provenance** — confidence tiers, AI disclosure, links to the source repository, plus seven categorised limitations sections (math, SPF estimator, data sourcing, scope, visualization, real-world translation, regulatory currency).

## Repository layout

```
sunscreen-filters/
├── README.md                 # this file
├── MASTER-SYNTHESIS.md       # consolidated reference doc with comparison tables
├── index.md                  # project dashboard / phase status
├── webapp/
│   ├── index.html            # main atlas page (~225 KB single file, vanilla JS)
│   ├── md.html               # client-side markdown viewer (marked.js via CDN)
│   └── data/
│       └── spectrum-data.json    # 587 (λ, E1%) data points across 36 filters
├── research/
│   ├── uvb-organic/          # 12 claim files + summary + sources
│   │   ├── _summary.md
│   │   ├── sources.md
│   │   └── claims/
│   │       ├── c001-octinoxate.md
│   │       └── ... (11 more)
│   ├── uva-organic/          # 5 claim files (avobenzone, meradimate, DHHB, MBBT, iscotrizinol)
│   ├── broad-spectrum/       # 6 claim files (BEMT, ecamsule, Mexoryl XL/400, TBPT, bisdisulizole)
│   ├── benzophenones/        # 6 claim files (BP-1/3/4/8, mexenone, trolamine salicylate)
│   ├── inorganic/            # 3 claim files (ZnO, TiO2, iron oxides)
│   ├── photostab/            # 8 mechanism files + halflives.md
│   ├── calibration/          # ZnO, TiO2, iron-oxide deep-dives — recalibration to literature mass-extinction values
│   ├── verification/         # adversarial critique + spectra-verification + tail-corrections
│   └── sources/              # per-product source docs (Skin Aqua, UVMune 400)
└── scripts/
    └── build-html-docs.py    # MD→HTML build pipeline (renders all 66 .md files to static .html)
```

Every `.md` file has a pre-rendered `.html` neighbour (via `scripts/build-html-docs.py`) so the project serves cleanly from a static nginx instance.

## How it was built

The project was assembled across roughly 24 commits via Claude Code agents working in parallel where possible. Process highlights:

**Research phase (initial)**: Six parallel deep-research subagents covered the six filter categories (UVB organic, UVA organic, broad-spectrum, benzophenones, inorganic, photostabilization). Each produced 5–10 individual claim files with ~270 peer-reviewed citations across the project. Workflow followed `research-agent-instructions.md` from the workspace conventions, with C1–C5 confidence tiers per numerical claim.

**Verification phase**: An adversarial critique agent spot-checked 10 citations and identified 2 misattributions (Stange 2015 → actually Hanson, Narayanan, Nichols & Bardeen; Hamzavi 2023 → actually D'Ruiz et al.). Both corrected. Three parallel agents verified ε values against primary literature and proposed corrections; ecamsule's ε was corrected from 20,000 (per-arm) to 47,000 (whole molecule, bis-camphor).

**Calibration phase**: Discovered that the early "effective ε" values for inorganics were calibrated for visual comparison with organics, not for physical accuracy. Three parallel deep-dive agents (ZnO, TiO₂, iron oxides) recalibrated against published mass-extinction k(λ) values:

| Filter | Old E1% peak | Recalibrated | Validated against |
|---|---|---|---|
| ZnO | 9,800 | 160 | 9 mineral SPFs (22% mean error) |
| TiO₂ | 12,500 | 600 | 8 mineral SPFs (29% mean error) |
| Iron Oxide Red | 2,200 | 78 | 10 HEV-blockade measurements (2.7 pp mean error) |
| Iron Oxide Yellow | 1,800 | 62 | same |
| Iron Oxide Black | 1,800 | 95 | same |

Each agent fit a concentration-nonlinearity function `f(c) = 1 − α × tanh(max(0, c − c0)/scale)` against real published SPF / HEV-blockade measurements.

**Synthesis phase**: A coordinating agent assembled `MASTER-SYNTHESIS.md` with comparison tables, then iterative polish rounds (UI design, spectrum data extraction, photodegradation tail behavior, action spectrum integration) brought the webapp to its current state.

The full commit log tells this story chronologically — see `git log` for the trail.

## Numerical data summary

- **36 filters** covered (organic + inorganic + iron-oxide pigments + minor camphor)
- **~290 peer-reviewed citations** across the 6 sources.md files (claims, calibration, verification, sources directories)
- **587 (λ, E1%) data points** in `webapp/data/spectrum-data.json` — extracted from primary literature where possible, fitted from manufacturer datasheets where not, parametric fallback only for two C5 cases (Mexenone, BCSA)
- **5 jurisdictions** tracked: FDA (USA), EU Annex VI, Australia TGA, Japan, Korea — plus reef-ban legislation
- **~14 data points / filter** average, with confidence tiers
- **9 SPF validation formulations** (Badger, ThinkSport, Aveeno, industry benchmarks) — model errors 14% – 32%
- **10 HEV-blockade validation points** for iron oxides — model errors 2.7 pp mean
- **2 misattributed citations** found and corrected during the adversarial critique pass
- **0 fabricated DOIs** — every URL was verified during the verification phase

## Known limitations (categorised)

The full list lives in the in-app methodology section. Highlights:

**Math / model**
- Beer-Lambert assumes uniform homogeneous solution; cosmetic films aren't
- Per-filter f(c) double-counts when many organics share the load → US-classic stack predicted SPF ~3× lower than measured
- Linear interpolation between literature points; could miss sub-nm features

**SPF estimator**
- CIE 1987 erythema action spectrum understates UVA-1 sensitivity → mineral sunscreens over-predicted ~10× (math says SPF 500 for 15% ZnO + 5% TiO₂ but real lab measurement is 30–50)
- Display capped at "100+" — clinical SPF testing has a similar practical ceiling

**Data sourcing**
- Mexoryl 400 spectra all trace to L'Oréal sponsor measurements (no independent academic ε determination)
- Mexenone (BP-10) and BCSA (Mexoryl SD): no modern primary spectra; values held by structural analogy (C5)
- Cinoxate, Padimate O: original ε measurement papers not retrieved

**Scope**
- Some Korea- and China-only modern filters not included
- Photostabilizer interactions not factored into SPF math
- Filter interactions with skincare actives (retinol, AHAs, vitamin C) not addressed

**Real-world translation**
- Application thickness, coverage gaps, sweat resistance, reapplication kinetics, Fitzpatrick skin type — all uncaptured
- Geographic / seasonal UV varies by 10× and not factored

**Regulatory currency**
- Snapshot of May 2026; FDA Dec 2025 bemotrizinol Proposed Order is recent and not yet final

## How to serve

The webapp is a single self-contained HTML file plus a JSON data file plus pre-rendered HTML for every research doc. No build step required to view; just serve the project root with any static file server:

```bash
# Quick local preview
python3 -m http.server 8080
# Then open http://localhost:8080/webapp/index.html

# Or serve via nginx (the production setup):
# location / { root /path/to/sunscreen-filters; try_files $uri $uri.html $uri/index.html =404; }
```

To rebuild the static HTML pages after editing markdown:

```bash
python3 scripts/build-html-docs.py
# --clean to remove all generated .html before rebuilding
```

Requires Python's `markdown` package (`pip install markdown`). The script includes a complete handcoded fallback renderer for environments without it.

## AI disclosure

This atlas was researched, calibrated, written, and rendered by AI agents (Claude Code) under iterative human direction. Citations were spot-checked against PubMed and publisher pages — 2 misattributed citations were found and corrected during the adversarial critique pass. Numerical values, regulatory statuses, and SPF predictions should be re-verified against primary sources before any clinical, regulatory, or product-formulation use.

The atlas is **best read as a structured comparison tool for understanding the UV-filter landscape**, not as an authoritative product-formulation guide or SPF predictor. The methodology section in the webapp documents the systematic biases and limitations.

Background on the broader experiment of sharing Claude Code outputs publicly: [blog.sus.cat / share-your-claude-code-outputs](https://blog.sus.cat/p/share-your-claude-code-outputs).

## Provenance and licensing

- **Code** (Python build script, vanilla JS in `webapp/index.html`, Spectrum Builder math, SVG renderers) is original work.
- **Numerical data** in claim files and `spectrum-data.json` consists of facts (extinction coefficients, λmax, half-lives, regulatory caps) extracted from peer-reviewed literature and manufacturer datasheets — facts are not copyrightable.
- **Citation lists with URLs** are factual reference metadata, not protected expression.
- **Long-form prose** in claim files, MASTER-SYNTHESIS, source docs, and the README is original synthesis written by AI agents under human direction.
- **Spectrum curves** are rendered locally from extracted (λ, E1%) data points — original publication figures are not reproduced or embedded.
- **External links** point to publisher pages, regulatory documents, or open-access figure URLs as factual references; no external content is mirrored.

If you reuse this material, attribution to the original primary sources cited in each claim file is appreciated; treat the atlas itself as a structured pointer to those primary sources rather than as the authoritative reference in itself.
