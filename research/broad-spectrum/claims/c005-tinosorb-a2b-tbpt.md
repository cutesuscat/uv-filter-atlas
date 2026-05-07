# c005 — Tinosorb A2B (Tris-Biphenyl Triazine, TBPT)

> Status: Active research file. Created 2026-05-07.
> Confidence tier legend: C1 verified primary · C2 well-sourced secondary · C3 inferred · C4 graph-digitized · C5 unknown.
> **Note:** TBPT exists in two forms — *molecular/dissolved* (sometimes called "monomer") with very different absorption from the *micronized particulate dispersion* used in cosmetics. Cosmetic Tinosorb A2B is the particulate form.

---

## Section 1 — Identity

| Field | Value | Tier |
|---|---|---|
| INCI | Tris-Biphenyl Triazine | C1 |
| INCI (nano form) | Tris-Biphenyl Triazine (nano) | C1 |
| Synonyms | TBPT; 2,4,6-tris(biphenyl-4-yl)-1,3,5-triazine | C1 |
| Trade name | Tinosorb A2B (BASF) | C1 |
| IUPAC | 2,4,6-Tris(4-phenylphenyl)-1,3,5-triazine | C1 |
| CAS | 31274-51-8 | C1 |
| Molecular formula | C₃₉H₂₇N₃ | C1 |
| Molecular weight | 537.66 g·mol⁻¹ | C1 |
| Physical state | White solid; melting point 281.3 °C; supplied to formulators as a **microfine aqueous dispersion** (~150–200 nm primary particle size) | C1 |
| Class | Particulate organic UV absorber (POUA) — same supramolecular concept as Tinosorb M (MBBT) | C1 |
| GHS classification | H413 (long-term aquatic) | C1 |

### Regulatory status

| Region | Status | Max conc. | Notes |
|---|---|---|---|
| EU (Annex VI #29 nano + non-nano entries) | Approved (nano form approved via 2014 amendment; non-nano "S86" added in 2022) | **10%** | SCCS/1429/11 (Dec 2011) opinion supported nano form at 10%; updated SCCS work in 2020s for non-nano TBPT supports 10% |
| Australia (TGA) | Approved | 10% | ARGS list |
| Japan | Status partially listed; check regional CTFA listings | — | C5 confirmation |
| Korea | Status partially listed | — | C5 |
| USA (FDA) | **Not approved.** No TEA submission. Not in foreseeable U.S. market. | — | — |

> **Inhalation restriction:** Per SCCS/1429/11, TBPT (nano) cannot be used in applications that may lead to lung exposure by inhalation (e.g., sprayable powder formats prohibited).

### Typical use concentrations

* Sunscreen creams and lotions: 1–5% (w/w as active TBPT) typical; up to 10% maximum.
* Marketed as "Tinosorb A2B" by BASF since c. 2019, distinct from Tinosorb S (BEMT) and Tinosorb M (MBBT).

---

## Section 2 — UV absorption spectrum

TBPT is a **dual-action particulate organic UV filter** that combines true molecular absorption (UVB peak) with light scattering by submicron particles (UVA contribution).

| Parameter | Value | Solvent / form | Tier | Source |
|---|---|---|---|---|
| λmax (molecular, monomer) | ~310 nm (single peak) | THF / dilute organic solvent | C2 | Naumov, Herzog & Abel 2023 |
| λmax (microfine dispersion in cosmetic) | **~310 nm primary peak (UVB) + broadened shoulder extending into UVA2 (~340 nm)** | Aqueous dispersion | C1 | BASF Tinosorb A2B TDS; Couteau 2015 |
| Apparent λmax of microfine dispersion | Slight hypsochromic shift relative to monomer with long-wavelength tail (scattering contribution) | — | C1 | Naumov 2023 |
| ε of monomer at λmax | ~80,000 M⁻¹·cm⁻¹ (very high — three biphenyl arms in conjugation) | THF | C2 | Naumov 2023 (graph-digitized) |
| Coverage profile | UVB (280–320 nm) with absorption + UVA2 (320–340 nm) by molecular absorption + scattering enhancing apparent UVA protection | — | C1 | BASF; Couteau 2015 |
| Particle size (microfine) | 150–200 nm primary (sub-micron), per BASF | — | C2 | BASF TDS |
| Critical wavelength | ~370 nm (in formulation, with scattering) | — | C2 | Couteau 2015 |

> **Key conceptual point:** TBPT in solution is a *UVB-only* absorber. The dispersion form in cosmetics gains apparent broad-spectrum protection because the 150–200 nm particles **scatter** UVA light (Mie scattering), in addition to molecularly absorbing UVB. Naumov et al. 2023 explicitly explores how the spectrum changes from monomer to nanoparticle.

---

## Section 3 — Photostability

TBPT is reported as essentially photostable in cosmetic dispersion form, similar to its triazine cousin Tinosorb M.

| Test condition | Result | Tier | Source |
|---|---|---|---|
| Dispersion in O/W formulation, simulated solar | "Excellent photostability" — no significant absorbance loss | C2 | BASF TDS; SCCS/1429/11 dossier |
| Couteau 2015 in vitro photoprotective efficacy | Stable SPF performance under irradiation | C1 | Couteau 2015 |
| Photoproducts | None characterized | C5 | — |
| Ultrafast photophysics | Sub-ps internal conversion in monomer; deactivation in nanoparticle form involves both excitonic delocalization and inter-molecule energy transfer | C1 | Naumov 2023 |

The triazine core with three biphenyl arms is geometrically rigid and electron-rich. Naumov et al. demonstrated by ultrafast spectroscopy that the singlet excited state decays in <10 ps via internal conversion both as monomer and as aggregate. No long-lived triplet, no detectable singlet oxygen yield in their measurements.

---

## Section 4 — Mechanism / unique properties

* **Photophysics:** Symmetric C₃ triazine with three biphenyl chromophores. Excited singlet decays via fast IC (< 10 ps) involving twisting of biphenyl arms relative to the triazine core. In particle form, exciton delocalization across multiple TBPT molecules adds an additional fast deactivation path.
* **Particulate UV filter rationale:** Three benefits over molecular filters:
    1. **Molecular absorption** of UVB (high ε ~ 8 × 10⁴).
    2. **Mie scattering** of UVA from sub-micron particles (similar in concept to TiO₂/ZnO).
    3. **Zero skin penetration** — particles cannot cross stratum corneum.
* **Comparison to Tinosorb M (MBBT, methylene bis-benzotriazolyl tetramethylbutylphenol):** Same particulate-organic concept; MBBT covers UVB + UVA1 (peaks ~305 + 360 nm), while TBPT covers UVB + UVA2 (peaks ~310 + scattering shoulder to ~340–350 nm). The two are positioned as complementary in the BASF Tinosorb portfolio.
* **"Next generation" rationale:** Hybrid molecular-absorber + particulate-scatterer; very low skin uptake; broad UVB+UVA2 coverage; can replace need for high inorganic loadings; combined with BEMT and bisoctrizole gives complete UVB+UVA1+UVA2 coverage with fully photostable filters.
* **Inhalation safety constraint:** Because the molecule is in particulate form, SCCS prohibits formulations leading to end-user lung exposure (i.e., no aerosol spray products). This is identical to the constraint on Tinosorb M and on TiO₂ nano.

---

## Citations

* Naumov S, Herzog B, Abel B. **Spectra and photorelaxation of tris-biphenyl-triazine-type UV absorbers: from monomers to nanoparticles.** *Photochem. Photobiol. Sci.* 2023; 22(9):2143–2151. DOI: 10.1007/s43630-023-00436-y. PMID 37277672. **[C1 — primary photophysics]**
* Couteau C, Paparis E, Chauvet C, Coiffard L. **Tris-biphenyl triazine, a new ultraviolet filter studied in terms of photoprotective efficacy.** *Int. J. Pharm.* 2015; 487(1–2):120–123. DOI: 10.1016/j.ijpharm.2015.03.077. PMID 25843762. **[C1]**
* SCCS (Scientific Committee on Consumer Safety). **Opinion on 1,3,5-Triazine, 2,4,6-tris[1,1'-biphenyl]-4-yl- (S79 / S86 entries). SCCS/1429/11**, revision adopted 13–14 Dec 2011. **[C1 regulatory]**
* BASF. **Technical Information Tinosorb® A2B. PRD 30478125** (valid since 12 March 2019). BASF Care Creations / Personal Care.
* European Commission. **Commission Regulation (EU) on Annex VI of Regulation (EC) No 1223/2009** — entries adding tris-biphenyl triazine in nano (2014) and non-nano (2022) form, max 10%.
* Bernerd F, Passeron T, Castiel I, Marionnet C. **The damaging effects of long UVA (UVA1) rays.** *Int. J. Mol. Sci.* 2022; 23(15):8243. DOI: 10.3390/ijms23158243.

---

## C5 / unresolved items

* Quantitative photostability data (% remaining vs MED dose) in primary peer-reviewed sources. SCCS dossier referenced but not extracted. **C5.**
* Numerical ε in monomer form at 310 nm, peer-reviewed value. **C3 (graph-digitized).**
* Exact particle-size distribution of commercial Tinosorb A2B dispersion. **C2.**
* Singlet oxygen quantum yield Φ(¹O₂). **C5.**
* Confirmed Korea / Japan regulatory listing. **C5.**
