#!/usr/bin/env python3
"""
verify-ph23-doublet.py -- PH23: the Sym^2 source doublet (Sigma, chi) is timelike.

Record: agent/derivations/038-chi-scheme-ogs5-count.md, Addendum 2026-09-26 (nodes N10.x).

Model (finite-dimensional random-tensor layer, as in verify-chi-partner.py):
Psi in R^N, Sym^2 fields as coordinates x in R^m (m = N(N+1)/2) on the basis
E_(ii) = e_i e_i^T, E_(ij) = e_i e_j^T + e_j e_i^T (i<j). Random symmetric tensors
T4 (= V_4), T5 (= V_5). K_AB = V_4(E_A, E_B), W_AB = V_5(E_A, E_B, Psi),
p = coordinates of P = Psi (x) Psi, u = K p, v = W p = V_5(., P, Psi).

Doublet action through O(g^3) (A.1 of the addendum, plus the V_5 couplings):

    S_aux = g^2/4! [ Q_ab V4(phi^a, phi^b) + 2 lambda_a V4(phi^a, P) ]
          + g^3/5! B_ab V5(phi^a, phi^b, Psi),

target  S_t = g^2/4! V4(Psi^4) + g^3/5! V5(Psi^5)  (the Psi-only V2, V3 terms cancel,
and the sextic contact is omitted on both sides, so the O(g^4) mismatch is the pure
feedback composite of R17/R24).

S_aux is quadratic in phi, so its saddle is an exact linear solve at every g. The Taylor
coefficients c2, c3, c4 of [S_aux(saddle) - S_t] are extracted by a Chebyshev fit of the
exact solve over g in [-0.1, 0.1] -- a path that does not use the closed forms
    c2 = -(<l,l> + 1) V4(Psi^4)/4!,
    c3 = (phihat^T B phihat - 1) V5(Psi^5)/5!,    phihat = -Q^{-1} lambda,
    c4 = -<mu,mu> v^T K^{-1} v / 600,             mu = B phihat,
with <a,b> = a^T Q^{-1} b (dual pairing on doublet covectors).

What is verified: (A.2)-(A.3) [on-shell value, matching condition, sign], the normal
form (GL(2) transitivity on consistent O(g^2) data, the aligning boost), the dual-norm
form of the timelike criterion (correction N10.7), the O(g^3) failure of alignment
(Psi-degree independence of u, v; nullity of mu at R24's (a,b)=(1,2); no joint boost),
and the frame covariance of the O(g^2)-O(g^4) conditions (N10.5, through O(g^4) only).
What is not verified: anything at the CFT level (A4 of 038); the O(g^5) conditions of
038/048 are cited, not re-run; the exclusion of other O(g^2) terms (A3, A8) is a
structural argument, not a machine check.

Break legs (BREAK-...) are checks that MUST fail; they are counted separately and the
script exits nonzero if one of them passes.
"""

from __future__ import annotations

import sys
from itertools import permutations

import numpy as np

SEED = 20260926
N = 3
TOL = 1e-8

results: list[tuple[str, bool, str]] = []
breaks: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, info: str = "") -> bool:
    """Record a named PASS/FAIL check."""
    results.append((name, bool(ok), info))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")
    return bool(ok)


def break_leg(name: str, check_passed: bool, info: str = "") -> None:
    """Record a break leg: the underlying check must FAIL on the perturbed input."""
    fired = not check_passed
    breaks.append((name, fired, info))
    print(f"{'FIRES' if fired else 'SILENT'}  {name}  {info}")


def sym_tensor(rng: np.random.Generator, k: int) -> np.ndarray:
    """Fully symmetrised Gaussian tensor of rank k on R^N."""
    t = rng.standard_normal((N,) * k)
    s = np.zeros_like(t)
    perms = list(permutations(range(k)))
    for p in perms:
        s += np.transpose(t, p)
    return s / len(perms)


def sym2_basis() -> list[np.ndarray]:
    """Basis E_(ij), i<=j, of symmetric N x N matrices."""
    basis = []
    for i in range(N):
        for j in range(i, N):
            e = np.zeros((N, N))
            e[i, j] += 1.0
            if i != j:
                e[j, i] += 1.0
            basis.append(e)
    return basis


class Model:
    """Random V_4, V_5 and a generic off-shell Psi, in Sym^2 coordinates."""

    def __init__(self, seed: int) -> None:
        """Draw the random tensors and Psi from the given seed."""
        rng = np.random.default_rng(seed)
        self.T4 = sym_tensor(rng, 4)
        self.T5 = sym_tensor(rng, 5)
        self.psi = rng.standard_normal(N)
        self.E = sym2_basis()
        self.m = len(self.E)
        self.K = np.array(
            [[np.einsum("ijkl,ij,kl", self.T4, a, b) for b in self.E] for a in self.E]
        )
        self.set_psi(self.psi)

    def set_psi(self, psi: np.ndarray) -> None:
        """Recompute the Psi-dependent objects."""
        self.psi = psi
        self.W = np.array(
            [
                [np.einsum("ijklm,ij,kl,m", self.T5, a, b, psi) for b in self.E]
                for a in self.E
            ]
        )
        # coordinates of P = Psi Psi^T on the basis: p_(ii)=psi_i^2, p_(ij)=psi_i psi_j
        self.p = np.array([psi[i] * psi[j] for i in range(N) for j in range(i, N)])
        self.u = self.K @ self.p
        self.v = self.W @ self.p
        # independent einsum values of the target vertices
        self.V4psi = np.einsum("ijkl,i,j,k,l", self.T4, psi, psi, psi, psi)
        self.V5psi = np.einsum("ijklm,i,j,k,l,m", self.T5, psi, psi, psi, psi, psi)
        self.vKv = self.v @ np.linalg.solve(self.K, self.v)

    def onshell(self, g: float, Q: np.ndarray, lam: np.ndarray, B: np.ndarray) -> float:
        """Exact on-shell value of S_aux by a linear solve (no closed form used)."""
        H = g**2 / 24 * np.kron(Q, self.K) + g**3 / 120 * np.kron(B, self.W)
        J = g**2 / 12 * np.kron(lam, self.u)
        X = -0.5 * np.linalg.solve(H, J)
        return float(X @ H @ X + J @ X)

    def saddle(
        self, g: float, Q: np.ndarray, lam: np.ndarray, B: np.ndarray
    ) -> np.ndarray:
        """Saddle coordinates X = (x^1, x^2) of S_aux."""
        H = g**2 / 24 * np.kron(Q, self.K) + g**3 / 120 * np.kron(B, self.W)
        J = g**2 / 12 * np.kron(lam, self.u)
        return -0.5 * np.linalg.solve(H, J)

    def coeffs(self, Q: np.ndarray, lam: np.ndarray, B: np.ndarray) -> np.ndarray:
        """Taylor coefficients (c2, c3, c4) of S_aux(saddle) - S_t by Chebyshev fit."""
        gs = 0.1 * np.cos(np.pi * (np.arange(41) + 0.5) / 41)
        f = []
        for g in gs:
            s_aux = self.onshell(g, Q, lam, B)
            s_t = g**2 / 24 * self.V4psi + g**3 / 120 * self.V5psi
            f.append((s_aux - s_t) / g**2)
        cheb = np.polynomial.chebyshev.Chebyshev.fit(gs, f, 14, domain=[-0.1, 0.1])
        # convert to the monomial basis in g itself (identity domain/window map)
        poly = cheb.convert(kind=np.polynomial.Polynomial)
        c = poly.coef
        return np.array([c[0], c[1], c[2]])


def dual(Q: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    """Dual pairing <a,b> = a^T Q^{-1} b on doublet covectors."""
    return float(a @ np.linalg.solve(Q, b))


def boost(eta: float) -> np.ndarray:
    """O(1,1) boost preserving diag(-1, +1)."""
    return np.array([[np.cosh(eta), np.sinh(eta)], [np.sinh(eta), np.cosh(eta)]])


Q0 = np.diag([-1.0, 1.0])
LAM0 = np.array([1.0, 0.0])


def normal_form(Q: np.ndarray, lam: np.ndarray) -> np.ndarray | None:
    """
    Construct G in GL(2) with G^T Q G = diag(-1,1) and G^T lam = (1,0).

    Route: eigen-decomposition of Q (Sylvester), then the O(1,1) boost of rapidity
    -artanh(l_chi/l_Sigma), then the sign. Returns None if no real boost exists
    (|l_chi| >= |l_Sigma| after Sylvester: null or spacelike doublet).

    Args:
        Q: symmetric nondegenerate split-signature 2x2 matrix.
        lam: source covector.

    Returns:
        np.ndarray | None: the redefinition matrix G, or None.

    """
    w, R = np.linalg.eigh(Q)
    if not (w[0] < 0 < w[1]):
        return None
    G1 = R @ np.diag(1 / np.sqrt(np.abs(w)))  # G1^T Q G1 = diag(-1, 1)
    l1 = G1.T @ lam
    ratio = l1[1] / l1[0] if l1[0] != 0 else np.inf
    if not abs(ratio) < 1:
        return None
    eta1 = np.arctanh(ratio)
    eps = np.sign(l1[0])
    return G1 @ boost(-eta1) * eps


def random_split_Q(rng: np.random.Generator) -> np.ndarray:
    """Random symmetric 2x2 of split signature, non-diagonal."""
    while True:
        A = rng.standard_normal((2, 2))
        Q = A @ np.diag([-1.0, rng.uniform(0.3, 3.0)]) @ A.T
        if abs(np.linalg.det(Q)) > 0.1:
            return Q


def main() -> int:
    """Run all checks and break legs; return the exit code."""
    print(f"verify-ph23-doublet.py  seed={SEED}  N={N}")
    rng = np.random.default_rng(SEED)
    models = [Model(SEED + k) for k in range(3)]

    # ---------------- N10.1: on-shell value (A.2) --------------------------------
    for k, M in enumerate(models):
        Q = random_split_Q(rng)
        lam = rng.standard_normal(2)
        g = 0.37
        B0 = np.zeros((2, 2))
        exact = M.onshell(g, Q, lam, B0)
        closed = -(g**2) / 24 * dual(Q, lam, lam) * M.V4psi
        check(
            f"N10.1[{k}]",
            abs(exact - closed) < TOL * max(1, abs(closed)),
            f"exact={exact:.12g} closed={closed:.12g}",
        )
        wrong = -(g**2) / 24 * float(lam @ Q @ lam) * M.V4psi  # Q instead of Q^{-1}
        break_leg(
            f"BREAK-N10.1-Q-not-Qinv[{k}]",
            abs(exact - wrong) < TOL * max(1, abs(wrong)),
            f"wrong={wrong:.6g}",
        )
        # p^T K p = V4(Psi^4): Veronese identity in coordinates (independent einsum)
        check(
            f"N10.1-veronese[{k}]",
            abs(M.p @ M.K @ M.p - M.V4psi) < 1e-10,
            f"pKp={M.p @ M.K @ M.p:.10g} V4={M.V4psi:.10g}",
        )

    # ---------------- N10.2 / N10.3: matching condition and sign -----------------
    M = models[0]
    cases = {
        "timelike-unit": (np.array([np.cosh(0.8), np.sinh(0.8)]), True),
        "null": (np.array([1.0, 1.0]), False),
        "spacelike-unit": (np.array([np.sinh(0.8), np.cosh(0.8)]), False),
        "timelike-nonunit": (np.array([2.0, 0.5]), False),
    }
    for name, (lam, should_match) in cases.items():
        c = M.coeffs(Q0, lam, np.zeros((2, 2)))
        matches = abs(c[0]) < 1e-7 * abs(M.V4psi)
        pred = -(dual(Q0, lam, lam) + 1) * M.V4psi / 24
        check(
            f"N10.2-c2-closed-form[{name}]",
            abs(c[0] - pred) < 1e-7 * abs(M.V4psi),
            f"fit c2={c[0]:.10g} closed={pred:.10g}",
        )
        tag = "N10.2-timelike-matches" if should_match else f"N10.3-{name}-fails"
        check(
            tag,
            matches == should_match,
            f"<l,l>={dual(Q0, lam, lam):+.4f} c2={c[0]:.3e}",
        )

    # ---------------- N10.4: normal form, aligning boost, residual chi source ----
    for k in range(5):
        Q = random_split_Q(rng)
        # a random consistent source on the unit hyperboloid <l,l> = -1 of Q^{-1}
        eta = rng.uniform(-2, 2)
        w, R = np.linalg.eigh(Q)
        G1 = R @ np.diag(1 / np.sqrt(np.abs(w)))
        lam = np.linalg.solve(G1.T, np.array([np.cosh(eta), np.sinh(eta)]))
        G = normal_form(Q, lam)
        ok = G is not None
        if ok:
            ok = np.allclose(G.T @ Q @ G, Q0, atol=1e-10) and np.allclose(
                G.T @ lam, LAM0, atol=1e-10
            )
        check(
            f"N10.4-normal-form[{k}]",
            ok,
            f"<l,l>={dual(Q, lam, lam):+.12f} lam_chi(before)={lam[1]:+.3f}",
        )
        # residual chi source and chi saddle at O(g^2) in the aligned frame
        g = 0.05
        X = M.saddle(g, G.T @ Q @ G, G.T @ lam, np.zeros((2, 2)))
        chi = X[M.m :]
        sig = X[: M.m]
        # NOTE (2026-10-01, critic node check): implied by normal_form (block-diagonal H, J_chi=0); weak, not load-bearing evidence.
        check(
            f"N10.4-chi-saddle-zero[{k}]",
            np.max(np.abs(chi)) < 1e-10 and np.allclose(sig, M.p, atol=1e-10),
            f"max|chi*|={np.max(np.abs(chi)):.2e}",
        )
        # invariance of the on-shell value under the redefinition
        e1 = M.onshell(g, Q, lam, np.zeros((2, 2)))
        e2 = M.onshell(g, G.T @ Q @ G, G.T @ lam, np.zeros((2, 2)))
        # NOTE (2026-10-01, critic node check): identity -- the on-shell action is invariant under any invertible G; weak, not load-bearing evidence.
        check(
            f"N10.4-invariance[{k}]",
            abs(e1 - e2) < 1e-12 * max(1, abs(e1)),
            f"{e1:.12g} vs {e2:.12g}",
        )

    # stabiliser of (Q0, LAM0) in O(1,1): only diag(1, +-1)
    etas = np.linspace(-3, 3, 601)
    moved = [abs((boost(e).T @ LAM0)[1]) for e in etas if abs(e) > 1e-9]
    check(
        "N10.4-stabiliser-discrete",
        min(moved) > 0.0099,
        f"min_{{eta!=0}} |(Lambda^T lam0)_chi| = {min(moved):.4f} (grid step 0.01)",
    )

    # spacelike doublet: no aligning boost
    lam_sp = np.array([1.0, 2.0])
    Gsp = normal_form(Q0, lam_sp)
    best = min(abs((boost(e).T @ lam_sp)[1]) for e in np.linspace(-10, 10, 200001))
    check(
        "N10.4-spacelike-no-boost",
        Gsp is None and best >= np.sqrt(dual(Q0, lam_sp, lam_sp)) - 1e-6,
        f"min_eta |lam'_chi| = {best:.6f} >= sqrt(<l,l>) = "
        f"{np.sqrt(dual(Q0, lam_sp, lam_sp)):.6f}",
    )
    # break leg: the alignment check applied to the spacelike doublet must fail
    aligned_sp = Gsp is not None and np.allclose(Gsp.T @ lam_sp, LAM0)
    # NOTE (2026-10-01, critic node check): restates normal_form's own guard abs(ratio) < 1; perturbs no passing check (does not count among the genuine break legs).
    break_leg("BREAK-N10.4-spacelike-aligned", aligned_sp, "normal_form returns None")
    lam_null = np.array([1.0, 1.0])
    # NOTE (2026-10-01, critic node check): restates normal_form's own guard abs(ratio) < 1; perturbs no passing check (does not count among the genuine break legs).
    break_leg(
        "BREAK-N10.4-null-aligned",
        normal_form(Q0, lam_null) is not None,
        "rapidity diverges",
    )

    # ---------------- N10.7: dual-norm criterion (correction to 038 part 1) --------
    a_chi = 4.0
    Qa = np.diag([-1.0, a_chi])
    lam_a = np.array([1.0, 1.0])
    dual_timelike = lam_a[1] ** 2 < a_chi * lam_a[0] ** 2  # corrected criterion
    printed_038 = a_chi * lam_a[1] ** 2 < lam_a[0] ** 2  # 038 §2.4 part 1 as printed
    D = np.diag([1.0, 1 / np.sqrt(a_chi)])
    # the Q-preserving boost D L(eta) D^{-1} aligns lam_a (up to the norm) directly
    eta_a = np.arctanh((lam_a[1] / np.sqrt(a_chi)) / lam_a[0])
    Gq = D @ boost(-eta_a) @ np.linalg.inv(D)
    check(
        "N10.7-dual-norm-criterion",
        dual_timelike
        and np.allclose(Gq.T @ Qa @ Gq, Qa)
        and abs((Gq.T @ lam_a)[1]) < 1e-12,
        f"<l,l>={dual(Qa, lam_a, lam_a):+.3f}; Q-preserving boost kills lam_chi: "
        f"{(Gq.T @ lam_a)[1]:.1e}",
    )
    check(
        "N10.7-printed-038-inequality-wrong",
        dual_timelike and not printed_038,
        "a=4, lam=(1,1): alignable, yet a*l_chi^2 < l_S^2 is violated",
    )

    # ---------------- N10.6: O(g^3) -- degree independence and nullity of mu ------
    for k, Mk in enumerate(models):
        s = np.linalg.svd(np.column_stack([Mk.u, Mk.v]), compute_uv=False)
        check(
            f"N10.6-u-v-independent[{k}]",
            s[1] / s[0] > 1e-3,
            f"sigma2/sigma1={s[1] / s[0]:.3e}",
        )
        # Psi-degree: u(t Psi) = t^2 u, v(t Psi) = t^3 v
        psi0 = Mk.psi.copy()
        u0, v0 = Mk.u.copy(), Mk.v.copy()
        t = 1.7
        Mk.set_psi(t * psi0)
        deg_ok = np.allclose(Mk.u, t**2 * u0) and np.allclose(Mk.v, t**3 * v0)
        Mk.set_psi(psi0)
        # NOTE (2026-10-01, critic node check): true by construction of set_psi; weak, not load-bearing evidence.
        check(f"N10.6-degrees[{k}]", deg_ok, "u ~ Psi^2, v ~ Psi^3")
    # break leg of the independence check: v replaced by a multiple of u
    s = np.linalg.svd(np.column_stack([M.u, 2.3 * M.u]), compute_uv=False)
    break_leg("BREAK-N10.6-u-v-parallel", s[1] / s[0] > 1e-3, "rank 1 input")

    # O(g^3) source covector in the aligned frame, by numerical differentiation
    b_chi = 2.0
    B = np.array([[1.0, b_chi / 2], [b_chi / 2, 0.7]])
    g = 0.2
    X0 = np.concatenate([M.p, np.zeros(M.m)])  # aligned leading saddle (P, 0)

    def S3(X: np.ndarray) -> float:
        return float(g**3 / 120 * X @ np.kron(B, M.W) @ X)

    h = 1e-6
    grad = np.array(
        [(S3(X0 + h * e) - S3(X0 - h * e)) / (2 * h) for e in np.eye(2 * M.m)]
    )
    J3_chi = grad[M.m :]
    pred = g**3 * b_chi / 120 * M.v
    check(
        "N10.6-chi-source-O(g3)",
        np.allclose(J3_chi, pred, rtol=1e-6, atol=1e-12),
        f"|J3_chi|={np.linalg.norm(J3_chi):.4e} = g^3 b v/5! (b=2), nonzero",
    )
    phihat = -np.linalg.solve(Q0, LAM0)
    mu = B @ phihat
    check(
        "N10.6-mu-null",
        abs(dual(Q0, mu, mu)) < 1e-14 and abs(dual(Q0, LAM0, mu) + 1) < 1e-14,
        f"mu={mu}, <mu,mu>={dual(Q0, mu, mu):+.1e}, <lam,mu>={dual(Q0, LAM0, mu):+.3f}",
    )
    # no finite boost aligns mu: |mu'_chi / mu'_Sigma| = 1 for every eta
    ratios = [abs((boost(e).T @ mu)[1] / (boost(e).T @ mu)[0]) for e in etas]
    check(
        "N10.6-mu-never-aligned",
        np.allclose(ratios, 1.0, atol=1e-12),
        "|mu'_chi/mu'_Sigma| = 1 on eta in [-3,3]",
    )
    mu_tl = np.array([1.0, 0.5])
    ratios_tl = [abs((boost(e).T @ mu_tl)[1] / (boost(e).T @ mu_tl)[0]) for e in etas]
    break_leg(
        "BREAK-N10.6-timelike-mu-never-aligned",
        np.allclose(ratios_tl, 1.0, atol=1e-12) or min(ratios_tl) > 1e-2,
        f"timelike mu=(1,0.5): min ratio {min(ratios_tl):.2e}",
    )

    # joint doublet at O(g^2)+O(g^3): no single boost removes the chi source
    def chi_source(eta: float, lam: np.ndarray, muv: np.ndarray) -> float:
        L = boost(eta)
        return float(
            np.linalg.norm((L.T @ lam)[1] * M.u + g / 5 * (L.T @ muv)[1] * M.v)
        )

    grid = np.linspace(-4, 4, 80001)
    jmin = min(chi_source(e, LAM0, mu) for e in grid)
    check(
        "N10.6-no-joint-boost",
        jmin > 1e-3 * np.linalg.norm(M.u),
        f"min_eta |J'_chi| = {jmin:.4e} (|u|={np.linalg.norm(M.u):.3f}, g={g})",
    )
    jmin_par = min(chi_source(e, LAM0, np.array([1.0, 0.0])) for e in grid)
    break_leg(
        "BREAK-N10.6-mu-parallel-lam",
        jmin_par > 1e-3 * np.linalg.norm(M.u),
        f"mu || lam (b_chi=0): min |J'_chi| = {jmin_par:.1e}",
    )

    # ---------------- N10.6 / N10.5: exact coefficients through O(g^4) -------------
    c = M.coeffs(Q0, LAM0, B)
    c4_pred = -dual(Q0, mu, mu) * M.vKv / 600
    check(
        "N10.6-R24-closure-is-nullity",
        abs(c[0]) < 1e-7 * abs(M.V4psi)
        and abs(c[1]) < 1e-7 * abs(M.V5psi)
        and abs(c[2]) < 1e-6 * abs(M.vKv / 600),
        f"(c2,c3,c4)=({c[0]:.1e},{c[1]:.1e},{c[2]:.1e}); vK^-1v/600={M.vKv / 600:.4e}",
    )
    B1 = np.array([[1.0, 0.5], [0.5, 0.7]])  # b_chi = 1
    mu1 = B1 @ phihat
    c1 = M.coeffs(Q0, LAM0, B1)
    pred1 = -dual(Q0, mu1, mu1) * M.vKv / 600
    check(
        "N10.6-c4-closed-form[b=1]",
        abs(c1[2] - pred1) < 1e-6 * abs(pred1),
        f"fit c4={c1[2]:.10g}, (1-b^2/4) vK^-1v/600={pred1:.10g}",
    )
    break_leg(
        "BREAK-N10.6-b1-closes",
        abs(c1[2]) < 1e-6 * abs(M.vKv / 600),
        f"b_chi=1: c4={c1[2]:.4e}",
    )
    del c4_pred

    # O(g^3) matching condition <lam,mu> = -1, i.e. phihat^T B phihat = 1 (N10.5)
    Bq = np.array([[0.4, 1.0], [1.0, 0.7]])  # B_SS = 0.4: O(g^3) contact mismatched
    cq = M.coeffs(Q0, LAM0, Bq)
    pred3 = (phihat @ Bq @ phihat - 1) * M.V5psi / 120
    check(
        "N10.5-c3-closed-form",
        abs(cq[1] - pred3) < 1e-7 * abs(M.V5psi),
        f"fit c3={cq[1]:.10g}, (phihat^T B phihat - 1) V5/5!={pred3:.10g}",
    )

    # frame covariance: random GL(2) frames with lam_chi != 0 match through O(g^4)
    for k in range(4):
        G = rng.standard_normal((2, 2))
        if abs(np.linalg.det(G)) < 0.2:
            G = G + np.eye(2)
        Qg, lg, Bg = G.T @ Q0 @ G, G.T @ LAM0, G.T @ B @ G
        cg = M.coeffs(Qg, lg, Bg)
        mug = Bg @ (-np.linalg.solve(Qg, lg))
        ok = (
            abs(cg[0]) < 1e-7 * abs(M.V4psi)
            and abs(cg[1]) < 1e-7 * abs(M.V5psi)
            and abs(cg[2]) < 1e-6 * abs(M.vKv / 600)
        )
        check(
            f"N10.5-covariance[{k}]",
            ok
            and abs(dual(Qg, lg, lg) + 1) < 1e-10
            and abs(dual(Qg, mug, mug)) < 1e-10,
            f"lam={lg.round(3)}, <l,l>={dual(Qg, lg, lg):+.3f}, "
            f"<mu,mu>={dual(Qg, mug, mug):+.1e}, max|c|={np.max(np.abs(cg)):.1e}",
        )
        # the constructed normal form recovers the aligned frame and b_chi = +-2
        Gn = normal_form(Qg, lg)
        Bn = Gn.T @ Bg @ Gn
        check(
            f"N10.5-recover-aligned[{k}]",
            np.allclose(Gn.T @ Qg @ Gn, Q0)
            and np.allclose(Gn.T @ lg, LAM0)
            and abs(Bn[0, 0] - 1) < 1e-9
            and abs(abs(2 * Bn[0, 1]) - 2) < 1e-9,
            f"B_SS={Bn[0, 0]:.6f}, b_chi={2 * Bn[0, 1]:+.6f}",
        )

    # ---------------- summary ----------------------------------------------------
    n_pass = sum(ok for _, ok, _ in results)
    n_fire = sum(f for _, f, _ in breaks)
    print(
        f"\nSUMMARY seed={SEED}: {n_pass}/{len(results)} PASS, "
        f"{n_fire}/{len(breaks)} break legs fire"
    )
    return 0 if (n_pass == len(results) and n_fire == len(breaks)) else 1


if __name__ == "__main__":
    sys.exit(main())
