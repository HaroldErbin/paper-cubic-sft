"""
Verify record 082 (PH31' in the fixed-halves model): conservation law, witness, limit.

Checks (named after the claim-tree nodes of agent/derivations/082-ph31prime.md):

- C2-taylor: the mode coefficients (2.1) of a global CKV eta at a puncture with
  germ t = h(w), eta^{(k)}(w) = eta(h(w)) / h'(w), against a sympy series.
- C2-ward-ghost: in the holomorphic bc Fock space (modes on the SL(2) vacuum),
  b[eta] c(t1) c(t2)|0> = eta(t1) c(t2)|0> - eta(t2) c(t1)|0>, componentwise,
  for eta = vtilde = beta (t^2 - z^2) d_t, b[vtilde] = beta (b_1 - z^2 b_{-1}).
  Mode algebra {b_m, c_n} = delta_{m+n,0} vs the contour (Ward) prediction.
- C3-witness-ward: the c_0|0> coefficient of (b_1 - z^2 b_{-1}) c(t1)c(t2)|0>
  equals -(t2 - t1)(t1 t2 + z^2) and is non-zero at seeded random points.
- C3-witness-dressed-transcription: with sector weights k(level) applied before
  O_b (eq. 3.3), the target coefficient is -(t2-t1)[z^2 k_00 + t1 t2 k_20]
  (symbolic in k_00, k_20). A transcription check of the dressed coefficient only:
  whether it vanishes for the model's actual dressing k_m = fhat_5 / fhat_m is NOT
  checked (record 082 C3.5, argued). BREAK-witness-dressed: swapping the level
  assignment of k_00, k_20 is detected.
- C3-locus-dressed: at t1 t2 = -z^2 (ghost punctures on the zeros of vtilde) the
  dressed coefficient is -(t2-t1) z^2 (k_00 - k_20), non-zero unless k_00 = k_20
  (critic-082 #3); BREAK-locus-dressed: the form with k_00 + k_20 is detected.
- C3-limit: t1 = z, t2 = -z (zeros of vtilde on the ghost-carrying punctures):
  O_b^hol c(z)c(-z)|0> = 0 in all components up to the truncation (078's identity
  in the tachyon sector); BREAK-limit: b_1 + z^2 b_{-1} does not vanish there.

Not verified: the matter factor and germ factors (common scalars, eq. 3.3), the
antiholomorphic copy (identical algebra), the t_3 integral, the actual Q_5
regions and hence O_b x != 0 for the model's dressing, O_L, section 4.
"""

from __future__ import annotations

import random
import sys

import sympy as sp

SEED = 20261004
NMIN = -8  # lowest c-mode kept in c(t)|0>; components compared at L0 <= LMAX
LMAX = 4

t, w, t1, t2, z, beta = sp.symbols("t w t1 t2 z beta")
results: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, info: str = "") -> None:
    results.append((name, ok, info))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")


# --- fermionic Fock space: state = dict{tuple of c-mode indices (ordered): coeff}
def c_field(x: sp.Expr) -> dict:
    """c(x)|0> = sum_{n<=1} x^{1-n} c_n |0>, truncated at n >= NMIN."""
    return {(n,): x ** (1 - n) for n in range(1, NMIN - 1, -1)}


def mul_c(state_left: dict, state_right: dict) -> dict:
    """Product of c-strings (left string placed to the left), normal-ordered key."""
    out: dict = {}
    for kl, al in state_left.items():
        for kr, ar in state_right.items():
            modes = list(kl) + list(kr)
            if len(set(modes)) < len(modes):
                continue
            # sort descending with sign of permutation
            sign, arr = 1, modes[:]
            for i in range(len(arr)):
                for j in range(len(arr) - 1 - i):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        sign = -sign
            key = tuple(arr)
            out[key] = out.get(key, 0) + sign * al * ar
    return out


def apply_b(m: int, state: dict) -> dict:
    """b_m on c_{n1}...c_{nk}|0>, with b_m|0> = 0 for m >= -1."""
    assert m >= -1
    out: dict = {}
    for key, a in state.items():
        for i, n in enumerate(key):
            if m + n == 0:
                nk = key[:i] + key[i + 1 :]
                out[nk] = out.get(nk, 0) + (-1) ** i * a
    return out


def lin(*terms: tuple[sp.Expr, dict]) -> dict:
    out: dict = {}
    for coef, st in terms:
        for k, a in st.items():
            out[k] = out.get(k, 0) + coef * a
    return out


def level(key: tuple) -> int:
    return -sum(key)  # L0 of c_{n1}...|0>


def diff_ok(s1: dict, s2: dict, subs: dict, lmax: int) -> bool:
    keys = {k for k in list(s1) + list(s2) if level(k) <= lmax}
    for k in keys:
        d = sp.N((s1.get(k, 0) - s2.get(k, 0)).subs(subs), 30)
        if abs(complex(d)) > 1e-20:
            return False
    return True


rng = random.Random(SEED)
print(f"seed = {SEED}")


def rpt() -> dict:
    return {
        t1: sp.Rational(rng.randint(-90, 90), 37)
        + sp.I * sp.Rational(rng.randint(-90, 90), 41),
        t2: sp.Rational(rng.randint(-90, 90), 43)
        + sp.I * sp.Rational(rng.randint(-90, 90), 47),
        z: sp.Rational(1, 3),
        beta: sp.Rational(3, 2),
    }


points = [rpt() for _ in range(4)]

# C2-taylor ------------------------------------------------------------------
tk, h1, h2, h3, e0, e1, e2 = sp.symbols("tk h1 h2 h3 e0 e1 e2")
eta = e0 + e1 * t + e2 * t**2
hw = tk + h1 * w + h2 * w**2 + h3 * w**3
ser = sp.series(eta.subs(t, hw) / sp.diff(hw, w), w, 0, 3).removeO()
et, etp, etpp = (
    eta.subs(t, tk),
    sp.diff(eta, t).subs(t, tk),
    sp.diff(eta, t, 2).subs(t, tk),
)
pred = [
    et / h1,
    etp - 2 * h2 / h1**2 * et,
    sp.Rational(1, 2) * etpp * h1
    - h2 / h1 * etp
    + (4 * h2**2 - 3 * h1 * h3) / h1**3 * et,
]
ok = all(sp.simplify(ser.coeff(w, i) - pred[i]) == 0 for i in range(3))
record("C2-taylor", ok, "eta^{(k)}_{0,1,2} of (2.1)")
bad = pred[1] + h2 / h1**2 * et  # wrong factor 2 -> 1
record(
    "BREAK-C2-taylor",
    sp.simplify(ser.coeff(w, 1) - bad) != 0,
    "factor 1 instead of 2 is detected",
)

# C2-ward-ghost --------------------------------------------------------------
vt = beta * (t**2 - z**2)
psi = mul_c(c_field(t1), c_field(t2))
ob_hol = lin((1, apply_b(1, psi)), (-(z**2), apply_b(-1, psi)))
ward = lin((vt.subs(t, t1) / beta, c_field(t2)), (-vt.subs(t, t2) / beta, c_field(t1)))
ok = all(diff_ok(ob_hol, ward, p, LMAX) for p in points)
record("C2-ward-ghost", ok, f"(b1 - z^2 b-1) c c|0> = Ward sum, L0 <= {LMAX}")
ward_bad = lin(
    (vt.subs(t, t1) / beta, c_field(t2)), (vt.subs(t, t2) / beta, c_field(t1))
)
record(
    "BREAK-C2-ward-ghost",
    not any(diff_ok(ob_hol, ward_bad, p, LMAX) for p in points),
    "wrong relative Koszul sign fails",
)

# C3-witness-ward ------------------------------------------------------------
coef = sp.expand(ob_hol.get((0,), 0))
closed = -(t2 - t1) * (t1 * t2 + z**2)
ok = sp.simplify(coef - closed) == 0 and all(
    abs(complex(sp.N(closed.subs(p)))) > 1e-6 for p in points
)
record(
    "C3-witness-ward", ok, f"c_0|0> coeff = {sp.factor(coef)}, non-zero at random pts"
)

# C3-witness-dressed ---------------------------------------------------------
k00, k20 = sp.symbols("k00 k20")
# dressing K acts on the source sectors before O_b: weight by total L0 level of source
psiK = {
    k: a * (k00 if level(k) == -1 else k20 if level(k) == 1 else 0)
    for k, a in psi.items()
}
obK = lin((1, apply_b(1, psiK)), (-(z**2), apply_b(-1, psiK)))
coefK = sp.expand(obK.get((0,), 0))
closedK = -(t2 - t1) * (z**2 * k00 + t1 * t2 * k20)
ok = sp.simplify(coefK - closedK) == 0
record("C3-witness-dressed-transcription", ok, f"T coeff = {sp.factor(coefK)}")
# break: dressing assigned to the wrong source levels (k00 <-> k20)
psiK_bad = {
    k: a * (k20 if level(k) == -1 else k00 if level(k) == 1 else 0)
    for k, a in psi.items()
}
obK_bad = lin((1, apply_b(1, psiK_bad)), (-(z**2), apply_b(-1, psiK_bad)))
record(
    "BREAK-witness-dressed",
    sp.simplify(sp.expand(obK_bad.get((0,), 0)) - closedK) != 0,
    "swapped level assignment of k00, k20 is detected",
)

# C3-locus-dressed -----------------------------------------------------------
# ghost-carrying punctures on the zeros of vtilde: t2 = -z^2 / t1 (t1 = z: t2 = -z)
onlocus = sp.simplify(coefK.subs(t2, -(z**2) / t1))
expect = -(-(z**2) / t1 - t1) * z**2 * (k00 - k20)
record(
    "C3-locus-dressed",
    sp.simplify(onlocus - expect) == 0,
    f"t1 t2 = -z^2: T coeff = {sp.factor(onlocus)}",
)
expect_bad = -(-(z**2) / t1 - t1) * z**2 * (k00 + k20)
record(
    "BREAK-locus-dressed",
    sp.simplify(onlocus - expect_bad) != 0,
    "k00 + k20 form is detected",
)

# C3-limit and break ---------------------------------------------------------
lim = {t1: z, t2: -z, z: sp.Rational(1, 3)}
psi_l = {k: sp.sympify(a).subs(lim) for k, a in psi.items()}
zz = sp.Rational(1, 3)
ob_l = lin((1, apply_b(1, psi_l)), (-(zz**2), apply_b(-1, psi_l)))
ok = all(abs(complex(sp.N(a))) < 1e-25 for k, a in ob_l.items() if level(k) <= LMAX)
record("C3-limit", ok, "O_b^hol c(z)c(-z)|0> = 0 (all components, L0 <= LMAX)")
ob_bad = lin((1, apply_b(1, psi_l)), (zz**2, apply_b(-1, psi_l)))
ok = any(abs(complex(sp.N(a))) > 1e-6 for k, a in ob_bad.items() if level(k) <= LMAX)
record("BREAK-limit", ok, "b_1 + z^2 b_{-1} is non-zero at the same points")

nfail = sum(not r[1] for r in results)
print(f"\n{len(results) - nfail}/{len(results)} PASS")
sys.exit(1 if nfail else 0)
