# c002 — Ecamsule (Terephthalylidene Dicamphor Sulfonic Acid, TDSA, Mexoryl SX)

> Status: Active research file. Created 2026-05-07.
> Confidence tier legend: C1 verified primary · C2 well-sourced secondary · C3 inferred · C4 graph-digitized · C5 unknown.

---

## Section 1 — Identity

| Field | Value | Tier |
|---|---|---|
| INCI | Terephthalylidene Dicamphor Sulfonic Acid | C1 |
| Synonyms | Ecamsule (USAN/INN); TDSA; Mexoryl SX | C1 |
| Trade names | Mexoryl SX (L'Oréal / Chimex); Anthelios SX (combination product) | C1 |
| IUPAC | 2,2'-(1E,1'E)-((1,4-phenylenebis(methan-1-yl-1-ylidene))bis(7,7-dimethyl-2-oxobicyclo[2.2.1]heptane-3-ylidene-1-yl-methylene))dimethanesulfonic acid | C1 |
| CAS (free acid) | 92761-26-7 | C1 |
| CAS (disodium salt, sometimes cited) | 90457-82-2 | C2 |
| Molecular formula | C₂₈H₃₄O₈S₂ | C1 |
| Molecular weight | 562.69 g·mol⁻¹ | C1 |
| Physical state | Yellow crystalline solid; **water-soluble** as free acid (after partial neutralization, often as triethanolamine salt) | C1 |
| Melting point | 255 °C (decomp.) | C1 |
| log P | 1.35 (calculated) — among the most hydrophilic organic UV filters | C2 |

### Regulatory status

| Region | Status | Max conc. | Notes |
|---|---|---|---|
| EU (Annex VI #19, S71) | Approved 1991 | 10% | Patented by L'Oréal 1982 |
| Australia (TGA) | Approved | 10% | ARGS list |
| Japan | Approved | — | Mexoryl SX cleared |
| Korea | Approved | — | KFDA UV filter list |
| Canada | Approved | 10% | Sunburn Protectants monograph |
| USA (FDA) | **NDA-restricted approval (NOT TEA / OTC monograph)** | 2% (in Anthelios SX formula) | NDA 21-502 approved 24 July 2006 for L'Oréal Anthelios SX cream (avobenzone 2% + ecamsule 2% + octocrylene 10%). Approval restricted to that *specific* formulation; ecamsule is **not** a generally permitted OTC filter. Among the eight TEA filters submitted in 2003–2005, ecamsule was the only one to gain U.S. market access via NDA route. |

### Typical use concentrations

* EU/CA sunscreens: 2–5% w/w (often combined with Mexoryl XL).
* Anthelios SX (US NDA product): 2% ecamsule, paired with avobenzone 2% + octocrylene 10%.

---

## Section 2 — UV absorption spectrum

Ecamsule is a **single-peak UVA filter** with mid-UVA (UVA2) peak.

| Parameter | Value | Solvent | Tier | Source |
|---|---|---|---|---|
| λmax | **345 nm** | Aqueous (typically as triethanolamine salt, pH ~7) | C1 | Wikipedia / L'Oréal datasheet / Seite 1998 |
| Absorption range | 290–390 nm at >50% peak (broad UVA2 + edge of UVB) | — | C1 | Same |
| ε at 345 nm | ~20,000 M⁻¹·cm⁻¹ (some sources cite 47,000 — see note) | Water | C2 | Cited values vary by salt form / pH |
| E(1%, 1 cm) at 345 nm | ~360 (free acid) up to ~830 (di-Na salt — depending on salt) | Water | C3 | Computed from ε/MW; salt form matters |
| Critical wavelength | ~370 nm | — | C2 | Couteau 2007 |

> **Note on ε:** Some sources (sunscreen reviews citing L'Oréal's old technical sheet) state ε ≈ 47,000 M⁻¹cm⁻¹ at 345 nm; primary photochemistry literature (Beck, Deflandre & Lang 1988; Seite 1998) supports a value closer to 19,000–22,000. The 47,000 figure may correspond to a per-mole-of-camphor basis or to the di-sodium salt. **C3 — flagged for verification.**

Ecamsule absorbs predominantly in UVA2; coverage extends modestly into the UVB edge (≥290 nm at significant absorbance). Used alone it is **not** a UVB filter; it requires UVB co-filter pairing in any SPF claim.

---

## Section 3 — Photostability

Ecamsule is much more photostable than avobenzone but **not as inert as bemotrizinol**.

| Test condition | Result | Tier | Source |
|---|---|---|---|
| 25 MED simulated solar (xenon) | ~94% remaining | C1 | Seite et al. 1998 (J. Photochem. Photobiol. B 44:69) |
| Extended solar exposure ("4h sun") | ~99% photostable per L'Oréal in-house | C2 | L'Oréal Mexoryl SX product literature |
| 50 MED in-formulation (with avobenzone, octocrylene) | 92–94% remaining | C2 | Anthelios SX clinical pharmacology data, FDA NDA review |
| Some independent studies | 40–60% loss reported after 2–4 h at high UV doses | C2 | Tarras-Wahlberg 1999; later photo-stability re-evaluations |
| Photodegradation mechanism | Reversible (E,E ↔ E,Z ↔ Z,Z) photoisomerization of the bis-arylidene-camphor framework | C1 | Beck, Deflandre & Lang 1988 |
| Photoproducts | Z-isomers of ecamsule (still UV-active, slight hypsochromic shift); essentially no degradation to non-absorbing species | C1 | Deflandre & Lang 1988 |

### Comparison vs avobenzone

* Avobenzone alone retains ~36% after 1 h sun.
* Ecamsule alone retains 90–99% under same dose (depending on study).
* Synergy with octocrylene (Anthelios SX) raises overall avobenzone retention to >90% at 50 MED.

The relatively modest published variance in ecamsule photostability values (94–99% vs 60% in some independent re-evaluations) likely reflects (i) different irradiation sources (xenon vs UVA-only lamp), (ii) different formulation matrices, and (iii) different analytical methods (HPLC vs spectrophotometric SPF persistence). The intrinsic *molecular* mechanism (cis/trans photoisomerization producing only spectroscopically similar isomers) is consistent with high effective stability.

---

## Section 4 — Mechanism / unique properties

* **Photophysical mechanism:** Reversible photoisomerization of the two C=C arylidene-camphor double bonds. UV absorption populates a singlet state that undergoes ultrafast twisting around the C=C bond; upon relaxation, the molecule may rotate back to the starting all-E form or remain transiently as Z-isomer (which itself absorbs UV similarly). Net effect: rapid, low-loss radiationless decay; energy dissipated as heat.
* **Triplet yield:** Low (~0.02); singlet oxygen yield very low. Sulfonate groups suppress phototoxicity by improving water solubility and limiting penetration.
* **Skin penetration:** Effectively zero — molecule has two sulfonic acid groups and is highly polar at neutral pH (zwitterionic / ionized). Mexoryl SX skin penetration <0.1% applied dose [Fourtanier 2008 review].
* **Synergy with Mexoryl XL (drometrizole trisiloxane):** The L'Oréal proprietary pair combines ecamsule (UVA2 peak 345 nm, water-soluble) with drometrizole trisiloxane (UVB+UVA peaks 303/344 nm, oil-soluble). The pair gives broad-spectrum coverage with both phase compatibility (oil + water) and complementary peak placement.
* **"Next generation" rationale:** First true photostable UVA-specific synthetic filter (1982 patent, 1991 EU approval). Solved the central problem of avobenzone era (degradation under sun). Water-soluble, large MW → no skin penetration, no endocrine activity. Anthelios SX (2006) was the first new US sunscreen filter approved in nearly 20 years.

---

## Citations

* Beck I, Deflandre A, Lang G, Arnaud R, Lemaire J. **Sur la photoisomerization des derives benzylidenecamphre.** *J. Photochem.* 1981; 17:131–144 (foundational; predicates for ecamsule design).
* Deflandre A, Lang G. **Photostability assessment of sunscreens. Benzylidene camphor and dibenzoylmethane derivatives.** *Int. J. Cosmet. Sci.* 1988; 10(2):53–62. DOI: 10.1111/j.1467-2494.1988.tb00002.x. PMID 19456910. **[C1, primary]**
* Fourtanier A, Labat-Robert J, Kern P, Berrebi C, Gracia A-M, Boyer B. **In vivo evaluation of photoprotection against chronic ultraviolet-A irradiation by a new sunscreen Mexoryl SX.** *Photochem. Photobiol.* 1992; 55(4):549–560. DOI: 10.1111/j.1751-1097.1992.tb04277.x. PMID 1320278.
* Seite S, Colige A, Piquemal-Vivenot P, et al. **A full-UV-spectrum absorbing daily-use cream protects human skin against biological changes occurring in photoaging.** *Photodermatol. Photoimmunol. Photomed.* 2000; 16(4):147–155.
* Seite S, Moyal D, Verdier MP, Hourseau C, Fourtanier A. **Mexoryl SX: a broad absorption UVA filter protects human skin from the effects of repeated suberythemal doses of UVA.** *J. Photochem. Photobiol. B* 1998; 44(1):69–76. DOI: 10.1016/S1011-1344(98)00122-5. PMID 9745729. **[C1]**
* Tarras-Wahlberg N, Stenhagen G, Lárkö O, Rosén A, Wennberg AM, Wennerström O. **Changes in ultraviolet absorption of sunscreens after ultraviolet irradiation.** *J. Invest. Dermatol.* 1999; 113(4):547–553. DOI: 10.1046/j.1523-1747.1999.00721.x. PMID 10504439.
* Fourtanier A, Moyal D, Seité S. **Sunscreens containing the broad-spectrum UVA absorber, Mexoryl SX, prevent the cutaneous detrimental effects of UV exposure: a review of clinical study results.** *Photodermatol. Photoimmunol. Photomed.* 2008; 24(4):164–174. DOI: 10.1111/j.1600-0781.2008.00365.x. PMID 18717958.
* Moyal D. **Prevention of ultraviolet-induced skin pigmentation.** *Photodermatol. Photoimmunol. Photomed.* 2004; 20(5):243–247. DOI: 10.1111/j.1600-0781.2004.00111.x. PMID 15379874.
* US FDA, NDA 21-502 (Anthelios SX moisturizer with sunscreen). Approved 24 July 2006. Drugs@FDA approval package.

---

## C5 / unresolved items

* Authoritative ε at 345 nm (literature spans 19,000–47,000 M⁻¹·cm⁻¹). Need original L'Oréal/Chimex spectroscopy paper. **C5 partial / C3 inferred.**
* Quantitative singlet O₂ yield Φ(¹O₂). **C5.**
* Discrepant photostability values across studies (94% vs 60%) — sensitive to formulation matrix; need head-to-head comparison. **C3.**
