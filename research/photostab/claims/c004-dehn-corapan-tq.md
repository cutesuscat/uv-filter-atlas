# c004: DEHN — Diethylhexyl 2,6-Naphthalate (Corapan TQ) — Triplet Quencher

**Claim**: DEHN (diethylhexyl 2,6-naphthalate; CAS 127474-91-3; trade name Corapan TQ, Symrise) photostabilises avobenzone by triplet–triplet energy transfer (TTET) from the BMDBM diketo T1 to the lower-energy naphthalate T1. Approximately 60% of UV energy absorbed by DEHN is dissipated as fluorescence and ~40% generates the DEHN triplet, which decays radiatively/non-radiatively without producing significant photoproducts of avobenzone. Singlet-oxygen generation by DEHN is non-trivial (Φ_Δ ≈ 0.44 in ethanol) and is a known side-effect that needs to be quenched (e.g., by salicylates) in finished formulations.

**Confidence**: C1 for photophysics (Shimizu / Yagi / Kikuchi 2018 primary photophysics paper); C1 for the proposed TTET mechanism; C2 for finished-formulation efficacy numbers (largely Symrise technical literature).

---

## Section 1: Mechanism

### Photophysics of DEHN (naphthalate chromophore)

Shimizu et al. 2018 (Photochem Photobiol Sci 17(9):1206-1212) measured, in ethanol:

| Property | Value |
|---|---|
| Fluorescence quantum yield Φ_F | 0.59 ± 0.09 |
| Singlet-oxygen quantum yield Φ_Δ | 0.44 ± 0.04 |
| Sum (Φ_F + Φ_Δ) | ≈ 1.0 — accounts for the entire fate of the excited singlet |
| T1 character | Locally excited ³ππ* on the naphthalene ring |
| T1 energy (E_T) | ~58 kcal/mol (typical for 2,6-disubstituted naphthalenes; ZFS parameters consistent) |

The crucial energetic relationship: E_T(BMDBM diketo) ≈ 60–66 kcal/mol > E_T(DEHN) ≈ 58 kcal/mol, so triplet-triplet energy transfer from BMDBM* to DEHN is exergonic by 2–8 kcal/mol — sufficient driving force for diffusion-limited kinetics yet small enough that DEHN T1 thermal back-population is negligible.

### Mechanism summary

1. BMDBM (diketo) absorbs UV-A → S1 → ISC → T1 (n,π*, ~60–66 kcal/mol).
2. Encounter with DEHN: TTET → BMDBM (S0) + DEHN (T1, ³ππ*).
3. DEHN T1 either (a) phosphoresces / IC to S0, or (b) sensitises 3O2 → 1O2.
4. Result: BMDBM is rescued; potential cost is 1O2 generation.

### Salicylate co-formulation

A follow-up paper (Yagi et al. 2019, Photochem Photobiol Sci 18(?), DOI 10.1039/c9pp00104b) showed that ethylhexyl salicylate and homosalate suppress DEHN-photosensitised 1O2 by quenching DEHN T1 before it reaches O2. This rationalises the common formulation pairing of DEHN with salicylates.

---

## Section 2: Quantitative effect

### Photophysical numbers (primary)

- Φ_F(DEHN) = 0.59 ± 0.09 in ethanol (Shimizu 2018).
- Φ_Δ(DEHN) = 0.44 ± 0.04 in ethanol (Shimizu 2018).
- Triplet quenching of BMDBM by DEHN: rate not directly reported in the 2018 paper; expected near diffusion-limited (kq ≈ 10^9 – 10^10 M⁻¹ s⁻¹) given the favourable thermodynamics. [C3 inferred]

### Formulation efficacy (Symrise / industry)

- Symrise / Vigon technical literature: Corapan TQ at 1–5% in O/W or W/O formulations containing 3% AVB increases retention of AVB from <30% to >80% after 25 MED. [C2, manufacturer]
- Acts as a multi-functional emollient and excellent solvent for crystalline UV filters (e.g., bemotrizinol, ensulizole, MBBT). The dual role (solvent + photostabiliser) is a major reason for its popularity in EU/Asia.
- No FDA monograph status; Corapan TQ is a non-active ingredient in US OTC sunscreens (used for ancillary stabilisation).

### Independent academic data

- Limited beyond the 2018/2019 Yokohama National University photophysics work.
- Couteau et al. (Univ Caen) data sets on commercial sunscreens implicitly include DEHN-stabilised products but do not isolate DEHN as the active variable.

---

## Section 3: Practical formulation guidance

- Typical use level: 1–5% w/w.
- Pair with salicylate UV filters (homosalate, octisalate) to suppress 1O2 byproduct (Yagi 2019).
- Excellent solvent for solid filters; may replace a portion of fatty ester solvent.
- Compatibility good with all common cosmetic oils. Shelf-stable.
- INCI: Diethylhexyl 2,6-Naphthalate. CAS 127474-91-3. Trade names: Corapan TQ (Symrise; originally Pentapharm/Cognis lineage). Hallstar markets a similar offering as part of formulation kits.
- Patent: Symrise WO 2007/068344 and DE 102004039631 cover DEHN photostabilisation of dibenzoylmethane filters.

---

## Section 4: Citations

1. **Shimizu R, Yagi M, Oguchi-Fujiyama N, Miyazawa K, Kikuchi A.** "Photophysical properties of diethylhexyl 2,6-naphthalate (Corapan TQ), a photostabilizer for sunscreens." *Photochemical & Photobiological Sciences* 17(9):1206-1212 (2018). DOI: 10.1039/c8pp00204e. PMID: 30063240. **[C1, primary photophysics]**
2. **Yagi M, Shimizu R, Hyodo F, Oguchi-Fujiyama N, Miyazawa K, Kikuchi A.** "A novel characteristic of salicylate UV absorbers: suppression of diethylhexyl 2,6-naphthalate (Corapan TQ)-photosensitized singlet oxygen generation." *Photochemical & Photobiological Sciences* 18(?):? (2019). DOI: 10.1039/c9pp00104b. PMID: 31033968. **[C1]**
3. **Symrise / Vigon International.** Corapan TQ (Diethylhexyl 2,6-Naphthalate) Technical Data Sheet & SDS. **[C2, manufacturer]**
4. **WO 2007/068344 A1** (Symrise). Photostable sunscreen compositions comprising 2,6-naphthalate diesters. **[Patent]**
5. **Bonda CA, Lott D.** Sunscreen Photostability. Springer 2016 (chapter overview includes DEHN). **[C2, review]**

### Bias caveat

Most efficacy claims for finished formulations come from Symrise technical literature. The independent academic record (Yokohama group, Lhiaubet-Vallet group) confirms the photophysical foundations of the TTET mechanism and identifies the 1O2 byproduct as a real concern, supporting careful pairing with salicylate quenchers.
