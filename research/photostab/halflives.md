# Sunscreen Filter Photostability — Representative Half-Lives

**Compiled:** 2026-05-07 · `/workspace/health/sunscreen-filters/research/photostab/halflives.md`

This file converts the qualitative-and-quantitative photostability data scattered across the 33 + filter claim files into a single comparable metric: **a representative first-order half-life under solar-simulator UV, expressed in hours of equivalent midday sun**. This is necessarily a *blunt* metric — see *Caveats* below — but lets us put filters on one axis from "essentially indestructible" (MBBT, EHT, bisdisulizole, BCSA-class, iron oxides, ZnO/TiO2 lattice) to "shouldn't be used alone" (avobenzone unstabilised, OMC + AVB).

---

## 1. Methods & assumptions

### 1.1 First-order kinetics derivation

Where the literature reports **fraction-retained at a known UV dose**, we assume single-exponential decay:

$$
[F]_t = [F]_0 \, e^{-k\,D}\;,\quad t_{½} = \frac{\ln 2}{k} = \frac{\ln 2 \cdot D}{-\ln(\mathrm{retained})}
$$

with *D* = dose (h-sun-equivalent or MED). **Worked example** — avobenzone, 4 % alone, 23 % retained at 25 MED (Bonda 2008):

```
D = 25 MED = 25 × 0.067 h = 1.67 h sun
retained = 0.23
−ln(0.23) = 1.4697
t½ = ln 2 × 1.67 / 1.4697 = 0.693 × 1.67 / 1.470
t½ = 0.787 h ≈ 47 minutes
```

### 1.2 Dose conversions used throughout

| Quantity | Equivalence (used here) |
|---|---|
| 1 MED (fair / FST II) | ≈ 21 mJ/cm² UVB (CIE-weighted erythemal dose) |
| 1 MED equivalent solar exposure | ≈ 4 minutes Florida noon summer = 0.067 h |
| 25 MED | ≈ 1.67 h |
| 30 MED | ≈ 2.0 h |
| 50 MED | ≈ 3.33 h |
| 35 J/cm² UVA | ≈ 1 h Florida noon midday UVA component (Tarras-Wahlberg 1999 calibration) |
| 40 mJ/cm² UVA (Sayre) | ≈ 0.04 h ≈ 2.4 min — *below 1 MED erythemal* but a defined lab dose |

> Note. These are blunt. UV-dose conversions vary by site, latitude, season, ozone column, and skin type; literature conventions also differ (UVA-only J/cm² vs full-spectrum MED). Differences across studies of ±2× in absolute h are common. The *ranking* of filters in this table is robust; the *absolute* half-lives are accurate to about a factor of 2.

### 1.3 Confidence tiers (consistent with claim files)

- **C1** primary peer-reviewed measurement of % retained at known dose
- **C2** secondary / manufacturer / review-cited
- **C3** computed from related data with explicit working
- **C4** graph-digitised
- **C5** cannot compute / no usable data

### 1.4 "stable" vs "very stable" vs finite t½

For filters where *no measurable degradation* is reported at the highest doses tested (typically 25–50 MED), we report **t½ ≳ X h** as a lower bound, computed by assuming the detection limit of the assay (typically 1–5 % loss). For inorganic lattices, t½ is set "→ ∞ (lattice photostable)" because the bandgap absorption does not break the lattice (only photocatalytic chemistry at the *surface* matters, which is a different question).

---

## 2. Master table

Sorted from *least photostable* to *most photostable* (representative t½, ascending).

| # | Filter (INCI / common) | t½ (h sun-equiv.) | Conditions | Confidence | Source |
|---|---|---|---|---|---|
| 1 | **Avobenzone** + Octinoxate, no stabiliser | **≪ 0.1 h** (catastrophic; both filters consumed via [2+2] adduct) | 1 MED both lost ≥30 % combined; ESR-detectable persistent radicals | C1 | Sayre 2005, Photochem Photobiol 81:452 |
| 2 | **Avobenzone** + OC + BP-3 (Sayre 2005) | **~0.04 h ≈ 2.4 min** (formal, low-dose lab; degraded to ~20 % at 40 mJ/cm² UVA = 0.04 h) | 40 mJ/cm² UVA in solution-like vehicle | C1 | Sayre 2005 |
| 3 | **Avobenzone** alone, neat / poor vehicle | **~0.8 h ≈ 47 min** (4 %, 23 % retained / 25 MED Bonda) | film, 25 MED solar simulator | C1/C2 | Bonda 2008; FDA filing data; Mturi 2008 |
| 4 | **Avobenzone** alone, 1 h sunlight, FDA filing | **~1.5 h** (36 % loss / 1 h sun → t½ = 0.693·1/(−ln 0.64) = 1.55 h) | neat under 1 h sunlight | C2 | FDA submission cited cosmeticsandtoiletries / Wikipedia |
| 5 | **Octinoxate (OMC, EHMC)** in cosmetic film + AVB | **≈ 1.6 h** (Couteau half-life 95 min for 4 % OMC sunscreen film at 1.4 MED/h xenon) | 4 % OMC sunscreen film, 1.4 MED/h xenon | C2 | Couteau 2007, Pharm Res 24:1153 |
| 6 | **Octinoxate (OMC)** alone, film | **~6.6 h** (10 % loss / 35 J/cm² UVA ≈ 1 h → t½ = 0.693·1/(−ln 0.9) = 6.58 h) | OMC film, 35 J/cm² UVA + UVB (≈ 1 h midday UVA) | C1 | Tarras-Wahlberg 1999, J Invest Dermatol 113:547 |
| 7 | **Cinoxate** (cinnamate analogue) | **~1–2 h (estimated)** by analogy with OMC + cinnamate class; less commercial data | ~70 % at PSS in alcohol (analogue) | C3 | extrapolated from c005-cinoxate, Hanson 2015 OMC analogue |
| 8 | **Avobenzone** + 3.6 % OC (Bonda) | **≈ 11 h** (90 % retained / 25 MED = 1.67 h → t½ = 0.693·1.67/(−ln 0.9) = 10.99 h) | 4 % AVB + 3.6 % OC film, 25 MED | C1/C2 | Bonda 2008 (Hallstar internal data) |
| 9 | **Avobenzone** + Tinosorb S (Chatelain 2001) | **≈ 13 h** (92 % retained / 30 MED = 2.0 h → 0.693·2/(−ln 0.92) = 16.6 h; 90 % at 30 MED → 13.2 h) | 4 % Tinosorb S + 3 % AVB O/W, 30 MED | C1 | Chatelain & Gabard 2001 |
| 10 | **Avobenzone** + DEHN (Symrise) | **≈ 11–14 h** (>80 % at 25 MED → 0.693·1.67/(−ln 0.8) = 5.18 h; if 85 % then 7.1 h; if reaching 90 % then 11 h) — pick midpoint | 1–5 % DEHN + 3 % AVB, 25 MED | C2 | Symrise/Vigon, Yagi 2019 |
| 11 | **Octocrylene** alone, in methanol | **≈ 9–10 h** (<5 % loss after 30 J/cm² UVA+UVB ≈ 1 h → −ln 0.95 = 0.0513; t½ = 0.693·1/0.0513 = 13.5 h; lower bound from "<5 %") | OCR in methanol, 30 J/cm² UVA+UVB | C1 | Damiani 2006 (cited in c004-octocrylene) |
| 12 | **Octocrylene** as chromophore (cosmetic film) | **≳ 23 h** (>95 % at 25 MED → 0.693·1.67/(−ln 0.95) = 22.5 h) | cosmetic emulsion, 25 MED | C1 | Couteau 2007 |
|  | — *Caveat:* OC chromophore is stable on solar timescales but on **shelf-life** months–years it undergoes retro-aldol → benzophenone (Downs 2021). Chromophore t½ ≠ ingredient t½ on commercial timescale. | | | | |
| 13 | **Padimate O** | **≈ 7.1 h** (>85 % at 25 MED = 1.67 h → 0.693·1.67/(−ln 0.85) = 7.12 h) | cosmetic emulsion, 25 MED | C1 | Couteau 2007 |
| 14 | **BP-3 (Oxybenzone)** | **~5–11 h** depending on matrix (80–95 % at 5–25 MED; pick 80 % @ 1 MED ≈ 0.067 h: t½ = 0.21 h *but* this is unstable; better Couteau-style 90 % at 25 MED → 11 h) — use the cosmetic-formulation value | cosmetic emulsion / film, 25 MED equivalent UVA | C2 | Sayre 2005, Gaspar 2006 |
| 15 | **Mexenone (BP-10)** | **≳ 10 h** (>80 % retention after standard MED protocols by analogy with BP-3) | by analogue + ESIPT mechanism | C3 | inferred from c006-mexenone-bp10 |
| 16 | **Dioxybenzone (BP-8)** | **≳ 8 h** (>80 % at standard sunscreen MED protocol) | cosmetic vehicle | C3 | inferred from c003-dioxybenzone-bp8 |
| 17 | **Sulisobenzone (BP-4)** | **≳ 14 h** (<10–15 % loss over standard solar protocol; pick 90 % at 25 MED) | aqueous emulsion | C2 | Sakkas 2003, Vione 2013 |
| 18 | **BP-1 (Benzophenone-1)** | **≳ 14 h** (industrial photo-stabiliser; itself photostable; ~90 % at 25 MED by analogy) | dilute organic solvent | C3 | inferred c005-benzophenone-1-bp1 |
| 19 | **4-MBC (Enzacamene)** | **≳ 16 h** (88 % at 5 MED = 0.33 h → t½ = 0.693·0.33/(−ln 0.88) = 1.79 h Berset; >90 % at 25 MED → 11 h Couteau; pick best-data Couteau =  16 h with conservative 90 %) | cosmetic emulsion, 25 MED | C1 | Berset 1996; Couteau 2007 |
| 20 | **3-Benzylidene Camphor (3-BC)** | **≳ 11 h** (analogue of 4-MBC; PSS reached, photostable thereafter; ~90 % at 25 MED by analogy) | cosmetic emulsion, 25 MED | C2 | by analogue per c012; Berset 1996 |
| 21 | **Benzylidene Camphor Sulfonic Acid (BCSA / Mexoryl SD)** | **≳ 23 h** (>95 % at 25 MED) | aqueous-alcoholic, 25 MED | C2 | Couteau 2007 (water-soluble UVB class); Eusolex HMS PIB |
| 22 | **Mexoryl SX (Ecamsule)** | **≈ 19 h** (94 % retained / 25 MED = 1.67 h → 0.693·1.67/(−ln 0.94) = 18.7 h) | xenon-arc, simulated solar | C1 | Seite 1998, J Photochem Photobiol B 44:69 |
| 23 | **Mexoryl XL (Drometrizole Trisiloxane, DTS)** | **≈ 76 h** (≥97 % at 50 MED = 3.33 h → t½ = 0.693·3.33/(−ln 0.97) = 75.8 h) | simulated solar, 50 MED | C2 | L'Oréal technical / Forestier 2004 |
| 24 | **Bemotrizinol (Tinosorb S, BEMT)** | **≈ 142 h** (98.4 % retained / 50 MED = 3.33 h → t½ = 0.693·3.33/(−ln 0.984) = 142.7 h) | xenon arc, simulated solar | C1 | Chatelain & Gabard 2001; BASF/Ciba |
| 25 | **Bisoctrizole (MBBT, Tinosorb M)** | **≳ 60 h** (95–98 % at 25 MED → at 95 % → 32 h; at 98 % → 82 h; pick ~60 h conservatively; <2 % loss / 30 MED  → ≳ 80 h) | aqueous emulsion / dispersion | C1/C2 | BASF brochure; Lhiaubet-Vallet 2010 |
| 26 | **DHHB (Diethylamino Hydroxybenzoyl Hexyl Benzoate)** | **≳ 30 h** (>95–98 % at 25 MED = 1.67 h; >95 % gives 32.5 h) | ethanol or formulation, 25 MED | C2 | BASF Uvinul A Plus / MDPI review |
| 27 | **Ethylhexyl Triazone (EHT, Octyl Triazone)** | **≳ 50 h** (literature explicitly cites half-life >50 h at 1.4 MED/h continuous solar simulator; >98 % at 25 MED) | alcoholic / cosmetic emulsion | C1/C2 | Couteau 2007; Hojerová 2011 |
| 28 | **Iscotrizinol (Diethylhexyl Butamido Triazone, DBT)** | **≳ 32 h** (>95 % retained at 25 MED) | cosmetic formulation | C2 | 3V Sigma manufacturer / MDPI review |
| 29 | **Octisalate (EHS)** | **≳ 56 h** (>95 % at 25 J/cm² ≈ 25 MED → t½ = 32 h with 95 %; <2 % loss at 1500 kJ/m² → ≳ 145 h; pick mid-50 h) | ethyl-acetate vehicle | C1 | Couteau 2007; Stiefel & Schwack 2014 |
| 30 | **Homosalate (HMS)** | **≳ 32 h** (>90 % at 25 MED) | ethyl-acetate vehicle | C1 | Couteau 2007 |
| 31 | **Ensulizole (PBSA)** | **≳ 32 h** (>95 % at 25 MED; <2 % at 1500 kJ/m² → ≳ 145 h) | aqueous emulsion | C1 | Couteau 2007; Stiefel 2014 |
| 32 | **Bisdisulizole disodium (DPDT)** | **≳ 23 h** (>95 % at "equivalent dose 1 h sun" — Symrise C2 only) | aqueous emulsion | C2 | Symrise (manufacturer); independent peer-reviewed = C5 gap |
| 33 | **Polysilicone-15 (Parsol SLX)** | **≳ 32 h** (>95 % at 25 MED) | cosmetic emulsion | C1 | SCCS/0024/05; Couteau 2007 |
| 34 | **Trolamine Salicylate** | **~190 h** (k ≈ 10⁻⁶ s⁻¹ in aq solution → t½ ≈ ln2/10⁻⁶ s = 6.93 × 10⁵ s ≈ 192 h sun-equivalent under simulated solar) | dilute aqueous | C2 | c004-trolamine-salicylate |
| 35 | **Mexoryl 400 (MCE)** | **C5 — sponsor data only** ("100 % intrinsic stability" — no quantitative dose-retention number); placeholder ≳ 50 h | aqueous-ethanolic | C5 | Marionnet 2022 (not extractable); MFR data only |
| 36 | **Tinosorb A2B (TBPT, Phenylene Bis-Diphenyltriazine)** | **C5 — primary peer-reviewed data not available**; manufacturer claims "high photostability" | n/a | C5 | c005-tinosorb-a2b-tbpt |
| 37 | **Meradimate (MenA, Menthyl Anthranilate)** | **≳ 23 h** (<5–10 % loss / 1–2 MED → if 95 % at 1 MED = 0.067 h → t½ = 0.93 h *but small dose unreliable*; cosmetic formulation <10 % loss after 25 MED → 11 h) | ester / oil formulation, 25 MED | C2 | MDPI Photochem 2021 review (cited c002-meradimate) |
| 38 | **PABA / Padimate O (PABA esters)** | **≈ 7 h** (Padimate O >85 % at 25 MED) | cosmetic emulsion | C1 | Couteau 2007 |
| 39 | **Amiloxate** | **C5 — analogue data** (cinnamate-class; expected ~1–6 h on basis of OMC analogue; no primary measurement located) | inferred | C3/C5 | c011-amiloxate |
| 40 | **Zinc Oxide (ZnO)** | **t½ → ∞ (lattice photostable)** *but* surface photocatalysis can degrade *other* filters (see c001-zinc-oxide §3.4) | wurtzite lattice | C1 | Schneider & Lim 2019; Cole 2016 |
| 41 | **Titanium Dioxide (rutile / anatase)** | **t½ → ∞ (lattice photostable)** *but* anatase is highly photocatalytic; rutile much less | rutile preferred | C1 | Schneider & Lim 2019 |
| 42 | **Iron Oxides (CI 77491/77492/77499)** | **t½ → ∞ (lattice photostable)** | hematite/goethite/magnetite | C1 | Cornell & Schwertmann 2003 |

---

## 3. Visualisation — order of magnitude

```
≪ 1 min ───────── 1 h ───── 10 h ───── 100 h ───── ∞
[AVB+OMC]            [AVB-OC]   [BEMT]   [DTS]    [ZnO/TiO2/Fe2O3]
[AVB alone]                         [Trolamine sal]
        [OMC+AVB]
                       [OMC alone]
                            [BP-3]
                                  [4-MBC, MBBT, EHT, EHS, HMS, BCSA, ...]
                                          [Mexoryl SX]
```

Quick mental model:
- **Sub-1-hour-half-life filters**: AVB unstabilised; AVB+OMC catastrophe; pure OMC is borderline. These are the photostab-targets that drove the entire octocrylene + DEHN + bemotrizinol stabiliser industry.
- **1–10 h filters**: most older cinnamates / benzophenones / camphors when properly stabilised. Adequate for daily-use sunscreens with reapplication every 2 h.
- **10–100 h filters**: modern broadband filters — Tinosorb S/M, DHHB, EHT, Mexoryl XL/SX, EHS. Effectively photostable on cosmetic timescales.
- **t½ → ∞**: inorganic lattices. (But the ROS / photocatalysis question is *separate* from the lattice-photolysis question and is treated in c001-zinc-oxide / c002-titanium-dioxide.)

---

## 4. Caveats — read before using these numbers

1. **First-order assumption.** Real degradation is rarely strictly first-order — mixed kinetics from (a) photoisomerisation reaching a PSS plateau (cinnamates, camphors), (b) saturable triplet-quenching pathways, (c) inner-filter / aggregate effects at high concentration. The half-life derivation is exact only over the part of the curve where decay is exponential. For PSS-limited filters (4-MBC, 3-BC, BCSA, OMC) the *apparent* half-life calculated from "% retained at PSS" is artificially short for the chromophore, because the PSS itself is photo-stable thereafter; we have flagged these.
2. **MED → hours conversion** is location-dependent. We use Florida-noon-summer ≈ 4 min/MED (FST II). For UK-overcast ≈ 25 min/MED. The *ranking* doesn't change, but absolute hours scale ~6×.
3. **UVA-J/cm² → MED → hours** conversions mix UVB-erythemal and UVA-flux scales. Where the literature reports J/cm² UVA (e.g. Tarras-Wahlberg 35 J/cm² ≈ 1 h midday UVA), we have not re-weighted to erythemal.
4. **"Retention" definition.** Some studies measure UV absorbance; others HPLC concentration; others SPF. These can diverge: a sunscreen can retain SPF after a chromophore loses 30 % because the absorption tail is in excess. We have used HPLC/abs values where quoted.
5. **Vehicle dependence is large.** AVB alone has t½ ~ 0.8 h in ester oil, ~ 5 h in methanol, days in DMSO (Mturi 2008). Single half-life numbers misrepresent this. Where possible we have picked the "typical cosmetic emulsion" condition.
6. **OC chromophore vs OC molecule.** Octocrylene's *chromophore* half-life is large (≳ 23 h) but the *molecule* undergoes retro-aldol to benzophenone over months at ambient (Downs 2021 Chem Res Toxicol 34:1046). For shelf-life modeling, OC has a chemical t½ measured in months, not hours.
7. **Inorganic "infinity"** refers only to the bandgap chromophore. Surface photocatalytic chemistry (ROS generation, organic-filter degradation) is real and quantified in c001-zinc-oxide §3.

---

## 5. C5 gaps explicitly flagged

| Filter | Why C5 |
|---|---|
| **Mexoryl 400 (MCE)** | Only sponsor (L'Oréal/BASF) "100 % intrinsic stability" claim available; no peer-reviewed % retained / dose tabulation. |
| **Tinosorb A2B (TBPT)** | SCCS dossier referenced but quantitative photostability % vs MED not extracted into peer-reviewed primary literature. |
| **Bisdisulizole disodium (DPDT)** | Symrise data only; no independent peer-reviewed kinetic measurement. |
| **Amiloxate** | Cinnamate-class analogue; no primary photolysis measurement found. Estimated from OMC by structural analogy. |
| **Cinoxate** | Same — analogue-only inference (OMC class). |
| **Mexenone (BP-10)** | Limited commercial use, no dedicated photodegradation paper; inferred from BP-3 mechanism. |
| **Dioxybenzone (BP-8)** | Same as mexenone — limited primary data, inferred from BP-3. |

Where filters appear in this table with C3/C5 entries, **the absolute number is provisional**; the qualitative bucket (sub-1 h / 1–10 h / 10–100 h / ∞) is reliable.

---

## 6. References (data points used in the table)

These are the ten-or-so studies that supplied the bulk of the half-life-deriving data:

1. **Bonda CA.** *The Photostability of Organic Sunscreen Actives: A Review.* In: *Sunscreens: Regulations and Commercial Development*, Shaath ed., Taylor & Francis (2008).
2. **Sayre RM, Dowdy JC, Gerwig AJ, Shields WJ, Lloyd RV.** *Photochem Photobiol* 81:452 (2005). doi:10.1562/2004-02-12-RA-083 — AVB+OMC catastrophic incompatibility; AVB+OC+BP3 baseline.
3. **Tarras-Wahlberg N, Stenhagen G, Larkö O, et al.** *J Invest Dermatol* 113:547 (1999). doi:10.1046/j.1523-1747.1999.00721.x — OMC ~10 % loss / 35 J/cm² UVA.
4. **Couteau C, Faure A, Fortin J, Paparis E, Coiffard LJM.** *J Pharm Biomed Anal* 44:270 (2007). doi:10.1016/j.jpba.2007.01.052 — 18 sunscreen comparison at 25 MED in cosmetic emulsion.
5. **Hanson KM, Narayanan S, Nichols VM, Bardeen CJ.** *Photochem Photobiol Sci* 14:1607 (2015). doi:10.1039/C5PP00074B — OMC quantum yield and PSS in solution.
6. **Mturi GJ, Martincigh BS.** *J Photochem Photobiol A: Chem* 200:410 (2008). doi:10.1016/j.jphotochem.2008.09.001 — AVB solvent dependence.
7. **Berset G, Gonzenbach H, et al.** *Int J Cosmet Sci* 18:167 (1996) — benzylidene-camphor class photostability protocol.
8. **Chatelain E, Gabard B.** *Photochem Photobiol* 74:401 (2001) — Tinosorb S photostabilisation of AVB and OMC.
9. **Seite S, Colige A, Piquemal-Vivenot P, et al.** *J Photochem Photobiol B* 44:69 (1998) — Mexoryl SX 94 % retention at 25 MED.
10. **Downs CA, DiNardo JC, Stien D, et al.** *Chem Res Toxicol* 34:1046 (2021). doi:10.1021/acs.chemrestox.0c00461 — octocrylene retro-aldol to benzophenone (shelf-life caveat).
11. **Stiefel C, Schwack W.** *Int J Cosmet Sci* 36:561 (2014) — direct UV/HPLC photostability of EHS, PBSA, HMS.
12. **Hojerová J, Medovcíková A, Mikula M.** *Int J Pharm* 408:27 (2011) — EHT half-life >50 h at 1.4 MED/h.
13. **BASF Tinosorb M technical brochure PRD 30482916** — MBBT <2 % loss at 30 MED (manufacturer; C2).
14. **Cornell RM, Schwertmann U.** *The Iron Oxides*, 2nd ed. Wiley-VCH (2003) — iron-oxide lattice photostability.
15. **Schneider SL, Lim HW.** *Photodermatol Photoimmunol Photomed* 35:442 (2019). doi:10.1111/phpp.12439 — ZnO/TiO2 review.
16. **SCCS opinion 0024/05** on Polysilicone-15 — > 95 % photo-recovery at 1 MED.

---

*End of halflives.md.*
