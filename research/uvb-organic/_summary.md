# UVB Organic Sunscreen Filters — Comparison Summary

Compiled 2026-05-07 for the knowledge base at `/workspace/sunscreen-filters/research/uvb-organic/`.
Each row links to a detailed claim file in `claims/`.

## Quick Reference Table

| # | Filter | INCI / common | CAS | MW (g/mol) | λmax (EtOH, nm) | ε (M⁻¹ cm⁻¹) | E(1%, 1cm) | Photostab. rank | FDA % | EU % | Aus % | JP % | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [c001](claims/c001-octinoxate.md) | Octinoxate (EHMC, OMC) | 5466-77-3 | 290.4 | 308–311 | 23,300–25,000 | ~826 | 4 (poor) | 7.5 | 10 | 10 | 20 | trans/cis isomerism; degrades in aggregate; banned Hawaii/Palau/Thailand |
| 2 | [c002](claims/c002-octisalate.md) | Octisalate (EHS) | 118-60-5 | 250.3 | 305–307 | ~4,800 | ~192 | 1 (excellent) | 5 | 5 | 10 | 10 | Weak ε; ESIPT mechanism; co-solvent for avobenzone |
| 3 | [c003](claims/c003-homosalate.md) | Homosalate (HMS) | 118-56-9 | 262.3 | 306–309 | ~5,000 | ~191 | 1 (excellent) | 15 | 7.34* face only | 10 | 10 | EU restricted by SCCS for endocrine concern |
| 4 | [c004](claims/c004-octocrylene.md) | Octocrylene (OCR) | 6197-30-4 | 361.5 | 303 | ~12,000 | ~332 | 2 (good but BP issue) | 10 | 10 | 10 | 10 | Generates benzophenone on storage; triplet quencher of avobenzone |
| 5 | [c005](claims/c005-cinoxate.md) | Cinoxate | 104-28-9 | 250.3 | 308 | ~20,650 | ~825 | 4 (analogous to OMC) | 3 | not listed | 6 | 5 | Obsolete; rare in modern products |
| 6 | [c006](claims/c006-paba-padimate-o.md) | PABA / Padimate O | 150-13-0 / 21245-02-3 | 137.1 / 277.4 | 283 / 311 | ~13,500 / ~28,400 | ~985 / ~1,024 | 2 / 2 | 15 / 8 | banned / 8 | banned / 8 | banned / 10 | PABA banned EU 2009; allergenic; sunlight mutagenicity (Knowland 1993); padimate O has highest E(1%,1cm) of any FDA filter |
| 7 | [c007](claims/c007-ensulizole.md) | Ensulizole (PBSA) | 27503-81-7 | 274.3 | 302 (water) | ~25,000 | ~911 | 1 (chromophore stable) | 4 | 8 | 4 | 3 | Water-soluble; ROS generator (Φ¹O₂ = 0.10); ΦF = 0.63 |
| 8 | [c008](claims/c008-polysilicone-15.md) | Polysilicone-15 (Parsol SLX) | 207574-74-1 | oligomer ~6,000 | 312 | per-chromophore ~6,500 | 160–190 | 1 (excellent) | not approved | 10 | 10 | 10 | Polymer → no skin penetration; photostabilizer for avobenzone |
| 9 | [c009](claims/c009-octyl-triazone.md) | Ethylhexyl Triazone (EHT, Uvinul T 150) | 88122-99-0 | 823.1 | 314 | ~135,000 | ~1,500 | 1 (best) | not approved | 5 | 5 | 5 | Highest ε of any commercial UV filter; large MW → no penetration |
| 10 | [c010](claims/c010-4-mbc.md) | 4-Methylbenzylidene Camphor (Enzacamene) | 36861-47-9 | 254.4 | 300 | 24,500 | ~963 | 2 (mostly photostable) | not approved | **banned (May 2026)** | 4 (under review) | not permitted | EU banned for endocrine disruption (estrogen + thyroid) |

\* Homosalate at 7.34 % is permitted in EU **only in face products excluding propellant/pump sprays**, per Reg. (EU) 2022/1176.

### Photostability rank legend
1 = effectively photostable (>95 % retention at 25 MED)
2 = mostly photostable, with caveats (>85 %)
3 = partial photostability (50–85 %)
4 = poor / significant photolysis under solar dose (<70 % at 25 MED for monomer/aggregate)
5 = highly photolabile (avobenzone-class, not in this UVB list)

## Bird's-eye observations

* **Highest ε:** Ethylhexyl triazone (~135,000 M⁻¹ cm⁻¹) > Padimate O (~28,400) > 4-MBC (~24,500) ≈ Octinoxate (~24,000) > Cinoxate (~20,650) > Octocrylene (~12,000) > PBSA (~25,000 in water; counterion-dependent) ≫ Salicylates (~5,000).
* **Highest specific extinction (per-mass efficacy):** Padimate O (~1,024 in EtOH) > Ethylhexyl triazone (~1,500) > 4-MBC (~963) > PABA (~985) > Octinoxate / Cinoxate (~826) > PBSA (~911) ≫ salicylates (~190) ≫ Polysilicone-15 (~175).
* **Photostability winners:** EHT, Polysilicone-15, salicylates (HMS, EHS) — flat absorbance even at 50 MED.
* **Photostability losers (in this UVB set):** Octinoxate (in aggregate or with avobenzone) and PABA family (photoallergenic, mutagenic in some studies).
* **Largest regulatory divergence (FDA vs EU):**
  * Homosalate: 15 % FDA vs 7.34 % EU (face only) — endocrine concern not yet acted on by FDA.
  * Octinoxate: 7.5 % FDA vs 10 % EU vs 20 % Japan.
  * Ethylhexyl triazone, polysilicone-15, 4-MBC: in EU/Japan/Australia but **not FDA-approved** (frozen FDA monograph since 1999).
  * 4-MBC: banned in EU/UK/China but still permitted in Canada and (transitionally) Australia.
* **Approved in all five major markets (FDA, EU, Australia, Japan, Korea):** Octinoxate, Octisalate, Homosalate, Octocrylene. (Ensulizole permitted in all but at variable concentrations.)
* **Endocrine concerns flagged 2020–2026:** Octinoxate (estrogenic + anti-androgenic), Homosalate (estrogenic, anti-androgenic, presumed thyroid disruptor), Octocrylene (under investigation), 4-MBC (estrogen + thyroid; EU ban), PABA (banned EU 2009 due to photoallergy more than endocrine).
* **Reef bans:** Octinoxate (Hawaii, Palau, Thailand, USVI), Octocrylene (Palau, USVI). The salicylates are not on reef-ban lists.
* **Skin-penetration low (>500 Da molecules):** Polysilicone-15 (~6,000), EHT (823). All small-molecule UVB filters in this list have detectable systemic absorption per FDA Maximal Usage Trial (Matta 2020 JAMA), exceeding the 0.5 ng/mL toxicology threshold.

## C5 ("not found / could not access") items aggregated across files

| File | Missing data |
|---|---|
| c005 (Cinoxate) | Modern photodegradation kinetics (k, t½), Φ values, biomonitoring %, aquatic LC50 |
| c008 (Polysilicone-15) | Direct Φd, Φ(E/Z) measurements; environmental half-life data |
| c001 (Octinoxate) | Detailed environmental persistence beyond aquatic LC50 |
| c002–c004, c006, c007, c009, c010 | Specific gaps noted within each file |

## See also

* `sources.md` — full bibliography
* `claims/c001` to `claims/c010` — individual claim files
