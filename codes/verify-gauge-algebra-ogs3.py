r"""
Companion checks for derivations 040 and 043 (gauge algebra at O(g_s^3)).

040: closure of the gauge algebra; 043 (Part D): removability of the E_Sigma-proportional
defect.

Hubbard-Stratonovich (cubic) form of closed bosonic SFT.

WHAT IS VERIFIED
----------------
Part A ($\Psi$ sector, symbolic, generic products).
  C1.1/C1.2/C1.3 — that
      [d_1, d_2] Psi - d_{Lam12} Psi - D_Psi
  lies in the linear span of the generalised Jacobi identities J_n of the L_infty
  algebra, order by order in g_s up to g_s^3, with
      Lam12  = sum_n g^{n+1}/n! l_{n+2}(A, B, Psi^n),
      D_Psi  = sum_n g^{n+2}/n! l_{n+3}(Psi^n, A, B, F),   F the Psi equation of motion.
  Conventions: Erbin (2023), *String Field Theory: A Modern Introduction*, ch. "Homotopy
  algebras", eqs. (math:Linf-ln-sym), (math:eq:Linf-degree-ln), (math:eq:Linf-gen-Jacobi);
  degree parity |x| = 1 - N_gh(x), graded-ANTIsymmetric products, and a prefactor in J_n
  fixed to (-1)^i by the explicitly displayed n=2,3 identities of the source (see the
  comment in `jacobi`). The products l_n are UNCONSTRAINED generic symbols: the L_infty relations are
  imposed as rewriting rules (membership in their span), never solved for particular l_n
  (METHOD NOTE of the brief, R16).

Part B ($\Sigma_2$ sector, exact rational arithmetic on a finite-dimensional toy).
  C2.1/C2.2/C2.3/C2.4 — the exact identity (record 040, eq. (5.5))
      [d_1, d_2] Sigma_2 = Phi([d_1,d_2] Psi) + A,
      A = (g/10) p22^{-1} [ p32(d_1 X, u_2) - p32(d_2 X, u_1) ],
  for the gauge law (2.3) and ARBITRARY polynomial maps u_i(Psi), as an identity of
  polynomials in (Psi, Sigma_2, g).
  C2.1-unsym — with the unsymmetrised reading 2 u (x) Psi of term (a), the same identity
  fails by exactly 2 (u_2 (x) u_1 - u_1 (x) u_2), a nonzero element of Lambda^2 H_0.
  C2.6 — the g_s^2 coefficient of A equals eq. (5.9).
  C4 — the g_s -> 0 limit: dX = 0 and the commutator on Sigma_2 is 2 w (o) Psi.
  NOTE: Part B uses the law (2.3), which is only the relative-O(g_s) truncation of the
  exact law.  Its remainder A is therefore NOT the full g_s^2 remainder; Part C supersedes
  it.  Part B is kept because C2.1/C2.2/C2.1-unsym are statements about that law.

Part C ($\Sigma_2$ sector in the EXACT variables, exact rational arithmetic, N=2).
  Uses the exact gauge law of derivation 011 (B.8)-(B.9) = R17 in the variables
  (Psi, Xt), Xt = Sigma_2 - Sigma_2^*(Psi):
      dPsi = u,  dXt = R_u Xt,  R_u = (g/10) K^{-1} V_5(., Xt, u),
      K = p22 - (g/5) p32(., Psi),  Sigma_2^* = Psi (x) Psi + (g/5) K^{-1} V_5(., Psi^3).
  C2.7  — [d1,d2] Sigma_2^*(Psi) = D Sigma_2^*[[d1,d2] Psi] exactly.
  C2.8/C2.9/C2.9-g1 — the remainder E of [d1,d2] Xt starts at g^2 and equals
      E|_{g^2} = (1/100) [A_{u1}, A_{u2}] Xt,   A_w := p22^{-1} p_{3,2}(., w),
  i.e. record 040 eq. (5.12) (the split +1/50 / -1/100 behind the net 1/100 is NOT
  machine-checked, only the net coefficient is; the split was verified by hand).
  C2.9-nonzero certifies it is generically nonzero (single random draw, seed SEED).
  C2.10 — STRUCTURAL, not falsifiable: E vanishes identically at Xt = 0 by construction
  (every term of comm_X is linear in Xt), so it is consistent with, but does not by itself
  establish, proportionality to the Sigma_2 EOM.
  C2.11 — the first bracket of (5.9) is nonzero but absent from E (the X-vs-Xt artifact);
  this is the falsifiable content. Its second conjunct (E at Xt=0 vanishes) is the same
  STRUCTURAL tautology as C2.10.
  C2.12 — the COMPOSITION check for Part C (not a join of Part A and Part C):
      Delta_Sigma := [d1,d2] Sigma_2 - delta_{Lam12} Sigma_2 = Phi_exact(D_Psi) + E,
  with delta_{Lam12} Sigma_2 formed explicitly as Phi_exact(delta_{Lam12} Psi) and
  D_Psi := [d1,d2] Psi - delta_{Lam12} Psi. Lam12 (hence D_Psi's L_infty content) is
  supplied by Part A (C1.2), not by this check; the parameter variation gw is left
  arbitrary, so the identity tested reduces to linearity of Phi_exact plus C2.7/C2.8, and
  holds for whatever Lam12 Part A returns. A genuinely computational join of Part A and
  Part C is impossible: Part A is symbolic in abstract l_n, Part C explicit at N=2.

Part D (record 043, GAP-3: is the defect E removable by an admissible redefinition?).
  Same toy as Part C, with operators on Sym^2 H_0 written as matrices and bilinear forms
  as Gram matrices, truncation g^GORD_D (= g^4).
  D0    — E != 0 for the R17 representative on this data (so D3 is not vacuous).
  D1    — the admissible family is exactly R_u + K^{-1} S_u with S_u ANTIsymmetric
          (invariance of K_Psi(Xt, Xt) fixes only Sym(K_Psi R_u) = (g/10) p_{3,2}).
  D2    — E[R + dR] = E[R] + (covariant differential of dR) + [dR, dR]: E is the
          curvature of R read as a connection on field space (record 043 eq. (4.3)).
  D3    — E[Rhat] = 0 identically for Rhat_u = (d_u M^{-1/2}) M^{1/2}, with
          dR_u = Rhat_u - R_u = -(g^2/200) [A_Psi, A_u] + O(g^3): REMOVABLE, as an exact
          identity in g_s for the quintic-truncated action S_3 (record 043 A3, 011 (B.2)),
          whose entire Xt-dependence is the quadratic form K_Psi(Xt, Xt); the premise fails
          at O(g^4) once V_6, Sigma_3 enter, and the statement must be re-established there.
  D4    — that shift has K_Psi dR_u antisymmetric, i.e. it is a Henneaux-Teitelboim
          trivial symmetry (complementary to R22, where the FORCED part is symmetric).
  D5    — G^T K_Psi G = p22 for G = M^{-1/2}: in Yhat = M^{1/2} Xt the auxiliary kinetic
          form is Psi-independent and delta Yhat = 0.

WHAT IS NOT VERIFIED
--------------------
- Nothing about the actual string vertices: V_4, V_5 are generic symmetric tensors, and
  p22^{-1} is a plain matrix inverse (the quotient by ker V_4 and its consistency are PH1
  and the R38 condition/PH5, inherited from the gauge law, not tested here).
- Part C truncates the geometric series for K^{-1} at g^GORD (= g^3); that is the only
  approximation there, and it is one order above the g^2 at which the new claims live.
  The Sigma_2 gauge law itself is NOT truncated: 011 (B.8)-(B.9) is exact in g_s for the
  action S_3.  (An earlier version of this script asserted that the O(g_s^2) tail of the
  law was unknown; that was wrong, and it is what produced the order-counting error of the
  first pass of section 5.)
- Part D truncates at g^GORD_D; the all-orders flatness of Rhat is the ANALYTIC pure-gauge
  argument of record 043 section 5.2, which the script only corroborates order by order.
- C2.12 joins the two Parts at the level of the composition law; the L_infty content of
  Lam12 and D_Psi themselves is Part A's, not Part C's.
- The Psi-sector check tests the ALGEBRAIC identity, not any worldsheet input; the L_infty
  relations themselves are taken as given (Erbin 2023, Zwiebach 1993).
- D1 tests admissibility (3.2), the linear-algebraic condition, only: its generic S_u is a
  random matrix and so does not itself satisfy record 043 section 2 item 8 (algebraicity).
  Ghost number, parity, reality, quotient and algebraicity (items 5, 6, 8, 9) are checked by
  inspection, not by D1.

Most checks carry a break leg (29 checks, 12 break legs): the tested quantity is perturbed
(a coefficient or a sign) and the check is required to FAIL. Seeds are printed.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import combinations

import sympy as sp

FAILURES: list[str] = []
SEED = 20260922


def report(name: str, ok: bool, detail: str) -> None:
    """Print one PASS/FAIL line and record a failure."""
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAILURES.append(name)


def report_break(name: str, failed: bool, detail: str) -> None:
    """Record a break leg: it passes when the perturbed quantity makes the check FAIL."""
    print(f"[{'PASS' if failed else 'FAIL'}] break-{name}: {detail}")
    if not failed:
        FAILURES.append(f"break-{name}")


# ----------------------------------------------------------------------------------
# Part A — the Psi sector.  Words, canonicalisation, Jacobi identities.
# ----------------------------------------------------------------------------------

# Atoms and their degree parity |x| = 1 - N_gh (opposite to Grassmann parity).
PARITY = {"P": 1, "A": 0, "B": 0}  # Psi, Lambda_1, Lambda_2


def parity(w) -> int:
    """Return the degree parity: deg l_n = n - 2, so |l_n(x)| = n + sum |x| (mod 2)."""
    if isinstance(w, str):
        return PARITY[w]
    n = len(w)
    return (n + sum(parity(c) for c in w)) % 2


def key(w):
    """Total order on children, used only to fix a canonical ordering."""
    if isinstance(w, str):
        return (0, w)
    return (1, len(w), tuple(key(c) for c in w))


def swap_sign(x, y) -> int:
    """l(.., x, y, ..) = (-1)^{1 + |x||y|} l(.., y, x, ..)   [Erbin (math:Linf-ln-sym)]."""
    return -1 if (parity(x) * parity(y)) % 2 == 0 else 1


def canon(w):
    """Canonical form of a word; returns (sign, word) or (0, None) if the word vanishes."""
    if isinstance(w, str):
        return 1, w
    sign = 1
    kids = []
    for c in w:
        s, cc = canon(c)
        if s == 0:
            return 0, None
        sign *= s
        kids.append(cc)
    # bubble sort with the graded transposition sign
    n = len(kids)
    for i in range(n):
        for j in range(n - 1 - i):
            if key(kids[j]) > key(kids[j + 1]):
                sign *= swap_sign(kids[j], kids[j + 1])
                kids[j], kids[j + 1] = kids[j + 1], kids[j]
    for j in range(n - 1):
        if kids[j] == kids[j + 1] and swap_sign(kids[j], kids[j + 1]) == -1:
            return 0, None
    return sign, tuple(kids)


# An expression is a dict {(g_power, canonical_word): Fraction}.
def add(expr, gp, w, coeff):
    """Add `coeff * g^gp * w` to the expression, canonicalising the word."""
    s, cw = canon(w)
    if s == 0 or coeff == 0:
        return
    k = (gp, cw)
    expr[k] = expr.get(k, Fraction(0)) + s * coeff
    if expr[k] == 0:
        del expr[k]


def lin(*pairs):
    """Linear combination of expressions given as (coefficient, expression) pairs."""
    out: dict = {}
    for coeff, e in pairs:
        for k, v in e.items():
            out[k] = out.get(k, Fraction(0)) + coeff * v
            if out[k] == 0:
                del out[k]
    return out


def truncate(expr, gmax):
    """Drop all terms of g-power above `gmax`."""
    return {k: v for k, v in expr.items() if k[0] <= gmax}


def fact(n: int) -> int:
    """Exact factorial."""
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


GMAX = 3


def delta_psi(lam: str) -> dict:
    """d_Lambda Psi = sum_n g^n/n! l_{n+1}(Psi^n, Lambda)."""
    e: dict = {}
    for n in range(0, GMAX + 1):
        add(e, n, tuple(["P"] * n + [lam]), Fraction(1, fact(n)))
    return e


def eom() -> dict:
    """F(Psi) = sum_{n>=1} g^{n-1}/n! l_n(Psi^n)."""
    e: dict = {}
    for n in range(1, GMAX + 2):
        add(e, n - 1, tuple(["P"] * n), Fraction(1, fact(n)))
    return e


def derivation(expr: dict, repl: dict) -> dict:
    """Apply a parity-even derivation that sends each atom 'P' to the expression `repl`."""
    out: dict = {}
    for (gp, w), c in expr.items():
        for gp2, w2, c2 in _subst(w, repl):
            add(out, gp + gp2, w2, c * c2)
    return out


def _subst(w, repl):
    """Yield (extra g power, word, coeff) for each single substitution of a 'P' in w."""
    if isinstance(w, str):
        if w == "P":
            for (gp, rw), c in repl.items():
                yield gp, rw, c
        return
    for i, child in enumerate(w):
        for gp, nw, c in _subst(child, repl):
            yield gp, tuple(list(w[:i]) + [nw] + list(w[i + 1:])), c


def lam12() -> dict:
    """Lam12 = sum_n g^{n+1}/n! l_{n+2}(A, B, Psi^n)  — record 040 eq. (4.7)."""
    e: dict = {}
    for n in range(0, GMAX):
        add(e, n + 1, tuple(["A", "B"] + ["P"] * n), Fraction(1, fact(n)))
    return e


def delta_lam12(lam12_expr: dict) -> dict:
    """d_{Lam12} Psi = sum_m g^m/m! l_{m+1}(Psi^m, Lam12)."""
    out: dict = {}
    for m in range(0, GMAX + 1):
        for (gp, lw), c in lam12_expr.items():
            add(out, m + gp, tuple(["P"] * m + [lw]), c * Fraction(1, fact(m)))
    return out


def defect(coeff_scale=Fraction(1)) -> dict:
    """D_Psi = sum_n g^{n+2}/n! l_{n+3}(Psi^n, A, B, F)  — record 040 eq. (4.8)."""
    F = eom()
    out: dict = {}
    for n in range(0, GMAX):
        for (gp, fw), c in F.items():
            add(out, n + 2 + gp, tuple(["P"] * n + ["A", "B", fw]),
                coeff_scale * c * Fraction(1, fact(n)))
    return out


def commutator_psi() -> dict:
    """[d_1, d_2] Psi, from the L_infty law (2.1)."""
    u1, u2 = delta_psi("A"), delta_psi("B")
    return lin((1, derivation(u2, u1)), (-1, derivation(u1, u2)))


def jacobi(args: list) -> dict:
    """J_n(x_1..x_n) of Erbin (math:eq:Linf-gen-Jacobi); returns an expression at g^0."""
    n = len(args)
    e: dict = {}
    for i in range(1, n + 1):
        # Prefactor.  Erbin's general formula prints (-1)^{i(j-1)}; with the sign
        # convention used here (the Koszul sign and the permutation signature merged
        # into `swap_sign`) that value is inconsistent with the n=2 and n=3 identities
        # displayed explicitly in the same subequation block of the source -- the
        # derivation property of l_1 and the Jacobiator, which are the statements with
        # physical content.  Requiring those two fixes the prefactor to (-1)^i at
        # (i,j) = (1,2), (2,1), (1,3), (2,2), (3,1).  The n=4 instances are then a
        # prediction, and the overdetermined O(g^3) check C1.2 confirms them.
        pref = (-1) ** i
        for sub in combinations(range(n), i):
            rest = [k for k in range(n) if k not in sub]
            perm = list(sub) + rest
            sgn = 1
            for a in range(n):
                for b in range(a + 1, n):
                    if perm.index(a) > perm.index(b):
                        sgn *= swap_sign(args[a], args[b])
            inner = tuple(args[k] for k in sub)
            word = tuple([inner] + [args[k] for k in rest])
            add(e, 0, word, Fraction(pref * sgn))
    return e


def jacobi_basis() -> list[dict]:
    """All J_n instances with arguments from {P^a, A^b, B^c}, a<=2, b,c<=1, 2<=n<=4."""
    out = []
    for a in range(0, 3):
        for b in range(0, 2):
            for c in range(0, 2):
                args = ["P"] * a + ["A"] * b + ["B"] * c
                if 2 <= len(args) <= 4:
                    J = jacobi(args)
                    if J:
                        out.append(J)
    return out


def in_span(target: dict, basis: list[dict]) -> tuple[bool, int]:
    """Test exactly whether `target` lies in the span of `basis`, shifted by g powers."""
    shifted = []
    for J in basis:
        for gp in range(0, GMAX + 1):
            shifted.append({(k[0] + gp, k[1]): v for k, v in J.items()})
    words = sorted({k for e in [target] + shifted for k in e}, key=lambda t: (t[0], key(t[1])))
    if not words:
        return True, 0
    M = sp.Matrix([[sp.Rational(e.get(w, 0)) for e in shifted] for w in words])
    b = sp.Matrix([sp.Rational(target.get(w, 0)) for w in words])
    rank_M = M.rank()
    rank_Mb = M.row_join(b).rank()
    return rank_M == rank_Mb, rank_M


def part_A() -> None:
    """Run the Psi-sector checks."""
    print("\n--- Part A: the Psi sector (symbolic, generic L_infty products) ---")
    basis = jacobi_basis()
    C = commutator_psi()

    # C1.3 — orders g^0 and g^1.
    g0 = {k: v for k, v in C.items() if k[0] == 0}
    report("C1.3", not g0, f"[d1,d2]Psi at O(g^0) has {len(g0)} terms (expected 0)")

    dL = delta_lam12(lam12())
    D = defect()
    for gmax, name in ((1, "C1.1"), (2, "C1.2-order2"), (3, "C1.2")):
        E = truncate(lin((1, C), (-1, dL), (-1, D)), gmax)
        E = {k: v for k, v in E.items() if k[0] <= gmax}
        ok, rk = in_span(E, basis)
        report(name, ok, f"residual through O(g^{gmax}) in span(J_n) "
                         f"({len(E)} residual words, span rank {rk})")

    # Break legs.
    bad = lam12()
    bad[(2, canon(("A", "B", "P"))[1])] = Fraction(2)  # wrong g^2 coefficient in Lam12
    E = truncate(lin((1, C), (-1, delta_lam12(bad)), (-1, D)), 3)
    ok, _ = in_span(E, basis)
    report_break("C1.1", not ok, "Lam12 g^2 coefficient 1 -> 2 leaves the span")

    E = truncate(lin((1, C), (-1, dL), (-1, defect(Fraction(-1)))), 3)
    ok, _ = in_span(E, basis)
    report_break("C1.2", not ok, "defect coefficient +1 -> -1 leaves the span")

    bad2 = lam12()
    k3 = (3, canon(("A", "B", "P", "P"))[1])
    bad2[k3] = Fraction(1, 3)  # wrong g^3 coefficient (should be 1/2)
    E = truncate(lin((1, C), (-1, delta_lam12(bad2)), (-1, D)), 3)
    ok, _ = in_span(E, basis)
    report_break("C1.2-g3", not ok, "Lam12 g^3 coefficient 1/2 -> 1/3 leaves the span")


# ----------------------------------------------------------------------------------
# Part B — the Sigma_2 sector (exact rational arithmetic, finite-dimensional toy).
# ----------------------------------------------------------------------------------

N = 2  # dim H_0
g = sp.Symbol("g")


def sym_tensor(rank: int, rng, dim: int = N) -> dict:
    """Totally symmetric tensor of given rank on H_0 = Q^dim, exact integer entries."""
    T: dict = {}
    for idx in _multi(rank, dim):
        val = sp.Integer(rng.randint(-6, 6))
        for p in _perms(idx):
            T[p] = val
    return T


def _multi(rank: int, dim: int = N):
    if rank == 0:
        yield ()
        return
    for rest in _multi(rank - 1, dim):
        for i in range(dim):
            if not rest or i >= rest[-1]:
                yield rest + (i,)


def _perms(idx):
    from itertools import permutations
    return set(permutations(idx))


def part_B() -> None:
    """Run the Sigma_2-sector checks."""
    import random
    print(f"\n--- Part B: the Sigma_2 sector (exact, N={N}, seed {SEED}) ---")
    rng = random.Random(SEED)
    V4 = sym_tensor(4, rng)
    V5 = sym_tensor(5, rng)

    psi = sp.Matrix(N, 1, sp.symbols(f"p0:{N}"))
    Svars = {}
    for i in range(N):
        for j in range(i, N):
            Svars[(i, j)] = sp.Symbol(f"S{i}{j}")
            Svars[(j, i)] = Svars[(i, j)]
    S = sp.Matrix(N, N, lambda i, j: Svars[(i, j)])

    # p22 as a linear map Sym^2 -> (Sym^2)^*, in the redundant NxN symmetric-matrix basis.
    def p22(M):
        return sp.Matrix(N, N, lambda i, j: sum(
            V4[(i, j, k, m2)] * M[k, m2] for k in range(N) for m2 in range(N)))

    def p32(M, u):
        """p_{3,2}(M, u) in (Sym^2)^*, M in Sym^2 (sym. matrix), u in H_0."""
        return sp.Matrix(N, N, lambda i, j: sum(
            V5[(i, j, k, m2, m3)] * M[k, m2] * u[m3]
            for k in range(N) for m2 in range(N) for m3 in range(N)))

    def p32v(a, b, c):
        return sp.Matrix(N, N, lambda i, j: sum(
            V5[(i, j, k, m2, m3)] * a[k] * b[m2] * c[m3]
            for k in range(N) for m2 in range(N) for m3 in range(N)))

    # inverse of p22 on the 3-dimensional space of symmetric matrices
    pairs = [(i, j) for i in range(N) for j in range(i, N)]

    def to_vec(M):
        return sp.Matrix([M[i, j] for (i, j) in pairs])

    Mp22 = sp.zeros(len(pairs), len(pairs))
    for cidx, (k, m2) in enumerate(pairs):
        E = sp.zeros(N, N)
        E[k, m2] = 1
        E[m2, k] = 1
        Mp22[:, cidx] = to_vec(p22(E))
    Mp22inv = Mp22.inv()

    def p22inv(cov):
        v = Mp22inv * to_vec(cov)
        M = sp.zeros(N, N)
        for idx, (i, j) in enumerate(pairs):
            M[i, j] = v[idx]
            M[j, i] = v[idx]
        return M

    X = S - psi * psi.T

    def odot(a, b):
        return (a * b.T + b * a.T) / 2

    def Phi(u, sym=True):
        a = 2 * odot(u, psi) if sym else 2 * u * psi.T
        b = sp.Rational(3, 5) * g * p22inv(p32v(u, psi, psi))
        c = sp.Rational(1, 10) * g * p22inv(p32(X, u))
        return sp.expand(a + b + c)

    # generic polynomial gauge variations u_i(Psi): affine + quadratic, integer data
    def rand_u():
        c0 = sp.Matrix(N, 1, lambda i, _: sp.Integer(rng.randint(-3, 3)))
        B = sp.Matrix(N, N, lambda i, j: sp.Integer(rng.randint(-3, 3)))
        Qt = sym_tensor(3, rng)
        quad = sp.Matrix(N, 1, lambda i, _: sum(
            Qt[(i, k, m2)] * psi[k] * psi[m2] for k in range(N) for m2 in range(N)))
        return sp.expand(c0 + B * psi + quad)

    u1, u2 = rand_u(), rand_u()

    def vfield(u, sym=True):
        return u, Phi(u, sym)

    def apply_delta(expr, u, Su):
        """Directional derivative of expr along the vector field (u, Su)."""
        res = sp.zeros(expr.rows, expr.cols)
        for i in range(N):
            res += sp.diff(expr, psi[i]) * u[i]
        for (i, j) in pairs:
            res += sp.diff(expr, Svars[(i, j)]) * Su[i, j]
        return sp.expand(res)

    def commutator(sym=True):
        uu1, S1 = vfield(u1, sym)
        uu2, S2 = vfield(u2, sym)
        wpsi = sp.expand(apply_delta(uu2, uu1, S1) - apply_delta(uu1, uu2, S2))
        wS = sp.expand(apply_delta(S2, uu1, S1) - apply_delta(S1, uu2, S2))
        return wpsi, wS

    wpsi, wS = commutator(sym=True)

    # the remainder A of eq. (5.5)/(5.9)
    dX1 = sp.expand(Phi(u1) - 2 * odot(u1, psi))
    dX2 = sp.expand(Phi(u2) - 2 * odot(u2, psi))
    Arem = sp.expand(sp.Rational(1, 10) * g * p22inv(p32(dX1, u2) - p32(dX2, u1)))

    # C2.4 (and with it C2.1-C2.3): the exact identity.
    resid = sp.expand(wS - Phi(wpsi) - Arem)
    ok = all(sp.simplify(e) == 0 for e in resid)
    report("C2.4", ok, "[d1,d2]Sigma_2 = Phi([d1,d2]Psi) + A, exact in g and in the fields")

    # C2.1/C2.2/C2.3 as separate, falsifiable statements about the three terms.
    cross_a = sp.expand(2 * odot(u2, u1) - 2 * odot(u1, u2))
    report("C2.1", all(e == 0 for e in cross_a),
           "cross terms of (a) cancel in the symmetrised reading")
    cross_b = sp.expand(p32v(u2, u1, psi) - p32v(u1, u2, psi))
    report("C2.2", all(sp.simplify(e) == 0 for e in cross_b),
           "cross terms of (b) cancel by total symmetry of p_{3,2}")
    report("C2.3", sp.expand(dX1.subs(g, 0)) == sp.zeros(N, N)
           and all(sp.simplify(sp.diff(e, g).subs(g, 0)) != 0 for e in [dX1[0, 0]]),
           "dX = O(g) exactly (eq. (2.4)), so the (c) cross term is O(g^2)")

    # C2.6 — the g^2 coefficient of A equals eq. (5.9).
    A2 = sp.expand(sp.diff(Arem, g, 2).subs(g, 0) / 2)
    piece1 = sp.Rational(3, 50) * p22inv(
        p32(p22inv(p32v(u1, psi, psi)), u2) - p32(p22inv(p32v(u2, psi, psi)), u1))
    piece2 = sp.Rational(1, 100) * p22inv(
        p32(p22inv(p32(X, u1)), u2) - p32(p22inv(p32(X, u2)), u1))
    r = sp.expand(A2 - piece1 - piece2)
    report("C2.6", all(sp.simplify(e) == 0 for e in r),
           "g^2 coefficient of A equals eq. (5.9); its second bracket is proportional to X")
    report("C2.6-nonzero", any(sp.simplify(e) != 0 for e in sp.expand(piece1)),
           "the non-EOM bracket of (5.9) is generically nonzero")

    # C4 — the g_s -> 0 limit.
    wS0 = sp.expand(wS.subs(g, 0))
    lim = sp.expand(wS0 - 2 * odot(wpsi.subs(g, 0), psi))
    report("C4", all(sp.simplify(e) == 0 for e in lim),
           "at g=0 the commutator on Sigma_2 is 2 w (o) Psi and dX = 0 (R11)")

    # break legs
    bad = sp.expand(wS - Phi(wpsi) - 2 * Arem)
    report_break("C2.4", any(sp.simplify(e) != 0 for e in bad),
                 "A -> 2A breaks the identity")
    badPhi = sp.expand(wS - (Phi(wpsi) + sp.Rational(1, 5) * g
                             * p22inv(p32v(wpsi, psi, psi))) - Arem)
    report_break("C2.4-coeff", any(sp.simplify(e) != 0 for e in badPhi),
                 "3/5 -> 4/5 in term (b) of Phi breaks the identity")

    # C2.1-unsym: the unsymmetrised reading, on a Sigma_2 taking values in the full
    # tensor square H_0 (x) H_0 (a general matrix), which is what that reading requires.
    Gv = {(i, j): sp.Symbol(f"G{i}{j}") for i in range(N) for j in range(N)}
    G = sp.Matrix(N, N, lambda i, j: Gv[(i, j)])
    XG = G - psi * psi.T

    def PhiU(u, Xmat):
        a = 2 * u * psi.T
        b = sp.Rational(3, 5) * g * p22inv(p32v(u, psi, psi))
        c = sp.Rational(1, 10) * g * p22inv(p32(Xmat, u))
        return sp.expand(a + b + c)

    def apply_deltaG(expr, u, Su):
        res = sp.zeros(expr.rows, expr.cols)
        for i in range(N):
            res += sp.diff(expr, psi[i]) * u[i]
        for i in range(N):
            for j in range(N):
                res += sp.diff(expr, Gv[(i, j)]) * Su[i, j]
        return sp.expand(res)

    G1, G2 = PhiU(u1, XG), PhiU(u2, XG)
    wpsi_u = sp.expand(apply_deltaG(u2, u1, G1) - apply_deltaG(u1, u2, G2))
    wG = sp.expand(apply_deltaG(G2, u1, G1) - apply_deltaG(G1, u2, G2))
    dX1u = sp.expand(G1 - 2 * u1 * psi.T)
    dX2u = sp.expand(G2 - 2 * u2 * psi.T)
    Aremu = sp.expand(sp.Rational(1, 10) * g * p22inv(p32(dX1u, u2) - p32(dX2u, u1)))
    resid_u = sp.expand(wG - PhiU(wpsi_u, XG) - Aremu)
    expected = sp.expand(2 * (u2 * u1.T - u1 * u2.T))
    report("C2.1-unsym", all(sp.simplify(e) == 0 for e in sp.expand(resid_u - expected)),
           "unsymmetrised reading: defect is exactly 2(u2 (x) u1 - u1 (x) u2) in Lambda^2 H_0")
    report("C2.1-unsym-nonzero",
           any(sp.simplify(e) != 0 for e in expected)
           and all(sp.simplify(e) == 0 for e in sp.expand(expected + expected.T)),
           "that defect is nonzero in H_0 (x) H_0, antisymmetric, hence zero in Sym^2")


# ----------------------------------------------------------------------------------
# Part C — the Sigma_2 sector in the EXACT variables (Psi, Xt), Xt = Sigma_2 - Sigma_2^*.
# ----------------------------------------------------------------------------------

GORD = 3  # truncation order in g_s for the series inversion of K_Psi


def part_C() -> None:  # noqa: PLR0915
    r"""
    Run the exact-variable ($\Psi$, $\tilde X$) checks of record 040 section 5.

    Uses the EXACT gauge law of derivation 011 (B.8)-(B.9) = R17,
        dPsi = u,   dXt = R_u Xt,   R_u = (g/10) K^{-1} V_5(., Xt, u),
        K = p22 - (g/5) p32(., Psi),   Sigma_2^* = Psi (x) Psi + (g/5) K^{-1} v,
    with v = V_5(., Psi^3).  K^{-1} is expanded as a geometric series in g and every
    expression is truncated at g^GORD; that truncation is the ONLY approximation here,
    and it is one order above the g^2 at which the new claims live.
    """
    import random
    print(f"\n--- Part C: exact variables (Psi, Xt), N={N}, seed {SEED}, g-order {GORD} ---")
    rng = random.Random(SEED)
    V4 = sym_tensor(4, rng)
    V5 = sym_tensor(5, rng)

    psi = sp.Matrix(N, 1, sp.symbols(f"q0:{N}"))
    Xv = {}
    for i in range(N):
        for j in range(i, N):
            Xv[(i, j)] = sp.Symbol(f"T{i}{j}")
            Xv[(j, i)] = Xv[(i, j)]
    Xt = sp.Matrix(N, N, lambda i, j: Xv[(i, j)])
    pairs = [(i, j) for i in range(N) for j in range(i, N)]

    def trunc(M):
        """Drop every power of g above GORD (the series truncation)."""
        return sp.Matrix(M.rows, M.cols, lambda i, j: sum(
            c * g**k for k, c in enumerate(sp.Poly(sp.expand(M[i, j]), g).all_coeffs()[::-1])
            if k <= GORD))

    def p22(M):
        return sp.Matrix(N, N, lambda i, j: sum(
            V4[(i, j, k, m2)] * M[k, m2] for k in range(N) for m2 in range(N)))

    def p32(M, u):
        return sp.Matrix(N, N, lambda i, j: sum(
            V5[(i, j, k, m2, m3)] * M[k, m2] * u[m3]
            for k in range(N) for m2 in range(N) for m3 in range(N)))

    def p32v(a, b, c):
        return sp.Matrix(N, N, lambda i, j: sum(
            V5[(i, j, k, m2, m3)] * a[k] * b[m2] * c[m3]
            for k in range(N) for m2 in range(N) for m3 in range(N)))

    def to_vec(M):
        return sp.Matrix([M[i, j] for (i, j) in pairs])

    Mp22 = sp.zeros(len(pairs), len(pairs))
    for cidx, (k, m2) in enumerate(pairs):
        E = sp.zeros(N, N)
        E[k, m2] = 1
        E[m2, k] = 1
        Mp22[:, cidx] = to_vec(p22(E))
    Mp22inv = Mp22.inv()

    def p22inv(cov):
        v = Mp22inv * to_vec(cov)
        M = sp.zeros(N, N)
        for idx, (i, j) in enumerate(pairs):
            M[i, j] = v[idx]
            M[j, i] = v[idx]
        return M

    def A_op(M, w):
        """A_w M := p22^{-1} p_{3,2}(M, w), the building block of R and of E."""
        return p22inv(p32(M, w))

    def Kinv(cov):
        """K^{-1} cov = sum_n (g/5 A_psi)^n p22^{-1} cov, truncated at g^GORD."""
        term = p22inv(cov)
        out = term
        for _ in range(GORD):
            term = sp.expand(sp.Rational(1, 5) * g * A_op(term, psi))
            out = out + term
        return trunc(out)

    vcov = p32v(psi, psi, psi)
    Sstar = trunc(psi * psi.T + sp.Rational(1, 5) * g * Kinv(vcov))

    def R(M, w):
        """R_w M = (g/10) K^{-1} V_5(., M, w): the homogeneous rotation, 011 (B.8)."""
        return trunc(sp.Rational(1, 10) * g * Kinv(p32(M, w)))

    def rand_u():
        c0 = sp.Matrix(N, 1, lambda i, _: sp.Integer(rng.randint(-3, 3)))
        B = sp.Matrix(N, N, lambda i, j: sp.Integer(rng.randint(-3, 3)))
        Qt = sym_tensor(3, rng)
        quad = sp.Matrix(N, 1, lambda i, _: sum(
            Qt[(i, k, m2)] * psi[k] * psi[m2] for k in range(N) for m2 in range(N)))
        return sp.expand(c0 + B * psi + quad)

    u1, u2 = rand_u(), rand_u()

    def d_psi(expr, u):
        """Directional derivative along Psi only."""
        res = sp.zeros(expr.rows, expr.cols)
        for i in range(N):
            res += sp.diff(expr, psi[i]) * u[i]
        return sp.expand(res)

    def delta(expr, u):
        """Full gauge variation: dPsi = u, dXt = R_u Xt."""
        res = d_psi(expr, u)
        RX = R(Xt, u)
        for (i, j) in pairs:
            res += sp.diff(expr, Xv[(i, j)]) * RX[i, j]
        return trunc(res)

    # the commutator on Psi, computed from the law alone
    w = trunc(delta(u2, u1) - delta(u1, u2))

    # [d1,d2] of a function of Psi alone: the second derivatives cancel, leaving D f[w].
    def comm_psi_only(expr):
        return trunc(d_psi(d_psi(expr, u2), u1) - d_psi(d_psi(expr, u1), u2))

    # C2.7 — Sigma_2^* transforms with no second-derivative leftover.
    comm_star = comm_psi_only(Sstar)
    resid = trunc(comm_star - d_psi(Sstar, w))
    report("C2.7", all(sp.simplify(e) == 0 for e in resid),
           "[d1,d2] Sigma_2^*(Psi) = D Sigma_2^*[[d1,d2]Psi] exactly (2nd derivative drops)")

    # C2.8 — the exact remainder E of [d1,d2] Xt.
    comm_X = trunc(delta(R(Xt, u2), u1) - delta(R(Xt, u1), u2))
    E_exact = trunc(comm_X - R(Xt, w))
    report("C2.8", all(sp.simplify(e) == 0 for e in trunc(E_exact).subs(g, 0)),
           "the remainder E of [d1,d2] Xt starts at order g^1 or higher")

    # C2.9 — E is purely Xt-proportional and equals (g^2/100)[A_{u1}, A_{u2}] Xt at g^2.
    E2 = sp.expand(sp.diff(E_exact, g, 2).subs(g, 0) / 2)
    closed = sp.expand(sp.Rational(1, 100) * (A_op(A_op(Xt, u2), u1) - A_op(A_op(Xt, u1), u2)))
    report("C2.9", all(sp.simplify(e) == 0 for e in sp.expand(E2 - closed)),
           "E|_{g^2} = (1/100) [A_{u1}, A_{u2}] Xt  (eq. (5.12)), purely Xt-proportional")
    report("C2.9-nonzero", any(sp.simplify(e) != 0 for e in closed),
           "that coefficient is generically nonzero (single seed): "
           "the g^2 E_Sigma-proportional defect is real")
    report("C2.9-g1", all(sp.simplify(e) == 0
                          for e in sp.expand(sp.diff(E_exact, g).subs(g, 0))),
           "E has no g^1 term: the leading remainder is exactly g^2")

    # C2.10 — STRUCTURAL, not falsifiable: comm_X is linear in Xt by construction, so E
    # vanishing at Xt = 0 cannot fail for any implementation of this law. Consistent with,
    # but does not by itself establish, proportionality to the Sigma_2 EOM.
    report("C2.10", all(sp.simplify(e) == 0
                        for e in sp.expand(E_exact.subs({Xv[p]: 0 for p in pairs}))),
           "STRUCTURAL: E vanishes identically at Xt = 0 (consistent with E ~ Sigma_2 EOM)")

    # C2.11 — the 'piece1' bracket of (5.9) is NOT in the exact remainder (it was the
    # X-vs-Xt artifact).  Build it here and show it is nonzero yet absent from E. The first
    # conjunct (piece1 != 0) is the falsifiable content; the second conjunct is the same
    # STRUCTURAL tautology as C2.10.
    piece1 = sp.Rational(3, 50) * p22inv(
        p32(p22inv(p32v(u1, psi, psi)), u2) - p32(p22inv(p32v(u2, psi, psi)), u1))
    report("C2.11", any(sp.simplify(e) != 0 for e in sp.expand(piece1))
           and all(sp.simplify(e) == 0
                   for e in sp.expand(E2.subs({Xv[p]: 0 for p in pairs}))),
           "(5.9) piece 1 is nonzero but absent from E: it is the X-vs-Xt artifact "
           "(second conjunct STRUCTURAL)")

    # C2.12 — the COMPOSITION check for Part C (NOT a join of Part A and Part C): form
    # delta_{Lam12} Sigma_2 explicitly and check Delta_Sigma = Phi_exact(D_Psi) + E with
    # D_Psi := [d1,d2]Psi - delta_{Lam12}Psi. Lam12 (and hence D_Psi's L_infty content) is
    # supplied by Part A (C1.2); here it is represented by an ARBITRARY Psi-dependent
    # parameter variation gw (any vector field of the same shape), so by linearity of
    # Phi_exact the identity tested reduces to C2.7 + C2.8 plus linearity itself — no Part A
    # object enters this check computationally.
    gw = sp.expand(g * rand_u())

    def Phi_exact(y):
        """Apply the exact gauge law as a linear operator in the argument y = delta Psi."""
        return trunc(d_psi(Sstar, y) + R(Xt, y))

    Sigma2 = trunc(Sstar + Xt)
    comm_Sigma = trunc(comm_star + comm_X)
    D_Psi = trunc(w - gw)
    composition = trunc(comm_Sigma - Phi_exact(gw) - Phi_exact(D_Psi) - E_exact)
    report("C2.12", all(sp.simplify(e) == 0 for e in composition),
           "COMPOSITION: [d1,d2]Sigma_2 - delta_{Lam12}Sigma_2 = Phi_exact(D_Psi) + E")
    del Sigma2

    # break legs
    bad = trunc(comm_Sigma - Phi_exact(gw) - Phi_exact(D_Psi) - 2 * E_exact)
    report_break("C2.12", any(sp.simplify(e) != 0 for e in bad),
                 "E -> 2E breaks the composition check")
    bad2 = sp.expand(E2 - 2 * closed)
    report_break("C2.9", any(sp.simplify(e) != 0 for e in bad2),
                 "1/100 -> 2/100 breaks the closed form of E|_{g^2}")


GORD_D = 4  # truncation order in g_s for Part D (one above the g^3 of Parts A-C)


def part_D(N: int = N, gord: int = GORD_D) -> None:  # noqa: PLR0915
    r"""
    Run the GAP-3 checks of record 043 (is the closure defect E removable?).

    Operators on Sym^2 H_0 are represented as matrices in the basis E_(kl) (1 at (k,l)
    and (l,k)); bilinear forms as Gram matrices in the same basis.  With
        A_w := p22^{-1} p_{3,2}(., ., w),  M := 1 - (g/5) A_Psi,  K_Psi = p22 M,
    the R17/011 (B.8) representative is R_u = (g/10) M^{-1} A_u = -(1/2) M^{-1} d_u M,
    and the admissible family (record 043 eq. (3.2)) is R_u + K^{-1} S_u with S_u
    antisymmetric.  The candidate flat representative is Rhat_u = (d_u M^{-1/2}) M^{1/2}.

    Checks: D1 admissibility (and that it is exactly the K-symmetric condition),
    D2 the transformation law (4.3) of E, D3 E[Rhat] = 0 and the closed form (5.4),
    D4 the shift is a Henneaux-Teitelboim trivial symmetry (mu antisymmetric),
    D5 the trivialisation G^T K G = p22.  Each has a break leg; D0 re-establishes
    E[R] != 0 on the same data so that D3 is not vacuous.

    GAP-3a (record 043, line 472): parametrised by N (= dim H_0, default 2, the original
    run) and gord (= truncation order in g_s, default GORD_D = 4).  A second call with
    N=3, gord=5 extends every check (D0-D5, all break legs) to a larger H_0 and one more
    order in g_s, as an independent invocation that does not alter the default N=2 run.
    """
    import random
    print(f"\n--- Part D: GAP-3, removability of E, N={N}, seed {SEED}, g-order {gord} ---")
    # empty tag at the default (N, gord) keeps the N=2 run's printed lines byte-identical
    # (GAP-3a); the extended invocation tags its check names so FAILURES stays unambiguous.
    tag = "" if (N == 2 and gord == GORD_D) else f"-N{N}g{gord}"

    def rep(name, ok, detail):
        report(name + tag, ok, detail)

    def repb(name, ok, detail):
        report_break(name + tag, ok, detail)

    rng = random.Random(SEED)
    V4 = sym_tensor(4, rng, N)
    V5 = sym_tensor(5, rng, N)
    psi = sp.Matrix(N, 1, sp.symbols(f"q0:{N}"))
    pairs = [(i, j) for i in range(N) for j in range(i, N)]
    n = len(pairs)

    def trunc(M):
        return sp.Matrix(M.rows, M.cols, lambda i, j: sum(
            c * g**k for k, c in enumerate(sp.Poly(sp.expand(M[i, j]), g).all_coeffs()[::-1])
            if k <= gord))

    def basis(a):
        (k, m) = pairs[a]
        E = sp.zeros(N, N)
        E[k, m] = 1
        E[m, k] = 1
        return E

    def to_vec(M):
        return sp.Matrix([M[i, j] for (i, j) in pairs])

    def p22(M):
        return sp.Matrix(N, N, lambda i, j: sum(
            V4[(i, j, k, m)] * M[k, m] for k in range(N) for m in range(N)))

    def p32(M, u):
        return sp.Matrix(N, N, lambda i, j: sum(
            V5[(i, j, k, m, r)] * M[k, m] * u[r]
            for k in range(N) for m in range(N) for r in range(N)))

    # Gram matrices of the forms p22 and p32(., ., w) in the basis E_(kl)
    Gp = sp.Matrix(n, n, lambda a, b: sum(
        basis(a)[i, j] * p22(basis(b))[i, j] for i in range(N) for j in range(N)))
    Gp = sp.Matrix(Gp)
    Mp22 = sp.Matrix(n, n, lambda a, b: to_vec(p22(basis(b)))[a])
    Mp22inv = Mp22.inv()

    def A_mat(w):
        """Matrix of A_w = p22^{-1} p_{3,2}(., ., w) in the basis E_(kl)."""
        cols = [Mp22inv * to_vec(p32(basis(b), w)) for b in range(n)]
        return sp.Matrix(n, n, lambda a, b: sp.expand(cols[b][a]))

    def rand_u():
        c0 = sp.Matrix(N, 1, lambda i, _: sp.Integer(rng.randint(-3, 3)))
        B = sp.Matrix(N, N, lambda i, j: sp.Integer(rng.randint(-3, 3)))
        Qt = sym_tensor(3, rng, N)
        quad = sp.Matrix(N, 1, lambda i, _: sum(
            Qt[(i, k, m)] * psi[k] * psi[m] for k in range(N) for m in range(N)))
        return sp.expand(c0 + B * psi + quad)

    u1, u2 = rand_u(), rand_u()
    Apsi, Au1, Au2 = A_mat(psi), A_mat(u1), A_mat(u2)
    Id = sp.eye(n)
    Mop = trunc(Id - sp.Rational(1, 5) * g * Apsi)
    GK = trunc(Gp * Mop)          # Gram matrix of K_Psi
    Y = sp.Rational(1, 5) * g * Apsi

    def series(coeffs):
        """sum_k coeffs(k) Y^k, truncated (Y = (g/5) A_Psi carries one power of g)."""
        out, pw = sp.zeros(n, n), Id
        for k in range(gord + 1):
            out = out + coeffs(k) * pw
            pw = trunc(pw * Y)
        return trunc(out)

    Minv = series(lambda k: sp.Integer(1))                       # (1 - Y)^{-1}
    Gpinv = Gp.inv()                       # g-independent
    GKinv = None  # set below: K^{-1} = M^{-1} p22^{-1}, as a truncated series in g
    Mhalf = series(lambda k: sp.binomial(sp.Rational(1, 2), k) * (-1)**k)   # (1-Y)^{1/2}
    Mmhalf = series(lambda k: sp.binomial(sp.Rational(-1, 2), k) * (-1)**k)  # (1-Y)^{-1/2}
    GKinv = trunc(Minv * Gpinv)

    def d_psi(M, u):
        res = sp.zeros(M.rows, M.cols)
        for i in range(N):
            res += sp.diff(M, psi[i]) * u[i]
        return sp.expand(res)

    def R17(u, Au):
        """R_u = (g/10) M^{-1} A_u, the R17/011 (B.8) representative."""
        return trunc(sp.Rational(1, 10) * g * Minv * Au)

    def Rflat(u, Au):
        """Rhat_u = (d_u M^{-1/2}) M^{1/2}: the pure-gauge (flat) representative."""
        return trunc(d_psi(Mmhalf, u) * Mhalf)

    def is_zero(M):
        return all(sp.simplify(e) == 0 for e in sp.expand(M))

    def curvature(Rfun):
        """E[R] = d_{u1} R_{u2} - d_{u2} R_{u1} + [R_{u2}, R_{u1}] - R_w, w = [d1,d2]Psi."""
        R1, R2 = Rfun(u1, Au1), Rfun(u2, Au2)
        w = sp.expand(d_psi(u2, u1) - d_psi(u1, u2))
        Rw = Rfun(w, A_mat(w))
        return trunc(d_psi(R2, u1) - d_psi(R1, u2) + R2 * R1 - R1 * R2 - Rw)

    def sym_part(M):
        return sp.expand(M + M.T) / 2

    # --- D0: E[R] != 0 on this data (so D3 is not vacuous) ---
    E_R = curvature(R17)
    rep("D0", not is_zero(E_R),
           "E is nonzero for the R17 representative on this data (R45); D3 is not vacuous")

    # --- D1: admissibility is exactly Sym(K R_u) = (g/10) p32 ---
    adm_R = trunc(sym_part(GK * R17(u1, Au1)) - sp.Rational(1, 10) * g * Gp * Au1)
    Zc = sp.Matrix(n, n, lambda i, j: sp.Integer(rng.randint(-3, 3)))
    Santi = trunc(g**2 * (Gp * Au1 * Zc - (Gp * Au1 * Zc).T))   # antisymmetric, linear in u1
    dR_gen = trunc(GKinv * Santi)
    adm_gen = trunc(sym_part(GK * (R17(u1, Au1) + dR_gen)) - sp.Rational(1, 10) * g * Gp * Au1)
    rep("D1", is_zero(adm_R) and is_zero(adm_gen),
           "R17 is admissible, and stays admissible under R -> R + K^{-1}S with S antisym "
           "(eq. (3.2): only the K-symmetric part is fixed)")
    Ssym = trunc(g**2 * (Gp * Au1 * Zc + (Gp * Au1 * Zc).T))
    adm_bad = trunc(sym_part(GK * (R17(u1, Au1) + trunc(GKinv * Ssym)))
                    - sp.Rational(1, 10) * g * Gp * Au1)
    repb("D1", not is_zero(adm_bad),
                 "a SYMMETRIC S breaks admissibility: the freedom really is the "
                 "antisymmetric part only")

    # --- D2: the transformation law (4.3) ---
    def shift(u, Au):
        """Build a generic admissible O(g^2) shift, to test (4.3) (not the flat one)."""
        S = trunc(g**2 * (Gp * Au * Zc - (Gp * Au * Zc).T))
        return trunc(GKinv * S)

    E_shift = curvature(lambda u, Au: trunc(R17(u, Au) + shift(u, Au)))
    d1, d2 = shift(u1, Au1), shift(u2, Au2)
    R1, R2 = R17(u1, Au1), R17(u2, Au2)
    wv = sp.expand(d_psi(u2, u1) - d_psi(u1, u2))
    pred = trunc(E_R
                 + (d_psi(d2, u1) - d_psi(d1, u2) - shift(wv, A_mat(wv)))
                 + (R2 * d1 - d1 * R2) + (d2 * R1 - R1 * d2)
                 + (d2 * d1 - d1 * d2))
    rep("D2", is_zero(trunc(E_shift - pred)),
           "E[R+dR] = E[R] + (covariant d of dR) + [dR,dR]  (eq. (4.3)), both terms moving")
    repb("D2", not is_zero(trunc(E_shift - trunc(pred - (R2 * d1 - d1 * R2)
                                                         - (d2 * R1 - R1 * d2)))),
                 "dropping the cross brackets [R,dR] breaks (4.3)")

    # --- D3: the flat representative kills E, and its shift is (5.4) ---
    E_flat = curvature(Rflat)
    rep("D3", is_zero(E_flat),
           f"E[Rhat] = 0 identically through g^{gord} for Rhat = (d_u M^-1/2) M^1/2: "
           "the defect is REMOVABLE")
    dR = trunc(Rflat(u1, Au1) - R17(u1, Au1))
    closed = sp.expand(-sp.Rational(1, 200) * g**2 * (Apsi * Au1 - Au1 * Apsi))
    rep("D3-closed", is_zero(sp.expand(sp.diff(dR - closed, g, 2).subs(g, 0)))
           and is_zero(sp.expand(sp.diff(dR, g).subs(g, 0)))
           and is_zero(sp.expand(dR.subs(g, 0))),
           "the shift is dR_u = -(g^2/200)[A_Psi, A_u] + O(g^3) (eq. (5.4)), no g^0, g^1 part")
    repb("D3", not is_zero(curvature(
        lambda u, Au: trunc(R17(u, Au) - sp.Rational(1, 100) * g**2
                            * (Apsi * A_mat(u) - A_mat(u) * Apsi)))),
                 "the coefficient -1/200 is sharp: -1/100 leaves E != 0")

    # --- D4: the shift is a Henneaux-Teitelboim trivial symmetry ---
    KdR = trunc(GK * dR)
    rep("D4", is_zero(sp.expand(KdR + KdR.T)),
           "K_Psi dR_u is ANTIsymmetric: mu = -(12/g^2) K^-1 S K^-1 is antisymmetric, "
           "i.e. the shift is an HT-trivial symmetry for even fields (R22 (1))")
    KR = trunc(GK * R17(u1, Au1))
    repb("D4", not is_zero(sp.expand(KR + KR.T)) and is_zero(sp.expand(KR - KR.T)),
                 "the FORCED part K_Psi R_u is symmetric, not antisymmetric (R22): the "
                 "antisymmetry test discriminates")

    # --- D5: the trivialisation ---
    rep("D5", is_zero(trunc(Mmhalf.T * GK * Mmhalf - Gp)),
           "G^T K_Psi G = p22 for G = M^{-1/2}: Yhat = M^{1/2} Xtilde has a Psi-INDEPENDENT "
           "kinetic form")
    rep("D5-inert", is_zero(trunc(d_psi(Mhalf, u1) + Mhalf * Rflat(u1, Au1))),
           "STRUCTURAL: delta Yhat = 0 in the flat representative (integrates (5.2))")
    repb("D5", not is_zero(trunc(Mhalf.T * GK * Mhalf - Gp)),
                 "G = M^{+1/2} does NOT trivialise K_Psi: the square-root branch matters")


def main() -> int:
    """Run all checks; exit nonzero on any failure."""
    import time

    print(f"verify-gauge-algebra-ogs3 — seed {SEED}")
    part_A()
    part_B()
    part_C()
    part_D()
    # GAP-3a (record 043, line 472): a second, independent invocation of Part D at
    # N=3 (dim H_0) and one more order in g_s (gord=5), leaving the N=2/gord=4 run above
    # untouched.  Wall time is printed so a slow run can be diagnosed without re-running.
    t0 = time.time()
    part_D(N=3, gord=5)
    print(f"--- Part D (N=3, g-order 5) wall time: {time.time() - t0:.1f} s ---")
    print()
    if FAILURES:
        print(f"SUMMARY: {len(FAILURES)} FAILED: {', '.join(FAILURES)}")
        return 1
    print("SUMMARY: all checks PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
