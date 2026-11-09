"""
Companion checks for derivation record 074 (p_{2,2}^{-1} as a circle gluing).

What is verified:

- C1.3-star, C1.3-period, C1.3-area: at beta = 3/2 the preimage Q_V of
  V_{0,4} (= M'_x of record 032, the complement of the three V_3' Feynman
  regions) under the s-channel surface map Z(q) = (q + 4 beta^2)^2 / (16 beta^2 q)
  (R2) is star-shaped in log q: along every ray q = exp(sigma + i theta) the
  indicator of M'_x is 1 on (0, sigma_V(theta)) and 0 after, with no re-entry
  before |q| = 4 beta^2; sigma_V is pi-periodic; the pulled-back Euclidean area
  int_{Q_V} |q|^2 |Z'(q)|^2 dsigma dtheta reproduces the grid area of M'_x of
  record 032 (14.534), an independent route (ray marching in q vs a grid in Z);
  the two routes share the membership criterion min(|q_t|,|q_u|) > 1 and Z(q),
  so their agreement checks covering-once (injectivity / Jacobian), and the
  anchor to 032's independently computed 14.534 is asserted separately.
  Channel closures as in 032 (3.1): z_s = z (s), z/(z-1) (t), 1 - 1/z (u).
- C2.1-gram, C2.1-onto, C2.1-break: finite-dimensional model of the circle-gluing
  form G = J b0+ b0- F (J the pairing, F diagonal), supported on W x W with
  W = c0+ c0- H^down: for an injective Phi with image I, Pi = Phi (Phi^T G Phi)^{-1}
  Phi^T satisfies G Pi G = G on I and G Pi is idempotent. C2.1-onto models the
  actual situation of record 071 (B.5)-(B.7): Phi has components in all four
  ghost-zero-mode summands (I is not inside W) while its projection pi_W Phi
  is bijective onto W (the finite-dimensional stand-in for H1 / PH31,
  surjectivity of the extended pi_W Phi_2 modulo ker G); then G Pi G = G on
  all of W and pi_W Pi J = (i/kappa) c0- c0+ F^{-1} on H^down, while Pi J
  itself differs from that target by its off-W components (invisible between
  two G's). Limits of C2.1-onto: it is a transcription check of linear algebra
  (ordering of c0- c0+, the factor kappa); it does not test surjectivity of the
  infinite-dimensional extended pi_W Phi_2 (H1 itself), nor the kernel case
  ker p != 0 (R38's quotient, where Pi needs a section and G Pi G must be
  section-independent), nor any f_m near a zero.
  C2.1-break: when pi_W Phi does not span W, G Pi G differs from G off I
  (the projector P_I is not the identity).
- C2.2-zero-modes: in the 4-dimensional representation of {b0+-, c0+-},
  b0+ b0- c0- c0+ = 1 on H^down and c0- c0+ b0+ b0- = 1 on c0+ c0- H^down.
- C2.3-inverse-region (bookkeeping): the Laplace transform of the reversed
  interval [-sigma, 0] times that of the inverse interval [0, sigma] is not 1.
- C2.4-laplace, C2.4-poles (bookkeeping), C2.4-fourier-odd: h / (e^{sigma h} - 1)
  equals the tower sum_{n>=1} h e^{-n sigma h} for Re h > 0, its value at h = 0 is
  1/sigma, it vanishes at h = 2 pi i k / sigma (one k; not that these are all the
  zeros); the Fourier coefficients f_m(h) of (e^{sigma(theta) h} - 1)/h vanish
  for odd m when sigma is pi-periodic and do not when it is not (break leg).
  C2.4-fourier-sigmaV (bookkeeping) restates C1.3-period on the computed sigma_V.
- C2.4-real-zeros: for the computed sigma_V(theta) the even-m coefficients
  f_m(h) = (1/h) int e^{i m theta} e^{sigma_V(theta) h} dtheta, real on real h,
  are tabulated on h in [-10, 10] for m = 2, 4, 6; the sign at h = +10 is
  compared with the fold-arc prediction sgn[sin(m th2) - sin(m th1)],
  th1,2 = arccos(+-(2 (16/25) - 1)) etc. (the fold arcs of C1.3-fold, where
  sigma_V = ln 4 beta^2 is flat and dominates e^{sigma_V h} as h -> +inf), the
  sign at h = -10 with the prediction "negative for every even m" (the minima
  theta = 0, pi dominate as h -> -inf); real zeros are located by sign change
  and bisection. Expected: f_4 changes sign on the real axis (critic 074 #8), so
  G_W has a zero at real timelike channel momentum in the L_0^- = 4 sector.
  What the sign test discriminates for m <= 6: a profile maximal at theta = pi/2
  and minimal at theta = 0, pi (the fold-arc width enters only from m = 12).
  Bookkeeping leg: f_0 > 0 on the real axis ((e^{sigma h} - 1)/h > 0 for any
  positive profile; cannot fail). Break leg: the same sign comparison on the
  profile 0.8 + 0.3 cos 2 theta (maximal at theta = 0), whose h -> +inf signs
  are +, +, + for m = 2, 4, 6, must disagree with the fold-arc prediction -, +, -.
- C2.5-boundary: f_{[-sigma,0]} + f_{[0,inf)} = e^{sigma h}/h and
  f_{[-ln(4 beta^2), inf)} = (4 beta^2)^h / h (exact sympy).
- C3-telescoping, C3-telescoping-break: the signed neck measure
  sum_{n>=1} d/dS (1_{[-s,0]} * 1_{[-s,0]})(S - n s) equals 1_{[-s,0]}
  pointwise (exact rational arithmetic), and does not when the two slabs
  have width s5 != s (the C4 non-telescoping statement).
- C4-telescoping-trichotomy (record (4.4)(i), critic 074 node check #4): for
  slabs of widths (a, b) and shift s the measure sum_{n>=1} d/dS
  (1_{[-a,0]} * 1_{[-b,0]})(S - n s) is, in exact rational arithmetic,
  (a) with a = s: the other width's slab 1_{(-b,0)}, for b < s and for b > s;
  (b) with (a, b) = (s/2, 3s/2), the sum a + b = 2s of the record's old
      criterion: +1 on (k s, k s + s/2), -1 on ((n - 1/2) s, n s), i.e. signed
      weight at arbitrarily long necks, and on [-s, 0] only 1_{(-s,-s/2)} --
      the old "telescopes to [-s, 0] iff a + b = 2 s" fails on both counts
      (break leg of the old criterion);
  (c) with a = 2 s: the two overlapping slabs 1_{(-b,0)} + 1_{(-b-s,-s)};
  (d) break leg of the new criterion: with a = s and b != s the result is
      not 1_{(-s,0)}.
- C4-neck-measure: the Laplace transform of the truncated signed measure
  sum_{n<=N} d/dS (1_{[-s5,0]} * 1_{[-s5,0]})(S - n s) agrees with
  f_5(h)^2 h / (e^{s h} - 1) to the truncation error e^{-N s Re h}.

Not verified: anything about the actual V_4's local coordinates (C1.5), the
hypothesis H1 (surjectivity of the extended pi_W Phi_2 modulo ker G), the
convergence of level sums (A3 makes them finite correlators), and the overall
normalisation kappa (cancels).
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp
from scipy.optimize import brentq

SEED = 20261001
rng = np.random.default_rng(SEED)
print(f"seed {SEED}")

RESULTS: list[tuple[str, bool]] = []


def report(name: str, ok: bool, info: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")


# ---------------------------------------------------------------------------
# C1.3 -- star-shapedness of Q_V in the q-plane, beta = 3/2
# ---------------------------------------------------------------------------
BETA = 1.5
B2 = BETA**2


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


n_theta, n_sigma = 1440, 6000
thetas = np.linspace(0, 2 * np.pi, n_theta, endpoint=False)
sigmas = np.linspace(1e-4, np.log(4 * B2) - 1e-4, n_sigma)
TH, SG = np.meshgrid(thetas, sigmas, indexing="ij")
Q = np.exp(SG + 1j * TH)
Z = z_of_q(Q)
inside = min_tu(Z) > 1.0  # in M'_x iff the t- and u-parameters exceed 1 (|q_s|>1 holds)
# star-shaped: along each ray the indicator is a prefix of ones
prefix_len = np.argmin(inside, axis=1)  # first False
prefix_len = np.where(inside.all(axis=1), n_sigma, prefix_len)
reenter = np.array(
    [inside[i, prefix_len[i] :].any() for i in range(n_theta)]
)  # any True after the first False
sigma_V = sigmas[np.clip(prefix_len - 1, 0, n_sigma - 1)]
at_cap = (
    prefix_len == n_sigma
)  # rays still inside M'_x at the fold circle |q| = 4 beta^2
star_ok = (not reenter.any()) and (prefix_len > 0).all()
report(
    "C1.3-star",
    bool(star_ok),
    f"rays re-entering M'_x: {int(reenter.sum())}/{n_theta}; "
    f"sigma_V in [{sigma_V.min():.4f}, {sigma_V.max():.4f}]; rays reaching the fold: {int(at_cap.sum())}",
)
# fold arcs: Z(4 b^2 e^{i th}) = cos^2(th/2) lies in M'_x iff cos^2(th/2) in (9/25, 16/25)
# (real-axis data of 032 (1.4): F'_u cap R = [-9/16, 9/25], F'_t cap R = [16/25, 25/16])
c2 = np.cos(thetas / 2) ** 2
predicted_cap = (c2 > 9 / 25) & (c2 < 16 / 25)
fold_mismatch = int((predicted_cap != at_cap).sum())
report(
    "C1.3-fold",
    bool(fold_mismatch <= 4),
    f"fold arcs vs prediction cos^2(th/2) in (9/25,16/25): {fold_mismatch} rays differ",
)
# closed form at theta = pi: the ray Z = -(9 - x)^2/(36 x), x = e^sigma, enters F'_u at Z = -9/16, x = 9/4
i_pi = n_theta // 2
report(
    "C1.3-min",
    bool(abs(sigma_V[i_pi] - np.log(9 / 4)) < 2e-3),
    f"sigma_V(pi) = {sigma_V[i_pi]:.4f} vs ln(9/4) = {np.log(9 / 4):.4f}",
)
half = n_theta // 2
period_err = np.max(np.abs(sigma_V - np.roll(sigma_V, half)))
report(
    "C1.3-period",
    bool(period_err < 2e-3),
    f"max |sigma_V(th+pi)-sigma_V(th)| = {period_err:.2e}",
)

# pulled-back area of Q_V vs grid area of M'_x (032: 14.534 at h = 0.004)
dZ = (Q - 4 * B2) * (Q + 4 * B2) / (16 * B2 * Q**2)  # Z'(q)
jac = np.abs(Q) ** 2 * np.abs(dZ) ** 2
dsig = sigmas[1] - sigmas[0]
dth = thetas[1] - thetas[0]
area_pullback = float((jac * inside).sum() * dsig * dth)
# independent route: Z-grid as in 032, step 0.004 on [-3,4]x[-3,3]
hx = 0.004
xs = np.arange(-3, 4, hx) + hx / 2
ys = np.arange(-3, 3, hx) + hx / 2
X, Y = np.meshgrid(xs, ys, indexing="ij")
ZG = X + 1j * Y
with np.errstate(divide="ignore", invalid="ignore"):
    qs = q_of_zs(ZG)
    in_grid = (np.abs(qs) > 1) & (min_tu(ZG) > 1)
area_grid = float(in_grid.sum() * hx * hx)
AREA_032 = 14.534  # |M'_x| of record 032 l.212, computed there on its own grid
report(
    "C1.3-area",
    bool(
        abs(area_pullback - area_grid) / area_grid < 2e-3  # covering once
        and abs(area_grid - AREA_032) < 0.01  # anchor to 032's independent value
        and abs(area_pullback - AREA_032) < 0.01
    ),
    f"pull-back {area_pullback:.4f} vs Z-grid {area_grid:.4f} vs 032's {AREA_032}",
)
# also the Feynman region |q|<=1 pulled back equals the grid area of F'_s (|q_s|<=1)
inside_F = np.ones_like(inside)  # the full disc 0<sigma<ln 4b^2 minus Q_V minus F_t,F_u
# consistency: area of {|q|<4b^2} pulled back = area of M_{0,4}\[0,1] is infinite (Z ~ q); skip.

# ---------------------------------------------------------------------------
# C2.2 -- ghost zero modes in the 4-dim representation
# ---------------------------------------------------------------------------
a1 = np.array([[0, 1], [0, 0]], dtype=complex)  # annihilator
eye2 = np.eye(2)
par = np.diag([1, -1]).astype(complex)  # Jordan-Wigner parity
b_plus = np.kron(a1, eye2)
c_plus = np.kron(a1.T, eye2)
b_minus = np.kron(par, a1)
c_minus = np.kron(par, a1.T)
down = np.array([1, 0, 0, 0], dtype=complex)  # H^down: killed by b0+-
top = c_plus @ c_minus @ down  # c0+ c0- |down>
assert np.allclose(b_plus @ down, 0) and np.allclose(b_minus @ down, 0)
anti = lambda x, y: x @ y + y @ x  # noqa: E731
clifford_ok = (
    np.allclose(anti(b_plus, c_plus), np.eye(4))
    and np.allclose(anti(b_minus, c_minus), np.eye(4))
    and np.allclose(anti(b_plus, c_minus), 0)
    and np.allclose(anti(b_minus, c_plus), 0)
    and np.allclose(anti(c_plus, c_minus), 0)
    and np.allclose(anti(b_plus, b_minus), 0)
)
bb = b_plus @ b_minus
cc = c_minus @ c_plus
zm_ok = (
    clifford_ok
    and np.allclose(bb @ cc @ down, down)
    and np.allclose(cc @ bb @ top, top)
)
report(
    "C2.2-zero-modes",
    bool(zm_ok),
    "b0+b0-c0-c0+ = 1 on H^down, c0-c0+b0+b0- = 1 on top",
)

# ---------------------------------------------------------------------------
# C2.1 -- Gram-matrix inverse in the finite model H = C^4 (x) C^d
# ---------------------------------------------------------------------------
d = 5
fvals = rng.normal(size=d) + 1j * rng.normal(size=d)
F = np.kron(np.eye(4), np.diag(fvals))
Finv = np.kron(np.eye(4), np.diag(1 / fvals))
BB = np.kron(bb, np.eye(d))
CC = np.kron(cc, np.eye(d))
# pairing J: pairs |down> with top and c+|down> with c-|down> (any non-degenerate choice)
J4 = np.zeros((4, 4), dtype=complex)
J4[0, 3] = 1
J4[3, 0] = 1
J4[1, 2] = 1
J4[2, 1] = -1
J = np.kron(J4, np.eye(d))
kappa = 0.7 - 0.2j  # overall constant of the Schiffer measure; must cancel
Oglue = -1j * kappa * BB @ F  # the gluing operator
G = J @ Oglue  # the bilinear form
# block W = top (x) C^d; a basis of W:
W = np.kron(top.reshape(4, 1), np.eye(d))  # 4d x d


def gram_test(Phi: np.ndarray) -> tuple[bool, bool, np.ndarray]:
    """Return (G Pi G = G on the image, G Pi idempotent, Pi) for Pi = Phi p^{-1} Phi^T."""
    p = Phi.T @ G @ Phi
    Pi = Phi @ np.linalg.inv(p) @ Phi.T
    on_image = np.allclose(G @ Pi @ G @ Phi, G @ Phi)
    idem = np.allclose(G @ Pi @ G @ Pi, G @ Pi)
    return on_image, idem, Pi


# (a) pi_W Phi onto the block, Phi itself with components in all four summands
# (071 (B.5)-(B.7): the circle state is not inside W) -- the restated H1 / PH31.
Down = np.kron(down.reshape(4, 1), np.eye(d))
Cp = np.kron((c_plus @ down).reshape(4, 1), np.eye(d))
Cm = np.kron((c_minus @ down).reshape(4, 1), np.eye(d))


def rnd(*shape: int) -> np.ndarray:
    """Random complex matrix of the given shape."""
    return rng.normal(size=shape) + 1j * rng.normal(size=shape)


Phi_onto = W @ rnd(d, d) + Down @ rnd(d, d) + Cp @ rnd(d, d) + Cm @ rnd(d, d)
PW = W @ W.conj().T  # orthogonal projector onto W (the basis W is orthonormal)
assert not np.allclose(PW @ Phi_onto, Phi_onto)  # I is not inside W
ok_a, idem_a, Pi_a = gram_test(Phi_onto)
# G sees only W-components: G Pi G = G on all of W, and pi_W Pi J equals
# (i/kappa) c0- c0+ F^{-1} on H^down (x) C^d; Pi J itself carries off-W parts.
target = (1j / kappa) * CC @ Finv @ Down
on_all_W = np.allclose(G @ Pi_a @ G @ W, G @ W)
proj_target_ok = np.allclose(PW @ Pi_a @ J @ Down, target)
off_W_present = not np.allclose(Pi_a @ J @ Down, target)
onto_ok = ok_a and idem_a and on_all_W and proj_target_ok and off_W_present
report(
    "C2.1-gram", bool(ok_a and idem_a), "G Pi G = G on I, G Pi idempotent (onto case)"
)
report(
    "C2.1-onto",
    bool(onto_ok),
    "I not in W, pi_W Phi spans W: G Pi G = G on W, pi_W Pi J = (i/kappa) c c F^{-1}; "
    "Pi J itself differs off W",
)
# (b) pi_W Phi not onto: k = 3 < d columns in W
k = 3
Phi_sub = W @ rnd(d, k) + Down @ rnd(d, k)
ok_b, idem_b, Pi_b = gram_test(Phi_sub)
v = W @ (
    rng.normal(size=d) + 1j * rng.normal(size=d)
)  # generic vector of the block, off I
off_image_differs = not np.allclose(G @ Pi_b @ G @ v, G @ v)
# and Pi_b J = P_I (i/kappa) c c F^{-1} with P_I = Phi p^{-1} Phi^T G
P_I = Phi_sub @ np.linalg.inv(Phi_sub.T @ G @ Phi_sub) @ Phi_sub.T @ G
proj_form_ok = np.allclose(Pi_b @ J @ Down, P_I @ target)
report(
    "C2.1-break",
    bool(ok_b and idem_b and off_image_differs and proj_form_ok),
    "pi_W Phi not onto: G Pi G = G on I only, Pi J = P_I (i/kappa) c c F^{-1}; differs off I",
)

# ---------------------------------------------------------------------------
# C2.3 / C2.4 / C2.5 -- Laplace transforms of regions (exact sympy)
# ---------------------------------------------------------------------------
h, sig, s = sp.symbols("h sigma s")
f_rev = (sp.exp(sig * h) - 1) / h  # [-sigma, 0]
f_fwd = (1 - sp.exp(-sig * h)) / h  # [0, sigma]
assert (
    sp.simplify(sp.integrate(sp.exp(-s * h), (s, -sig, 0), conds="none") - f_rev) == 0
)
assert sp.simplify(sp.integrate(sp.exp(-s * h), (s, 0, sig), conds="none") - f_fwd) == 0
f_prop = 1 / h  # [0, inf), Re h > 0
prod = sp.simplify(f_rev * f_fwd)
pts = [(0.7 + 0.3j, 1.1), (1.3 - 0.4j, 0.6), (0.2 + 0.9j, 2.0)]
not_one = all(abs(complex(prod.subs({h: hv, sig: sv})) - 1) > 1e-3 for hv, sv in pts)
report(
    "C2.3-inverse-region",
    bool(not_one),
    "f_[-s,0] * f_[0,s] != 1 at 3 generic points (bookkeeping)",
)

inv_rev = h / (sp.exp(sig * h) - 1)
tower = sum(h * sp.exp(-n * sig * h) for n in range(1, 60))
lap_ok = all(
    abs(complex((inv_rev - tower).subs({h: hv, sig: sv}))) < 1e-10 for hv, sv in pts
)
at_zero = sp.limit(inv_rev, h, 0)
report(
    "C2.4-laplace",
    bool(lap_ok and sp.simplify(at_zero - 1 / sig) == 0),
    "tower sum, value 1/sigma at h=0",
)
k_ = 2
pole_pt = 2 * sp.pi * sp.I * k_ / sig
zero_of_f = sp.simplify(f_rev.subs(h, pole_pt))
report(
    "C2.4-poles",
    bool(zero_of_f == 0),
    "f_[-s,0] vanishes at h = 2 pi i k / sigma (bookkeeping: one k, not all zeros)",
)

# Fourier coefficients of (e^{sigma(theta) h} - 1)/h, pi-periodic vs not
hv = 0.8 + 0.5j
th = np.linspace(0, 2 * np.pi, 4096, endpoint=False)


def fourier(sig_fn: np.ndarray, m: int, grid: np.ndarray = th) -> complex:
    """m-th Fourier coefficient of (e^{sigma(theta) h} - 1)/h on the given theta grid."""
    return complex(np.mean(np.exp(1j * m * grid) * (np.exp(sig_fn * hv) - 1) / hv))


sig_pi = 0.6 + 0.2 * np.cos(2 * th)
sig_no = 0.6 + 0.2 * np.cos(th)
odd_zero = all(abs(fourier(sig_pi, m)) < 1e-12 for m in (1, 3, 5))
even_nonzero = all(abs(fourier(sig_pi, m)) > 1e-6 for m in (0, 2, 4))
odd_nonzero_break = abs(fourier(sig_no, 1)) > 1e-6
report(
    "C2.4-fourier-odd",
    bool(odd_zero and even_nonzero and odd_nonzero_break),
    "odd m vanish for pi-periodic sigma, not for the break function",
)
# the computed sigma_V(theta) itself: odd coefficients vanish within the grid error
odd_V = max(abs(fourier(sigma_V, m, thetas)) for m in (1, 3))
even_V = abs(fourier(sigma_V, 2, thetas))
report(
    "C2.4-fourier-sigmaV",
    bool(odd_V < 1e-3 * even_V),
    f"|f_odd| / |f_2| = {odd_V / even_V:.1e} (bookkeeping: restates C1.3-period)",
)

# C2.4-real-zeros: real zeros of the even-m coefficients for the actual sigma_V
# (critic 074 #8). f_m(h) = (1/h) int e^{i m th} e^{sigma_V(th) h} dth, real on
# real h because sigma_V is even in theta. Asymptotics: h -> +inf is dominated by
# the fold arcs (sigma_V = ln 4 beta^2, flat), where the angular integral is
# 2 int_{th1}^{th2} cos(m th) dth = (2/m)[sin(m th2) - sin(m th1)]; h -> -inf by the
# minima theta = 0, pi (sigma_V = ln 9/4), giving (1 + e^{i m pi}) x positive / h < 0.
# These predictions use only the fold arcs and the minima of C1.3, not the zeros.
th1 = float(np.arccos(2 * 16 / 25 - 1))  # cos^2(th/2) = 16/25 -> th = 73.74 deg
th2 = float(np.arccos(2 * 9 / 25 - 1))  # cos^2(th/2) = 9/25  -> th = 106.26 deg


def f_real(m: int, hval: float) -> float:
    """Real even-m Fourier-Laplace coefficient of the actual region at real h."""
    return float(
        np.real(np.mean(np.exp(1j * m * thetas) * np.exp(sigma_V * hval))) / hval
    )


h_grid = np.linspace(-10, 10, 2001)
h_grid = h_grid[np.abs(h_grid) > 1e-9]  # f_m(0) finite but the formula has 1/h
real_zeros: dict[int, list[float]] = {}
sign_ok = True
for m in (2, 4, 6):
    vals = np.array([f_real(m, hv) for hv in h_grid])
    pred_plus = np.sign(np.sin(m * th2) - np.sin(m * th1))
    sign_ok &= bool(np.sign(vals[-1]) == pred_plus and np.sign(vals[0]) < 0)
    zs = []
    for i in range(len(h_grid) - 1):
        if vals[i] * vals[i + 1] < 0:
            zs.append(brentq(lambda x, m=m: f_real(m, x), h_grid[i], h_grid[i + 1]))
    real_zeros[m] = zs
    print(
        f"   f_{m}: sign(h=-10) {np.sign(vals[0]):+.0f}, sign(h=+10) {np.sign(vals[-1]):+.0f} "
        f"(fold-arc prediction {pred_plus:+.0f}); real zeros on [-10,10]: "
        f"{[round(z, 4) for z in zs]}"
    )
f0_vals = np.array(
    [float(np.mean(np.exp(sigma_V * hv) - 1) / hv) for hv in h_grid]
)  # bookkeeping: f_0 > 0 for any positive profile, cannot fail
f0_no_zero = bool((f0_vals > 0).all())
# break leg (critic 074 node check #3): a profile maximal at theta = 0 instead of
# pi/2 (0.8 + 0.3 cos 2 theta) has h -> +inf signs +, +, + for m = 2, 4, 6
# (modified Bessel I_{m/2}(3 h) > 0), so the fold-arc prediction -, +, - must
# be contradicted at m = 2 and m = 6.
sig_break = 0.8 + 0.3 * np.cos(2 * thetas)
break_signs = {
    m: np.sign(
        float(
            np.real(np.mean(np.exp(1j * m * thetas) * np.exp(sig_break * 10.0))) / 10.0
        )
    )
    for m in (2, 4, 6)
}
break_disagree = all(
    break_signs[m] != np.sign(np.sin(m * th2) - np.sin(m * th1)) for m in (2, 6)
)
report(
    "C2.4-real-zeros",
    bool(sign_ok and len(real_zeros[4]) >= 1 and f0_no_zero and break_disagree),
    f"f_4 has {len(real_zeros[4])} real zero(s) at h = {[round(z, 3) for z in real_zeros[4]]}; "
    f"f_6 at {[round(z, 3) for z in real_zeros[6]]}; asymptotic signs as predicted; "
    f"f_0 > 0 on the real axis (bookkeeping); break profile max at theta=0 gives signs "
    f"{[int(break_signs[m]) for m in (2, 4, 6)]} vs prediction (fails at m=2,6 as required)",
)

bnd = sp.simplify(f_rev + f_prop - sp.exp(sig * h) / h)
bpos, hpos = sp.symbols("b h_pos", positive=True)  # Re h > 0 for the half-line
full = sp.integrate(sp.exp(-s * hpos), (s, -sp.log(4 * bpos**2), sp.oo), conds="none")
full_ok = sp.simplify(full - (4 * bpos**2) ** hpos / hpos) == 0
report(
    "C2.5-boundary",
    bool(bnd == 0 and full_ok),
    "f_[-s,0]+1/h = e^{sh}/h; f_[-ln4b^2,inf) = (4b^2)^h/h",
)

# ---------------------------------------------------------------------------
# C3 / C4 -- the signed neck measure, exact rational arithmetic
# ---------------------------------------------------------------------------
S = sp.symbols("S", real=True)


def tent(width: sp.Rational, x):
    """(1_{[-w,0]} * 1_{[-w,0]})(x): tent on [-2w, 0], peak w at x = -w."""
    return sp.Piecewise(
        (x + 2 * width, (x >= -2 * width) & (x < -width)),
        (-x, (x >= -width) & (x <= 0)),
        (0, True),
    )


def dtent(width: sp.Rational, x):
    """Return the derivative of the tent: +1 on (-2w, -w), -1 on (-w, 0)."""
    return sp.Piecewise(
        (1, (x > -2 * width) & (x < -width)), (-1, (x > -width) & (x < 0)), (0, True)
    )


def neck_measure(w5: sp.Rational, w: sp.Rational, nmax: int):
    """Signed neck measure sum_{n<=nmax} d/dS tent_{w5}(S - n w), record (4.3)."""
    return sum(dtent(w5, S - n * w) for n in range(1, nmax + 1))


sig0 = sp.Rational(3, 4)
N = 12
mu_equal = neck_measure(sig0, sig0, N)
samples = [sp.Rational(i, 40) * sig0 for i in range(-38, 40 * (N - 1) - 2, 3)]
samples = [x for x in samples if x not in (0, -sig0)]  # off the breakpoints
tele_ok = all(mu_equal.subs(S, x) == (1 if -sig0 < x < 0 else 0) for x in samples)
report(
    "C3-telescoping",
    bool(tele_ok),
    f"sum_n d/dS tent(S - n s) = 1_[-s,0] at {len(samples)} points",
)
sig5 = sp.Rational(1, 2)
mu_diff = neck_measure(sig5, sig0, N)
nonzero_long = [x for x in samples if x > 0 and mu_diff.subs(S, x) != 0]
report(
    "C3-telescoping-break",
    bool(len(nonzero_long) > 0),
    f"with s5 = {sig5} != s = {sig0}: non-zero at {len(nonzero_long)} points with S > 0 (long necks)",
)


# C4-telescoping-trichotomy: unequal slab widths (a, b), record (4.4)(i) after the
# iteration-2 node check (#4). (1_{[-a,0]} * 1_{[-b,0]}) is the trapezoid on
# [-a-b, 0] with flat top on [-max(a,b), -min(a,b)]; its derivative is +1 on
# (-a-b, -max(a,b)) and -1 on (-min(a,b), 0).
def dtrap(a: sp.Rational, b: sp.Rational, x):
    """Return the derivative of the trapezoid 1_{[-a,0]} * 1_{[-b,0]} at x (exact)."""
    hi, lo = max(a, b), min(a, b)
    return sp.Piecewise(
        (1, (x > -a - b) & (x < -hi)), (-1, (x > -lo) & (x < 0)), (0, True)
    )


def neck_measure_ab(a: sp.Rational, b: sp.Rational, w: sp.Rational, nmax: int):
    """Signed neck measure sum_{n<=nmax} d/dS trapezoid_{a,b}(S - n w)."""
    return sum(dtrap(a, b, S - n * w) for n in range(1, nmax + 1))


def indicator(lo: sp.Rational, hi: sp.Rational, x: sp.Rational) -> int:
    """1 if lo < x < hi else 0."""
    return 1 if lo < x < hi else 0


N_ab = 14
# sample points off every breakpoint (multiples of sig0/4 are the only breakpoints
# for the widths used below), from S = -2 sig0 up to S = (N_ab - 3) sig0
samples_ab = [
    sp.Rational(8 * i + 1, 32) * sig0 for i in range(-8, 4 * (N_ab - 3))
]  # x = (k + 1/8) sig0 / 4: never a multiple of sig0 / 4
b_lt, b_gt = sp.Rational(1, 2), sp.Rational(5, 4)  # b < sig0 and b > sig0
leg_a = all(
    neck_measure_ab(sig0, b, sig0, N_ab).subs(S, x) == indicator(-b, 0, x)
    for b in (b_lt, b_gt)
    for x in samples_ab
)
# (b) a + b = 2 sig0 with neither width equal to sig0: alternating weight forever
a_h, b_h = sig0 / 2, 3 * sig0 / 2
mu_half = neck_measure_ab(a_h, b_h, sig0, N_ab)


# predicted: +1 on (k s, k s + s/2) for k >= -1, -1 on ((n - 1/2) s, n s) for n >= 1
# (floor(x/s) = n - 1 >= 0 on the latter)
def pred_half(x: sp.Rational) -> int:
    """Predicted signed weight for widths (s/2, 3s/2)."""
    k = sp.floor(x / sig0)
    frac = x / sig0 - k
    if k >= -1 and frac < sp.Rational(1, 2):
        return 1
    if k >= 0 and frac > sp.Rational(1, 2):
        return -1
    return 0


leg_b_pattern = all(mu_half.subs(S, x) == pred_half(x) for x in samples_ab)
long_neck_weight = [x for x in samples_ab if x > 8 * sig0 and mu_half.subs(S, x) != 0]
old_claim_fails = (
    mu_half.subs(S, -sig0 / 4) == 0  # old claim: 1 on (-s, 0)
    and mu_half.subs(S, sig0 / 4) == 1  # old claim: 0 for S > 0
)
leg_b = leg_b_pattern and len(long_neck_weight) > 0 and old_claim_fails
# (c) a = 2 sig0: two overlapping slabs on the reversed side
leg_c = all(
    neck_measure_ab(2 * sig0, b_lt, sig0, N_ab).subs(S, x)
    == indicator(-b_lt, 0, x) + indicator(-b_lt - sig0, -sig0, x)
    for x in samples_ab
)
# (d) break leg of the new criterion: a = sig0, b != sig0 is not 1_{(-s,0)}
leg_d = not all(
    neck_measure_ab(sig0, b_lt, sig0, N_ab).subs(S, x) == indicator(-sig0, 0, x)
    for x in samples_ab
)
report(
    "C4-telescoping-trichotomy",
    bool(leg_a and leg_b and leg_c and leg_d),
    f"(a) a=s -> 1_(-b,0) for b={b_lt},{b_gt}; (b) (s/2,3s/2): alternating pattern, "
    f"non-zero at {len(long_neck_weight)} points with S > 8s, not 1_(-s,0); "
    f"(c) a=2s -> two slabs; (d) a=s,b!=s is not 1_(-s,0); {len(samples_ab)} points",
)

# C4-neck-measure: Laplace transform of the truncated signed measure vs f5^2 h/(e^{sh}-1)
hv2 = 1.1 + 0.4j
sig0f, sig5f = float(sig0), float(sig5)


def laplace_signed(w5: float, w: float, nmax: int, hval: complex) -> complex:
    """Laplace transform at hval of the truncated signed neck measure (4.3), in closed form per slab."""
    tot = 0j
    for n in range(1, nmax + 1):
        # +1 on (n w - 2 w5, n w - w5), -1 on (n w - w5, n w)
        a, b_, c = n * w - 2 * w5, n * w - w5, n * w
        tot += (np.exp(-a * hval) - np.exp(-b_ * hval)) / hval - (
            np.exp(-b_ * hval) - np.exp(-c * hval)
        ) / hval
    return tot


f5 = (np.exp(sig5f * hv2) - 1) / hv2
target_c4 = f5**2 * hv2 / (np.exp(sig0f * hv2) - 1)
lhs_c4 = laplace_signed(sig5f, sig0f, 60, hv2)
err_c4 = abs(lhs_c4 - target_c4)
report(
    "C4-neck-measure",
    bool(err_c4 < 1e-8),
    f"|L[mu] - f5^2/f| = {err_c4:.1e} (truncation e^-60 s Re h)",
)
# break leg: using f5 f (wrong middle factor) must fail
wrong = f5**2 * (np.exp(sig0f * hv2) - 1) / hv2
report(
    "C4-neck-measure-break",
    bool(abs(lhs_c4 - wrong) > 1e-3),
    "wrong middle factor fails",
)

# ---------------------------------------------------------------------------
n_fail = sum(1 for _, ok in RESULTS if not ok)
print(f"\n{len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
sys.exit(1 if n_fail else 0)
