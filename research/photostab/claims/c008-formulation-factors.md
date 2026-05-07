# c008: General Formulation Factors Affecting Sunscreen Photostability

**Claim**: Beyond stabiliser identity, the photostability of avobenzone (and other photolabile filters) in finished sunscreens is strongly modulated by (i) the vehicle (solvent / emulsion type), (ii) film thickness and uniformity, (iii) oxygen access, (iv) presence of antioxidants (vitamin E, vitamin C, ferulic acid, ubiquinone, etc.), and (v) pH. These effects can change the half-life of avobenzone by an order of magnitude, often more than the addition or removal of a single stabiliser.

**Confidence**: C1 for the qualitative direction of each factor; C2 for absolute quantitative comparisons across studies (different methodologies, doses, MEDs, and quantitation methods make cross-study comparison imperfect).

---

## Section 1: Mechanism

### (i) Vehicle / solvent

Mturi & Martincigh 2008 quantified avobenzone photostability in four solvents under matched UV-A irradiation:

| Solvent | Polarity | Proticity | AVB behaviour | Inferred mechanism |
|---|---|---|---|---|
| Methanol | polar | protic | essentially photostable | Strong intermolecular H-bond stabilises enol; productive ESIPT pathway dominates |
| Ethyl acetate | medium polar | aprotic | photoisomerises + photodegrades in ~equal measure | Mixed enol/diketo populations; both pathways operate |
| DMSO | polar | aprotic | photoisomerises (enol → diketo) but does not fragment | Diketo triplet stabilised, no productive H-donor for ESIPT, but no radical chain initiator |
| Cyclohexane | non-polar | aprotic | appreciable photodegradation (radical fragmentation) | Diketo triplet long-lived, no H-bond stabilisation, free radicals form |

Key: solvents that *donate* a hydrogen-bond to the enol oxygen (alcohols, water-rich phases) stabilise the enol → ESIPT cycle wins over diketo radical chemistry. Non-polar oils (mineral oil, isopropyl palmitate, isopropyl myristate) are *worst* for AVB because they support the diketo tautomer's photochemistry.

### (ii) Film thickness and uniformity

- ISO 24443 in-vitro test: 1.3 mg/cm² standard application; SPF and UVAPF measurements are highly sensitive to thickness uniformity.
- AVB photostability is non-linear in thickness because optical depth is wavelength-dependent. In thin films, all AVB sees similar fluence; in thicker films, deeper-layer AVB is shielded by surface AVB. Empirically, doubling the film thickness can roughly double measured "% retained" AVB.
- Uneven films expose ridges and edges to higher fluence — these are the first to bleach.

### (iii) Oxygen access

- Mturi & Martincigh 2008 and others: degassed solutions show modestly slower AVB decay than air-saturated. Oxygen contributes through (a) generating singlet oxygen from BMDBM triplet (Φ_Δ ≈ 0.3 reported for BMDBM in air-saturated solutions), and (b) scavenging fragment radicals to form peroxyl species that propagate damage to other formulation components.
- W/O emulsions and high-oil-phase O/W systems present a continuous oil "ocean" with substantial dissolved O2 — usually worse for AVB than tightly packed films of low porosity. Antioxidant supplementation is the formulator's lever here.

### (iv) Antioxidants

Afonso et al. 2014 (J Photochem Photobiol B 140:36-40) tested several antioxidants at varying AVB:antioxidant ratios:

| Antioxidant | Optimal ratio AVB:AOX | Effect |
|---|---|---|
| Vitamin E (α-tocopherol) | 1:2 | Strong stabilisation of AVB |
| Vitamin C (ascorbic acid) | 1:0.5 | Strong stabilisation |
| Ubiquinone (CoQ10) | 1:0.5 | Strong stabilisation |
| Trans-resveratrol | varies | Moderate |
| β-carotene | varies | Moderate |
| Mangiferin | varies | Strong (1O2 quencher) |

Mechanism: H-atom donors quench peroxyl radical chains and intercept singlet oxygen (vitamin C, mangiferin); chain-breaking phenolics regenerate via ascorbate (vitamin E + vitamin C synergy); CoQ10 quenches both radicals and 1O2.

Skinceuticals-type CEFer formulation (15% L-AA + 1% α-tocopherol + 0.5% ferulic acid) — Lin et al. 2008 — was developed for skin antioxidant protection independent of UV filters but the same chemistry contributes to filter stabilisation when included in a sunscreen vehicle.

### (v) pH

- Aqueous AVB photodegradation kinetics are pH-dependent: hydroxide-catalysed first-order decay observed across pH 2–10 (Scalia et al., Pharmazie 2007 / aqueous degradation kinetics paper). In O/W vehicles, water-phase pH should be kept slightly acidic to neutral (pH 4–7); strongly alkaline systems accelerate AVB hydrolytic + photochemical loss.
- Antioxidants like vitamin C are themselves pH-sensitive (require pH < 3.5 for chemical stability); finished sunscreen pH targets are usually 4.5–6.5.

---

## Section 2: Quantitative effect (representative datasets)

| Variable | Best case | Worst case | Source |
|---|---|---|---|
| Solvent (single-filter solution) | Methanol: ~5% AVB loss after long UV-A | Cyclohexane: >50% loss after equivalent UV-A | Mturi & Martincigh 2008 |
| Vehicle (formulated cream) | Lipid microparticle encapsulation: AVB loss reduced from 28.9% to 15–17% | Mineral-oil-rich anhydrous: >50% loss | Bordat et al. 2009; Afonso 2014 |
| Antioxidant (CoQ10) | AVB+CoQ10 (1:0.5): >90% retained | AVB alone: ~60% retained at same dose | Afonso 2014 |
| Antioxidant (Vit E) | AVB+VitE (1:2): >85% retained | AVB alone: ~60% | Afonso 2014 |
| Encapsulation (β-cyclodextrin) | >90% retained | <50% non-encapsulated | Wang & Qi 2024; Scalia 2002 |
| Film thickness | 2 mg/cm²: substantially better stability | <0.75 mg/cm²: rapid bleach | ISO 24443 / Diffey method studies |

### Special cases

- **Ethanol-rich aerosols / sprays**: ethanol stabilises AVB by ESIPT-favourable H-bond donation but also volatilises rapidly — the *effective* vehicle as the spray dries can become worse than the bottle. Couteau 2021 (Eur Rev Med Pharmacol Sci) showed alcohol-containing sprays gave higher initial photostability that converged with cream values after drying.
- **Anhydrous sticks**: typically worst-case vehicle for AVB; benefits most from triplet quenchers and encapsulation.

---

## Section 3: Practical formulation guidance

1. **Pick a polar-protic-leaning oil phase**: prefer alkyl benzoates (C12-C15 alkyl benzoate, Crodamol AB), dicaprylyl carbonate, and a small amount of ethanol/glycols if compatible. Avoid mineral oil and high levels of paraffinic emollients with photolabile filters.
2. **Always include a triplet quencher** (octocrylene 5–10%; or DEHN 1–5%; or Tinosorb S 2–6%; or DESM 1–3%) when avobenzone is present at >1.5%.
3. **Add a chain-breaking antioxidant** (tocopherol 0.1–0.5%, optionally with ascorbic acid/ferulic acid in the water phase) for residual radical chemistry.
4. **Maintain water-phase pH 4.5–6.5**.
5. **Validate film integrity**: 1.3 mg/cm² ISO standard. Confirm a minimum 75% AVB retention after 25 MED (industry rule of thumb) before progressing to clinical SPF.
6. **Encapsulate** (cyclodextrin / lipid microparticle) for hard-to-stabilise systems.

---

## Section 4: Citations

1. **Mturi GJ, Martincigh BS.** "Photostability of the sunscreening agent 4-tert-butyl-4'-methoxydibenzoylmethane (avobenzone) in solvents of different polarity and proticity." *J. Photochem. Photobiol. A: Chemistry* 200(2-3):410-420 (2008). DOI: 10.1016/j.jphotochem.2008.09.007. **[C1, primary]**
2. **Afonso S, Horita K, Sousa e Silva JP, Almeida IF, Amaral MH, Lobão PA, Costa PC, Miranda MS, Esteves da Silva JCG, Sousa Lobo JM.** "Photodegradation of avobenzone: Stabilization effect of antioxidants." *J. Photochem. Photobiol. B: Biology* 140:36-40 (2014). DOI: 10.1016/j.jphotobiol.2014.07.004. PMID: 25086322. **[C1, primary]**
3. **Couteau C, et al.** "Study of the influence of alcohol on the photostability of four UV filters." *Eur. Rev. Med. Pharmacol. Sci.* 25(19):6025-6033 (2021). PMID: 34661262. **[C1]**
4. **Bordat P, et al.** "Incorporation in Lipid Microparticles of the UVA Filter, Butyl Methoxydibenzoylmethane Combined with the UVB Filter, Octocrylene: Effect on Photostability." *AAPS PharmSciTech* 11(1):145-153 (2009). DOI: 10.1208/s12249-009-9217-2. **[C1]**
5. **Lin FH, Lin JY, Gupta RD, Tournas JA, Burch JA, Selim MA, Monteiro-Riviere NA, Grichnik JM, Zielinski J, Pinnell SR.** "A topical antioxidant solution containing vitamins C and E stabilized by ferulic acid…" *Journal of Investigative Dermatology* (full citation in PubMed 18603326). **[C1]**
6. **Scalia S, Mezzena M.** "Photostabilization effect of quercetin on the UV filter combination, butyl methoxydibenzoylmethane–octyl methoxycinnamate." *Photochem. Photobiol.* 86(2):273-278 (2010). DOI: 10.1111/j.1751-1097.2009.00676.x. **[C1]**
7. **Bonda CA, Lott D.** "Sunscreen Photostability." Chapter 14 in *Principles and Practice of Photoprotection* (Springer 2016). DOI: 10.1007/978-3-319-29382-0_14. **[C2 review]**
8. **Couteau C, Faure A, Fortin J, Paparis E, Coiffard LJM.** "Study of the photostability of 18 sunscreens in creams by measuring the SPF in vitro." *J. Pharm. Biomed. Anal.* 44(1):270-273 (2007). **[C1]**
9. **Downs CA, DiNardo JC, Stien D, Rodrigues AMS, Lebaron P.** "Benzophenone Accumulates over Time from the Degradation of Octocrylene in Commercial Sunscreen Products." *Chem. Res. Toxicol.* 34(4):1046-1054 (2021). DOI: 10.1021/acs.chemrestox.0c00461. **[C1, secondary safety relevance]**
10. **Kockler J, Oelgemöller M, Robertson S, Glass BD.** "Photostability of sunscreens." *J. Photochem. Photobiol. C: Photochemistry Reviews* 13(1):91-110 (2012). DOI: 10.1016/j.jphotochemrev.2011.12.001. **[C1, comprehensive review]**

### Bias caveat

Cross-study quantitative comparisons must be made cautiously: irradiation sources (xenon arc vs solar simulator vs sunlight), MED definitions (different national standards), film thicknesses, and assay methods (HPLC vs UV-vis vs SPF) all differ. The qualitative ordering (encapsulation > triplet quencher > antioxidant > vehicle choice in their *typical* magnitude of contribution to AVB rescue) is well-supported.
