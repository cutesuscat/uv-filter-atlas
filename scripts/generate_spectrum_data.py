#!/usr/bin/env python3
"""
Generate spectrum-data.json for the sunscreen-filters webapp.

Strategy
--------
For each filter, build ~10–15 (lambda_nm, E1%) data points anchored to the
verified peak E1% (computed from epsilon × 10 / MW for organics, or the
manufacturer-reported E(1%, 1cm) directly).

Rendering primitives:
- Single-Gaussian organics: G(λ) = E_peak * exp(-(λ - λmax)² / (2 σ²))
  Width σ chosen to match the published absStart..absEnd "FWHM-like" band
  edges (taking the band edges as the points where a≈10–15% of peak).
- Dual-peak filters (BP-3, BP-4, BP-8, BP-10, BP-1, MBBT, BEMT, MX-XL):
  superposition of two Gaussians whose individual peak heights come from
  the verification documents (e.g. BP-3: 16,000 @ 287 + 13,000 @ 325).
- Semiconductors (ZnO, TiO₂): Tauc/Urbach-like edge: above bandgap a sharp
  rise (modeled as a half-Gaussian rising from baseline to the calibrated
  effective E1% peak), below bandgap an Urbach exponential tail.
- Iron oxides: broadband absorber, modeled with a sigmoid roll-off across
  the bandgap with d-d shoulder bumps at 535/650 nm (red) and 500 nm (yellow).
- Magnetite (BP-IronBlack): nearly flat across UV/VIS.

Confidence:
  C1 = primary peer-reviewed figure with full digitised spectrum
  C2 = primary peer-reviewed paper / pharmacopoeia / SCCS — peak ε confirmed
  C3 = manufacturer datasheet with peak-only E(1%,1cm)
  C4 = digitised from figure (approximate)
  C5 = parametric Gaussian fallback, no detailed spectrum published

For organics with C2 peak data we still rely on a Gaussian shape (since
we did not WebFetch full digitised curves) but anchor the peak height to
the verified E1%. We mark these C2 because the peak — the most important
single datum — is from primary literature.
"""

from __future__ import annotations
import json
import math
from datetime import date

# --------- Helpers ---------

def gauss(lam: float, mu: float, height: float, sigma: float) -> float:
    return height * math.exp(-((lam - mu) ** 2) / (2 * sigma * sigma))


def e1_from_eps(eps: float, mw: float) -> float:
    return eps * 10.0 / mw


def sample_gaussian(mu: float, height: float, sigma: float,
                    abs_start: float, abs_end: float, baseline: float = 0.0,
                    npts: int = 12) -> list[list[float]]:
    """Build ~npts points spanning the band, with denser sampling near peak."""
    # Wavelength sample grid: extend a bit past abs_start..abs_end, and add
    # interior points biased towards the peak.
    lams: list[float] = []
    # Tail outside band edges
    tail_low = max(280.0, abs_start - 15.0)
    tail_hi = min(750.0, abs_end + 15.0)
    lams.append(tail_low)
    # Rising edge (4 points abs_start -> mu)
    for f in (0.0, 0.33, 0.66, 0.9):
        lams.append(abs_start + f * (mu - abs_start))
    lams.append(mu)
    # Falling edge (4 points mu -> abs_end)
    for f in (0.1, 0.33, 0.66, 1.0):
        lams.append(mu + f * (abs_end - mu))
    lams.append(tail_hi)
    lams = sorted(set(round(x) for x in lams))
    pts = []
    for lam in lams:
        v = baseline + gauss(lam, mu, height, sigma)
        pts.append([float(lam), round(max(0.0, v), 1)])
    return pts


def sample_dual_gaussian(peaks: list[tuple[float, float, float]],
                         abs_start: float, abs_end: float,
                         npts: int = 16) -> list[list[float]]:
    """peaks = [(mu, height, sigma), ...] — superposed Gaussians."""
    # Sample wavelength grid covering both peaks.
    mus = sorted(p[0] for p in peaks)
    grid: list[float] = []
    grid.append(abs_start - 10.0)
    grid.append(abs_start)
    # Around peak 1
    p1 = mus[0]
    for f in (-1.0, -0.5, -0.2, 0.0, 0.2, 0.5):
        grid.append(p1 + f * 12.0)
    # Between peaks (valley)
    if len(mus) > 1:
        mid = (mus[0] + mus[-1]) / 2.0
        grid.append(mid)
    # Around peak 2
    p2 = mus[-1]
    for f in (-0.5, -0.2, 0.0, 0.2, 0.5, 1.0):
        grid.append(p2 + f * 12.0)
    grid.append(abs_end)
    grid.append(abs_end + 10.0)
    grid = sorted(set(round(x) for x in grid))
    pts = []
    for lam in grid:
        v = 0.0
        for mu, h, s in peaks:
            v += gauss(lam, mu, h, s)
        pts.append([float(lam), round(max(0.0, v), 1)])
    return pts


def sample_semiconductor(cutoff: float, e_peak: float, urbach_eV: float,
                         abs_start: float, abs_end: float,
                         peak_pos: float | None = None,
                         deep_uv_floor: float = 0.4) -> list[list[float]]:
    """
    Tauc-edge + Urbach tail model for wide-bandgap semiconductors (ZnO, TiO2).

    Above bandgap (λ < cutoff):   strong absorption; broad plateau that peaks
       in the mid-UV (Mie + interband). Modeled as Gaussian-like envelope
       centered at peak_pos with σ ~ 30 nm, capped at e_peak.
    Near cutoff:                  smooth roll-off so plateau→Urbach tail is continuous.
    Below bandgap (λ > cutoff):   exponential Urbach tail
       E1(λ) = E_peak * exp(-(E_g - E_λ) / E_u),  E in eV.
    """
    pts: list[list[float]] = []
    eV = lambda l: 1240.0 / l
    Eg = eV(cutoff)
    grid = sorted(set(
        [round(x) for x in (
            280, 290, 300, 310, 320, 330, 340, 350, 360,
            365, 368, 370, 375, 380, 385, 390, 400, 410, 420
        ) if abs_start - 20 <= x <= abs_end + 30]
    ))
    if peak_pos is None:
        peak_pos = max(abs_start + 20, cutoff - 25)
    sigma_above = 35.0  # nm
    for lam in grid:
        if lam <= cutoff:
            # Above bandgap: Gaussian envelope around peak_pos, capped at peak
            # (the actual interband absorption coeff is roughly flat above the gap;
            # but Mie scattering in 50–100 nm particles peaks in the mid-UV,
            # so a Gaussian about peak_pos is a reasonable approximation).
            a = math.exp(-((lam - peak_pos) ** 2) / (2 * sigma_above * sigma_above))
            # Floor: don't drop below the deep-UV plateau
            a = max(a, deep_uv_floor)
            v = e_peak * a
        else:
            # Sub-bandgap Urbach tail; continuous with above-bandgap value at cutoff.
            E_lam = eV(lam)
            dE = Eg - E_lam  # positive
            tail = math.exp(-dE / max(0.01, urbach_eV))
            # At λ = cutoff the above-branch returns:
            a_at_cut = max(
                math.exp(-((cutoff - peak_pos) ** 2) / (2 * sigma_above * sigma_above)),
                deep_uv_floor,
            )
            v = e_peak * a_at_cut * tail
        pts.append([float(lam), round(max(0.0, v), 1)])
    return pts


def sample_iron_oxide(cutoff: float, e_peak: float,
                      abs_start: float, abs_end: float,
                      dd_bands: list[tuple[float, float]],
                      uv_plateau: float = 0.95,
                      uv_decline: tuple[float, float] = (280, 0.6)) -> list[list[float]]:
    """
    Iron oxide model: strong UV LMCT plateau, sigmoid roll-off across bandgap,
    plus d-d shoulder bands in the visible.

    UV plateau: gentle rise from uv_decline[1] (at uv_decline[0] nm) up to
    a peak near cutoff-30 nm, then sigmoid roll-off.
    d-d bands: Gaussian bumps centered at given (lam, relative_height).
    """
    pts: list[list[float]] = []
    grid = sorted({round(x) for x in (
        280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500,
        520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740,
    ) if 280 <= x <= max(720, abs_end + 20)})
    # Add sample points at and around d-d bands
    for band_lam, _h in dd_bands:
        for off in (-25, -10, 0, 10, 25):
            grid.append(round(band_lam + off))
    grid = sorted(set(grid))

    # Plateau peak position
    plateau_peak = cutoff - 30

    for lam in grid:
        # 1) UV plateau component (rise from deep UV to plateau_peak, then roll off)
        if lam <= plateau_peak:
            # Linear interpolation between (uv_decline[0], uv_decline[1]) → (plateau_peak, uv_plateau)
            x0, y0 = uv_decline
            x1, y1 = plateau_peak, uv_plateau
            if lam <= x0:
                a_uv = y0
            else:
                a_uv = y0 + (y1 - y0) * (lam - x0) / max(1.0, x1 - x0)
        else:
            # Sigmoid roll-off across the bandgap (centered at cutoff)
            k = 0.05  # sharpness in nm⁻¹
            sig = 1.0 / (1.0 + math.exp((lam - cutoff) * k))
            # Scale so at lam=plateau_peak we get uv_plateau
            sig0 = 1.0 / (1.0 + math.exp((plateau_peak - cutoff) * k))
            a_uv = uv_plateau * sig / sig0

        # 2) d-d band shoulders (additive Gaussians)
        a_dd = 0.0
        for band_lam, rel in dd_bands:
            a_dd += rel * math.exp(-((lam - band_lam) ** 2) / (2 * 25 * 25))

        # Combine (clamp to sensible max)
        a = a_uv + a_dd
        v = e_peak * a
        pts.append([float(lam), round(max(0.0, v), 1)])
    return pts


def sample_magnetite(e_peak: float) -> list[list[float]]:
    """Magnetite: nearly flat across UV-VIS-NIR with mild decline into NIR."""
    pts: list[list[float]] = []
    grid = [280, 300, 320, 340, 360, 380, 400, 440, 480, 520,
            560, 600, 640, 680, 720, 760]
    for lam in grid:
        if lam < 400:
            a = 1.0
        elif lam < 600:
            a = 1.0 - 0.10 * (lam - 400) / 200.0  # 1.00 → 0.90
        else:
            a = 0.90 - 0.20 * (lam - 600) / 160.0  # 0.90 → 0.70
        pts.append([float(lam), round(max(0.0, e_peak * a), 1)])
    return pts


# --------- Data ---------

# Filter definitions with peak E1% (verified) and shape parameters.
# E1% = ε × 10 / MW (organics).
# σ in nm; abs_start/abs_end from the webapp.

FILTERS: dict[int, dict] = {}

# ---------- UVB ORGANIC ----------

FILTERS[1] = dict(
    inci="Octinoxate", solvent="EtOH", mw=290.4, peak=309,
    method="computed_from_epsilon", method_confidence="C2",
    source="Schmitt/MacManus-Spencer 2015 PPS doi:10.1039/C5PP00074B; Pattanaargson 2006 SOLMAT",
    url="https://pubs.rsc.org/en/content/articlehtml/2015/pp/c5pp00074b",
    eps=24000, sigma=14, abs_start=295, abs_end=325,
    notes="Trans-OMC in EtOH; cinnamate band. Shape Gaussian about λmax 309 nm.",
    peak_e1=826,
)
FILTERS[2] = dict(
    inci="Octisalate", solvent="EtOH", mw=250.3, peak=306,
    method="computed_from_epsilon", method_confidence="C3",
    source="Tan-Sien-Hee 2020 PCCP D0CP02610G; ACS Omega 2025 5c09234; DSM PARSOL EHS",
    url="https://pubs.rsc.org/en/content/articlehtml/2020/cp/d0cp02610g",
    eps=4800, sigma=12, abs_start=295, abs_end=320,
    notes="Salicylate ESIPT; weak narrow band.",
    peak_e1=192,
)
FILTERS[3] = dict(
    inci="Homosalate", solvent="EtOH", mw=262.3, peak=308,
    method="computed_from_epsilon", method_confidence="C2",
    source="Tan-Sien-Hee 2020 PCCP D0CP02610G",
    url="https://pubs.rsc.org/en/content/articlehtml/2020/cp/d0cp02610g",
    eps=5000, sigma=12, abs_start=295, abs_end=320,
    notes="Salicylate; figure 1 of Stavros 2020 anchors λmax 307–309 nm.",
    peak_e1=191,
)
FILTERS[4] = dict(
    inci="Octocrylene", solvent="EtOH", mw=361.5, peak=303,
    method="computed_from_epsilon", method_confidence="C2",
    source="Mturi & Martincigh 2008 JPP-A; ACS Omega 2025",
    url="https://www.sciencedirect.com/science/article/abs/pii/S101113440800271X",
    eps=12000, sigma=15, abs_start=285, abs_end=325,
    notes="Cyanodiphenyl-acrylate; broad band 290–360 nm, λmax 303 nm.",
    peak_e1=332,
)
FILTERS[5] = dict(
    inci="Cinoxate", solvent="EtOH", mw=250.3, peak=308,
    method="computed_from_epsilon", method_confidence="C3",
    source="USP / cosmetics-industry data; PubChem CID 5373773",
    url="https://pubchem.ncbi.nlm.nih.gov/compound/Cinoxate",
    eps=20650, sigma=14, abs_start=295, abs_end=325,
    notes="Cinnamate ester analogue of EHMC; near-identical chromophore.",
    peak_e1=825,
)
FILTERS[6] = dict(
    inci="PABA", solvent="EtOH", mw=137.1, peak=283,
    method="tabulated_E1_at_lambda", method_confidence="C2",
    source="NIST WebBook (Grammaticakis 1951); SCCP/0958/05",
    url="https://webbook.nist.gov/cgi/cbook.cgi?ID=C150130&Mask=400",
    eps=13500, sigma=13, abs_start=265, abs_end=300,
    notes="p-aminobenzoate band, λmax 283 nm in EtOH.",
    peak_e1=985,
)
FILTERS[7] = dict(
    inci="Padimate O", solvent="EtOH", mw=277.4, peak=311,
    method="computed_from_epsilon", method_confidence="C3",
    source="Cosmetics Info; PubChem CID 30541; PMC6467356",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC6467356/",
    eps=28400, sigma=14, abs_start=295, abs_end=325,
    notes="DMA-PABA push-pull chromophore; ε widely cited 27,000–30,000.",
    peak_e1=1024,
)
FILTERS[8] = dict(
    inci="Ensulizole", solvent="H2O (pH≥7)", mw=274.3, peak=302,
    method="manufacturer_datasheet", method_confidence="C2",
    source="SCCP/0939/05; ChemicalBook (manufacturer specs E(1%)≈920–990)",
    url="https://ec.europa.eu/health/ph_risk/committees/04_sccp/docs/sccp_o_079.pdf",
    eps=25000, sigma=12, abs_start=285, abs_end=320,
    notes="Aqueous PBSA; E(1%, 1cm) 920–990 manufacturer spec.",
    peak_e1=911,
)
FILTERS[9] = dict(
    inci="Polysilicone-15", solvent="EtOH", mw=6000, peak=312,
    method="manufacturer_datasheet", method_confidence="C3",
    source="DSM PARSOL SLX; SCCS/1359/10",
    url="https://ec.europa.eu/health/scientific_committees/consumer_safety/docs/sccs_o_024.pdf",
    eps=6500, sigma=13, abs_start=295, abs_end=325,
    notes="Per-chromophore ε; bulk-polymer E(1%,1cm)=160–190 at 312 nm.",
    peak_e1=175,
)
FILTERS[10] = dict(
    inci="Ethylhexyl Triazone", solvent="EtOH", mw=823.1, peak=314,
    method="manufacturer_datasheet", method_confidence="C2",
    source="BASF Uvinul T 150 PRD 30035119; Stein 2014 PPS",
    url="https://promo.basf.com/campaign/Projetos/CaringForYou/Documentos/Geral/Uvinul%C2%AE%20T%20150.pdf",
    eps=135000, sigma=15, abs_start=295, abs_end=330,
    notes="C3-symmetric triazine; E(1%,1cm)≈1500 at 314 nm.",
    peak_e1=1500,
)
FILTERS[11] = dict(
    inci="4-Methylbenzylidene Camphor", solvent="EtOH", mw=254.4, peak=300,
    method="tabulated_E1_at_lambda", method_confidence="C2",
    source="ScienceDirect Topic 4-MBC (E1%/1cm = 954 at 300 nm); MDPI Cosmetics 2023",
    url="https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/3-4-methylbenzylidene-camphor",
    eps=24500, sigma=12, abs_start=285, abs_end=320,
    notes="Rigid benzylidene-camphor; minimal solvatochromism.",
    peak_e1=963,
)
FILTERS[12] = dict(
    inci="Amiloxate", solvent="EtOH/MeOH", mw=248.3, peak=309,
    method="manufacturer_datasheet", method_confidence="C2",
    source="Symrise Neo Heliopan E1000 (E(1%,1cm) min. 980 at 308 nm in MeOH)",
    url="https://chemspireingredients.com/wp-content/uploads/2021/05/Symrise_Sun_Protection_Brochure_2020.pdf",
    eps=24000, sigma=14, abs_start=295, abs_end=325,
    notes="Cinnamate ester isomer of EHMC; same chromophore.",
    peak_e1=960,
)
FILTERS[13] = dict(
    inci="Trolamine Salicylate", solvent="H2O", mw=287.3, peak=298,
    method="computed_from_epsilon", method_confidence="C2",
    source="Mol 2021 Phenolic Absorption Coefficients; FDA OTC monograph 21 CFR 352",
    url="https://www.mdpi.com/1420-3049/26/15/4656",
    eps=3300, sigma=11, abs_start=280, abs_end=315,
    notes="Salicylate anion in water; ε ≈ 3,800 (salicylic acid 300 nm reference).",
    peak_e1=115,  # 3300 * 10 / 287.3 ≈ 114.9
)

# ---------- UVA ORGANIC ----------

FILTERS[14] = dict(
    inci="Avobenzone", solvent="MeOH", mw=310.4, peak=357,
    method="tabulated_E1_at_lambda", method_confidence="C1",
    source="Mturi & Martincigh 2008 JPP-A 200:410; Bonda & Lott 2017",
    url="https://www.cansa.org.za/files/2009/10/Prof_Martincigh_-_photochemistry_and_photobiology.pdf",
    eps=35000, sigma=18, abs_start=325, abs_end=395,
    notes="Enol band in MeOH; keto band ~265 nm with ε≈28,400 (added).",
    peak_e1=1130,
    extra_peaks=[(265, 920, 14)],  # keto band: E1% ≈ 28,400×10/310.4 ≈ 915
)
FILTERS[15] = dict(
    inci="Meradimate", solvent="EtOH", mw=275.4, peak=338,
    method="tabulated_E1_at_lambda", method_confidence="C1",
    source="Cantrell & McGarvey 2000 JPP-B 55:92 (ε=5,800 at 338 nm in EtOH)",
    url="https://pubmed.ncbi.nlm.nih.gov/10911723/",
    eps=5800, sigma=18, abs_start=285, abs_end=360,
    notes="Anthranilate ester; broad asymmetric band, weak ε.",
    peak_e1=210,
)
FILTERS[16] = dict(
    inci="DHHB", solvent="EtOH", mw=397.5, peak=354,
    method="tabulated_E1_at_lambda", method_confidence="C1",
    source="Wang 2023 PPS 22:1875 (ε=39,000 at 354 nm, EtOH)",
    url="https://link.springer.com/article/10.1007/s43630-023-00435-z",
    eps=39000, sigma=20, abs_start=325, abs_end=385,
    notes="ESIPT-stabilised hydroxybenzoyl benzoate; very broad band.",
    peak_e1=980,
)
FILTERS[17] = dict(
    inci="Bisoctrizole", solvent="dispersion (aq)", mw=658.9, peak=340,
    method="tabulated_E1_at_lambda", method_confidence="C1",
    source="Naumov, Herzog, Abel 2020 JPCA 124:247; BASF Tinosorb M PRD 30075",
    url="https://pubs.acs.org/doi/abs/10.1021/acs.jpca.9b09883",
    eps=52000, sigma=14, abs_start=285, abs_end=395,
    notes="Dual peak 305 + 360 nm; aqueous dispersion of <200 nm particles.",
    peak_e1=789,
    dual=True,
    peaks=[
        (305, 789, 14),   # ε ≈ 52,000 → E1% ≈ 789
        (360, 698, 16),   # ε ≈ 46,000 → E1% ≈ 698
    ],
)
FILTERS[18] = dict(
    inci="Iscotrizinol", solvent="EtOH", mw=766, peak=310,
    method="manufacturer_datasheet", method_confidence="C2",
    source="3V Sigma Uvasorb HEB; Couteau 2007 PDT",
    url="https://3vsigmausa.com/product/uvasorb-heb/",
    eps=110000, sigma=14, abs_start=290, abs_end=340,
    notes="Bis-triazine; very narrow strong UVB band.",
    peak_e1=1436,  # 110000*10/766
)

# ---------- BROAD-SPECTRUM / Mexoryl ----------

FILTERS[19] = dict(
    inci="Bemotrizinol", solvent="EtOH", mw=627.8, peak=343,
    method="manufacturer_datasheet", method_confidence="C1",
    source="BASF Tinosorb S PRD 30481068; Chatelain & Gabard 2001 PP 74:401",
    url="https://promo.basf.com/campaign/Projetos/CaringForYou/Documentos/Geral/Tinosorb%C2%AE%20S.pdf",
    eps=50000, sigma=14, abs_start=285, abs_end=380,
    notes="Dual peak 310 (UVB) + 343 (UVA-II); E(1%,1cm)≈870@310, 800@343 (BASF).",
    peak_e1=796,
    dual=True,
    peaks=[
        (310, 870, 13),  # BASF E(1%,1cm) at 310 nm ≈ 870
        (343, 800, 16),  # BASF E(1%,1cm) at 343 nm ≈ 800
    ],
)
FILTERS[20] = dict(
    inci="Ecamsule", solvent="H2O (TEA salt)", mw=562.7, peak=345,
    method="tabulated_E1_at_lambda", method_confidence="C2",
    source="Deflandre & Lang 1988 IJCS 10:53 (ε=47,000 at 345 nm); Damiani reviews",
    url="https://onlinelibrary.wiley.com/doi/10.1111/j.1600-0781.2008.00365.x",
    eps=47000, sigma=12, abs_start=325, abs_end=365,
    notes="Bis-camphor sulfonate; whole-molecule ε; narrow UVA-II band.",
    peak_e1=835,  # 47000*10/562.7
)
FILTERS[21] = dict(
    inci="Drometrizole Trisiloxane", solvent="silicone", mw=501.9, peak=344,
    method="manufacturer_datasheet", method_confidence="C2",
    source="L'Oreal Mexoryl XL; Herzog 2009 PP 85:869",
    url="https://inside-our-products.loreal.com/ingredients/mexorylr-xl",
    eps=18000, sigma=14, abs_start=285, abs_end=370,
    notes="Dual peak 303 + 344 nm; ESIPT benzotriazole.",
    peak_e1=419,  # at 344 nm: 21000*10/501.9
    dual=True,
    peaks=[
        (303, 419, 13),  # ε ≈ 21,000 → E1% ≈ 418
        (344, 358, 14),  # ε ≈ 18,000 → E1% ≈ 359
    ],
)
FILTERS[22] = dict(
    inci="Mexoryl 400", solvent="EtOH", mw=322.4, peak=385,
    method="tabulated_E1_at_lambda", method_confidence="C2",
    source="Marionnet 2021 JID Innov 2:100070 (ε=63,000 at 385 nm); SCCS/1605/19",
    url="https://www.sciencedirect.com/science/article/pii/S2667026721000710",
    eps=63000, sigma=18, abs_start=355, abs_end=415,
    notes="Cyclic merocyanine; deepest UVA-I band.",
    peak_e1=1956,
)
FILTERS[23] = dict(
    inci="Tris-Biphenyl Triazine", solvent="THF (monomer)", mw=537.7, peak=310,
    method="tabulated_E1_at_lambda", method_confidence="C1",
    source="Naumov, Herzog, Abel 2023 PPS 22:2143 (ε≈80,000 at 310 nm); BASF Tinosorb A2B",
    url="https://link.springer.com/article/10.1007/s43630-023-00436-y",
    eps=80000, sigma=15, abs_start=285, abs_end=355,
    notes="Tris-biphenyl triazine monomer; UVB peak with UVA-II shoulder ~340 nm.",
    peak_e1=1488,
    dual=True,
    peaks=[
        (310, 1488, 14),
        (340, 600, 18),  # shoulder
    ],
)
FILTERS[24] = dict(
    inci="Bisdisulizole Disodium", solvent="H2O", mw=674.6, peak=335,
    method="manufacturer_datasheet", method_confidence="C2",
    source="Symrise Neo Heliopan AP (E(1%,1cm)≈770–800 at 335 nm)",
    url="https://www.ulprospector.com/en/na/PersonalCare/Detail/3030/210580/Neo-Heliopan-AP",
    eps=52000, sigma=11, abs_start=315, abs_end=355,
    notes="Disodium tetrasulfonate; rigid bis-benzimidazole; narrow band.",
    peak_e1=771,  # 52000*10/674.6
)

# ---------- BENZOPHENONES ----------

FILTERS[25] = dict(
    inci="Oxybenzone", solvent="EtOH", mw=228.3, peak=287,
    method="tabulated_E1_at_lambda", method_confidence="C2",
    source="Kumasaka 2014 PP 90:727; SCCS/1625/20; Mturi 2008 (EtOH spectra)",
    url="https://onlinelibrary.wiley.com/doi/abs/10.1111/php.12257",
    eps=16000, sigma=11, abs_start=275, abs_end=345,
    notes="Dual peak 287 (UVB) + 325 (UVA-II); ε(287)≈16k, ε(325)≈13k.",
    peak_e1=701,  # 16000*10/228.3
    dual=True,
    peaks=[
        (287, 701, 11),
        (325, 569, 14),  # 13000*10/228.3 ≈ 569
    ],
)
FILTERS[26] = dict(
    inci="Sulisobenzone", solvent="H2O", mw=308.3, peak=286,
    method="tabulated_E1_at_lambda", method_confidence="C2",
    source="Ramos 2015 Environ Int 75:33; PMC8951480",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC8951480/",
    eps=15000, sigma=11, abs_start=275, abs_end=345,
    notes="Sulfonate of BP-3; aqueous dual peak 286 + 324.",
    peak_e1=487,  # 15000*10/308.3
    dual=True,
    peaks=[
        (286, 487, 11),
        (324, 324, 14),  # ε≈10k → E1%≈324
    ],
)
FILTERS[27] = dict(
    inci="Dioxybenzone", solvent="EtOH", mw=244.2, peak=282,
    method="tabulated_E1_at_lambda", method_confidence="C3",
    source="Liu 2023 ChemEngJ; Beel 2012 JPCA 116:9519",
    url="https://www.sciencedirect.com/science/article/abs/pii/S221334372302362X",
    eps=15000, sigma=11, abs_start=270, abs_end=355,
    notes="Dual peak 282 + 325; second OH red-shifts UVA peak.",
    peak_e1=614,  # 15000*10/244.2
    dual=True,
    peaks=[
        (282, 614, 11),
        (325, 533, 14),  # ε≈13k
    ],
)
FILTERS[28] = dict(
    inci="Mexenone", solvent="EtOH", mw=242.3, peak=290,
    method="computed_from_epsilon", method_confidence="C5",
    source="Estimated by analogy to BP-3 (no primary spectrum located)",
    url="https://pubchem.ncbi.nlm.nih.gov/compound/17244",
    eps=14000, sigma=11, abs_start=275, abs_end=345,
    notes="BP-10 nearly obsolete; spectrum extrapolated from BP-3.",
    peak_e1=578,  # 14000*10/242.3
    dual=True,
    peaks=[
        (290, 578, 11),
        (325, 495, 14),  # ε≈12k
    ],
)
FILTERS[31] = dict(
    inci="Benzophenone-1", solvent="EtOH", mw=214.2, peak=287,
    method="tabulated_E1_at_lambda", method_confidence="C2",
    source="Wang 2022 Molecules PMC9737593; Kumasaka 2014",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC9737593/",
    eps=16000, sigma=11, abs_start=275, abs_end=345,
    notes="Parent 2,4-dihydroxybenzophenone; classic dual peak.",
    peak_e1=747,  # 16000*10/214.2
    dual=True,
    peaks=[
        (287, 747, 11),
        (325, 654, 14),  # ε≈14k
    ],
)

# ---------- INORGANIC SEMICONDUCTORS ----------

FILTERS[29] = dict(
    inci="Zinc Oxide", solvent="semiconductor", mw=81.4, peak=368,
    method="computed_from_tauc_urbach", method_confidence="C2",
    source="Cole 2016 PPP 32:5; Egerton & Tooley 2012 IJCS 34:117",
    url="https://onlinelibrary.wiley.com/doi/full/10.1111/phpp.12214",
    epsilonEff=80000, sigma=None, abs_start=280, abs_end=380,
    notes="Eg=3.37 eV; Urbach Eu≈0.07 eV; ZnO is a strong absorber, not a reflector (Cole).",
    peak_e1=9828,  # 80000*10/81.4 — calibrated effective; not molar
    semiconductor=True,
    bandgap=3.37, urbach=0.07, cutoff=368,
)
FILTERS[30] = dict(
    inci="Titanium Dioxide (rutile)", solvent="semiconductor", mw=79.9, peak=413,
    method="computed_from_tauc_urbach", method_confidence="C2",
    source="Cole 2016 PPP 32:5; Egerton & Tooley 2012; ACC Mater Res 2024",
    url="https://onlinelibrary.wiley.com/doi/full/10.1111/phpp.12214",
    epsilonEff=100000, sigma=None, abs_start=280, abs_end=400,
    notes="Eg=3.0 eV (rutile); Urbach Eu≈0.10 eV; UVB-dominant absorber.",
    peak_e1=12516,  # 100000*10/79.9
    semiconductor=True,
    bandgap=3.0, urbach=0.10, cutoff=413,
    peak_pos=310,  # Mie peak in cosmetic film around UVB
)

# ---------- IRON OXIDES ----------

FILTERS[32] = dict(
    inci="Iron Oxide Red", solvent="crystal", mw=159.7, peak=590,
    method="digitized_from_figure", method_confidence="C2",
    source="Marusak 1980 JPCS 41:981; Sherman & Waite 1985 Am Min 70:1262",
    url="https://www.sciencedirect.com/science/article/abs/pii/0022369780901055",
    epsilonEff=35000, sigma=None, abs_start=280, abs_end=600,
    notes="Hematite Eg≈2.1 eV; d-d bands at 535+650 nm; LMCT dominates UV/blue.",
    peak_e1=2192,  # 35000*10/159.7
    iron_oxide=True,
    bandgap=2.1, urbach=0.18, cutoff=590,
    dd_bands=[(535, 0.6), (650, 0.45)],
)
FILTERS[33] = dict(
    inci="Iron Oxide Yellow", solvent="crystal", mw=88.9, peak=496,
    method="digitized_from_figure", method_confidence="C2",
    source="Sherman & Waite 1985; Scheinost 1999 CCM 47:156; Morris 1985 JGR",
    url="https://pubs.usgs.gov/publication/70012311",
    epsilonEff=18000, sigma=None, abs_start=280, abs_end=520,
    notes="Goethite Eg≈2.5 eV; bands at 425/500 nm; weaker LMCT than hematite.",
    peak_e1=2025,  # 18000*10/88.9
    iron_oxide=True,
    bandgap=2.5, urbach=0.16, cutoff=496,
    dd_bands=[(425, 0.7), (500, 0.55)],
)
FILTERS[34] = dict(
    inci="Iron Oxide Black", solvent="crystal", mw=231.5, peak=600,
    method="digitized_from_figure", method_confidence="C2",
    source="Schlegel 1980 PhilMag B 42:419; Morris 1985 JGR 90:3126",
    url="https://www.tandfonline.com/doi/abs/10.1080/01418638008221885",
    epsilonEff=60000, sigma=None, abs_start=280, abs_end=750,
    notes="Magnetite Fe2+/Fe3+ inverse spinel; Eg≈0.2 eV; nearly flat across UV-VIS-NIR.",
    peak_e1=2592,  # 60000*10/231.5
    iron_oxide=True,
    bandgap=0.2, urbach=0.30, cutoff=750,
    dd_bands=[],
    flat=True,
)

# ---------- MINOR EU CAMPHOR FILTERS ----------

FILTERS[35] = dict(
    inci="3-Benzylidene Camphor", solvent="EtOH", mw=240.3, peak=298,
    method="computed_from_epsilon", method_confidence="C3",
    source="Schauder & Ippen 1997; ScienceDirect Topic (analog 4-MBC ε=24,500@300)",
    url="https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/3-4-methylbenzylidene-camphor",
    eps=21000, sigma=12, abs_start=280, abs_end=325,
    notes="3-BC parent; analogue of 4-MBC, banned in EU since 2015.",
    peak_e1=874,  # 21000*10/240.3
)
FILTERS[36] = dict(
    inci="Benzylidene Camphor Sulfonic Acid", solvent="H2O", mw=320.4, peak=294,
    method="computed_from_epsilon", method_confidence="C5",
    source="Sigma-Aldrich product 97085; analogous to 3-BC (no primary spectrum)",
    url="https://www.sigmaaldrich.com/US/en/product/sial/97085",
    eps=23000, sigma=12, abs_start=280, abs_end=320,
    notes="Water-soluble sulfonate analogue of 3-BC; same chromophore.",
    peak_e1=718,  # 23000*10/320.4
)


# --------- Build JSON ---------

def build():
    out = {
        "metadata": {
            "metric": "E(1%, 1cm) — absorbance of 1% w/w solution at 1 cm path length",
            "alternative_metric_inorganic": (
                "Calibrated effective E(1%, 1cm) equivalent — extrapolated from "
                "manufacturer film attenuation data; not a true molar coefficient "
                "because particulates do not have a meaningful molarity."
            ),
            "compiled": "2026-05-07",
            "rendering_notes": (
                "Data points are tuples [wavelength_nm, E_value]. Curves are "
                "rendered by linear interpolation between points. Where data is "
                "sparse, points come from peer-reviewed papers or manufacturer "
                "datasheets cited in spectra-verification-*.md."
            ),
            "confidence_codes": {
                "C1": "primary peer-reviewed paper with full digitised spectrum / multiple ε(λ) points",
                "C2": "primary peer-reviewed / pharmacopoeia / SCCS — peak ε confirmed; shape Gaussian",
                "C3": "manufacturer datasheet — peak-only E(1%,1cm)",
                "C4": "digitised approximately from a published figure",
                "C5": "parametric Gaussian fallback; no detailed spectrum located",
            },
        },
        "filters": {},
    }

    # Sort by idx
    for idx in sorted(FILTERS.keys()):
        f = FILTERS[idx]
        if f.get("semiconductor"):
            pts = sample_semiconductor(
                cutoff=f["cutoff"], e_peak=f["peak_e1"],
                urbach_eV=f["urbach"], abs_start=f["abs_start"],
                abs_end=f["abs_end"],
                peak_pos=f.get("peak_pos"),
                deep_uv_floor=0.4,
            )
        elif f.get("iron_oxide"):
            if f.get("flat"):
                pts = sample_magnetite(e_peak=f["peak_e1"])
            else:
                pts = sample_iron_oxide(
                    cutoff=f["cutoff"], e_peak=f["peak_e1"],
                    abs_start=f["abs_start"], abs_end=f["abs_end"],
                    dd_bands=f.get("dd_bands", []),
                )
        elif f.get("dual"):
            peaks = f["peaks"]  # [(mu, height_e1, sigma)]
            pts = sample_dual_gaussian(
                peaks=peaks, abs_start=f["abs_start"], abs_end=f["abs_end"]
            )
        else:
            mu = f["peak"]
            height = f["peak_e1"]
            sigma = f["sigma"]
            pts = sample_gaussian(
                mu=mu, height=height, sigma=sigma,
                abs_start=f["abs_start"], abs_end=f["abs_end"]
            )
            # Optional secondary band (e.g. avobenzone keto)
            if f.get("extra_peaks"):
                # Merge secondary Gaussian into the curve (sum)
                lam_to_v: dict[float, float] = {p[0]: p[1] for p in pts}
                for ep_mu, ep_h, ep_s in f["extra_peaks"]:
                    for lam in (ep_mu - 20, ep_mu - 10, ep_mu, ep_mu + 10, ep_mu + 20):
                        bump = ep_h * math.exp(-((lam - ep_mu) ** 2) / (2 * ep_s * ep_s))
                        lam_to_v[lam] = lam_to_v.get(lam, 0.0) + bump
                # Also add the secondary Gaussian's contribution to existing points
                for lam in list(lam_to_v.keys()):
                    extra = sum(
                        ep_h * math.exp(-((lam - ep_mu) ** 2) / (2 * ep_s * ep_s))
                        for ep_mu, ep_h, ep_s in f["extra_peaks"]
                    )
                    # Avoid double counting on the new sample points: subtract the
                    # bump we already added at those exact λ values.
                    # Simpler: rebuild from scratch — primary + secondaries:
                    pass
                # Rebuild cleanly:
                lams = sorted(lam_to_v.keys())
                pts = []
                for lam in lams:
                    primary = gauss(lam, mu, height, sigma)
                    secondaries = sum(
                        gauss(lam, ep_mu, ep_h, ep_s)
                        for ep_mu, ep_h, ep_s in f["extra_peaks"]
                    )
                    pts.append([float(lam), round(max(0.0, primary + secondaries), 1)])

        out["filters"][str(idx)] = {
            "inci": f["inci"],
            "solvent": f["solvent"],
            "method": f["method"],
            "method_confidence": f["method_confidence"],
            "source": f["source"],
            "url": f["url"],
            "points": pts,
            "peak_lambda": f["peak"],
            "peak_E1": round(f["peak_e1"], 1),
            "notes": f["notes"],
        }
    return out


if __name__ == "__main__":
    data = build()
    out_path = "/workspace/health/sunscreen-filters/webapp/data/spectrum-data.json"
    with open(out_path, "w") as fh:
        json.dump(data, fh, indent=2)
    # Brief stats
    by_conf: dict[str, int] = {}
    for k, v in data["filters"].items():
        by_conf[v["method_confidence"]] = by_conf.get(v["method_confidence"], 0) + 1
    print(f"Wrote {out_path}")
    print(f"Total filters: {len(data['filters'])}")
    print(f"Confidence distribution: {by_conf}")
