# Source: La Roche-Posay Anthelios UVMune 400 SPF50+

**Product**: Anthelios UVMune 400 Invisible Fluid SPF50+ (and UVMune 400 product family)
**Manufacturer**: La Roche-Posay (L'Oréal Group), France
**Label**: SPF 50+ / Critical wavelength claim "to 400 nm" / Mexoryl 400 launch product
**Preset key**: `uvmune-400`

## Sources for the ingredient list

The verified ingredient list comes from cross-checked retail and review sources:

- [La Roche-Posay official ingredient panel (incidecoder)](https://incidecoder.com/products/la-roche-posay-anthelios-uvmune-400-invisible-fluid-spf50)
- [Lab Muffin Beauty Science detailed review](https://labmuffin.com/la-roche-posay-uvmune-400-science-and-review/)
- [French Pharmacy product page](https://frenchpharmacy.com/products/la-roche-posay-anthelios-uvmune-400-spf50-fragrance-free)
- [What's in My Jar review](https://whatsinmyjar.com/product/la-roche-posay-anthelios-uvmune-400-invisible-fluid-fragrance-free-spf50)
- [SCCS opinion SCCS/1605/19 on Methoxypropylamino Cyclohexenylidene Ethoxyethylcyanoacetate (MCE)](http://yjj.sc.gov.cn/scyjj/uploads/20200515/sccs_o_227.pdf) — regulatory dossier with reference spectrum

## Active ingredients (UV filters)

EU INCI ordering rule is the same as Japan's: ingredients ≥1% appear in decreasing concentration; sub-1% may be in any order at the end. Eight UV filters appear in the formula — an unusual stack even for high-end EU sunscreens.

| INCI / common name | Position in list | EU cap | Inferred % |
|---|---|---|---|
| Ethylhexyl Salicylate (Octisalate) | early (#6) | 5% | 5% |
| Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine (Bemotrizinol / Tinosorb S) | early (#7) | 10% | 5% |
| Ethylhexyl Triazone (EHT / Uvinul T 150) | early-mid | 5% | 3% |
| Butyl Methoxydibenzoylmethane (Avobenzone) | mid | 5% | 4% |
| Methoxypropylamino Cyclohexenylidene Ethoxyethylcyanoacetate (Mexoryl 400 / MCE) | mid | 3% | 3% |
| Diethylamino Hydroxybenzoyl Hexyl Benzoate (DHHB / Uvinul A Plus) | post-1% | 10% | 3% |
| Drometrizole Trisiloxane (Mexoryl XL) | post-1% | 15% | 1.5% |
| Terephthalylidene Dicamphor Sulfonic Acid (Ecamsule / Mexoryl SX) | last among filters | 10% | 1% |

**Total active load: ~25.5% w/w** — at the upper end of EU broad-spectrum formulations.

## Concentration inference reasoning

EU regulatory caps are tighter than Japan's, so several filters are at or near maximum:

- **Mexoryl 400 (MCE)** is at the regulatory ceiling (3%, EU Reg 2020/1684 Annex VI). This is the signature filter the product was launched around — adding it at less than max would defeat the marketing premise.
- **Octisalate** at 5% is at EU cap. Used as a co-solvent for the rest of the oil-soluble filters and for marginal UVB contribution.
- **Avobenzone** at 4% is high; the 5% cap leaves headroom for stabilization-formulation tradeoffs. Avobenzone is photolabile and would normally need octocrylene as a stabilizer — but UVMune 400 famously omits octocrylene (no benzophenone shelf-life issue) and instead relies on bemotrizinol as the triplet quencher, plus its own intrinsic photostability in the L'Oréal-formulated vehicle.
- **Bemotrizinol** at 5% is moderate; could go higher but L'Oréal's stack already covers UVB strongly.
- **EHT** at ~3% is typical; its very high E1% (~1500) means even modest concentrations contribute strongly to UVB.
- **DHHB** at ~3%, **Mexoryl XL** at ~1.5%, **Mexoryl SX** at ~1% — these fill the UVA-1 and UVA-2 gaps that ZnO/TiO₂ would in a mineral formulation, but more selectively per wavelength.

The post-1% items (DHHB, Mexoryl XL, Mexoryl SX) appear with INCI list positions that suggest single-digit percent loadings, with Mexoryl SX (water-soluble, used at lowest) appearing last among the filters.

## What's notably absent

- **No octocrylene** — a deliberate choice given the Downs 2021 benzophenone-shelf-life issue. UVMune 400 demonstrates that octocrylene is no longer needed for avobenzone stabilization when bemotrizinol + the rest of the L'Oréal proprietary stack are present.
- **No octinoxate** — standard in older EU broad-spectrum but reformulated out by L'Oréal in this generation.
- **No inorganic filters** (no ZnO, no TiO₂) — purely organic stack. Mineral-free formulation is part of the "invisible fluid" aesthetic.
- **No iron oxides** — not a tinted product.

## Predicted SPF (atlas model)

| Mode | Predicted SPF | Predicted UVA-PF | Critical λ | HEV blockade |
|---|---|---|---|---|
| Lab (2 mg/cm²) | 100+ (ceiling) | 50+ | 376–384 nm | ~5–10% |
| Real-world (0.75 mg/cm²) | ~50 | ~30+ | same | same |

Label is **SPF 50+** with the critical-wavelength claim of "to 400 nm" — referencing Mexoryl 400's λmax at 385 nm being the longest UVA-1 absorption peak of any approved organic filter. Predicted critical wavelength of 376–384 nm clears the FDA broad-spectrum threshold (≥370 nm) easily.

## Why this formulation works (qualitatively)

The stack is designed to fill the entire 290–400 nm band with overlapping absorption peaks:

- **UVB workhorses**: Octisalate (305 nm), Bemotrizinol UVB peak (310 nm), EHT (314 nm) — three filters covering UVB
- **UVA-2 bridge**: Bemotrizinol UVA peak (343 nm), Mexoryl SX (345 nm), Mexoryl XL UVA peak (344 nm) — three overlapping absorbers
- **UVA-1 anchor**: Avobenzone (357 nm), DHHB (354 nm), Mexoryl 400 (385 nm) — three filters with distinct UVA-1 peak positions
- **Photostability**: Bemotrizinol acts as the universal triplet quencher (replaces octocrylene); Mexoryl 400's cyclic merocyanine is intrinsically photostable; EHT and DHHB are ESIPT-photostable via their hydroxyphenyl chromophores

The deep-UVA Mexoryl 400 peak at 385 nm is the headline novelty — it pushes effective protection ~15 nm further into the UVA-1 band than any pre-2020 commercial sunscreen, which is the rationale for the "Mune 400" branding (referring to the 400 nm absorption boundary).

## Caveats

- Concentration estimates are inferred from INCI ordering, regulatory caps, and SPF performance — not from L'Oréal disclosure (which is treated as proprietary).
- Mexoryl 400 spectral data in the atlas all traces back to L'Oréal-affiliated measurements (Marionnet 2021, SCCS/1605/19); no independent academic ε determination is published as of 2026-05.
- The atlas's lab-mode SPF prediction ("100+") matches the regulatory ceiling rather than a finite physical prediction. Real lab in-vitro SPF of UVMune 400 is reported by L'Oréal as 100+, capped at "50+" on label per EU/FDA convention.

## Files referenced

- `MASTER-SYNTHESIS.md` — atlas-wide synthesis with regulatory matrix
- `research/broad-spectrum/claims/c004-mexoryl-400-mce.md` — Mexoryl 400 primary photochemistry
- `research/broad-spectrum/claims/c001-bemotrizinol.md` — Tinosorb S spectrum + photostabilizer role
- `research/uva-organic/claims/c001-avobenzone.md` — Avobenzone solvent dependence + photochemistry
- `research/uvb-organic/claims/c009-octyl-triazone.md` — EHT (highest ε of any commercial filter)
- `research/photostab/_summary.md` — overall photostabilization landscape
