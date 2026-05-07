# c004 — Mexoryl 400 (MCE / S87 — Methoxypropylamino Cyclohexenylidene Ethoxyethylcyanoacetate)

> Status: Active research file. Created 2026-05-07.
> Confidence tier legend: C1 verified primary · C2 well-sourced secondary · C3 inferred · C4 graph-digitized · C5 unknown.
> **Note:** Mexoryl 400 is the *newest* approved UV filter (EU 2019, commercial 2022 — La Roche-Posay UVMune 400; broad rollout 2024). Public peer-reviewed data is limited; many parameters remain C5.

---

## Section 1 — Identity

| Field | Value | Tier |
|---|---|---|
| INCI | Methoxypropylamino Cyclohexenylidene Ethoxyethylcyanoacetate | C1 |
| Synonyms | MCE; S87 (EU code); Mexoryl 400 | C1 |
| Trade name | Mexoryl 400 (L'Oréal — exclusive); developed jointly by L'Oréal and BASF | C1 |
| IUPAC | 2-Ethoxyethyl (2Z)-2-cyano-2-[3-(3-methoxypropylamino)cyclohex-2-en-1-ylidene]acetate | C1 |
| CAS | 1419401-88-9 | C1 |
| Molecular formula | C₁₇H₂₆N₂O₄ | C1 |
| Molecular weight | 322.41 g·mol⁻¹ | C1 |
| Physical state | Yellow solid powder; oil-soluble (lipophilic) | C1 |
| Melting point | 85–120 °C (range reported) | C1 |
| Solubility | Phenoxyethanol, dimethyl capramide, ethoxydiglycol, dimethyl isosorbide, alcohol (at 25 °C); poorly water-soluble | C2 |
| Chemical class | Cyclic merocyanine (donor–π–acceptor push–pull dye) | C1 |

### Regulatory status

| Region | Status | Max conc. | Notes |
|---|---|---|---|
| EU (Annex VI new entry) | **Approved 2019** via Regulation 2020/1684 (added as S87) | **3%** | Based on SCCS/1605/19 (final opinion adopted 13 Dec 2019) |
| Australia (TGA) | Approved (post-2020) | 3% | Following EU |
| Japan | Status pending — not yet listed | — | C5 |
| Korea | Status pending — not yet listed | — | C5 |
| USA (FDA) | **Not approved.** No TEA submission has been made (this filter was discovered after the original 8 TEA submissions in 2003–2005). | — | Likely no US market access in foreseeable future |

### Typical use concentrations

* Single permitted maximum: **3 %** in EU.
* La Roche-Posay UVMune 400 (commercial 2022, mass rollout 2024): MCE typically ~1 %; combined with avobenzone (3%), bemotrizinol, octocrylene, ethylhexyl triazone, drometrizole trisiloxane, etc., for full-spectrum SPF 50+.

---

## Section 2 — UV absorption spectrum

MCE is a **single-peak deep-UVA1 filter** — uniquely targeting the previously under-protected 370–400 nm "ultra-long UVA" band.

| Parameter | Value | Solvent | Tier | Source |
|---|---|---|---|---|
| λmax | **385 nm** | Ethanol / hydroethanolic / cosmetic vehicle | C1 | SCCS/1605/19; Marionnet 2022; Wikipedia |
| ε at 385 nm | **63,052 L·mol⁻¹·cm⁻¹** (≈6.3 × 10⁴) | Ethanol | C2 | Cited in product/secondary review literature; SCCS dossier |
| E(1%, 1 cm) at 385 nm | ≈1956 (computed: ε × 10 / MW = 63052 × 10 / 322.41) | Ethanol | C3 | Computed |
| Spectral coverage | ~340–400 nm at >50% peak; significant absorbance to ~410 nm | — | C2 | Marionnet 2022 |
| Critical wavelength | ~389 nm (per Marionnet; in formula) | — | C2 | Marionnet 2022 |
| Coverage profile | Almost no UVB activity; primarily UVA1 with some UVA2 | — | C1 | Same |

The molecule is a *cyclic merocyanine* — a push-pull chromophore with the methoxypropylamino group (electron donor, secondary amine) and the cyanoacetate (electron acceptor) connected through a cyclohexenylidene π-bridge. The exceptionally long λmax (385 nm) is uncommon for cosmetic-approved filters; the closest analogue in regulatory inventory is Disodium Phenyl Dibenzimidazole Tetrasulfonate (335 nm) and DHHB (354 nm).

---

## Section 3 — Photostability

MCE is reported to be **highly photostable**, though peer-reviewed photokinetic data is limited.

| Test condition | Result | Tier | Source |
|---|---|---|---|
| Solar simulator irradiation, in-formula (50 J/cm² UVA1) | "No significant photodegradation detected" | C2 | Marionnet 2022 |
| Hydroethanolic solution, accelerated UV stress | "100% intrinsic stability"; thermostable in different media | C2 | L'Oréal/BASF technical literature, secondary review |
| Photostability under high O₂ concentration | Stable | C2 | Same |
| Photoproducts | None characterized in published in-formula studies | C5 | — |
| Comparison vs avobenzone | MCE retains essentially full absorbance under conditions that degrade avobenzone by 30–50% | C2 | Marionnet 2022 (in-formula) |

### Mechanism

Cyclic merocyanines decay from the S₁ state via ultrafast twisted intramolecular charge-transfer (TICT) relaxation around the central C=C bond (analogous to ecamsule/cinnamate isomerization but with constrained geometry). The cyclohexenylidene ring constrains the barrierless twist back to ground state, giving radiationless decay with negligible bond breaking.

Key point: unlike avobenzone (which has UVB-active photoproducts), and ecamsule (which generates Z-isomers), MCE has shown no published photoproducts under standard solar-simulator conditions — but data is from L'Oréal/BASF-sponsored literature only.

---

## Section 4 — Mechanism / unique properties

* **Photophysical mechanism:** Push–pull merocyanine with TICT/torsional relaxation. Absorption populates an intramolecular charge-transfer state; ultrafast twisting around C=C of the cyclohexenylidene–cyanoacetate exocyclic double bond returns molecule to ground state without bond cleavage.
* **Triplet/ROS yield:** Reportedly very low; Φ(¹O₂) not published. C5 quantitative.
* **Why this matters — the "ultra-long UVA1" gap:** Until 2019, most UVA filters (avobenzone λmax 357 nm, ecamsule 345, DHHB 354) had absorbance falling rapidly above 380 nm. The 380–400 nm band ("ultra-long UVA") penetrates deepest into dermis, drives most photoaging and pigmentary disorders, and was only weakly attenuated by inorganic ZnO. MCE is the first organic filter with *peak* absorbance at 385 nm — closing the protection gap above 380 nm.
* **Clinical UVA1 efficacy (Marionnet 2022, Bernerd 2022, de Dormael 2022, Flament 2024):** In RCTs MCE-containing formulae reduced UVA1-induced pigmentation, dermal alteration, MMP-1 expression, IL-1/IL-6 expression in a 50 J/cm² UVA1 challenge; Flament 2024 showed measurable reduction of pigmentation/aging signs over 8 weeks of real-life sun exposure compared to MCE-free SPF50 control.
* **Safety constraint:** SCCS/1605/19 noted MCE is a secondary amine prone to N-nitrosation. Cosmetic formulations must keep nitrosamine impurities <50 ppb and avoid nitrosating co-formulants (e.g., bronopol, 2-bromo-2-nitropropane-1,3-diol). One case of severe allergic contact dermatitis was reported in 2024 (Loretan et al.) — first published sensitization signal for the molecule.
* **"Next generation" rationale:** First-in-class for ultra-long UVA1 organic filtration; closes the photoaging-relevant >380 nm gap; high ε at peak (~6.3 × 10⁴); photostable; complementary spectrum to BEMT and avobenzone.

---

## Citations

* Winkler B, Hoeffken HW, Eichin K, Houy W. **A cyclic merocyanine UV-A absorber: mechanism of formation and crystal structure.** *Tetrahedron Lett.* 2014; 55(10):1749–1751. DOI: 10.1016/j.tetlet.2014.01.113. **[C1 — original chemistry, BASF]**
* SCCS (Scientific Committee on Consumer Safety). **Opinion on Methoxypropylamino Cyclohexenylidene Ethoxyethylcyanoacetate (S87) — Submission II. SCCS/1605/19**, final opinion adopted 13 Dec 2019. **[C1, regulatory]**
* European Commission. **Commission Regulation (EU) 2020/1684** of 12 Nov 2020 amending Annex VI to Regulation (EC) No 1223/2009 of the European Parliament and of the Council on cosmetic products. (Adds Methoxypropylamino Cyclohexenylidene Ethoxyethylcyanoacetate at 3% max.)
* Marionnet C, de Dormael R, Marat X, et al. **Sunscreens with the new MCE filter cover the whole UV spectrum: improved UVA1 photoprotection in vitro and in a randomized controlled trial.** *JID Innov.* 2021; 2(1):100070. DOI: 10.1016/j.xjidi.2021.100070. PMID 35072138. **[C1]**
* de Dormael R, Marionnet C, Bastien P, et al. **Improvement of photoprotection with sunscreen formulas containing the cyclic merocyanine UVA1 absorber MCE: in vivo demonstration under simulated and real sun exposure conditions in three randomised controlled trials.** *JEADV Clin. Pract.* 2022; 1(3):229–239. DOI: 10.1002/jvc2.38.
* Bernerd F, Passeron T, Castiel I, Marionnet C. **The damaging effects of long UVA (UVA1) rays: a major challenge to preserve skin health and integrity.** *Int. J. Mol. Sci.* 2022; 23(15):8243. DOI: 10.3390/ijms23158243. PMC 9368482.
* Flament F, Bourokba N, Nouveau S, et al. **The impact of methoxypropylamino cyclohexenylidene ethoxyethylcyanoacetate (MCE) UVA1 filter on pigmentary and ageing signs: an outdoor prospective 8-week randomized intra-individual comparative study in two populations of different genetic background.** *J. Eur. Acad. Dermatol. Venereol.* 2024; 38(1):214–222. DOI: 10.1111/jdv.19486. PMID 37655436.
* Aguilera J, Gracia-Cazaña T, Gilaberte Y. **New developments in sunscreens.** *Photochem. Photobiol. Sci.* 2023; 22(10):2473–2482. DOI: 10.1007/s43630-023-00453-x. PMID 37543534.
* Loretan A, Spring P, Christen-Zaech S, Bonnet A. **Severe allergic contact dermatitis caused by methoxypropylamino cyclohexenylidene ethoxyethylcyanoacetate.** *Contact Dermatitis* 2025. DOI: 10.1111/cod.14700. PMID 39305114.

---

## C5 / unresolved items

* Quantitative photostability metrics (% remaining at defined MED / J·cm⁻²) in peer-reviewed primary photochemistry literature — only sponsor-derived data found. **C5.**
* Quantum yields Φ_F, Φ_ISC, Φ(¹O₂), Φ(•O₂⁻) — none published. **C5.**
* Detailed photoproduct identification under solar simulation. **C5.**
* Japan / Korea regulatory listing dates. **C5.**
* Skin penetration percentages (cited as low; actual values not in public data). **C5.**
