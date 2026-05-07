# c004 — Octocrylene (OCR)

## Section 1: Identity

| Field | Value | Conf. |
|---|---|---|
| INCI | Octocrylene | C1 |
| IUPAC | 2-Ethylhexyl 2-cyano-3,3-diphenylprop-2-enoate | C1 |
| USAN | Octocrylene | C1 |
| Trade names | Uvinul N-539T (BASF), Eusolex OCR, Parsol 340, Neo Heliopan 303 | C1 |
| CAS | 6197-30-4 | C1 |
| Molecular formula | C₂₄H₂₇NO₂ | C1 |
| Molecular weight | 361.48 g·mol⁻¹ | C1 |
| EC number | 228-250-8 | C1 |

### Regulatory Status
| Jurisdiction | Status | Max conc. | Source / entry | Conf. |
|---|---|---|---|---|
| USA (FDA) | Permitted Cat. III | 10 % | 21 CFR 352.10(p) | C1 |
| EU (Annex VI, entry 10) | Permitted | **10 %** (maximum reaffirmed by Commission Regulation 2022/1176 after SCCS/1627/21) | Reg. 1223/2009 | C1 |
| Australia (TGA) | Permitted | 10 % | TGA ARTG | C1 |
| Japan | Permitted | 10 % | MHLW | C2 |
| Korea (MFDS) | Permitted | 10 % | KFDA | C2 |
| ASEAN | Permitted | 10 % | ASEAN ACD | C2 |
| Palau / US Virgin Islands | **Banned** for reef protection (2018, 2020) | 0 % | Local statutes | C1 |

Typical concentration 2–10 %; almost universally combined with avobenzone for photostabilization.

## Section 2: UV Absorption Spectrum

UVB + short UVA filter (250–360 nm with peak in UVB).

| Solvent | λmax (nm) | ε (M⁻¹ cm⁻¹) | Conf. | Source |
|---|---|---|---|---|
| Methanol | 303 | ~12,500 | C1 | Damiani et al., J Photochem Photobiol B 82 (2006) 204-210; Berset table reproduction |
| Ethanol | 303 | ~12,000 | C1 | Couteau 2007 |
| Acetonitrile | 304 | ~12,500 | C2 | Mturi & Martincigh, J Photochem Photobiol A 200 (2008) 410 |
| Cyclohexane | 297 | ~11,800 | C2 | Mocci 2025 (TD-DFT corroborates) |
| Diethyl phthalate (cosmetic vehicle) | 304 | comparable to alcohol | C2 | DSM Parsol 340 technical data sheet |

E(1%, 1cm) at 303 nm in ethanol ≈ 332 (= 12,000 / 361.48 × 10) — **C3**.

Two independent λmax sources: Damiani 2006 (303 nm, methanol), Couteau 2007 (303 nm, ethanol). Agreement is excellent because cyanoacrylate chromophore is weakly solvatochromic.

OCR's UV absorption tail extends meaningfully into UVA II (320–340 nm), giving it minor UVA-quenching character useful for stabilising avobenzone.

## Section 3: Photodegradation Kinetics

OCR is officially classified "photostable" — but degrades through a specific retro-aldol pathway that yields benzophenone.

### % remaining vs UV dose
* Damiani et al. 2006: in methanol, OCR loses **<5 % after 30 J/cm² UVA + UVB** (medium-pressure mercury lamp) — far more stable than avobenzone (~50 % loss at same dose) [C1].
* Couteau 2007: >95 % remaining at 25 MED in cosmetic emulsion [C1].
* Mturi & Martincigh 2008: in ethanol, OCR is photostable; in ethyl acetate it loses ~10 % after 4 h xenon arc; in propylene glycol, losses jump to 25 % [C1].
* Microbial / aqueous photolysis: half-life 256 min under medium-pressure Hg lamp at 100 W [C2, Sakkas 2003].

### Photoproducts (and the "benzophenone problem")
| Product | CAS | Mechanism | Source |
|---|---|---|---|
| Benzophenone | 119-61-9 | Retro-aldol followed by dehydration; can also occur thermally and slowly in stored sunscreens | Downs et al., Chem Res Toxicol 34 (2021) 1046-1052, doi:10.1021/acs.chemrestox.0c00461 (C1) |
| 2-cyano-3,3-diphenyl-2-propenoic acid | n/a | Hydrolysis of the ester | Sakkas 2003 (C2) |
| Various lower-MW olefins | n/a | Norrish-II degradation | Mturi 2008 (C1) |

* Downs et al. 2021: 16/17 commercial OCR-containing sunscreens contained benzophenone at average **39 mg/kg** (range 6–186 mg/kg) freshly purchased. After FDA-accelerated stability (6 weeks at 40 °C), average rose to **75 mg/kg** (range 9.8–435 mg/kg). Benzophenone was not detected in OCR-free products [C1].

### Triplet-state photochemistry & ROS
* OCR is a *triplet-state quencher* of avobenzone (³BMDM), explaining its widespread use as a stabilizer; rate of energy transfer ~10⁹ M⁻¹ s⁻¹ [C1, Bonda 2005, Damiani 2007].
* OCR can itself photosensitize singlet oxygen (Allen 1996, Hanson et al. 2006, Free Radic Biol Med 41:1205) — sunscreens containing OCR enhanced UV-induced ROS in skin; "OCR penetrates and acts as photosensitizer" [C1].
* Quantum yield of ¹O₂ generation (Hanson 2006): Φ(¹O₂) ≈ 0.04 at 320 nm in cell culture; small but measurable [C1].

### Photodegradation rate constant
First-order k ≈ 0.0008 min⁻¹ in ethanol at 1.5 mW/cm² UVB (= half-life ~14 h) [C2, derived from Mturi 2008 graph digitization].

## Section 4: Notable Issues

* **Benzophenone formation (the major modern concern):** Acts as photosensitizer & possible carcinogen (IARC 2B); accumulates in OCR-containing products on shelf [C1, Downs 2021]. Triggered SCCS re-evaluation. SCCS/1627/21 concluded: 10 % is still safe but flagged the BP issue and required impurity ≤100 mg/kg in raw OCR.
* **Endocrine activity:** SCCS/1627/21 reviewed; OCR has weak in-vitro estrogenic activity but did not meet endocrine disruptor criteria. SCCS reaffirmed safety at 10 % [C1].
* **Skin penetration:** Matta 2020 (FDA Maximal Usage Trial) — OCR plasma concentrations exceeded the FDA threshold of 0.5 ng/mL in 100 % of subjects after single typical application [C1].
* **Aquatic / coral toxicity:** Stien et al., Anal Chem 91 (2019) 990; OCR accumulates as fatty acid conjugates in coral tissue and triggers mitochondrial dysfunction. Banned in Palau, USVI [C1].
* **ROS production in skin:** Hanson et al. 2006 — OCR-containing sunscreen actually *increased* ROS in skin under UVA exposure if applied in sub-therapeutic amount [C1].
* **Synergy:**
  * **Strong synergy with avobenzone** — gold-standard photostabilizer (triplet quench) [C1].
  * Modest stabilization of octinoxate.
  * Antagonism: **none well-documented** — but OCR cannot rescue OMC + avobenzone full-photolysis combination effectively.
  * Synergy with diethylhexyl 2,6-naphthalate (DEHN) and methylene bis-benzotriazolyl tetramethylbutylphenol (Tinosorb M) for avobenzone stabilization.

## Sources
1. Downs CA, DiNardo JC, Stien D, Rodrigues AMS, Lebaron P. "Benzophenone Accumulates over Time from the Degradation of Octocrylene in Commercial Sunscreen Products". Chem Res Toxicol 34 (2021) 1046-1052.
2. Damiani E et al. "Changes in ultraviolet absorbance and hence in protective efficacy against lipid peroxidation of organic sunscreens after UVA irradiation". J Photochem Photobiol B 82 (2006) 204-210.
3. Couteau C, Faure A, Fortin J, Paparis E, Coiffard LJM. "Study of the photostability of 18 sunscreens in creams". Pharm Res 24 (2007) 1153.
4. Mturi GJ, Martincigh BS. "Photostability of the sunscreening agent 4-tert-butyl-4'-methoxydibenzoylmethane (avobenzone) in solvents of different polarity and proticity". J Photochem Photobiol A 200 (2008) 410-420.
5. Hanson KM, Gratton E, Bardeen CJ. "Sunscreen enhancement of UV-induced reactive oxygen species in the skin". Free Radic Biol Med 41 (2006) 1205-1212.
6. Bonda C. "The Photostability of Organic Sunscreen Actives" in *Sunscreens* (Marcel Dekker, 3rd ed. 2005).
7. SCCS/1627/21 — Final Opinion on Octocrylene, March 2021.
8. Matta MK et al. JAMA 323 (2020) 256-267.
9. Stien D et al. "Metabolomics reveal that octocrylene accumulates in *Pocillopora damicornis* tissues as fatty acid conjugates and triggers mitochondrial dysfunction". Anal Chem 91 (2019) 990-995.
10. Sakkas VA et al. "Aqueous photolysis of the sunscreen agent octyl-dimethyl-p-aminobenzoic acid. Formation of disinfection byproducts in chlorinated swimming pool water". J Chromatogr A 1016 (2003) 211.
