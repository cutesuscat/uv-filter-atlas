# Sunscreen UV Filters — Spectra & Photodegradation

Research project: comprehensive collection of UV absorption spectra and photodegradation kinetics for all globally-approved sunscreen active ingredients, sourced from peer-reviewed scientific literature.

**Initiated:** 2026-05-07
**Methodology:** Following `/workspace/overview/research-agent-instructions.md` — claim files, confidence tiers, citations.

## Research Areas

| # | Area | Location | Status | Filters Covered |
|---|------|----------|--------|-----------------|
| 1 | UVB organic filters | `research/uvb-organic/` | dispatched | Octinoxate, Octisalate, Homosalate, Octocrylene, Cinoxate, PABA/Padimate O, Ensulizole, Polysilicone-15, Octyl Triazone, 4-MBC |
| 2 | UVA organic filters | `research/uva-organic/` | dispatched | Avobenzone, Meradimate, DHHB, Tinosorb M, Iscotrizinol |
| 3 | Broad-spectrum / Mexoryl | `research/broad-spectrum/` | dispatched | Bemotrizinol (Tinosorb S), Ecamsule, Mexoryl XL, Mexoryl 400, Tinosorb A2B, Bisdisulizole |
| 4 | Benzophenones | `research/benzophenones/` | dispatched | Oxybenzone (BP-3), Sulisobenzone (BP-4), Dioxybenzone (BP-8), Trolamine Salicylate |
| 5 | Inorganic / mineral | `research/inorganic/` | dispatched | Zinc Oxide, Titanium Dioxide |
| 6 | Photostabilization | `research/photostab/` | dispatched | Octocrylene+Avobenzone, DEHN, Polycrylene, formulation effects |

## Output deliverables (per filter)
- INCI name, IUPAC name, CAS number
- Molar absorption coefficient, λmax (UVA / UVB peaks)
- Full spectrum (digitized or referenced figure source)
- Photostability: % active remaining vs UV dose / time
- Half-life or first-order rate constant where reported
- Photoproducts where characterized
- Regulatory status (FDA / EU / Australia / Japan / Korea)

## Confidence tiers
C1 verified primary source · C2 well-sourced secondary · C3 inferred (show working) · C4 anecdotal · C5 unknown

## Status
Phase 1 complete (2026-05-07). All 6 deep-research agents returned. 37 individual claim files + 6 area summaries + 6 source lists + 1 master synthesis.

**Read first:** [MASTER-SYNTHESIS.md](MASTER-SYNTHESIS.md) — consolidated reference with comparison tables, spectral coverage map, photostability rankings, regulatory matrix, and aggregated data gaps.

## Counts
- 30 individual UV filters covered
- 270+ peer-reviewed sources cited across the six `sources.md` files
- ~37 claim files, each with full citations and confidence tiers
- 13 cross-area data gaps documented in MASTER-SYNTHESIS.md §8
