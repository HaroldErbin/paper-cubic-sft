"""
Companion checks for derivation record 085 (paper gaps 3 and 4).

Gap 3 (record 085, C1): finite-dimensional model of the cubic action
`eq:all:action` with two auxiliary levels (K = 3),

    S = S0(psi) + sum_{k=2,3} [ - a_k s_k.K_k s_k + 2 a_k s_k.K_k T_k(psi, s_{k-1})
                                + b_k V_k(s_k, s_k, psi) ],      s_1 := psi,

a_k = g^{2k-2}/(2k)!, b_k = g^{2k-1}/(2k+1)!, Euclidean pairing, K_k symmetric with
a one-dimensional kernel n_k, T_2 symmetric bilinear (stand-in for Psi (x) Psi),
T_3 bilinear (stand-in for Psi (x) Sigma_2). The kernel condition
`eq:hs8:kernel-condition` is, in the model,
    clause 1:  V_k(n_k, A, B) = 0          (k = 2, 3),
    clause 2:  K_3 T_3(B, n_2) = 0.
Everything is exact (sympy rationals).

What is verified:

- C1.1: d/dt F(psi0 + t v) at t = 0, with F the action on the auxiliary solution
  (solved exactly on a complement of the kernels, as a rational function of t),
  equals v . E_psi(psi0, s*) (record 085 (1.2)). Break leg: E_psi at a
  non-stationary s* + delta differs.
- C1.1-kernel: the full gradient dS/ds vanishes at s* along the kernel directions
  too (stationarity in every direction, record 085 Step 4). Break leg
  C1.1-kernel-break: in a model violating clause 1, the complement solution is
  not stationary along the kernel (n_2 . dS/ds_2 != 0): the falsifier of the
  existence clause of C1.1. (C1.1 itself would also pass in such a model; it
  tests the chain rule, which needs stationarity only along ds*/dt.)
- C1.2: the kernel shift D = S(s + N) - S(s) equals formula (1.4) in models with a
  violated clause, and is homogeneous of degree one in psi.
- C1.3: under the condition, E_psi, E_s and F are the same at s* and s* + N.
  Break legs: with clause 1 alone violated, or clause 2 alone violated, E_psi
  changes (instance level), and the Euler identity psi . dD/dpsi = D holds
  with D != 0 (record 085 (1.6)); the Euler legs (C1.2-euler-*) are consistency
  checks only, implied by the homogeneity asserted in C1.2.
- C1.3-separation-k2, -k3: the lambda-separation (1.7) of the (=>) direction.
  For a single shift N_k = lam n_k (lam symbolic) in a model violating both
  clauses, the lam^2 and lam^1 coefficients of D, computed directly from the
  action, equal b_k V_k(n_k, n_k, psi) and
  2 a_{k+1} <s_{k+1}, K_{k+1} T_{k+1}(psi, n_k)> + 2 b_k V_k(n_k, s_k, psi), with
  no other power of lam; the specialisations s_{k+1} = 0 and s_k = 0 isolate
  the two clauses (each nonzero in the broken model, zero in the good one).
  Break leg: the coefficient a_{k+1} in place of 2 a_{k+1} fails.
- C1.3-top-clause1: necessity of clause 1 at the top level k = K isolated: in a
  model where clause 1 fails only at k = 3, a shift along n_3 alone changes
  E_psi, a shift along n_2 alone does not.

Gap 4 (record 085, C2):

- C2.1 (an illustration, not a test of the lemma: the Cartan decomposition of a
  symmetric pair satisfies rule, closure and Jacobi by Lie theory; it fails
  only on a coding error in perp_basis / proj_along_perp; C2.2 is the real
  test): sl(3, R) with omega = tr(A B), U = so(3), U^perp = symmetric traceless:
  every vertex tr(y [u, u']) with y in U^perp vanishes, [U, U] in U, Jacobi holds
  for the restricted bracket, and vertices with two legs in U^perp are nonzero
  (U is not a decoupled summand). Break leg: U' a random 5-dim subspace: some vertex with one leg in U'^perp is
  nonzero, and the bracket projected onto U' along U'^perp fails Jacobi.
- C2.1-nonorthogonal: random cyclic structure in which the vertices vanish with
  one leg in a non-orthogonal complement Y of U: l_2(U, U) has a component
  outside U ("outside" must mean U^perp).
- C2.2: random multilinear l_1, l_2, l_3 on V = U + U^perp, built from vertices
  obeying the rule: the L-infinity-shaped compositions R_1, R_2, R_3 evaluated on
  U inputs with the full maps lie in U and equal the same compositions built
  from the restricted maps (record 085 (2.3)). Break leg: with the rule
  violated, the compositions of the projected maps differ from the projection
  of the full compositions.

Not verified: the matching statement `eq:all:recovered` used in record 085 Step 5
(cited, R26), the graded signs of the string-field L-infinity relations (the
argument of (2.3) does not use their form), and the universality rule itself.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

SEED = 20261004
RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, info: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, bool(ok), info))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {info}")


# --------------------------------------------------------------------------
# Gap 3: finite-dimensional cubic action with kernel directions
# --------------------------------------------------------------------------

M, P2, P3 = 3, 4, 5  # dims of psi, sigma_2, sigma_3


def rmat(rng: np.random.Generator, r: int, c: int) -> sp.Matrix:
    """Random small-integer rational matrix."""
    return sp.Matrix(r, c, lambda i, j: sp.Rational(int(rng.integers(-4, 5)), 1))


def null_rows(n: sp.Matrix, rng: np.random.Generator, rows: int) -> sp.Matrix:
    """Random matrix R (rows x len(n)) with R n = 0."""
    basis = sp.Matrix.hstack(*n.T.nullspace())  # columns orthogonal to n
    return rmat(rng, rows, basis.shape[1]) * basis.T


def build_model(rng: np.random.Generator, clause1: bool, clause2: bool) -> dict:
    """
    Build the K = 3 model; clause1/clause2 select whether the kernel condition holds.

    Args:
        rng: random generator.
        clause1: if True, V_2 and V_3 vanish on the kernels.
        clause2: if True, K_3 T_3(B, n_2) = 0 for all B.

    Returns:
        dict: the model data.

    """
    n2 = sp.Matrix([1, 2, -1, 1])
    n3 = sp.Matrix([2, -1, 1, 0, 1])
    R2 = null_rows(n2, rng, P2)
    R3 = null_rows(n3, rng, P3)
    K2 = R2.T * R2  # symmetric, kernel span(n2) generically
    K3 = R3.T * R3
    assert K2.rank() == P2 - 1 and K3.rank() == P3 - 1
    Q = rmat(rng, M, M)
    Q = Q + Q.T
    pr2 = sp.eye(P2) - n2 * n2.T / (n2.T * n2)[0]
    pr3 = sp.eye(P3) - n3 * n3.T / (n3.T * n3)[0]

    def sym_family(dim: int, count: int) -> list[sp.Matrix]:
        out = []
        for _ in range(count):
            A = rmat(rng, dim, dim)
            out.append(A + A.T)
        return out

    # V_k(A, A', B) = A^T W_k(B) A', W_k(B) = sum_i B_i W_k^i, symmetric
    W2 = sym_family(P2, M)
    W3 = sym_family(P3, M)
    if clause1:
        W2 = [pr2 * W * pr2 for W in W2]
        W3 = [pr3 * W * pr3 for W in W3]
    # T_2(psi, psi)_a = psi^T T2[a] psi
    T2 = sym_family(M, P2)
    # T_3(B, s)_a = B^T T3[a] s  (M x P2 matrices)
    T3 = [rmat(rng, M, P2) for _ in range(P3)]
    if clause2:
        # T_3(B, s) = T3raw(B, pr2 s) + (n2-coefficient of s) (w.B) n3
        w = rmat(rng, M, 1)
        c2 = n2.T / (n2.T * n2)[0]  # row: coefficient of s along n2
        T3 = [T3[a] * pr2 + n3[a] * w * c2 for a in range(P3)]
    c3 = [sym_family(M, 1)[0] for _ in range(M)]  # cubic term of S0
    return dict(n2=n2, n3=n3, K2=K2, K3=K3, Q=Q, W2=W2, W3=W3, T2=T2, T3=T3, c3=c3)


def action(mod: dict, g: sp.Expr, psi: sp.Matrix, s2: sp.Matrix, s3: sp.Matrix):
    """The model action S(psi, s2, s3) (record 085 (1.0))."""
    a2, b2 = g**2 / 24, g**3 / 120
    a3, b3 = g**4 / 720, g**5 / 5040
    S0 = (psi.T * mod["Q"] * psi)[0] / 2 + g / 6 * sum(
        psi[i] * (psi.T * mod["c3"][i] * psi)[0] for i in range(M)
    )
    T2 = sp.Matrix([(psi.T * mod["T2"][a] * psi)[0] for a in range(P2)])
    T3 = sp.Matrix([(psi.T * mod["T3"][a] * s2)[0] for a in range(P3)])
    W2 = sum((psi[i] * mod["W2"][i] for i in range(M)), sp.zeros(P2, P2))
    W3 = sum((psi[i] * mod["W3"][i] for i in range(M)), sp.zeros(P3, P3))
    K2, K3 = mod["K2"], mod["K3"]
    S = S0
    S += -a2 * (s2.T * K2 * s2)[0] + 2 * a2 * (s2.T * K2 * T2)[0]
    S += b2 * (s2.T * W2 * s2)[0]
    S += -a3 * (s3.T * K3 * s3)[0] + 2 * a3 * (s3.T * K3 * T3)[0]
    S += b3 * (s3.T * W3 * s3)[0]
    return sp.expand(S)


def complement_basis(n: sp.Matrix) -> sp.Matrix:
    """Columns spanning the orthogonal complement of n."""
    return sp.Matrix.hstack(*n.T.nullspace())


def solve_aux_first_order(mod: dict, g, psi0: sp.Matrix, v: sp.Matrix):
    """
    Stationary point in sigma at psi0 + t v, to first order in t.

    Solved on the complements of the kernels: A(t) x = r(t) with A, r polynomial
    in t; x0 = A0^{-1} r0, x1 = A0^{-1} (r1 - A1 x0). Exact rationals, no symbolic
    inversion.

    Returns:
        tuple: (s2_0, s3_0, s2_1, s3_1), the solution and its t-derivative.

    """
    t = sp.Symbol("t")
    C2, C3 = complement_basis(mod["n2"]), complement_basis(mod["n3"])
    u = sp.Matrix(sp.symbols(f"u0:{C2.shape[1]}"))
    w = sp.Matrix(sp.symbols(f"w0:{C3.shape[1]}"))
    S = action(mod, g, psi0 + t * v, C2 * u, C3 * w)
    vars_ = list(u) + list(w)
    eqs = [sp.diff(S, x) for x in vars_]
    A, rhs = sp.linear_eq_to_matrix(eqs, vars_)
    A0, r0 = A.subs(t, 0), rhs.subs(t, 0)
    A1, r1 = A.diff(t).subs(t, 0), rhs.diff(t).subs(t, 0)
    x0 = A0.LUsolve(r0)
    x1 = A0.LUsolve(r1 - A1 * x0)
    m2 = C2.shape[1]
    return C2 * x0[:m2, :], C3 * x0[m2:, :], C2 * x1[:m2, :], C3 * x1[m2:, :]


def grad_psi(mod, g, psi_sym, s2, s3, psi_val):
    """E_psi at (psi_val, s2, s3): exact gradient of the action in psi."""
    S = action(mod, g, psi_sym, s2, s3)
    sub = dict(zip(psi_sym, psi_val))
    return sp.Matrix([sp.diff(S, x).subs(sub) for x in psi_sym])


def grad_sigma(mod, g, psi_val, s2, s3):
    """E_sigma at (psi_val, s2, s3): exact gradient of the action in sigma."""
    x2 = sp.Matrix(sp.symbols(f"x0:{P2}"))
    x3 = sp.Matrix(sp.symbols(f"y0:{P3}"))
    S = action(mod, g, psi_val, x2, x3)
    sub = dict(zip(list(x2) + list(x3), list(s2) + list(s3)))
    return sp.Matrix([sp.diff(S, x).subs(sub) for x in list(x2) + list(x3)])


def gap3(rng: np.random.Generator) -> None:
    """Checks C1.1-C1.3 of record 085."""
    g = sp.Rational(3, 10)
    psi_sym = sp.Matrix(sp.symbols(f"p0:{M}"))
    psi0 = sp.Matrix([sp.Rational(int(rng.integers(-9, 10)), 7) for _ in range(M)])
    v = sp.Matrix([sp.Rational(int(rng.integers(-9, 10)), 5) for _ in range(M)])
    t = sp.Symbol("t")

    good = build_model(rng, clause1=True, clause2=True)

    # C1.1: chain rule, exact. dF/dt is the total derivative of S along the
    # solution curve (psi0 + t v, s*(t)), with ds*/dt computed from the linear
    # solve, independently of the stationarity argument.
    s2s, s3s, s2d, s3d = solve_aux_first_order(good, g, psi0, v)
    Ft = action(good, g, psi0 + t * v, s2s + t * s2d, s3s + t * s3d)
    dF = sp.diff(Ft, t).subs(t, 0)
    Epsi = grad_psi(good, g, psi_sym, s2s, s3s, psi0)
    lhs = (v.T * Epsi)[0]
    chain = sp.simplify(dF - lhs)
    check(
        "C1.1",
        chain == 0 and (s2d.norm() != 0),
        f"dF/dt = {float(dF):.12g}, v.E_psi(s*) = {float(lhs):.12g}",
    )
    delta2 = sp.Matrix([1, 0, 2, -1])  # not in span(n2)
    Ebad = grad_psi(good, g, psi_sym, s2s + delta2, s3s, psi0)
    bad = (v.T * Ebad)[0]
    check(
        "C1.1-break",
        sp.simplify(dF - bad) != 0,
        f"non-stationary sigma: v.E_psi = {float(bad):.12g} != dF/dt (expected)",
    )

    # C1.1-kernel: stationarity along the kernel directions too
    Es = grad_sigma(good, g, psi0, s2s, s3s)
    k2 = (good["n2"].T * Es[:P2, :])[0]
    k3 = (good["n3"].T * Es[P2:, :])[0]
    full = all(sp.simplify(e) == 0 for e in Es)
    check(
        "C1.1-kernel", full and k2 == 0 and k3 == 0, "full gradient in sigma = 0 at s*"
    )
    # C1.1-kernel-break: clause 1 violated -> the complement solution is not
    # stationary along the kernel of K_2 (falsifier of the existence clause)
    kb = build_model(np.random.default_rng(SEED + 2), clause1=False, clause2=True)
    s2k, s3k, _, _ = solve_aux_first_order(kb, g, psi0, v)
    Esk = grad_sigma(kb, g, psi0, s2k, s3k)
    kb2 = sp.simplify((kb["n2"].T * Esk[:P2, :])[0])
    kb3 = sp.simplify((kb["n3"].T * Esk[P2:, :])[0])
    check(
        "C1.1-kernel-break",
        kb2 != 0 or kb3 != 0,
        f"clause 1 violated: n2.dS/ds2 = {float(kb2):.4g}, n3.dS/ds3 = "
        f"{float(kb3):.4g} at the complement solution (nonzero expected)",
    )

    # C1.3: representative independence under the condition
    lam2, lam3 = sp.Rational(7, 3), sp.Rational(-5, 4)
    N2, N3 = lam2 * good["n2"], lam3 * good["n3"]
    E1 = grad_psi(good, g, psi_sym, s2s + N2, s3s + N3, psi0)
    Es1 = grad_sigma(good, g, psi0, s2s + N2, s3s + N3)
    F0 = action(good, g, psi0, s2s, s3s)
    F1 = action(good, g, psi0, s2s + N2, s3s + N3)
    ok = (E1 - Epsi).applyfunc(sp.simplify) == sp.zeros(M, 1)
    ok = ok and all(sp.simplify(e) == 0 for e in Es1) and sp.simplify(F1 - F0) == 0
    check("C1.3", ok, "E_psi, E_sigma, F unchanged under s* -> s* + N")

    # break legs: each clause alone violated
    for label, c1, c2 in (("clause1", False, True), ("clause2", True, False)):
        mod = build_model(np.random.default_rng(SEED + 1), clause1=c1, clause2=c2)
        s2b = sp.Matrix([sp.Rational(int(rng.integers(-5, 6)), 3) for _ in range(P2)])
        s3b = sp.Matrix([sp.Rational(int(rng.integers(-5, 6)), 3) for _ in range(P3)])
        Ea = grad_psi(mod, g, psi_sym, s2b, s3b, psi0)
        Eb = grad_psi(mod, g, psi_sym, s2b + N2, s3b + N3, psi0)
        diff = (Eb - Ea).applyfunc(sp.simplify)
        check(
            f"C1.3-break-{label}",
            diff != sp.zeros(M, 1),
            f"|Delta E_psi|_inf = {float(max(abs(x) for x in diff)):.3e} (nonzero expected)",
        )
        # C1.2: D equals (1.4) and is linear in psi; Euler identity (1.6)
        b2, b3, a3 = g**3 / 120, g**5 / 5040, g**4 / 720
        D = sp.expand(
            action(mod, g, psi_sym, s2b + N2, s3b + N3)
            - action(mod, g, psi_sym, s2b, s3b)
        )
        W2 = sum((psi_sym[i] * mod["W2"][i] for i in range(M)), sp.zeros(P2, P2))
        W3 = sum((psi_sym[i] * mod["W3"][i] for i in range(M)), sp.zeros(P3, P3))
        T3N = sp.Matrix([(psi_sym.T * mod["T3"][a] * N2)[0] for a in range(P3)])
        D14 = (
            2 * a3 * (s3b.T * mod["K3"] * T3N)[0]
            + b2 * (2 * (N2.T * W2 * s2b)[0] + (N2.T * W2 * N2)[0])
            + b3 * (2 * (N3.T * W3 * s3b)[0] + (N3.T * W3 * N3)[0])
        )
        lin = (
            sp.Poly(D, *psi_sym).is_homogeneous
            and sp.Poly(D, *psi_sym).total_degree() == 1
        )
        check(
            f"C1.2-{label}",
            sp.simplify(D - sp.expand(D14)) == 0 and lin and D != 0,
            "D = (1.4), homogeneous of degree one in psi, nonzero",
        )
        euler = sum(psi_sym[i] * sp.diff(D, psi_sym[i]) for i in range(M))
        check(
            f"C1.2-euler-{label}",
            sp.expand(euler - D) == 0,
            "psi.dD/dpsi = D (consistency; implied by homogeneity)",
        )

    separation(rng, g, psi_sym, psi0)


def separation(rng: np.random.Generator, g, psi_sym, psi0) -> None:
    """
    Check the lambda-separation (1.7) of record 085 and its specialisations.

    For a single kernel shift N_k = lam n_k the shift D of the action is a
    polynomial in lam; its lam^2 and lam^1 coefficients must be the two sides of
    (1.7), and setting s_{k+1} = 0 or s_k = 0 must isolate clause 1 or clause 2.

    """
    lam = sp.Symbol("lam")
    a3 = g**4 / 720
    bk = {2: g**3 / 120, 3: g**5 / 5040}
    bad = build_model(np.random.default_rng(SEED + 3), clause1=False, clause2=False)
    good = build_model(np.random.default_rng(SEED + 4), clause1=True, clause2=True)
    s2 = sp.Matrix(sp.symbols(f"x0:{P2}"))
    s3 = sp.Matrix(sp.symbols(f"y0:{P3}"))

    def pieces(mod: dict, k: int):
        n = mod[f"n{k}"]
        N2 = lam * n if k == 2 else sp.zeros(P2, 1)
        N3 = lam * n if k == 3 else sp.zeros(P3, 1)
        D = sp.expand(
            action(mod, g, psi_sym, s2 + N2, s3 + N3) - action(mod, g, psi_sym, s2, s3)
        )
        poly = sp.Poly(D, lam)
        W = sum(
            (psi_sym[i] * mod[f"W{k}"][i] for i in range(M)),
            sp.zeros(P2 if k == 2 else P3, P2 if k == 2 else P3),
        )
        sk = s2 if k == 2 else s3
        vnn = sp.expand(bk[k] * (n.T * W * n)[0])
        vns = sp.expand(2 * bk[k] * (n.T * W * sk)[0])
        if k == 2:
            T3n = sp.Matrix([(psi_sym.T * mod["T3"][a] * n)[0] for a in range(P3)])
            src = sp.expand(2 * a3 * (s3.T * mod["K3"] * T3n)[0])
            src_wrong = sp.expand(a3 * (s3.T * mod["K3"] * T3n)[0])
        else:
            src = src_wrong = sp.Integer(0)  # no Sigma_4 at K = 3
        return poly, vnn, vns, src, src_wrong

    for k in (2, 3):
        poly, vnn, vns, src, src_wrong = pieces(bad, k)
        c2 = sp.expand(poly.coeff_monomial(lam**2))
        c1 = sp.expand(poly.coeff_monomial(lam))
        only = set(m[0] for m in poly.monoms()) <= {1, 2}
        ok = only and sp.expand(c2 - vnn) == 0 and sp.expand(c1 - vns - src) == 0
        ok = ok and vnn != 0 and vns != 0 and (k == 3 or src != 0)
        # specialisations: s_{k+1} = 0 leaves the clause-1 term, s_k = 0 the
        # clause-2 term
        zero_up = {y: 0 for y in s3} if k == 2 else {}
        zero_k = {x: 0 for x in (s2 if k == 2 else s3)}
        ok = ok and sp.expand(c1.subs(zero_up) - vns) == 0
        ok = ok and sp.expand(c1.subs(zero_k) - src) == 0
        # good model: both coefficients vanish identically
        pg, _, _, _, _ = pieces(good, k)
        ok = ok and pg.is_zero
        check(
            f"C1.3-separation-k{k}",
            ok,
            "lam^2 coeff = b_k V(n,n,psi), lam^1 coeff = 2 a_{k+1} <s_{k+1}, K T(psi,n)>"
            " + 2 b_k V(n,s_k,psi); s_{k+1}=0 / s_k=0 isolate the clauses; 0 in the"
            " good model",
        )
        if k == 2:
            wrong = sp.expand(c1 - vns - src_wrong) == 0
            check(
                "C1.3-separation-break",
                not wrong,
                "coefficient a_3 in place of 2 a_3 in (1.7): mismatch detected",
            )

    # top level isolated: clause 1 fails only at k = 3
    top = build_model(np.random.default_rng(SEED + 4), clause1=True, clause2=True)
    W3 = []
    for _ in range(M):
        A = rmat(rng, P3, P3)
        W3.append(A + A.T)
    top["W3"] = W3
    s2b = sp.Matrix([sp.Rational(int(rng.integers(-5, 6)), 3) for _ in range(P2)])
    s3b = sp.Matrix([sp.Rational(int(rng.integers(-5, 6)), 3) for _ in range(P3)])
    E0 = grad_psi(top, g, psi_sym, s2b, s3b, psi0)
    E3 = grad_psi(top, g, psi_sym, s2b, s3b + sp.Rational(3, 2) * top["n3"], psi0)
    E2 = grad_psi(top, g, psi_sym, s2b + sp.Rational(3, 2) * top["n2"], s3b, psi0)
    d3 = (E3 - E0).applyfunc(sp.simplify)
    d2 = (E2 - E0).applyfunc(sp.simplify)
    check(
        "C1.3-top-clause1",
        d3 != sp.zeros(M, 1) and d2 == sp.zeros(M, 1),
        f"clause 1 broken at k = 3 only: |Delta E_psi| along n3 = "
        f"{float(max(abs(x) for x in d3)):.3e} (nonzero), along n2 = 0",
    )


# --------------------------------------------------------------------------
# Gap 4: closure of the products on a subspace
# --------------------------------------------------------------------------


def sl3_basis() -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Bases of so(3) (antisymmetric) and of symmetric traceless 3x3 matrices."""
    so3, sym = [], []
    for i, j in itertools.combinations(range(3), 2):
        A = np.zeros((3, 3))
        A[i, j], A[j, i] = 1, -1
        so3.append(A)
        S = np.zeros((3, 3))
        S[i, j] = S[j, i] = 1
        sym.append(S)
    sym.append(np.diag([1.0, -1.0, 0.0]))
    sym.append(np.diag([1.0, 1.0, -2.0]))
    return so3, sym


def flat(A: np.ndarray) -> np.ndarray:
    return A.reshape(-1)


def proj_along_perp(U: list[np.ndarray]) -> callable:
    """Projector of sl(3) onto span U along U^perp (omega = tr(A B))."""
    G = np.array([[np.trace(a @ b) for b in U] for a in U])  # Gram on U
    Ginv = np.linalg.inv(G)

    def P(X: np.ndarray) -> np.ndarray:
        c = Ginv @ np.array([np.trace(a @ X) for a in U])
        return sum(ci * a for ci, a in zip(c, U))

    return P


def jacobi(br, a, b, c) -> np.ndarray:
    return br(a, br(b, c)) + br(b, br(c, a)) + br(c, br(a, b))


def perp_basis(U: list[np.ndarray], full: list[np.ndarray]) -> list[np.ndarray]:
    """Basis of U^perp in span(full) for omega = tr(A B)."""
    Om = np.array([[np.trace(u @ f) for f in full] for u in U])
    _, s, vh = np.linalg.svd(Om)
    null = vh[len(U) :]
    return [sum(c * f for c, f in zip(row, full)) for row in null]


def gap4(rng: np.random.Generator) -> None:
    """Checks C2.1, C2.2 of record 085."""
    so3, sym = sl3_basis()
    full = so3 + sym
    br = lambda a, b: a @ b - b @ a  # noqa: E731
    V3 = lambda a, b, c: np.trace(a @ br(b, c))  # noqa: E731
    tol = 1e-12

    # C2.1: U = so(3)
    Uperp = perp_basis(so3, full)
    one_out = max(abs(V3(y, u, w)) for y in Uperp for u in so3 for w in so3)
    P = proj_along_perp(so3)
    closure = max(np.linalg.norm(br(u, w) - P(br(u, w))) for u in so3 for w in so3)
    jac = max(
        np.linalg.norm(jacobi(lambda x, y: P(br(x, y)), a, b, c))
        for a, b, c in itertools.product(so3, repeat=3)
    )
    two_out = max(abs(V3(u, y, z)) for u in so3 for y in Uperp for z in Uperp)
    check(
        "C2.1",
        one_out < tol and closure < tol and jac < tol and two_out > 0.1,
        f"max|V(y,u,u')| = {one_out:.1e}, closure defect {closure:.1e}, "
        f"Jacobi on U {jac:.1e}, max|V(u,y,y')| = {two_out:.2f} (nonzero)",
    )

    # break: U' a seeded random 5-dim subspace of sl(3), not a subalgebra. A cyclic
    # bracket is a 3-form f_abc; in dim <= 4 every 3-form is decomposable and the
    # bracket is a cross product (plus a centre), hence always Lie, so the Jacobi
    # leg needs dim U' >= 5 (found when 3- and 4-dim choices gave Jacobi = 0).
    coef = rng.normal(size=(5, 8))
    Up = [sum(c * f for c, f in zip(row, full)) for row in coef]
    Upperp = perp_basis(Up, full)
    one_out_b = max(abs(V3(y, u, w)) for y in Upperp for u in Up for w in Up)
    Pp = proj_along_perp(Up)
    jac_b = max(
        np.linalg.norm(jacobi(lambda x, y: Pp(br(x, y)), a, b, c))
        for a, b, c in itertools.product(Up, repeat=3)
    )
    check(
        "C2.1-break",
        one_out_b > 1e-3 and jac_b > 1e-3,
        f"U' not closed: max|V(y,u,u')| = {one_out_b:.3f}, projected Jacobi {jac_b:.3f}",
    )

    # C2.1-nonorthogonal: rule with a non-orthogonal complement Y does not close
    d = 3
    n = 2 * d
    Om = rng.normal(size=(n, n))
    Om = Om + Om.T  # omega, U = e_0..e_2 and Y = e_3..e_5 not orthogonal
    V = rng.normal(size=(n, n, n))
    V = sum(np.transpose(V, p) for p in itertools.permutations(range(3))) / 6
    for idx in itertools.product(range(n), repeat=3):
        if sum(i >= d for i in idx) == 1:  # exactly one leg in Y
            V[idx] = 0.0
    l2 = np.einsum("ab,bcd->acd", np.linalg.inv(Om), V)  # omega(x, l2(u,w)) = V(x,u,w)
    outY = np.abs(l2[d:, :d, :d]).max()
    check(
        "C2.1-nonorthogonal",
        outY > 1e-3,
        f"Y-component of l2(U,U) = {outY:.3f} (nonzero: outside must mean U^perp)",
    )

    # C2.2: random l1, l2, l3 built from vertices obeying the rule
    def build(rule: bool):
        A = rng.normal(size=(d, d))
        B = rng.normal(size=(d, d))
        Om = np.zeros((n, n))
        Om[:d, :d], Om[d:, d:] = A + A.T, B + B.T  # U and Y = U^perp orthogonal
        Omi = np.linalg.inv(Om)
        ls = []
        for k in (2, 3, 4):  # vertices V_k -> l_{k-1}
            T = rng.normal(size=(n,) * k)
            T = sum(np.transpose(T, p) for p in itertools.permutations(range(k)))
            if rule:
                for idx in itertools.product(range(n), repeat=k):
                    if sum(i >= d for i in idx) == 1:
                        T[idx] = 0.0
            ls.append(np.tensordot(Omi, T, axes=([1], [0])))
        return Om, ls

    def apply(l: np.ndarray, *args: np.ndarray) -> np.ndarray:
        out = l
        for a in args:
            out = np.tensordot(out, a, axes=([1], [0]))
        return out

    def relations(l1, l2, l3, x, y, z):
        """Symmetric L-infinity-shaped compositions (signs: all inputs even)."""
        R1 = apply(l1, apply(l1, x))
        R2 = (
            apply(l1, apply(l2, x, y))
            + apply(l2, apply(l1, x), y)
            + apply(l2, x, apply(l1, y))
        )
        R3 = (
            apply(l1, apply(l3, x, y, z))
            + apply(l2, apply(l2, x, y), z)
            + apply(l2, apply(l2, y, z), x)
            + apply(l2, apply(l2, z, x), y)
            + apply(l3, apply(l1, x), y, z)
            + apply(l3, x, apply(l1, y), z)
            + apply(l3, x, y, apply(l1, z))
        )
        return [R1, R2, R3]

    for rule, name in ((True, "C2.2"), (False, "C2.2-break")):
        Om, (l1, l2, l3) = build(rule)
        # restricted maps: U-block of the inputs, output projected onto U along Y
        PU = np.zeros((n, n))
        PU[:d, :d] = np.eye(d)
        r1 = np.einsum("ab,bc->ac", PU, l1)
        r2 = np.einsum("ab,bcd->acd", PU, l2)
        r3 = np.einsum("ab,bcde->acde", PU, l3)
        x, y, z = (np.concatenate([rng.normal(size=d), np.zeros(d)]) for _ in range(3))
        full_R = relations(l1, l2, l3, x, y, z)
        restr_R = relations(r1, r2, r3, x, y, z)
        dev = max(np.linalg.norm(PU @ F - G) for F, G in zip(full_R, restr_R))
        leak = max(np.linalg.norm(F - PU @ F) for F in full_R)
        scale = max(np.linalg.norm(F) for F in full_R)
        if rule:
            check(
                name,
                dev < 1e-10 * scale and leak < 1e-10 * scale,
                f"R_n|_U = R_n^U: dev {dev:.1e}, outside-U part {leak:.1e} (scale {scale:.1e})",
            )
        else:
            check(
                name,
                dev > 1e-3 * scale,
                f"rule violated: projected relations differ, dev {dev:.3e} (scale {scale:.1e})",
            )


def main() -> int:
    print(f"seed = {SEED}")
    rng = np.random.default_rng(SEED)
    gap3(rng)
    gap4(rng)
    n_fail = sum(not ok for _, ok, _ in RESULTS)
    print(f"\n{len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
