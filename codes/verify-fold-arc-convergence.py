"""
Companion checks for derivation record 079 (fold-arc convergence of the (h, m)
sector expansion of the fixed-halves gluing p^circ of record 074 / R80).

Model (record 079 Sec. 1, A1-A3): two V_3' halves (R2), ordinary punctures at
w = +-2 beta in the special-leg coordinate, glued by w1 w2 = q, local coordinates
transported from the halves (074 A5). Four tachyons c cbar e^{i k X}: a, b on copy 1
at w1 = +2 beta, -2 beta; c, d on copy 2 at w2 = +2 beta, -2 beta, i.e. at
w1 = +-q / (2 beta). With y = q / (4 beta^2) the integrand of 074 (1.3) per
ds dtheta is

    I(q) = N |y|^{h0} |1 - y|^{2 a_-} |1 + y|^{2 a_+},                   (079 (1.4))
    h0   = alpha' (k_c + k_d)^2 / 2 - 2,
    a_-  = 1 + alpha' (k_a.k_c + k_b.k_d) / 2,
    a_+  = 1 + alpha' (k_a.k_d + k_b.k_c) / 2,

so that with f(y) = (1 - y)^{a_-} (1 + y)^{a_+} = sum_N g_N y^N the sector
coefficients are c_{h,m} (4 beta^2)^h = N g_N g_Nbar, h = h0 + N + Nbar,
m = N - Nbar (079 (1.6)).

What is verified:

- C1.1-onshell: (079 (1.4)) agrees, for on-shell tachyons, with the
  Virasoro-Shapiro integrand computed in an independent Moebius frame
  (three punctures sent to infinity, 0, 1) times the Jacobian |dZ/dq|^2 |q|^2:
  the ratio is constant over seeded random q in the disc. Break leg: dropping
  the ghost factor |1 - y^2|^2 makes the ratio non-constant.
- C1.1-ghost: the holomorphic ghost factor <c c b_0 c c> computed by residues
  of <b(w) c c c c> = prod z_ij / prod (w - z_i) agrees with x (a^2 - x^2).
- C1.3-darboux-m: at fixed m the exact |g_N g_{N-m}| follows the Darboux
  asymptotic (three-term transfer from the singularities y = +-1) with relative
  error decreasing like 1/N, and the log-log slope is -2 alpha - 2,
  alpha = min(a_-, a_+). Break leg: the slope -alpha - 1 is rejected.
- C1.3-darboux-theta: at fixed theta on a fold arc the level-n term
  T_n(theta) = sum_{N + Nbar = n} g_N g_Nbar e^{i (N - Nbar) theta} has RMS
  envelope slope -alpha - 1; at theta = pi/2 the slope is -(a_- + a_+) - 1
  (coalescence of y = 1 and ybar = -1 singularities). Break leg: the generic
  slope is rejected at pi/2.
- C2.1-profile, C3.1-table: sigma_V(theta) by per-ray bisection (geometry of
  074, functions copied, that script not edited) is monotone on [0, th1] with
  rho = ln 4 b^2 - sigma_V ~ sqrt3 (th1 - th)^{1/2} at the arc ends; the table
  F_m(h) = int e^{i m th} e^{-rho h} matches a uniform grid and reproduces the
  real zero of fhat_4 at -2.36 (074 C2.4).
- C2.2-absolute: alpha > -1: level-ordered partial sums reach the direct
  quadrature J of the region integral to 1e-8; sector and absolute series
  converge with increments ~ H^{-2 alpha - 2}.
- C2.2-sector-divergence: alpha <= -1: fixed-m sector partial sums grow as
  H^{-2 alpha - 2}; break leg: stationary for alpha > -1.
- C2.3-level-order: level-order error envelope ~ H^{max(-alpha-3, h0-3)},
  tested to 0.1 where one term dominates: arc endpoints (C, conditional), arc
  midpoint (E, conditional), divergence for alpha < -3 (D, break leg); the
  subdominant exponent is rejected at each. At B the two terms compete
  (-1.30, -1.60) and only convergence is tested, not the exponent law.
- C2.3-h0-threshold: divergent side of h0 < 3 at F = (h0, a_-, a_+) =
  (3.5, -1.75, -1.75), alpha > -3: the error envelope grows as H^{h0-3}.
- C2.4-abel: sum_n L_n r^n = r^{-h0} int_{Q_V} I(r y) exactly (pipeline test
  independent of convergence) and the Abel limit is J; break leg: a wrong
  m = 0 transform violates it.
- C2.5-rays: ray theta = pi converges geometrically (error < 1e-12 at H = 40);
  fold-arc ray theta = 80 deg has error envelope ~ H^{-alpha-2} (break leg:
  not exponential; divergent for alpha < -2).
- C4.1-onshell-map: (sympy) on-shell a_- = -3 - a't/2, a_+ = -3 - a'u/2,
  h0 = -a's/2 - 2, and a_- + a_+ + h0 = 0 by conservation; break leg: fails
  without conservation.

Domain: h0 + n != 0 for every even n (h0 a non-positive even integer makes the
m != 0 terms 0/0 in the level pipeline; a ValueError is raised). None of the
test points is there.

What is not verified: the identification of the Schiffer antighosts with
b_0^+-, 074 (1.2) (cited); the normalisation N (cancels in every claim);
excited (non-tachyon) external states, for which only the integer shift of the
exponents is argued in the record.

Run from the project root:
    .venv/bin/python codes/verify-fold-arc-convergence.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import numpy as np

SEED = 20261004
rng = np.random.default_rng(SEED)
print(f"seed {SEED}")

SCRATCH = Path(__file__).resolve().parent / "output" / "fold-arc-convergence"
SCRATCH.mkdir(parents=True, exist_ok=True)
LOG = open(SCRATCH / "partial-results.txt", "w")  # noqa: SIM115

RESULTS: list[tuple[str, bool]] = []


def report(name: str, ok: bool, info: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, ok))
    line = f"{'PASS' if ok else 'FAIL'}  {name}  {info}"
    print(line, flush=True)
    LOG.write(line + "\n")
    LOG.flush()


BETA = 1.5
B2 = BETA**2
FOUR_B2 = 4 * B2


# ---------------------------------------------------------------------------
# Integrand and coefficients
# ---------------------------------------------------------------------------
def integrand(q: np.ndarray, h0: float, am: float, ap: float) -> np.ndarray:
    """Fixed-halves tachyon integrand per ds dtheta, normalisation N = 1 (079 (1.4))."""
    y = q / FOUR_B2
    return np.abs(y) ** h0 * np.abs(1 - y) ** (2 * am) * np.abs(1 + y) ** (2 * ap)


def g_coeffs(am: float, ap: float, nmax: int, dps: int = 40) -> np.ndarray:
    """
    Taylor coefficients of f(y) = (1 - y)^am (1 + y)^ap to order nmax.

    Recurrence from (1 - y^2) f' = ((ap - am) - (ap + am) y) f:
    (N + 1) g_{N+1} = (ap - am) g_N + (N - 1 - ap - am) g_{N-1}.

    Args:
        am: exponent at y = 1.
        ap: exponent at y = -1.
        nmax: highest order.
        dps: mpmath working precision.

    Returns:
        np.ndarray: g_0 .. g_nmax as float64.

    """
    mp.mp.dps = dps
    a_m, a_p = mp.mpf(am), mp.mpf(ap)
    g = [mp.mpf(1), a_p - a_m]
    for n in range(1, nmax):
        g.append(((a_p - a_m) * g[n] + (n - 1 - a_p - a_m) * g[n - 1]) / (n + 1))
    return np.array([float(x) for x in g[: nmax + 1]])


def g_by_convolution(am: float, ap: float, nmax: int) -> np.ndarray:
    """Independent route: Cauchy product of the two binomial series in float64."""
    n = np.arange(nmax + 1)
    bm = np.ones(nmax + 1)
    bp = np.ones(nmax + 1)
    for k in range(1, nmax + 1):
        bm[k] = bm[k - 1] * (k - 1 - am) / k  # (1 - y)^am
        bp[k] = bp[k - 1] * (ap - k + 1) / k  # (1 + y)^ap
    return np.array([np.dot(bm[: k + 1], bp[k::-1]) for k in n])


def darboux_g(am: float, ap: float, n: np.ndarray) -> np.ndarray:
    """Leading Darboux asymptotic of g_N from the singularities y = 1 and y = -1."""
    out = np.zeros_like(n, dtype=float)
    if not float(am).is_integer() or am < 0:
        out += (
            2.0**ap
            * np.exp(
                np.array([float(mp.loggamma(k - am) - mp.loggamma(k + 1)) for k in n])
            )
            / float(mp.gamma(-am))
        )
    if not float(ap).is_integer() or ap < 0:
        out += (
            (-1.0) ** n
            * 2.0**am
            * np.exp(
                np.array([float(mp.loggamma(k - ap) - mp.loggamma(k + 1)) for k in n])
            )
            / float(mp.gamma(-ap))
        )
    return out


def level_terms(g: np.ndarray, theta: float, nmax: int) -> np.ndarray:
    """T_n(theta) = sum_{N+Nbar=n} g_N g_Nbar e^{i(N-Nbar)theta}, real for real g."""
    t = np.zeros(nmax + 1)
    for n in range(nmax + 1):
        nn = np.arange(n + 1)
        t[n] = np.dot(g[nn] * g[n - nn], np.cos((2 * nn - n) * theta))
    return t


def slope(x: np.ndarray, y: np.ndarray) -> float:
    """Least-squares slope of log y against log x."""
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


def rms_envelope(t: np.ndarray, centres: list[int], half: int) -> np.ndarray:
    """RMS of t over windows [c - half, c + half] (even n only)."""
    out = []
    for c in centres:
        idx = np.arange(c - half, c + half + 1)
        idx = idx[idx % 2 == 0]
        out.append(np.sqrt(np.mean(t[idx] ** 2)))
    return np.array(out)


# Momentum points: (label, h0, a_-, a_+). "onshell" is four on-shell tachyons with
# alpha' t = -5.2, alpha' u = -6.4, alpha' s = -16 + 11.6 = -4.4 (s through the
# circle): a_- = -3 - alpha' t / 2, a_+ = -3 - alpha' u / 2, h0 = -alpha' s / 2 - 2.
# Momentum conservation forces h0 = -(a_- + a_+) on and off shell (C4.1-onshell-map).
MOMENTA = {
    "A": (-0.45, -0.35, 0.8),
    "B": (2.0, -1.4, -0.6),
    "onshell": (0.2, -0.4, 0.2),
}

# ---------------------------------------------------------------------------
# C1.1 -- closed form of the integrand
# ---------------------------------------------------------------------------
print("\n# C1.1 integrand")
# on shell: alpha' k^2 = 4; alpha' k_a.k_c = alpha' k_b.k_d = -alpha' t/2 - 4, etc.
at, au = -5.2, -6.4
as_ = -16 - at - au
kk = {
    ("a", "b"): -as_ / 2 - 4,
    ("c", "d"): -as_ / 2 - 4,
    ("a", "c"): -at / 2 - 4,
    ("b", "d"): -at / 2 - 4,
    ("a", "d"): -au / 2 - 4,
    ("b", "c"): -au / 2 - 4,
}
h0_os, am_os, ap_os = MOMENTA["onshell"]
assert abs(am_os - (1 + kk[("a", "c")])) < 1e-12
assert abs(ap_os - (1 + kk[("a", "d")])) < 1e-12
assert abs(h0_os - (-as_ / 2 - 2)) < 1e-12


def vs_frame(q: complex) -> float:
    """
    On-shell integrand in an independent Moebius frame.

    Map w -> zeta with w_a -> infinity, w_b -> 0, w_c -> 1; zeta_d is the
    modulus; the on-shell Koba-Nielsen factor is |zeta_d|^{alpha' k_b.k_d}
    |1 - zeta_d|^{alpha' k_c.k_d}, times |d zeta_d / dq|^2 |q|^2 (d^2 q =
    |q|^2 ds dtheta) and the c-ghost Jacobian (absorbed in |dzeta|^2 on shell).
    """

    def zeta(qq: complex) -> complex:
        wa, wb, wc, wd = 2 * BETA, -2 * BETA, qq / (2 * BETA), -qq / (2 * BETA)
        return ((wd - wb) * (wc - wa)) / ((wd - wa) * (wc - wb))

    eps = 1e-6
    dz = (zeta(q + eps) - zeta(q - eps)) / (2 * eps)
    z = zeta(q)
    return (
        abs(z) ** kk[("b", "d")]
        * abs(1 - z) ** kk[("c", "d")]
        * abs(dz) ** 2
        * abs(q) ** 2
    )


qs = 4 * B2 * rng.uniform(0.05, 0.95, 8) * np.exp(1j * rng.uniform(0, 2 * np.pi, 8))
ratio = np.array([integrand(q, h0_os, am_os, ap_os) / vs_frame(q) for q in qs])
ratio_nog = np.array(
    [
        integrand(q, h0_os, am_os, ap_os)
        / abs(1 - (q / FOUR_B2) ** 2) ** 2
        / vs_frame(q)
        for q in qs
    ]
)
spread = np.std(ratio) / np.mean(ratio)
spread_break = np.std(ratio_nog) / np.mean(ratio_nog)
report(
    "C1.1-onshell",
    bool(spread < 1e-6 and spread_break > 1e-2),
    f"rel. spread of I / VS-frame over 8 seeded q: {spread:.1e}; "
    f"break (no ghost factor): {spread_break:.1e}",
)
# holomorphic ghost factor by residues of <b(w) c1 c2 c3 c4> = prod z_ij / prod(w - z_i)
aa, xx = 2 * BETA, 0.37 + 0.52j
zs_ = [aa, -aa, xx, -xx]
pref = np.prod([zs_[i] - zs_[j] for i in range(4) for j in range(i + 1, 4)])
res = sum(
    zi * pref / np.prod([zi - zj for zj in zs_ if zj != zi]) for zi in (xx, -xx)
)  # b_0 = oint w b(w), circle enclosing the copy-2 punctures
pred = xx * (aa**2 - xx**2)
r1 = res / pred
xx2 = -0.81 + 0.23j
zs_ = [aa, -aa, xx2, -xx2]
pref = np.prod([zs_[i] - zs_[j] for i in range(4) for j in range(i + 1, 4)])
res2 = sum(
    zi * pref / np.prod([zi - zj for zj in zs_ if zj != zi]) for zi in (xx2, -xx2)
)
r2 = res2 / (xx2 * (aa**2 - xx2**2))
report(
    "C1.1-ghost",
    bool(abs(r1 - r2) < 1e-12 * abs(r1)),
    f"residue route / x(a^2-x^2) = {r1:.6f} at two x (constant)",
)

# ---------------------------------------------------------------------------
# C1.2 -- growth at fixed m (Darboux)
# ---------------------------------------------------------------------------
print("\n# C1.2 growth at fixed m")
NMAX = 1700
G: dict[str, np.ndarray] = {}
for lab, (h0, am, ap) in MOMENTA.items():
    G[lab] = g_coeffs(am, ap, NMAX)
# independent route for the coefficients
gc = g_by_convolution(-0.35, 0.8, 300)
conv_err = np.max(np.abs(gc - G["A"][:301]) / (np.abs(G["A"][:301]) + 1e-300))
report(
    "C1.2-coeffs",
    bool(conv_err < 1e-8),
    f"recurrence vs convolution, max rel err {conv_err:.1e}",
)

ok_all = True
for lab, (h0, am, ap) in MOMENTA.items():
    alpha = min(am, ap)
    g = G[lab]
    for m in (0, 2, 4):
        Ns = np.array([200, 400, 800, 1600])
        exact = g[Ns] * g[Ns - m]
        dar = darboux_g(am, ap, Ns) * darboux_g(am, ap, Ns - m)
        rel = np.abs(exact / dar - 1)
        Nfit = np.arange(800, 1601, 2)
        sl = slope(Nfit, np.abs(g[Nfit] * g[Nfit - m]))
        ok = bool(
            rel[-1] < rel[0] and rel[-1] < 0.05 and abs(sl - (-2 * alpha - 2)) < 0.03
        )
        brk = abs(sl - (-alpha - 1)) > 0.1
        ok_all &= ok and brk
        msg = (
            f"[{lab} m={m}] slope {sl:+.4f} vs -2a-2 = {-2 * alpha - 2:+.4f} "
            f"(break -a-1 = {-alpha - 1:+.4f}); Darboux rel.err {rel[0]:.1e} -> {rel[-1]:.1e}"
        )
        print("   ", msg)
        LOG.write(msg + "\n")
report("C1.3-darboux-m", ok_all, "fixed-m growth c_{h,m}(4b^2)^h ~ h^{-2 alpha - 2}")

# ---------------------------------------------------------------------------
# C1.3 -- growth at fixed theta (level terms), on the fold arcs and at pi/2
# ---------------------------------------------------------------------------
print("\n# C1.3 growth at fixed theta")
TH1 = float(np.arccos(2 * 16 / 25 - 1))  # 73.74 deg, fold-arc endpoint
TH2 = float(np.arccos(2 * 9 / 25 - 1))  # 106.26 deg
ok_all = True
NT = 1600
centres = [200, 400, 800, 1500]
for lab, (h0, am, ap) in MOMENTA.items():
    alpha = min(am, ap)
    g = G[lab]
    for thdeg, pred in ((80.0, -alpha - 1), (100.0, -alpha - 1), (90.0, -am - ap - 1)):
        t = level_terms(g, np.deg2rad(thdeg), NT)
        env = rms_envelope(t, centres, 60)
        sl = slope(np.array(centres[1:], float), env[1:])
        ok = abs(sl - pred) < 0.06
        if thdeg == 90.0 and abs(am - ap) > 0.3:
            ok &= (
                abs(sl - (-alpha - 1)) > 0.15
            )  # break: the generic exponent fails here
        ok_all &= bool(ok)
        msg = f"[{lab} theta={thdeg}] envelope slope {sl:+.4f} vs predicted {pred:+.4f}"
        print("   ", msg)
        LOG.write(msg + "\n")
report(
    "C1.3-darboux-theta",
    ok_all,
    "T_n(theta) ~ n^{-alpha-1} on the arcs, n^{-(a_-+a_+)-1} at pi/2",
)
np.save(SCRATCH / "g_coeffs.npy", np.array([G[k] for k in MOMENTA]))


# ---------------------------------------------------------------------------
# Geometry: sigma_V(theta) by per-ray bisection (functions copied from
# codes/verify-circle-gluing-inverse.py, record 074; that script is not edited)
# ---------------------------------------------------------------------------
def z_of_q(q: np.ndarray) -> np.ndarray:
    """s-channel puncture location, R2: Z = (q + 4 beta^2)^2 / (16 beta^2 q)."""
    return (q + 4 * B2) ** 2 / (16 * B2 * q)


def q_of_zs(zs: np.ndarray) -> np.ndarray:
    """Root of q^2 + (8 b^2 - 16 b^2 zs) q + 16 b^4 = 0 with |q| < 4 b^2 (032 (3.1))."""
    b = 8 * B2 - 16 * B2 * zs
    disc = np.sqrt(b * b - 4 * 16 * B2**2 + 0j)
    r1 = (-b + disc) / 2
    r2 = (-b - disc) / 2
    return np.where(np.abs(r1) < np.abs(r2), r1, r2)


def min_tu(z: np.ndarray) -> np.ndarray:
    """min(|q_t|, |q_u|) with the closures of 032 (3.1)."""
    qt = q_of_zs(z / (z - 1))
    qu = q_of_zs(1 - 1 / z)
    return np.minimum(np.abs(qt), np.abs(qu))


LN4B2 = float(np.log(FOUR_B2))


def sigma_v(th: np.ndarray, iters: int = 60) -> np.ndarray:
    """sigma_V(theta): exit of the ray q = e^{sigma + i theta} from M'_x (074 (1.4))."""
    th = np.asarray(th, float)
    lo = np.full(th.shape, 1e-6)
    hi = np.full(th.shape, LN4B2)
    at_fold = min_tu(z_of_q(np.exp(hi - 1e-13 + 1j * th))) > 1
    for _ in range(iters):
        mid = (lo + hi) / 2
        ins = min_tu(z_of_q(np.exp(mid + 1j * th))) > 1
        lo = np.where(ins, mid, lo)
        hi = np.where(ins, hi, mid)
    return np.where(at_fold, LN4B2, lo)


print("\n# C2 geometry")
# profile at the arc endpoint: rho = ln 4b^2 - sigma_V ~ c sqrt(theta_1 - theta)
dl = np.array([1e-2, 1e-3, 1e-4, 1e-5])
rho_end = LN4B2 - sigma_v(TH1 - dl)
cfit = rho_end / np.sqrt(dl)
mono = np.all(np.diff(sigma_v(np.linspace(0, TH1, 3001))) >= -1e-12)
report(
    "C2.1-profile",
    bool(
        mono
        and abs(cfit[-1] - np.sqrt(3)) < 2e-3
        and abs(sigma_v(np.array([0.0]))[0] - np.log(9 / 4)) < 1e-9
    ),
    f"sigma_V monotone on [0, th1]; rho/sqrt(th1-th) = {np.round(cfit, 4)} -> sqrt3; sigma_V(0) = ln 9/4",
)
LOG.write(f"rho/sqrt(delta) at delta={dl}: {cfit}\n")

# theta nodes on [0, th1]: theta = th1 - v^2, composite Gauss-Legendre in v,
# geometric panels near v = 0 (boundary layer rho ~ sqrt3 v of width 1/h).
xg, wg = np.polynomial.legendre.leggauss(16)
vmax = float(np.sqrt(TH1))
edges = np.concatenate(
    [[0.0], np.geomspace(1e-6, 2e-3, 14), np.arange(4e-3, vmax, 2e-3), [vmax]]
)
edges = np.unique(edges)
vn = np.concatenate(
    [(b - a) / 2 * xg + (a + b) / 2 for a, b in zip(edges[:-1], edges[1:])]
)
vw = np.concatenate([(b - a) / 2 * wg for a, b in zip(edges[:-1], edges[1:])])
TH_OFF = TH1 - vn**2
W_OFF = 2 * vn * vw  # d theta = 2 v dv
RHO_OFF = LN4B2 - sigma_v(TH_OFF)
# arc piece [th1, pi/2] (rho = 0): Gauss-Legendre for the direct integral
xa, wa = np.polynomial.legendre.leggauss(400)
TH_ARC = (np.pi / 2 - TH1) / 2 * xa + (np.pi / 2 + TH1) / 2
W_ARC = (np.pi / 2 - TH1) / 2 * wa
print(f"   theta nodes off the arc: {len(TH_OFF)}")


def fhat_table(ms: np.ndarray, hs: np.ndarray) -> np.ndarray:
    """
    F_m(h) = int_0^{2 pi} e^{i m theta} e^{-rho(theta) h} d theta for even m >= 0.

    Uses evenness and pi-periodicity of sigma_V: F_m = 4 int_0^{pi/2}; on the arc
    (rho = 0) exactly 4 (sin(m pi/2) - sin(m th1)) / m. Then
    c_{h,m} fhat_m(h) = N g_N g_Nbar [F_m(h) - 2 pi delta_{m0} (4 b^2)^{-h}] / h.
    """
    off = np.cos(np.outer(ms, TH_OFF)) @ (
        W_OFF[:, None] * np.exp(-np.outer(RHO_OFF, hs))
    )
    arc = np.where(
        ms == 0, np.pi / 2 - TH1, -np.sin(ms * TH1) / np.where(ms == 0, 1, ms)
    )
    return 4 * (off + arc[:, None])


# independent check of the table against the 074 definition on a uniform grid
thu = np.linspace(0, 2 * np.pi, 2**16, endpoint=False)
sgu = sigma_v(thu)
for m_, h_ in ((0, 3.3), (4, 7.1), (6, -2.0)):
    ref = np.mean(np.exp(1j * m_ * thu) * np.exp(-(LN4B2 - sgu) * h_)) * 2 * np.pi
    val = fhat_table(np.array([m_]), np.array([h_]))[0, 0]
    LOG.write(f"F_{m_}({h_}) table {val:.10f} uniform {ref.real:.10f}\n")
    assert abs(val - ref.real) < 1e-4 * max(1, abs(ref)), (m_, h_, val, ref)
# the 074 zero of fhat_4 at h* ~ -2.36 (C2.4-real-zeros) is reproduced by the table
hz = np.linspace(-2.6, -2.1, 501)
f4 = fhat_table(np.array([4]), hz)[0] / hz
zc = hz[np.where(np.diff(np.sign(f4)))[0]]
report(
    "C3.1-table",
    bool(len(zc) == 1 and abs(zc[0] + 2.36) < 0.01),
    f"F_m(h) table vs uniform grid (asserted 1e-4); real zero of fhat_4 at {zc} (074: -2.36)",
)


def direct_integral(h0: float, am: float, ap: float, nr: int = 48) -> float:
    """J = int_{Q_V} I ds dtheta = 2 int_0^{pi/2} dth int_0^{sigma_V} dsigma [I(y) + I(-y)]."""
    xr, wr = np.polynomial.legendre.leggauss(nr)
    tot = 0.0
    for ths, ws, sv in (
        (TH_OFF, W_OFF, LN4B2 - RHO_OFF),
        (TH_ARC, W_ARC, np.full(TH_ARC.shape, LN4B2)),
    ):
        sig = np.outer(sv / 2, xr + 1)  # nodes in [0, sigma_V]
        wsig = np.outer(sv / 2, wr)
        q = np.exp(sig + 1j * ths[:, None])
        val = integrand(q, h0, am, ap) + integrand(-q, h0, am, ap)
        tot += float(np.sum(ws[:, None] * wsig * val))
    return 2 * tot


# ---------------------------------------------------------------------------
# C2 -- region-integrated sums in three orders
# ---------------------------------------------------------------------------
print("\n# C2 integrated sums")
MOM2 = {
    "A": (-0.45, -0.35, 0.8),  # alpha > -1
    "onshell": (0.2, -0.4, 0.2),
    "B": (1.7, -1.4, -0.3),  # -2 < alpha < -1, a_- + a_+ > -2
    "C": (1.9, -2.4, 0.5),  # -3 < alpha < -2: level order conditional (endpoints)
    "E": (
        2.4,
        -1.2,
        -1.2,
    ),  # -3 < a_- + a_+ < -2: level order conditional (arc midpoint)
    "D": (2.5, -3.5, 1.0),  # alpha < -3: level order diverges
    "F": (3.5, -1.75, -1.75),  # alpha > -3 but h0 >= 3: diverges through the midpoint
}
for _lab, (_h0, _am, _ap) in {**MOMENTA, **MOM2}.items():
    assert abs(_h0 + _am + _ap) < 1e-12, _lab  # conservation: h0 = -(a_- + a_+)
HMAX = 1600
ns = np.arange(0, HMAX + 1, 2)  # only even n = N + Nbar meet even m
ms = np.arange(0, HMAX + 1, 2)
SUMS: dict[str, dict] = {}
for lab, (h0, am, ap) in MOM2.items():
    g = g_coeffs(am, ap, HMAX)
    hs = h0 + ns
    if np.any(np.isclose(hs, 0.0)):
        # h0 a non-positive even integer: the m != 0 terms are 0/0 here (their
        # analytic value is finite); outside the domain of this pipeline.
        raise ValueError(
            f"[{lab}] h = h0 + n = 0 for some even n: h0 = {h0} not allowed"
        )
    Ft = fhat_table(ms, hs)  # [m_idx, n_idx]
    Ft[0] -= 2 * np.pi * FOUR_B2 ** (-hs)  # the -1 of the m = 0 transform
    # term(n, m) for m >= 0 (m and -m together for m > 0)
    term = np.zeros((len(ms), len(ns)))
    for j, n in enumerate(ns):
        mm = ms[ms <= n]
        nb = (n - mm) // 2
        nn = (n + mm) // 2
        mult = np.where(mm == 0, 1.0, 2.0)
        term[: len(mm), j] = mult * g[nn] * g[nb] * Ft[: len(mm), j] / hs[j]
    level = np.cumsum(term.sum(axis=0))  # level order: partial sums over n <= H
    absolute = np.cumsum(np.abs(term).sum(axis=0))
    sector = np.cumsum(term, axis=1)  # sector order: fixed m, partial sums over n
    J = direct_integral(h0, am, ap)
    SUMS[lab] = dict(level=level, absolute=absolute, sector=sector, J=J, term=term, g=g)
    msg = (
        f"[{lab}] a=({am},{ap}) J={J:.10f}; level S(H) at H=400,800,1600: "
        f"{level[200]:.10f} {level[400]:.10f} {level[800]:.10f}; "
        f"abs sum {absolute[200]:.4e} {absolute[400]:.4e} {absolute[800]:.4e}; "
        f"sector m=4 partial {sector[2, 200]:.6e} {sector[2, 400]:.6e} {sector[2, 800]:.6e}"
    )
    print("   ", msg, flush=True)
    LOG.write(msg + "\n")
    LOG.flush()

Hs = ns  # level cut H = n_max of the partial sum
iw = (Hs >= 400) & (Hs <= 1600)


def win_env(e: np.ndarray, half: int) -> np.ndarray:
    """Windowed max of |e| over [k - half, k + half] (envelope of an oscillating error)."""
    a = np.abs(e)
    return np.array([a[max(0, k - half) : k + half + 1].max() for k in range(len(a))])


def env_err(lab: str) -> np.ndarray:
    """Envelope of the level-order error |S(H) - J| (windows of 50 even levels)."""
    return win_env(SUMS[lab]["level"] - SUMS[lab]["J"], 25)


# C2.1: absolutely convergent regime (alpha > -1): every order converges to J
ok = True
for lab in ("A", "onshell"):
    S = SUMS[lab]
    h0, am, ap = MOM2[lab]
    alpha = min(am, ap)
    err = abs(S["level"][-1] - S["J"]) / S["J"]
    # tail of the absolute series: increments over doubling windows ~ H^{-2 alpha - 2}
    inc = np.array([S["absolute"][k] - S["absolute"][k // 2] for k in (200, 400, 800)])
    sl_abs = np.log(inc[-1] / inc[0]) / np.log(4)
    # each sector converges: increments ~ H^{-2 alpha - 2}
    sec_inc = np.array(
        [abs(S["sector"][2, k] - S["sector"][2, k // 2]) for k in (200, 400, 800)]
    )
    sl_sec = np.log(sec_inc[-1] / sec_inc[0]) / np.log(4)
    ok &= bool(
        err < 1e-8
        and abs(sl_abs - (-2 * alpha - 2)) < 0.15
        and abs(sl_sec - (-2 * alpha - 2)) < 0.15
    )
    msg = (
        f"[{lab}] |S(1600)-J|/J = {err:.1e}; abs-series increment slope {sl_abs:+.3f}, "
        f"sector m=4 increment slope {sl_sec:+.3f} (pred. -2a-2 = {-2 * alpha - 2:+.3f})"
    )
    print("   ", msg)
    LOG.write(msg + "\n")
report(
    "C2.2-absolute",
    ok,
    "alpha > -1: unordered sum absolutely convergent, = J; sectors converge",
)

# C2.2: alpha <= -1: sector sums and the absolute series diverge like H^{-2 alpha - 2}
ok = True
for lab in ("B", "C", "E", "D"):
    S = SUMS[lab]
    h0, am, ap = MOM2[lab]
    alpha = min(am, ap)
    for mi in (0, 1, 2):  # m = 0, 2, 4
        sec = np.abs(S["sector"][mi, iw])
        sl = slope(Hs[iw].astype(float), sec)
        ok &= bool(abs(sl - (-2 * alpha - 2)) < 0.08)
        msg = f"[{lab} m={2 * mi}] |F_m(H)| slope {sl:+.3f} vs -2a-2 = {-2 * alpha - 2:+.3f}"
        print("   ", msg)
        LOG.write(msg + "\n")
# break leg: in the convergent regime the same partial sums do not grow
brk = all(
    abs(SUMS[lab]["sector"][2, -1] / SUMS[lab]["sector"][2, 200] - 1) < 1e-2
    for lab in ("A", "onshell")
)
report(
    "C2.2-sector-divergence",
    bool(ok and brk),
    "alpha <= -1: fixed-m sector sums grow as H^{-2 alpha - 2}; not for alpha > -1",
)

# C2.3: level order, error envelope ~ H^{p}, p = max(-alpha - 3, -(a_- + a_+) - 3)
# (endpoint terms n^{-alpha-3}, centre n^{-(a_-+a_+)-3}, record 079 (2.4)).
# Exponent law tested where one term dominates by >= 0.5 (critic 079 #17):
#   C (-3 < alpha <= -2): endpoint term alone, -alpha-3 = -0.60 vs centre -1.10;
#   E (-3 < a_- + a_+ <= -2): centre term alone, -(a_-+a_+)-3 = -0.60 vs endpoint -1.80;
#   D (alpha < -3): endpoint term, divergent, +0.50 vs centre -0.50 (break leg).
# Tolerance 0.1, and the subdominant exponent must be rejected (|sl - p_sub| > 0.3).
# B (-2 < alpha, a_- + a_+ > -2): the two terms (-1.30, -1.60) compete at H <= 1600,
# so B tests only convergence (error decreasing, slope within the bracket of the two
# exponents widened by 0.1), not the exponent law.
ok = True
for lab in ("B", "C", "E", "D"):
    h0, am, ap = MOM2[lab]
    alpha = min(am, ap)
    p_end, p_mid = -alpha - 3, -(am + ap) - 3
    p_pred, p_sub = max(p_end, p_mid), min(p_end, p_mid)
    e = env_err(lab)
    sl = slope(Hs[iw].astype(float), e[iw])
    if lab == "B":
        ok &= bool(sl < -0.3 and p_sub - 0.1 < sl < p_pred + 0.1)
    elif lab in ("C", "E"):
        ok &= bool(sl < -0.3 and abs(sl - p_pred) < 0.1 and abs(sl - p_sub) > 0.3)
    else:  # D: grows; break leg of the convergence criterion
        ok &= bool(sl > 0.2 and abs(sl - p_pred) < 0.1 and abs(sl - p_sub) > 0.3)
    msg = (
        f"[{lab}] level-order error envelope slope {sl:+.3f} (pred. {p_pred:+.3f}, "
        f"subdominant {p_sub:+.3f}); |S(1600)-J| = "
        f"{abs(SUMS[lab]['level'][-1] - SUMS[lab]['J']):.2e}"
    )
    print("   ", msg)
    LOG.write(msg + "\n")
report(
    "C2.3-level-order",
    ok,
    "level order converges to J for alpha > -3 (abs. for alpha > -2), diverges below",
)


# C2.3-h0-threshold: divergent side of h0 < 3 (critic 079 #18). F: alpha = -1.75 > -3
# (endpoint term n^{-alpha-3} = n^{-1.25} convergent), h0 = 3.5 >= 3 (centre term
# n^{h0-3} = n^{+0.5}): the level-order error envelope must grow with slope +0.5.
h0, am, ap = MOM2["F"]
e = env_err("F")
sl = slope(Hs[iw].astype(float), e[iw])
okF = bool(sl > 0.2 and abs(sl - (h0 - 3)) < 0.1 and abs(sl - (-min(am, ap) - 3)) > 0.3)
msg = (
    f"[F] level-order error envelope slope {sl:+.3f} (pred. h0-3 = {h0 - 3:+.3f}, "
    f"endpoint {-min(am, ap) - 3:+.3f}); |S(1600)-J| = "
    f"{abs(SUMS['F']['level'][-1] - SUMS['F']['J']):.2e}"
)
print("   ", msg)
LOG.write(msg + "\n")
report(
    "C2.3-h0-threshold",
    okF,
    "alpha > -3 but h0 >= 3: level order diverges through the arc midpoint",
)


# C2.4: Abel identity: sum_n L_n r^n = r^{-h0} int_{Q_V} I(r y), for every momentum
# (the pipeline test independent of convergence), and the Abel limit r -> 1 is J.
def direct_integral_r(h0: float, am: float, ap: float, r: float, nr: int = 48) -> float:
    """r^{-h0} int_{Q_V} I(r q) ds dtheta, the Abel-regularised region integral."""
    xr, wr = np.polynomial.legendre.leggauss(nr)
    tot = 0.0
    for ths, ws, sv in (
        (TH_OFF, W_OFF, LN4B2 - RHO_OFF),
        (TH_ARC, W_ARC, np.full(TH_ARC.shape, LN4B2)),
    ):
        sig = np.outer(sv / 2, xr + 1)
        wsig = np.outer(sv / 2, wr)
        q = r * np.exp(sig + 1j * ths[:, None])
        val = integrand(q, h0, am, ap) + integrand(-q, h0, am, ap)
        tot += float(np.sum(ws[:, None] * wsig * val))
    return 2 * tot * r ** (-h0)


ok = True
for lab in ("A", "D"):
    h0, am, ap = MOM2[lab]
    L = SUMS[lab]["term"].sum(axis=0)
    for r in (0.97, 0.985):
        ab = float(np.sum(L * r**ns))
        dr = direct_integral_r(h0, am, ap, r)
        tol = (
            1e-9 if lab == "A" else 1e-7
        )  # D: g_N ~ N^{2.5}, float64 cancellation in L_n
        ok &= bool(abs(ab - dr) < tol * abs(dr))
        msg = f"[{lab} r={r}] Abel sum {ab:.12f} vs direct {dr:.12f}"
        print("   ", msg)
        LOG.write(msg + "\n")
    lim = [direct_integral_r(h0, am, ap, r) for r in (0.999, 0.9999)]
    ok &= bool(
        abs(lim[-1] - SUMS[lab]["J"]) < 1e-3 * SUMS[lab]["J"]
        and abs(lim[-1] - SUMS[lab]["J"]) < abs(lim[0] - SUMS[lab]["J"])
    )
# break: a wrong transform (drop the -1 of m = 0) breaks the identity
h0, am, ap = MOM2["D"]
Lb = SUMS["D"]["term"].sum(axis=0) + 2 * np.pi * FOUR_B2 ** (-(h0 + ns)) * SUMS["D"][
    "g"
][ns // 2] ** 2 / (h0 + ns)
brk = abs(float(np.sum(Lb * 0.97**ns)) - direct_integral_r(h0, am, ap, 0.97)) > 1e-6
report(
    "C2.4-abel",
    bool(ok and brk),
    "sum_n L_n r^n = r^{-h0} int_{Q_V} I(r y) exactly; Abel limit = J for all momenta",
)


# C2.5: ray-wise sums at fixed theta
def ray_partial(g: np.ndarray, h0: float, theta: float, nmax: int) -> np.ndarray:
    """Partial sums over n of T_n(theta) [e^{-rho h} - (4b^2)^{-h}] / h on the ray theta."""
    t_n = level_terms(g, theta, nmax)
    rho = LN4B2 - sigma_v(np.array([theta]))[0]
    hh = h0 + np.arange(nmax + 1)
    return np.cumsum(t_n * (np.exp(-rho * hh) - FOUR_B2 ** (-hh)) / hh)


def ray_direct(h0: float, am: float, ap: float, theta: float) -> float:
    """int_0^{sigma_V(theta)} I(e^{sigma + i theta}) d sigma by Gauss-Legendre."""
    xr, wr = np.polynomial.legendre.leggauss(80)
    sv = sigma_v(np.array([theta]))[0]
    sig = sv / 2 * (xr + 1)
    return float(np.sum(sv / 2 * wr * integrand(np.exp(sig + 1j * theta), h0, am, ap)))


ok = True
for lab in ("A", "B", "D"):
    h0, am, ap = MOM2[lab]
    g = SUMS[lab]["g"]
    # theta = pi: strictly inside (rho = ln 4): exponential convergence, ratio -> 1/4
    rp = ray_partial(g, h0, np.pi, 60)
    jp = ray_direct(h0, am, ap, np.pi)
    e40 = abs(rp[40] - jp) / abs(jp)
    ok &= bool(e40 < 1e-12)
    # fold-arc ray theta = 80 deg: polynomial; converges iff alpha > -2 (abs. iff > -1)
    th80 = np.deg2rad(80.0)
    ra = ray_partial(g, h0, th80, 1600)
    ja = ray_direct(h0, am, ap, th80)
    ea = np.abs(ra - ja)
    env = win_env(ea, 50)
    sl = slope(np.arange(400, 1501, dtype=float), env[400:1501])
    e40_arc = abs(ra[40] - ja) / abs(ja)
    ok &= bool(
        abs(sl - (-(min(am, ap) + 2))) < 0.15
    )  # D: -alpha-2 > 0, the ray sum diverges
    ok &= bool(
        e40_arc > 1e-6
    )  # break leg: the fold-arc ray is not exponentially convergent
    msg = (
        f"[{lab}] ray pi: rel.err(H=40) {e40:.1e}; ray 80deg: rel.err(H=40) {e40_arc:.1e}, "
        f"envelope slope {sl:+.3f} (pred. {-(min(am, ap) + 2):+.3f})"
    )
    print("   ", msg)
    LOG.write(msg + "\n")
report(
    "C2.5-rays",
    ok,
    "theta = pi exponential; fold-arc ray ~ H^{-alpha-2}, divergent for alpha < -2",
)

# ---------------------------------------------------------------------------
# C4 -- on-shell map of the exponents (sympy, exact)
# ---------------------------------------------------------------------------
print("\n# C4 on-shell exponents")
import sympy as sp  # noqa: E402

lab4 = "abcd"
kap = {}
for i in range(4):
    for j in range(i, 4):
        kap[(i, j)] = sp.Symbol(f"k_{lab4[i]}{lab4[j]}", real=True)


def K(i: int, j: int) -> sp.Symbol:
    """alpha' k_i . k_j, symmetric."""
    return kap[(min(i, j), max(i, j))]


cons = [sum(K(i, j) for j in range(4)) for i in range(4)]  # momentum conservation
a, b, c, d = range(4)
am_s = 1 + (K(a, c) + K(b, d)) / 2
ap_s = 1 + (K(a, d) + K(b, c)) / 2
h0_s = (K(c, c) + K(d, d) + 2 * K(c, d)) / 2 - 2
s_, t_, u_ = sp.symbols("s t u", real=True)  # alpha' times Mandelstam
onshell = {K(i, i): 4 for i in range(4)}
sol = sp.solve(
    [e.subs(onshell) for e in cons] + [t_ + (8 + 2 * K(a, c)), u_ + (8 + 2 * K(a, d))],
    [K(a, b), K(a, c), K(a, d), K(b, c), K(b, d), K(c, d)],
    dict=True,
)[0]
s_val = sp.simplify(-(8 + 2 * K(c, d)).subs(sol))  # alpha' s = -alpha' (k_c + k_d)^2
am_os_s = sp.simplify(am_s.subs(onshell).subs(sol))
ap_os_s = sp.simplify(ap_s.subs(onshell).subs(sol))
h0_os_s = sp.simplify(h0_s.subs(onshell).subs(sol))
ok = (
    sp.simplify(s_val + t_ + u_ + 16) == 0
    and sp.simplify(am_os_s - (-3 - t_ / 2)) == 0
    and sp.simplify(ap_os_s - (-3 - u_ / 2)) == 0
    and sp.simplify(h0_os_s - (-s_val / 2 - 2)) == 0
)
# a_- + a_+ + h0 = (alpha'/2)(k_a + k_b + k_c + k_d).(k_c + k_d): zero by conservation,
# on and off shell. Check off shell (all k_i^2 free), and the break leg without conservation.
sol_gen = sp.solve(cons, [K(a, b), K(a, c), K(b, d), K(a, d)], dict=True)[0]
rel = sp.simplify((am_s + ap_s + h0_s).subs(sol_gen))
rel_free = sp.simplify(am_s + ap_s + h0_s)
report(
    "C4.1-onshell-map",
    bool(ok and rel == 0 and rel_free != 0),
    f"on shell a_- = -3 - a't/2, a_+ = -3 - a'u/2, h0 = -a's/2 - 2; a_- + a_+ + h0 = {rel} "
    f"off shell with conservation; without conservation: {rel_free} (break leg)",
)

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
npass = sum(ok for _, ok in RESULTS)
print(f"\n{npass}/{len(RESULTS)} PASS (seed {SEED})")
LOG.write(f"{npass}/{len(RESULTS)} PASS (seed {SEED})\n")
LOG.close()
sys.exit(0 if npass == len(RESULTS) else 1)
