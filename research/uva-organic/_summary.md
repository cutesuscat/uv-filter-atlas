# UVA Organic Sunscreen Filters — Comparison Summary

Five UVA-active organic sunscreen filters reviewed. Files: `claims/c001-avobenzone.md` through `claims/c005-iscotrizinol.md`. Date: 2026-05-07.

## Master Comparison Table

| # | Filter (INCI) | Trade name | CAS | MW (g/mol) | λmax (nm) | ε at λmax (M⁻¹cm⁻¹) | E(1%, 1cm) | UV range | Photostability | FDA US | EU max | JP | AU | KR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Butyl Methoxydibenzoylmethane (Avobenzone, BMDBM) | Parsol 1789 | 70356-09-1 | 310.39 | **357 (enol, MeOH)**; 265 (keto) | ~35,000 (MeOH) | ~1130 | UVA-I, UVA-II (310–400) | **POOR** — ~36% loss / 1 h sun alone; needs stabilizer | 3% | 5% | 10% | 5% | 5% |
| 2 | Menthyl Anthranilate (Meradimate) | Neo Heliopan MA | 134-09-8 | 275.39 | ~336 | ~5,000 | ~180 | UVA-II / UVB edge (260–360) | **MODERATE chromophore stability but generates ¹O₂** (Φ_Δ ~0.20–0.30) | 5% | **N/A** (not approved) | **N/A** | 5% | 5% |
| 3 | Diethylamino Hydroxybenzoyl Hexyl Benzoate (DHHB) | Uvinul A Plus / Parsol DHHB | 302776-68-7 | 397.51 | **354** | **~39,000 (EtOH)** | ~980 | UVA (320–400) | **EXCELLENT** — >95% remaining; ESIPT mechanism | TEA pending | 10% | 10% | 10% | 10% |
| 4 | Methylene Bis-Benzotriazolyl Tetramethylbutylphenol (Bisoctrizole, MBBT) | Tinosorb M | 103597-45-1 | 658.88 | **305 + 360** (dispersion); 305 + 350 (solution) | ~52,000 @305; ~46,000 @350 | ~700 @350 | Broad UVB+UVA (280–400 + shoulder to ~410) | **EXCELLENT** — >95–99% remaining; ESIPT + particulate | TEA pending | 10% | 10% | 10% | 10% |
| 5 | Diethylhexyl Butamido Triazone (Iscotrizinol) | Uvasorb HEB | 154702-15-5 | 765.98 | **310** | ~110,000 (manuf.) | ~1435 | UVB + edge UVA-II (280–340) | **EXCELLENT** — ~10% loss / 25 h sun | TEA pending | 10% | 10% | 10% | 10% |

## Photostability Ranking (best to worst, neat or in standard cosmetic vehicle)

1. **Bisoctrizole (Tinosorb M / MBBT)** — particulate ESIPT; >95% remaining; also stabilizes others
2. **Iscotrizinol (Uvasorb HEB)** — ~10% loss in 25 h sun
3. **DHHB (Uvinul A Plus)** — ESIPT, >95% remaining; stabilizes others
4. **Meradimate** — chromophore mass-stable but is a ¹O₂ photosensitizer; effectively destabilizing to formulations and skin
5. **Avobenzone** — **photolabile** (~36% loss/1 h sunlight alone); requires stabilizer (octocrylene most common)

## Spectral Coverage Map (UV protection profile)

```
UVB    UVA-II         UVA-I        Visible
280───315────340─────────400nm
        |
[1] Avobenzone:           ░░██████████ (peak 357)
[2] Meradimate:        ░░░██░░         (peak 336, weak)
[3] DHHB:                  ░██████░░  (peak 354)
[4] MBBT:        █████░░░██████░░    (peak 305 + 360)
[5] Iscotrizinol: █████░░              (peak 310)
```

## Strengths/Weaknesses Quick-View

| Filter | Strengths | Weaknesses |
|---|---|---|
| **Avobenzone** | Strongest UVA-I per gram; FDA-approved (only US-approved UVA-I filter); cheap; universally available | Photolabile; needs stabilizer; degrades to phenylglyoxals/benzils (sensitizers); incompatible with octinoxate ([2+2] cycloaddition) |
| **Meradimate** | FDA-approved; oil-soluble | Low ε; weak UVA-II only; ¹O₂ photosensitizer; not in EU/JP |
| **DHHB** | Excellent UVA-I; photostable; stabilizes others | Not FDA-approved; phthalate impurity concern (DnHexP) |
| **MBBT (Tinosorb M)** | Broadest spectrum; very photostable; stabilizes others; reef-safer | Not FDA-approved; particulate (formulation complexity); aqueous dispersion only |
| **Iscotrizinol** | Excellent UVB; very photostable | Not FDA-approved; minimal UVA-I contribution; expensive |

## Important Cross-Filter Interactions

- **Avobenzone + Octinoxate**: AVOID. Concomitant photolysis via [2+2] cinnamate–dibenzoylmethane cycloaddition; persistent free radicals (Sayre 2005, doi:10.1562/2004-02-12-RA-083).
- **Avobenzone + Octocrylene**: STANDARD STABILIZATION (triplet–triplet energy transfer). However: octocrylene degrades to **benzophenone via retro-aldol** over shelf life (Downs et al., Chem Res Toxicol 2021, doi:10.1021/acs.chemrestox.0c00461) — 6–186 mg/kg fresh; 9.8–435 mg/kg after accelerated aging.
- **Avobenzone + DEHN (Corapan TQ)**: triplet-triplet energy transfer; effective stabilizer (doi:10.1039/c8pp00204e).
- **Avobenzone + Polyester-8 (Polycrylene)**: synergizes with DEHN; same chromophore class as octocrylene but polymeric (less skin penetration).
- **Avobenzone + DHHB / MBBT / bemotrizinol / Mexoryl**: compatible and frequently stabilizing.
- **Meradimate**: combine with α-tocopherol or Trolox to suppress ¹O₂ output.
- **DHHB / MBBT / Iscotrizinol**: no known negative interactions.

## Solvent Effects on Avobenzone (CRITICAL)

| Solvent | λmax enol (nm) | Photodegradation |
|---|---|---|
| Cyclohexane | 355 | Appreciable |
| Ethyl acetate | 356 | Photoiso. + photodegradation |
| Methanol | 358 | **Essentially photostable** (protic solvent stabilizes enol) |
| DMSO | 363 | Photoisomerisation only (O₂-dependent), no photodegradation |

(Mturi & Martincigh 2008, *J Photochem Photobiol A* 200:410–420.)

This is the single most important caveat in interpreting any avobenzone data: the ε, λmax, and photostability all shift dramatically with solvent. Always state the solvent.

## Confidence overview

- All identity & MW: **C1**
- λmax for all five: **C1** (literature-confirmed)
- ε values: **C1** (DHHB, avobenzone E1%); **C2** (MBBT solution, iscotrizinol manufacturer); **C2** (meradimate)
- Photostability rankings: **C1–C2**
- Specific quantum yields (Φ): mixed; iscotrizinol Φ_T and Φ_Δ are **C5 unknowns** in accessible literature
- Regulatory: **C1** for current state, primary EU/FDA documents

## C5 (Unknown / Not Located)

1. **Iscotrizinol** Φ_T and Φ_Δ — primary peer-reviewed values not located
2. **Iscotrizinol** ultrafast photoprotection mechanism (specific TEAS study) — not located
3. **Meradimate** specific solvent-dependent λmax variation — limited public data
4. **Bisoctrizole** primary peer-reviewed ε values (most data are manufacturer/secondary)
5. Avobenzone Φ for individual photoproduct channels — **estimated** from indirect data

See `sources.md` for full citations.
