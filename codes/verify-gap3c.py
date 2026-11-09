"""
Verify GAP-3c (record 043, addendum 2026-09-26).

The residual freedom of the flat admissible representative of the Sigma_2 gauge law
is physically trivial.

Setting (043 §1-§5, 053 §3-§5, 056 §2). The auxiliary sector enters the action only
through the Psi-dependent quadratic form K(Psi)(X, X) (043 A3). A gauge law
delta X = F_u(X) is *admissible* iff it preserves K(X, X):

    K(X, F_u(X)) = -1/2 (d_u K)(X, X)          (043 (3.1); linear case: K R + R^T K = -d_u K)

and its closure defect is the curvature (043 (4.1), 053 (4.1))

    E = d_{u1} F_{u2} - d_{u2} F_{u1} + [F_{u1}, F_{u2}]_Lie,
    [X, Z]_Lie = DZ . X - DX . Z   (linear F = R X: E = (d1 R2 - d2 R1 + [R2, R1]) X).

The flat representative (043 (5.1), 053/056 convention Yhat = calG(Psi) X) is
calG = M^{1/2}, M = p^{-1} K, Rhat_u = -calG^{-1} d_u calG.
Addendum claim: the flat admissible laws are exactly those of h_Psi o calG with h_Psi
a Psi-dependent map preserving p(Yhat, Yhat), h_0 = id; each differs from Rhat by a
trivial symmetry (K Delta R antisymmetric; nonlinear: K(X, Delta F(X)) = 0) and has E = 0.

Model: finite, float64, JAX forward-mode derivatives (no finite differences).
V = R^D with a random symmetric *indefinite* p; field space R^n;
  model "lin":  K(Psi) = p - (g/5) P_Psi                  (043's S_3)
  model "quad": K(Psi) = p - (g/5) P_Psi + g^2 Q(Psi, Psi)  (a generic Psi-dependent
                symmetric form, standing in for 053's saddle Hessian calK(Psi)).
P_a, Q_ab random symmetric. Only the symmetry of K is used by the claims; total symmetry
of the string vertices is not needed and not modelled (the model is a superset).

Checks are named after the addendum nodes (C5.*). Break legs (expected to FAIL the
property, reported as PASS when they do) end in "-break".

Not verified here: the Frobenius/Koszul steps of the characterisation C5.1 (analytic,
cited from 053 §3, §5), the O(g_s^4) Morse map itself (053, R57), and anything about
convergence (formal series only in the record; here g is a small number).
"""

from __future__ import annotations

import os
import sys

os.environ.setdefault("JAX_PLATFORMS", "cpu")  # CPU only: small dense algebra

import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402
import numpy as np  # noqa: E402
from jax.scipy.linalg import expm  # noqa: E402

jax.config.update("jax_enable_x64", True)

SEED = 20260926
D, NPSI = 5, 3
TOL = 1e-10  # relative tolerance for identities (float64, DB square root)

RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, info: str) -> None:
    """Store and print one named PASS/FAIL line."""
    RESULTS.append((name, ok, info))
    print(f"{'PASS' if ok else 'FAIL'}  {name:22s} {info}")


def sym(a: np.ndarray) -> np.ndarray:
    """Symmetrise the last two axes."""
    return 0.5 * (a + np.swapaxes(a, -1, -2))


def asym(a: np.ndarray) -> np.ndarray:
    """Antisymmetrise the last two axes."""
    return 0.5 * (a - np.swapaxes(a, -1, -2))


def sqrtm_db(m: jnp.ndarray, iters: int = 30) -> jnp.ndarray:
    """
    Principal square root by the Denman-Beavers iteration.

    Y_{k+1} = (Y_k + Z_k^{-1})/2, Z_{k+1} = (Z_k + Y_k^{-1})/2, Y_0 = M, Z_0 = 1;
    Y_k -> M^{1/2}. Differentiable (products and inverses only). Valid for M near 1.

    Args:
        m: square matrix with spectrum away from the negative real axis.
        iters: number of iterations (quadratic convergence near 1).

    Returns:
        jnp.ndarray: M^{1/2}.

    """
    y, z = m, jnp.eye(m.shape[0])
    for _ in range(iters):
        y, z = 0.5 * (y + jnp.linalg.inv(z)), 0.5 * (z + jnp.linalg.inv(y))
    return y


def d_dir(f, psi: jnp.ndarray, u: jnp.ndarray):
    """Directional derivative d_u f at psi (forward mode)."""
    return jax.jvp(f, (psi,), (u,))[1]


def rel(x, scale) -> float:
    """Relative size ||x|| / ||scale||."""
    return float(jnp.linalg.norm(x) / jnp.linalg.norm(scale))


class Model:
    """Random finite model of the auxiliary sector (see module docstring)."""

    def __init__(self, rng: np.random.Generator, quad: bool, g: float) -> None:
        """Draw the random tensors (seeded generator `rng`) at coupling `g`."""
        self.g = g
        # well-conditioned indefinite p: random orthogonal frame, eigenvalues |.| in [2, 3]
        qo, _ = np.linalg.qr(rng.normal(size=(D, D)))
        self.p = jnp.asarray(qo @ np.diag([3.0, -2.0, 2.5, -3.0, 2.0]) @ qo.T)
        self.pinv = jnp.linalg.inv(self.p)
        pa = sym(rng.normal(size=(NPSI, D, D)))
        self.P = jnp.asarray(pa / np.linalg.norm(pa, ord=2, axis=(1, 2))[:, None, None])
        q = sym(rng.normal(size=(NPSI, NPSI, D, D)))
        q = 0.5 * (q + np.swapaxes(q, 0, 1))
        q = q / np.max(np.linalg.norm(q, ord=2, axis=(2, 3)))
        self.Q = jnp.asarray(q) if quad else jnp.zeros_like(jnp.asarray(q))
        # residual rotation data: p-antisymmetric generators Omega = p^{-1} X, X^T = -X
        self.Xa = jnp.einsum(
            "ij,ajk->aik", self.pinv, asym(rng.normal(size=(NPSI, D, D)))
        )
        self.Xab = jnp.einsum(
            "ij,abjk->abik", self.pinv, asym(rng.normal(size=(NPSI, NPSI, D, D)))
        )
        # nonlinear p-antisymmetric generator, linear in Yhat (C5.5)
        self.Xak = jnp.einsum(
            "ij,akjl->akil", self.pinv, asym(rng.normal(size=(NPSI, D, D, D)))
        )
        # break data: p-SYMMETRIC generator (non-orthogonal H), non-closed antisym S
        self.Sa = jnp.einsum(
            "ij,ajk->aik", self.pinv, sym(rng.normal(size=(NPSI, D, D)))
        )
        self.Yab = jnp.asarray(asym(rng.normal(size=(NPSI, NPSI, D, D))))
        self.C = jnp.asarray(
            0.5 * (lambda c: c + np.swapaxes(c, 1, 2))(rng.normal(size=(D, D, D)))
        )
        self.w = jnp.asarray(rng.normal(size=NPSI))

    # ---- the form and the two representatives ---------------------------------
    def K(self, psi):
        """Return the form p - (g/5) P_Psi + g^2 Q(Psi, Psi)."""
        g = self.g
        return (
            self.p
            - (g / 5) * jnp.einsum("a,aij->ij", psi, self.P)
            + g**2 * jnp.einsum("a,b,abij->ij", psi, psi, self.Q)
        )

    def calG(self, psi):
        """Return calG = M^{1/2}, M = p^{-1} K (043 (5.2): Yhat = M^{1/2} X)."""
        return sqrtm_db(self.pinv @ self.K(psi))

    def R17(self, psi, u):
        """Symmetric-logarithmic-derivative law -1/2 K^{-1} d_u K (043 (3.4))."""
        return -0.5 * jnp.linalg.solve(self.K(psi), d_dir(self.K, psi, u))

    @staticmethod
    def pure_gauge(gmap):
        """Law of X for which Yhat = gmap(psi) X is inert: -gmap^{-1} d_u gmap."""
        return lambda psi, u: -jnp.linalg.solve(gmap(psi), d_dir(gmap, psi, u))

    # ---- residual rotations -----------------------------------------------------
    def Omega(self, psi):
        """Return the p-antisymmetric generator of the rotation; zero at Psi = 0."""
        g = self.g
        return g * jnp.einsum("a,aij->ij", psi, self.Xa) + g**2 * jnp.einsum(
            "a,b,abij->ij", psi, psi, self.Xab
        )

    def H(self, psi):
        """Return the Psi-dependent p-orthogonal rotation (1 at Psi = 0, 1 + O(g))."""
        return expm(self.Omega(psi))

    def Hsym(self, psi):
        """Break: Psi-dependent NON-orthogonal map (p-symmetric generator)."""
        return expm(0.3 * self.g * jnp.einsum("a,aij->ij", psi, self.Sa))


def adm_residual(m: Model, law, psi, u) -> float:
    """Relative violation of K R + R^T K + d_u K = 0 (043 (3.2))."""
    k, r, dk = m.K(psi), law(psi, u), d_dir(m.K, psi, u)
    return rel(k @ r + r.T @ k + dk, dk)


def curvature(law, psi, u1, u2):
    """E = d1 R2 - d2 R1 + [R2, R1] (043 (4.1)), generic, from the law alone."""
    d1r2 = d_dir(lambda q: law(q, u2), psi, u1)
    d2r1 = d_dir(lambda q: law(q, u1), psi, u2)
    r1, r2 = law(psi, u1), law(psi, u2)
    return d1r2 - d2r1 + r2 @ r1 - r1 @ r2


def run_linear(m: Model, rng: np.random.Generator, tag: str) -> None:
    """Run checks C5.1-C5.4 and their break legs on one model."""
    psi = jnp.asarray(rng.normal(size=NPSI))
    u1, u2 = jnp.asarray(rng.normal(size=NPSI)), jnp.asarray(rng.normal(size=NPSI))
    mm = m.pinv @ m.K(psi)
    spec = float(jnp.max(jnp.abs(jnp.linalg.eigvals(mm - jnp.eye(D)))))
    cg2 = rel(m.calG(psi) @ m.calG(psi) - mm, mm)
    record(
        f"model[{tag}]",
        spec < 0.5 and cg2 < 1e-13,
        f"spectral radius of M-1 {spec:.2f} (<0.5); |calG^2-M|/|M|={cg2:.1e}",
    )
    rhat = Model.pure_gauge(m.calG)
    e17 = curvature(m.R17, psi, u1, u2)
    scale_r = m.R17(psi, u1)

    # baseline: Rhat admissible and flat, R17 curved (makes the flatness checks non-vacuous)
    a0 = adm_residual(m, rhat, psi, u1)
    e0 = rel(curvature(rhat, psi, u1, u2), e17)
    record(
        f"C5.1-base[{tag}]",
        a0 < TOL and e0 < TOL and float(jnp.linalg.norm(e17)) > 1e-6,
        f"adm(Rhat)={a0:.1e} |E[Rhat]|/|E[R17]|={e0:.1e} |E[R17]|={float(jnp.linalg.norm(e17)):.2e}",
    )

    # C5.2: constant p-orthogonal O and constant non-orthogonal L leave the law unchanged
    rot = expm(jnp.einsum("a,aij->ij", jnp.asarray(rng.normal(size=NPSI)), m.Xa))
    L = jnp.asarray(np.eye(D) + 0.3 * rng.normal(size=(D, D)))
    dO = rel(
        Model.pure_gauge(lambda q: rot @ m.calG(q))(psi, u1) - rhat(psi, u1), scale_r
    )
    dL = rel(
        Model.pure_gauge(lambda q: L @ m.calG(q))(psi, u1) - rhat(psi, u1), scale_r
    )
    orthO = rel(rot.T @ m.p @ rot - m.p, m.p)
    orthL = rel(L.T @ m.p @ L - m.p, m.p)
    record(
        f"C5.2[{tag}]",
        dO < TOL and orthO < TOL,
        f"O^T p O=p to {orthO:.1e}; |R'-Rhat|/|R|={dO:.1e}",
    )
    record(
        f"C5.2-nonorth[{tag}]",
        dL < TOL and orthL > 1e-2,
        f"L non-orthogonal ({orthL:.2f}); law still unchanged |R'-Rhat|/|R|={dL:.1e}",
    )

    # C5.3: Psi-dependent p-orthogonal H: Delta R = -calG^{-1}(H^{-1} d_u H) calG, K Delta R antisym
    gp = lambda q: m.H(q) @ m.calG(q)  # noqa: E731
    rp = Model.pure_gauge(gp)
    cg, hh = m.calG(psi), m.H(psi)
    dh = d_dir(m.H, psi, u1)
    dR_pred = -jnp.linalg.solve(cg, jnp.linalg.solve(hh, dh) @ cg)
    dR = rp(psi, u1) - rhat(psi, u1)
    S = m.K(psi) @ dR
    c1 = rel(dR - dR_pred, dR)
    c2 = rel(S + S.T, S)
    a1 = adm_residual(m, rp, psi, u1)
    record(
        f"C5.3[{tag}]",
        c1 < TOL and c2 < TOL and a1 < TOL and rel(dR, scale_r) > 1e-3,
        f"DeltaR vs formula {c1:.1e}; |S+S^T|/|S|={c2:.1e}; adm(R')={a1:.1e}; |DeltaR|/|R|={rel(dR, scale_r):.2e}",
    )

    # C5.3-gauge: R' = g Rhat g^{-1} + (d g) g^{-1}, g = calG^{-1} H^{-1} calG, g^T K g = K
    gg = lambda q: jnp.linalg.solve(m.calG(q), jnp.linalg.solve(m.H(q), m.calG(q)))  # noqa: E731
    g0 = gg(psi)
    rg = g0 @ rhat(psi, u1) @ jnp.linalg.inv(g0) + d_dir(gg, psi, u1) @ jnp.linalg.inv(
        g0
    )
    c3 = rel(rg - rp(psi, u1), dR)
    c4 = rel(g0.T @ m.K(psi) @ g0 - m.K(psi), m.K(psi))
    record(
        f"C5.3-gauge[{tag}]",
        c3 < TOL and c4 < TOL,
        f"|gRg^-1+dg g^-1 - R'|/|DeltaR|={c3:.1e}; g^T K g=K to {c4:.1e}",
    )

    # C5.3-break: Psi-dependent NON-orthogonal map: still flat, no longer admissible
    rs = Model.pure_gauge(lambda q: m.Hsym(q) @ m.calG(q))
    a2 = adm_residual(m, rs, psi, u1)
    e2 = rel(curvature(rs, psi, u1, u2), e17)
    record(
        f"C5.3-break[{tag}]",
        a2 > 1e-3 and e2 < TOL,
        f"adm residual {a2:.2e} (must be large); |E|/|E[R17]|={e2:.1e} (flat)",
    )

    # C5.4-flat: E[R'] = 0 for the rotated representative
    e3 = rel(curvature(rp, psi, u1, u2), e17)
    record(f"C5.4-flat[{tag}]", e3 < TOL, f"|E[R']|/|E[R17]|={e3:.1e}")

    # C5.4-cov: E[g.R17] = g E[R17] g^{-1} (R17 curved, explicit law, no pure-gauge structure)
    def law_g17(q, u):
        gq = gg(q)
        return gq @ m.R17(q, u) @ jnp.linalg.inv(gq) + d_dir(gg, q, u) @ jnp.linalg.inv(
            gq
        )

    eg = curvature(law_g17, psi, u1, u2)
    c5 = rel(eg - g0 @ e17 @ jnp.linalg.inv(g0), e17)
    moved = rel(eg - e17, e17)
    record(
        f"C5.4-cov[{tag}]",
        c5 < TOL and moved > 1e-4,
        f"|E[gR]-gEg^-1|/|E|={c5:.1e}; E itself moved by {moved:.1e} (conjugation, non-vacuous)",
    )

    # C5.4-break: admissible but NOT pure-gauge trivial-symmetry shift changes E
    def law_break(q, u):
        s = m.g**2 * jnp.einsum("a,b,abij->ij", q, u, m.Yab)  # antisym, curl != 0
        return rhat(q, u) + jnp.linalg.solve(m.K(q), s)

    a4 = adm_residual(m, law_break, psi, u1)
    e4 = rel(curvature(law_break, psi, u1, u2), e17)
    ke = m.K(psi) @ curvature(law_break, psi, u1, u2)
    c6 = rel(ke + ke.T, ke)
    record(
        f"C5.4-break[{tag}]",
        a4 < TOL and e4 > 1e-3 and c6 < TOL,
        f"adm={a4:.1e}; |E|/|E[R17]|={e4:.2e} (must be large); K E antisym to {c6:.1e}",
    )


def run_order(rng_seed: int) -> None:
    """C5.4-order: E[g.R17] - E[R17] = O(g^3) and E[R17] = g^2/100 [A1,A2] + O(g^3)."""
    diffs, lead = [], []
    for gval in (0.02, 0.01):
        rng = np.random.default_rng(rng_seed)
        m = Model(rng, quad=False, g=gval)
        psi = jnp.asarray(rng.normal(size=NPSI))
        u1, u2 = jnp.asarray(rng.normal(size=NPSI)), jnp.asarray(rng.normal(size=NPSI))

        def gg(q, m=m):
            return jnp.linalg.solve(m.calG(q), jnp.linalg.solve(m.H(q), m.calG(q)))

        def law_g17(q, u, m=m, gg=gg):
            gq = gg(q)
            return gq @ m.R17(q, u) @ jnp.linalg.inv(gq) + d_dir(
                gg, q, u
            ) @ jnp.linalg.inv(gq)

        e17 = curvature(m.R17, psi, u1, u2)
        eg = curvature(law_g17, psi, u1, u2)
        A1 = m.pinv @ jnp.einsum("a,aij->ij", u1, m.P)
        A2 = m.pinv @ jnp.einsum("a,aij->ij", u2, m.P)
        r45 = gval**2 / 100 * (A1 @ A2 - A2 @ A1)
        diffs.append(float(jnp.linalg.norm(eg - e17)))
        lead.append(float(jnp.linalg.norm(e17 - r45)))
    r1, r2 = diffs[0] / diffs[1], lead[0] / lead[1]
    record(
        "C5.4-order",
        7.5 < r1 < 8.5 and 7.5 < r2 < 8.5,
        f"|E[gR17]-E[R17]| halving ratio {r1:.3f} (8 = O(g^3)); "
        f"|E[R17]-g^2/100[A1,A2]| ratio {r2:.3f} (R45 leading term invariant)",
    )


def run_nonlinear(m: Model, rng: np.random.Generator) -> None:
    """C5.5 (nonlinear residual freedom, C1.1) and C5.7 (056 §5a) with break legs."""
    psi = jnp.asarray(rng.normal(size=NPSI))
    u1, u2 = jnp.asarray(rng.normal(size=NPSI)), jnp.asarray(rng.normal(size=NPSI))
    x = jnp.asarray(0.5 * rng.normal(size=D))
    g = m.g

    def h(q, y):
        """Map y to expm(Omega(q, y)) y: p-preserving, Omega p-antisym, h_0 = id."""
        om = g * jnp.einsum("a,aij->ij", q, m.Xa) + g * jnp.einsum(
            "a,k,akij->ij", q, y, m.Xak
        )
        return expm(om) @ y

    def h_bad(q, y):
        """Break: Psi-dependent nonlinear map NOT preserving p."""
        return y + g * jnp.dot(m.w, q) * jnp.einsum("ijk,j,k->i", m.C, y, y)

    def law_of(Gmap):
        """F_u(X) = -(D_X Gmap)^{-1} d_u Gmap (053 (4.2))."""

        def F(q, u, xx):
            J = jax.jacfwd(lambda z: Gmap(q, z))(xx)
            dG = jax.jvp(lambda qq: Gmap(qq, xx), (q,), (u,))[1]
            return -jnp.linalg.solve(J, dG)

        return F

    def curv_nl(F, q, xx):
        """E = d1 F2 - d2 F1 + DF2.F1 - DF1.F2 (053 (4.1))."""
        d1f2 = jax.jvp(lambda qq: F(qq, u2, xx), (q,), (u1,))[1]
        d2f1 = jax.jvp(lambda qq: F(qq, u1, xx), (q,), (u2,))[1]
        f1, f2 = F(q, u1, xx), F(q, u2, xx)
        Df1 = jax.jacfwd(lambda z: F(q, u1, z))(xx)
        Df2 = jax.jacfwd(lambda z: F(q, u2, z))(xx)
        return d1f2 - d2f1 + Df2 @ f1 - Df1 @ f2

    def adm_nl(F, q, xx) -> float:
        """Relative violation of K(X, F_u) + 1/2 d_u K(X, X) = 0 (043 (3.1))."""
        dk = d_dir(m.K, q, u1)
        return float(
            abs(xx @ m.K(q) @ F(q, u1, xx) + 0.5 * xx @ dk @ xx)
            / abs(0.5 * xx @ dk @ xx)
        )

    Gflat = lambda q, xx: m.calG(q) @ xx  # noqa: E731
    Fflat = law_of(Gflat)
    Fh = law_of(lambda q, xx: h(q, m.calG(q) @ xx))
    Fbad = law_of(lambda q, xx: h_bad(q, m.calG(q) @ xx))
    e17 = float(jnp.linalg.norm(curvature(m.R17, psi, u1, u2) @ x))

    dF = Fh(psi, u1, x) - Fflat(psi, u1, x)
    stab = float(
        abs(x @ m.K(psi) @ dF) / (jnp.linalg.norm(m.K(psi) @ x) * jnp.linalg.norm(dF))
    )
    a5 = adm_nl(Fh, psi, x)
    e5 = float(jnp.linalg.norm(curv_nl(Fh, psi, x))) / e17
    record(
        "C5.5",
        a5 < TOL
        and stab < TOL
        and e5 < TOL
        and float(jnp.linalg.norm(dF))
        > 1e-4 * float(jnp.linalg.norm(Fflat(psi, u1, x))),
        f"adm(F^h)={a5:.1e}; K(X,DeltaF) normalised={stab:.1e}; |E_Lie[F^h]|/|E[R17]X|={e5:.1e}",
    )
    ab = adm_nl(Fbad, psi, x)
    eb = float(jnp.linalg.norm(curv_nl(Fbad, psi, x))) / e17
    record(
        "C5.5-break",
        ab > 1e-3 and eb < TOL,
        f"non-p-preserving h: adm residual {ab:.2e} (must be large); flat |E|={eb:.1e}",
    )

    # C5.7: Psi-independent nonlinear H o calG leaves F^flat (and hence Psi-hat^+) unchanged
    Hc = lambda y: y + jnp.einsum("ijk,j,k->i", m.C, y, y) + 0.2 * jnp.tanh(y)  # noqa: E731
    GH = lambda q, xx: Hc(m.calG(q) @ xx)  # noqa: E731
    FH = law_of(GH)
    c7 = rel(FH(psi, u1, x) - Fflat(psi, u1, x), Fflat(psi, u1, x))
    # direct 056 (2.4): Psi-hat^+ = Psi^+ - (d_Psi G)^T (D_Y G)^{-T} Y^+, for G and H o G
    yplus = jnp.asarray(rng.normal(size=D))

    def psihat_shift(Gmap):
        J = jax.jacfwd(lambda z: Gmap(psi, z))(x)
        dPsiG = jax.jacfwd(lambda q: Gmap(q, x))(psi)  # D x NPSI
        return -dPsiG.T @ jnp.linalg.solve(J.T, yplus)

    s0, s1 = psihat_shift(Gflat), psihat_shift(GH)
    c8 = rel(s1 - s0, s0)
    # (2.7): Psi-hat^+ . w - Psi^+ . w = Y^+ . F^flat_w
    c9 = float(
        abs(s0 @ u1 - yplus @ Fflat(psi, u1, x)) / abs(yplus @ Fflat(psi, u1, x))
    )
    record(
        "C5.7",
        c7 < TOL and c8 < TOL and c9 < TOL,
        f"|F[HoG]-F[G]|/|F|={c7:.1e}; Psi-hat^+ shift unchanged {c8:.1e}; (2.7) {c9:.1e}",
    )
    GHb = lambda q, xx: Hc(m.calG(q) @ xx) + g * jnp.dot(m.w, q) * (m.calG(q) @ xx)  # noqa: E731
    c10 = rel(law_of(GHb)(psi, u1, x) - Fflat(psi, u1, x), Fflat(psi, u1, x))
    record("C5.7-break", c10 > 1e-3, f"Psi-DEPENDENT H changes F^flat by {c10:.2e}")


def main() -> int:
    """Run all checks; return the exit code (1 on any FAIL)."""
    print(f"verify-gap3c: seed {SEED}, D={D}, n={NPSI}, tol {TOL:g}")
    rng = np.random.default_rng(SEED)
    # sanity of the square root against scipy (independent algorithm)
    import scipy.linalg as sla

    m = Model(rng, quad=False, g=0.2)
    psi = jnp.asarray(rng.normal(size=NPSI))
    mm = np.asarray(m.pinv @ m.K(psi))
    c = rel(m.calG(psi) - jnp.asarray(sla.sqrtm(mm).real), m.calG(psi))
    record("sqrt-sanity", c < 1e-12, f"Denman-Beavers vs scipy sqrtm {c:.1e}")

    for quad, gval in ((False, 0.2), (False, 0.1), (True, 0.2), (True, 0.1)):
        tag = f"{'quad' if quad else 'lin'},g={gval}"
        run_linear(Model(rng, quad=quad, g=gval), rng, tag)
    run_order(SEED + 1)
    run_nonlinear(Model(rng, quad=True, g=0.2), rng)

    nfail = sum(not ok for _, ok, _ in RESULTS)
    print(f"SUMMARY: {len(RESULTS)} checks, {len(RESULTS) - nfail} PASS, {nfail} FAIL")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
