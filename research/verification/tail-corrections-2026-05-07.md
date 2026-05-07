# Filter Tail Extension Corrections — 2026-05-07

## Context
The webapp interpolates linearly between data points and then exponentially decays (1/e per 4 nm) past the last point. Filters whose tails ended at high E1% values (e.g., Avobenzone at 410 nm with E1%=14.8, Tris-Biphenyl Triazine at 365 nm with E1%=229) produced unrealistic flat-then-fast-decay artifacts in the visible region. Each tail was extended so that the final point sits at <2 E1% within ~30-50 nm past the spectral peak.

## Filters updated (21 total)

**HIGH PRIORITY (10):** idx 14 Avobenzone (+3, to 440 nm; Mturi 2008), idx 15 Meradimate (+3, to 410 nm; Cantrell 2000), idx 16 DHHB (+3, to 435 nm; Wang 2023), idx 17 Bisoctrizole (+3, to 435 nm; Naumov 2020), idx 18 Iscotrizinol (+3, to 385 nm; 3V Sigma), idx 19 Bemotrizinol (+3, to 420 nm; Chatelain 2001), idx 20 Ecamsule (+3, to 415 nm; Deflandre 1988), idx 21 Drometrizole Trisiloxane (+3, to 415 nm; ESIPT analogy), idx 23 TBPT (+5, to 415 nm; Naumov 2023 — biggest fix, last point was 229 E1%), idx 24 Bisdisulizole (+3, to 405 nm; Symrise).

**MEDIUM PRIORITY benzophenones (5):** idx 25 BP-3 (+4, to 395 nm), idx 26 BP-4 (+4, to 400 nm), idx 27 BP-8 (+3, to 400 nm), idx 28 BP-10 (+4, to 400 nm; C5 by analogy), idx 31 BP-1 (+4, to 400 nm).

**LOW PRIORITY UVB filters (6):** idx 1 Octinoxate (+4, to 385 nm; cinnamate red asymmetry), idx 4 Octocrylene (+3, to 375 nm), idx 7 Padimate O (+4, to 385 nm), idx 10 EHT (+4, to 385 nm), idx 11 4-MBC (+3, to 368 nm), idx 13 Trolamine Salicylate (+2, to 355 nm).

## Already adequate (no change)
- idx 22 Mexoryl 400 (already extended to 460 nm at E1%=3 in prior fix).
- idx 29 ZnO, idx 30 TiO₂ (manually fixed previously).
- idx 32-34 Iron Oxides (already extend to 720 nm).

## C5 cases (estimated by analogy)
- **idx 28 Mexenone (BP-10):** sparse independent spectrum data. Tail extrapolated by analogy to BP-3 and BP-1 (same chromophore class).
- **idx 18 Iscotrizinol** and **idx 21 Drometrizole Trisiloxane:** independent academic spectra are limited; tails follow benzotriazole/triazine class shape from Naumov 2020/2023 figures.

## Quality check
- JSON validated (36 filters intact).
- All tails decay to <2 E1% within ~30-50 nm of last existing data point.
- Asymmetry preserved per chromophore class: cinnamates (Octinoxate, Padimate O) extend further on red side; ESIPT (BMOT, BEMT, Mexoryl XL) decay sharply; benzophenones (BP-3/4/8/10/1) decay symmetrically from the UVA-II peak.
- Existing in-range data points were not modified; only appended past last point.
