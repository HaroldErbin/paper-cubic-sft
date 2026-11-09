"""
Verify record 055: graded exchange symmetry of omega_k = omega_1^{(x)k}.

Physical statistics eps = N_gh mod 2 (record 002 REVISION-2). Toy graded space H
with basis states at N_gh = 1, 2, 2, 3, 3, 4 (parities 1, 0, 0, 1, 1, 0);
omega_1 pairs N_gh 1<->4 and 2<->3 (sum 5, record 002 eq. R2.4), with generic
random entries and exchange sign (A3 of 055)

    omega_1(B, A) = s (-1)^{eps(A) eps(B)} omega_1(A, B),   s = +-1,

s = -1 being record 002 eq. R2.6 and s = +1 the book relation
<A,B> = (-1)^{(1+|A|)(1+|B|)} <B,A> (Erbin 2023, bos:eq:closed-product-rearrangement)
restricted to the support. omega_k is the Koszul tensor of forms (055 A4):

    omega_k(X, Y) = (-1)^{sum_{i<j} eps(y_i) eps(x_j)} prod_i omega_1(x_i, y_i).

Checks (named after the claim-tree nodes of 055):
  C1.1  exchange law omega_k(Y,X) = s^k (-1)^{eps(X)eps(Y)} omega_k(X,Y), k=1..5, s=+-1,
        random homogeneous basis tensors (on and off support).
  C1.2  the other two groupings of the c0^- insertions (odd-map Koszul tensor,
        operator insertion (c0^-)^{(x)k} + BPZ) obey the same exchange law.
  C1.3  map-Koszul grouping differs from A4 by the constant (-1)^{k(k-1)/2} on support.
  C2.1  S_k covariance on support: omega_k(pi X, pi Y) = sgn(pi) omega_k(X, Y).
  C2.2  omega_k vanishes identically on H_0^{(x)k} x H_0^{(x)k} (N_gh 2 strands).
  C2.3  Sym^k H_0 pairs with the Koszul-antisymmetric (component-symmetric) part of
        H_3^{(x)k} only; that pairing is non-degenerate (rank = dim Sym^k H_0).
  C3.1  kinetic-term consistency: with omega_1(A, Q B) = omega_1(Q A, B) on even A, B,
        the form omega_1(Psi, Q Psi) vanishes identically iff s = -1.
  C3.1b the book's derivation line -(-1)^{|A|(1+|B|)}(-1)^{|B|} equals
        (-1)^{(1+|A|)(1+|B|)} and gives s = +1 on support.
  C3.2  Route C ordering: omega_k(sigma, lambda) = s^k omega_k(lambda, sigma).
  C3.3  028 reversal sign: Koszul reversal of k odd strands = (-1)^{k(k-1)/2}.
Break legs (must FAIL, reported as PASS when they do fail):
  BRK1  naive nearest-neighbour extension of R2.7's Koszul sign fails at k=3.
  BRK2  the guess sigma_k = k(k-1)/2 fails at some k in 2..5 for both s.
  BRK3  exchange law with s^k replaced by s^{k+1} fails.

Not verified: worldsheet evaluation of <A|c0^-|B> on the level-matched space;
the value of s itself beyond the book relation and the kinetic-term argument (C3.1);
Grassmann-odd component coefficients (toy components commute).

Run: .venv/bin/python codes/verify-omega-k.py   (VERIFY_SEED overrides the seed)
"""

from __future__ import annotations

import itertools
import math
import os
import sys

import numpy as np

SEED = int(os.environ.get("VERIFY_SEED", 20260926))
rng = np.random.default_rng(SEED)
RESULTS: list[tuple[str, bool]] = []
TOL = 1e-10

NGH = [1, 2, 2, 3, 3, 4]
PAR = [g % 2 for g in NGH]
D = len(NGH)
H0 = [1, 2]  # N_gh = 2 (even), the tower's strands
H3 = [3, 4]  # N_gh = 3 (odd), Route C multiplier strands


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print a named PASS/FAIL line."""
    RESULTS.append((name, bool(ok)))
    print(
        f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else "")
    )


def make_omega1(s: int) -> np.ndarray:
    """Build a generic omega_1 on the toy with exchange sign s (055 A3)."""
    w = np.zeros((D, D))
    for a in range(D):
        for b in range(D):
            if NGH[a] + NGH[b] == 5 and NGH[a] < NGH[b]:
                w[a, b] = rng.normal()
    for a in range(D):
        for b in range(D):
            if NGH[a] + NGH[b] == 5 and NGH[a] > NGH[b]:
                w[a, b] = s * (-1) ** (PAR[a] * PAR[b]) * w[b, a]
    return w


def eps(t: tuple[int, ...]) -> int:
    """Physical parity of a basis tensor."""
    return sum(PAR[i] for i in t) % 2


def kappa(X, Y) -> int:
    """Koszul shuffle exponent of A4: sum_{i<j} eps(y_i) eps(x_j)."""
    k = len(X)
    return sum(PAR[Y[i]] * PAR[X[j]] for i in range(k) for j in range(i + 1, k))


def omega_k(w, X, Y, rule: str = "A4") -> float:
    """omega_1^{(x)k} on basis tensors, for several sign rules."""
    k = len(X)
    prod = math.prod(w[X[i], Y[i]] for i in range(k))
    if rule == "A4":
        e = kappa(X, Y)
    elif rule == "map":  # tensor of odd maps: extra sum_{i<j} (eps(x_i)+eps(y_i))
        e = kappa(X, Y) + sum((PAR[X[i]] + PAR[Y[i]]) * (k - 1 - i) for i in range(k))
    elif rule == "op":  # (c0^-)^{(x)k} on Y, then BPZ tensor pairing with X
        e = sum(PAR[Y[i]] * (k - 1 - i) for i in range(k))  # c0^- past y's
        e += sum((PAR[Y[i]] + 1) * PAR[X[j]] for i in range(k) for j in range(i + 1, k))
    elif rule == "naive":  # nearest-neighbour extension of R2.7 (wrong for k>=3)
        e = sum(PAR[Y[i]] * PAR[X[i + 1]] for i in range(k - 1))
    else:
        raise ValueError(rule)
    return (-1) ** (e % 2) * prod


def random_pair(k: int, on_support: float = 0.85):
    """Random basis tensors X, Y; Y strand paired with X strand with prob on_support."""
    X = tuple(int(rng.integers(D)) for _ in range(k))
    Y = []
    for x in X:
        partners = [b for b in range(D) if NGH[x] + NGH[b] == 5]
        Y.append(
            int(rng.choice(partners))
            if rng.random() < on_support
            else int(rng.integers(D))
        )
    return X, tuple(Y)


def exchange_violations(w, k, s_pow, rule="A4", n=1500, extra=0) -> tuple[int, int]:
    """Count violations of omega(Y,X) = s_pow (-1)^{eps eps + extra} omega(X,Y)."""
    bad = nonzero = 0
    for _ in range(n):
        X, Y = random_pair(k)
        lhs = omega_k(w, Y, X, rule)
        rhs = s_pow * (-1) ** ((eps(X) * eps(Y) + extra) % 2) * omega_k(w, X, Y, rule)
        nonzero += abs(lhs) > TOL
        bad += abs(lhs - rhs) > TOL * (1 + abs(lhs))
    return bad, nonzero


print(f"seed = {SEED}")

# ---------------------------------------------------------------- C1: exchange law
for s in (+1, -1):
    w = make_omega1(s)
    for k in range(1, 6):
        bad, nz = exchange_violations(w, k, s**k)
        check(
            f"C1.1 exchange law s={s:+d} k={k}",
            bad == 0 and nz > 50,
            f"viol={bad}, nonzero={nz}",
        )
        for rule in ("map", "op"):
            bad, nz = exchange_violations(w, k, s**k, rule=rule)
            check(
                f"C1.2 grouping '{rule}' same law s={s:+d} k={k}",
                bad == 0 and nz > 50,
                f"viol={bad}",
            )

    # C1.3: map-Koszul grouping = (-1)^{k(k-1)/2} x A4 on support
    for k in range(1, 6):
        ok = True
        for _ in range(400):
            X, Y = random_pair(k, on_support=1.0)
            a, b = omega_k(w, X, Y, "A4"), omega_k(w, X, Y, "map")
            ok &= abs(b - (-1) ** (k * (k - 1) // 2) * a) < TOL * (1 + abs(a))
        check(f"C1.3 map grouping = (-1)^(k(k-1)/2) * A4 on support s={s:+d} k={k}", ok)

    # break legs
    w3 = w
    bad, _ = exchange_violations(w3, 3, s**3, rule="naive")
    check(
        f"BRK1 naive nearest-neighbour Koszul fails at k=3 (s={s:+d})",
        bad > 0,
        f"viol={bad}",
    )
    fails = []
    for k in range(2, 6):
        # guess: omega(Y,X) = (-1)^{eps eps + k(k-1)/2} omega(X,Y)
        bad, _ = exchange_violations(w, k, 1, extra=k * (k - 1) // 2)
        fails.append(bad > 0)
    check(
        f"BRK2 guess sigma_k=k(k-1)/2 fails for some k (s={s:+d})",
        any(fails),
        f"fails at k={[k for k, f in zip(range(2, 6), fails, strict=True) if f]}",
    )
    bad, _ = exchange_violations(w, 3, s**4)
    check(
        f"BRK3 wrong power s^(k+1) fails at k=3 (s={s:+d})",
        (bad > 0) == (s == -1),
        f"viol={bad}",
    )


# ---------------------------------------------------------------- C2: restrictions
def koszul_perm_sign(t, perm) -> int:
    """Koszul sign of permuting the strands of basis tensor t by perm (new[i]=t[perm[i]])."""
    e = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                e += PAR[t[perm[i]]] * PAR[t[perm[j]]]
    return (-1) ** (e % 2)


for s in (+1, -1):
    w = make_omega1(s)
    for k in range(2, 5):
        ok = True
        for _ in range(300):
            X, Y = random_pair(k, on_support=1.0)
            perm = tuple(rng.permutation(k))
            pX = tuple(X[p] for p in perm)
            pY = tuple(Y[p] for p in perm)
            sgn = round(np.linalg.det(np.eye(k)[list(perm)]))
            lhs = (
                koszul_perm_sign(X, perm)
                * koszul_perm_sign(Y, perm)
                * omega_k(w, pX, pY)
            )
            ok &= abs(lhs - sgn * omega_k(w, X, Y)) < TOL * (1 + abs(lhs))
        check(
            f"C2.1 S_k covariance omega_k(piX,piY)=sgn(pi)omega_k(X,Y) s={s:+d} k={k}",
            ok,
        )

    for k in range(2, 5):
        basis0 = list(itertools.product(H0, repeat=k))
        basis3 = list(itertools.product(H3, repeat=k))
        z = max(abs(omega_k(w, X, Y)) for X in basis0 for Y in basis0)
        check(f"C2.2 omega_k = 0 on H_0^k x H_0^k s={s:+d} k={k}", z == 0)
        # matrix M[X,Y] on H_0^{(x)k} x H_3^{(x)k}
        M = np.array([[omega_k(w, X, Y) for Y in basis3] for X in basis0])
        # Koszul symmetriser on H_0^k (plain) and on H_3^k (sgn-weighted, all strands odd)
        idx0 = {t: i for i, t in enumerate(basis0)}
        idx3 = {t: i for i, t in enumerate(basis3)}
        P0 = np.zeros((len(basis0),) * 2)
        Psym3 = np.zeros((len(basis3),) * 2)
        for perm in itertools.permutations(range(k)):
            for t in basis0:
                P0[idx0[tuple(t[p] for p in perm)], idx0[t]] += 1
            for t in basis3:
                Psym3[idx3[tuple(t[p] for p in perm)], idx3[t]] += koszul_perm_sign(
                    t, perm
                )
        P0 /= math.factorial(k)
        Psym3 /= math.factorial(k)
        Panti3 = np.zeros_like(Psym3)
        for perm in itertools.permutations(range(k)):
            sgn = round(np.linalg.det(np.eye(k)[list(perm)]))
            for t in basis3:
                Panti3[idx3[tuple(t[p] for p in perm)], idx3[t]] += (
                    sgn * koszul_perm_sign(t, perm)
                )
        Panti3 /= math.factorial(k)
        zero_sym = np.linalg.norm(P0.T @ M @ Psym3)
        rank_anti = np.linalg.matrix_rank(P0.T @ M @ Panti3, tol=1e-9)
        dim_sym0 = math.comb(len(H0) + k - 1, k)
        check(
            f"C2.3 Sym^k H_0 pairs only with Koszul-antisym H_3^k, non-degenerately s={s:+d} k={k}",
            zero_sym < 1e-10 and rank_anti == dim_sym0,
            f"|Sym x Sym_gr|={zero_sym:.1e}, rank(Sym x Antisym_gr)={rank_anti}, dim Sym^k H_0={dim_sym0}",
        )
        # break: the same test with the Koszul-graded Sym on H_3 would be the wrong dual
        check(
            f"C2.3-brk graded-Sym dual of Sym^k H_0 is zero (wrong-dual claim fails) s={s:+d} k={k}",
            np.linalg.matrix_rank(P0.T @ M @ Psym3, tol=1e-9) == 0 < dim_sym0,
        )

# ---------------------------------------------------------------- C3: consequences
# C3.1 kinetic term: omega_1(A, qB) = omega_1(qA, B) for even A, B (Q adjointness with
# (-1)^{|A|}=+1). Construct generic q satisfying it and evaluate the quadratic form.
for s in (+1, -1):
    w = make_omega1(s)
    g = w[np.ix_(H0, H3)]  # omega_1(A, y), A in H_0, y in H_3
    gT = w[np.ix_(H3, H0)]  # omega_1(y, A)
    # adjointness: A^T g q B = (qA)^T gT B  <=>  g q = q^T gT ; solve linear system for q
    n = len(H0)
    rows = []
    for i in range(n):
        for j in range(n):
            row = np.zeros((n, n))
            row += np.outer(g[i], np.eye(n)[j])  # (g q)_{ij} = sum_m g_im q_mj
            row -= np.outer(gT[:, j], np.eye(n)[i])  # (q^T gT)_{ij} = sum_m q_mi gT_mj
            rows.append(row.reshape(-1))
    A = np.array(rows)
    _, sv, vt = np.linalg.svd(A)
    null = vt[np.sum(sv > 1e-10) :]
    q = (null.T @ rng.normal(size=null.shape[0])).reshape(n, n)
    xs = rng.normal(size=(20, n))
    kin = max(abs(x @ g @ q @ x) for x in xs)
    if s == -1:
        check(
            "C3.1 s=-1: kinetic form omega_1(Psi,Q Psi) vanishes identically",
            kin < 1e-10,
            f"max|K|={kin:.1e}",
        )
    else:
        check(
            "C3.1 s=+1: kinetic form omega_1(Psi,Q Psi) is generically nonzero",
            kin > 1e-3,
            f"max|K|={kin:.2e}",
        )

ok = all(
    (-1) * (-1) ** (a * (1 + b)) * (-1) ** b == (-1) ** ((1 + a) * (1 + b))
    for a in (0, 1)
    for b in (0, 1)
)
s_book = (-1) ** ((1 + 0) * (1 + 1)) * (-1) ** (
    0 * 1
)  # s = book sign / (-1)^{eps eps} at (0,1)
check(
    "C3.1b book derivation line = (-1)^{(1+|A|)(1+|B|)}; on support s=+1",
    ok and s_book == 1,
)

for s in (+1, -1):
    w = make_omega1(s)
    for k in range(1, 6):
        ok = True
        for _ in range(200):
            lam = tuple(int(rng.choice(H3)) for _ in range(k))
            sig = tuple(int(rng.choice(H0)) for _ in range(k))
            a, b = omega_k(w, sig, lam), omega_k(w, lam, sig)
            ok &= abs(a - s**k * b) < TOL * (1 + abs(a))
        check(
            f"C3.2 Route C ordering omega_k(sigma,lambda)=s^k omega_k(lambda,sigma) s={s:+d} k={k}",
            ok,
        )

for k in range(1, 7):
    t = tuple([3] * k)
    rev = tuple(range(k - 1, -1, -1))
    check(
        f"C3.3 Koszul reversal of {k} odd strands = (-1)^(k(k-1)/2)",
        koszul_perm_sign(t, rev) == (-1) ** (k * (k - 1) // 2),
    )

n_fail = sum(not ok for _, ok in RESULTS)
print(f"\nseed = {SEED}: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
sys.exit(1 if n_fail else 0)
