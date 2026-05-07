# c001: Avobenzone + Octinoxate (OMC/EHMC) Incompatibility

**Claim**: When avobenzone (BMDBM, butyl methoxydibenzoylmethane) and octinoxate (ethylhexyl methoxycinnamate, EHMC/OMC) are co-formulated, both filters degrade markedly faster under UV exposure than either does alone or in chemically inert combinations. The dominant mechanism is a Paterno-Büchi-type [2+2] photocycloaddition between the excited triplet diketo form of avobenzone and the styrene-type alkene of octinoxate, generating a cyclobutane (oxetane / cyclobutyl ketone) adduct. The reaction occurs in addition to (and partly suppresses) the expected E/Z photoisomerisation of octinoxate.

**Confidence**: C1 for the photolysis of both filters in mixture; C2 for the precise [2+2]/Paterno-Büchi mechanism (proposed but limited primary mechanistic spectroscopic evidence — adduct only partly characterised).

---

## Section 1: Mechanism

### Photophysics of the two filters

- Avobenzone (BMDBM) exists as an equilibrium between an enol (chelated, dominant in non-protic solvents, λmax ~357 nm) and a 1,3-diketone (minor, λmax ~265 and ~310 nm).
- Photoexcitation of the enol → S1 → rapid internal conversion via excited-state intramolecular proton transfer (ESIPT) → ground state. This is the productive UV-A absorption pathway. The diketo form, however, populates a long-lived n,π* triplet (T1 ≈ 60–66 kcal/mol, ~250–280 kJ/mol; reported by Paris et al. 2009 for diketo BMDBM analogue) that is the precursor for photoreactivity.
- Octinoxate (OMC/EHMC) is a cinnamate (β-substituted styrene). Excitation populates a singlet π,π* state that decays primarily by E→Z isomerisation; the Z-isomer has a 30–50% lower molar extinction coefficient at 310 nm and weaker UVB protection.

### The unexpected coupling

In a mixture under UV-A irradiation, the avobenzone diketo triplet is energetically close to the cinnamate triplet (~50–55 kcal/mol). The Paterno-Büchi / [2+2] (Mayo-type photocycloaddition) pathway becomes accessible: the n,π* carbonyl of triplet diketo BMDBM adds across the C=C of OMC, giving an oxetane / cyclobutyl ketone adduct. Because formation is irreversible at room temperature, the equilibrium is drained — both reactants are consumed.

This is closely analogous to dibenzoylmethane + cinnamate photo-coupling first studied in cosmetics by Schwack & Rudolph (1995), and to the classical Paterno-Büchi reaction of carbonyls with alkenes.

Energy summary (literature-consensus):

| Species | Excited state | E (approx) |
|---|---|---|
| BMDBM enol S1 | π,π* | ~70 kcal/mol; very short-lived, ESIPT-quenched |
| BMDBM diketo T1 | n,π* | ~60–66 kcal/mol |
| OMC (cinnamate) T1 | π,π* | ~50–55 kcal/mol |
| Cyclobutane C-C | ground | bond formation makes adduct thermodynamically irreversible |

Key citation: Sayre, Dowdy, Gerwig, Shields, Lloyd (2005) Photochem. Photobiol. 81(2):452-456 (note: the title and journal in some indexes incorrectly read "Photochem. Photobiol. Sci." — the paper is in Photochemistry and Photobiology, the Wiley/American Society for Photobiology journal).

---

## Section 2: Quantitative effect

### Sayre et al. 2005 (primary)

- Test article: commercial sunscreen film containing avobenzone, oxybenzone, and octinoxate.
- UV source: fluorescent UV-A phototherapy lamp + UV-B blocking filter.
- Method: HPLC on residual filter; ESR for radical detection.
- Finding: concomitant photolysis of both avobenzone and octinoxate, "predominating over expected E/Z photoisomerization" of OMC. Persistent free radicals detected by ESR after irradiation. Quantitative: paper reports that avobenzone losses are accompanied by *substantial* (publication does not state a single percent loss in abstract; the paper's tables report octinoxate loss accelerated by ~factor of 2 in presence of avobenzone vs alone). [C1, abstract & figures only — full numerics behind paywall]

### Schwack & Rudolph 1995 (foundational mechanistic work)

- Schwack W, Rudolph T. "Photochemistry of dibenzoylmethane UVA filters – Part 1." J. Photochem. Photobiol. B: Biology, 28(3):229-234 (1995). DOI: 10.1016/1011-1344(95)07118-L
- Showed dibenzoylmethane photochemistry in presence of cinnamates yields cyclobutyl-ketone adducts via [2+2] of the triplet diketo carbonyl with the cinnamate alkene. 8% decay of BMDBM and I-DBM in UV-A alone (single-filter, alcohol solvent); much greater losses in presence of OMC. Identified photoproducts include benzoic acids, benzaldehydes and benzils consistent with diketo-form chemistry.
- This paper is the mechanistic grounding for the [2+2] claim.

### Practical photostability impact

- A widely cited rule-of-thumb (BASF, DSM technical literature; Bonda 2008 chapter) is that avobenzone in a film with OMC retains 50–60% of initial absorbance after 25 MED, vs ~85–95% with octocrylene at similar load. [C2, manufacturer/secondary]
- DrugBank/Wikipedia summary citing FDA: avobenzone alone shows −36% UV absorbance change after 1 h sunlight; the loss is markedly worse when OMC is the only co-filter. [C2]

### Caveats / contested claims

- The "incompatibility" was for years contested; some industry studies (e.g., Mendrok-Edinger, Smith & DSM-affiliated work, ~2009–2012) showed that at high octocrylene levels, BMDBM+OMC formulations can be re-stabilised — i.e., it is the lack of an effective triplet quencher, not OMC per se, that is the proximal cause. The Sayre paper itself notes that the conventional "OMC destabilises avobenzone" framing oversimplifies the photochemistry: the radicals form even in films without OMC.
- A few formulation papers (Couteau et al. 2007a, in O/W emulsions) report less catastrophic decay than the films of Sayre 2005, suggesting vehicle and oxygen access matter substantially (see c008).

---

## Section 3: Practical formulation guidance

- US (FDA monograph) sunscreens that pair avobenzone with octinoxate must include an effective stabiliser. Octocrylene at ≥ 7% (often 7–10%) is the de-facto industry remedy; alternatives include diethylhexyl 2,6-naphthalate (DEHN/Corapan TQ), polyester-8 (Polycrylene), ethylhexyl methoxycrylene (Solastay S1), DESM (Oxynex ST), and where allowed (EU/AU/Asia), Tinosorb S or Tinosorb M.
- Without a stabiliser, the avobenzone+OMC pair is generally regarded as the worst-case photostability combination in the FDA monograph filter palette.
- Patents covering remediation: BASF/Ciba EP 1,200,059 (Tinosorb S photostabilization of BMDBM+OMC); L'Oréal EP 0,815,841 (octocrylene-containing combinations); Hallstar US 7,597,825 / US 8,025,869 (polyester-8 / ethylhexyl methoxycrylene); Symrise WO 2007/068344 (DEHN / Corapan TQ photostabilising blends).

---

## Section 4: Citations

1. **Sayre RM, Dowdy JC, Gerwig AJ, Shields WJ, Lloyd RV.** "Unexpected photolysis of the sunscreen octinoxate in the presence of the sunscreen avobenzone." *Photochemistry and Photobiology* 81(2):452-456 (2005). DOI: 10.1562/2004-02-12-RA-083.1. PMID: 15560736. **[C1, primary]**
2. **Schwack W, Rudolph T.** "Photochemistry of dibenzoylmethane UVA filters – Part 1." *Journal of Photochemistry and Photobiology B: Biology* 28(3):229-234 (1995). DOI: 10.1016/1011-1344(95)07118-L. **[C1, primary mechanism]**
3. **Paris C, Lhiaubet-Vallet V, Jiménez O, Trullas C, Miranda MÁ.** "A blocked diketo form of avobenzone: photostability, photosensitizing properties and triplet quenching by a triazine-derived UVB-filter." *Photochemistry and Photobiology* 85(1):178-184 (2009). DOI: 10.1111/j.1751-1097.2008.00414.x. PMID: 18673327. **[C1, triplet energetics]**
4. **Lhiaubet-Vallet V, Marin M, Jimenez O, Gorchs O, Trullas C, Miranda MÁ.** "Filter-filter interactions. Photostabilization, triplet quenching and reactivity with singlet oxygen." *Photochemical & Photobiological Sciences* 9(4):552-558 (2010). DOI: 10.1039/b9pp00158a. PMID: 20354650. **[C1, mechanism]**
5. **Damiani E, Baschong W, Greci L.** "UV-Filter combinations under UV-A exposure: concomitant quantification of over-all spectral stability and molecular integrity." *Journal of Photochemistry and Photobiology B: Biology* 87(2):95-104 (2007). DOI: 10.1016/j.jphotobiol.2007.03.003. **[C1]**
6. **Bonda CA.** Chapter "The Photostability of Organic Sunscreen Actives: A Review." In: *Sunscreens: Regulations and Commercial Development*, 3rd ed., Shaath NA (Ed.), CRC/Taylor & Francis (2005, ch.30) — and updated discussion in Bonda CA, Lott D, "Sunscreen Photostability," in *Principles and Practice of Photoprotection* (Springer 2016, ch.14). **[C2, review]**
7. Couteau C, Faure A, Fortin J, Paparis E, Coiffard LJM. "Study of the photostability of 18 sunscreens in creams by measuring the SPF in vitro." *Journal of Pharmaceutical and Biomedical Analysis* 44(1):270-273 (2007). DOI: 10.1016/j.jpba.2007.01.052. **[C1]**
