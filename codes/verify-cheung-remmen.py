"""
Structural checks for record 099 (Cheung–Remmen cubic gravity vs the cubic HS step).

Verified:
    C2.2-shift   In a finite-dimensional model of Cheung–Remmen's eq. (18),
                 L(h, A) = -A.M(h).A - A.b(h) with M(h) = M0 - M1(h), M1 and b
                 linear in h, the local linear shift A = A' - (1/2) M0^{-1} b(h)
                 gives L = (1/4) b M0^{-1} b + (1/4) b M0^{-1} M1 M0^{-1} b
                 - A'.M(h).A' - A'.J(h, h), J(h, h) = M1(h) M0^{-1} b(h)
                 (exact polynomial identity, random integer data).
    C2.2-tower   Integrating A out exactly gives (1/4) b M(h)^{-1} b; its
                 degree-n Taylor coefficient in h is (1/4) b (M0^{-1} M1)^{n-2}
                 M0^{-1} b for n = 2..7, and the quartic one is (1/4) J M0^{-1} J.
    C2.3-D<d>    Cheung–Remmen's auxiliary kernel at sigma = eta, the quadratic
                 form (A^a_bc A^b_ad - A^a_ac A^b_bd / (D-1)) eta^cd on A^a_bc =
                 A^a_cb, is nondegenerate for D = 3, 4, 5 (exact determinant);
                 its inertia is printed and asserted indefinite.
    C2.4-map     The paper's quartic HS step, -V4(S, S) + 2 V4(S, h h), applied
                 to a quartic form factorised as V4 = (1/4) J^T M0^{-1} J, equals
                 the quartic-order part of the shifted Cheung–Remmen action
                 -A' M0 A' - A'.J(h, h) under A' = -(1/2) M0^{-1} J(S).
    C2.4-rank    For that V4, dim Sym^2 / ker V4 = rank J (the quotient of the
                 paper is the image of the composite map).
    Each check is run once more on deliberately broken input and must then
    fail (falsifiability), reported as "<name>-break".

Not verified:
    That eq. (18) is equivalent to Einstein–Hilbert (cited from Cheung–Remmen,
    arXiv:1705.00626, sec. 2.1); the finite-dimensional model stands for the
    tensor structure of eq. (18) (h, A as vectors, derivatives absorbed in the
    linear map b), so the checks establish the algebra of the shift and of the
    Hubbard–Stratonovich map, not properties of the Einstein–Hilbert vertices.
    No string vertex data enter.

Run: uv run --no-sync python codes/verify-cheung-remmen.py (from the project root).
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

SEED = 20261012
RNG = np.random.default_rng(SEED)
RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, info: str = "") -> None:
    """Store and print one labelled check."""
    RESULTS.append((name, ok, info))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")


def rand_int_matrix(n: int, m: int, lo: int = -3, hi: int = 4) -> sp.Matrix:
    """Random integer matrix (exact sympy entries)."""
    return sp.Matrix(RNG.integers(lo, hi, size=(n, m)).tolist())


def rand_sym(n: int) -> sp.Matrix:
    """Random symmetric integer matrix."""
    a = rand_int_matrix(n, n)
    return a + a.T


# ---------------------------------------------------------------- model data
NA, NH = 4, 3  # dimensions of the auxiliary and graviton spaces in the model
hs = sp.symbols(f"h0:{NH}")
ap = sp.symbols(f"a0:{NA}")
h = sp.Matrix(hs)
Ap = sp.Matrix(ap)

while True:
    M0 = rand_sym(NA)
    if M0.det() != 0:
        break
S = [rand_sym(NA) for _ in range(NH)]  # M1(h) = sum_i h_i S_i
B = rand_int_matrix(NA, NH)  # b(h) = B h stands for the derivative of h


def M1(hv: sp.Matrix) -> sp.Matrix:
    """Linear field-dependent part of the auxiliary kernel."""
    return sum((hv[i] * S[i] for i in range(NH)), sp.zeros(NA, NA))


def lag_original(hv: sp.Matrix, av: sp.Matrix, m0: sp.Matrix) -> sp.Expr:
    """Model of Cheung–Remmen eq. (18): -A.(M0 - M1(h)).A - A.b(h)."""
    return (-(av.T * (m0 - M1(hv)) * av) - av.T * (B * hv))[0]


def lag_shifted_claim(
    hv: sp.Matrix, av: sp.Matrix, m0: sp.Matrix, jsign: int = 1
) -> sp.Expr:
    """Claimed form after A = A' - M0^{-1} b / 2, as a function of (h, A')."""
    m0i = m0.inv()
    b = B * hv
    l2 = sp.Rational(1, 4) * (b.T * m0i * b)[0]
    l3 = sp.Rational(1, 4) * (b.T * m0i * M1(hv) * m0i * b)[0]
    j = M1(hv) * m0i * b
    return l2 + l3 - (av.T * (m0 - M1(hv)) * av)[0] - jsign * (av.T * j)[0]


def check_shift(m0: sp.Matrix, jsign: int) -> bool:
    """Compare the substituted original Lagrangian with the claimed form."""
    a_full = Ap - sp.Rational(1, 2) * m0.inv() * (B * h)
    lhs = sp.expand(lag_original(h, a_full, m0))
    rhs = sp.expand(lag_shifted_claim(h, Ap, m0, jsign))
    return sp.simplify(lhs - rhs) == 0


record("C2.2-shift", check_shift(M0, 1), f"(NA, NH) = ({NA}, {NH})")
record("C2.2-shift-break", not check_shift(M0, -1), "sign of A'.J flipped: must fail")

# ------------------------------------------------------------- tower, C2.2
t = sp.symbols("t")
hvals = sp.Matrix([sp.Rational(int(x), 7) for x in RNG.integers(-6, 7, size=NH)])
m_t = M0 - t * M1(hvals)
b_t = t * (B * hvals)
# exact elimination of A: L_eff = (1/4) b M^{-1} b, expanded in t (h -> t h)
l_eff = sp.Rational(1, 4) * (b_t.T * m_t.inv() * b_t)[0]
ser = sp.series(l_eff, t, 0, 8).removeO()
m0i = M0.inv()
ok_tower = True
for n in range(2, 8):
    coeff = ser.coeff(t, n)
    pred_mat = m0i
    for _ in range(n - 2):
        pred_mat = m0i * M1(hvals) * pred_mat
    pred = sp.Rational(1, 4) * ((B * hvals).T * pred_mat * (B * hvals))[0]
    ok_tower &= sp.simplify(coeff - pred) == 0
jv = M1(hvals) * m0i * (B * hvals)
quartic_ok = sp.simplify(ser.coeff(t, 4) - sp.Rational(1, 4) * (jv.T * m0i * jv)[0])
record(
    "C2.2-tower",
    bool(ok_tower and quartic_ok == 0),
    "n = 2..7 and quartic = J M0^-1 J / 4",
)
wrong = sp.Rational(1, 4) * (jv.T * m0i * jv)[0] * 2
record(
    "C2.2-tower-break",
    sp.simplify(ser.coeff(t, 4) - wrong) != 0,
    "factor 2 on quartic: must fail",
)


# -------------------------------------------------- Cheung–Remmen kernel, C2.3
def cr_kernel(dim: int, metric: list[int], coef: sp.Rational) -> sp.Matrix:
    """
    Gram matrix of Q(A, A) = (A^a_bc A^b_ad - coef A^a_ac A^b_bd) g^cd.

    Basis: A^a_bc with b <= c (symmetric pair), so dim * dim (dim + 1) / 2
    components; the symmetric bilinear form is the polarisation of Q.

    """
    pairs = [(b, c) for b in range(dim) for c in range(b, dim)]
    basis = [(a, b, c) for a in range(dim) for (b, c) in pairs]

    def comp(vec: dict, a: int, b: int, c: int) -> sp.Expr:
        key = (a, min(b, c), max(b, c))
        return vec.get(key, 0)

    def q(v: dict, w: dict) -> sp.Expr:
        tot = sp.Integer(0)
        for c in range(dim):
            g = metric[c]  # diagonal inverse metric g^cc
            for a, b in itertools.product(range(dim), repeat=2):
                tot += g * comp(v, a, b, c) * comp(w, b, a, c)
            tr_v = sum(comp(v, a, a, c) for a in range(dim))
            tr_w = sum(comp(w, b, b, c) for b in range(dim))
            tot -= coef * g * tr_v * tr_w
        return tot

    n = len(basis)
    gram = sp.zeros(n, n)
    for i, j in itertools.product(range(n), repeat=2):
        vi = {basis[i]: 1}
        vj = {basis[j]: 1}
        gram[i, j] = sp.Rational(1, 2) * (q(vi, vj) + q(vj, vi))
    return gram


def inertia(mat: sp.Matrix) -> tuple[int, int, int]:
    """(n+, n-, n0) from the float eigenvalues of a symmetric matrix."""
    ev = np.linalg.eigvalsh(np.array(mat.tolist(), dtype=float))
    tol = 1e-9 * max(1.0, float(np.max(np.abs(ev))))
    return int(np.sum(ev > tol)), int(np.sum(ev < -tol)), int(np.sum(np.abs(ev) <= tol))


for dim in (3, 4, 5):
    eta = [-1] + [1] * (dim - 1)
    gram = cr_kernel(dim, eta, sp.Rational(1, dim - 1))
    det = gram.det(method="bareiss")
    npl, nmi, nze = inertia(gram)
    record(
        f"C2.3-D{dim}",
        det != 0 and npl > 0 and nmi > 0,
        f"size {gram.shape[0]}, det = {det}, inertia (n+, n-, n0) = ({npl}, {nmi}, {nze})",
    )
# break: a degenerate inverse metric must give a degenerate kernel
gram_b = cr_kernel(3, [0, 1, 1], sp.Rational(1, 2))
record(
    "C2.3-break", gram_b.det(method="bareiss") == 0, "degenerate g^cd: det must vanish"
)

# ------------------------------------------------- HS map and quotient, C2.4
NH2 = 4
pairs2 = [(i, j) for i in range(NH2) for j in range(i, NH2)]  # basis of Sym^2
NA2 = 5
while True:
    M02 = rand_sym(NA2)
    if M02.det() != 0:
        break
# a generic bilinear composite J: Sym^2 -> R^NA2 (stands for M1(h) M0^{-1} b(h))
Jmat = rand_int_matrix(NA2, len(pairs2))
V4 = sp.Rational(1, 4) * Jmat.T * M02.inv() * Jmat  # quartic form on Sym^2

sig = sp.Matrix(sp.symbols(f"s0:{len(pairs2)}"))
h2 = sp.Matrix(sp.symbols(f"k0:{NH2}"))
hh = sp.Matrix([h2[i] * h2[j] * (1 if i == j else 2) for (i, j) in pairs2])
proj_side = (-(sig.T * V4 * sig) + 2 * (sig.T * V4 * hh))[0]


def cr_side(sign: int) -> sp.Expr:
    """Shifted Cheung–Remmen quartic-order part under A' = -M0^{-1} J(S) / 2."""
    a_of_s = -sp.Rational(1, 2) * M02.inv() * Jmat * sig
    return (-(a_of_s.T * M02 * a_of_s) - sign * (a_of_s.T * (Jmat * hh)))[0]


record("C2.4-map", sp.expand(proj_side - cr_side(1)) == 0, "S -> A' = -M0^-1 J(S)/2")
record(
    "C2.4-map-break",
    sp.expand(proj_side - cr_side(-1)) != 0,
    "source sign flipped: must fail",
)
rk_v4 = V4.rank()
rk_j = Jmat.rank()
record(
    "C2.4-rank",
    rk_v4 == rk_j == NA2,
    f"dim Sym^2 = {len(pairs2)}, rank V4 = {rk_v4}, rank J = {rk_j}",
)
# break: a J of lower rank must lower the quotient dimension
Jlow = Jmat.copy()
Jlow[0, :] = Jlow[1, :]
V4low = Jlow.T * M02.inv() * Jlow
record(
    "C2.4-rank-break",
    V4low.rank() < NA2,
    f"rank-deficient J: rank V4 = {V4low.rank()} < {NA2}",
)

# ----------------------------------------------------------------- summary
n_fail = sum(not ok for _, ok, _ in RESULTS)
print(f"seed = {SEED}; {len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
sys.exit(1 if n_fail else 0)
