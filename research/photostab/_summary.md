# Sunscreen Photostabilization — Summary

Compiled 2026-05-07 for /workspace/sunscreen-filters/research/photostab/

This summary aggregates the eight detailed claim files (c001–c008) on the photostabilisation of organic UV filter combinations, with primary focus on rescuing avobenzone (BMDBM, butyl methoxydibenzoylmethane).

## Master table — stabilisers vs avobenzone

| # | Stabiliser (INCI / trade) | Primary mechanism | Typical use level | AVB residual: with vs without (representative) | Best key reference |
|---|---|---|---|---|---|
| 1 | **Octinoxate** (EHMC) | **DESTABILISER** — [2+2] / Paterno-Büchi cycloaddition with BMDBM diketo triplet | (3–7.5% — but causes harm) | Both AVB and OMC degrade faster together; OMC loss roughly doubled | Sayre 2005, Schwack 1995 |
| 2 | **Octocrylene** (OC) | Triplet–triplet energy transfer (TTET); kq ~10⁹ M⁻¹s⁻¹ | 5–10% | ~23% → ~90% at 25 MED in 4% AVB film | Damiani 2007; Lhiaubet-Vallet 2010; Bonda 2008/2016 |
| 3 | **Polyester-8** (Polycrylene, Hallstar) | TTET via grafted cyanodiphenyl-acrylate (same chromophore as OC) | 1–4% | Substantial improvement; less than free OC at equal mass | Hallstar PIB; SI Sci Rep 2023 |
| 4 | **DEHN** (Diethylhexyl 2,6-Naphthalate, Corapan TQ) | TTET; ³ππ* naphthalate; Φ_F=0.59, Φ_Δ=0.44 (so generates 1O2 — pair with salicylates) | 1–5% | <30% → >80% at 25 MED (manufacturer) | Shimizu 2018; Yagi 2019 |
| 5 | **Bemotrizinol** (Tinosorb S, BEMT) | TTET; broadband UV filter intrinsically photostable via ESIPT | 2–6% (max 10% EU) | ~30% → ~90% at 30 MED | Chatelain & Gabard 2001; Paris 2009 |
| 6 | **Tinosorb M** (MBBT, bisoctrizole) | Optical filtering (particulate scatterer) + ESIPT in chromophore + some TTET | 2–10% | 70–85% retention typical | BASF brochure; Lhiaubet-Vallet 2010 |
| 7 | **DESM** (Diethylhexyl Syringylidenemalonate, Oxynex ST) | TTET + 1O2 quencher + phenolic radical scavenger | 1–3% | >85% at 25 MED (manufacturer); "comparable to OC" | Chaudhuri 2006; Yagi 2025 |
| 8 | **Vitamin E / C / ferulic acid / CoQ10** | Radical scavenging + 1O2 quenching (chemical antioxidants, not photophysical) | 0.1–2% each | AVB+VitE (1:2): ≈85% retained vs ≈60% alone | Afonso 2014; Lin 2008 |
| 9 | **Solastay S1** (Ethylhexyl Methoxycrylene) | Singlet-state quencher of BMDBM (different mechanism) | 2–4% | 50.6% AVB after 120 min direct sun (best in commercial-SPF50 study) | IJSR 2023; Bonda C&T |

## Mechanism map (energy hierarchy)

Triplet energies (kcal/mol; approximate, literature consensus):

```
~70  | BMDBM enol S1 (fast ESIPT — productive UV-A absorption)
~60–66 | BMDBM diketo T1 (n,π*) — the photoreactive species ← all triplet quenchers attack here
~58  | DEHN T1 (³ππ* naphthalene)
~55  | OC ≈ MBC ≈ MBBT T1 (cyanodiphenyl-acrylate / benzylidene-camphor / hydroxyphenyl-benzotriazole)
~50–55 | Bemotrizinol T1, DESM T1
~50  | OMC (cinnamate) T1
```

Effective triplet quenching requires the quencher's T1 to lie **below** BMDBM diketo T1 by ≥2–3 kcal/mol (Förster–Dexter exergonic threshold) — satisfied by all listed photostabilisers.

## Top-line empirical numbers (sanity check)

- **Avobenzone alone**: −36% UV absorbance after 1 h sunlight (FDA/CTFA cited).
- **Avobenzone alone, 4%, 25 MED**: ~23% retained (Bonda).
- **Avobenzone + 3.6% octocrylene, 25 MED**: ~90% retained.
- **Avobenzone + 4% Tinosorb S, 30 MED, O/W**: SPF and UVA-PF maintained (~90% retained).
- **Avobenzone + DESM (1–3%), 25 MED**: >85% retained (Chaudhuri).
- **Avobenzone + octinoxate, no stabiliser**: catastrophic — both filters lost; radicals detected by ESR (Sayre).

## Vehicle / formulation pecking order (worst to best for unstabilised AVB)

Worst → Best:
mineral oil ≈ light paraffins ≈ anhydrous waxes < cyclohexane ≈ DMSO < ethyl acetate < C12-C15 alkyl benzoate ≈ dicaprylyl carbonate < ethanol < methanol/water (protic) ≈ encapsulated (β-cyclodextrin, lipid microparticles)

Adding antioxidants and photostabilisers shifts every column further to the right.

## Side-effect / contested issues

- **Octocrylene → benzophenone** (Downs 2021 Chem Res Toxicol): retro-aldol decomposition over time generates benzophenone (avg 39 mg/kg fresh; 75 mg/kg after 6-week FDA accelerated aging; max 435 mg/kg). Photostab story for AVB is intact, but a secondary safety conversation has emerged. Detailed in c002 and c008.
- **MBBT US status**: not approved by FDA — irrelevant to US monograph products.
- **DEHN 1O2 byproduct**: solvable by salicylate co-formulation (Yagi 2019).

## Confidence-tier breakdown

- **C1 (primary peer-reviewed)** dominates mechanism claims (Sayre 2005, Schwack 1995, Chatelain 2001, Chaudhuri 2006, Lhiaubet-Vallet 2010, Shimizu 2018, Mturi 2008, Afonso 2014, Downs 2021).
- **C2 (secondary, manufacturer-affiliated, or trade press)** dominates absolute % residual avobenzone numbers; treat as directional rather than authoritative.
- **C3 inferred** is used for triplet energy values that are extrapolated from analogous chromophores (e.g., Polycrylene cyanodiphenyl-acrylate ≈ OC).
- **C5 unknown**: see end of report.
