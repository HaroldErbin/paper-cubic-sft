"""Verification companion of record 081: the n=3 patch V'_4 and the two-patch map to M_{0,6}.

Verified (all at beta = 3/2, surfaces only, record 081):
- C1.1-n2-normal-form: the V_3' half in normal form, (lambda, c) = (beta, 1/2) (exact).
- C1.2-F3-jet: F_3 = Z/F_1 with F_1 = R S W/(S W + R) equals Z/R + Z/(S W) (sympy, symbolic).
- C1.2-scale: |m/S_0(m)| = beta |m (m-1)|^{1/2} with S_0 = beta^{-1} sqrt(m/(m-1)).
- C2.2-mobius / C2.2-seam: the three cross-ratios (2.2) of the six points (2.1) are
  Mobius invariant and seam invariant (break legs included).
- C2.3-n2: with two bare V_3' the cross-ratio chi gives Z_4^{(s)}(q) = 1/(1 - chi) (R2).
- C2.4-jacobian: det of d(chi)/d(m_L, m_R, q) nonzero at random points (local injectivity there).
- C4-*: marches |q| from 1 outwards at sample points (m_L, m_R) and a few twists:
  Jacobian rank along the march, collision radius (first coincidence of two punctures),
  and the inversion test for the V_4-V_4 Feynman regions of all ten (3|3) channels, the
  own channel included (re-entry at large |q|, record 081 (3.1); fix pass 1, critic #3;
  the run-6 output quoted in the record predates this change and tested nine channels)
  (record 081 §4; a root find, reported as found/not found per point).

Not verified: the covering theorem (077 (3.5)); membership in the V_3-containing Feynman
regions of M_{0,6} (kinds (b), (c), (d) of record §3, next sub-tasks); anything off shell.
Hypothesis H1 (centre c(m) ~ (1+m)/3, an approximation) enters only the C4 numbers.
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import fsolve

SEED = 20261004
rng = np.random.default_rng(SEED)
print(f"seed {SEED}")
RESULTS: list[tuple[str, bool]] = []
BETA = 1.5
B2 = BETA**2
ALPHA = 0.3  # branch rotation of sqrt in lam(); a phase convention only
SCRATCH = Path(__file__).resolve().parent / "output" / "npatch-n3"
SCRATCH.mkdir(parents=True, exist_ok=True)


def report(name: str, ok: bool, info: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")


# --- geometry of V_{0,4} as a set of surfaces (copied from codes/verify-circle-gluing-inverse.py,
# record 074 A4 / 032 (3.1); that script is never edited) ---------------------------------
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


def min_stu(z: np.ndarray) -> np.ndarray:
    """min(|q_s|, |q_t|, |q_u|): the surface Z is in V_{0,4} = M'_x iff this exceeds 1."""
    qs = q_of_zs(z)
    qt = q_of_zs(z / (z - 1))
    qu = q_of_zs(1 - 1 / z)
    return np.minimum(np.abs(qs), np.minimum(np.abs(qt), np.abs(qu)))


def in_v04(m: complex) -> bool:
    """Membership criterion of 032 §3 / 074 (1.4)."""
    return bool(min_stu(np.asarray(m, dtype=complex)) > 1.0)


# --- the patch (record (1.3)–(1.4)) ------------------------------------------------------
def lam_naive(m: complex) -> complex:
    """Scale of the special coordinate: beta sqrt(m (m-1)); the branch (cut rotated by
    ALPHA so that it avoids the sample points) is a phase convention = a rotation of q."""
    return BETA * np.exp(1j * ALPHA) * np.sqrt(np.exp(-2j * ALPHA) * m * (m - 1) + 0j)


# the six anharmonic relabellings g(m) of the ordinary triple {0,1,m} (special puncture fixed at
# infinity) are affine maps u' = a u + b of the global coordinate; the vertex section is
# S_3-equivariant, so lambda(m) = lambda(g m)/a_g with g m in the fundamental domain
# FD = {Im > 0, |m| > 1, Re < 1/2} (closure; conjugation leaves |lambda| unchanged). The naive
# formula |S_0| is NOT equivariant (it fails m -> 1/m by |m|^{-1/2}): record 081 §1 (1.3'), §4.
ANHARMONIC = [
    (lambda m: m, lambda m: 1.0),
    (lambda m: 1 - m, lambda m: -1.0),
    (lambda m: 1 / m, lambda m: 1 / m),
    (lambda m: (m - 1) / m, lambda m: -1 / m),
    (lambda m: 1 / (1 - m), lambda m: -1 / (1 - m)),
    (lambda m: m / (m - 1), lambda m: 1 / (1 - m)),
]


def in_fd(m: complex, tol: float = 1e-9) -> bool:
    return abs(m) >= 1 - tol and m.real <= 0.5 + tol


def lam(m: complex, g_index: int | None = None) -> complex:
    """Equivariant scale: transport of the naive FD value by the anharmonic relabelling.

    With g_index given, the relabelling is frozen (a holomorphic local representative: the
    phase of lambda jumps by a sign across the FD walls, a twist convention only, which would
    wreck finite differences in m otherwise).
    """
    m = complex(m)
    if g_index is not None:
        g, a = ANHARMONIC[g_index]
        return lam_naive(g(m)) / a(m)
    for g, a in ANHARMONIC:
        if in_fd(g(m)):
            return lam_naive(g(m)) / a(m)
    raise ValueError(f"no anharmonic image of {m} in the FD")


def g_index_of(m: complex) -> int:
    m = complex(m)
    for i, (g, _a) in enumerate(ANHARMONIC):
        if in_fd(g(m)):
            return i
    raise ValueError(f"no anharmonic image of {m} in the FD")


def cen(m: complex) -> complex:
    """Centre of the special coordinate under H1: the centroid (1+m)/3."""
    return (1 + m) / 3


def six_points(
    mL: complex, mR: complex, q: complex, jets=None, gidx=None
) -> np.ndarray:
    """The six punctures (2.1) in u_L; jets = ((lamL, cL), (lamR, cR)) overrides (1.3)."""
    if jets is None:
        gl, gr = (None, None) if gidx is None else gidx
        lL, cL, lR, cR = lam(mL, gl), cen(mL), lam(mR, gr), cen(mR)
    else:
        (lL, cL), (lR, cR) = jets
    Lam = lL * lR / q
    return np.array(
        [0, 1, mL, cL - Lam / cR, cL + Lam / (1 - cR), cL + Lam / (mR - cR)],
        dtype=complex,
    )


def cross_ratio(p1, p2, p3, p4) -> complex:
    """(p1-p3)(p2-p4) / ((p1-p4)(p2-p3))."""
    return (p1 - p3) * (p2 - p4) / ((p1 - p4) * (p2 - p3))


def moduli(pts: np.ndarray) -> np.ndarray:
    """The three cross-ratios (2.2) of six labelled points."""
    return np.array([cross_ratio(pts[0], pts[1], pts[2], pts[3 + k]) for k in range(3)])


def chi(mL, mR, q, gidx=None) -> np.ndarray:
    return moduli(six_points(mL, mR, q, gidx=gidx))


def mobius(pts: np.ndarray, a, b, c, d) -> np.ndarray:
    return (a * pts + b) / (c * pts + d)


def rnd_c(scale: float = 1.0) -> complex:
    return complex(scale * (rng.normal() + 1j * rng.normal()))


def jacobian(mL, mR, q, h: float = 1e-6) -> np.ndarray:
    """Complex 3x3 Jacobian of chi w.r.t. (m_L, m_R, q), central differences."""
    J = np.zeros((3, 3), dtype=complex)
    gidx = (
        g_index_of(mL),
        g_index_of(mR),
    )  # frozen relabelling: holomorphic representative
    for j, (dm, dr, dq) in enumerate([(h, 0, 0), (0, h, 0), (0, 0, h)]):
        J[:, j] = (
            chi(mL + dm, mR + dr, q + dq, gidx) - chi(mL - dm, mR - dr, q - dq, gidx)
        ) / (2 * h)
    return J


# =========================================================== C1
# C1.1: affine normal form of V_3'
b_, u_ = sp.symbols("beta u", positive=True)
affine = lambda u: b_ * u + sp.Rational(1, 2)  # noqa: E731
ok = sp.simplify(affine(-1 / (2 * b_))) == 0 and sp.simplify(affine(1 / (2 * b_))) == 1
w_in_uprime = sp.simplify(
    1 / ((sp.Symbol("up") - sp.Rational(1, 2)) / b_)
)  # w = 1/u, u = (u'-1/2)/beta
ok = ok and sp.simplify(w_in_uprime - b_ / (sp.Symbol("up") - sp.Rational(1, 2))) == 0
report("C1.1-n2-normal-form", bool(ok), "(lambda, c) = (beta, 1/2)")

# C1.2: F_3 = Z/F_1 is Z/R + Z/(S W)
R, S, Z, W = sp.symbols("R S Z W")
F1 = R * S * W / (S * W + R)
F3 = Z / F1
ok = sp.simplify(F3 - (Z / R + Z / (S * W))) == 0
bad = sp.simplify(F3 - (Z / R + 2 * Z / (S * W))) == 0
report(
    "C1.2-F3-jet",
    bool(ok and not bad),
    "F_3 = Z/R + Z/(S W); break leg (2Z/(SW)) fails as required",
)

# C1.2: scale from |S_0|
ok = True
for _ in range(5):
    m = rnd_c(1.5)
    S0 = np.sqrt(m / (m - 1) + 0j) / BETA
    ok = ok and abs(abs(m / S0) - abs(lam_naive(m))) < 1e-12
report(
    "C1.2-scale",
    bool(ok),
    "|m/S_0| = beta |m(m-1)|^{1/2} at 5 random m (naive formula, valid on the FD)",
)

# C1.2': equivariance of the scale under the relabellings of the ordinary triple (1.3')
ok, okb = True, True
for _ in range(6):
    m = rnd_c(1.5)
    for g, a in ANHARMONIC:
        ok = ok and abs(abs(lam(g(m))) - abs(a(m)) * abs(lam(m))) < 1e-10 * abs(lam(m))
    okb = okb and abs(abs(lam_naive(1 / m)) - abs(lam_naive(m)) / abs(m)) > 1e-6 * abs(
        lam_naive(m)
    )
report(
    "C1.2-equivariance",
    bool(ok and okb),
    "|lambda(g m)| = |a_g| |lambda(m)| for all six g (u' = a_g u + b_g); break leg: the naive |S_0| formula fails m -> 1/m",
)

# =========================================================== C2
ok, okb = True, True
for _ in range(5):
    mL, mR, q = rnd_c(1.5), rnd_c(1.5), np.exp(rnd_c(0.7))
    pts = six_points(mL, mR, q)
    a, b, c, d = (rnd_c() for _ in range(4))
    img = mobius(pts, a, b, c, d)
    ok = ok and np.allclose(moduli(pts), moduli(img), rtol=1e-9, atol=1e-12)
    pert = pts.copy()
    pert[4] += 1e-3
    okb = okb and not np.allclose(moduli(pts), moduli(pert), rtol=1e-9, atol=1e-12)
report(
    "C2.2-mobius",
    bool(ok and okb),
    "cross-ratios Mobius invariant; break leg (point moved by 1e-3) fails",
)

ok, okb = True, True
for _ in range(5):
    mL, mR, q, k = rnd_c(1.5), rnd_c(1.5), np.exp(rnd_c(0.7)), np.exp(rnd_c(0.5))
    base = six_points(mL, mR, q)
    seam = six_points(mL, mR, q, jets=((k * lam(mL), cen(mL)), (lam(mR) / k, cen(mR))))
    brk = six_points(mL, mR, q, jets=((k * lam(mL), cen(mL)), (lam(mR), cen(mR))))
    ok = ok and np.allclose(base, seam, rtol=1e-12, atol=1e-12)
    okb = okb and not np.allclose(base, brk, rtol=1e-9, atol=1e-12)
report(
    "C2.2-seam",
    bool(ok and okb),
    "seam (kappa lam_L, lam_R/kappa) invisible; break leg fails (transcription check)",
)

# C2.3: n = 2 reduction, exact and numeric
qs = sp.Symbol("q")
a_ = 2 * b_**2 / qs
chi_sym = cross_ratio(0, 1, sp.Rational(1, 2) - a_, sp.Rational(1, 2) + a_)
Z4 = (qs + 4 * b_**2) ** 2 / (16 * b_**2 * qs)
ok = sp.simplify(1 / (1 - chi_sym) - Z4) == 0
okn = True
for _ in range(5):
    q = np.exp(rnd_c(0.7))
    pts = six_points(0, 0, q, jets=((BETA, 0.5), (BETA, 0.5)))[[0, 1, 3, 4]]
    okn = okn and abs(1 / (1 - cross_ratio(*pts)) - z_of_q(q)) < 1e-10 * abs(z_of_q(q))
    ptsb = six_points(0, 0, q, jets=((BETA, 0.4), (BETA, 0.4)))[[0, 1, 3, 4]]
    okn = okn and abs(1 / (1 - cross_ratio(*ptsb)) - z_of_q(q)) > 1e-3
report(
    "C2.3-n2",
    bool(ok and okn),
    "1/(1-chi) = Z_4^{(s)}(q) exactly (sympy) and at 5 random q; break leg c = 0.4 fails",
)

ok = True
conds = []
for _ in range(5):
    mL, mR, q = rnd_c(1.5), rnd_c(1.5), np.exp(rnd_c(0.7))
    J = jacobian(mL, mR, q)
    sv = np.linalg.svd(J, compute_uv=False)
    conds.append(sv[0] / sv[-1])
    ok = ok and sv[-1] > 1e-8 * sv[0]
report(
    "C2.4-jacobian",
    bool(ok),
    f"rank 3 at 5 random points; condition numbers {np.round(conds, 1).tolist()}",
)


# =========================================================== C4
# membership test for the V_4-V_4 Feynman region of a (3|3) channel {abc}|{def}:
# find (m'_L, m'_R, Lambda') with g_{m'_L}(p_{d,e,f}) = c(m'_L) + Lambda'/(u_R - c(m'_R)), u_R in {0,1,m'_R}
def g_frame(pts3: np.ndarray, mprime: complex, x: np.ndarray) -> np.ndarray:
    """Mobius map sending (pts3[0], pts3[1], pts3[2]) to (0, 1, mprime), applied to x."""
    a, b, c = pts3
    v = ((x - a) * (b - c)) / ((x - c) * (b - a))  # (a,b,c) -> (0,1,inf)
    return mprime * v / (v + mprime - 1)  # (0,1,inf) -> (0,1,m')


def channel_residual(x: np.ndarray, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    mL_, mR_ = x[0] + 1j * x[1], x[2] + 1j * x[3]
    cl, cr = cen(mL_), cen(mR_)
    img = g_frame(left, mL_, right)
    Lams = (img - cl) * (
        np.array([0, 1, mR_]) - cr
    )  # three estimates of Lambda', must agree
    r = np.array([Lams[0] - Lams[1], Lams[0] - Lams[2]])
    return np.array([r[0].real, r[0].imag, r[1].real, r[1].imag])


def in_v4v4_channel(
    pts: np.ndarray, left_idx, right_idx, n_starts: int = 12
) -> tuple[bool, dict]:
    """True if the surface lies in the |q'|<=1 V_4-V_4 region of the channel (root find; best-effort)."""
    left, right = pts[list(left_idx)], pts[list(right_idx)]
    found = []
    # independent initial guess: the special puncture of each side sits near the centroid of the
    # other triple, so m' ~ cross-ratio of the triple with that centroid as the fourth point
    gl = ((left[2] - left[0]) * (left[1] - right.mean())) / (
        (left[2] - right.mean()) * (left[1] - left[0])
    )
    for perm in itertools.permutations(range(3)):  # labelling of the right triple
        rp = right[list(perm)]
        gr = ((rp[2] - rp[0]) * (rp[1] - left.mean())) / (
            (rp[2] - left.mean()) * (rp[1] - rp[0])
        )
        for k in range(n_starts):
            x0 = (
                np.array([gl.real, gl.imag, gr.real, gr.imag])
                + (k > 0) * rng.normal(size=4) * 0.5
            )
            sol, info, ier, _ = fsolve(
                channel_residual, x0, args=(left, rp), full_output=True
            )
            if ier != 1 or np.max(np.abs(channel_residual(sol, left, rp))) > 1e-9:
                continue
            mL_, mR_ = sol[0] + 1j * sol[1], sol[2] + 1j * sol[3]
            cl, cr = cen(mL_), cen(mR_)
            Lam = (g_frame(left, mL_, rp)[0] - cl) * (0 - cr)
            qprime = (
                abs(lam(mL_)) * abs(lam(mR_)) / abs(Lam)
            )  # modulus: branch-independent
            found.append((mL_, mR_, abs(qprime), in_v04(mL_) and in_v04(mR_)))
            if in_v04(mL_) and in_v04(mR_) and abs(qprime) <= 1.0:
                return True, {"mL": mL_, "mR": mR_, "|q'|": abs(qprime)}
    return False, {"n_roots": len(found)}


SAMPLES = {
    "sym-sym": (np.exp(1j * np.pi / 3), np.exp(1j * np.pi / 3)),
    # H1 puts c(-1) = 0, i.e. one right puncture at u_L = infinity at the Z_2 point itself;
    # the samples sit next to it on the real segment of V_{0,4} (-16/9, -9/16).
    "nearZ2-nearZ2": (-1.3 + 0j, -1.3 + 0j),
    "sym-nearZ2": (np.exp(1j * np.pi / 3), -1.3 + 0j),
    "near-boundary": (-0.62 + 0j, np.exp(1j * np.pi / 3)),
}
for name, (mL, mR) in SAMPLES.items():
    report(
        f"C4-sample-{name}-in-V04",
        in_v04(mL) and in_v04(mR),
        f"min|q_stu| = {min_stu(np.array([mL]))[0]:.3f}, {min_stu(np.array([mR]))[0]:.3f}",
    )

# self-consistency of the channel inversion on the construction's own channel at |q|<1 (break leg: |q|>1)
mL, mR = SAMPLES["sym-nearZ2"]
pts = six_points(mL, mR, 0.7 * np.exp(0.4j))
okin, info_in = in_v4v4_channel(pts, (0, 1, 2), (3, 4, 5))
pts_out = six_points(mL, mR, 1.6 * np.exp(0.4j))
okout, info_out = in_v4v4_channel(pts_out, (0, 1, 2), (3, 4, 5))
report(
    "C4-inversion-selfcheck",
    bool(okin and not okout and abs(info_in["|q'|"] - 0.7) < 1e-6),
    f"own channel at |q|=0.7 found {info_in}; at |q|=1.6 not in region {info_out}",
)

twists = [0.0, np.pi / 2, np.pi]
radii = np.exp(np.linspace(0.0, np.log(12.0), 15))
other_channels = [
    (l, tuple(sorted(set(range(6)) - set(l))))
    for l in itertools.combinations(range(6), 3)
    if 0 in l
]
march_log = {}
for name, (mL, mR) in SAMPLES.items():
    for th in twists:
        first_entry, collision, min_sv = None, None, np.inf
        for r in radii:
            q = r * np.exp(1j * th)
            pts = six_points(mL, mR, q)
            dmin = min(
                abs(pts[i] - pts[j]) for i, j in itertools.combinations(range(6), 2)
            )
            if dmin < 1e-3:
                collision = r
                break
            sv = np.linalg.svd(jacobian(mL, mR, q), compute_uv=False)
            min_sv = min(min_sv, sv[-1] / sv[0])
            if first_entry is None:
                for li, ri in other_channels:
                    hit, info = in_v4v4_channel(pts, li, ri, n_starts=4)
                    if hit:
                        first_entry = (
                            r,
                            li,
                            {
                                k: (complex(v) if isinstance(v, complex) else v)
                                for k, v in info.items()
                            },
                        )
                        break
        march_log[f"{name}|theta={th:.3f}"] = {
            "first_entry_other_V4V4": None
            if first_entry is None
            else [first_entry[0], first_entry[1], str(first_entry[2])],
            "collision_radius": collision,
            "min_rel_singular_value": min_sv,
        }
        print(
            f"  march {name} theta={th:.2f}: entry={None if first_entry is None else (round(first_entry[0], 3), first_entry[1])} collision={collision} min_sv/max_sv={min_sv:.2e}"
        )
(SCRATCH / "march-log.json").write_text(json.dumps(march_log, indent=1, default=str))
ok_rank = all(v["min_rel_singular_value"] > 1e-6 for v in march_log.values())
report(
    "C4-march-rank",
    bool(ok_rank),
    "Jacobian rank 3 along every march (relative smallest singular value > 1e-6)",
)
n_entries = sum(v["first_entry_other_V4V4"] is not None for v in march_log.values())
report(
    "C4-march-recorded",
    True,
    f"{n_entries}/{len(march_log)} marches enter another (3|3) V4-V4 region before collision (recorded, not a pass/fail)",
)

n_fail = sum(1 for _, ok in RESULTS if not ok)
print(f"summary: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
sys.exit(1 if n_fail else 0)
