"""
Companion checks for derivation record 084 (fold-arc convergence threshold of the
(h, m) sector expansion of the fixed-halves gluing for excited inputs; establishes
or corrects 079 C4.3 / R83's argued clause).

Model: as record 079 (fixed-halves gluing, 074 A5; beta = 3/2; y = q / 4 beta^2;
punctures w_a = 2 beta, w_b = -2 beta, w_c = 2 beta y, w_d = -2 beta y). The
tachyon integrand is 079 (1.4), |y|^{h0} |1 - y|^{2 a_-} |1 + y|^{2 a_+}; excited
inputs multiply it by the Wick oscillator factor (084 (1.1)-(1.6)), computed here
from the raw puncture positions.

What is verified:

- C1.2-exponent: the full integrand (Wick factor at raw positions times 079 (1.4))
  behaves as |1 - y|^{2 (a_- - N_tot)} at y -> 1 and |1 + y|^{2 (a_+ - N_tot)} at
  y -> -1, for one level-(1,1) input at a (generic transverse tensor
  polarisation), two level-one inputs at a and c, a level-(2,2) input at a
  ((e1.dX)(e2.dX) and e.d^2X, leading Wick term), and level zero (break legs: the
  tachyon exponent 2 a_- is rejected for every excited case).
- C1.3-subleading: (084 (1.5)) eps.Phi(y) (1 - y)^{1 - a_-} / (2^{a_+} eps.k_c)
  = 1 - (1 + a_+)(1 - y)/2 + O((1 - y)^2) (break: (1 + a_-) instead of 1 + a_+).
- C2.1-coeffs: Taylor coefficients of the holomorphic factor from the series route
  (binomial recurrences, 079 g_coeffs, combined through 084 (1.4)) agree with an
  FFT of the raw Wick factor on |y| = 0.9 for N <= 60 (single and two excited).
- C2.2-darboux-m: fixed-m coefficients |c_{N, N-m}| grow as N^{-2 alpha_eff - 2},
  alpha_eff = min(a_-, a_+) - N_tot (single and two excited inputs); the Darboux
  amplitude of the single case is reproduced (ratio -> 1); break: the tachyon
  slope -2 alpha - 2 is rejected. The fit at h <= 60 is printed.
- C2.3-darboux-theta: level terms T_n(theta) on a fold arc (80 deg) have envelope
  slope -alpha_eff - 1; at the arc midpoint slope h0 + 2 N_tot - 1.
- C2.4-level-zero: the generalised pipeline with the level-zero factor reproduces
  079's numbers (J and S(400, 800, 1600) at A and on shell) to 1e-10.
- C3.2-sector-divergence: at 079's point A (tachyons absolutely convergent), the
  excited (1,1) input gives fixed-m sector sums growing as H^{-2 alpha_eff - 2}
  while the level order converges to the direct integral J (break: tachyon sums
  at the same momenta are stationary).
- C3.2-absolute: a point with alpha_eff > -1: level sums reach J, sector sums
  converge.
- C3.2-midpoint: a point where tachyons converge absolutely but the excited
  midpoint exponent h0 + 2 N_tot >= 3: level-order error grows as
  H^{h0 + 2 N_tot - 3} (the endpoint exponent is rejected).
- C3.5-counterexample: (critic-084 #2) the withdrawn unbalanced criterion (3.3)
  fails. Level-(1,1) inputs at a and b with crossed rank-one polarisations
  (u_a perp k_a, k_d; v_a perp k_a, k_c; u_b perp k_b, k_c; v_b perp k_b, k_d) at
  a_- = a_+ = 1/4: pole orders (2, 0, 0, 2) from the raw Wick factors; the
  quadratic Q's of the series route agree with an FFT; the fixed-m sector terms
  (m = 0, 2, 4) scale as h^{-(alpha^L_- + alpha^R_+) - 3} = h^{1/2} with
  alternating sign, and the partial-sum swing grows as H^{1/2}, so every sector
  sum diverges where (3.3) predicted fixed-sign terms h^{-3/2} (rejected by 2);
  break: tachyon terms at the same momenta decay (envelope slope < -2). The
  integrand of this configuration is complex (no reality condition imposed); the
  check is on the complex terms.
- C4.1-onshell: (sympy) with on-shell masses alpha' k_j^2 = 4 (1 - N_j),
  a_- - N_tot = -3 - alpha' t / 2 and a_+ - N_tot = -3 - alpha' u / 2,
  independent of the levels; alpha'(s + t + u) = -16 + 4 N_tot (break: with the
  wrong mass shell alpha' k^2 = 4 (1 + N) the identity fails).
- C4.3-parity-odd: (critic-084 #4) B-fields (antisymmetric transverse eps) at a
  and c, tachyons at b, d, point A: the full Wick integrand behaves as
  |1 - y|^{2 (a_- - 2)} at y -> 1 (B-B couples to the tachyon through the eta
  contractions) but as |1 + y|^{2 a_+ - 2} at y -> -1, not |1 + y|^{2 (a_+ - 2)}:
  the B-T pairs do not couple to the channel tachyon and the leading term is the
  spin-one exchange. Break: symmetric generic tensors at a and c give
  2 (a_+ - 2) at y -> -1.

What is not verified: the non-primary local-coordinate corrections (argued
lower-level, 084 (1.4)); ghost-oscillator inputs (outside A3); the generic
non-vanishing of the leading OPE coefficient beyond the sampled polarisations;
the normalisation N (cancels).

Run from the project root:
    uv run --no-sync python codes/verify-fold-arc-excited.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

SEED = 20261004
rng = np.random.default_rng(SEED)
print(f"seed {SEED}")

SCRATCH = Path(__file__).resolve().parent / "output" / "fold-arc-excited"
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


def note(msg: str) -> None:
    """Print and log an informational line."""
    print("   ", msg, flush=True)
    LOG.write(msg + "\n")
    LOG.flush()


BETA = 1.5
B2 = BETA**2
FOUR_B2 = 4 * B2
ALPHA_P = 1.0  # Regge slope alpha' (the exponents are set through the momenta)
D = 6
ETA = np.diag([-1.0] + [1.0] * (D - 1))


def dot(u: np.ndarray, v: np.ndarray) -> float:
    """Minkowski product u.v with eta = diag(-1, +1, ...)."""
    return float(u @ ETA @ v)


# ---------------------------------------------------------------------------
# Coefficients (copied from codes/verify-fold-arc-convergence.py, not edited)
# ---------------------------------------------------------------------------
def g_coeffs(am: float, ap: float, nmax: int, dps: int = 40) -> np.ndarray:
    """
    Taylor coefficients of (1 - y)^am (1 + y)^ap to order nmax (079 (1.6)).

    Recurrence (N + 1) g_{N+1} = (ap - am) g_N + (N - 1 - ap - am) g_{N-1}.

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


def slope(x: np.ndarray, y: np.ndarray) -> float:
    """Least-squares slope of log y against log x."""
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


def rms_envelope(t: np.ndarray, centres: list[int], half: int) -> np.ndarray:
    """RMS of |t| over windows [c - half, c + half] (even n only)."""
    out = []
    for c in centres:
        idx = np.arange(c - half, c + half + 1)
        idx = idx[idx % 2 == 0]
        out.append(np.sqrt(np.mean(np.abs(t[idx]) ** 2)))
    return np.array(out)


# ---------------------------------------------------------------------------
# Kinematics: explicit momenta in R^{1,5} with prescribed (h0, a_-, a_+)
# ---------------------------------------------------------------------------
def make_kin(h0: float, am: float, seed: int) -> dict:
    """
    Explicit off-shell momenta with sum k = 0 realising (h0, a_-) (a_+ = -h0 - a_-).

    (k_a + k_b)^2 = 2 (h0 + 2) / alpha'; a_- - 1 = alpha'/2 [(k_a - k_b).k_c
    - k_a.k_b - k_b^2] is linear in k_c and is solved along a random direction.
    The exponents are then recomputed from the vectors (079 (1.4)).
    """
    r = np.random.default_rng(seed)
    p2 = 2 * (h0 + 2) / ALPHA_P
    p = np.zeros(D)
    if p2 >= 0:
        p[1] = np.sqrt(p2)
    else:
        p[0] = np.sqrt(-p2)
    delta = r.normal(size=D) * 0.7
    ka, kb = p / 2 + delta, p / 2 - delta
    kc = r.normal(size=D) * 0.7
    e = r.normal(size=D)
    target = 2 * (am - 1) / ALPHA_P + dot(ka, kb) + dot(kb, kb)
    t = (target - dot(ka - kb, kc)) / dot(ka - kb, e)
    kc = kc + t * e
    kd = -(ka + kb + kc)
    k = {"a": ka, "b": kb, "c": kc, "d": kd}
    kap = {(i, j): ALPHA_P * dot(k[i], k[j]) for i in k for j in k}
    h0v = ALPHA_P / 2 * dot(kc + kd, kc + kd) - 2
    amv = 1 + (kap[("a", "c")] + kap[("b", "d")]) / 2
    apv = 1 + (kap[("a", "d")] + kap[("b", "c")]) / 2
    assert abs(h0v - h0) < 1e-10 and abs(amv - am) < 1e-10, (h0v, amv)
    assert abs(h0v + amv + apv) < 1e-10
    return dict(k=k, h0=h0v, am=amv, ap=apv)


def transverse_tensor(ka: np.ndarray, seed: int) -> np.ndarray:
    """Random eps_{mu nu} (lower indices) with eps_{mu nu} k_a^mu = eps_{mu nu} k_a^nu = 0."""
    r = np.random.default_rng(seed)
    eps = r.normal(size=(D, D))
    m = np.eye(D) - np.outer(ka, ETA @ ka) / dot(ka, ka)  # m @ ka = 0
    eps2 = m.T @ eps @ m
    assert np.abs(ka @ eps2).max() < 1e-10 and np.abs(eps2 @ ka).max() < 1e-10
    return eps2


def transverse_vector(k: np.ndarray, seed: int) -> np.ndarray:
    """Random polarisation (lower index) with e.k = sum e_mu k^mu = 0."""
    r = np.random.default_rng(seed)
    e = r.normal(size=D)
    return e - (e @ k) / (k @ ETA @ k) * (ETA @ k)


# ---------------------------------------------------------------------------
# Raw Wick factors at the puncture positions (084 (1.1))
# ---------------------------------------------------------------------------
def positions(y: np.ndarray) -> dict:
    """w_j in copy 1's special-leg coordinate (079 Sec. 1 Setup)."""
    y = np.asarray(y, complex)
    return {
        "a": 2 * BETA + 0 * y,
        "b": -2 * BETA + 0 * y,
        "c": 2 * BETA * y,
        "d": -2 * BETA * y,
    }


def osc(kin: dict, j: str, pol: np.ndarray, w: dict, n: int = 1) -> np.ndarray:
    """
    Contraction of pol . d^n X(w_j) with the exponentials (084 (1.1)).

    -i alpha'/2 (-1)^{n-1} (n-1)! sum_{l != j} pol.k_l / (w_j - w_l)^n.
    """
    pre = -0.5j * ALPHA_P * (-1) ** (n - 1) * float(mp.factorial(n - 1))
    return pre * sum((pol @ kin["k"][l]) / (w[j] - w[l]) ** n for l in "abcd" if l != j)


def kn_ghost(kin: dict, y: np.ndarray) -> np.ndarray:
    """079 (1.4) without N: |y|^{h0} |1-y|^{2a_-} |1+y|^{2a_+}."""
    return (
        np.abs(y) ** kin["h0"]
        * np.abs(1 - y) ** (2 * kin["am"])
        * np.abs(1 + y) ** (2 * kin["ap"])
    )


def holo_kn(kin: dict, y: np.ndarray) -> np.ndarray:
    """Holomorphic part (1 - y)^{a_-} (1 + y)^{a_+} (principal branch, |y| < 1)."""
    return (1 - y) ** kin["am"] * (1 + y) ** kin["ap"]


def wick_single_vec(kin: dict, y: np.ndarray) -> np.ndarray:
    """Vector F^mu(y) = -i a'/2 sum_{j != a} k_j^mu / (w_a - w_j), shape (D, ...)."""
    w = positions(y)
    return np.array(
        [
            -0.5j * ALPHA_P * sum(kin["k"][l][mu] / (w["a"] - w[l]) for l in "bcd")
            for mu in range(D)
        ]
    )


def integrand_single(kin: dict, eps: np.ndarray, q: np.ndarray) -> np.ndarray:
    """Full integrand, level-(1,1) input at a: KN-ghost x eps_{mu nu} F^mu Fbar^nu."""
    y = q / FOUR_B2
    f = wick_single_vec(kin, y)  # holomorphic, argument y
    fb = wick_single_vec(kin, np.conj(y))  # antiholomorphic: same function of ybar
    return kn_ghost(kin, y) * np.einsum("m...,mn,n...->...", f, eps, fb)


def holo_two(kin: dict, ea: np.ndarray, ec: np.ndarray, y: np.ndarray) -> np.ndarray:
    """y [F_a F_c - a'/2 e_a.e_c / (w_a - w_c)^2], two level-one inputs (084 (1.6))."""
    w = positions(y)
    eaec = ea @ np.linalg.inv(ETA) @ ec  # lower-index polarisations
    return y * (
        osc(kin, "a", ea, w) * osc(kin, "c", ec, w)
        - 0.5 * ALPHA_P * eaec / (w["a"] - w["c"]) ** 2
    )


def holo_level2(kin: dict, e1, e2, e3, y: np.ndarray) -> np.ndarray:
    """Leading Wick term of a level-2 holomorphic excitation at a: (e1.dX)(e2.dX) + e3.d^2X."""
    w = positions(y)
    return osc(kin, "a", e1, w) * osc(kin, "a", e2, w) + osc(kin, "a", e3, w, n=2)


# ---------------------------------------------------------------------------
# Kinematic points (h0, a_-, a_+), conservation h0 = -(a_- + a_+)
# ---------------------------------------------------------------------------
PTS = {
    "A": (-0.45, -0.35, 0.8),  # 079's point A: tachyons absolutely convergent
    "G": (
        -1.5,
        0.2,
        1.3,
    ),  # alpha_eff = -0.8 for one (1,1) input; y = -1 term subleading
    "M": (1.4, -0.7, -0.7),  # tachyons abs. conv.; excited midpoint h0 + 2 = 3.4
}
KIN = {
    lab: make_kin(h0, am, SEED + i) for i, (lab, (h0, am, ap)) in enumerate(PTS.items())
}
for lab, kin in KIN.items():
    assert abs(kin["ap"] - PTS[lab][2]) < 1e-10
EPS = {
    lab: transverse_tensor(KIN[lab]["k"]["a"], SEED + 10 + i)
    for i, lab in enumerate(PTS)
}
for lab in PTS:
    kin, eps = KIN[lab], EPS[lab]
    note(
        f"[{lab}] (h0, a_-, a_+) = ({kin['h0']:.3f}, {kin['am']:.3f}, {kin['ap']:.3f}); "
        f"eps.k_c (both slots) = {np.abs(eps.T @ kin['k']['c']).max():.3f}, "
        f"k_c eps k_c = {kin['k']['c'] @ eps @ kin['k']['c']:.4f}, "
        f"k_d eps k_d = {kin['k']['d'] @ eps @ kin['k']['d']:.4f}"
    )

# ---------------------------------------------------------------------------
# C1.2 -- exponent of the full integrand at the cross-channel collisions
# ---------------------------------------------------------------------------
print("\n# C1.2 OPE exponent at y -> +-1")
kin = KIN["A"]
eps = EPS["A"]
ea = transverse_vector(kin["k"]["a"], SEED + 21)
eab = transverse_vector(kin["k"]["a"], SEED + 22)
ec = transverse_vector(kin["k"]["c"], SEED + 23)
ecb = transverse_vector(kin["k"]["c"], SEED + 24)
e1, e2, e3 = (rng.normal(size=D) for _ in range(3))
e1b, e2b, e3b = (rng.normal(size=D) for _ in range(3))


def full_two(y: np.ndarray) -> np.ndarray:
    """Two level-one inputs at a and c (product polarisations), full integrand."""
    return (
        kn_ghost(kin, y)
        * holo_two(kin, ea, ec, y)
        * holo_two(kin, eab, ecb, np.conj(y))
    )


def full_level2(y: np.ndarray) -> np.ndarray:
    """Level-(2,2) input at a, leading Wick term, full integrand."""
    return (
        kn_ghost(kin, y)
        * holo_level2(kin, e1, e2, e3, y)
        * holo_level2(kin, e1b, e2b, e3b, np.conj(y))
    )


CASES = {
    "level 0": (lambda y: kn_ghost(kin, y), 0),
    "(1,1) at a": (lambda y: integrand_single(kin, eps, y * FOUR_B2), 1),
    "(1,1) at a and c": (full_two, 2),
    "(2,2) at a": (full_level2, 2),
}
deltas = np.array([1e-3, 1e-4, 1e-5, 1e-6])
ok_all = True
for name, (fun, ntot) in CASES.items():
    for y0, a_ex in ((1.0, kin["am"]), (-1.0, kin["ap"])):
        sls = []
        for phi in (0.4, 1.9, 3.0):  # approach directions
            yy = y0 * (1 - deltas * np.exp(1j * phi))
            sls.append(slope(deltas, np.abs(fun(yy))))
        pred = 2 * (a_ex - ntot)
        ok = all(abs(s_ - pred) < 1e-3 for s_ in sls)
        if ntot > 0:  # break leg: the tachyon exponent is rejected
            ok &= all(abs(s_ - 2 * a_ex) > 1.0 for s_ in sls)
        ok_all &= ok
        note(
            f"[{name}, y -> {y0:+.0f}] local exponent {np.round(sls, 5)} "
            f"vs 2(a - N_tot) = {pred:+.4f} (tachyon {2 * a_ex:+.4f})"
        )
report(
    "C1.2-exponent",
    ok_all,
    "|1 -+ y|^{2(a_-+ - N_tot)} at the cross-channel collisions",
)

# C1.3: first subleading term of eps.Phi near y = 1 (084 (1.5)), vector eps_{mu nu} Phi^mu
kc = kin["k"]["c"]
u = rng.normal(size=D)  # contract the second slot with a random vector
vc = (kc @ eps) @ u
ok = True
for dl in (1e-2, 5e-3, 2.5e-3):
    yv = np.array([1 - dl * np.exp(0.7j)])
    phi_vec = holo_kn(kin, yv) * wick_single_vec(kin, yv) / (-0.25j * ALPHA_P / BETA)
    lhs = (
        (phi_vec[:, 0] @ eps @ u)
        * (1 - yv[0]) ** (1 - kin["am"])
        / (2 ** kin["ap"] * vc)
    )
    pred = 1 - (1 + kin["ap"]) / 2 * (1 - yv[0])
    wrong = 1 - (1 + kin["am"]) / 2 * (1 - yv[0])
    err, err_w = abs(lhs - pred), abs(lhs - wrong)
    ok &= bool(err < 3 * dl**2 * 10 and err_w > 10 * err)
    note(f"[(1.5) delta={dl}] |lhs - pred| = {err:.2e}, |lhs - wrong| = {err_w:.2e}")
report(
    "C1.3-subleading",
    ok,
    "eps.Phi = 2^{a_+} eps.k_c (1-y)^{a_- - 1}[1 - (1+a_+)(1-y)/2 + ...]",
)

# ---------------------------------------------------------------------------
# C2 -- sector coefficients: series route, FFT cross-check, Darboux growth
# ---------------------------------------------------------------------------
print("\n# C2 sector coefficients")
NMAX = 1700
PREF = -(ALPHA_P**2) / (16 * B2)  # F^mu Fbar^nu = PREF P^mu(y) P^nu(ybar), 084 (1.4)


def single_series(kin: dict, eps: np.ndarray, nmax: int) -> tuple[np.ndarray, list]:
    """
    Series route for one level-(1,1) input at a (084 (1.4)).

    Phi^mu(y) = k_b^mu/2 g[a_-, a_+] + k_c^mu g[a_- - 1, a_+] + k_d^mu g[a_-, a_+ - 1];
    c_{N Nbar} = PREF sum_{XY} E_{XY} g^X_N g^Y_Nbar, E_{XY} = khat_X eps khat_Y.

    Returns:
        tuple: (E matrix 3x3 including PREF, [g^b, g^c, g^d]).

    """
    am, ap = kin["am"], kin["ap"]
    gs = [
        g_coeffs(am, ap, nmax),
        g_coeffs(am - 1, ap, nmax),
        g_coeffs(am, ap - 1, nmax),
    ]
    kh = [kin["k"]["b"] / 2, kin["k"]["c"], kin["k"]["d"]]
    E = PREF * np.array([[kx @ eps @ ky for ky in kh] for kx in kh])
    return E, gs


def poly_two(kin: dict, ea: np.ndarray, ec: np.ndarray) -> np.ndarray:
    """Coefficients of Q(y) = (1 - y^2)^2 holo_two(y), a polynomial (sympy, exact in y)."""
    y = sp.Symbol("y")
    b = sp.Rational(3, 2)
    w = {"a": 2 * b, "b": -2 * b, "c": 2 * b * y, "d": -2 * b * y}

    def F(j: str, e: np.ndarray):
        return (
            -sp.I
            * sp.Rational(ALPHA_P)
            / 2
            * sum(
                sp.Rational(float(e @ kin["k"][l])) / (w[j] - w[l])
                for l in "abcd"
                if l != j
            )
        )

    eaec = sp.Rational(float(ea @ ETA @ ec))  # exact binary rationals: cancel is exact
    ap_ = sp.Rational(ALPHA_P)
    h = y * (F("a", ea) * F("c", ec) - ap_ / 2 * eaec / (w["a"] - w["c"]) ** 2)
    qy = sp.Poly(sp.cancel(sp.together(h * (1 - y**2) ** 2)), y)
    return np.array([complex(cf) for cf in reversed(qy.all_coeffs())])


def conv_poly(qc: np.ndarray, g: np.ndarray) -> np.ndarray:
    """Taylor coefficients of Q(y) * sum g_N y^N, truncated to len(g)."""
    out = np.zeros(len(g), complex)
    for k, qk in enumerate(qc):
        out[k:] += qk * g[: len(g) - k]
    return out


def fft_coeffs(fun, nmax: int, r: float = 0.9, m: int = 4096) -> np.ndarray:
    """[y^N] of a function holomorphic in |y| < 1 by FFT on |y| = r (Cauchy)."""
    z = r * np.exp(2j * np.pi * np.arange(m) / m)
    c = np.fft.fft(fun(z), axis=-1) / m
    return c[..., : nmax + 1] / r ** np.arange(nmax + 1)


SER = {lab: single_series(KIN[lab], EPS[lab], NMAX) for lab in PTS}
# two level-one inputs at a and c, at point A
kinA = KIN["A"]
QH = poly_two(kinA, ea, ec)
QA = poly_two(kinA, eab, ecb)
g22 = g_coeffs(kinA["am"] - 2, kinA["ap"] - 2, NMAX)
GH2 = conv_poly(QH, g22)
GA2 = conv_poly(QA, g22)

# C2.1: series route vs FFT of the raw Wick factor
ok = True
for lab in PTS:
    kin = KIN[lab]
    E, gs = SER[lab]
    vec_series = (
        np.outer(kin["k"]["b"] / 2, gs[0][:61])
        + np.outer(kin["k"]["c"], gs[1][:61])
        + np.outer(kin["k"]["d"], gs[2][:61])
    )
    vec_fft = fft_coeffs(
        lambda z, kin=kin: (
            holo_kn(kin, z) * wick_single_vec(kin, z) / (-0.25j * ALPHA_P / BETA)
        ),
        60,
    )
    err = np.abs(vec_series - vec_fft).max() / np.abs(vec_series).max()
    ok &= bool(err < 1e-9)
    note(f"[{lab} single] series vs FFT, N <= 60: max rel. error {err:.1e}")
for name, gser, ee, ec_ in (("holo", GH2, ea, ec), ("antiholo", GA2, eab, ecb)):
    ff = fft_coeffs(
        lambda z, ee=ee, ec_=ec_: holo_kn(kinA, z) * holo_two(kinA, ee, ec_, z), 60
    )
    err = np.abs(gser[:61] - ff).max() / np.abs(gser[:61]).max()
    ok &= bool(err < 1e-9)
    note(f"[A two level-one, {name}] series vs FFT, N <= 60: max rel. error {err:.1e}")
report("C2.1-coeffs", ok, "series route = FFT of the raw Wick factor (N <= 60)")


def cmat_diag(E: np.ndarray, gs: list, m: int, ns: np.ndarray) -> np.ndarray:
    """c_{N, N-m} = sum_XY E_XY g^X_N g^Y_{N-m} at the given N."""
    return sum(
        E[x, yy] * gs[x][ns] * gs[yy][ns - m] for x in range(3) for yy in range(3)
    )


# C2.2: fixed-m growth, single (1,1) input and two level-one inputs
ok = True
NF = np.arange(800, 1601, 50)
NL = np.arange(30, 61, 2)
for lab in PTS:
    kin = KIN[lab]
    E, gs = SER[lab]
    a_eff = min(kin["am"], kin["ap"]) - 1
    alpha = min(kin["am"], kin["ap"])
    for m in (0, 2, 4):
        c = np.abs(cmat_diag(E, gs, m, NF))
        sl = slope(NF.astype(float), c)
        sl_low = slope(NL.astype(float), np.abs(cmat_diag(E, gs, m, NL)))
        pred = -2 * a_eff - 2
        ok &= bool(abs(sl - pred) < 0.05 and abs(sl - (-2 * alpha - 2)) > 1.0)
        note(
            f"[{lab} single m={m}] slope N in [800,1600] {sl:+.4f}, N in [30,60] {sl_low:+.3f}; "
            f"pred -2 a_eff - 2 = {pred:+.3f} (tachyon {-2 * alpha - 2:+.3f})"
        )
# Darboux amplitude at A (y = 1 singularity of g[a_- - 1, a_+] squared, coefficient E_cc)
kin = KIN["A"]
E, gs = SER["A"]
bexp = kin["am"] - 1
ratios = []
for n_ in (200, 400, 800, 1600):
    lead = 2 ** kin["ap"] * float(
        mp.exp(mp.loggamma(n_ - bexp) - mp.loggamma(n_ + 1)) / mp.gamma(-bexp)
    )
    lead_m = 2 ** kin["ap"] * float(
        mp.exp(mp.loggamma(n_ - 4 - bexp) - mp.loggamma(n_ - 4 + 1)) / mp.gamma(-bexp)
    )
    ratios.append(cmat_diag(E, gs, 4, np.array([n_]))[0] / (E[1, 1] * lead * lead_m))
ratios = np.array(ratios)
ok &= bool(abs(ratios[-1] - 1) < 1e-2 and abs(ratios[-1] - 1) < abs(ratios[0] - 1))
note(f"[A single m=4] c / Darboux leading at N=200..1600: {np.round(ratios, 5)}")
for m in (0, 2, 4):
    c = np.abs(GH2[NF] * GA2[NF - m])
    sl = slope(NF.astype(float), c)
    pred = -2 * (min(kinA["am"], kinA["ap"]) - 2) - 2
    ok &= bool(abs(sl - pred) < 0.05)
    note(f"[A two level-one m={m}] slope {sl:+.4f} vs -2 a_eff - 2 = {pred:+.3f}")
report(
    "C2.2-darboux-m",
    ok,
    "fixed-m |c_{h,m}|(4b^2)^h ~ h^{-2 alpha_eff - 2}, alpha_eff = alpha - N_tot",
)


def level_terms_c(a: np.ndarray, b: np.ndarray, theta: float, nmax: int) -> np.ndarray:
    """sum_{N+Nbar=n} a_N b_Nbar e^{i(N-Nbar) theta} (complex)."""
    t = np.zeros(nmax + 1, complex)
    for n in range(nmax + 1):
        nn = np.arange(n + 1)
        t[n] = np.dot(a[nn] * b[n - nn], np.exp(1j * (2 * nn - n) * theta))
    return t


# C2.3: fixed theta on the fold arc (80 deg) and at the arc midpoint
ok = True
NT = 1600
centres = [200, 400, 800, 1500]
for lab in ("A", "M"):
    kin = KIN[lab]
    E, gs = SER[lab]
    a_eff = min(kin["am"], kin["ap"]) - 1
    for thdeg, pred in ((80.0, -a_eff - 1), (90.0, kin["h0"] + 2 - 1)):
        th = np.deg2rad(thdeg)
        t = sum(
            E[x, yy] * level_terms_c(gs[x], gs[yy], th, NT)
            for x in range(3)
            for yy in range(3)
        )
        env = rms_envelope(t, centres, 60)
        sl = slope(np.array(centres[1:], float), env[1:])
        ok &= bool(abs(sl - pred) < 0.06)
        note(f"[{lab} theta={thdeg}] envelope slope {sl:+.4f} vs predicted {pred:+.4f}")
report(
    "C2.3-darboux-theta",
    ok,
    "T_n ~ n^{-alpha_eff-1} on the arc, n^{h0+2N_tot-1} at pi/2",
)

# ---------------------------------------------------------------------------
# Geometry: copied verbatim from codes/verify-fold-arc-convergence.py (not edited)
# ---------------------------------------------------------------------------
TH1 = float(np.arccos(2 * 16 / 25 - 1))  # 73.74 deg, fold-arc endpoint


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


def win_env(e: np.ndarray, half: int) -> np.ndarray:
    """Windowed max of |e| over [k - half, k + half] (envelope of an oscillating error)."""
    a = np.abs(e)
    return np.array([a[max(0, k - half) : k + half + 1].max() for k in range(len(a))])


def direct_integral_f(fun, nr: int = 48) -> float:
    """
    J = int_{Q_V} I ds dtheta for an integrand I(q) (complex allowed).

    sigma_V is even and pi-periodic, so theta in [0, pi/2] with the four images
    q, -q, conj(q), -conj(q); the imaginary part must cancel (asserted).
    """
    xr, wr = np.polynomial.legendre.leggauss(nr)
    tot = 0.0 + 0.0j
    for ths, ws, sv in (
        (TH_OFF, W_OFF, LN4B2 - RHO_OFF),
        (TH_ARC, W_ARC, np.full(TH_ARC.shape, LN4B2)),
    ):
        sig = np.outer(sv / 2, xr + 1)
        wsig = np.outer(sv / 2, wr)
        q = np.exp(sig + 1j * ths[:, None])
        val = fun(q) + fun(-q) + fun(np.conj(q)) + fun(-np.conj(q))
        tot += np.sum(ws[:, None] * wsig * val)
    assert abs(tot.imag) < 1e-9 * max(1.0, abs(tot.real)), tot
    return float(tot.real)


HMAX = 1600
NS = np.arange(0, HMAX + 1, 2)
MS = np.arange(0, HMAX + 1, 2)


def sums(h0: float, E: np.ndarray, gs: list, J: float) -> dict:
    """
    Level, absolute and sector partial sums of sum c_{h,m} fhat_m(h) (079 (2.1)).

    term(n, m) = sum_XY E_XY [g^X_N g^Y_Nbar + (m > 0) g^X_Nbar g^Y_N] F_m(h) / h,
    with the -2 pi delta_{m0} (4 b^2)^{-h} of the m = 0 transform.
    """
    hs = h0 + NS
    if np.any(np.isclose(hs, 0.0)):
        raise ValueError(f"h0 = {h0}: h = 0 at an even level")
    Ft = fhat_table(MS, hs)
    Ft[0] -= 2 * np.pi * FOUR_B2 ** (-hs)
    term = np.zeros((len(MS), len(NS)))
    k = len(gs)
    for j, n in enumerate(NS):
        mm = MS[MS <= n]
        nb, nn = (n - mm) // 2, (n + mm) // 2
        c = sum(E[x, y_] * gs[x][nn] * gs[y_][nb] for x in range(k) for y_ in range(k))
        cr = sum(E[x, y_] * gs[x][nb] * gs[y_][nn] for x in range(k) for y_ in range(k))
        tot = np.where(mm == 0, c, c + cr)
        term[: len(mm), j] = np.real(tot) * Ft[: len(mm), j] / hs[j]
    return dict(
        level=np.cumsum(term.sum(axis=0)),
        absolute=np.cumsum(np.abs(term).sum(axis=0)),
        sector=np.cumsum(term, axis=1),
        J=J,
    )


print("\n# C2.4 level zero reproduces 079")
REF079 = {  # 079 run-fix.log: J, S(400), S(800), S(1600)
    "A": (
        (-0.45, -0.35, 0.8),
        (17.1479252597, 17.1479254303, 17.1479252817, 17.1479252599),
    ),
    "onshell": (
        (0.2, -0.4, 0.2),
        (6.1497650597, 6.1497652060, 6.1497650902, 6.1497650631),
    ),
}
ok = True
for lab, ((h0, am, ap), ref) in REF079.items():
    kin0 = dict(h0=h0, am=am, ap=ap)
    J = direct_integral_f(lambda q, kin0=kin0: kn_ghost(kin0, q / FOUR_B2))
    S = sums(h0, np.array([[1.0]]), [g_coeffs(am, ap, HMAX)], J)
    got = (J, S["level"][200], S["level"][400], S["level"][800])
    dev = max(abs(a - b) for a, b in zip(got, ref))
    ok &= bool(dev < 2e-10)
    note(
        f"[{lab}] (J, S(400), S(800), S(1600)) = {np.round(got, 10)}; max |dev| from 079 = {dev:.1e}"
    )
report(
    "C2.4-level-zero", ok, "the generalised pipeline at level zero gives 079's numbers"
)

# ---------------------------------------------------------------------------
# C3 -- integrated sums for one level-(1,1) input
# ---------------------------------------------------------------------------
print("\n# C3 integrated sums, one (1,1) input at a")
SUMS = {}
for lab in PTS:
    kin, eps = KIN[lab], EPS[lab]
    E, gs = SER[lab]
    J = direct_integral_f(lambda q, kin=kin, eps=eps: integrand_single(kin, eps, q))
    S = sums(kin["h0"], E, [g[: HMAX + 1] for g in gs], J)
    J0 = direct_integral_f(lambda q, kin=kin: kn_ghost(kin, q / FOUR_B2))
    S0 = sums(kin["h0"], np.array([[1.0]]), [g_coeffs(kin["am"], kin["ap"], HMAX)], J0)
    SUMS[lab] = (S, S0)
    note(
        f"[{lab}] excited: J = {J:.10f}, S(400,800,1600) = {S['level'][200]:.10f} "
        f"{S['level'][400]:.10f} {S['level'][800]:.10f}; sector m=4 "
        f"{S['sector'][2, 200]:.4e} {S['sector'][2, 400]:.4e} {S['sector'][2, 800]:.4e}"
    )
    note(
        f"[{lab}] tachyons, same momenta: J = {J0:.10f}, S(1600) = {S0['level'][800]:.10f}; "
        f"sector m=4 {S0['sector'][2, 200]:.6e} {S0['sector'][2, 800]:.6e}"
    )
Hs = NS
iw = (Hs >= 400) & (Hs <= 1600)

# C3.2-sector-divergence: A: tachyons absolutely convergent, excited alpha_eff = -1.35: sectors diverge
S, S0 = SUMS["A"]
kin = KIN["A"]
a_eff = min(kin["am"], kin["ap"]) - 1
ok = True
for mi in (0, 1, 2):
    sl = slope(Hs[iw].astype(float), np.abs(S["sector"][mi, iw]))
    ok &= bool(abs(sl - (-2 * a_eff - 2)) < 0.08)
    note(
        f"[A excited m={2 * mi}] |F_m(H)| slope {sl:+.3f} vs -2 a_eff - 2 = {-2 * a_eff - 2:+.3f}"
    )
lev_err = abs(S["level"][-1] - S["J"]) / abs(S["J"])
ok &= bool(lev_err < 1e-4)
brk = (
    abs(S0["sector"][2, -1] / S0["sector"][2, 200] - 1) < 1e-2
    and abs(S0["level"][-1] - S0["J"]) < 1e-8 * S0["J"]
)
note(
    f"[A excited] level order |S(1600)-J|/|J| = {lev_err:.1e}; tachyon sector stationary: {brk}"
)
report(
    "C3.2-sector-divergence",
    bool(ok and brk),
    "excited input moves A from every-order to level-order convergence",
)

# C3.2-absolute: G: alpha_eff = -0.8 > -1: every order
S, S0 = SUMS["G"]
kin = KIN["G"]
a_eff = min(kin["am"], kin["ap"]) - 1
err = abs(S["level"][-1] - S["J"]) / abs(S["J"])
inc = np.array(
    [abs(S["sector"][2, k] - S["sector"][2, k // 2]) for k in (200, 400, 800)]
)
sl_sec = np.log(inc[-1] / inc[0]) / np.log(4)
inc_a = np.array([S["absolute"][k] - S["absolute"][k // 2] for k in (200, 400, 800)])
sl_abs = np.log(inc_a[-1] / inc_a[0]) / np.log(4)
ok = bool(err < 1e-6 and abs(sl_sec - (-2 * a_eff - 2)) < 0.15 and sl_abs < -0.2)
note(
    f"[G excited] |S(1600)-J|/|J| = {err:.1e}; sector m=4 increment slope {sl_sec:+.3f} "
    f"(pred {-2 * a_eff - 2:+.3f}); absolute-series increment slope {sl_abs:+.3f}"
)
report("C3.2-absolute", ok, "alpha_eff > -1: absolutely convergent to J")

# C3.2-midpoint: M: tachyons absolutely convergent; excited midpoint exponent h0 + 2 = 3.4 >= 3
S, S0 = SUMS["M"]
kin = KIN["M"]
a_eff = min(kin["am"], kin["ap"]) - 1
p_mid, p_end = kin["h0"] + 2 - 3, -a_eff - 3
e = win_env(S["level"] - S["J"], 25)
sl = slope(Hs[iw].astype(float), e[iw])
e0 = abs(S0["level"][-1] - S0["J"]) / S0["J"]
# tachyons at the same momenta: alpha = -0.7 > -1; terms n^{h0-3} = n^{-1.6} (midpoint)
# and n^{-alpha-3} = n^{-2.3} (endpoints) compete at H <= 1600 (as 079's point B), so
# this leg tests convergence only: slope in [-2.3 - 0.1, -1.6 + 0.1].
sl0 = slope(Hs[iw].astype(float), win_env(S0["level"] - S0["J"], 25)[iw])
ok = bool(
    sl > 0.2
    and abs(sl - p_mid) < 0.1
    and abs(sl - p_end) > 0.3
    and (-min(kin["am"], kin["ap"]) - 3 - 0.1 < sl0 < kin["h0"] - 3 + 0.1)
)
note(
    f"[M excited] level-order error envelope slope {sl:+.3f} (pred midpoint h0+2N-3 = {p_mid:+.3f}, "
    f"endpoint {p_end:+.3f}); tachyons same momenta |S(1600)-J|/J = {e0:.1e}, "
    f"error slope {sl0:+.3f} (pred h0-3 = {kin['h0'] - 3:+.3f})"
)
report("C3.2-midpoint", ok, "midpoint threshold shifts by 2 N_tot: h0 + 2 N_tot < 3")

# ---------------------------------------------------------------------------
# C3.5 -- counterexample to the withdrawn unbalanced criterion (3.3) (critic-084 #2)
# ---------------------------------------------------------------------------
print("\n# C3.5 crossed rank-one level-(1,1) polarisations at a and b")


def perp(ks: list[np.ndarray], seed: int) -> np.ndarray:
    """Random lower-index vector e with e.k = e_mu k^mu = 0 for every k in ks."""
    r = np.random.default_rng(seed)
    e = r.normal(size=D)
    gram = np.array([[dot(ki, kj) for kj in ks] for ki in ks])
    x = np.linalg.solve(gram, np.array([e @ k for k in ks]))
    e = e - sum(xi * (ETA @ ki) for xi, ki in zip(x, ks))
    assert max(abs(e @ k) for k in ks) < 1e-10
    return e


def holo_pair(kin: dict, i: str, ei: np.ndarray, j: str, ej: np.ndarray, y):
    """
    Level-one inputs at i and j in copy 1: F_i F_j - a'/2 e_i.e_j / (w_i - w_j)^2.

    holo_two without the copy-2 Jacobian factor y (both punctures in copy 1).
    """
    w = positions(y)
    eiej = ei @ np.linalg.inv(ETA) @ ej
    return (
        osc(kin, i, ei, w) * osc(kin, j, ej, w)
        - 0.5 * ALPHA_P * eiej / (w[i] - w[j]) ** 2
    )


# a_- = a_+ = 1/4, h0 = -1/2; level-(1,1) inputs at a and b, rank-one polarisations
# u_a (x) v_a and u_b (x) v_b with u_a perp k_a, k_d; v_a perp k_a, k_c;
# u_b perp k_b, k_c; v_b perp k_b, k_d.  Pole orders (nu_-, nu_+, nubar_-, nubar_+)
# = (2, 0, 0, 2): alpha^L = (-7/4, 1/4), alpha^R = (1/4, -7/4).
kx = make_kin(-0.5, 0.25, SEED + 50)
kk_ = kx["k"]
ua = perp([kk_["a"], kk_["d"]], SEED + 51)
va = perp([kk_["a"], kk_["c"]], SEED + 52)
ub = perp([kk_["b"], kk_["c"]], SEED + 53)
vb = perp([kk_["b"], kk_["d"]], SEED + 54)
am5, ap5 = kx["am"], kx["ap"]


def hol5(y):
    """Holomorphic factor (1-y)^{a_-} (1+y)^{a_+} x Wick(u_a, u_b)."""
    return holo_kn(kx, y) * holo_pair(kx, "a", ua, "b", ub, y)


def ahol5(y):
    """Antiholomorphic factor as a function of ybar: same with (v_a, v_b)."""
    return holo_kn(kx, y) * holo_pair(kx, "a", va, "b", vb, y)


ok = True
# (i) local exponents at y -> +-1 of the raw Wick factors
dl = np.array([1e-3, 1e-4, 1e-5])
exps = {}
for nm, f in (("hol", hol5), ("ahol", ahol5)):
    for pt in (1, -1):
        v = np.abs(f(pt * (1 - dl)))
        exps[(nm, pt)] = slope(dl, v)
pred = {
    ("hol", 1): am5 - 2,
    ("hol", -1): ap5,
    ("ahol", 1): am5,
    ("ahol", -1): ap5 - 2,
}
dev = max(abs(exps[k] - pred[k]) for k in pred)
ok &= bool(dev < 1e-3)
note(
    "pole orders (2,0,0,2): local exponents "
    + ", ".join(f"{k[0]}@{k[1]:+d} {exps[k]:+.4f} (pred {pred[k]:+.2f})" for k in pred)
)
# (ii) series route: Q(y) = Wick(u) (1-y)^2, Qt(y) = Wick(v) (1+y)^2 are quadratic
zq = 0.5 * np.exp(2j * np.pi * np.arange(16) / 16)
qc = (
    np.fft.fft(holo_pair(kx, "a", ua, "b", ub, zq) * (1 - zq) ** 2)
    / 16
    / 0.5 ** np.arange(16)
)
qtc = (
    np.fft.fft(holo_pair(kx, "a", va, "b", vb, zq) * (1 + zq) ** 2)
    / 16
    / 0.5 ** np.arange(16)
)
quad = max(
    np.abs(qc[3:]).max() / np.abs(qc[:3]).max(),
    np.abs(qtc[3:]).max() / np.abs(qtc[:3]).max(),
)
ok &= bool(quad < 1e-10)
G5 = conv_poly(qc[:3], g_coeffs(am5 - 2, ap5, NMAX))
Gt5 = conv_poly(qtc[:3], g_coeffs(am5, ap5 - 2, NMAX))
ff = fft_coeffs(hol5, 60)
fft_err = np.abs(G5[:61] - ff).max() / np.abs(ff).max()
fft_err = max(
    fft_err, np.abs(Gt5[:61] - fft_coeffs(ahol5, 60)).max() / np.abs(ff).max()
)
ok &= bool(fft_err < 1e-10)
note(
    f"Q, Qt quadratic (rel. higher coeffs {quad:.1e}); series vs FFT, N <= 60: {fft_err:.1e}"
)
# (iii) fixed-m sector terms [c_{N,Nbar} + c_{Nbar,N}] F_m(h) / h, h = h0 + n
hs5 = kx["h0"] + NS
ms5 = np.array([0, 2, 4])
Ft5 = fhat_table(ms5, hs5)
Ft5[0] -= 2 * np.pi * FOUR_B2 ** (-hs5)
g0 = g_coeffs(am5, ap5, NMAX)  # break leg: tachyons at the same momenta
p_cross = -(am5 - 2 + ap5 - 2) - 3  # -(alpha^L_- + alpha^R_+) - 3 = +1/2
p_same = -(am5 - 2 + am5) - 3  # withdrawn (3.3): -(alpha^L_- + alpha^R_-) - 3 = -3/2
p_tach = -2 * min(am5, ap5) - 3
iw5 = (NS >= 400) & (NS <= 1600)
for mi, m in enumerate(ms5):
    nn, nb = (NS[NS >= m] + m) // 2, (NS[NS >= m] - m) // 2
    sel = NS >= m
    c = G5[nn] * Gt5[nb] + (m > 0) * G5[nb] * Gt5[nn]
    term = c * Ft5[mi, sel] / hs5[sel]
    c0 = g0[nn] * g0[nb] * (1 + (m > 0))
    term0 = c0 * Ft5[mi, sel] / hs5[sel]
    w5 = iw5[sel]
    nf = NS[sel][w5].astype(float)
    sl_t = slope(nf, np.abs(term[w5]))
    alt = float(np.mean(np.real(term[w5][1:] / term[w5][:-1])))
    # swing of the partial sums S_m(H) about their local mean (alternating terms)
    ps = np.cumsum(term)
    swing = np.array(
        [
            np.abs(
                ps[max(0, k - 25) : k + 26] - ps[max(0, k - 25) : k + 26].mean()
            ).max()
            for k in range(len(ps))
        ]
    )
    sl_s = slope(nf, swing[w5])
    # tachyons: a_- = a_+ makes odd-N coefficients vanish; windowed max of |term0|
    sl_0 = slope(nf, win_env(term0, 25)[w5])
    ok &= bool(
        abs(sl_t - p_cross) < 0.1
        and abs(sl_t - p_same) > 1.0
        and alt < -0.95
        and abs(sl_s - p_cross) < 0.1
        and sl_0 < -2.0
    )
    note(
        f"[m={m}] |term| slope {sl_t:+.3f} (cross pred {p_cross:+.2f}; withdrawn (3.3) "
        f"{p_same:+.2f}); mean Re(term_n+2/term_n) = {alt:+.3f}; partial-sum swing "
        f"slope {sl_s:+.3f}; break: tachyon |term| slope {sl_0:+.3f} (pred {p_tach:+.2f})"
    )
report(
    "C3.5-counterexample",
    ok,
    "crossed (2,0,0,2) poles: sector terms ~ (-1)^N h^{1/2}, sector sums diverge",
)

# ---------------------------------------------------------------------------
# C4.1 -- on-shell reading (sympy, exact)
# ---------------------------------------------------------------------------
print("\n# C4.1 on-shell exponents")
ap_, s_, t_, u_ = sp.symbols("alpha_p s t u", positive=True)
Na, Nb, Nc, Nd = sp.symbols("N_a N_b N_c N_d", nonnegative=True, integer=True)
Ntot = Na + Nb + Nc + Nd
k2 = {
    "a": 4 * (1 - Na) / ap_,
    "b": 4 * (1 - Nb) / ap_,
    "c": 4 * (1 - Nc) / ap_,
    "d": 4 * (1 - Nd) / ap_,
}
# k_i.k_j from Mandelstams: s = -(k_c+k_d)^2 = -(k_a+k_b)^2, t = -(k_a+k_c)^2 = -(k_b+k_d)^2, u = -(k_a+k_d)^2 = -(k_b+k_c)^2


def kk(i: str, j: str, m: sp.Expr, k2m: dict | None = None) -> sp.Expr:
    """k_i.k_j from -(k_i + k_j)^2 = m (masses k2m, default the on-shell k2)."""
    k2m = k2 if k2m is None else k2m
    return (-m - k2m[i] - k2m[j]) / 2


am_os = 1 + ap_ / 2 * (kk("a", "c", t_) + kk("b", "d", t_))
apl_os = 1 + ap_ / 2 * (kk("a", "d", u_) + kk("b", "c", u_))
h0_os = ap_ / 2 * (-s_) - 2
# conservation: sum_i k_i^2 + 2 sum_{i<j} k_i.k_j = 0 fixes s + t + u
cons = sum(k2.values()) + 2 * (
    kk("a", "b", s_)
    + kk("c", "d", s_)
    + kk("a", "c", t_)
    + kk("b", "d", t_)
    + kk("a", "d", u_)
    + kk("b", "c", u_)
)
stu = sp.solve(sp.Eq(cons, 0), s_)[0]
c1 = sp.simplify(am_os - Ntot - (-3 - ap_ * t_ / 2)) == 0
c2 = sp.simplify(apl_os - Ntot - (-3 - ap_ * u_ / 2)) == 0
c3 = sp.simplify(ap_ * (stu + t_ + u_) - (-16 + 4 * Ntot)) == 0
c4 = sp.simplify((am_os + apl_os + h0_os).subs(s_, stu)) == 0
# break leg (critic-084 #10): with the wrong mass shell alpha' k^2 = 4 (1 + N) the
# levels must not cancel, so the same identity has to fail
k2_bad = {j: 4 * (1 + Nj) / ap_ for j, Nj in zip("abcd", (Na, Nb, Nc, Nd))}
am_bad = 1 + ap_ / 2 * (kk("a", "c", t_, k2_bad) + kk("b", "d", t_, k2_bad))
brk = sp.simplify(am_bad - Ntot - (-3 - ap_ * t_ / 2)) != 0
note(
    f"a_- - N_tot = -3 - a't/2: {c1}; a_+ - N_tot = -3 - a'u/2: {c2}; a'(s+t+u) = -16 + 4 N_tot: {c3}; a_- + a_+ + h0 = 0: {c4}; break: {brk}"
)
report(
    "C4.1-onshell",
    bool(c1 and c2 and c3 and c4 and brk),
    "on shell the effective exponents are level independent in t, u",
)

# ---------------------------------------------------------------------------
# C4.3 -- parity-odd pairs: B at a and c, tachyons at b, d (critic-084 #4)
# ---------------------------------------------------------------------------
print("\n# C4.3 B-fields at a and c: no tachyon exchange in the u-channel")
kin = KIN["A"]
ETA_UP = np.linalg.inv(ETA)


def fvec(kin: dict, j: str, y: np.ndarray) -> np.ndarray:
    """F_j^mu(y) = -i a'/2 sum_{l != j} k_l^mu / (w_j - w_l), shape (D, ...)."""
    w = positions(y)
    return np.array(
        [
            -0.5j
            * ALPHA_P
            * sum(kin["k"][l][mu] / (w[j] - w[l]) for l in "abcd" if l != j)
            for mu in range(D)
        ]
    )


def hmat_ac(kin: dict, y: np.ndarray) -> np.ndarray:
    """H^{mu rho}(y) = F_a^mu F_c^rho - a'/2 eta^{mu rho} / (w_a - w_c)^2 (084 (1.1))."""
    w = positions(y)
    fa, fc = fvec(kin, "a", y), fvec(kin, "c", y)
    return np.einsum("m...,r...->mr...", fa, fc) - 0.5 * ALPHA_P * np.einsum(
        "mr,...->mr...", ETA_UP, 1 / (w["a"] - w["c"]) ** 2
    )


def full_ac(kin: dict, ea: np.ndarray, ec: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Level-(1,1) inputs at a and c: KN x |y|^2 x ea_{mu nu} ec_{rho sigma} H^{mu rho}(y) H^{nu sigma}(ybar)."""
    h, hb = hmat_ac(kin, y), hmat_ac(kin, np.conj(y))
    return (
        kn_ghost(kin, y)
        * np.abs(y) ** 2
        * np.einsum("mn,rs,mr...,ns...->...", ea, ec, h, hb)
    )


def antisym(t: np.ndarray) -> np.ndarray:
    """Antisymmetric part (keeps transversality on both slots)."""
    return (t - t.T) / 2


def symm(t: np.ndarray) -> np.ndarray:
    """Symmetric part."""
    return (t + t.T) / 2


Ba = antisym(transverse_tensor(kin["k"]["a"], SEED + 61))
Bc = antisym(transverse_tensor(kin["k"]["c"], SEED + 62))
Sa = symm(transverse_tensor(kin["k"]["a"], SEED + 63))
Sc = symm(transverse_tensor(kin["k"]["c"], SEED + 64))
dl = np.array([1e-3, 1e-4, 1e-5])
ok = True
res = {}
for lab, (ea_, ec_) in (("B", (Ba, Bc)), ("sym", (Sa, Sc))):
    for pt in (1, -1):
        v = np.mean(
            [
                np.abs(full_ac(kin, ea_, ec_, pt * (1 - dl * np.exp(1j * ph))))
                for ph in (0.3, 1.1, -0.7)
            ],
            axis=0,
        )
        res[(lab, pt)] = slope(dl, v)
pr = {
    ("B", 1): 2 * (kin["am"] - 2),
    ("B", -1): 2 * kin["ap"] - 2,
    ("sym", 1): 2 * (kin["am"] - 2),
    ("sym", -1): 2 * (kin["ap"] - 2),
}
ok = bool(
    max(abs(res[k] - pr[k]) for k in pr) < 2e-3
    and abs(res[("B", -1)] - pr[("sym", -1)]) > 1.0
)
note(
    ", ".join(f"{k[0]} y->{k[1]:+d}: {res[k]:+.4f} (pred {pr[k]:+.2f})" for k in pr)
    + f"; |B_a k_d k_d| = {abs(kin['k']['d'] @ Ba @ kin['k']['d']):.1e}"
)
report(
    "C4.3-parity-odd",
    ok,
    "B-T pairs: u-channel exponent 2 a_+ - 2 (spin-one exchange), not 2 (a_+ - N_tot)",
)

# ---------------------------------------------------------------------------
print()
nfail = sum(not ok_ for _, ok_ in RESULTS)
print(f"{len(RESULTS) - nfail}/{len(RESULTS)} PASS (seed {SEED})")
LOG.write(f"{len(RESULTS) - nfail}/{len(RESULTS)} PASS (seed {SEED})\n")
LOG.close()
sys.exit(1 if nfail else 0)
