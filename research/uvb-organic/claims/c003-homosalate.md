# c003 — Homosalate (HMS)

## Section 1: Identity

| Field | Value | Conf. |
|---|---|---|
| INCI | Homosalate | C1 |
| IUPAC | 3,3,5-Trimethylcyclohexyl 2-hydroxybenzoate | C1 |
| USAN | Homosalate | C1 |
| Trade names | Eusolex HMS, Neo Heliopan HMS, Escalol 567 | C1 |
| CAS | 118-56-9 | C1 |
| Molecular formula | C₁₆H₂₂O₃ | C1 |
| Molecular weight | 262.35 g·mol⁻¹ | C1 |
| EC number | 204-260-8 | C1 |

### Regulatory Status
| Jurisdiction | Status | Max conc. | Source / entry | Conf. |
|---|---|---|---|---|
| USA (FDA) | Permitted Cat. III | **15 %** (highest of any FDA-approved filter) | 21 CFR 352.10(g) | C1 |
| EU (Annex VI, entry 3) | **Restricted** to face products only after SCCS opinion | **7.34 %** in face products only (excluding propellant/pump sprays); banned in body products from 2023 transition | Commission Regulation (EU) 2022/1176; SCCS/1622/20 final | C1 |
| Australia (TGA) | Permitted | 10 % | TGA ARTG | C1 |
| Japan | Permitted | 10 % | MHLW | C2 |
| Korea (MFDS) | Permitted | 10 % | KFDA | C2 |
| ASEAN | Permitted at 10 % | 10 % | ASEAN | C2 |

Found in ~45 % of US sunscreens [C2, EWG].

Typical use 5–15 %; in EU now limited to face products at 7.34 %.

## Section 2: UV Absorption Spectrum

UVB filter (290–320 nm). Like octisalate, HMS shows minimal solvatochromism due to intramolecular H-bonding.

| Solvent | λmax (nm) | ε (M⁻¹ cm⁻¹) | Conf. | Source |
|---|---|---|---|---|
| Cyclohexane | 309 | ~5,200 | C1 | Krokidi et al., PCCP 22 (2020) 18044 |
| Ethanol | 306–307 | ~5,000 | C1 | Krokidi 2020; Shaath 2005 |
| Acetonitrile | 306 | ~5,100 | C1 | Krokidi 2020 |
| Methanol | 306 | ~5,000 | C2 | Couteau 2007 (digitized) |
| TD-DFT computed | ~306 | f = 0.10 | C3 | Mocci 2025 |

Specific extinction E(1%, 1cm) ≈ 191 at 307 nm in ethanol — **C3** (= 5,000/262.35 × 10).

Like EHS, HMS is a *weak* UVB absorber — among the lowest ε of all approved organic UVB filters. Two independent λmax sources: Krokidi (PCCP 2020), Shaath (Marcel Dekker 2005) — both cite 306–309 nm in alcohols [C1].

## Section 3: Photodegradation Kinetics

**Mechanism — ultrafast ESIPT** (excited-state intramolecular proton transfer) on the salicylate moiety; this is the source of HMS's photostability.

* ESIPT time constant τ₁: 55–105 fs (cyclohexane, ethanol, acetonitrile) [C1, Krokidi 2020].
* Vibrational cooling/IC τ₂: 9.4–14.2 ps [C1].
* Fluorescence τ₃: 180–532 ps [C1].
* Fluorescence quantum yield ΦF: 0.035 (ACN), 0.046 (EtOH), 0.116 (CHX) [C1, Krokidi 2020].
* Phosphorescence (ethanol, 77 K) ΦP: 0.049 [C1].
* Stokes shift ~120 nm in solution; ~0.72 eV in gas phase, confirming ESIPT.

### % remaining vs UV dose
* Couteau et al. 2007: HMS classified photostable, **>90 % remaining at 25 MED** in ethyl-acetate vehicle [C1].
* Stiefel & Schwack 2014: <5 % loss of HMS over 1.5 MJ/m² xenon-arc exposure in alcoholic solution [C1].
* Bonda C., "The Photostability of Organic Sunscreen Actives", in *Sunscreens* 2005: salicylates "essentially photostable to all terrestrial UV doses" [C2].
* Caveat: in formulations, HMS can quench avobenzone's triplet to a small extent but is much less efficient than octocrylene; reports of antagonism with avobenzone (Bonda 2005, Damiani 2007) suggest formulations of avobenzone + HMS without OCR may show 10–25 % avobenzone loss after 1 MED [C2].

### Photoproducts
No major bond-breaking photoproducts identified for monomer HMS in solution; gas-phase deprotonated [HS – H]⁻ decays only via electron detachment without ionic fragments [C1, Wong et al., PCCP 24 (2022) 18101].

### Quantum yield of degradation
Φd ≪ 10⁻³ (effectively "photostable") — **C3** derived from absence of detectable products.

## Section 4: Notable Issues

* **Endocrine disruption (the headline issue):** SCCS final opinion 2020 (SCCS/1622/20) found HMS estrogenic, antiandrogenic, and "presumed thyroid disruptor"; recommended **maximum safe concentration of 0.5 % in body products and 7.34 % only in face products**. EU adopted 7.34 % limit (face only) in Regulation 2022/1176. SCCS noted the "Margin of Safety is too low at 10 %" [C1].
* **Skin penetration:** Kasichayanula et al. (2007) — measurable urinary HMS for ≥48 h after single application; FDA Maximal Usage Trial (Matta et al., JAMA 2020) measured **plasma HMS >0.5 ng/mL** (the FDA toxicology threshold) after a single typical sunscreen application — repeat exposure pushes plasma even higher [C1].
* **Photostability:** Photostable when alone; controversial when paired with avobenzone — see Bonda 2005, Sayre 2005.
* **ROS/phototoxicity:** Negligible singlet oxygen generation [C1, Allen 1996; Krokidi 2020].
* **Aquatic toxicity:** LC50 fish ≈ 0.4 mg/L, classified Aquatic Chronic 1 (H410) by ECHA; one of the longer-environmental-half-life UV filters (log Kow 6.2) — accumulates in sediment [C2].
* **Synergy:** Frequently used as a solvent/carrier for avobenzone and Tinosorb. Modest triplet quenching of BMDM. No useful synergy reported with octocrylene (overlap in UVB only) [C2].

## Sources
1. Krokidi KM et al. "Insights into the photoprotection mechanism of the UV filter homosalate". PCCP 22 (2020) 18044, doi:10.1039/D0CP02610G.
2. Wong NHM et al. "Photostability of the deprotonated forms of the UV filters homosalate and octyl salicylate". PCCP 24 (2022) 18101.
3. SCCS/1622/20 — Opinion on Homosalate, final 2020. doi:10.2875/95028.
4. Commission Regulation (EU) 2022/1176 amending Annex VI — restriction of homosalate.
5. Couteau C et al. "Study of the photostability of 18 sunscreens in creams". Pharm Res 24 (2007) 1153-1160.
6. Matta MK et al. "Effect of sunscreen application on plasma concentration of sunscreen active ingredients". JAMA 323 (2020) 256-267, doi:10.1001/jama.2019.20747.
7. Mocci F et al. ACS Omega (2025) doi:10.1021/acsomega.5c09234 (DFT spectra).
8. Bonda C. "The Photostability of Organic Sunscreen Actives" in *Sunscreens: Regulations and Commercial Development*, 3rd ed., Marcel Dekker 2005, Ch. 14.
9. Schlumpf M et al. "In vitro and in vivo estrogenicity of UV screens". EHP 109 (2001) 239-244.
10. Stiefel C, Schwack W. Int J Cosmet Sci 36 (2014) 561-572.
