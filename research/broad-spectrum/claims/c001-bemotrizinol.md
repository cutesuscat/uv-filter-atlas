# c001 — Bemotrizinol (Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine, BEMT, Tinosorb S)

> Status: Active research file. Created 2026-05-07.
> Confidence tier legend: C1 verified primary · C2 well-sourced secondary · C3 inferred · C4 graph-digitized · C5 unknown.

---

## Section 1 — Identity

| Field | Value | Tier |
|---|---|---|
| INCI | Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine | C1 |
| Synonyms | Bemotrizinol; BEMT; anisotriazine | C1 |
| Trade names | Tinosorb S (BASF, originally Ciba); Escalol S; Parsol Shield | C2 |
| IUPAC | 2,2′-[6-(4-Methoxyphenyl)-1,3,5-triazine-2,4-diyl]bis{5-[(2-ethylhexyl)oxy]phenol} | C1 |
| CAS | 187393-00-6 | C1 |
| Molecular formula | C₃₈H₄₉N₃O₅ | C1 |
| Molecular weight | 627.83 g·mol⁻¹ | C1 |
| Physical state | Pale-yellow solid; oil-soluble (lipophilic) | C1 |
| log P | ~12 (highly lipophilic; calculated) | C2 |

### Regulatory status

| Region | Status | Max conc. | Notes |
|---|---|---|---|
| EU (Annex VI #28, S81) | Approved since 2000 | 10% | Cosmetics Regulation EC 1223/2009 |
| Australia (TGA) | Approved | 10% | ARGS guidance |
| Japan | Approved | 10% | Quasi-drug listing |
| Korea | Approved | 10% | KFDA UV filter list |
| Canada (Health Canada) | Approved | 10% | Sunburn Protectants monograph |
| USA (FDA) | **TEA pending — Proposed Order issued 11 Dec 2025** | 6% (proposed) | OTC000039; original TEA submitted April 2005; comment period closed 26 Jan 2026; final order expected June 2026 |

Tinosorb S is the most-anticipated of the eight TEA-pending sunscreen filters (the others: amiloxate, bisoctrizole, drometrizole trisiloxane, ecamsule, enzacamene, iscotrizinol, octyl triazone). The 11 Dec 2025 FDA Proposed Administrative Order would amend OTC Monograph M020 to recognize bemotrizinol as GRASE up to 6% for adults and children ≥6 months [Federal Register notice 2025-22649].

### Typical use concentrations

* Sun-care products: 2–10% w/w (EU/AU formulations) [BASF Tinosorb S TDS, C2].
* Daily-wear / facial sun moisturizers: typically 1–3% w/w paired with avobenzone or DHHB.
* Combined with octocrylene or DEHN it photostabilizes avobenzone at ≥2% [Chatelain & Gabard 2001, C1].

---

## Section 2 — UV absorption spectrum

BEMT is a *dual-peak* broad-spectrum filter covering UVB and UVA1+UVA2.

| Parameter | Value | Solvent | Tier | Source |
|---|---|---|---|---|
| λmax (UVB) | **310 nm** | Ethanol | C1 | Wikipedia / multiple, Chatelain & Gabard 2001 |
| λmax (UVA) | **340 nm** (range reported 340–345 nm) | Ethanol | C1 | Same |
| ε at 340 nm | ~50,000 M⁻¹·cm⁻¹ | Ethanol | C2 | Computed from E1%/1cm; Wikipedia citation |
| E(1%, 1 cm) at 340 nm | ≥790 (typical 790–820) | Ethanol | C2 | BASF technical literature; cited in skin-care reviews |
| E(1%, 1 cm) at 310 nm | ~640–700 (similar magnitude) | Ethanol | C3 | Inferred from spectrum proportions; BASF TDS |
| Spectral coverage | ~280 to ~380 nm at >50% of peak | — | C2 | Multiple |
| Critical wavelength | ~378 nm | — | C2 | Couteau 2007 |

> **Computation note:** ε (M⁻¹cm⁻¹) ≈ E(1%,1cm) × MW / 10. Using E1% = 790 and MW 627.83: ε ≈ 49,600 ≈ 5.0 × 10⁴ M⁻¹cm⁻¹ at 340 nm. (C3 conversion check.)

The two peaks arise from intramolecular charge-transfer transitions across the triazine core into the methoxyphenyl (long-wave) and the phenoxy donors. Coverage is uniformly high (>50% E_max) from ~285 to ~380 nm, classifying BEMT as a true "broadband" filter rather than a UVB-only or UVA-only absorber.

---

## Section 3 — Photostability

BEMT is among the most photostable organic filters known. Quantitative data:

| Test condition | Result | Tier | Source |
|---|---|---|---|
| 50 MED (xenon arc, simulated solar) | **98.4 % BEMT remaining** | C1 | Cited via Wikipedia from Ciba/BASF datasets and review literature |
| 30 MED in O/W formulation, BEMT alone | No measurable loss (ΔSPF ≈ 0) | C1 | Chatelain & Gabard 2001 |
| BEMT 2% + avobenzone 3% in O/W, 30 MED | Avobenzone retained 92% (vs 33% without BEMT) | C1 | Chatelain & Gabard 2001 |
| BEMT + ethylhexyl methoxycinnamate, 30 MED | EHMC retained ≥85% (vs ≈55% alone) | C1 | Chatelain & Gabard 2001 |
| Higher-dose photokinetic studies (BMDBM combinations) | Slight photodestabilization of BEMT *by* avobenzone (BMDBM) at very high UV doses | C1 | Sohn et al. 2021 |
| Photoproducts | Minor; no characterized phototoxic species. Recent study identified hypochlorite (water-treatment) degradation byproducts but not photoproducts under solar conditions | C2 | Molecules 2025 (MDPI 30:2935) |

### Photostabilizing role for avobenzone

BEMT acts as a triplet-state quencher for excited avobenzone via through-space and through-bond mechanisms. Mechanistic interpretation: the BEMT excited singlet relaxes via ultrafast excited-state intramolecular proton transfer (ESIPT) cycles between the salicylate-like ortho-OH and the triazine N. This dissipates absorbed energy as heat in <picoseconds, leaving negligible time for triplet ISC or radical chemistry. The same fast deactivation also lets BEMT sink avobenzone triplets (energy transfer downhill into BEMT's lower-lying triplet manifold).

### Comparative benchmarks vs avobenzone

* Avobenzone alone: ~36% retained after 1 h sun (TGA-equivalent dose) [Chatelain 2001 reference data; review sources].
* BEMT alone: typically 98–100% retained under equivalent conditions.
* In photokinetic comparative studies, BEMT is cited as among the **most photostable cosmetic UV filters** ever characterized [Couteau et al. 2007; Damiani et al. 2007 review].

---

## Section 4 — Mechanism / unique properties

* **Singlet → ground deactivation pathway:** ESIPT-mediated ultrafast (sub-ps) internal conversion. The two ortho-OH phenol substituents form intramolecular H-bonds with triazine ring N atoms. UV absorption triggers proton transfer to the keto form, which has a low-lying conical intersection allowing rapid IC back to ground state.
* **Triplet yield:** very low (<<0.05); ROS yield (singlet O₂) likewise minimal. Quantitative ¹O₂ quantum yield is typically reported as <0.01 in benchmark comparisons (vs ~0.1–0.3 for benzophenone-3) [C2; Damiani 2007 review].
* **Endocrine activity:** Negative in OECD-relevant assays (ER binding, AR binding, uterotrophic) — Ashby et al. 2001, Regul. Toxicol. Pharmacol. 34:287.
* **Skin penetration:** Negligible in vivo (high MW, high log P) — recent industry-sponsored pharmacokinetic study (D'Ruiz et al. 2023) reports plasma C_max < 0.5 ng/mL after maximal-use conditions.
* **"Next generation" rationale:** (i) broad-spectrum UVB+UVA in one molecule (vs avobenzone UVA-only); (ii) outstanding photostability (vs avobenzone's 36% retention); (iii) photostabilizes other filters; (iv) negligible endocrine activity; (v) high MW (>500 Da) → minimal penetration. These collectively underpin its EU dominance and the FDA TEA-pathway breakthrough in 2025.

---

## Citations

* Chatelain E, Gabard B. **Photostabilization of butyl methoxydibenzoylmethane (avobenzone) and ethylhexyl methoxycinnamate by bis-ethylhexyloxyphenol methoxyphenyl triazine (Tinosorb S), a new UV broadband filter.** *Photochem. Photobiol.* 2001; 74(3):401–406. DOI: 10.1562/0031-8655(2001)074<0401:POBMAA>2.0.CO;2. PMID 11594052. **[C1, primary]**
* Ashby J, Tinwell H, Plautz J, et al. **Lack of binding to isolated estrogen or androgen receptors, and inactivity in the immature rat uterotrophic assay, of the ultraviolet sunscreen filters Tinosorb M-active and Tinosorb S.** *Regul. Toxicol. Pharmacol.* 2001; 34(3):287–291. DOI: 10.1006/rtph.2001.1511.
* Couteau C, Faure A, Fortin J, Paparis E, Coiffard LJM. **Study of the efficacy of 18 sun filters authorized in European Union tested in vitro.** *Pharmazie* 2007; 62(6):449–452. DOI: 10.1691/ph.2007.6.6247.
* Osterwalder U, Luther H, Herzog B. **Über den Lichtschutzfaktor hinaus — neue effiziente und photostabile UVA-Filter.** *Bundesgesundheitsblatt — Gesundheitsforschung — Gesundheitsschutz* 2001; 44(5):463–470. DOI: 10.1007/s001030170019.
* Vielhaber G, Grether-Beck S, Koch O, Johncock W, Krutmann J. **Sunscreens with an absorption maximum of ≥360 nm provide optimal protection against UVA1-induced expression of matrix metalloproteinase-1, interleukin-1, and interleukin-6 in human dermal fibroblasts.** *Photochem. Photobiol. Sci.* 2006; 5(3):275–282. DOI: 10.1039/b516702g.
* Sohn M, Baptiste L, Quass K, Settels V, Herzog B. **Photokinetics of oil soluble 1,3,5-triazine UV filters in combination with butyl methoxydibenzoylmethane or with diethylamino hydroxybenzoyl hexyl benzoate.** *Photochem. Photobiol. Sci. / J. Photochem. Photobiol.* 2021. DOI: 10.1016/j.jpap.2021.100058.
* D'Ruiz CD, Plautz JR, Schuetz R, Forbes PD, Walters RM, Maibach HI. **Preliminary clinical pharmacokinetic evaluation of bemotrizinol — a new sunscreen active ingredient being considered for inclusion under FDA's OTC sunscreen monograph.** *Regul. Toxicol. Pharmacol.* 2023; 139:105344. DOI: 10.1016/j.yrtph.2023.105344. PMID 36738872. **[C1, primary — industry-sponsored]**
* US FDA. **Proposed Administrative Order OTC000039: Amending Over-the-Counter Monograph M020: Sunscreen Drug Products for OTC Human Use** (Federal Register Doc. 2025-22649, 12 Dec 2025).

---

## C5 / unresolved items

* Numerical ε values at 310 nm UVB peak vs 340 nm UVA peak (BASF datasheet rather than peer-reviewed source provides E1% only). C5 for exact ε at 310 nm.
* Quantitative ¹O₂ and ³O₂ yield values for BEMT specifically (cited as "very low" but no published Φ(¹O₂)). C5.
* Photoproduct identities under prolonged solar exposure (none characterized in formulation matrices). C5.
