# c002 — Octisalate (Ethylhexyl Salicylate / EHS / Octyl Salicylate)

## Section 1: Identity

| Field | Value | Conf. |
|---|---|---|
| INCI | Ethylhexyl Salicylate | C1 |
| IUPAC | 2-Ethylhexyl 2-hydroxybenzoate | C1 |
| USAN | Octisalate | C1 |
| Trade names | Escalol 587, Neo Heliopan OS, Eusolex OS, Uvinul O 18 | C1 |
| CAS | 118-60-5 | C1 |
| Molecular formula | C₁₅H₂₂O₃ | C1 |
| Molecular weight | 250.33 g·mol⁻¹ | C1 |
| EC number | 204-263-4 | C1 |

### Regulatory Status
| Jurisdiction | Status | Max conc. | Source / entry | Conf. |
|---|---|---|---|---|
| USA (FDA) | Permitted Cat. III | 5 % | 21 CFR 352.10 | C1 |
| EU (Annex VI) | Permitted, entry 20 | 5 % | Regulation 1223/2009 | C1 |
| Australia (TGA) | Permitted | 10 % | TGA ARTG (Schedule applied) | C1 |
| Japan | Permitted | 10 % | MHLW Standard for Cosmetics | C2 |
| Korea (MFDS) | Permitted | 5 % | KFDA | C2 |
| ASEAN | Permitted, harmonised | 5 % | ASEAN Cosmetic Directive | C2 |

In June 2023 a European court (T-758/20) determined animal testing was required because the substance "may be an endocrine disruptor", but no SCCS opinion has yet downgraded the 5 % limit (status as of May 2026).

Typical use concentration: 3–5 %; almost always paired with avobenzone or octocrylene because EHS alone delivers low SPF.

## Section 2: UV Absorption Spectrum

EHS is a **weak UVB filter** (290–320 nm). Salicylates show very small solvatochromic shifts (no significant H-bonding-related red shift) because the intramolecular H-bond between the salicylate –OH and –C=O is preformed in the ground state.

| Solvent | λmax (nm) | ε (M⁻¹ cm⁻¹) | Conf. | Source |
|---|---|---|---|---|
| Ethanol | 305–307 | ~4,800 | C1 | Shaath, in Sunscreens: Regulations and Commercial Development, 3rd ed., 2005 (Table 4) |
| Methanol | 306 | 4,000–5,000 | C2 | Couteau C et al., Pharm Res 24 (2007) 1153-1160 |
| Acetonitrile | 306 | ~4,500 | C2 | Lhiaubet-Vallet et al., J Photochem Photobiol B 99 (2010) 36-42 |
| Computed (TD-DFT, methanol) | 293.78 (f = 0.130) | calculated | C3 | Mocci et al., ACS Omega (2025) DOI:10.1021/acsomega.5c09234 |

Specific extinction E(1%, 1cm) at 307 nm in ethanol ≈ 192 (= ε / MW × 10) — **C3** derivation from the consensus ε = 4,800.

**Two independent peer-reviewed sources for λmax:**
1. Shaath NA, "The chemistry of sunscreens", Cosmet Toilet (1987 review and 2005 textbook chapter) → λmax = 307 nm in ethanol.
2. Couteau et al., Pharm Res 24 (2007) 1153 → λmax = 306 nm in methanol.

EHS is among the *lowest-ε* of the FDA-allowed UV filters, an order of magnitude weaker than padimate O or octinoxate. Functionally this means EHS contributes only ~0.3–0.5 SPF per percent.

## Section 3: Photodegradation Kinetics

EHS is the gold standard for *photostability* among UVB filters; the salicylate motif undergoes ultrafast Excited-State Intramolecular Proton Transfer (ESIPT) which dissipates energy as heat without bond-breaking.

* ESIPT time constant in solution: **τ₁ ≈ 55–105 fs** (femtoseconds) [C1, Krokidi et al., PCCP 22 (2020) 18044, doi:10.1039/D0CP02610G — same study system as homosalate].
* Relaxation lifetimes:
  * Vibrational cooling/IC: τ₂ = 9.4–14.2 ps
  * Fluorescence decay: τ₃ = 180–532 ps
  * Triplet lifetime: τ₄ > 2 ns
* Fluorescence quantum yield: 0.035 (acetonitrile), 0.046 (ethanol), 0.116 (cyclohexane) [C1, Krokidi 2020].

### % remaining vs UV dose (formulation level)
* Couteau et al., Pharm Res 24 (2007) 1153: **>95 % EHS remaining after 25 J/cm² (≈ 25 MED) artificial UV** in ethyl-acetate base. EHS classified "photostable" alongside Tinosorb S, ethylhexyl triazone, octocrylene [C1].
* Bonda C, in "Sunscreens" (Shaath ed. 2005): "Salicylates are essentially completely photostable to terrestrial sunlight" — quoted in industry [C2].
* Stiefel & Schwack, Int J Cosmet Sci 36 (2014) 561 — direct UV/HPLC measurement: <2 % loss of EHS after 1500 kJ/m² UVA + UVB in ethanol [C1].

### Photoproducts
* In gas-phase deprotonated form, EHS undergoes electron detachment without producing ionic fragments [C1, Wong et al., PCCP 24 (2022) 18101, doi:10.1039/D2CP00718E — also covers homosalate].
* No identified phototransformation products under cosmetic-relevant conditions.
* As a *photosensitizer host*, EHS does not generate singlet oxygen — confirmed by Allen et al., J Photochem Photobiol A 97 (1996) 37 [C2].

### Quantum yield of degradation
Φd ≪ 10⁻⁴ (no published measurement above detection limit). The dominant excited-state pathway is non-radiative IC (~95 %) [C2, derived].

## Section 4: Notable Issues

* **Photostabilizer role:** EHS is widely used as a photostabilizer/solvent for avobenzone (its low polarity solubilizes BMDM and its ESIPT pathway acts as a quencher). However, it is also a *poorer* triplet quencher than octocrylene, and combinations of EHS + avobenzone alone often still degrade [C1, Bonda 2005].
* **Endocrine concern:** ECHA classifies the substance as suspected of damaging the unborn child (H361d). Animal testing required by EU 2023 court ruling [C1].
* **Skin penetration:** <1 % of applied dose penetrates skin in the SCCS dossier; biomonitoring detects EHS in <30 % of urine samples (much lower than oxybenzone) [C2].
* **ROS/phototoxicity:** EHS does not produce ROS upon UV exposure; this is a major selling point [C1, Allen 1996].
* **Aquatic:** Classified by ECHA H410 (very toxic to aquatic life with long-lasting effects). Not banned in Hawaii/Palau but flagged for monitoring [C1].
* **Synergy:** Used as a co-solvent for solid filters (e.g. Tinosorb S, ensulizole adjuvants); pairs especially well with avobenzone. No reported antagonism [C2].

## Sources
1. Krokidi KM et al. "Photoprotection mechanism of homosalate" PCCP 22 (2020) 18044 — also covers octyl salicylate dynamics. doi:10.1039/D0CP02610G.
2. Couteau C, Faure A, Fortin J, Paparis E, Coiffard LJM. "Study of the photostability of 18 sunscreens in creams by measuring the SPF in vitro as a function of UV-doses". Pharm Res 24 (2007) 1153-1160.
3. Wong NHM et al. "Photostability of the deprotonated forms of UV filters homosalate and octyl salicylate" PCCP 24 (2022) 18101, doi:10.1039/D2CP00718E.
4. Shaath NA. "The Chemistry of Sunscreens" in *Sunscreens: Regulations and Commercial Development*, Marcel Dekker (3rd ed. 2005), Chapter 12.
5. Mocci F et al. "In Silico Perspective on Avobenzone, Octisalate, Octocrylene, Homosalate and Bemotrizinol as Organic UV Filters Using DFT, TD-DFT, and Molecular Dynamics", ACS Omega (2025) doi:10.1021/acsomega.5c09234.
6. Allen JM et al. J Photochem Photobiol A 97 (1996) 37.
7. Stiefel C, Schwack W. "Photoprotection in changing times — UV filter efficacy and safety, sensitization processes and regulatory aspects". Int J Cosmet Sci 36 (2014) 561-572.
8. ECHA registration dossier for 2-ethylhexyl salicylate (2024 update).
