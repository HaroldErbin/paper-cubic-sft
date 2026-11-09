"""Finite-model checks for record 114 (remarks on the IBL section).

Run from the project root (the project .venv lacked sympy on 2026-11-07):
    uv run --no-project --with sympy python codes/verify-ibl-remarks.py \
        [--seed N] [--out DIR] [--perturb NAME]

VERIFIED (each check named after the claim-tree node of
agent/derivations/114-ibl-remarks-check.md):
  C2.1   Ghost-number balance (K.1)-(K.2): for an n-string field of total ghost
         number 2n, distributed in any way over the strands, the n-string
         pairing (saturating 5 per strand) is nonzero only against an operator
         of ghost number n = N_gh(p_{n,n}); an operator of ghost number 1 (such
         as the derivation extension of Q_B) is allowed only for n = 1.
  C3     Grading (D.1)-(D.2): the per-strand degree s = a N_gh + b reproduces
         CFL's degree -2d(m-1)-1 for all (m, n) iff (a, b, d) = (-1, 3, 1/2);
         Harold's s = N_gh - 2 gives deg = n (no d).
  C2.3   (S.2): in a finite model (A at gh 2, B at gh 3, invertible pairing
         omega between them, 2-string pairing the tensor square), the operator
         p22 defined from V_4 is self-adjoint for the 2-string pairing iff V_4
         is pair-exchange symmetric; and with a pairing of the wrong symmetry
         self-adjointness fails even for a fully symmetric V_4 (so the pairing
         does enter, as the remark claims).
  C4.1   Kuenneth for the IBL derivation differential: on a random graded
         complex (C, Q) with N_gh in {1,..,4}, the homology of
         Qhat = Q (x) 1 + (-1)^{|.|} 1 (x) Q on the graded-symmetric square
         Sym^2 C equals Sym^2 H(Q) degree by degree (multi-particle states
         survive in the IBL canonical model).
  C4.2   Cubic-action Sigma sector: on the classical complex
         (C_2 -> C_3 by Q) (+) (Sym^2 C_2 -> Sym^2 C_3 by p22), with V_4 random
         and fully symmetric, the total cohomology equals H(C_2 -> C_3): the
         Sigma pair is acyclic (auxiliary field, no state).

Break legs (named -break, each must report the check FAILING on perturbed
input): C2.1-break (pairing saturating 6), C3-break (CFL constant -3),
C2.3-break (V_4 symmetric within pairs only), C4.1-break (Koszul sign dropped
in Qhat), C4.2-break (V_4 degenerate on Sym^2 C_2).

NOT VERIFIED: anything about the closed-string vertices themselves; CFL's
theorems (taken from the cached reviews); signs of the IBL relations on odd
inputs; infinite-dimensional statements (PH1).
"""

from __future__ import annotations

import argparse
import itertools
import random
import sys
from pathlib import Path

import sympy as sp

RESULTS: list[tuple[str, bool, str]] = []


def report(name: str, ok: bool, detail: str) -> None:
    """Record and print one named check."""
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")


# ---------------------------------------------------------------- C2.1
def check_c21(sat: int = 5) -> bool:
    """Kinetic-operator ghost number for n-string fields at total gh 2n."""
    ok = True
    for n in range(1, 7):
        # every distribution of total gh 2n over n strands, each strand gh 0..6
        allowed = set()
        for dist in itertools.product(range(0, 7), repeat=n):
            if sum(dist) != 2 * n:
                continue
            # K Phi must pair with Phi strand by strand: total gh of K Phi is
            # sat*n - 2n; the operator gh is that minus 2n
            allowed.add(sat * n - 2 * n - 2 * n)
        g_pnn = 3 * n - 2 * n
        ok &= allowed == {g_pnn}
        ok &= (1 in allowed) == (n == 1)
    return ok


# ---------------------------------------------------------------- C3
def check_c3(const: int = -1) -> tuple[bool, str]:
    """Unique affine per-strand degree matching CFL's genus-zero degrees."""
    a, b, d = sp.symbols("a b d")
    eqs = []
    for m in range(1, 5):
        for n in range(1, 5):
            g = 3 * n - 2 * m
            eqs.append(sp.Eq(a * g + b * (n - m), -2 * d * (m - 1) + const))
    sol = sp.solve(eqs, [a, b, d], dict=True)
    ok = sol == [{a: -1, b: 3, d: sp.Rational(1, 2)}]
    # Harold's proposal s = N_gh - 2: degree must be independent of n
    deg_h = {(m, n): (3 * n - 2 * m) - 2 * (n - m) for m in (1, 2) for n in (1, 2)}
    ok &= deg_h[(1, 1)] != deg_h[(1, 2)]
    return ok, f"solution {sol}; Harold s=N-2 gives deg(m,n)=n: {deg_h}"


# ---------------------------------------------------------------- helpers
def rand_mat(rng: random.Random, r: int, c: int) -> sp.Matrix:
    return sp.Matrix(r, c, lambda i, j: rng.randint(-5, 5))


def rand_invertible(rng: random.Random, n: int) -> sp.Matrix:
    while True:
        m = rand_mat(rng, n, n)
        if m.det() != 0:
            return m


def sym_tensor4(rng: random.Random, k: int, mode: str) -> dict:
    """Random 4-index tensor on a k-dim space.

    mode 'full': fully symmetric; 'pairs': symmetric within (01) and (23) only.
    """
    t = {}
    for idx in itertools.product(range(k), repeat=4):
        t[idx] = sp.Integer(rng.randint(-4, 4))
    if mode == "full":
        out = {}
        for idx in t:
            out[idx] = sum(t[p] for p in itertools.permutations(idx))
        return out
    out = {}
    for i, j, p, q in t:
        out[(i, j, p, q)] = (
            t[(i, j, p, q)] + t[(j, i, p, q)] + t[(i, j, q, p)] + t[(j, i, q, p)]
        )
    return out


# ---------------------------------------------------------------- C2.3
def check_c23(rng: random.Random, vmode: str, pair_sign: int) -> tuple[bool, str]:
    """Self-adjointness of p22 versus pair-exchange symmetry of V_4.

    omega(a_i, b_j) = M_ij.  2-string pairing:
    <x1 x2, y1 y2>_2 = omega(x1, y1) omega(x2, y2), and in the other order
    <Y, X>_2 = pair_sign <X, Y>_2 (graded symmetry on these even 2-string
    states gives pair_sign = +1; -1 is the wrong-symmetry control).  p22: A(x)A -> B(x)B with
    <X, p22 Y>_2 = V_4(X, Y) for X, Y in A(x)A.
    """
    k = 2
    M = rand_invertible(rng, k)
    V = sym_tensor4(rng, k, vmode)
    # matrix of the 2-string pairing (A(x)A) x (B(x)B): MM = M (x) M
    MM = sp.kronecker_product(M, M)
    Vmat = sp.Matrix(k * k, k * k, lambda r, c: V[(r // k, r % k, c // k, c % k)])
    P = MM.inv() * Vmat  # columns: p22(e_c) in B(x)B basis; <X,p22 Y> = X^T MM P Y
    lhs = MM * P  # <X, p22 Y>  as bilinear form X^T lhs Y
    # <p22 X, Y>_2 with p22 X in the first slot: the 2-string pairing
    # (B(x)B) x (A(x)A) is pair_sign (M (x) M)^T (pair_sign = +1: symmetric)
    MMba = pair_sign * sp.kronecker_product(M.T, M.T)
    rhs = P.T * MMba  # X^T rhs Y = (P X)^T MMba Y
    selfadj = sp.simplify(lhs - rhs) == sp.zeros(k * k, k * k)
    pairsym = Vmat == Vmat.T
    return (
        selfadj,
        f"vmode={vmode}, pair_sign={pair_sign}: self-adjoint={selfadj}, V4 pair-symmetric={pairsym}",
    )


# ---------------------------------------------------------------- C4.1
def random_complex(
    rng: random.Random, dims: dict[int, int]
) -> tuple[list[int], sp.Matrix]:
    """Graded complex with Q of degree +1, Q^2 = 0, by conjugating a normal form."""
    degs = [g for g in sorted(dims) for _ in range(dims[g])]
    n = len(degs)
    Q0 = sp.zeros(n, n)
    # normal form: pair the first free vector of degree g with one of degree g+1
    used = set()
    for g in sorted(dims):
        src = [i for i in range(n) if degs[i] == g and i not in used]
        tgt = [i for i in range(n) if degs[i] == g + 1 and i not in used]
        if src and tgt:
            i, j = src[0], tgt[0]
            Q0[j, i] = 1
            used |= {i, j}
    G = sp.zeros(n, n)
    for g in sorted(dims):
        idx = [i for i in range(n) if degs[i] == g]
        blk = rand_invertible(rng, len(idx))
        for a, i in enumerate(idx):
            for b, j in enumerate(idx):
                G[i, j] = blk[a, b]
    return degs, G * Q0 * G.inv()


def homology_dims(
    degs: list[int], Q: sp.Matrix, sub: sp.Matrix | None = None
) -> dict[int, int]:
    """dim H^g of Q (degree +1) on the span of the columns of sub (degree-pure)."""
    n = Q.shape[0]
    basis = sub if sub is not None else sp.eye(n)
    out = {}
    cols_by_deg: dict[int, list[int]] = {}
    for c in range(basis.shape[1]):
        nz = [i for i in range(n) if basis[i, c] != 0]
        cols_by_deg.setdefault(degs[nz[0]], []).append(c)
    for g, cols in cols_by_deg.items():
        Bg = basis.extract(list(range(n)), cols)
        img_out = (Q * Bg).rank()  # rank of Q on degree g
        prev = cols_by_deg.get(g - 1, [])
        img_in = (Q * basis.extract(list(range(n)), prev)).rank() if prev else 0
        out[g] = len(cols) - img_out - img_in
    return out


def check_c41(rng: random.Random, koszul: bool) -> tuple[bool, str]:
    dims = {1: 1, 2: 3, 3: 3, 4: 1}  # normal form leaves H = {2: 1, 3: 1}
    degs, Q = random_complex(rng, dims)
    n = len(degs)
    h = homology_dims(degs, Q)
    # tensor square with Koszul derivation
    I = sp.eye(n)
    S = sp.diag(*[(-1) ** degs[i] if koszul else 1 for i in range(n)])
    Qhat = sp.kronecker_product(Q, I) + sp.kronecker_product(S, Q)
    sq_ok = Qhat * Qhat == sp.zeros(n * n, n * n)
    degs2 = [degs[i] + degs[j] for i in range(n) for j in range(n)]
    # graded symmetric square: span of e_i e_j + (-1)^{|i||j|} e_j e_i
    cols = []
    for i in range(n):
        for j in range(i, n):
            v = sp.zeros(n * n, 1)
            v[i * n + j] += 1
            v[j * n + i] += (-1) ** (degs[i] * degs[j])
            if any(v):
                cols.append(v)
    Sym = sp.Matrix.hstack(*cols)
    h2 = homology_dims(degs2, Qhat, Sym) if sq_ok else {}
    # expected Sym^2 H graded
    exp: dict[int, int] = {}
    for p in h:
        for q in h:
            if p < q:
                exp[p + q] = exp.get(p + q, 0) + h[p] * h[q]
            elif p == q:
                hp = h[p]
                exp[2 * p] = exp.get(2 * p, 0) + (
                    hp * (hp + 1) // 2 if p % 2 == 0 else hp * (hp - 1) // 2
                )
    h2c = {g: v for g, v in h2.items() if v}
    expc = {g: v for g, v in exp.items() if v}
    ok = sq_ok and h2c == expc and sum(expc.values()) > 0
    return ok, f"H(Q)={h}; H(Qhat|Sym2)={h2c}; Sym2 H={expc}; Qhat^2=0: {sq_ok}"


# ---------------------------------------------------------------- C4.2
def check_c42(rng: random.Random, degenerate: bool) -> tuple[bool, str]:
    k2, k3 = 2, 2  # dim C_2, dim C_3
    Qc = rand_mat(rng, k3, k2)  # Q: C_2 -> C_3 (rank <= 2)
    Qc[:, 1] = 2 * Qc[:, 0]  # force rank 1 so that H(Q) is nonzero in both degrees
    M = rand_invertible(rng, k2)  # pairing C_2 x C_3
    V = sym_tensor4(rng, k2, "full")
    Vmat = sp.Matrix(
        k2 * k2, k2 * k2, lambda r, c: V[(r // k2, r % k2, c // k2, c % k2)]
    )
    # restrict to Sym^2 C_2 (symmetric tensors) and Sym^2 C_3
    symb = []
    for i in range(k2):
        for j in range(i, k2):
            v = sp.zeros(k2 * k2, 1)
            v[i * k2 + j] += 1
            v[j * k2 + i] += 1
            symb.append(v)
    Ssym = sp.Matrix.hstack(*symb)
    form = Ssym.T * Vmat * Ssym  # V_4 on Sym^2 C_2: the quadratic form of Sigma
    if degenerate:
        form[:, 0] = sp.zeros(form.shape[0], 1)
        form[0, :] = sp.zeros(1, form.shape[1])
    # p22 restricted, in dual coordinates: Sym^2 C_3 = (Sym^2 C_2)^* via the
    # pairing, so its matrix is the form itself up to the invertible pairing
    MM = sp.kronecker_product(M, M)
    pair_sym = Ssym.T * MM * Ssym  # pairing Sym^2 C_2 x Sym^2 C_3 (invertible)
    m2 = pair_sym.inv() * form
    # total complex: degree 0 = C_2 (+) Sym^2 C_2, degree 1 = C_3 (+) Sym^2 C_3
    d = sp.diag(Qc, m2)
    n0, n1 = d.shape[1], d.shape[0]
    r = d.rank()
    H0, H1 = n0 - r, n1 - r
    rq = Qc.rank()
    ok = (H0, H1) == (k2 - rq, k3 - rq)
    return (
        ok,
        f"total (H0,H1)=({H0},{H1}); Psi sector ({k2 - rq},{k3 - rq}); rank V4|Sym2={form.rank()}/{form.shape[0]}",
    )


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--seed", type=int, default=20261107)
    ap.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parent / "output" / "ibl-remarks",
    )
    ap.add_argument(
        "--perturb", default=None, help="name of a -break check to run as plain check"
    )
    args = ap.parse_args()
    print(f"seed = {args.seed}")
    rng = random.Random(args.seed)
    p = args.perturb

    if p is None or p == "C2.1-break":
        sat = 6 if p else 5
        report(
            "C2.1",
            check_c21(sat),
            f"kinetic gh = n = N_gh(p_nn), gh-1 operator only at n=1 (saturation {sat})",
        )
    if p is None:
        report(
            "C2.1-break", not check_c21(6), "saturation 6 per strand must break C2.1"
        )

    if p is None or p == "C3-break":
        ok, det = check_c3(-3 if p else -1)
        report("C3", ok, det)
    if p is None:
        report("C3-break", not check_c3(-3)[0], "CFL constant -3 must break C3")

    if p is None or p == "C2.3-break":
        mode = "pairs" if p else "full"
        ok, det = check_c23(rng, mode, +1)
        report("C2.3", ok, det)
    if p is None:
        ok_b, det_b = check_c23(rng, "pairs", +1)
        report("C2.3-break", not ok_b, det_b + " (must not be self-adjoint)")
        ok_s, det_s = check_c23(rng, "full", -1)
        report(
            "C2.3-pairing",
            not ok_s,
            det_s + " (wrong pairing symmetry spoils self-adjointness)",
        )

    if p is None or p == "C4.1-break":
        ok, det = check_c41(rng, koszul=(p is None))
        report("C4.1", ok, det)
    if p is None:
        ok_b, det_b = check_c41(rng, koszul=False)
        report("C4.1-break", not ok_b, det_b)

    if p is None or p == "C4.2-break":
        ok, det = check_c42(rng, degenerate=(p is not None))
        report("C4.2", ok, det)
    if p is None:
        ok_b, det_b = check_c42(rng, degenerate=True)
        report("C4.2-break", not ok_b, det_b)

    n_pass = sum(ok for _, ok, _ in RESULTS)
    print(f"SUMMARY: {n_pass}/{len(RESULTS)} PASS (seed {args.seed})")
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "verify-ibl-remarks.txt").write_text(
        "\n".join(f"{'PASS' if ok else 'FAIL'} {n}: {d}" for n, ok, d in RESULTS) + "\n"
    )
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
