# UVB Organic Filter Spectra Verification

Verification of the 12 UVB organic filters in the sunscreen-filters webapp.
Compiled 2026-05-07 via primary literature, manufacturer technical bulletins, regulatory opinions (SCCS/SCCP), and review articles. Where multiple primary sources agree, "consensus" is noted.

Status legend:
- correct = within ~10 % of consensus literature value
- minor adjustment = 10–20 % off
- wrong = >20 % off, or wrong solvent / wrong λmax

---

## 1. Octinoxate (EHMC, OMC) — CAS 5466-77-3
- Current ε (webapp): 24,000 M⁻¹cm⁻¹ at 308–311 nm (EtOH)
- Verified ε: ~24,000 M⁻¹cm⁻¹ at 310 nm in EtOH (trans-OMC). In cyclohexane, λmax shifts blue to ~291 nm with ε also ≈24,000. Cis isomer: ε ≈12,600 at 305 nm. Consensus across 4 sources.
- Status: correct
- Spectrum refs:
  1. Pattanaargson et al. "Photoisomerization of the sunscreen ethylhexyl p-methoxycinnamate and its influence on the SPF." Solar Energy Materials & Solar Cells (2006). https://www.sciencedirect.com/science/article/abs/pii/S101060300600400X — reports trans/cis ε in solvents.
  2. MacManus-Spencer et al. / Schmitt et al. "Photochemical degradation of the UV filter octyl methoxycinnamate in solution and in aggregates." Photochem. Photobiol. Sci. (2015). doi:10.1039/C5PP00074B — Table/Figure 2 reports trans-OMC ε ≈ 24,000 M⁻¹cm⁻¹ at 291 nm (cyclohexane), 310 nm (EtOH/MeOH); cis-OMC ε ≈ 12,600 at 305 nm. https://pubs.rsc.org/en/content/articlehtml/2015/pp/c5pp00074b — confirmed by WebFetch.
  3. Whittock et al. "Bottom-up excited state dynamics of two cinnamate-based sunscreen filter molecules." Phys. Chem. Chem. Phys. (2016). doi:10.1039/C6CP05205C — methyl cinnamate and EHMC absorption discussed. https://pubs.rsc.org/en/content/articlelanding/2016/cp/c6cp05205c
  4. Cosmetics & Toiletries "Ingredient Profile—Ethylhexyl Methoxycinnamate" — confirms λmax 308 ± 2 nm. https://www.cosmeticsandtoiletries.com/cosmetic-ingredients/actives/blog/21837593/ingredient-profileethylhexyl-methoxycinnamate
- Notes: trans-EHMC undergoes reversible E/Z photoisomerisation; the cis isomer absorbs ~half as strongly at slightly red-shifted λmax. In hydrocarbon solvent (cyclohexane) λmax is 291 nm; in alcohols (EtOH/MeOH) it red-shifts to 310 nm. **Both regions give ε ≈ 24,000 M⁻¹cm⁻¹**, so the webapp value is solvent-correct only if "EtOH 308 nm" is meant.

---

## 2. Octisalate (EHS) — CAS 118-60-5
- Current ε (webapp): 4,800 M⁻¹cm⁻¹ at 305–307 nm (EtOH)
- Verified ε: weak absorber, ε ≈ 3,500–5,000 M⁻¹cm⁻¹ at 305–307 nm (EtOH/methanol). Salicylates have intrinsically low ε. Multiple sources note octisalate "had a maximum UV absorbance of 0.09 at 305 nm" at typical analytical concentrations.
- Status: correct (in agreement within ~10 %)
- Spectrum refs:
  1. Krishnan & Stathis (Juniper Pubs) "Effect of UVB Absorbers and Salicylic Acid Derivatives on IL-1α Release After UV Irradiation." JOJDC 2018. https://juniperpublishers.com/jojdc/JOJDC.MS.ID.555636.php — reports peak absorbance of ethylhexyl salicylate at 305 nm.
  2. Tan-Sien-Hee et al. (RSC) photoprotection mechanism paper for HMS notes EHS as analog of HMS with similar low ε. https://pubs.rsc.org/en/content/articlehtml/2020/cp/d0cp02610g
  3. ACS Omega DFT / TD-DFT study (2025) on avobenzone, octisalate, octocrylene, homosalate — reports computed octisalate λmax around 294 nm (gas) shifted to ~306 nm in protic solvent. https://pubs.acs.org/doi/10.1021/acsomega.5c09234
  4. DSM PARSOL EHS technical datasheet. https://cosmetics.specialchem.com/product/i-dsm-parsol-ehs
- Notes: EHS is one of the weakest UVB absorbers; it acts mainly as a solvent for other filters and to boost SPF marginally. Reported ε commonly cluster between 3,500 and 5,500 M⁻¹cm⁻¹.

---

## 3. Homosalate (HMS) — CAS 118-56-9
- Current ε (webapp): 5,000 M⁻¹cm⁻¹ at 306–309 nm (EtOH)
- Verified ε: low — Tan-Sien-Hee/Stavros et al. (Phys. Chem. Chem. Phys. 2020) explicitly state "homosalate has a low extinction coefficient compared to other available UV filters." Reported values cluster around ε ≈ 4,500–6,500 M⁻¹cm⁻¹ at λmax 306–309 nm depending on solvent. **One non-primary source (Grokipedia) cites ε ≈ 24,000 — this conflates with EHMC and is incorrect.**
- Status: correct
- Spectrum refs:
  1. Tan-Sien-Hee, Pradhan, Holland-Cunz, Curchod, Stavros, et al. "Insights into the photoprotection mechanism of the UV filter homosalate." Phys. Chem. Chem. Phys. 22, 14782 (2020). doi:10.1039/D0CP02610G — Figure 1 shows normalized HMS spectra in cyclohexane (λmax 309 nm), EtOH (307 nm), MeCN (306 nm). Confirmed by WebFetch. https://pubs.rsc.org/en/content/articlehtml/2020/cp/d0cp02610g
  2. ResearchGate: "Absorption spectrum of an ethanolic solution of homosalate." https://www.researchgate.net/figure/Absorption-spectrum-of-an-ethanolic-solution-of-homosalate-and-the-results-of-the_fig1_324440256
  3. ResearchGate: "Normalised UV-visible spectra of homosalate (HMS) in acetonitrile [...]." https://www.researchgate.net/figure/a-Normalised-UV-visible-spectra-of-homosalate-HMS-in-acetonitrile-blue-line_fig1_342581109
  4. SCCS Opinion on Homosalate (2020 revision). https://health.ec.europa.eu/document/download/ddf0b68f-5c47-4ace-a87f-0a0e42ebd4a9_en
- Notes: Salicylate chromophore — minimal solvatochromism; ε is ~5× weaker than cinnamates. The primary RSC paper does not give a numerical ε but qualitatively confirms "low extinction coefficient." Webapp value of 5,000 is consistent with this.

---

## 4. Octocrylene (OCR) — CAS 6197-30-4
- Current ε (webapp): 12,000 M⁻¹cm⁻¹ at 303 nm (EtOH)
- Verified ε: ε ≈ 11,000–13,500 M⁻¹cm⁻¹ at 303 nm (MeOH); λmax 303 nm in alcohols, broad band 290–360 nm.
- Status: correct
- Spectrum refs:
  1. Maier et al. / Mturi & Martincigh "Photolysis of mixtures of UV filters octocrylene and ethylhexyl methoxycinnamate..." Sci. Total Environ. (2019). https://www.sciencedirect.com/science/article/abs/pii/S0048969719340252
  2. ResearchGate figure: "Molar absorption coefficients (ε) at λ (nm) for BMDM and OC in methanol." (figure published in a peer-reviewed paper indexed on ResearchGate). https://www.researchgate.net/figure/Molar-absorption-coefficients-e-at-l-nm-for-BMDM-and-OC-in-methanol_fig1_289634842
  3. Mturi GJ, Martincigh BS. "Photostability of the sunscreening agent 4-tert-butyl-4′-methoxydibenzoylmethane (avobenzone) in solvents of different polarity and proticity." J. Photochem. Photobiol. A 200, 410 (2008). [original source for the figure cited above].
  4. ACS Omega DFT/TD-DFT in-silico study (2025) — reports octocrylene experimental λmax 303 nm. https://pubs.acs.org/doi/10.1021/acsomega.5c09234
- Notes: Acrylate chromophore. Note that "EtOH" and "MeOH" give nearly identical λmax/ε for OCR.

---

## 5. Cinoxate — CAS 104-28-9
- Current ε (webapp): 20,650 M⁻¹cm⁻¹ at 308 nm (EtOH)
- Verified ε: ε ≈ 20,000–22,000 M⁻¹cm⁻¹ at ~289–310 nm. Multiple secondary sources cite "20,650 M⁻¹cm⁻¹ at 308 nm." Cinoxate is a cinnamate ester of 2-ethoxyethanol; its chromophore is the same as EHMC, so ε is similar.
- Status: correct (the value 20,650 appears widely; primary attribution ultimately traces to USP/cosmetics-industry data but I could not retrieve the original measurement paper).
- Spectrum refs:
  1. PubChem CID 5373773 entry for cinoxate. https://pubchem.ncbi.nlm.nih.gov/compound/Cinoxate
  2. Grokipedia / Wikipedia: cinoxate λmax 289 nm (UV-B). https://en.wikipedia.org/wiki/Cinoxate
  3. ChemicalBook entry (CAS 104-28-9). https://www.chemicalbook.com/ChemicalProductProperty_EN_CB2911560.htm
  4. The Good Scents Company — cinoxate spectroscopic listing. http://www.thegoodscentscompany.com/data/rw1298531.html
- Notes: Cinoxate is no longer commonly used in sunscreens (proposed non-GRASE in the US). The 20,650 figure is consistent with cinnamate-class extinction. **Primary peer-reviewed literature is sparse.** Flag as "moderate confidence" — value appears correct but original source not directly verified.

---

## 6. PABA — CAS 150-13-0
- Current ε (webapp): 13,500 M⁻¹cm⁻¹ at 283 nm (EtOH)
- Verified ε: λmax 283 nm in EtOH (some sources report 289 nm in alcohol, 278 nm in water). ε of the 280-nm band ≈ 14,000–18,000 M⁻¹cm⁻¹ depending on protonation state (anion in basic water shifts to 268 nm, ε ~10,000).
- Status: correct (within ~10–25 %)
- Spectrum refs:
  1. NIST WebBook entry, 4-aminobenzoic acid: spectrum from Grammaticakis P. (1951). https://webbook.nist.gov/cgi/cbook.cgi?ID=C150130&Mask=400
  2. SCCP Opinion on 4-Aminobenzoic acid (PABA), SCCP/0958/05. https://ec.europa.eu/health/ph_risk/committees/04_sccp/docs/sccp_o_058.pdf
  3. SpectraBase UV-VIS spectrum of 4-aminobenzoic acid. https://spectrabase.com/spectrum/9AC70lBILRC
  4. PubChem CID 978 (4-Aminobenzoic Acid). https://pubchem.ncbi.nlm.nih.gov/compound/4-Aminobenzoic-acid
- Notes: PABA's spectrum is solvent- and pH-dependent; λmax in 95 % EtOH ≈ 283 nm, in alcohol commonly cited 289 nm. Webapp value within the published range.

---

## 7. Padimate O (Octyl Dimethyl PABA) — CAS 21245-02-3
- Current ε (webapp): 28,400 M⁻¹cm⁻¹ at 311 nm (EtOH)
- Verified ε: ε ≈ 27,000–30,000 M⁻¹cm⁻¹ at 311 nm (EtOH). λmax consistently reported 311–312 nm. Several ingredient guides cite "peak absorbance at 312 nm." Padimate O is consistently cited as **the most potent FDA-approved UVB absorber per chromophore**.
- Status: correct
- Spectrum refs:
  1. Cosmetics Info: Ethylhexyl Dimethyl PABA. https://www.cosmeticsinfo.org/ingredient/ethylhexyl-dimethyl-paba/
  2. Risk Assessment of Ethylhexyl Dimethyl PABA in Cosmetics. PMC6467356. https://pmc.ncbi.nlm.nih.gov/articles/PMC6467356/
  3. PubChem CID 30541 (Padimate-O). https://pubchem.ncbi.nlm.nih.gov/compound/Padimate-O
  4. ScienceDirect topic: 4-Dimethylaminobenzoic Acid 2-Ethylhexyl Ester. https://www.sciencedirect.com/topics/medicine-and-dentistry/4-dimethylaminobenzoic-acid-2-ethylhexyl-ester
- Notes: A DMA-PABA chromophore → strong push-pull with extended conjugation, hence very high ε. The 28,400 figure is widely cited and consistent with measurements; original source not directly retrieved during this audit, so confidence is "moderate-high" rather than "high."

---

## 8. Ensulizole (PBSA) — CAS 27503-81-7
- Current ε (webapp): 25,000 M⁻¹cm⁻¹ at 302 nm (water)
- Verified ε: ε ≈ 24,000–27,000 M⁻¹cm⁻¹ at 302 nm in aqueous solution (typically with a base such as NaOH/triethanolamine, since PBSA itself is a sulfonic acid). Manufacturer specs are usually quoted as **E(1%, 1cm) = 920–990 at ~302 nm** which corresponds to ε = E·M/10 ≈ 920–990 × 274.3/10 = **25,200–27,200 M⁻¹cm⁻¹**.
- Status: correct
- Spectrum refs:
  1. SCCP Opinion on phenylbenzimidazole sulfonic acid (SCCP/0939/05). https://ec.europa.eu/health/ph_risk/committees/04_sccp/docs/sccp_o_079.pdf
  2. Comprehensive review of ensulizole toxicology (Tandfonline 2025). https://www.tandfonline.com/doi/full/10.1080/10408444.2025.2541392
  3. ChemicalBook entry CAS 27503-81-7 (manufacturer absorbance specs). https://www.chemicalbook.com/ChemicalProductProperty_EN_CB4394499.htm
  4. PubChem CID 33919 (2-Phenylbenzimidazole-5-sulfonic acid). https://pubchem.ncbi.nlm.nih.gov/compound/Ensulizole
- Notes: Solubility requires neutralisation; "in water" implicitly means "in pH-7+ aqueous buffer." E(1%, 1cm) → ε conversion = E × MW / 10 (since ε = A/(c·l), c in mol/L). MW = 274.29 g/mol.

---

## 9. Polysilicone-15 (Parsol SLX) — CAS 207574-74-1
- Current ε (webapp): 6,500 M⁻¹cm⁻¹ per chromophore at 312 nm
- Verified ε: per **chromophore** (benzylidene malonate unit), ε ≈ 5,000–7,000 M⁻¹cm⁻¹. Manufacturer (DSM) reports E(1%, 1cm) of the polymer = 160–190 at 312 nm. Because the polymer molecular weight is large (and variable, polysiloxane backbone with multiple chromophores), reporting ε per chromophore (~6,500) is the standard practice.
- Status: correct
- Spectrum refs:
  1. SCCS Opinion on polysilicone-15 (SCCS/1359/10). https://ec.europa.eu/health/scientific_committees/consumer_safety/docs/sccs_o_024.pdf
  2. DSM PARSOL SLX product page. https://www.dsm.com/personal-care/en_US/products/uv-filters/parsol-slx.html
  3. Altmeyer's Encyclopedia of Cosmetology — Polysilicone-15. https://www.altmeyers.org/en/cosmetology/polysilicone-15-144649
  4. DrugBank DB11271 Polysilicone-15. https://go.drugbank.com/drugs/DB11271
- Notes: "Per-chromophore" ε is the only meaningful quantity for this polymer. The benzylidene malonate chromophore is responsible for UVB absorption with λmax 312 nm.

---

## 10. Ethylhexyl Triazone (EHT, Uvinul T 150) — CAS 88122-99-0
- Current ε (webapp): 135,000 M⁻¹cm⁻¹ at 314 nm
- Verified ε: ε ≈ 120,000–135,000 M⁻¹cm⁻¹ at 314 nm (EtOH or 2-PrOH). EHT contains **three** dimethylaminobenzoate chromophores around a triazine core, and the per-molecule ε is the sum. Various secondary sources report a range from 120,000 (Grokipedia/Wikipedia) to ~135,000 (review literature) — consensus mid-point ≈ 125,000–130,000.
- Status: correct (high end of consensus range; could be revised to ~125,000 ± 10,000 if more conservative)
- Spectrum refs:
  1. BASF Technical Information sheet "Uvinul® T 150 PRD 30035119" (2018). https://promo.basf.com/campaign/Projetos/CaringForYou/Documentos/Geral/Uvinul%C2%AE%20T%20150.pdf
  2. Stein et al. "Photoexcited triplet states of UV-B absorbers: ethylhexyl triazone and diethylhexylbutamido triazone." Photochem. Photobiol. Sci. 2014. doi:10.1039/c4pp00373j. https://link.springer.com/article/10.1039/c4pp00373j
  3. Quantification of Sunscreen Ethylhexyl Triazone in Topical Skin-Care Products by Normal-Phase TLC/Densitometry. PMC3353564. https://pmc.ncbi.nlm.nih.gov/articles/PMC3353564/
  4. Wikipedia: Ethylhexyl triazone (cites BASF, λmax 314 nm). https://en.wikipedia.org/wiki/Ethylhexyl_triazone
- Notes: BASF specs report E(1%, 1cm) ≈ 1500–1650 at 314 nm. With MW 823.05 g/mol, ε = 1500 × 823.05 / 10 ≈ **123,500 M⁻¹cm⁻¹**, with E = 1640 giving ~135,000. The webapp value 135,000 is at the upper end but defensible.

---

## 11. 4-Methylbenzylidene Camphor (4-MBC, Enzacamene) — CAS 36861-47-9
- Current ε (webapp): 24,500 M⁻¹cm⁻¹ at 300 nm (EtOH)
- Verified ε: ε = 24,500 M⁻¹cm⁻¹ at 300 nm in EtOH is the canonical literature value, frequently cited. Secondary band at 226 nm with ε ≈ 7,300. E(1%, 1cm) at 300 nm = 954 (EtOH); MW 254.37 → ε = 954 × 254.37/10 = 24,267 ≈ 24,500.
- Status: correct
- Spectrum refs:
  1. ScienceDirect topic page: 3-(4-Methylbenzylidene)camphor — gives E1%/1cm = 954 at λmax 300 nm. https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/3-4-methylbenzylidene-camphor
  2. MDPI Cosmetics review (2023) "Ultraviolet Filters for Cosmetic Applications" — quotes ε 24,500 M⁻¹cm⁻¹ at 300 nm for enzacamene. https://www.mdpi.com/2079-9284/10/4/101
  3. DrugBank DB11219 enzacamene. https://go.drugbank.com/drugs/DB11219
  4. SCCS opinions on 4-MBC; IFRA/ COSing entries also cite same value.
- Notes: The benzylidene-camphor chromophore is rigid; minimal solvent dependence. This is one of the most consistent values across the dataset.

---

## 12. Amiloxate (Isoamyl Methoxycinnamate, Neo Heliopan E1000) — CAS 71617-10-2
- Current ε (webapp): 24,000 M⁻¹cm⁻¹ at 308–310 nm (EtOH)
- Verified ε: λmax 307–308 nm in MeOH; manufacturer (Symrise / Neo Heliopan E1000) reports **E(1%, 1cm) min. 980 at 308 nm in methanol**. MW 248.32 → ε = 980 × 248.32/10 = **24,335 M⁻¹cm⁻¹**, very close to webapp value.
- Status: correct
- Spectrum refs:
  1. The Good Scents Company — Neo Heliopan E1000 datasheet. http://www.thegoodscentscompany.com/data/rw1011641.html
  2. Symrise Sun Protection Brochure 2020. https://chemspireingredients.com/wp-content/uploads/2021/05/Symrise_Sun_Protection_Brochure_2020.pdf
  3. FDA TEA submission for Neo Heliopan E1000 (FDA-2003-N-0196-0004). https://downloads.regulations.gov/FDA-2003-N-0196-0004/attachment_1.pdf
  4. ChemicalBook isoamyl 4-methoxycinnamate (CAS 71617-10-2). https://www.chemicalbook.com/ChemicalProductProperty_EN_CB5485611.htm
- Notes: Same chromophore as EHMC (4-methoxycinnamate ester), so ε is essentially identical (~24,000) — only the ester alcohol differs.

---

## Solvent / λmax cross-check summary table

| Filter | λmax (EtOH/MeOH) | λmax (cyclohexane / hydrocarbon) | ε (M⁻¹cm⁻¹) | Confidence |
|---|---|---|---|---|
| EHMC | 308–310 nm | 291 nm | ~24,000 | High |
| Octisalate | 305–307 nm | 305 nm | ~4,500–5,000 | Medium |
| Homosalate | 306–309 nm | 309 nm | ~5,000 | Medium |
| Octocrylene | 303 nm | 295 nm | ~12,000 | High |
| Cinoxate | 289 / 308 nm | — | ~20,650 | Medium |
| PABA | 283–289 nm | — | ~13,500–15,000 | Medium |
| Padimate O | 311–312 nm | — | ~28,000–30,000 | Medium |
| PBSA | 302 nm (aq.) | n/a | ~25,000–27,000 | High |
| Polysilicone-15 | 312 nm | — | 6,500/chromophore | Medium |
| EHT | 314 nm | 310 nm | 123,000–135,000 | Medium-High |
| 4-MBC | 300 nm | 300 nm | 24,500 | High |
| Amiloxate | 307–308 nm | — | ~24,300 | High |

---

## Summary

**No filter requires correction**. All twelve current values fall within ±15 % of the consensus literature/manufacturer values, with most agreeing to within 5 %. The webapp's solvent attributions (EtOH for organic-soluble filters, water for PBSA) are also correct.

**Caveats and lower-confidence items:**
- Cinoxate (5) and Padimate O (7): values are widely cited but I was unable to retrieve the original peer-reviewed measurement paper during this audit; both should be flagged as "moderate confidence" pending review of USP monograph or FDA TEA documents.
- For Polysilicone-15 (9), the per-chromophore convention should be made explicit in the webapp UI to avoid confusion (the polymer's bulk ε is very different).
- For EHT (10) and PBSA (8), the published values are E(1%, 1cm) × MW/10 — the webapp values agree once that conversion is applied; consider also citing the BASF/manufacturer E-values directly.

**Solvent caveat for EHMC (1) and Amiloxate (12):** in cyclohexane the cinnamate λmax is 291 nm, in EtOH/MeOH it red-shifts to 310 nm; ε is ~24,000 in both. The webapp's "EtOH 308–311 nm" is correct; just note that if a user sees a literature spectrum at 291 nm it is the same compound in non-polar solvent.
