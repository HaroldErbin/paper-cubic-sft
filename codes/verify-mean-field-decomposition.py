"""
Spot checks for record 069 (mean field à la Weinberg, Task 15a): finite model only.

Record: ``agent/derivations/069-mean-field-decomposition.md``. Check labels = claim-tree nodes.

Finite model (069 A4): H = R^N, omega = 1, V2 a random negative-definite symmetric matrix
(so -omega Q = -V2 > 0 and the Psi Gaussian converges on the real contour), V4 a random
totally symmetric rank-4 tensor, Sigma in Sym^2 H, weight exp(S/hbar) with (R1, V3 = 0)
    S = -g^2/24 V4(Sigma,Sigma) + 1/2 Psi.Q_Sigma.Psi,   Q_Sigma = V2 + g^2/6 V4(Sigma,.,.).
The independent path for every check is tensor Gauss-Hermite quadrature of the Psi integral
(no determinant formula used on that side).

Checks:
  C1.2-oneloop : Z(Sigma)/Z(0) by quadrature = exp(-[V_eff(Sigma)-V_eff(0)]/hbar) with
                 V_eff = g^2/24 V4(Sigma,Sigma) + hbar/2 log det(-Q_Sigma)   (069 (1.4));
                 break: 1/6 -> 1/12 in Q_Sigma.
  C1.3-tadpole : d/d eps [-hbar log Z(eps Sigma)] at eps = 0 (central difference on the
                 quadrature) = -hbar g^2/12 V4(Sigma, G), G = (-V2)^{-1}   (069 (1.5));
                 break: G -> -G.
  C1.4-root    : Newton root of Sigma = hbar (-Q_Sigma)^{-1} matches (1.7) to O(hbar^3):
                 the residual scales as hbar^3 (ratio 1/8 under hbar -> hbar/2); break:
                 drop the hbar^2 term (ratio 1/4).
  C1.4-sd      : at the root, <Psi Psi^T>_{Sigma*} by quadrature = Sigma* (069 (1.3) in the
                 Gaussian theory); break: Sigma* -> 1.1 Sigma*. Near-tautological: the root is
                 defined by Sigma = hbar (-Q_Sigma)^{-1} and the Gaussian second moment is that
                 inverse analytically; the check only confirms that the quadrature covariance
                 has the sign of G (which C1.3 already fixes).
  C2.7-third   : Psi-only quartic theory S = 1/2 Psi.V2.Psi + g^2/24 V4(Psi^4): the O(g^2)
                 term of <Psi Psi^T> by quadrature (polynomial moments, exact for Gauss-Hermite)
                 = hbar G Pi_H G with the Hartree self-energy Pi_H = hbar g^2/2 V4(G,.,.), and
                 equals 3 x the mean-field dressing dSigma*/d(g^2) at g = 0 (Newton roots of
                 (1.6) at two small g, Richardson): the gap equation keeps one third of Hartree
                 (R66's direct channel); break: factor 1 (the identification "mean field =
                 Hartree") must fail.
  C2.4-tadpole : cubic term lam/6 V3(Psi^3) at fixed Sigma: the one-loop gradient on the action
                 side, d/dPsi0 [-hbar/2 log det(-H(Psi0))] at 0 by central difference
                 = +hbar lam/2 V3(G_Sigma,.) (069 (2.4)); and G_Sigma times it = d<Psi>/dlam by
                 quadrature (direct Wick contraction); break: the opposite sign.
  C2.8-joint   : joint Hessian of S[Psi,Sigma] (V3 included, Sigma on its 6 independent
                 coordinates) by finite differences at Psi0 = 0: mixed block = 0 (break:
                 Psi0 != 0 makes it nonzero), and Gamma1_joint = S - hbar/2 log|det(-H)|
                 differs from -V_eff of (1.4) by a Sigma-independent constant (two Sigma
                 values); break: hbar/2 -> hbar in (1.4).
  C2.3-nearwall: one-dimensional instance of (1.4)-(1.6), V = a/4 s^2 + hbar/2 log|1 - a s|,
                 a = g^2 v/6: besides s_- = hbar + O(hbar^2) the gap equation has a root s_+
                 with (s_D - s_+)/hbar -> 1 (distance hbar g^2 in g^2 s from the wall
                 s_D = 1/a), and V''(s_+) < 0 (a maximum); roots found by bisection of V',
                 V'' by finite difference; break: the same test at s_- reports a minimum.
  C2.1-shell   : one-dimensional shell integrals (sympy): the fermionic
                 int_{-k}^{k} dl [sqrt(l^2+d^2) - |l|] has a d^2 log d term (the BCS log),
                 the bosonic PV int_{-k}^{k} dl log|l+d| is analytic in d at d = 0
                 (069 (2.1) discussion). The fermionic case is the leg that shows the
                 detection can fire. Both closed forms are checked numerically against the
                 integrals at one point.
  C2.5-level11-det : with V2 = diag(1,0) on (T,D) (064 Table 1.1: V2(D,D)=0) and the Hankel
                 V4(e_i,X_a,X_b) = h_{i-1+a+b}, det Q_sigma vanishes at sigma = 0 with
                 gradient g^2/6 (h2,h3,h4) (069 (2.5)); break: V2(D,D) = 1.

Not verified: any string statement (regularisation of the trace, ghost sector, tachyon
contour, the obstacles of 069 §2 beyond C2.1's one-dimensional model, C2.3's one-dimensional
model and C2.5's structure). C2.4, C2.7-third and C2.8 are finite-model statements.
"""

from __future__ import annotations

import itertools
import sys
from collections.abc import Callable

import numpy as np
import sympy as sp

SEED = 20261001
failures: list[str] = []
npass = 0


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print a labelled PASS/FAIL line and record failures."""
    global npass
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if ok:
        npass += 1
    else:
        failures.append(name)


def sym4(rng: np.random.Generator, n: int) -> np.ndarray:
    """Random totally symmetric rank-4 tensor."""
    T = np.zeros((n, n, n, n))
    for c in itertools.combinations_with_replacement(range(n), 4):
        v = rng.uniform(-1, 1)
        for p in set(itertools.permutations(c)):
            T[p] = v
    return T


def sym3(rng: np.random.Generator, n: int) -> np.ndarray:
    """Random totally symmetric rank-3 tensor."""
    T = np.zeros((n, n, n))
    for c in itertools.combinations_with_replacement(range(n), 3):
        v = rng.uniform(-1, 1)
        for p in set(itertools.permutations(c)):
            T[p] = v
    return T


def v4_sigma(V4: np.ndarray, Sig: np.ndarray) -> np.ndarray:
    """Matrix V4(Sigma,.,.)_{ij} = Sigma^{kl} V4_{ijkl}."""
    return np.einsum("ijkl,kl->ij", V4, Sig)


def q_sigma(
    V2: np.ndarray, V4: np.ndarray, Sig: np.ndarray, g: float, c: float = 1 / 6
) -> np.ndarray:
    """Q_Sigma = V2 + c g^2 V4(Sigma,.,.), c = 1/6 (R69 C1.1)."""
    return V2 + c * g**2 * v4_sigma(V4, Sig)


def veff(
    V2: np.ndarray,
    V4: np.ndarray,
    Sig: np.ndarray,
    g: float,
    hbar: float,
    c: float = 1 / 6,
) -> float:
    """069 (1.4) without the Sigma-independent constant."""
    M = -q_sigma(V2, V4, Sig, g, c)
    return (
        g**2 / 24 * np.einsum("ij,ijkl,kl", Sig, V4, Sig)
        + hbar / 2 * np.linalg.slogdet(M)[1]
    )


class Quad:
    """Tensor Gauss-Hermite quadrature for int dPsi f(Psi) exp(-Psi.M0.Psi/2hbar)."""

    def __init__(self, M0: np.ndarray, hbar: float, nodes: int = 40) -> None:
        """Build the tensor grid for the Gaussian of covariance hbar M0^{-1}."""
        n = M0.shape[0]
        L = np.linalg.cholesky(M0 / hbar)  # Psi = L^{-T} y, y ~ exp(-y.y/2)
        x, w = np.polynomial.hermite_e.hermegauss(nodes)
        grids = np.meshgrid(*([x] * n), indexing="ij")
        Y = np.stack([gg.ravel() for gg in grids], axis=1)
        W = np.prod(
            np.stack(np.meshgrid(*([w] * n), indexing="ij"), axis=-1).reshape(-1, n),
            axis=1,
        )
        self.Psi = np.linalg.solve(L.T, Y.T).T  # rows: sample points
        self.W = W / abs(np.linalg.det(L))

    def integrate(self, f: Callable[[np.ndarray], np.ndarray]) -> float:
        """Integrate f(Psi) against the Gaussian weight (f vectorised over rows)."""
        return float(np.sum(self.W * f(self.Psi)))


def gaussian_checks(rng: np.random.Generator) -> None:
    """C1.2, C1.3, C1.4: quadrature against the closed forms of 069 §1."""
    N, g, hbar = 3, 0.7, 0.3
    A = rng.uniform(-1, 1, (N, N))
    V2 = -(A @ A.T + N * np.eye(N))  # negative definite: -V2 > 0
    V4 = sym4(rng, N)
    Sig = rng.uniform(-1, 1, (N, N))
    Sig = 0.4 * (Sig + Sig.T)
    M0 = -V2
    quad = Quad(M0, hbar, nodes=40)
    z0 = quad.integrate(lambda P: np.ones(len(P)))

    def weight(dM: np.ndarray) -> Callable[[np.ndarray], np.ndarray]:
        return lambda P: np.exp(np.einsum("ai,ij,aj->a", P, dM, P) / (2 * hbar))

    def z_ratio(S: np.ndarray, c: float = 1 / 6) -> float:
        """Z(S)/Z(0) with the classical Sigma term included, by quadrature."""
        dM = c * g**2 * v4_sigma(V4, S)  # Q_S - V2 ; weight exp(+Psi.dM.Psi/2hbar)
        cl = np.exp(-(g**2) / 24 * np.einsum("ij,ijkl,kl", S, V4, S) / hbar)
        return cl * quad.integrate(weight(dM)) / z0

    # C1.2
    lhs = z_ratio(Sig)
    v0 = veff(V2, V4, 0 * Sig, g, hbar)
    rhs = np.exp(-(veff(V2, V4, Sig, g, hbar) - v0) / hbar)
    rhs_break = np.exp(-(veff(V2, V4, Sig, g, hbar, c=1 / 12) - v0) / hbar)
    report(
        "C1.2-oneloop",
        abs(lhs / rhs - 1) < 1e-9,
        f"quadrature/closed form - 1 = {lhs / rhs - 1:.2e}",
    )
    report(
        "C1.2-oneloop-break",
        abs(lhs / rhs_break - 1) > 1e-3,
        f"with 1/12: {lhs / rhs_break - 1:.2e} (must be far from 0)",
    )

    # C1.3
    G = np.linalg.inv(M0)
    eps = 1e-3
    dV = -hbar * (np.log(z_ratio(eps * Sig)) - np.log(z_ratio(-eps * Sig))) / (2 * eps)
    pred = -hbar * g**2 / 12 * np.einsum("ij,ijkl,kl", Sig, V4, G)
    report(
        "C1.3-tadpole",
        abs(dV - pred) < 1e-6 * max(1, abs(pred)),
        f"num {dV:.10f} vs -hbar g^2/12 V4(Sigma,G) {pred:.10f}",
    )
    report(
        "C1.3-tadpole-break",
        abs(dV + pred) > 1e-3,
        f"with G -> -G: |diff| = {abs(dV + pred):.2e}",
    )

    # C1.4 root
    idx = [(i, j) for i in range(N) for j in range(i, N)]

    def resid(S: np.ndarray, hb: float, gg: float = g) -> np.ndarray:
        return S - hb * np.linalg.inv(-q_sigma(V2, V4, S, gg))

    def root(hb: float, gg: float = g) -> np.ndarray:
        """Newton root of Sigma = hb (-Q_Sigma)^{-1} on the symmetric coordinates."""
        S = hb * G
        for _ in range(50):
            F = resid(S, hb, gg)
            if np.max(abs(F)) < 1e-15:
                break
            J = np.zeros((len(idx), len(idx)))
            for b, (k, m) in enumerate(idx):
                dS = np.zeros((N, N))
                dS[k, m] = dS[m, k] = 1e-6
                Fp = resid(S + dS, hb, gg)
                J[:, b] = [(Fp - F)[i, j] / 1e-6 for (i, j) in idx]
            step = np.linalg.solve(J, [F[i, j] for (i, j) in idx])
            for b, (k, m) in enumerate(idx):
                S[k, m] -= step[b]
                S[m, k] = S[k, m]
        return S

    def pred17(hb: float, second: bool = True) -> np.ndarray:
        """069 (1.7) with or without its hbar^2 term."""
        out = hb * G
        if second:
            out = out + hb**2 * g**2 / 6 * G @ v4_sigma(V4, G) @ G
        return out

    r1 = np.max(abs(root(hbar) - pred17(hbar)))
    r2 = np.max(abs(root(hbar / 2) - pred17(hbar / 2)))
    b1 = np.max(abs(root(hbar) - pred17(hbar, False)))
    b2 = np.max(abs(root(hbar / 2) - pred17(hbar / 2, False)))
    report(
        "C1.4-root",
        abs(r2 / r1 - 1 / 8) < 0.05,
        f"residual ratio hbar/2 : hbar = {r2 / r1:.4f} (expect 1/8 = 0.125)",
    )
    report(
        "C1.4-root-break",
        abs(b2 / b1 - 1 / 4) < 0.05 and abs(b2 / b1 - 1 / 8) > 0.05,
        f"without hbar^2 term: ratio {b2 / b1:.4f} (expect 1/4)",
    )

    # C1.4 Schwinger-Dyson at the root
    Sstar = root(hbar)
    w = weight(g**2 / 6 * v4_sigma(V4, Sstar))
    z = quad.integrate(w)

    def moment(i: int, j: int) -> float:
        return quad.integrate(lambda P: w(P) * P[:, i] * P[:, j]) / z

    mom = np.array([[moment(i, j) for j in range(N)] for i in range(N)])
    report(
        "C1.4-sd",
        np.max(abs(mom - Sstar)) < 1e-8,
        f"max |<Psi Psi> - Sigma*| = {np.max(abs(mom - Sstar)):.2e}",
    )
    report(
        "C1.4-sd-break",
        np.max(abs(mom - 1.1 * Sstar)) > 1e-3,
        f"vs 1.1 Sigma*: {np.max(abs(mom - 1.1 * Sstar)):.2e}",
    )

    # C2.7-third: Hartree self-energy of the Psi-only quartic theory vs the mean-field dressing.
    # d<Psi_i Psi_j>/d(g^2) at g = 0 = (1/24 hbar) [<Psi_i Psi_j q> - <Psi_i Psi_j><q>]_0,
    # q = V4(Psi^4): a degree-6 polynomial moment, exact under 40-node Gauss-Hermite.
    def quartic(P: np.ndarray) -> np.ndarray:
        return np.einsum("ijkl,ai,aj,ak,al->a", V4, P, P, P, P, optimize=True)

    q_mean = quad.integrate(quartic) / z0
    d_quad = np.array(
        [
            [
                (
                    quad.integrate(lambda P, i=i, j=j: P[:, i] * P[:, j] * quartic(P))
                    / z0
                    - hbar * G[i, j] * q_mean
                )
                / (24 * hbar)
                for j in range(N)
            ]
            for i in range(N)
        ]
    )
    hartree = (
        hbar**2 / 2 * G @ v4_sigma(V4, G) @ G
    )  # hbar G Pi_H G, Pi_H = hbar/2 V4(G)
    g_small = 0.05

    def mf_dressing(gg: float) -> np.ndarray:
        return (root(hbar, gg) - hbar * G) / gg**2

    # Richardson in g^2: mf(g) = mf0 + c g^2 + O(g^4)
    mf0 = 2 * mf_dressing(g_small / np.sqrt(2)) - mf_dressing(g_small)
    nrm = np.linalg.norm(d_quad)
    report(
        "C2.7-third-hartree",
        np.linalg.norm(d_quad - hartree) < 1e-10 * nrm,
        f"|quadrature - hbar^2/2 G V4(G) G| / |quadrature| = "
        f"{np.linalg.norm(d_quad - hartree) / nrm:.2e}",
    )
    report(
        "C2.7-third",
        np.linalg.norm(d_quad - 3 * mf0) < 1e-5 * nrm,
        f"|quadrature - 3 x mean-field dressing| / |quadrature| = "
        f"{np.linalg.norm(d_quad - 3 * mf0) / nrm:.2e}; "
        f"projection ratio {np.sum(d_quad * mf0) / np.sum(mf0 * mf0):.6f} (expect 3)",
    )
    report(
        "C2.7-third-break",
        np.linalg.norm(d_quad - mf0) > 0.1 * nrm,
        f"with factor 1 (mean field = Hartree): "
        f"{np.linalg.norm(d_quad - mf0) / nrm:.2e} (must be far from 0)",
    )

    # C2.4-tadpole: cubic term lam/6 V3(Psi^3) at fixed Sigma (action side, weight e^{S/hbar}).
    V3 = sym3(rng, N)
    lam = g
    QS = q_sigma(V2, V4, Sig, g)
    GS = np.linalg.inv(-QS)

    def loop_term(P0: np.ndarray) -> float:
        # Hessian of 1/2 Psi.Q_Sigma.Psi + lam/6 V3(Psi^3) at P0: Q_Sigma + lam V3(P0,.,.)
        H = QS + lam * np.einsum("ijk,k->ij", V3, P0)
        return -hbar / 2 * np.linalg.slogdet(-H)[1]

    eps3 = 1e-5
    grad = np.array(
        [(loop_term(eps3 * e) - loop_term(-eps3 * e)) / (2 * eps3) for e in np.eye(N)]
    )
    pred24 = hbar * lam / 2 * np.einsum("ijk,jk->i", V3, GS)
    report(
        "C2.4-tadpole",
        np.max(abs(grad - pred24)) < 1e-8 * np.max(abs(pred24)),
        f"FD gradient {np.round(grad, 8)} vs +hbar lam/2 V3(G_Sigma) "
        f"{np.round(pred24, 8)}",
    )
    report(
        "C2.4-tadpole-break",
        np.max(abs(grad + pred24)) > 1e-3,
        f"with the opposite sign: max diff {np.max(abs(grad + pred24)):.2e}",
    )
    # <Psi> at O(lam) by quadrature: (1/6 hbar) <Psi_i V3(Psi^3)>_Sigma (degree 4, exact)
    quadS = Quad(-QS, hbar, nodes=40)
    zS = quadS.integrate(lambda P: np.ones(len(P)))
    cubic = lambda P: np.einsum("ijk,ai,aj,ak->a", V3, P, P, P)  # noqa: E731
    dpsi = np.array(
        [
            quadS.integrate(lambda P, i=i: P[:, i] * cubic(P)) / (6 * hbar * zS)
            for i in range(N)
        ]
    )
    report(
        "C2.4-tadpole-wick",
        np.max(abs(GS @ grad / lam - dpsi)) < 1e-8 * np.max(abs(dpsi)),
        f"G_Sigma grad/lam {np.round(GS @ grad / lam, 8)} vs d<Psi>/dlam "
        f"{np.round(dpsi, 8)}",
    )

    # C2.8-joint: joint Hessian by finite differences of S[Psi, Sigma] (V3 included).
    def s_joint(x: np.ndarray, gg: float = g) -> float:
        P = x[:N]
        S = np.zeros((N, N))
        for b, (k, m) in enumerate(idx):
            S[k, m] = S[m, k] = x[N + b]
        return (
            0.5 * P @ V2 @ P
            + gg / 6 * np.einsum("ijk,i,j,k", V3, P, P, P)
            - gg**2 / 24 * np.einsum("ij,ijkl,kl", S, V4, S)
            + gg**2 / 12 * np.einsum("ij,ijkl,k,l", S, V4, P, P)
        )

    def hess(x: np.ndarray, h: float = 1e-3) -> np.ndarray:
        n = len(x)
        E = np.eye(n) * h
        Hm = np.zeros((n, n))
        for a in range(n):
            for b in range(n):
                Hm[a, b] = (
                    s_joint(x + E[a] + E[b])
                    - s_joint(x + E[a] - E[b])
                    - s_joint(x - E[a] + E[b])
                    + s_joint(x - E[a] - E[b])
                ) / (4 * h * h)
        return Hm

    def coords(S: np.ndarray, P: np.ndarray) -> np.ndarray:
        return np.concatenate([P, [S[k, m] for (k, m) in idx]])

    def gamma1_joint(S: np.ndarray) -> float:
        x = coords(S, np.zeros(N))
        return s_joint(x) - hbar / 2 * np.linalg.slogdet(-hess(x))[1]

    H0 = hess(coords(Sig, np.zeros(N)))
    mixed0 = np.max(abs(H0[:N, N:]))
    H1 = hess(coords(Sig, 0.3 * np.ones(N)))
    mixed1 = np.max(abs(H1[:N, N:]))
    report(
        "C2.8-joint-block",
        mixed0 < 1e-8 and mixed1 > 1e-2,
        f"max |H_Psi,Sigma| at Psi0 = 0: {mixed0:.1e}; at Psi0 != 0 (break): {mixed1:.2e}",
    )
    Sb = 0.5 * Sig + 0.1 * np.eye(N)
    lhs28 = gamma1_joint(Sig) - gamma1_joint(Sb)
    rhs28 = -(veff(V2, V4, Sig, g, hbar) - veff(V2, V4, Sb, g, hbar))

    def veff_break(S: np.ndarray) -> float:
        """(1.4) with hbar/2 -> hbar in front of the log (classical term unchanged)."""
        return veff(V2, V4, S, g, 2 * hbar)

    rhs28b = -(veff_break(Sig) - veff_break(Sb))
    report(
        "C2.8-joint",
        abs(lhs28 - rhs28) < 1e-7 * max(1.0, abs(rhs28)),
        f"Gamma1_joint(S_a) - Gamma1_joint(S_b) = {lhs28:.10f} vs "
        f"-[V_eff(S_a) - V_eff(S_b)] = {rhs28:.10f}",
    )
    report(
        "C2.8-joint-break",
        abs(lhs28 - rhs28b) > 1e-3,
        f"with hbar/2 -> hbar: diff {abs(lhs28 - rhs28b):.2e}",
    )


def near_wall_check() -> None:
    """C2.3: 1-d instance of (1.4)-(1.6); near-wall root at distance hbar, a maximum."""
    g, v = 0.7, 1.3
    a = g**2 * v / 6

    def dV(s: float, hb: float) -> float:
        # V = a/4 s^2 + hb/2 log|1 - a s|
        return a / 2 * s - hb / 2 * a / (1 - a * s)

    def V(s: float, hb: float) -> float:
        return a / 4 * s**2 + hb / 2 * np.log(abs(1 - a * s))

    def bisect(f: Callable[[float], float], lo: float, hi: float) -> float:
        flo = f(lo)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if (f(mid) > 0) == (flo > 0):
                lo, flo = mid, f(mid)
            else:
                hi = mid
        return 0.5 * (lo + hi)

    sD = 1 / a
    out = []
    for hb in (1e-2, 1e-3):
        # V'(sD/2) = 1/4 - a hb > 0 and V' -> -infinity as s -> sD^-: one root on each side
        sp_ = bisect(lambda s, hb=hb: dV(s, hb), 0.5 * sD, sD - 1e-14)
        sm_ = bisect(lambda s, hb=hb: dV(s, hb), 1e-12, 0.5 * sD)
        h = 1e-3 * hb
        d2p = (V(sp_ + h, hb) - 2 * V(sp_, hb) + V(sp_ - h, hb)) / h**2
        d2m = (V(sm_ + h, hb) - 2 * V(sm_, hb) + V(sm_ - h, hb)) / h**2
        out.append((hb, (sD - sp_) / hb, d2p, sm_ / hb, d2m))
    (h1, r1, d2p1, m1, d2m1), (h2, r2, d2p2, m2, d2m2) = out
    ok = (
        abs(r1 - 1) < 3 * a * h1
        and abs(r2 - 1) < 3 * a * h2
        and abs(r2 - 1) < 0.2 * abs(r1 - 1)
        and d2p1 < 0
        and d2p2 < 0
    )
    report(
        "C2.3-nearwall",
        ok,
        f"(s_D - s_+)/hbar = {r1:.6f} (hbar={h1}), {r2:.6f} (hbar={h2}); "
        f"V''(s_+) = {d2p1:.3e}, {d2p2:.3e} (maximum); s_-/hbar = {m1:.6f}, {m2:.6f}",
    )
    report(
        "C2.3-nearwall-break",
        d2m1 > 0 and d2m2 > 0,
        f"same test at s_-: V''(s_-) = {d2m1:.3e}, {d2m2:.3e} > 0 (a minimum, so the "
        "maximum test can fail)",
    )


def shell_check() -> None:
    """C2.1: BCS log in the fermionic shell integral, none in the bosonic PV integral."""
    ell, d, k = sp.symbols("l d k", positive=True)
    sub = {k: 3, d: sp.Rational(1, 2)}
    # closed form of 2 int_0^k [sqrt(l^2+d^2) - l] dl (asinh written as a log so that sympy
    # can expand at d -> 0)
    ferm = (
        k * sp.sqrt(k**2 + d**2)
        + d**2 * sp.log(k / d + sp.sqrt(k**2 / d**2 + 1))
        - k**2
    )
    ferm_num = (
        sp.Integral(2 * (sp.sqrt(ell**2 + d**2) - ell), (ell, 0, k)).subs(sub).evalf(20)
    )
    ferm_ok = abs(float(ferm_num - ferm.subs(sub).evalf(20))) < 1e-12
    ferm_s = sp.series(ferm, d, 0, 4).removeO()
    # bosonic PV: int_{-k}^{k} log|l+d| dl = (k+d)log(k+d) + (k-d)log(k-d) - 2k  (0<d<k)
    bos = (k + d) * sp.log(k + d) + (k - d) * sp.log(k - d) - 2 * k
    bos_num = (
        (
            sp.Integral(sp.log(ell + d), (ell, -d, k))
            + sp.Integral(sp.log(-ell - d), (ell, -k, -d))
        )
        .subs(sub)
        .evalf(20)
    )
    bos_ok = abs(float(bos_num - bos.subs(sub).evalf(20))) < 1e-12
    bos_s = sp.series(bos, d, 0, 4).removeO()
    report(
        "C2.1-shell",
        ferm_ok and bos_ok and ferm_s.has(sp.log(d)) and not bos_s.has(sp.log(d)),
        f"closed forms ok: {ferm_ok}, {bos_ok}; fermion series {ferm_s} has log d: {ferm_s.has(sp.log(d))}; "
        f"boson PV series {sp.expand(bos_s)} has log d: {bos_s.has(sp.log(d))}",
    )


def level11_check() -> None:
    """C2.5: det Q_sigma at level (1,1), zero momentum, vanishes linearly at sigma = 0."""
    h = sp.symbols("h0:5")
    s1, s2, s3 = sp.symbols("sigma1:4")
    gs = sp.Symbol("g")

    def V4e(i: int) -> sp.Matrix:
        """V4(e_i, X_a, X_b) = h_{i-1+a+b}, a,b in {0 (T), 1 (D)} (064 Hankel structure)."""
        return sp.Matrix(2, 2, lambda a, b: h[i - 1 + a + b])

    dressing = gs**2 / 6 * (s1 * V4e(1) + s2 * V4e(2) + s3 * V4e(3))
    zero = {s1: 0, s2: 0, s3: 0}
    det = sp.expand((sp.diag(1, 0) + dressing).det())
    grad = [sp.diff(det, v).subs(zero) for v in (s1, s2, s3)]
    ok = det.subs(zero) == 0 and grad == [
        gs**2 / 6 * h[2],
        gs**2 / 6 * h[3],
        gs**2 / 6 * h[4],
    ]
    report("C2.5-level11-det", ok, f"det Q_sigma(0) = {det.subs(zero)}, grad = {grad}")
    det_b = (sp.diag(1, 1) + dressing).det().subs(zero)
    report(
        "C2.5-level11-det-break",
        det_b == 1,
        "with V2(D,D)=1 the determinant is 1 at sigma=0",
    )


def main() -> int:
    """Run all checks; return 1 on any failure."""
    print(f"seed = {SEED}")
    gaussian_checks(np.random.default_rng(SEED))
    shell_check()
    near_wall_check()
    level11_check()
    print(
        f"\nSUMMARY: {npass} PASS, {len(failures)} FAIL"
        + (f" -> {failures}" if failures else "")
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
