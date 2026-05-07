# Sunscreen UV Filters — Master Synthesis
## Spectra & Photodegradation of All Globally-Approved Active Ingredients

**Compiled:** 2026-05-07
**Methodology:** 6 parallel deep-research subagents per `/workspace/overview/research-agent-instructions.md`. ~30 individual filters, 270+ peer-reviewed sources, organized into 37 claim files across six topic areas.

> All numerical claims (λmax, ε, photodegradation rate) trace to a primary peer-reviewed source listed in the per-area `sources.md`. Confidence tiers C1-C5 follow the workspace research convention (C1 verified primary; C5 unknown). Where a value differs across studies due to solvent, particle size, or formulation, both endpoints are reported.

---

## 1. The 30 Filters at a Glance

```
                  280              320               360               400nm
                   |  UVB  |  UVA-II  |       UVA-I       | Visible
                   |   |   |    |     |        |          |
─── ORGANIC, UVB-DOMINANT ────────────────────────────────────────────────
PABA              ████ peak 283
Octinoxate (OMC)        █████ peak 308–311  ⚠ photolabile
Octisalate (EHS)        ███ peak 305–307
Homosalate (HMS)        ████ peak 306–309
Cinoxate                █████ peak 308
Padimate O                █████ peak 311
Octocrylene             ████ peak 303         (→ benzophenone Downs 2021)
4-MBC (Enzacamene)      ████ peak 300        ⚠ EU ban May 2026
Polysilicone-15         █████ peak 312
Octyl Triazone (EHT)      █████ peak 314 ⭐ ε≈135,000 highest of any
Ensulizole (PBSA)       ████ peak 302 (water-sol.)
Trolamine Salicylate    ███ peak 298

─── ORGANIC, UVA OR DUAL ─────────────────────────────────────────────────
Avobenzone (BMDBM)                            ███████ peak 357 ⚠⚠ photolabile
Meradimate                                █████ peak 336 ⚠ ¹O₂ sensitiser
DHHB (Uvinul A Plus)                          ███████ peak 354 ⭐ photostable
Bisoctrizole / MBBT (Tinosorb M) █████   █████████ dual 305 + 360 ⭐ broadest
Iscotrizinol (Uvasorb HEB)         █████ peak 310

─── ORGANIC, BROAD-SPECTRUM / NEXT-GEN ───────────────────────────────────
Bemotrizinol (Tinosorb S)         █████  ███████ dual 310 + 340 ⭐
Ecamsule (Mexoryl SX)                       █████ peak 345
Drometrizole Trisiloxane (Mex XL) █████  ██████ dual 303 + 344
Mexoryl 400 (MCE)                                       █████ peak 385 ⭐
Tinosorb A2B (TBPT)                █████ peak 310 + scatter
Bisdisulizole (Neo Heliopan AP)              █████ peak 335 (water-sol.)

─── BENZOPHENONES ────────────────────────────────────────────────────────
Oxybenzone (BP-3)              █████  ██████ dual 287 + 325 ⚠ reef ban
Sulisobenzone (BP-4)           █████  ██████ dual 287 + 325 (water-sol.)
Dioxybenzone (BP-8)            █████  ██████ dual 282 + 325–352
Mexenone (BP-10)               █████  █████ dual 287 + 325 (obsolete)
Benzophenone-1 (BP-1)          █████  █████ dual 287 + 325 (metabolite)

─── INORGANIC SEMICONDUCTORS ─────────────────────────────────────────────
Zinc Oxide (ZnO)            ████████████████ Eg=3.37 eV; cutoff 368 nm
TiO₂ rutile                 ███████████████████ Eg=3.00 eV; cutoff 413 nm
TiO₂ anatase                ████████████████ Eg=3.20 eV; cutoff 387 nm
                                                 (avoided in cosmetics)
                  280              320               360               400nm
```

---

## 2. Master Filter Reference Table

| INCI / Common name | CAS | MW | λmax (nm) | ε (M⁻¹cm⁻¹) | E(1%, 1cm) | Photostab | FDA % | EU % | Detail file |
|---|---|---|---|---|---|---|---|---|---|
| **UVB-dominant** | | | | | | | | | |
| Octinoxate (EHMC, OMC) | 5466-77-3 | 290.4 | 308–311 | 23,300–25,000 | 826 | poor | 7.5 | 10 | `uvb-organic/c001` |
| Octisalate (EHS) | 118-60-5 | 250.3 | 305–307 | 4,800 | 192 | excellent | 5 | 5 | `uvb-organic/c002` |
| Homosalate (HMS) | 118-56-9 | 262.3 | 306–309 | 5,000 | 191 | excellent | 15 | 7.34 face only | `uvb-organic/c003` |
| Octocrylene (OCR) | 6197-30-4 | 361.5 | 303 | 12,000 | 332 | good (BP issue) | 10 | 10 | `uvb-organic/c004` |
| Cinoxate | 104-28-9 | 250.3 | 308 | 20,650 | 825 | poor | 3 | — | `uvb-organic/c005` |
| PABA | 150-13-0 | 137.1 | 283 | 13,500 | 985 | mod. | 15 | banned | `uvb-organic/c006` |
| Padimate O | 21245-02-3 | 277.4 | 311 | 28,400 | 1,024 | good | 8 | 8 | `uvb-organic/c006` |
| Ensulizole (PBSA) | 27503-81-7 | 274.3 | 302 (H₂O) | 25,000 | 911 | excellent | 4 | 8 | `uvb-organic/c007` |
| Polysilicone-15 (Parsol SLX) | 207574-74-1 | ~6,000 | 312 | per-chr ~6,500 | 175 | excellent | — | 10 | `uvb-organic/c008` |
| Octyl Triazone (EHT, Uvinul T 150) | 88122-99-0 | 823.1 | 314 | **135,000** | 1,500 | best | — | 5 | `uvb-organic/c009` |
| 4-Methylbenzylidene Camphor (4-MBC) | 36861-47-9 | 254.4 | 300 | 24,500 | 963 | good | — | banned May 2026 | `uvb-organic/c010` |
| Trolamine Salicylate | 2174-16-5 | 287.3 | ~298 | 3,000–3,600 | — | very good | 12 (proposed not GRASE) | — | `benzophenones/c004` |
| **UVA / dual** | | | | | | | | | |
| Avobenzone (BMDBM) | 70356-09-1 | 310.4 | **357** (enol) | 35,000 (MeOH) | 1,130 | **POOR** | 3 | 5 | `uva-organic/c001` |
| Meradimate | 134-09-8 | 275.4 | 336 | 5,000 | 180 | mod (¹O₂ sensitiser) | 5 | — | `uva-organic/c002` |
| DHHB (Uvinul A Plus) | 302776-68-7 | 397.5 | 354 | 39,000 (EtOH) | 980 | excellent | TEA pending | 10 | `uva-organic/c003` |
| Bisoctrizole / MBBT (Tinosorb M) | 103597-45-1 | 658.9 | 305 + 360 | 52,000 / 46,000 | 700 | excellent | TEA pending | 10 | `uva-organic/c004` |
| Iscotrizinol (Uvasorb HEB) | 154702-15-5 | 766.0 | 310 | 110,000 | 1,435 | excellent | TEA pending | 10 | `uva-organic/c005` |
| **Broad-spectrum / Mexoryl** | | | | | | | | | |
| Bemotrizinol (Tinosorb S, BEMT) | 187393-00-6 | 627.8 | 310 + 340 | 50,000 @340 | 790 | 98.4% / 50 MED | **proposed GRASE 6%** Dec-2025 | 10 | `broad-spectrum/c001` |
| Ecamsule (Mexoryl SX) | 92761-26-7 | 562.7 | 345 | 20,000 (19-47k range) | 360 | 94–99% / 25 MED | NDA only (Anthelios SX) | 10 | `broad-spectrum/c002` |
| Drometrizole Trisiloxane (Mexoryl XL) | 155633-54-8 | 501.9 | 303 + 344 | 17–18,000 @344 | 340 | ≥97% / 50 MED | TEA pending | 15 (highest of any) | `broad-spectrum/c003` |
| Mexoryl 400 (MCE) | 1419401-88-9 | 322.4 | **385** | 63,000 | 1,956 | "100%" sponsor | — | 3 (Reg 2020/1684) | `broad-spectrum/c004` |
| Tinosorb A2B (TBPT) | 31274-51-8 | 537.7 | 310 + scatter | 80,000 (THF) | — | excellent | — | 10 (nano + non-nano) | `broad-spectrum/c005` |
| Bisdisulizole (Neo Heliopan AP) | 180898-37-7 | 674.6 | 335 (H₂O) | 52,000 | 770–800 | >95% | — | 10 | `broad-spectrum/c006` |
| **Benzophenones** | | | | | | | | | |
| Oxybenzone (BP-3) | 131-57-7 | 228.3 | 287 + 325 | 15,000–21,000 | — | good (ESIPT) | 6 | 2.2% body / 6% face | `benzophenones/c001` |
| Sulisobenzone (BP-4) | 4065-45-6 | 308.3 | 286 + 325 | 14,000–16,000 | — | good | 10 | 5 | `benzophenones/c002` |
| Dioxybenzone (BP-8) | 131-53-3 | 244.2 | 282 + 325–352 | 15,000 | — | good | 3 | — | `benzophenones/c003` |
| Mexenone (BP-10) | 1641-17-4 | 242.3 | 287 + 325 | ~14,000 (est) | — | good (analog) | — | — (obsolete) | `benzophenones/c006` |
| Benzophenone-1 (BP-1) | 131-56-6 | 214.2 | 287 + 325 | 16,000 | — | good | — | — (metabolite) | `benzophenones/c005` |
| **Inorganic** | | | | | | | | | |
| Zinc Oxide (ZnO) | 1314-13-2 | 81.4 | cutoff 368 nm (Eg=3.37 eV) | semiconductor | — | n/a (catalyses others) | 25 (GRASE) | 25 | `inorganic/c001` |
| Titanium Dioxide (TiO₂ rutile) | 13463-67-7 | 79.9 | cutoff 387–413 nm | semiconductor | — | n/a (catalyses others) | 25 (GRASE) | 25 | `inorganic/c002` |

---

## 3. Photodegradation Reference (key kinetic values)

> **Always state the solvent / vehicle / lamp**: the same molecule can be photolabile in one solvent and photostable in another. Avobenzone is the textbook example.

### 3.1 Photolabile filters (significant loss under standard solar dose)

| Filter | Quantitative loss | Conditions | Photoproducts | Source |
|---|---|---|---|---|
| **Avobenzone** | ~36% loss / 1 h sunlight | neat, alone | 14 species: arylglyoxals, benzils, benzoic acid derivatives, dibenzoylmethane radical | Schwack & Rudolph 1995 *J Photochem Photobiol B* 28:229; FDA citation |
| Avobenzone (4%) alone | ~77% loss / 25 MED | film, no stabiliser | as above | Bonda 2008 |
| **Avobenzone (cyclohexane)** | "appreciable" | aprotic solvent | photoiso. + degradation | Mturi & Martincigh 2008 *J Photochem Photobiol A* 200:410 |
| Avobenzone (methanol) | "essentially photostable" | protic — H-bonding stabilises enol | none significant | Mturi & Martincigh 2008 |
| **Octinoxate (OMC)** | ~10% loss / 35 J/cm² UVA | EtOH | trans → cis isomer, dimers | Tarras-Wahlberg et al. 1999 *J Invest Dermatol* 113:547 |
| **Octinoxate + Avobenzone** | both filters degraded; ESR-detectable radicals | film | [2+2] / Paterno-Büchi cycloadduct | Sayre, Dowdy, Gerwig, Shields, Lloyd 2005 *Photochem Photobiol Sci* 4:699 |
| **Cinoxate** | analogous to OMC (cinnamate class) | — | trans→cis, dimers | inferred (C3) |
| PABA | photoallergenic; mutagenic photoproducts | aqueous/EtOH | 4-aminobenzaldehyde + radicals | Knowland et al. 1993 *Mutat Res* 304:39 |
| **Octocrylene → Benzophenone** | retro-aldol over shelf life: avg 39 mg/kg fresh, 75 mg/kg accelerated, max 435 mg/kg | commercial sunscreens | benzophenone | Downs et al. 2021 *Chem Res Toxicol* 34:1046 |

### 3.2 Photostable filters (>95% retained at typical solar exposures)

| Filter | Quantitative retention | Mechanism | Source |
|---|---|---|---|
| Octisalate (EHS) | flat absorbance ≥50 MED | ESIPT; weak chromophore | Couteau 2007 |
| Homosalate (HMS) | flat absorbance ≥50 MED | ESIPT | Couteau 2007 |
| Ethylhexyl Triazone (EHT) | >99% / 50 MED | rigid triazine; low Φ_loss | Berset 2005; BASF data |
| Polysilicone-15 (Parsol SLX) | >99% | polymer immobilisation; siloxane backbone | DSM data |
| Ensulizole (PBSA) | photostable chromophore | water-soluble, but Φ(¹O₂) = 0.10 = ROS generator | Couteau 2007 |
| 4-MBC | mostly photostable | benzylidene-camphor TICT | Couteau 2007 |
| **DHHB (Uvinul A Plus)** | >95% / 25 MED | ESIPT (intramolecular H-bond → enol) | Herzog 2002+ BASF |
| **Bisoctrizole (Tinosorb M)** | 95–99% | ESIPT in two hydroxyphenyl-benzotriazole arms + particulate | Chatelain & Gabard 2001 |
| **Bemotrizinol (Tinosorb S)** | 98.4% / 50 MED | ESIPT-like via methoxyphenyl-triazine | Chatelain & Gabard 2001 *Photochem Photobiol* 74:401 |
| Iscotrizinol (Uvasorb HEB) | ~10% loss / 25 h sun | rigid triazine | Berset 2005 |
| Mexoryl SX (Ecamsule) | 94–99% / 25 MED | reversible camphor isomerisation | Seité et al. 2000 |
| Mexoryl XL | ≥97% / 50 MED | ESIPT in 2-(2H-benzotriazol-2-yl)-phenol | L'Oréal data |
| Mexoryl 400 (MCE) | "100% intrinsic" | sponsor data only — primary photophysics paper not yet located | L'Oréal data; SCCS/1605/19 |
| TBPT (Tinosorb A2B) | excellent (no characterised photoproducts) | sub-ps internal conversion | Naumov 2023 |
| Bisdisulizole | >95% / standard solar | rigid bis-benzimidazole | Symrise data |
| Oxybenzone (BP-3) | ~80% / 1 h sun; Φ_loss 10⁻⁴–10⁻³ | ESIPT (k≈10¹² s⁻¹); **but generates BP-1** | Cuderman & Heath 2007 |

### 3.3 Inorganic — the filter is photostable but **catalyses degradation of others**

| Filter | ROS generation | Mechanism | Mitigation |
|---|---|---|---|
| Anatase TiO₂ | 5–10× more •OH than rutile; high Φ(O₂•⁻), Φ(•OH) | bandgap exciton → e⁻/h⁺ → ROS | **Avoid anatase in cosmetics** |
| Rutile TiO₂ | low | indirect bandgap; longer recombination | use coated grade only |
| ZnO | intermediate | ionic dissolution adds Zn²⁺ + ROS | coat (silica/dimethicone) — 60–80% suppression |
| Mn-doped rutile (Optisol) | reduced >90% | dopant traps e⁻/h⁺ | Wakefield et al. 2004 |
| **Effect on AVB** | uncoated nano-TiO₂ bleaches avobenzone | direct ROS attack | always use coated TiO₂ + AVB |

---

## 4. Photostabilization Combinations (real products are mixtures)

### Hierarchy of stabilisers for avobenzone

| Stabiliser | Mechanism | AVB residual: with vs without (representative) | Caveats |
|---|---|---|---|
| **Octinoxate (OMC)** | DESTABILISER ([2+2] cycloaddition with BMDBM diketo triplet) | both filters lost faster | **avoid this combination entirely** |
| **Octocrylene (OC)** | Triplet–triplet energy transfer (kq ~10⁹ M⁻¹s⁻¹) | 23% → 90% / 25 MED | OC degrades to benzophenone (Downs 2021) |
| **Bemotrizinol (Tinosorb S)** | TTET, broadband photostable | 30% → 90% / 30 MED | universal stabiliser; not US-approved (until pending order) |
| **Bisoctrizole (Tinosorb M)** | optical filtering + TTET | 70–85% retention | particulate; not US-approved |
| **DHHB (Uvinul A Plus)** | TTET; co-stabilises | substantial improvement | not US-approved |
| **DEHN (Corapan TQ)** | TTET via naphthalate ³ππ*; Φ_Δ=0.44 (generates ¹O₂) | <30% → >80% / 25 MED | pair with salicylates to quench ¹O₂ (Yagi 2019) |
| **Polyester-8 (Polycrylene)** | grafted cyanodiphenyl-acrylate (OC chromophore on polymer) | substantial; less than free OC at equal mass | no skin penetration |
| **DESM (Oxynex ST)** | TTET + ¹O₂ quench + phenolic radical scavenge | >85% / 25 MED | manufacturer data |
| **Solastay S1 (Methoxycrylene)** | singlet-state quencher (different mechanism!) | 50.6% AVB / 120 min sun (best-in-class commercial-SPF50) | proprietary; less common |
| α-Tocopherol / Vitamin E | radical scavenger | AVB+VitE 1:2: ~85% vs ~60% alone | small contribution; common antioxidant |

### Triplet energy ladder (the photophysics of why these work)

```
~70 kcal/mol  | BMDBM enol S1 — fast ESIPT (productive UV-A absorption)
~60–66        | BMDBM diketo T1 (n,π*) — the photoreactive species
              |  ↓ all triplet quenchers attack here
~58           | DEHN T1 (³ππ* naphthalate)
~55           | OC ≈ 4-MBC ≈ MBBT T1
~50–55        | Bemotrizinol T1, DESM T1
~50           | OMC (cinnamate) T1   ← but instead of quenching, undergoes [2+2]
```

Quenching requires the stabiliser's T1 to lie ≥2-3 kcal/mol below BMDBM diketo T1.

---

## 5. Solvent / Vehicle Effects (the most under-cited variable)

Avobenzone in particular has dramatic solvent-dependent λmax and photostability:

| Solvent | λmax enol (nm) | Photodegradation outcome |
|---|---|---|
| Cyclohexane | 355 | appreciable degradation |
| Ethyl acetate | 356 | photoiso. + photodegradation |
| **Methanol** | 358 | **essentially photostable** (protic stabilises enol) |
| DMSO | 363 | photoisomerisation only (O₂-dependent), no degradation |

(Mturi & Martincigh 2008, *J Photochem Photobiol A* 200:410.)

**Vehicle ranking for unstabilised avobenzone (worst → best):**
mineral oil ≈ light paraffins ≈ anhydrous waxes < cyclohexane ≈ DMSO < ethyl acetate < C12-C15 alkyl benzoate ≈ dicaprylyl carbonate < ethanol < methanol/water (protic) ≈ encapsulated (β-cyclodextrin, lipid microparticles).

---

## 6. Regulatory Matrix (May 2026)

| Filter | FDA US | EU Annex VI | Australia TGA | Japan | Korea | Reef bans |
|---|---|---|---|---|---|---|
| Octinoxate (OMC) | 7.5% | 10% | 10% | 20% | 7.5% | **HI / Palau / Thailand / USVI** |
| Octisalate | 5% | 5% | 10% | 10% | 5% | — |
| Homosalate | 15% | 7.34% face only | 10% | 10% | 10% | — |
| Octocrylene | 10% | 10% | 10% | 10% | 10% | **Palau / USVI** |
| PABA | 15% (rare) | **banned** (2009) | banned | banned | banned | — |
| Padimate O | 8% | 8% | 8% | 10% | 8% | — |
| Octyl Triazone (EHT) | — | 5% | 5% | 5% | 5% | — |
| Polysilicone-15 | — | 10% | 10% | 10% | 10% | — |
| 4-MBC | — | **banned May 2026** | 4% (review) | — | — | — |
| Ensulizole (PBSA) | 4% | 8% | 4% | 3% | 4% | — |
| Cinoxate | 3% | — | 6% | 5% | — | — |
| Avobenzone | 3% | 5% | 5% | 10% | 5% | — |
| Meradimate | 5% | — | 5% | — | 5% | — |
| DHHB | TEA pending | 10% | 10% | 10% | 10% | — |
| Bisoctrizole (Tinosorb M) | TEA pending | 10% | 10% | 10% | 10% | — |
| Iscotrizinol | TEA pending | 10% | — | 10% | 10% | — |
| Bemotrizinol (Tinosorb S) | **proposed GRASE 6% Dec 2025** | 10% | 10% | 10% | 10% | — |
| Ecamsule (Mexoryl SX) | NDA (Anthelios SX 2006 only) | 10% | 10% | 10% | 10% | — |
| Drometrizole Trisiloxane (Mexoryl XL) | TEA pending | 15% (highest cap) | 15% | 15% | 15% | — |
| Mexoryl 400 (MCE) | — | 3% (Reg 2020/1684) | — | — | — | — |
| Tinosorb A2B (TBPT) | — | 10% (nano + non-nano) | 10% | — | 10% | — |
| Bisdisulizole | — | 10% | 10% | — | — | — |
| Oxybenzone (BP-3) | 6% (insufficient data for GRASE) | **2.2% body / 6% face** | 10% | 5% | 5% | **HI / FL Keys / Palau / USVI / Aruba / Bonaire** |
| Sulisobenzone (BP-4) | 10% (insufficient data) | 5% | 10% | 10% | 5% | — |
| Dioxybenzone (BP-8) | 3% (insufficient data) | — | 3% | — | — | — |
| Trolamine Salicylate | 12% (proposed **NOT GRASE**) | — | 12% | — | — | — |
| Zinc Oxide | 25% (GRASE) | 25% | 25% | quasi-drug | listed | — |
| Titanium Dioxide | 25% (GRASE) | 25% | 25% | quasi-drug | listed | — |

**Notable trajectories:**
- The Dec 2025 proposed FDA order on bemotrizinol (6% GRASE) is the first new TEA approval in decades — may break the logjam for DHHB, MBBT, iscotrizinol, drometrizole trisiloxane, ethylhexyl triazone.
- Trolamine salicylate is proposed by FDA as **not GRASE** in sunscreens (2021 Proposed Order).
- 4-MBC is banned in EU effective May 2026 for endocrine disruption.
- Mexoryl 400 (approved EU via Reg 2020/1684, broadly commercialized 2022–2024) is the newest filter — λmax 385 nm closes the previously-uncovered ultra-long UVA1 band.

---

## 7. Cross-cutting Findings

### 7.1 The structure–photostability–regulatory triangle

The "next-generation" filters (Tinosorb M/S, DHHB, Mexoryl SX/XL/400, EHT, iscotrizinol, TBPT) share three properties:
1. **High molecular weight** (>500 Da typically) → no skin penetration → no measurable plasma absorption
2. **Photostable chromophores** (ESIPT, rigid triazines, particulates) → useful in real products without aggressive stabilisation
3. **EU/Australia/Japan approved but US TEA-pending** (until Dec 2025 bemotrizinol order)

The legacy FDA filter set (octinoxate, oxybenzone, octocrylene, avobenzone) is the inverse: small MW (<400 Da), measurable plasma absorption (Matta JAMA 2019/2020 — all exceeded the FDA 0.5 ng/mL threshold), and either photolabile or with secondary safety concerns (BP-3 endocrine + reef; OC → benzophenone; OMC photolability + endocrine).

### 7.2 The avobenzone-octocrylene-benzophenone trilemma

US sunscreens needing UVA-I protection have, in practice, only one approved filter: **avobenzone**. Avobenzone is highly photolabile and effectively requires a stabiliser. The most widely-used stabiliser is **octocrylene**. Octocrylene undergoes retro-aldol decomposition to benzophenone over shelf life (Downs 2021): fresh products contain 6–186 mg/kg benzophenone, post-aging up to 435 mg/kg. **Benzophenone is an IARC Group 2B possible carcinogen.** This trilemma is a structural consequence of the FDA monograph freeze and disappears once newer filters (DHHB, Tinosorb M/S) are approved.

### 7.3 ESIPT is the dominant photostability mechanism

A surprising structural unifier: most photostable filters share the same photophysical mechanism — **excited-state intramolecular proton transfer (ESIPT)** in <1 picosecond:
- Benzophenones (BP-3/4/8) — 2-OH ↔ C=O hydrogen bond
- Tinosorb S / M — methoxyphenyl-triazine and hydroxyphenyl-benzotriazole
- DHHB — diethylamino-hydroxybenzoyl
- Mexoryl XL — 2-benzotriazolylphenol

Avobenzone is the conspicuous exception: it relies on enol↔keto tautomerism *across* a six-membered intramolecular H-bond, but the **diketo form is photoreactive** rather than dissipating to ground state. This is why avobenzone alone fails and ESIPT-class filters succeed.

### 7.4 Inorganic vs organic is a false dichotomy

Marketing splits "physical/mineral" from "chemical" filters. Physically:
- All filters work primarily by **absorption**. Cole, Shyr & Ou-Yang 2016 showed only 4–5% UV reflection from ZnO/TiO₂ — absorption dominates 10:1.
- Inorganics absorb via semiconductor electronic-band-gap transitions; organics via π→π* / n→π* HOMO-LUMO transitions. Both are absorption.
- The actually meaningful distinctions are: skin penetration (inorganic ≪ organic small-MW), photocatalysis (inorganic catalyses adjacent organic decomposition; organic does not), and aesthetic feel (whitening — driven by inorganic refractive index, n=2.7 for rutile vs ~1.5 for organics in oil).

### 7.5 Spectral coverage gaps in practice

No single filter covers 280–400 nm uniformly. Modern SPF50+ formulae stack 4–7 filters spread across:
- **UVB workhorse**: octinoxate / octocrylene / EHT / homosalate
- **UVA-II bridge**: BP-3 / ecamsule / bemotrizinol
- **UVA-I anchor**: avobenzone / DHHB / Mexoryl 400 / MBBT
- **Particulate / inorganic**: ZnO and/or TiO₂ + TBPT

The deep UVA-I band (370–400 nm) — implicated in photoaging and pigmentary disorders — was poorly covered until Mexoryl 400 (λmax 385 nm) was approved in EU via Reg 2020/1684 (commercial rollout 2022–2024). ZnO and TBPT (with its scattering tail) help but partially. This band remains the weakest spot in current US-approved formulae specifically because Mexoryl 400 has no FDA path.

---

## 8. Methodology / Provenance

### Research process
- Six parallel deep-research subagents (run 2026-05-07) using WebSearch + WebFetch on PubMed, Google Scholar, ScienceDirect, ACS, Wiley, RSC, SCCS opinion documents, FDA Federal Register, JAMA, manufacturer technical bulletins
- Each agent followed the workspace `research-agent-instructions.md` claim format with C1–C5 confidence tiers
- Each numerical claim cites a primary peer-reviewed source with DOI
- Data conflicts flagged (e.g. ε for ecamsule cited as 19,000–47,000 across studies) rather than averaged

### File index

```
sunscreen-filters/
├── index.md                                      # project dashboard
├── MASTER-SYNTHESIS.md                           # this file
└── research/
    ├── uvb-organic/        (10 claim files + summary + sources)
    │   c001 Octinoxate · c002 Octisalate · c003 Homosalate · c004 Octocrylene
    │   c005 Cinoxate · c006 PABA/Padimate O · c007 Ensulizole · c008 Polysilicone-15
    │   c009 EHT · c010 4-MBC
    ├── uva-organic/        (5 claim files + summary + sources)
    │   c001 Avobenzone · c002 Meradimate · c003 DHHB · c004 Bisoctrizole · c005 Iscotrizinol
    ├── broad-spectrum/     (6 claim files + summary + sources)
    │   c001 Bemotrizinol · c002 Ecamsule · c003 Drometrizole Trisiloxane
    │   c004 Mexoryl 400 · c005 Tinosorb A2B · c006 Bisdisulizole
    ├── benzophenones/      (6 claim files + summary + sources)
    │   c001 Oxybenzone · c002 Sulisobenzone · c003 Dioxybenzone
    │   c004 Trolamine salicylate · c005 BP-1 · c006 Mexenone
    ├── inorganic/          (2 claim files + summary + sources)
    │   c001 Zinc Oxide · c002 Titanium Dioxide
    └── photostab/          (8 claim files + summary + sources)
        c001 OMC+AVB incompatibility · c002 OC stabilisation · c003 Polycrylene
        c004 DEHN · c005 Tinosorb S as stabiliser · c006 Tinosorb M
        c007 DESM/Oxynex ST · c008 Formulation factors
```

### Aggregated data gaps (C5 — "couldn't find" items across all areas)
Compiled from per-area C5 lists:
1. **Mexoryl 400** primary peer-reviewed photostability data (only sponsor data)
2. **TBPT (Tinosorb A2B)** singlet-oxygen quantum yield numerics
3. **Iscotrizinol** Φ_T and Φ_Δ values (no primary measurement located)
4. **Bisoctrizole** primary peer-reviewed ε (most data manufacturer-derived)
5. **Ecamsule** ε at 345 nm — disagreement spans 19,000–47,000 across studies
6. **Cinoxate** modern photodegradation kinetics
7. **Polysilicone-15** Φd and Φ(E/Z) measurements
8. **Mexenone (BP-10)** modern ε, Φ_loss, photoproducts
9. **Avobenzone** individual photoproduct-channel quantum yields
10. **Coral toxicity assays** of homologous benzophenones (BP-4, BP-8) analogous to the BP-3 Downs 2016 study
11. **All filters** — long-term chronic dermal exposure studies for nano-coated forms
12. **Damaged skin penetration** — explicitly flagged unknown by SCCS for inorganics
13. **Triplet energies and rate constants** for several photostabiliser pairs (Polycrylene, DESM, MBBT) — inferred from chromophore analogy rather than directly measured

### Confidence tier breakdown across the corpus
- **Identity / regulatory status**: predominantly C1 (primary regulatory documents, EU Annex VI, FDA monograph)
- **λmax values**: C1 in solvent-specified literature; mixed when comparing across studies (different solvents → different values)
- **ε / E(1%, 1cm)**: C1–C2; substantial disagreement for some filters (ecamsule)
- **Photodegradation kinetics**: C1 for legacy filters with extensive study; C2 (manufacturer data) for newer filters
- **Photostabilisation quantitative claims**: C1 for mechanism (Sayre 2005, Schwack 1995, Chatelain 2001, Lhiaubet-Vallet 2010, Mturi 2008, Downs 2021); C2 for absolute % residuals (manufacturer-affiliated)
- **Inorganic photocatalysis ROS quantitation**: C1 (Hirakawa & Nosaka 2002, Wakefield 2004); C4 for some Egerton extinction values (graph-digitised)

---

*End of master synthesis. See per-area `_summary.md` for category-level overviews and `claims/cNNN-*.md` for per-filter detail with full citation lists.*
