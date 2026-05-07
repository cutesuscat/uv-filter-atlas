# C002 — Meradimate (Menthyl Anthranilate / Neo Heliopan MA)

## Section 1: Identity

| Property | Value | Confidence |
|---|---|---|
| **INCI** | Menthyl Anthranilate | C1 |
| **USAN (US adopted)** | Meradimate | C1 |
| **IUPAC** | (1R,2S,5R)-2-isopropyl-5-methylcyclohexyl 2-aminobenzoate (commonly: l-menthyl 2-aminobenzoate; (1R,3R,4S)-p-menthan-3-yl 2-aminobenzoate per Wikipedia) | C2 |
| **Common synonyms** | Menthyl-o-aminobenzoate; anthranilic acid menthyl ester; menthyl-o-aminobenzoic acid ester | C1 |
| **Trade names** | Neo Heliopan MA (Symrise) | C1 |
| **CAS** | **134-09-8** (the bulk specification CAS used by FDA / Symrise / Sigma-Aldrich for racemic/l-menthyl form). Note: Wikipedia lists 307556-71-4 for stereodefined (1R,2S,5R) form — both refer to the regulated material; **134-09-8 is the FDA-cited CAS** | C1 |
| **Molecular formula** | C₁₇H₂₅NO₂ | C1 |
| **Molecular weight** | 275.39 g/mol | C1 |
| **Appearance** | Yellow viscous oil; characteristic faint odor | C2 |

### Regulatory status

| Region | Status | Max concentration |
|---|---|---|
| **USA (FDA)** | Approved Category I, OTC Monograph M020 (active ingredient) | **5%** |
| **EU (Annex VI)** | **NOT approved** for use in cosmetics — not listed in Annex VI | — |
| **Australia (TGA)** | Approved | 5% |
| **Japan** | **NOT permitted** | — |
| **South Korea** | Approved | 5% |
| **Brazil, Canada, South Africa, ASEAN** | Approved | 5% |

C1 — confirmed against US FDA M020 and absence from EU Annex VI.

### Typical use concentration

Rarely used today even in jurisdictions where allowed because of its modest UV performance and singlet-oxygen sensitization issues. When used: 1–5%, almost always in combination with stronger UVA (avobenzone) and UVB filters.

---

## Section 2: UV Absorption Spectrum

Meradimate is a **weak UVA-II / borderline UVB filter**. The chromophore is an *ortho-aminobenzoate*, which has an internal H-bond between –NH₂ and the ester carbonyl that stabilizes a charge-transfer excited state.

| Quantity | Value | Confidence |
|---|---|---|
| **λmax** | **~336 nm** (literature consensus 334–340 nm in ethanol) | C2 |
| Spectral range | ~260–360 nm; main feature centered near UVA-II/UVB boundary | C2 |
| **ε at λmax** | **~4,500–5,500 M⁻¹cm⁻¹** in ethanol — reported as one of the *lowest* among approved filters; ortho-disubstitution causes steric crowding and reduced oscillator strength | C2 (Cantrell & McGarvey 2001 and follow-on photophysics literature) |
| E(1%, 1cm) | ≈ 165–200 (computed: ε ≈ 5000 → E1% ≈ 5000·10/275 ≈ 182) | C3 |

The **low ε** is the main practical limitation: compared to avobenzone's ε ≈ 35,000 at 357 nm, meradimate is ~7× weaker per molecule and absorbs at a less useful wavelength (UVA-II edge rather than UVA-I peak). It does not provide meaningful UVA-I (340–400 nm) protection.

Solvent effects: bathochromic shift in polar protic solvents (intramolecular H-bond modulation), but data are limited.

References:
- Cantrell A, McGarvey DJ. *J Photochem Photobiol B* (2001) 64:117–122 — "The photophysical properties of menthyl anthranilate: a UV-A sunscreen" (PMID 10911723)
- Baker LA et al. *Nature Communications* (2018) 9:5095 — wavepacket photoprotection mechanism of methyl anthranilate (precursor)
- Whittock AL et al. *J Photochem Photobiol A: Chem* (2017) 350 — bottom-up photoprotection

---

## Section 3: Photodegradation Kinetics

The anthranilates are **moderately photostable as parent compounds** (no facile cleavage like avobenzone), but they have a **photophysical pathology**: they generate **singlet oxygen (¹O₂)** efficiently due to long-lived triplet state.

### Mechanism

1. UV absorption populates S₁ (charge-transfer state)
2. Slow internal conversion permits intersystem crossing to T₁
3. T₁ has long lifetime in oxygenated solution → energy transfer to O₂ → **¹O₂ generation**
4. ¹O₂ is a reactive oxidant: damages skin lipids, DNA, and *other sunscreen ingredients*

This makes meradimate a **photosensitizer**, ironically: while the compound itself is comparatively stable, it generates ROS that damage other formulation components and skin.

### Quantitative data

| Parameter | Value | Conditions | Source / Confidence |
|---|---|---|---|
| Triplet quantum yield (Φ_T) of methyl anthranilate (precursor) | ~0.4 | Acetonitrile, room temp | Cantrell & McGarvey 2001 — C2 |
| Singlet oxygen quantum yield (Φ_Δ) of menthyl anthranilate | **~0.20–0.30** | Air-equilibrated organic solvent | Cantrell & McGarvey 2001 / Yamaji follow-up — C2 |
| Photodegradation extent of MenA itself | **<5–10% loss** at typical UV doses (1–2 MED) | Ethanol or oil | C2 (cited in MDPI Photochem 2021 review) |
| Singlet oxygen suppression by Trolox / α-tocopherol | Substantial (Φ_Δ reduced by ~70%) | Yamaji et al. *Photochem Photobiol Sci* 2020 — | C1 (PMID 32484499) |

Compared to avobenzone, meradimate's mass-balance photostability is much better, but it does not behave as a "photophysically ideal sunscreen" because it converts UV into chemical reactivity (¹O₂) rather than purely heat.

### Photoproducts

When degradation does occur:
- Hydrolysis of ester → menthol + anthranilic acid (slow, but accelerated by ¹O₂-mediated oxidation)
- ¹O₂-mediated oxidation of the aromatic amine → quinones, azo coupling products (small fraction)
- N-acetyl-menthyl anthranilate is more photostable; studied as an alternative (Albini et al. *J Photochem Photobiol A* 2002)

### Effect of solvent / vehicle

- Cosmetic emollients (esters, oils) — typical commercial conditions: <10% loss after 25 MED
- Polar aprotic — no major change in degradation rate
- Co-formulation with antioxidants (Vit E, BHT) substantially reduces ¹O₂ leakage

---

## Section 4: Photostabilization

Because meradimate is a *photosensitizer rather than a photodegrader*, the goal of "stabilization" is to **suppress ¹O₂ release** rather than to protect the chromophore itself.

### ¹O₂ quenchers

- **α-Tocopherol (Vitamin E)** — physical quencher, also chemical scavenger. Documented to suppress MenA-sensitized ¹O₂ generation.
- **Trolox** — water-soluble Vit E analogue; research-grade, suppresses MenA ¹O₂. (Yamaji et al. 2020, doi:10.1039/d0pp00023j)
- **β-Carotene, lycopene** — ¹O₂ physical quenchers
- **DESM (Diethylhexyl Syringylidenemalonate / Oxynex ST)** — quencher
- **Ascorbyl tetraisopalmitate, ubiquinone** — radical scavenging

### Combination behavior

- Meradimate has not been reported to *destabilize* avobenzone (unlike octinoxate)
- It can be combined with octocrylene, Tinosorb S, BMDBM with no reported [2+2] cycloaddition or radical-pair degradation
- However, its low ε means it adds little SPF / UVA-PF for the formulation real estate it occupies

### Known issue — declining commercial use

Meradimate is increasingly phased out:
1. Low absorptive efficiency
2. ¹O₂ photosensitization (skin oxidative stress concerns)
3. Lack of EU and Japan approval limits global formulations
4. Better alternatives (DHHB, Tinosorb M/S, bemotrizinol) available outside US

---

## Confidence summary

- §1 Identity: C1
- §2 Spectrum: λmax C2; ε C2
- §3 Photodegradation: ¹O₂ quantum yield C2; mass-loss data C2
- §4 Stabilizers: C2

## Key references

1. Cantrell A, McGarvey DJ. *J Photochem Photobiol B* (2001) 64(2-3):117–122. PMID 10911723. "The photophysical properties of menthyl anthranilate: a UV-A sunscreen."
2. Baker LA et al. *Nat Commun* (2018) 9:5095. doi:10.1038/s41467-018-07681-1
3. Yamaji M, Kida M. *Photochem Photobiol Sci* (2020) 19:992. doi:10.1039/d0pp00023j (suppression of MenA ¹O₂ by Trolox/α-tocopherol). PMID 32484499.
4. Whittock AL et al. *J Photochem Photobiol A: Chem* (2017) 350. doi:10.1016/j.jphotochem.2017.09.058
5. Albini A et al. *J Photochem Photobiol A* (2002) 147:111 — N-acetyl-menthyl anthranilate photophysics
6. FDA OTC Monograph M020 (Sunscreen Drug Products). 2021.
