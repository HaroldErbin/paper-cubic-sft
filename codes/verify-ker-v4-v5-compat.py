"""
Verification for derivation 034: compatibility of the ker V4 quotient with V5.

Setting (finite-dimensional algebraic layer, 011/R17 normalisations):
  H_0 = R^n, S = Sym^2 H_0 with orthonormal basis Lambda_I (R14 housekeeping),
  V4 = sum_s c_s w_s^{x4}  (totally symmetric, rank r < dim S, kernel N),
  V5 = generic totally symmetric 5-tensor (failure case) or a random element of
       {V5 in Sym^5 : V5(Xi,.,.,.) = 0 for all Xi in N} (closure case, C_full).
  F(Sigma)   = -(g^2/4!) V4(Sigma,Sigma) + (2g^2/4!) V4(Sigma,P) + (g^3/5!) V5(Sigma,Sigma,Psi)
  F_eff      = (g^2/4!) V4(P,P) + (g^3/5!) V5(P,P,Psi),   P = Psi^{x2}.

Verified (record 034, equation numbers there):
  (1) complement theory (Sigma in C, S = C + N): on-shell mismatch equals
      -(g^3/5!) [V5(P,P,Psi) - V5(pi_C P, pi_C P, Psi)] + O(g^4)        (1.4)
  (2) the O(g^3) mismatch depends on the choice of complement C
  (3) diagram route: 15 class-(c) assignments with propagator V_CC^{-1} sum to
      g^3 Pol[V5(pi_C P, pi_C P, Psi)], the polarisation computed independently  (1.7)
  (4) full-space dressed kernel K = V4 - (g/5) W: mismatch
      -(g^3/5!) v_N^T W_NN^{-1} v_N + O(g^4), and ||K^{-1}|| ~ 1/g              (2.3)
  (4c) singular W_NN (W_NN = 0 at Psi_0): a saddle exists, mismatch
      -(g^2/24) u^T (W_NC V_CC^{-1} W_CN)^{-1} u + O(g^3), u = W_NC pi_C P       (2.4)
  (5) closure case (C_full): mismatch O(g^4) and on-shell value C-independent   (1.2)
  (6) ker V4 = 0 limit reproduces R17: mismatch = (g^4/600) v V4^{-1} v + O(g^5)
  (7) remedy (a) (multiplier on N): mismatch O(g^4) in the failure case         (3.1)
  (8) polarisation collapse (1.6): the subspace {V5 in Sym^5 : V5(Xi,Psi,Psi,Psi)=0
      for all Psi, Xi in N} (C_ver) equals the (C_full) nullspace; for
      non-symmetric V5 the two differ (8b), which is the falsifier of the step
  (9) the dressed-kernel mismatch coefficient (2.3) is homogeneous of degree 5
      in Psi (not 6)
Each check is broken on purpose once (perturbed formula must FAIL); the number of
PASS/FAIL lines is printed in the summary.

Not verified: infinite-dimensional regularity of ker V4; anything at O(g^4) beyond
the leading feedback; ghost-number / reality assignment of the multiplier in (7).
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np

SEED = 20260919
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}")

n = 4  # dim H_0
D = n * (n + 1) // 2  # dim Sym^2 = 10
r = 8  # rank of V4 on Sym^2  ->  nu = D - r = 2
G1, G2 = 1e-3, 5e-4  # couplings for log-slope tests (g^4/g^3 ratios are O(10-100))
failures: list[str] = []
N_CHECKS = 0


def report(num: int | str, name: str, ok: bool, detail: str = "") -> None:
    """Print one PASS/FAIL line and record failures."""
    global N_CHECKS
    N_CHECKS += 1
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] check {num}: {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        failures.append(str(num))


def sym_tensor(shape: tuple[int, ...]) -> np.ndarray:
    """Totally symmetric random tensor."""
    T = rng.standard_normal(shape)
    S = np.zeros_like(T)
    k = len(shape)
    for perm in itertools.permutations(range(k)):
        S += np.transpose(T, perm)
    return S / math.factorial(k)


# orthonormal Sym^2 basis (Frobenius): E_aa and (E_ab+E_ba)/sqrt2
Lam = []
for a in range(n):
    E = np.zeros((n, n))
    E[a, a] = 1.0
    Lam.append(E)
for a in range(n):
    for b in range(a + 1, n):
        E = np.zeros((n, n))
        E[a, b] = E[b, a] = 1 / np.sqrt(2)
        Lam.append(E)
Lam = np.array(Lam)


def coords(M: np.ndarray) -> np.ndarray:
    """Coordinates of a symmetric matrix in the orthonormal Sym^2 basis."""
    return np.einsum("Iab,ab->I", Lam, M)


def to_S(V4: np.ndarray, V5: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Project V4, V5 onto the Sym^2 basis: V4S[I,J], V5S[I,J,e]."""
    V4S = np.einsum("abcd,Iab,Jcd->IJ", V4, Lam, Lam)
    V5S = np.einsum("abcde,Iab,Jcd->IJe", V5, Lam, Lam)
    return V4S, V5S


def degenerate_V4(rank: int) -> np.ndarray:
    """Totally symmetric 4-tensor of prescribed rank on Sym^2 (sum of c_s w_s^{x4})."""
    ws = rng.standard_normal((rank, n))
    cs = rng.standard_normal(rank)
    return sum(
        c * np.einsum("a,b,c,d->abcd", w, w, w, w) for c, w in zip(cs, ws, strict=True)
    )


def kernel_basis(V4S: np.ndarray) -> np.ndarray:
    """Orthonormal basis of ker V4S (columns)."""
    U, s, _ = np.linalg.svd(V4S)
    tol = 1e-10 * s[0]
    return U[:, s < tol]


def random_complement(Nb: np.ndarray) -> np.ndarray:
    """Columns spanning a generic complement C of N (not orthogonal to N)."""
    B = rng.standard_normal((D, D - Nb.shape[1]))
    assert np.linalg.matrix_rank(np.hstack([B, Nb])) == D
    return B


def proj_C(B: np.ndarray, Nb: np.ndarray) -> np.ndarray:
    """Projector onto C = span(B) along N = span(Nb)."""
    T = np.hstack([B, Nb])
    Tinv = np.linalg.inv(T)
    return B @ Tinv[: B.shape[1], :]


# ---------------- action pieces ----------------
def W_of(V5S: np.ndarray, psi: np.ndarray) -> np.ndarray:
    """Dressed-kernel piece W_Psi = V5(.,.,Psi) as a matrix on Sym^2."""
    return np.einsum("IJe,e->IJ", V5S, psi)


def onshell_on_subspace(V4S, V5S, psi, g, B):
    """Stationary value of F restricted to Sigma = B y (quadratic in y, exact)."""
    p = coords(np.outer(psi, psi))
    A = (g**2 / 12) * (V4S - (g / 5) * W_of(V5S, psi))  # F = -1/2 S A S + b S
    b = (g**2 / 12) * V4S @ p
    Ay = B.T @ A @ B
    by = B.T @ b
    y = np.linalg.solve(Ay, by)
    return 0.5 * by @ y


def F_eff(V4S, V5S, psi, g):
    """Target (g^2/4!) V4(P,P) + (g^3/5!) V5(P,P,Psi), shared part dropped."""
    p = coords(np.outer(psi, psi))
    return (g**2 / 24) * p @ V4S @ p + (g**3 / 120) * p @ W_of(V5S, psi) @ p


def log_slope(f, g1=G1, g2=G2):
    """Empirical power of f between two couplings."""
    return math.log(abs(f(g1)) / abs(f(g2))) / math.log(g1 / g2)


def c3_richardson(f, g=G1):
    """Leading g^3 coefficient of f = c3 g^3 + c4 g^4 + ... (two Richardson levels, error O(g^3))."""
    R = lambda h: (
        2 * f(h / 2) / (h / 2) ** 3 - f(h) / h**3
    )  # c3 + O(h^2)   # noqa: E731
    return (4 * R(g / 2) - R(g)) / 3


# ---------------- tensors ----------------
V4 = degenerate_V4(r)
V5 = sym_tensor((n,) * 5)
V4S, V5S = to_S(V4, V5)
Nb = kernel_basis(V4S)
nu = Nb.shape[1]
assert nu == D - r, f"kernel dim {nu}, expected {D - r}"
B1 = random_complement(Nb)
B2 = random_complement(Nb)
PC1, PC2 = proj_C(B1, Nb), proj_C(B2, Nb)
psi0 = rng.standard_normal(n)
p0 = coords(np.outer(psi0, psi0))
print(f"dim Sym^2 = {D}, rank V4S = {r}, dim ker = {nu}")

# Sym^5(R^n) parametrised by multisets (basis tensors with entries 0/1)
multisets = list(itertools.combinations_with_replacement(range(n), 5))
basis5 = []
for ms in multisets:
    T = np.zeros((n,) * 5)
    for perm in set(itertools.permutations(ms)):
        T[perm] = 1.0
    basis5.append(T)
Xis = [np.einsum("I,Iab->ab", Nb[:, k], Lam) for k in range(nu)]


def nullspace(M: np.ndarray) -> np.ndarray:
    """Orthonormal rows spanning the nullspace of M (right singular vectors)."""
    _, sv, Vt = np.linalg.svd(M)
    rank = int((sv > 1e-10 * sv[0]).sum())
    return Vt[rank:]


# ============ check 1: complement theory, closed-form O(g^3) mismatch (1.4) ============
def delta_C(g, B, PC, V5S_=V5S):
    """On-shell mismatch of the complement theory (Sigma in C = span B)."""
    return onshell_on_subspace(V4S, V5S_, psi0, g, B) - F_eff(V4S, V5S_, psi0, g)


def c3_pred(PC, V5S_=V5S, psi=psi0):
    """Closed-form g^3 coefficient (1.4): -(1/5!)[V5(P,P,Psi) - V5(pi_C P, pi_C P, Psi)]."""
    p = coords(np.outer(psi, psi))
    W = W_of(V5S_, psi)
    return -(1 / 120) * (p @ W @ p - (PC @ p) @ W @ (PC @ p))


res1 = lambda g: delta_C(g, B1, PC1) - c3_pred(PC1) * g**3  # noqa: E731
sl1 = log_slope(res1)
c3_num = c3_richardson(lambda g: delta_C(g, B1, PC1))
ok1 = (
    abs(sl1 - 4) < 0.1
    and abs(c3_pred(PC1)) > 1e-3
    and abs(c3_num - c3_pred(PC1)) < 1e-4 * abs(c3_pred(PC1))
)
report(
    1,
    "complement theory: mismatch = -(g^3/5!)[V5(P,P,Psi)-V5(pi_C P,pi_C P,Psi)] + O(g^4)",
    ok1,
    f"c3 pred={c3_pred(PC1):.6e}, Richardson={c3_num:.6e}, residual log-slope={sl1:.3f}",
)
# break: wrong projection (use P instead of pi_C P)  ->  residual O(g^3)
res1b = lambda g: delta_C(g, B1, PC1) - 0.0 * g**3  # noqa: E731
sl1b = log_slope(res1b)
report(
    "1b",
    "break-on-purpose: without the pi_C term the residual is O(g^3), not O(g^4)",
    abs(sl1b - 3) < 0.1,
    f"log-slope={sl1b:.3f}",
)

# ============ check 2: C-dependence of the O(g^3) mismatch ============
c31, c32 = c3_pred(PC1), c3_pred(PC2)
report(
    2,
    "O(g^3) mismatch depends on the complement C",
    abs(c31 - c32) > 1e-3,
    f"c3(C1)={c31:.4e}, c3(C2)={c32:.4e}",
)

# ============ check 3: diagram route (1.7) vs independent polarisation ============
g = 0.3
psis = [rng.standard_normal(n) for _ in range(5)]
Bd, PCd = B1, PC1
VCC = Bd.T @ V4S @ Bd


def q_pair(i, j):
    """Symmetrised pair psi_i psi_j in Sym^2 coordinates."""
    return coords(0.5 * (np.outer(psis[i], psis[j]) + np.outer(psis[j], psis[i])))


def chain(q):
    """Source (g^2/6) V4(.,q)|_C  ->  propagator (12/g^2) V_CC^{-1}  ->  vector in C."""
    src = (g**2 / 6) * (Bd.T @ V4S @ q)
    return Bd @ np.linalg.solve(VCC, (12 / g**2) * src)


def assignment(i, jk, lm, wick=2):
    """Class-(c) diagram for one assignment {i; {jk},{lm}} (011 eq. B.7 with V_CC^{-1})."""
    l1, l2 = chain(q_pair(*jk)), chain(q_pair(*lm))
    return wick * (g**3 / 120) * np.einsum("IJe,I,J,e->", V5S, l1, l2, psis[i])


def all_assignments(wick=2):
    """Sum over the 15 unordered assignments."""
    tot, cnt = 0.0, 0
    for i in range(5):
        others = [k for k in range(5) if k != i]
        for jk in itertools.combinations(others, 2):
            lm = tuple(k for k in others if k not in jk)
            if jk < lm:
                tot += assignment(i, jk, lm, wick)
                cnt += 1
    return tot, cnt


def f_C(psi, PC=PCd, V5S_=V5S):
    """Quintic V5(pi_C Psi^2, pi_C Psi^2, Psi) whose polarisation is the diagram sum."""
    p = PC @ coords(np.outer(psi, psi))
    return np.einsum("IJe,I,J,e->", V5S_, p, p, psi)


def polarise5(f):
    """(1/5!) sum_{S subset {1..5}} (-1)^{5-|S|} f(sum_{i in S} psi_i)  (exact for quintics)."""
    tot = 0.0
    for k in range(6):
        for S in itertools.combinations(range(5), k):
            v = sum((psis[i] for i in S), np.zeros(n))
            tot += (-1) ** (5 - k) * f(v)
    return tot / 120


diag_sum, cnt = all_assignments()
pol = g**3 * polarise5(f_C)
target = g**3 * np.einsum("abcde,a,b,c,d,e->", V5, *psis)
ok3 = (
    cnt == 15
    and abs(diag_sum - pol) < 1e-12 * max(1, abs(pol))
    and abs(diag_sum - target) > 1e-6
)
report(
    3,
    "diagram route: 15 class-(c) assignments = g^3 Pol[V5(pi_C P,pi_C P,Psi)] != g^3 V5(psi_1..psi_5)",
    ok3,
    f"count={cnt}, |sum-pol|={abs(diag_sum - pol):.1e}, |sum-target|={abs(diag_sum - target):.2e}",
)
d1, _ = all_assignments(wick=1)
report("3b", "break-on-purpose: Wick factor 1 instead of 2 fails", abs(d1 - pol) > 1e-6)


# ============ check 4: full-space dressed kernel (2.3) ============
def delta_full(g, V5S_=V5S):
    """On-shell mismatch on the full Sym^2 with the dressed kernel K_Psi (no quotient)."""
    return onshell_on_subspace(V4S, V5S_, psi0, g, np.eye(D)) - F_eff(
        V4S, V5S_, psi0, g
    )


W0 = W_of(V5S, psi0)
v0 = W0 @ p0
vN = Nb.T @ v0
WNN = Nb.T @ W0 @ Nb
c3_full = -(1 / 120) * vN @ np.linalg.solve(WNN, vN)
res4 = lambda g: delta_full(g) - c3_full * g**3  # noqa: E731
sl4 = log_slope(res4)
# propagator scaling: smallest singular value of K ~ g
smin = lambda g: np.linalg.svd(V4S - (g / 5) * W0, compute_uv=False)[-1]  # noqa: E731
sl_prop = log_slope(smin)
ok4 = abs(sl4 - 4) < 0.1 and abs(c3_full) > 1e-4 and abs(sl_prop - 1) < 0.05
report(
    4,
    "full Sym^2 with dressed kernel: mismatch = -(g^3/5!) v_N^T W_NN^{-1} v_N + O(g^4); ||K^{-1}|| ~ 1/g",
    ok4,
    f"c3={c3_full:.4e}, residual log-slope={sl4:.3f}, smin(K) log-slope={sl_prop:.3f}",
)
res4b = lambda g: delta_full(g) + c3_full * g**3  # noqa: E731
report(
    "4b",
    "break-on-purpose: sign-flipped closed form leaves O(g^3)",
    abs(log_slope(res4b) - 3) < 0.1,
)

# ---- 4c: singular W_NN.  V5 in the subspace V5(Xi_k, Xi_l, psi0) = 0 (nu(nu+1)/2 constraints on Sym^5)
Mnn = np.array(
    [
        [np.einsum("ab,cd,e,abcde->", Xis[k], Xis[m], psi0, T) for T in basis5]
        for k in range(nu)
        for m in range(k, nu)
    ]
)
null_nn = nullspace(Mnn)
V5nn = sum(
    c * T
    for c, T in zip(
        null_nn.T @ rng.standard_normal(null_nn.shape[0]), basis5, strict=True
    )
)
_, V5nnS = to_S(V4, V5nn)
Wnn0 = W_of(V5nnS, psi0)
assert np.linalg.norm(Nb.T @ Wnn0 @ Nb) < 1e-12 * np.linalg.norm(Wnn0), "W_NN not zero"


def c2_singular(B: np.ndarray, PC: np.ndarray) -> float:
    """Return the closed form (2.4): -(1/24) u^T (W_NC V_CC^{-1} W_CN)^{-1} u, u = W_NC pi_C P, blocks in the (B, Nb) bases."""
    VCC_ = B.T @ V4S @ B
    WCN_ = B.T @ Wnn0 @ Nb
    WNC_ = Nb.T @ Wnn0 @ B
    u = Nb.T @ Wnn0 @ (PC @ p0)
    return -(1 / 24) * u @ np.linalg.solve(WNC_ @ np.linalg.solve(VCC_, WCN_), u)


c2a, c2b = c2_singular(B1, PC1), c2_singular(B2, PC2)
res4c = lambda g: delta_full(g, V5nnS) - c2a * g**2  # noqa: E731
sl4c = log_slope(res4c)
xi_slope = log_slope(
    lambda g: np.linalg.norm(Nb.T @ np.linalg.solve(V4S - (g / 5) * Wnn0, V4S @ p0))
)  # kernel component of the saddle ~ 1/g
ok4c = (
    abs(sl4c - 3) < 0.1
    and abs(c2a) > 1e-4
    and abs(c2a - c2b) < 1e-10 * abs(c2a)
    and abs(xi_slope + 1) < 0.05
)
report(
    "4c",
    "singular W_NN (=0 at Psi_0): saddle exists with xi ~ 1/g; mismatch = (2.4) g^2 + O(g^3), C-independent",
    ok4c,
    f"c2={c2a:.4e} (C2: {c2b:.4e}), residual log-slope={sl4c:.3f}, |xi| log-slope={xi_slope:.3f}",
)
res4d = lambda g: delta_full(g, V5nnS) + c2a * g**2  # noqa: E731
report(
    "4d",
    "break-on-purpose: sign-flipped (2.4) leaves O(g^2)",
    abs(log_slope(res4d) - 2) < 0.1,
)


# ============ check 5: closure case, V5 satisfying (C_full) ============
# constraints Xi^{ab} V5_{abcde} = 0 for Xi in N (C_full), on the Sym^5 basis
def cfull_rows(basis: list[np.ndarray]) -> np.ndarray:
    """Constraint matrix of (C_full): rows (Xi, cde), columns = basis tensors."""
    M = np.array(
        [[np.einsum("ab,abcde->cde", Xi, T).ravel() for T in basis] for Xi in Xis]
    )
    return np.transpose(M, (0, 2, 1)).reshape(-1, len(basis))


Mcons = cfull_rows(basis5)
null = nullspace(Mcons)
print(
    f"closure family: dim Sym^5 = {len(basis5)}, constraint rank = {len(basis5) - null.shape[0]}, "
    f"nullspace dim = {null.shape[0]}"
)
coef = null.T @ rng.standard_normal(null.shape[0])
V5c = sum(c * T for c, T in zip(coef, basis5, strict=True))
_, V5cS = to_S(V4, V5c)
PiN = Nb @ Nb.T
cfull = max(np.linalg.norm(PiN @ V5cS[:, :, a]) for a in range(n))
sl5a = log_slope(lambda g: delta_C(g, B1, PC1, V5cS))
val1 = onshell_on_subspace(V4S, V5cS, psi0, 0.3, B1)
val2 = onshell_on_subspace(V4S, V5cS, psi0, 0.3, B2)
ok5 = (
    cfull < 1e-10
    and abs(sl5a - 4) < 0.1
    and abs(val1 - val2) < 1e-12 * abs(val1)
    and abs(c3_pred(PC1, V5cS)) < 1e-12
)
report(
    5,
    "closure (C_full): Pi_N V5S[:,:,a]=0; mismatch O(g^4); on-shell value C-independent at finite g",
    ok5,
    f"|Pi_N W|={cfull:.1e}, log-slope={sl5a:.3f}, |val(C1)-val(C2)|={abs(val1 - val2):.1e}",
)
V5mix = V5cS + 1e-2 * V5S
c3mix_num = c3_richardson(lambda g: delta_C(g, B1, PC1, V5mix))
c3mix = c3_pred(PC1, V5mix)
report(
    "5b",
    "break-on-purpose: adding 1e-2 x generic V5 restores an O(g^3) mismatch (= closed form (1.4))",
    abs(c3mix) > 1e-6 and abs(c3mix_num - c3mix) < 1e-3 * abs(c3mix),
    f"c3 pred={c3mix:.6e}, Richardson={c3mix_num:.6e}",
)

# ============ check 6: ker V4 = 0 limit reproduces R17 ============
V4g = sym_tensor((n,) * 4)
V4gS, _ = to_S(V4g, V5)
assert np.linalg.matrix_rank(V4gS) == D
vg = W0 @ p0
fb = (1 / 600) * vg @ np.linalg.solve(V4gS, vg)
res6 = lambda g: (
    onshell_on_subspace(V4gS, V5S, psi0, g, np.eye(D))
    - F_eff(V4gS, V5S, psi0, g)
    - fb * g**4
)  # noqa: E731
sl6 = log_slope(res6)
report(
    6,
    "ker V4 = 0 limit: mismatch = (g^4/600) v V4^{-1} v + O(g^5)  (R17 feedback)",
    abs(sl6 - 5) < 0.1,
    f"log-slope={sl6:.3f}",
)
res6b = lambda g: (
    onshell_on_subspace(V4gS, V5S, psi0, g, np.eye(D))
    - F_eff(V4gS, V5S, psi0, g)
    - (600 / 500) * fb * g**4
)  # noqa: E731
report(
    "6b",
    "break-on-purpose: 1/500 instead of 1/600 leaves O(g^4)",
    abs(log_slope(res6b) - 4) < 0.1,
)


# ============ check 7: remedy (a): multiplier fixes xi = pi_N P ============
def onshell_remedy_a(V4S_, V5S_, psi, g, B, PC, xi_scale=1.0):
    """
    Sigma = B y + xi, xi = xi_scale (1 - PC) P imposed by a multiplier; stationary in y (exact).

    xi_scale = 1 is remedy (a); any other value is a wrong multiplier constraint (break leg 7b).
    """
    p = coords(np.outer(psi, psi))
    xi = xi_scale * (np.eye(D) - PC) @ p
    A = (g**2 / 12) * (V4S_ - (g / 5) * W_of(V5S_, psi))
    b = (g**2 / 12) * V4S_ @ p
    # F(By + xi) = -1/2 (By+xi)^T A (By+xi) + b^T (By+xi)
    Ay = B.T @ A @ B
    by = B.T @ (b - A @ xi)
    y = np.linalg.solve(Ay, by)
    Sig = B @ y + xi
    return -0.5 * Sig @ A @ Sig + b @ Sig


d7 = lambda g, B=B1, PC=PC1: (
    onshell_remedy_a(V4S, V5S, psi0, g, B, PC) - F_eff(V4S, V5S, psi0, g)
)  # noqa: E731
sl7 = log_slope(d7)
c4a = d7(1e-2, B1, PC1) / 1e-8
c4b = d7(1e-2, B2, PC2) / 1e-8
report(
    7,
    "remedy (a): complement + multiplier for N closes at O(g^3) (mismatch O(g^4)) in the failure case",
    abs(sl7 - 4) < 0.1,
    f"log-slope={sl7:.3f}; O(g^4) coefficient C1: {c4a:.4e}, C2: {c4b:.4e}",
)
d7b = lambda g: (
    onshell_remedy_a(V4S, V5S, psi0, g, B1, PC1, xi_scale=0.5)
    - F_eff(V4S, V5S, psi0, g)
)  # noqa: E731
report(
    "7b",
    "break-on-purpose: multiplier imposing xi = 0.5 pi_N P instead of pi_N P leaves O(g^3)",
    abs(log_slope(d7b) - 3) < 0.1,
    f"log-slope={log_slope(d7b):.3f}",
)


# ============ check 8: polarisation collapse (1.6): (C_ver) subspace = (C_full) nullspace ============
def cver_rows(basis: list[np.ndarray], n_samples: int = 40) -> np.ndarray:
    """Constraint matrix of (C_ver): V5(Xi, Psi, Psi, Psi) = 0 at sampled Psi (no symmetry used)."""
    psis_s = rng.standard_normal((n_samples, n))
    return np.array(
        [
            [np.einsum("ab,c,d,e,abcde->", Xi, ps, ps, ps, T) for T in basis]
            for Xi in Xis
            for ps in psis_s
        ]
    )


def same_subspace(A: np.ndarray, B: np.ndarray) -> float:
    """Frobenius distance of the orthogonal projectors on the row spaces (0 iff equal)."""
    return np.linalg.norm(A.T @ A - B.T @ B)


null_ver = nullspace(cver_rows(basis5))
dist8 = same_subspace(null_ver, null)
report(
    8,
    "(C_ver) subspace of Sym^5 (sampled cubic in Psi) = (C_full) nullspace, dimension 20",
    null_ver.shape[0] == null.shape[0] == 20 and dist8 < 1e-10,
    f"dim ver={null_ver.shape[0]}, dim full={null.shape[0]}, projector distance={dist8:.1e}",
)
# falsifier: without total symmetry the implication (C_ver) => (C_full) fails
basis_all = []
for idx in itertools.product(range(n), repeat=5):
    T = np.zeros((n,) * 5)
    T[idx] = 1.0
    basis_all.append(T)
dim_full_ns = nullspace(cfull_rows(basis_all)).shape[0]
dim_ver_ns = nullspace(cver_rows(basis_all, n_samples=60)).shape[0]
report(
    "8b",
    "break-on-purpose: for non-symmetric V5 the (C_ver) space is strictly larger than (C_full)",
    dim_ver_ns > dim_full_ns,
    f"dim ver={dim_ver_ns}, dim full={dim_full_ns} (of {n**5})",
)


# ============ check 9: (2.3) is homogeneous of degree 5 in Psi ============
def c3_full_of(psi: np.ndarray) -> float:
    """Coefficient -(1/5!) v_N^T W_NN^{-1} v_N of (2.3) at Psi = psi."""
    W = W_of(V5S, psi)
    v = Nb.T @ (W @ coords(np.outer(psi, psi)))
    return -(1 / 120) * v @ np.linalg.solve(Nb.T @ W @ Nb, v)


lams = [1.7, -0.6, 2.3]
hom5 = max(abs(c3_full_of(lam * psi0) - lam**5 * c3_full_of(psi0)) for lam in lams)
hom6 = max(abs(c3_full_of(lam * psi0) - lam**6 * c3_full_of(psi0)) for lam in lams)
report(
    9,
    "dressed-kernel mismatch coefficient (2.3) scales as lambda^5 under Psi -> lambda Psi",
    hom5 < 1e-12 * abs(c3_full_of(psi0)),
    f"max |c3(l psi) - l^5 c3(psi)| = {hom5:.1e}",
)
report(
    "9b",
    "break-on-purpose: lambda^6 scaling fails",
    hom6 > 1e-3 * abs(c3_full_of(psi0)),
    f"max |c3(l psi) - l^6 c3(psi)| = {hom6:.1e}",
)

print(
    f"SUMMARY: {N_CHECKS - len(failures)}/{N_CHECKS} PASS;",
    "ALL PASS" if not failures else f"FAILURES in checks {failures}",
)
sys.exit(1 if failures else 0)
