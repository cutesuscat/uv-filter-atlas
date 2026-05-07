# Claim File c002 — Titanium Dioxide (TiO2)

**Class:** Inorganic / mineral UV filter (wide-bandgap n-type semiconductor)
**Research date:** 2026-05-07
**Author tier scheme:** C1 primary verified · C2 well-sourced secondary · C3 inferred (working shown) · C4 graph-digitized · C5 unknown

---

## 1. Identity & Physical Chemistry

### 1.1 Identifiers (C1)

| Field | Value |
|---|---|
| INCI name | Titanium Dioxide |
| IUPAC | Titanium(IV) oxide / titanium dioxide |
| Common synonyms | Titania, CI 77891, Pigment White 6 |
| CAS | 13463-67-7 (general TiO2) |
| Polymorph CAS | 1317-70-0 (anatase) · 1317-80-2 (rutile) · 12188-41-9 (brookite) |
| EC / EINECS | 236-675-5 |
| Molecular formula | TiO2 |
| Molecular weight | 79.866 g·mol⁻¹ |
| Density | 4.23 g·cm⁻³ (rutile) · 3.78 g·cm⁻³ (anatase) · 4.17 g·cm⁻³ (brookite) |
| Melting point | 1843 °C (rutile, in air); anatase converts to rutile at ~600–800 °C |
| Appearance | White crystalline powder, odourless |

Sources: PubChem CID 26042; ChemicalBook CB0461627; Cosmetic Ingredient Review monograph 2002.

### 1.2 Crystal structures (C1)

Three natural polymorphs; all have octahedral TiO6 building blocks but differ in connectivity:

| Polymorph | Space group | a (Å) | c (Å) | Photocatalytic activity | Use in cosmetics |
|---|---|---|---|---|---|
| **Rutile** | P4₂/mnm (tetragonal) | 4.594 | 2.959 | Low | Yes, preferred grade |
| **Anatase** | I4₁/amd (tetragonal) | 3.785 | 9.514 | High | No (avoided as cosmetic UV filter, used in foods/pigments) |
| **Brookite** | Pbca (orthorhombic) | 9.184 | 5.447 | Intermediate | Rare |

**Phase choice in sunscreens (C1):** Rutile is universally preferred because (a) higher refractive index → broader UVA scattering, (b) much lower photocatalytic activity, (c) broader spectral cutoff (~410 nm) extending UVA protection. Anatase, despite slightly higher mass-specific UVB absorption, is rarely used in sunscreens because of ROS generation. Schneider & Lim 2019 explicitly note "rutile … is generally used in cosmetic and sunscreen products due to … not possessing observed ability to damage the skin … and having a higher UV absorption."

### 1.3 Bandgap & cutoff wavelength (C1 / C3)

| Polymorph | Bandgap E_g (eV) | λ_g calc = 1240/E_g (C3) | Type |
|---|---|---|---|
| **Rutile (bulk)** | 3.00–3.03 | 1240/3.00 = **413 nm** | Direct (some authors call it indirect; subtle controversy — but optical edge ~410 nm) |
| **Anatase (bulk)** | 3.20 | 1240/3.20 = **387 nm** | Indirect |
| **Brookite (bulk)** | 3.14 | 1240/3.14 = **395 nm** | Indirect |

**Key consequence (C1):** Rutile's bandgap is at *visible* edge wavelengths (~410 nm) — meaning rutile absorbs through the entire UVA range and slightly into the violet. Anatase cuts off at 387 nm. Both extend further into UVA than ZnO (368–380 nm).

Caveat: bandgap shifts by ~+0.05–0.15 eV (blueshift) for nano-particles < 10 nm by quantum confinement (Brus formula). Sunscreen-grade rutile (20–100 nm) shows minimal shift; effective edge ~395–410 nm. Smijs & Pavel (2011) note 4.7 nm anatase showed +0.15 eV shift.

### 1.4 Refractive index (C1)

| Polymorph | λ = 590 nm (visible) | UV (~310 nm) | Implication |
|---|---|---|---|
| Rutile | n_o = 2.616, n_e = 2.903 (avg ~2.7) | n ≈ 3.0–3.5 | Highest n of any common transparent oxide → strong scattering / white cast |
| Anatase | n_o = 2.561, n_e = 2.488 (avg ~2.5) | n ≈ 2.7–3.1 | Lower scattering than rutile |
| Brookite | ≈ 2.58 | — | Similar to anatase |

(DeVore tabulation; refractiveindex.info; Wikipedia titanium dioxide.)

**Cosmetic implication:** TiO2's high n (≈ 2.7) is *the* reason it whitens skin more than ZnO (n ≈ 2.0) at the same particle size and load. The Mie scattering cross-section in the visible scales steeply with (n−1)². Hence formulators reduce TiO2 particle size to push the scattering peak below visible wavelengths.

### 1.5 Particle sizes used in sunscreen (C1)

| Grade | d50 typical | Use case |
|---|---|---|
| Pigment-grade TiO2 | 200–300 nm | White paints, opaque sunscreens, foundation. Strong white cast. |
| "Microfine" TiO2 | 80–150 nm | Older sun lotions; partial transparency. |
| Nano-TiO2 | 10–50 nm primary; aggregates 70–150 nm | Modern transparent sunscreens. |

**EU regulatory threshold:** 50 % (number) ≤ 100 nm = "nano". Same as ZnO. (C1)

SCCS/1516/13 specifies safe nano-TiO2 must have ≥ 95 % rutile, primary particle size ≥ 30 nm and aspect ratio ≤ 4.5; impurities limited.

### 1.6 Surface coatings (C1)

Cosmetic-grade nano-TiO2 is **always** coated, both for dispersion and to suppress photocatalysis.

**SCCS-approved coatings on nano-TiO2 (SCCS/1516/13 + 2020 update SCCS/1617/20):**
- Silica (SiO2) / hydrated silica
- Alumina (Al2O3) / aluminium hydroxide
- Aluminium stearate, stearic acid
- **Trimethoxycaprylylsilane** (very common — same C8 silane as on ZnO)
- Glycerin
- Dimethicone, hydrogen dimethicone, simethicone

Multi-layer coatings are common: e.g., alumina underlayer + silica overlayer + stearate top-coat for hydrophobic dispersibility.

Coating loadings: typical 5–15 wt% of total particle. Croda's Solaveil™ rutile and BASF T-Lite™ are workhorse grades.

**Doped grades:** Manganese-doped rutile (Wakefield et al., Optisol™, *Photochem. Photobiol. Sci.* 3:648, 2004; doi:10.1039/B403697B) substitutes ~0.7 % Mn into rutile lattice — provides electron-hole de-excitation pathway, **reduces free-radical generation by >90 %**, and provides intrinsic radical-scavenging.

### 1.7 Regulatory status (C1)

| Jurisdiction | Status | Limit | Notes |
|---|---|---|---|
| **USA — FDA** | OTC monograph M020 / 21 CFR 352.10(t) | ≤ 25 % | GRASE Category I. No nano-specific restriction. |
| **EU** | Annex VI **entry 27** (non-nano, since original Annex VI) and **entry 27a** (nano, added 2016 by Reg. 2016/1143) | ≤ 25 % | Spray products prohibited (SCCS/1583/17). Coatings restricted to SCCS-approved list. |
| **EU food (E171)** | **Banned** (Reg. 2022/63 effective Aug 2022) | — | Different exposure route; cosmetic use unaffected. |
| **France** | Banned E171 in foods since 2020. Cosmetic use permitted. | — | — |
| **Australia (TGA)** | Listed sunscreen active | ≤ 25 % | TGA 2017 review concluded safe topically. |
| **Japan** | MHLW positive list, Quasi-drug ingredient | up to 25 % | Approved; nano forms require specific data. |
| **ASEAN / Korea (MFDS)** | Annex VII permitted UV filter | ≤ 25 % | Aligned with EU. |
| **IARC** | **Group 2B** — possibly carcinogenic to humans (inhalation) | — | Monograph 93 (2010). Topical use unaffected. |
| **California Prop 65** | Listed: TiO2 (airborne, unbound particles of respirable size) | — | Inhalation only. |
| **EU CLH (CLP)** | Originally classified Carc Cat 2 (inhalation, ≥ 1 % particles ≤ 10 μm) by Reg. 2020/217. Annulled by ECJ Nov 2022; classification withdrawn (Reg. 2024/197). | — | Now no harmonised CLP carcinogen classification. |

Key SCCS opinions: **SCCS/1516/13** (2014, base — nano-TiO2 ≤ 25 % safe except spray); **SCCS/1583/17** (final 2018 — spray products not safe); **SCCS/1617/20** (additional coatings); SCCS/1641/21 (oral E171 — separate route).

---

## 2. UV Attenuation Spectrum

### 2.1 Mechanism (C1)

Same physics as ZnO: bandgap absorption + Mie scattering. Cole, Shyr & Ou-Yang (2016) — average reflection across UV is **only 4–5 %** for TiO2 sunscreens, equivalent to < SPF 2 from scattering. Absorption dominates.

### 2.2 Cutoff (C1 / C3)

- **Rutile:** 1240/3.00 = **413 nm** (bulk). Practical absorption edge of cosmetic rutile typically ~390–400 nm. (Edge slightly blueshifted vs bulk because of Mie + dispersion effects.)
- **Anatase:** 1240/3.20 = **387 nm** (bulk), edge ~370–380 nm in nano grades.

Rutile thus extends slightly *deeper* into UVA than anatase, reinforcing rutile's preference for UVA1 protection. However, **practical UVA1 protection is weaker than ZnO** because:
1. Mass-specific absorption falls off above 360 nm — the absorption coefficient drops because photon energy becomes < bandgap and only band-tail / scattering contributes.
2. ZnO's higher visible transparency at the same particle size lets formulators load more ZnO.

### 2.3 Particle size dependence — Mie theory (C1)

Popov et al. 2005 (above):
- Optimum TiO2 size for **310 nm UVB** = **62 nm**.
- Optimum TiO2 size for **400 nm UVA** = **122 nm**.

Egerton & Tooley 2012 (*Int. J. Cosmet. Sci.* 34:117–122; doi:10.1111/j.1468-2494.2011.00689.x) computed Mie attenuation for 20, 50, 100 nm TiO2 — the 50 nm material gave the best mass-specific attenuation across UVB and UVA2 simultaneously; 100 nm shifted optimum into UVA1 but visible scattering rose.

In practice, sunscreen formulators commonly use **two TiO2 grades** in one product: 15–25 nm primary for UVB efficiency + 80–120 nm for UVA1, blended.

### 2.4 Mass extinction coefficient (C2 / C4)

Approximate values for typical 25 nm rutile + dispersing aid (Egerton 2012, graph-digitized — C4):

| λ | α (L·g⁻¹·cm⁻¹) | Note |
|---|---|---|
| 290 nm | ~25–35 | Strong UVB absorption |
| 310 nm | ~20–30 | UVB peak region |
| 340 nm | ~10–15 | UVA2 |
| 360 nm | ~5–10 | Edge of UVA2 |
| 380 nm | ~2–4 | UVA1 |
| 400 nm | ~1–2 | Far UVA1 / visible edge — Mie scattering only |

Compared to ZnO at the same size, TiO2 attenuates UVB roughly 2–3× more efficiently per gram, but ZnO catches up at λ > 370 nm.

### 2.5 Anatase vs rutile spectra (C2)

Anatase's slightly larger bandgap means it absorbs marginally more *intensely* in the UVB but *cuts off earlier* (~388 nm) than rutile (~410 nm). This is one reason commercial sunscreens use rutile despite anatase being mass-cheaper to manufacture: rutile gives broader UVA cover and dramatically lower photocatalysis.

### 2.6 Particle scattering vs absorption ratio (C1)

Cole et al. 2016, integrating-sphere measurements: for typical sunscreen film,

- UV reflection: 4–5 % (i.e., 4–5 % of incident UV is scattered back; the rest is *absorbed*).
- Above bandgap (visible): reflection rises to ~60 % — the cosmetic "white cast" the user sees.

Absorption: scattering ratio in the UV ≈ **>10:1**. The historical claim that TiO2 "reflects UV" is **wrong**; this was a marketing-driven simplification corrected by Cole et al. (Schneider & Lim 2019 reiterate this.)

---

## 3. Photocatalytic activity

### 3.1 Mechanism (C1)

Above bandgap: electron–hole pair → surface redox → ROS:
- e⁻(CB) + O2 → O2•⁻ (anatase CB at -0.5 V vs NHE; rutile CB at -0.3 V vs NHE → both thermodynamically generate O2•⁻).
- h⁺(VB) + H2O → •OH + H⁺ (anatase VB +2.7 V; rutile VB +2.7 V → both produce •OH).
- Indirect generation of H2O2 via dismutation; ¹O2 via energy transfer.

Anatase's electrons and holes have higher mobility (lower effective mass) and the conduction-band edge is more reducing — both factors make anatase substantially more photocatalytic than rutile. (C1)

### 3.2 Quantitative ROS / photocatalysis (C1)

- **Anatase produces ~5–10× more •OH than rutile** under matched UV365 illumination on per-mass basis. (Hirakawa & Nosaka, *Langmuir* 18:3247, 2002; Carlotti et al., *J. Photochem. Photobiol. B* 96:130, 2009.) (C2)
- Rutile produces detectable but much lower ROS; cosmetic-grade nano-rutile with multi-layer coating shows near-baseline ROS in DCFH-DA assays (Lewicka et al. 2013).
- **Mn-doped rutile (Optisol)**: free-radical generation reduced **>90 %** vs undoped (Wakefield et al. 2004; doi:10.1039/B403697B) and active radical-scavenging behaviour observed.

### 3.3 Effect of coatings (C1)

Carlotti et al. 2009; Egerton 2012; Lewicka et al. 2013:

- **Alumina (Al2O3)**: reduces rutile photocatalysis by 70–90 %.
- **Silica (SiO2)**: reduces by 80–95 %, increases with shell thickness.
- **Combined Al2O3/SiO2**: >95 % suppression typical for commercial-grade.
- **Stearic acid / stearate**: modest reduction (~30–50 %); mainly hydrophobic dispersion aid.
- **Trimethoxycaprylylsilane**: reduces ROS modestly + improves dispersion.

Nanoscale TiO2 from neat sunscreens (post-extraction) was found by Lewicka et al. 2013 to be **relatively inactive** upon UV illumination — coatings on commercial TiO2 are generally effective. ZnO from the same products produced substantially more ROS — i.e. industry has done a better job coating TiO2 than ZnO.

Overall, **coatings do not eliminate photocatalysis**; SCCS notes that residual photocatalytic activity remains a consideration but at coated-grade levels does not drive the safety conclusion.

### 3.4 Bleaching of co-formulated organic filters (C1)

- Photolysis of avobenzone is *accelerated* by uncoated nano-TiO2 (Serpone, Salinaro et al., *Photochem. Photobiol. Sci.* 2:970, 2003; Buchalska et al., *Photochem. Photobiol. Sci.* 9:1276, 2010). (C1)
- Co-formulating TiO2 with avobenzone without proper coating *and* without a photostabiliser (octocrylene, DEHN, polycrylene) is a known formulation pitfall — Croda Beauty's "Top 10 sun care formulation development mistakes" lists this as #1.
- Mn-doped rutile (Optisol) reportedly *triples* avobenzone photostability vs commercial undoped TiO2 in test formulations (Wakefield et al. 2004).

### 3.5 Implications for skin (C1 / C2)

- *In vitro* anatase + UV → keratinocyte / fibroblast DNA damage, lipid peroxidation, viability loss at 4–16 μg·mL⁻¹ + 10 J·cm⁻² UVA (Smijs & Pavel 2011 review).
- *In vivo* rutile, coated, intact skin → no measurable ROS escalation in clinical tests; multiple SCCS opinions and the TGA 2017 review concur "no biologically significant ROS reaches viable cells under normal use." (C1)
- The persistence of *intracellular* ROS would require nanoparticles to reach viable keratinocytes, which is not observed at meaningful levels.

---

## 4. Safety / Regulatory

### 4.1 Skin penetration (C1)

- Filipe et al. 2009 (above) — TiO2 detectable only in stratum corneum after 48 h occlusion; no penetration into viable epidermis.
- Mavon et al. 2007 — 20 nm TiO2 in decyl-glucoside vehicle: 83 % SC, 5 % viable epidermis, ~0.1 % dermis (using exhaustive analytical methods to detect any signal).
- Sadrieh, Wokovich, Hahn et al. *Toxicol. Sci.* 115:156, 2010 (doi:10.1093/toxsci/kfq041) — "Lack of significant dermal penetration of titanium dioxide from sunscreen formulations containing nano- and submicron-size TiO2 particles" — Yucatan pig skin in vivo, 4 weeks of daily application, four formulations including nano forms — TiO2 stays in stratum corneum.
- Lademann et al. *Skin Pharmacol. Appl. Skin Physiol.* 12:247, 1999 — TiO2 microparticles penetrate to upper 1–2 corneocyte layers in stratum corneum; some accumulation in hair-follicle openings; no viable-skin penetration.

**Consensus:** stratum corneum is an effective barrier; FDA, SCCS, TGA all accept this for coated rutile at commercial particle sizes. Damaged / sunburned skin remains a residual uncertainty noted explicitly by SCCS.

### 4.2 Inhalation hazard (C1)

- IARC Monograph 93 (2010) — TiO2 = **Group 2B**, possibly carcinogenic via inhalation, based on rat lung tumour studies at high chronic doses. Mechanism is "lung overload" particle clearance impairment, not a direct carcinogenic mechanism — relevance to humans contested.
- EU CLH initially classified TiO2 as Carc Cat 2 (inhalation; 2020/217) — annulled by ECJ 2022 (Case T-279/20); classification withdrawn 2024.
- Cosmetic spray products with nano-TiO2 are **prohibited** by EU (SCCS/1583/17) and by SCCS guidance.
- FDA does not separately restrict nano-TiO2 in sprays but warns about inhalation risk for any spray sunscreen.
- Regulatory landscape continues to evolve — formulators routinely avoid nano-TiO2 in any aerosol/pump-spray product.

### 4.3 Coral / aquatic safety (C1 / C2)

- Hawaii bans (Acts 104, 15) target organic filters; TiO2 is not banned but is not unconditionally "reef safe."
- Corinaldesi et al. 2018 (above) and Tang et al. 2024 — uncoated nano-TiO2 toxic to coral and marine invertebrates at sub-mg/L. Coated, larger-particle TiO2 substantially lower toxicity.
- TiO2 widely promoted alongside ZnO as "reef-friendlier" relative to oxybenzone/octinoxate; the comparison is favourable but not absolute.

### 4.4 Other regulatory / consumer concerns

- **EFSA (European Food Safety Authority)** withdrew safety opinion on TiO2 (E171) for food in 2021 due to potential genotoxicity — banned as food additive in EU since Aug 2022. Cosmetic / sunscreen use is **separate and unaffected** because oral exposure differs from topical.
- **GreenScreen for Safer Chemicals** lists nano-TiO2 as concern level "moderate" pending further nanotoxicology data.
- TiO2 is generally regarded as **low allergen risk** — Schneider & Lim 2019 note "no reports of allergic contact dermatitis or photoallergic contact dermatitis to titanium dioxide."

---

## 5. Confidence summary

| Datum | Tier | Notes |
|---|---|---|
| CAS, MW, density | C1 | Multiple primary refs |
| Polymorphs (rutile/anatase/brookite) | C1 | Universal consensus |
| Bandgap rutile 3.00 eV / anatase 3.20 eV | C1 | Multiple textbook + Smijs 2011 |
| Cutoff calc 413/387 nm (C3) vs observed ~400/380 nm | C3 / C2 | 1240/E shown |
| Refractive index ~2.5–2.7 (anatase/rutile) | C1 | DeVore; refractiveindex.info |
| Particle sizes 10–150 nm | C1 | SCCS + patent literature |
| Coating list | C1 | SCCS/1516/13, 1617/20 |
| Mn-doping >90 % free-radical reduction | C1 | Wakefield 2004 |
| Anatase 5–10× ROS rutile | C2 | Hirakawa & Nosaka; Carlotti |
| Coatings 70–95 % photocatalysis suppression | C2 | Carlotti, Egerton, Lewicka |
| FDA GRASE ≤ 25 % | C1 | 21 CFR 352 |
| EU Annex VI 27/27a | C1 | Reg. 1223/2009 + 2016/1143 |
| IARC Group 2B (inhalation) | C1 | Monograph 93 (2010) |
| Skin penetration < 0.1 % to dermis | C1 | Filipe; Mavon; Sadrieh |
| Spray prohibition | C1 | SCCS/1583/17 |

---

## 6. Key references (full list in /sources.md)

1. Schneider SL, Lim HW. A review of inorganic UV filters zinc oxide and titanium dioxide. *Photodermatol. Photoimmunol. Photomed.* 35:442–446 (2019). doi:10.1111/phpp.12439
2. Smijs TG, Pavel S. Titanium dioxide and zinc oxide nanoparticles in sunscreens: focus on their safety and effectiveness. *Nanotechnol. Sci. Appl.* 4:95–112 (2011). doi:10.2147/NSA.S19419
3. Cole C, Shyr T, Ou-Yang H. Metal oxide sunscreens protect skin by absorption, not by reflection or scattering. *Photodermatol. Photoimmunol. Photomed.* 32:5–10 (2016). doi:10.1111/phpp.12214
4. Popov AP, Priezzhev AV, Lademann J, Myllylä R. TiO2 nanoparticles as an effective UV-B radiation skin-protective compound in sunscreens. *J. Phys. D: Appl. Phys.* 38:2564–2570 (2005). doi:10.1088/0022-3727/38/15/006
5. Egerton TA, Tooley IR. UV absorption and scattering properties of inorganic-based sunscreens. *Int. J. Cosmet. Sci.* 34:117–122 (2012). doi:10.1111/j.1468-2494.2011.00689.x
6. Wakefield G, Lipscomb S, Holland E, Knowland J. The effects of manganese doping on UVA absorption and free radical generation of micronised titanium dioxide and its consequences for the photostability of UVA absorbing organic sunscreen components. *Photochem. Photobiol. Sci.* 3:648–652 (2004). doi:10.1039/B403697B
7. Lewicka ZA, Yu WW, Oliva BL, Contreras EQ, Colvin VL. Photochemical behavior of nanoscale TiO2 and ZnO sunscreen ingredients. *J. Photochem. Photobiol. A* 263:24–33 (2013). doi:10.1016/j.jphotochem.2013.04.019
8. Carlotti ME, Ugazio E, Sapino S, et al. Specific effects of single antioxidants in the lipid peroxidation caused by nano-titania used in sunscreen lotions. *J. Photochem. Photobiol. B* 96:130–135 (2009). doi:10.1016/j.jphotobiol.2009.05.001
9. Filipe P, Silva JN, Silva R, et al. Stratum corneum is an effective barrier to TiO2 and ZnO nanoparticle percutaneous absorption. *Skin Pharmacol. Physiol.* 22:266–275 (2009). doi:10.1159/000235554
10. Mavon A, Miquel C, Lejeune O, et al. In vitro percutaneous absorption and in vivo stratum corneum distribution of an organic and a mineral sunscreen. *Skin Pharmacol. Physiol.* 20:10–20 (2007). doi:10.1159/000096167
11. Sadrieh N, Wokovich AM, Gopee NV, et al. Lack of significant dermal penetration of titanium dioxide from sunscreen formulations containing nano- and submicron-size TiO2 particles. *Toxicol. Sci.* 115:156–166 (2010). doi:10.1093/toxsci/kfq041
12. Serpone N, Salinaro A, Emeline AV, Horikoshi S, Hidaka H, Zhao J. An in vitro systematic spectroscopic examination of the photostabilities of a random set of commercial sunscreen lotions and their chemical UVB/UVA active agents. *Photochem. Photobiol. Sci.* 1:970–981 (2002). doi:10.1039/B206338G
13. IARC Monograph 93 (2010) — Carbon Black, Titanium Dioxide, and Talc.
14. SCCS/1516/13 (2014) — Opinion on Titanium Dioxide (nano form).
15. SCCS/1583/17 (2018) — Opinion on Titanium Dioxide (nano form) as UV-Filter in sprays.
16. SCCS/1617/20 — Opinion on additional coatings for TiO2 (nano form).
17. EU Reg. 2016/1143 — Annex VI amendment, TiO2 (nano) entry 27a.
18. EU Reg. 2022/63 — ban of TiO2 (E171) in foods.
19. US FDA — 21 CFR 352.10; OTC Monograph M020 final administrative order (2021).
20. TGA Australia — Literature review on safety of TiO2 and ZnO nanoparticles in sunscreens (2017 update).
