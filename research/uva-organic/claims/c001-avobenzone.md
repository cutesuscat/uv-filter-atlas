# C001 — Avobenzone (Butyl Methoxydibenzoylmethane / BMDBM / Parsol 1789)

## Section 1: Identity

| Property | Value | Confidence |
|---|---|---|
| **INCI** | Butyl Methoxydibenzoylmethane | C1 |
| **USAN** | Avobenzone | C1 |
| **IUPAC** | 1-(4-tert-Butylphenyl)-3-(4-methoxyphenyl)propane-1,3-dione (also: 3-(4-tert-Butylphenyl)-1-(4-methoxyphenyl)propane-1,3-dione) | C1 |
| **Common abbreviations** | BMDBM, BMDM, AVB, AVOB, t-BMDBM | C1 |
| **Trade names** | Parsol 1789 (DSM/Hoffmann-La Roche), Eusolex 9020 (Merck), Neo Heliopan 357 (Symrise), Escalol 517 (Ashland) | C2 |
| **CAS** | 70356-09-1 | C1 |
| **Molecular formula** | C₂₀H₂₂O₃ | C1 |
| **Molecular weight** | 310.39 g/mol | C1 |
| **Appearance** | Whitish-yellow crystalline powder; mp 81–86 °C | C2 |

### Regulatory status

| Region | Status | Max concentration |
|---|---|---|
| **USA (FDA)** | Category I (currently allowed under stayed monograph M020) but FDA proposed in 2019 that GRASE status is "insufficient data"; remains in commerce pending further safety data | **3%** |
| **EU (Annex VI)** | Annex VI entry — approved | **5%** |
| **Australia (TGA)** | Approved (AICIS / TGA permitted sunscreen active) | **5%** |
| **Japan** | Approved (highest cap globally) | **10%** |
| **South Korea, ASEAN, Mercosur, Canada, China** | Approved | 5% (Korea, China, ASEAN, Mercosur); 3% (Canada) |
| **Palau** | Banned (2020) — reef toxicity concerns | — |

Source: avobenzone Wikipedia entry; OTC Monograph M020; reanalysis confirms 3% (US) / 5% (EU) / 10% (Japan) caps. C1.

### Typical formulation use

Avobenzone is almost always blended at 1–3% in US OTC products and 2–5% in EU products, **paired with photostabilizers** (octocrylene most common; see §4). It is rarely used alone above ~1.5% because of photolability.

---

## Section 2: UV Absorption Spectrum

Avobenzone exists as a **keto–enol tautomeric equilibrium** (β-diketone). The two tautomers have radically different spectra:

| Tautomer | λmax (nm) | Notes |
|---|---|---|
| **Chelated enol (CE)** — predominant in ground state, intramolecular H-bond | **355–360** (depends on solvent) | Active UVA absorber; π→π\* of enol-chelate |
| **Diketo (DK)** — minor, but populated under irradiation | **~265** | UVB region; DK is the photochemically reactive form |

### λmax by solvent (for the enol band)

| Solvent | λmax (nm) | Source / Confidence |
|---|---|---|
| Cyclohexane (nonpolar, aprotic) | 355 | Mturi & Martincigh 2008 — C1 |
| Cyclohexane (DK form, ~265 band) | 265 | Mturi & Martincigh 2008 — C1 |
| Ethyl acetate (aprotic, moderate polar) | 356 | Mturi & Martincigh 2008 — C1 |
| Methanol (protic, polar) | 358 | Mturi & Martincigh 2008 — C1 |
| DMSO (aprotic, polar) | 363 | Mturi & Martincigh 2008 — C1 |
| Ethanol (typical pharm reference) | ~357 | Cosmetics & Toiletries / wikipedia composite — C2 |

**Important caveat:** Increasing solvent polarity and H-bond accepting ability red-shifts the enol band; protic solvents that stabilize the enol form *decrease* photodegradation (see §3).

### Molar absorption coefficient (ε) and E(1%, 1cm)

| Quantity | Value | Solvent | Source / Confidence |
|---|---|---|---|
| **E(1%, 1cm)** at 357–358 nm | **1100–1160** | Methanol (EU pharmacopeial reference) | EU spec / Cosmetics & Toiletries — C1 |
| **ε (molar absorptivity)** | ~34,000 M⁻¹cm⁻¹ at λmax | Methanol (calculated from E1% via ε = E1%·MW/10 ≈ 1130·310.39/10 ≈ 35,000) | C3 (computed) |
| ε (literature reported) | 31,000–36,000 M⁻¹cm⁻¹ | Various organic solvents | C2 |

Conversion check: ε = E(1%,1cm) × MW / 10 = 1130 × 310.39 / 10 ≈ **35,070 M⁻¹cm⁻¹**. This high ε is the basis for avobenzone's reputation as the strongest UVA absorber per gram among organic filters approved in the US.

### Bandwidth / spectral range

- Effective absorption: **310–400 nm** (covers UVA-I and UVA-II); peak in UVA-I
- FWHM ~50 nm at λmax
- Critical wavelength reported ~380 nm (when stabilized)

---

## Section 3: Photodegradation Kinetics

Avobenzone is **the most notoriously photolabile of the major organic UV filters**. The neat compound and dilute solutions degrade dramatically; degradation is solvent-, oxygen-, and formulation-dependent.

### Primary mechanism

1. UV absorption populates S₁ of enol → fast H-transfer / IC mostly back to ground state
2. A fraction undergoes excited-state intramolecular H-transfer to populate **diketo (DK)** form
3. DK form has **long-lived triplet state** → undergoes **Norrish Type I α-cleavage** between the carbonyl and α-carbon
4. Radical fragments recombine, oxidize, or abstract H → photoproducts

This is why DK quenchers (octocrylene) and protic solvents (which stabilize enol) protect avobenzone.

### Quantitative degradation data

| Conditions | % loss / remaining | UV dose / time | Source |
|---|---|---|---|
| Avobenzone neat under 1 h sunlight (FDA filing data) | **~36% loss** of UV absorbance | 1 h sunlight | FDA submission, cited in Wikipedia / cosmeticsandtoiletries — C2 |
| Avobenzone in cyclohexane | "appreciable" photodegradation; major route | Sunlight-equivalent UVA | Mturi & Martincigh 2008 — C1 |
| Avobenzone in ethyl acetate | Photoisomerisation + photodegradation, similar extent | UVA | Mturi & Martincigh 2008 — C1 |
| Avobenzone in methanol | **Essentially photostable** (protic stabilizes enol) | UVA | Mturi & Martincigh 2008 — C1 |
| Avobenzone in DMSO | Photoisomerisation only (no photodegradation); requires O₂ | UVA | Mturi & Martincigh 2008 — C1 |
| Avobenzone 4% alone (in vehicle) | ~23% remaining after 25 MED | 25 MED | cited in Bonda 2008 / cosmeticsandtoiletries — C2 |
| Avobenzone + octinoxate (typical formulation) | rapid concomitant degradation, free radicals persist | UVA exposure | Sayre, Dowdy, Gerwig, Shields, Lloyd 2005, *Photochem Photobiol* — C1 |
| Avobenzone + octocrylene + BP-3 (Sayre 2005) | **~20%** avobenzone remaining | 40 mJ/cm² UVA | Sayre 2005 — C1 |
| Avobenzone + octocrylene 4% (Bonda 2008) | **~90%** remaining | 25 MED | Bonda 2008 / cosmeticsandtoiletries — C2 |

### Oxygen dependence

- **Photoisomerisation (enol ↔ keto + cis/trans of cinnamoyl-like fragments): O₂-dependent**
- **Photodegradation (Norrish cleavage to small molecules): O₂-independent** — proceeds in degassed solvent

(Mturi & Martincigh 2008, *J Photochem Photobiol A* **200**:410–420)

### Quantum yields (Φ)

Reported quantum yield for photoreactivity (formation of DK and downstream products) is small but non-negligible: Φ_total photoproduct ≈ 10⁻³–10⁻² depending on solvent (C2 from various ultrafast / steady-state studies). Specific Φ for cleavage in cyclohexane reported on the order of 10⁻³ — **C5 for exact value** without primary numerical access.

Ultrafast TEAS studies (Holt et al. 2021, *PCCP* 23, 24373; D1CP03610F) report excited-state lifetimes:
- τ₁ ≈ 150–235 fs (Franck-Condon evolution)
- τ₂ ≈ 0.7–1.2 ps (S₁ stimulated emission)
- τ₃ ≈ 7.7–8.4 ps (vibrational cooling)
- τ₄ > 2.5 ns (incomplete bleach recovery — productive photochemistry channel)
Confidence C1.

### Photoproducts (Schwack & Rudolph 1995, *J Photochem Photobiol B* / Z. Lebensm.-Unters. Forsch. cited in Wiley)

In cyclohexane, **14 photoproducts** identified, grouped as:

1. **Benzaldehydes** — 4-tert-butylbenzaldehyde, 4-methoxybenzaldehyde (anisaldehyde)
2. **Benzoic acids** — 4-tert-butylbenzoic acid, 4-methoxybenzoic acid (anisic acid)
3. **Phenylglyoxals (arylglyoxals)** — 4-tert-butylphenylglyoxal, 4-methoxyphenylglyoxal — **photosensitizers, generate singlet oxygen**
4. **Acetophenones** — 4-tert-butylacetophenone, 4-methoxyacetophenone
5. **Benzils** — 4,4'-disubstituted benzils (1,2-diketones) — also photosensitizers
6. **Dibenzoylmethanes** (parent and degraded analogues)
7. **Dibenzoylethane** (recombination product)
8. **t-Butylbenzene** (after decarbonylation)

Sensitizer photoproducts (arylglyoxals, benzils) raise toxicology concerns: they generate ¹O₂, may cause photoallergy, and have been implicated in reactive species formation.

Mechanism: α-cleavage of DK form → benzoyl + arylacetyl radicals → recombination/oxidation/disproportionation pathways.

C1 (Schwack & Rudolph) → secondary review citations; primary not directly accessed in this work — flag as **C1/C2 hybrid**.

### Effect of vehicle / formulation

- **Esters / oils (ethylhexyl benzoate, C12-15 alkyl benzoate, isopropyl myristate)** — moderate stability, similar to cyclohexane; standard sunscreen oil bases
- **Polar protic vehicles** — better stability but rare in cosmetic formulations
- **Silicones (cyclomethicone)** — moderate stability, common
- **Encapsulation (β-cyclodextrin, polymer microspheres, lipid nanoparticles)** — can dramatically improve stability (>80% remaining after extended UV exposure) — C2

---

## Section 4: Photostabilization

Avobenzone alone is **not viable** in modern sunscreens. The industry has developed multiple stabilization strategies.

### Triplet quenchers (most effective; quench DK triplet state via energy transfer, ET ≈ 56 kcal/mol)

| Stabilizer | INCI / trade name | Mechanism | Notes |
|---|---|---|---|
| **Octocrylene (OC)** | 2-Ethylhexyl 2-cyano-3,3-diphenylacrylate | Triplet–triplet energy transfer; quenches AVB(³DK) | Most common; "consistently performed best" — Bonda 2008 |
| **DEHN / Corapan TQ** | Diethylhexyl 2,6-naphthalate | Triplet–triplet energy transfer (T₁ of DEHN ≈ 60 kcal/mol) | Hallstar; established mechanism in Photochem Photobiol Sci 2018, c8pp00204e |
| **Polyester-8 (Polycrylene)** | Cyanodiphenyl-propenoate-terminated polyester | Same chromophore family as OC; polymeric → less penetration | Hallstar; synergizes with DEHN |
| **MBC (Enzacamene, 4-methylbenzylidene camphor)** | 4-Methylbenzylidene Camphor | Triplet quencher | EU-approved (Annex VI), banned in some markets; restricted use |
| **Bemotrizinol (Tinosorb S)** | Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine | Triplet quencher + own UVA absorber | Not FDA-approved, but EU-approved at 10% |
| **Mexoryl SX (Ecamsule)** | Terephthalylidene Dicamphor Sulfonic Acid | Photostable UVA filter; stabilizes AVB | L'Oréal proprietary; FDA-approved only in specific products |
| **DESM** | Diethylhexyl Syringylidenemalonate (Oxynex ST) | Triplet quencher + ¹O₂ quencher | |
| **Ethylhexyl Methoxycrylene (Solastay S1)** | Octocrylene-related | Triplet quencher, fluorescent | Hallstar |
| **Oxybenzone (BP-3)** | Benzophenone-3 | Modest triplet quenching + own absorption | Use declining due to hormone/reef concerns |

### Singlet oxygen / radical scavengers (secondary stabilization)

- α-Tocopherol (Vit E), tocopheryl acetate
- Ascorbyl tetraisopalmitate
- Trolox (research)
- BHT
- These reduce damage from photoproducts (arylglyoxals, benzils) more than they prevent primary degradation.

### Encapsulation

- β-cyclodextrin inclusion complexes (Scalia et al.)
- Lipid nanoparticles (NLC, SLN)
- Silica microspheres
- Polymer microcapsules
- Often improve photostability ≥30 percentage points.

### Known Negative Interactions (CRITICAL)

#### 1. Avobenzone + Octinoxate (Octyl Methoxycinnamate, OMC, Ethylhexyl Methoxycinnamate)

**Both filters degrade faster together than alone.** Mechanism (Sayre, Dowdy, Gerwig, Shields, Lloyd 2005, *Photochem Photobiol* **81**(2):452–456; doi:10.1562/2004-02-12-RA-083):

- Octinoxate's cinnamate C=C undergoes **[2+2] photocycloaddition** with carbonyl/alkene moieties of avobenzone (Paterno-Büchi-like or olefin–olefin cyclobutane formation)
- Concomitant photolysis predominates over expected E/Z isomerization
- ESR-detectable persistent free radicals form
- Result: both filters degrade faster, and free radicals damage skin

Many regulators / formulators now **avoid this pairing**. Despite this, octinoxate + avobenzone combos persist in some legacy products. C1.

#### 2. Octocrylene degrades to benzophenone (Downs 2021)

Downs CA, DiNardo JC, Stien D, Rodrigues AMS, Lebaron P. (2021). *Benzophenone Accumulates over Time from the Degradation of Octocrylene in Commercial Sunscreen Products*. **Chem Res Toxicol** 34(4):1046–1054. doi:10.1021/acs.chemrestox.0c00461.

- Mechanism: **retro-aldol condensation** of octocrylene → benzophenone + 2-ethylhexyl cyanoacetate
- 16 octocrylene-containing products: avg 39 mg/kg benzophenone (range 6–186)
- After FDA-accelerated stability (1 year @ 40 °C): avg 75 mg/kg (max 435)
- Benzophenone is a 2B IARC carcinogen, endocrine disruptor, strict EU restriction
- Implication: while OC stabilizes avobenzone, OC itself is unstable on shelf-life timescales (months–years), generating benzophenone

This is a **paradoxical regulatory situation**: the stabilizer used to make avobenzone-containing products viable is itself producing a problem ingredient over shelf life. ACS published a Comment/response (doi:10.1021/acs.chemrestox.1c00265) disputing magnitude but not mechanism. C1.

#### 3. Avobenzone + UV filters with overlapping triplet energies

Some triazine filters can over-quench, dropping protective effect.

---

## Confidence summary

- §1 Identity: C1
- §2 Spectrum (λmax by solvent): C1; ε computed C3, literature confirmed C2
- §3 Photodegradation:
  - Mturi & Martincigh solvent data: C1
  - Schwack & Rudolph photoproduct list: C1 via secondary
  - Quantum yield (numerical): **C5**
  - In-formulation % remaining: C2
- §4 Stabilizers: mechanism C1, comparative effectiveness C2; Downs 2021 C1

## Key references

1. Mturi GJ, Martincigh BS. *J Photochem Photobiol A: Chem* **200**(2008):410–420. doi:10.1016/j.jphotochem.2008.09.001
2. Schwack W, Rudolph T. *J Photochem Photobiol B* (1995) 28:229–234 (avobenzone photoproducts in cyclohexane)
3. Sayre RM, Dowdy JC, Gerwig AJ, Shields WJ, Lloyd RV. *Photochem Photobiol* (2005) 81:452–456. doi:10.1562/2004-02-12-RA-083
4. Bonda CA. (2008) "The Photostability of Organic Sunscreen Actives: A Review." In: *Sunscreens: Regulations and Commercial Development*, Shaath ed., Taylor & Francis.
5. Downs CA et al. *Chem Res Toxicol* (2021) 34:1046–1054. doi:10.1021/acs.chemrestox.0c00461
6. Holt EL et al. *Phys Chem Chem Phys* (2021) 23:24373. doi:10.1039/D1CP03610F
7. Karpkird T et al. *Photochem Photobiol Sci* (2018) — DEHN photophysics. doi:10.1039/c8pp00204e
8. SCCS opinions on UV filters — health.ec.europa.eu
