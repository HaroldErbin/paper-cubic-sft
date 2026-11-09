"""
Complex-s line of Task 18c (record 051): frozen-momentum zero scan of F(s,0,0) (group c5).

What is verified (group ``c5``, record 051 section 18c.5)
---------------------------------------------------------
The frozen-momentum contact term of ledger R48 at t = u = 0,

    F(s,0,0) = 4 beta^{8 - s/2} G(s),
    G(s) = J(s/4, -s/4) + J(-s/4, s/4) + J(-s/4, -s/4),        (alpha' = 1)

with J(p,q) = int_R |Z|^p |1-Z|^q d^2Z over R = FD cap V_{0,4} (record 044/045), is an
entire function of s; its zeros are the zeros of G.  The scan locates the zeros of G in the
rectangle Re s in [-40, 20], |Im s| <= 10 (the strip of 049 Part 2 item 5) for
beta in {3/2, 2}, by the argument principle on the rectangle boundary, quadtree
subdivision, Newton refinement, and a winding count on a small circle for the multiplicity.

Analytic continuation of the evaluators to complex exponents (record 051 A6).  The
integrand |Z|^p |1-Z|^q = exp(p ln|Z| + q ln|1-Z|) is entire in (p, q) with *no* phase
from arg Z, so (i) the direct 2D quadrature continues verbatim and (ii) the sharp bound
is |J(p,q)| <= J(Re p, Re q).  The boundary representation of R50 continues as

    J = (1/2i) oint_{dR} G^*(Z) dG(Z),   G' = f = Z^{p/2} (1-Z)^{q/2},
    G^*(Z) := conj(G(Z; conj p, conj q)),  d/dZbar G^* = f^*,  f f^* = |Z|^p |1-Z|^q,

which is Green's theorem for the (1,0)-form G^* f dZ; at real exponents G^* = conj(G) and
it reduces to R50's (1/2) Im oint conj(G) dG.  The boundary route loses digits at complex
exponents: |f| carries exp(-Im p arg Z / 2 - Im q arg(1-Z) / 2), so the integrand of the
boundary formula is larger than J by up to exp(pi |Im s| / 2) for the tiles of G, i.e.
about 7 digits at |Im s| = 10 (checked, C2-cond).

Checks (named after the claim-tree nodes of record 051):
  C1            F(s,0,0) = 4 beta^{8-s/2} G(s) equals the six-tile ``contact_F`` of R50's
                script with ``J_boundary_cheb`` at seeded real s; F(0,0,0) = 12 Vol beta^8;
  C2-real       ``j_vec_c`` at real exponents equals ``j_vec`` of verify-kp-kernel.py;
  C2-2d         ``j_vec_c`` at seeded complex exponents equals the direct 2D quadrature
                ``j_2d_c`` (the defining integral, continued verbatim; n = 120, converged
                to ~1e-8 as n^{-3});
  C2-hyp        the same against the mpmath 2F1 route continued as above (``j_hyp_c``);
  C2-growth     |J(p,q)| <= J(Re p, Re q) at seeded complex points, and the ratio is
                strictly below 1 at Im p != 0 (the bound is sharp, not vacuous);
  C2-cond       the digit loss of the boundary route at Im s = 10 is as estimated
                (agreement with j_2d_c to 1e-7, not to 1e-12);
  C3-real       G(s) > 0 on the real interval [-40, 20] at beta = 3/2 (no real zero: a
                positive integrand), and likewise C4-real at beta = 2;
  C3-wind       the winding number of F(s,0,0) around the rectangle
                [-40,20] x [-10,10]i equals the number of zeros found (with multiplicity)
                by subdivision + Newton, at beta = 3/2; C4-wind at beta = 2;
  C3-newton     every located zero satisfies |F| < 1e-9 |F|_typical and the winding on a
                circle of radius 1e-3 around it is its multiplicity; C4-newton likewise;
  BREAK-C3-plant  multiplying F by (s - s_1) with a planted s_1 inside the rectangle raises
                the winding count by exactly one (the counting can fail);
  C3-wide, C4-wide  (informational, no PASS criterion beyond self-consistency) the first
                zeros above the strip, located by the 2D route on |Im s| <= 40, and the
                winding/count agreement there.

What is not verified
--------------------
R48 (the (s,t,u) reduction) and R50 (the boundary representation at real exponents) are
inputs.  Nothing here concerns the level-0 operator K_P: the frozen block is the scalar
F(s,0,0) (record 051 C5 states what the model does and does not say).

Group ``c6a`` (record 051 section 18c.6a, Blocks 8-10): tabulation of F(s,t,u) on the
Nystrom node triples of the beta = 2 design over the region Re s in [-40, 20],
|Im s| <= 40.  The plan's real-interval Chebyshev interpolant is unsound there (its
continuation amplifies rounding by r^N ~ 3.45^72; BREAK-C6-real-cheb measures 8e24).
Adopted: per tile type X (three s-dependences, record 051 (8.1)), the centred Laplace
transform h_X = exp(-c_X s) J_X(s) is expanded in Chebyshev polynomials of
x = (s - s_c)/(i h) from samples on the Bernstein ellipse |w| = r (Joukowski
x = (w + 1/w)/2) of each of three real panels [-40,-20], [-20,0], [0,20], semi-axes
(A, B) = (19, 48), N_ELL = 104 samples (degree 52), 53 evaluations per panel with
Im s >= 0 (entrywise reflection F(conj s) = conj F(s)).  Complex-s evaluations use the
smooth 2D rule ``j_2d_s`` (``_rule_2d_smooth``: y = sin(psi) below the unit circle's
top, spectral; the c5 rule ``j_2d_c`` converges only as n^-1 at the design exponents).

Checks of group c6a (named after node C6):
  C6-2d-real      smooth 2D rule (n = 60) against ``j_vec`` at real s on the triples;
  C6-2d-conv      n = 60 against n = 90 at |Im s| ~ 40;
  C6-2d-bnd       against ``j_vec_c`` at Im s = 4 (where the boundary route is accurate);
  C6-coef-real    a_k i^-k real (the reflection symmetry) to 1e-12;
  C6-tail         last three |a_k| r^k below 1e-10 of the largest (truncation resolved);
  C6-interp-entry per-entry relative error of the interpolant against the direct
                  evaluation at 14 seeded points of the region, < 1e-8;
  C6-interp-bound the same relative to the bound F(Re s, t, u) (record 051 C2);
  C6-interp-eig   four leading eigenvalues of M^(0), M^(2), relative to |mu_0|, < 1e-8;
  C6-interp-eig-own  own-relative eigenvalue errors explained by the absolute matrix
                  error (|mu_3/mu_0| falls to 3e-7 at large |Im s|);
  C6-overlap      two panels agree at a point of their overlap;
  BREAK-C6-degree every second / fourth node (degree 26 / 13) must fail 1e-8;
  BREAK-C6-real-cheb  the plan's real-interval scheme at Im s = 40 must fail.

Group ``c6b`` (record 051 section 18c.6b, Block 11): the full (56,8,24) tabulation is
re-validated (C6-tail, the anchors of record 050 (2.1)/(3.4)); the eigenvalue branches
mu_{n,j}(s) of the complex-symmetric Nystrom matrices are followed by eigenvector overlap
with adaptive steps (``carry``), their winding read on rectangles (``branch_winding``,
with the closure overlap as the monodromy test), zeros refined by Newton with the
Hellmann-Feynman derivative mu' = v^T M' v / v^T v from the analytic s-derivative of the
tabulation (``tab_eval_d``).  Checks (named after node C7):
  C7.1-tail, C7.1-anchor-n0, C7.1-anchor-n2   the tabulation against Block 9 and 050;
  C7.2-reflect, C7.2-deriv, C7.2-HF           reflection, derivative, Hellmann-Feynman;
  C7.3-left[n]      no zero of mu_{n,j}, j <= 3, on [-40,-20] x [0,40]i (windings 0,
                    loops closing) for n = 0, 2;
  C7.3-newton-none  Newton from the 8 leading anchor branches at the cells where the
                    set winding of the exploration read +1 converges nowhere in S;
  BREAK-C7-plant-wind, BREAK-C7-plant-newton  a planted zero mu -> mu (s - s1) winds
                    once and is found by Newton;
  BREAK-C7-order    value-order labelling switches branches on the column Re s = 3.
What is NOT verified here: a complete census of the zeros on Re s in [-20, 20] (record
051 (11.3): the exceptional points are dense there and the single-branch winding is not
defined through them); beta = 3/2.

Run: ``.venv/bin/python codes/verify-kp-complex-s.py [--only c5|c6a|c6b] [--design 16,8,24]``
Full tabulation (record 051 (10.2)):
  ``--only tab --design 56,8,24 --workers 6 --out output/kp-tab-beta2-56-8-24.npz``
Block 13 of record 051 (the zero s** under n2d = 60 -> 90 and Lambda = 8 -> 10, from cached DD
matrices ``output/c6j-M-*.npy``): ``--only c6j`` (docstring of ``group_c6j``).
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import multiprocessing
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
from mpmath import hyp2f1, mp, mpc, mpf, quad
from numpy.polynomial import chebyshev as C

_CODES_DIR = Path(__file__).resolve().parent
SEED = 20260923
ALPHA_P = 1.0

mp.dps = 30


def _load_module(name: str, filename: str):  # noqa: ANN202
    """Import a hyphenated module file (never modified here)."""
    spec = importlib.util.spec_from_file_location(name, _CODES_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


jcf = _load_module("verify_j_closed_form", "verify-j-closed-form.py")
kpk = _load_module("verify_kp_kernel", "verify-kp-kernel.py")
kpr = _load_module("verify_kp_real_s", "verify-kp-real-s.py")

_RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    _RESULTS.append((name, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


# ---------------------------------------------------------------------------------------
# Evaluators of J at complex exponents
# ---------------------------------------------------------------------------------------
def j_vec_c(p: np.ndarray, q: np.ndarray, beta: float, deg: int = 300) -> np.ndarray:
    """
    J(p_k, q_k) for complex arrays p, q by the continued boundary representation.

    J = (1/2i) oint G^* dG with G^*(Z) = conj(G(Z; conj p, conj q)) (record 051 A6);
    same arcs, branches and cumulative Chebyshev scheme as ``j_vec`` of
    verify-kp-kernel.py (whose ``_rule`` and ``_arc_data`` caches are reused).
    """
    p = np.asarray(p, dtype=complex)
    q = np.asarray(q, dtype=complex)
    xcheb, gl_x, gl_w, V_gl, V_one, Vc = kpk._rule(deg)  # noqa: SLF001
    total = np.zeros(p.shape, dtype=complex)
    G0 = np.zeros(p.shape, dtype=complex)
    G0s = np.zeros(p.shape, dtype=complex)
    for la, lw, th0, th1, dz in kpk._arc_data(beta, deg):  # noqa: SLF001
        # f = exp[p/2 (ln|Z| + i th0) + q/2 (ln|1-Z| + i th1)]; f^* with -i (Z-conjugated,
        # exponents untouched); dz^* = conj(dz)
        lp = 0.5 * (p[None, :] * la[:, None] + q[None, :] * lw[:, None])
        ph = 0.5j * (p[None, :] * th0[:, None] + q[None, :] * th1[:, None])
        h = np.exp(lp + ph) * dz[:, None]
        hs_ = np.exp(lp - ph) * np.conj(dz)[:, None]
        coef = Vc.T @ h
        coef[0] /= deg + 1
        coef[1:] /= 0.5 * (deg + 1)
        coefs = Vc.T @ hs_
        coefs[0] /= deg + 1
        coefs[1:] /= 0.5 * (deg + 1)
        cum = C.chebint(coef, lbnd=-1.0)
        cums = C.chebint(coefs, lbnd=-1.0)
        Gs_star = G0s[None, :] + V_gl @ cums
        hvals = V_gl[:, : deg + 1] @ coef
        total += np.sum(gl_w[:, None] * Gs_star * hvals, axis=0)
        G0 = G0 + V_one @ cum
        G0s = G0s + V_one @ cums
    return total / (2j)


_RULE2D: dict[tuple[float, int], tuple] = {}


def _rule_2d(beta: float, n: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the cached nodes (ln|Z|, ln|1-Z|) and weights of the 2D rule on R."""
    key = (beta, n)
    if key in _RULE2D:
        return _RULE2D[key]
    a, b = jcf.axes(beta)
    breaks = (0.0, math.asin(math.sqrt(3) / (2 * b)), math.asin(1.0 / b), math.pi / 2)
    gt, wt = np.polynomial.legendre.leggauss(n)
    gx, wx = np.polynomial.legendre.leggauss(n)
    lz_all, lo_all, w_all = [], [], []
    for k in range(3):
        t0, t1 = breaks[k], breaks[k + 1]
        th = 0.5 * (t1 - t0) * gt + 0.5 * (t1 + t0)
        wth = 0.5 * (t1 - t0) * wt
        for t, w in zip(th, wth, strict=True):
            y = b * math.sin(t)
            jac = b * math.cos(t)
            x_left = 0.5 - a * math.cos(t)
            segs = []
            if y < 1.0:
                r = math.sqrt(max(0.0, 1.0 - y * y))
                segs.append((x_left, -r))
                if r <= 0.5:
                    segs.append((r, 0.5))
            else:
                segs.append((x_left, 0.5))
            for x0, x1 in segs:
                if x1 <= x0:
                    continue
                xs = 0.5 * (x1 - x0) * gx + 0.5 * (x1 + x0)
                wxs = 0.5 * (x1 - x0) * wx
                lz_all.append(0.5 * np.log(xs * xs + y * y))
                lo_all.append(0.5 * np.log((1.0 - xs) ** 2 + y * y))
                w_all.append(w * jac * wxs)
    out = (np.concatenate(lz_all), np.concatenate(lo_all), np.concatenate(w_all))
    _RULE2D[key] = out
    return out


def j_2d_c(p: np.ndarray, q: np.ndarray, beta: float, n: int = 120) -> np.ndarray:
    """J(p,q) at complex exponents by the defining 2D integral (nested Gauss-Legendre)."""
    p = np.asarray(p, dtype=complex)
    q = np.asarray(q, dtype=complex)
    lz, lo, w = _rule_2d(beta, n)
    return np.exp(p[:, None] * lz[None, :] + q[:, None] * lo[None, :]) @ w


def _inc_beta_c(z: mpc, p: complex, q: complex) -> mpc:
    """Incomplete Beta B_Z(p/2+1, q/2+1) with complex exponents, R50's branches."""
    z = mpc(z)
    alpha = mpc(p) / 2 + 1
    gam = mpc(q) / 2 + 1
    th0 = mp.arg(z) if z.imag != 0 or z.real >= 0 else mp.pi
    zalpha = mp.exp(alpha * (mp.log(abs(z)) + 1j * th0))
    return zalpha / alpha * hyp2f1(alpha, 1 - gam, alpha + 1, z)


def _f_c(z: mpc, p: complex, q: complex) -> mpc:
    z = mpc(z)
    th0 = mp.arg(z) if z.imag != 0 or z.real >= 0 else mp.pi
    if th0 < 0:
        th0 = mpf(0)
    w = 1 - z
    th1 = mp.arg(w)
    if th1 > 0:
        th1 = mpf(0)
    return mp.exp(
        mpc(p) / 2 * (mp.log(abs(z)) + 1j * th0)
        + mpc(q) / 2 * (mp.log(abs(w)) + 1j * th1)
    )


def j_hyp_c(p: complex, q: complex, beta: float) -> complex:
    """J at complex exponents by the continued mpmath 2F1 boundary route."""
    pb, qb = complex(p).conjugate(), complex(q).conjugate()

    def G_star(z: mpc) -> mpc:
        g = _inc_beta_c(z, pb, qb) - _inc_beta_c(mpc(-1, 0), pb, qb)
        return mp.conj(g)

    total = mpc(0)
    for _name, zf, dzf, t0, t1 in jcf.arcs(beta):

        def integrand(t, zf=zf, dzf=dzf):  # noqa: ANN001, ANN202
            z = mpc(zf(float(t)))
            return _f_c(z, p, q) * G_star(z) * mpc(dzf(float(t)))

        total += quad(integrand, [t0, t1])
    return complex(total / (2j))


# ---------------------------------------------------------------------------------------
# The frozen-momentum contact term
# ---------------------------------------------------------------------------------------
def G_frozen(s: np.ndarray, beta: float, route: str = "boundary") -> np.ndarray:
    """G(s) = J(s/4,-s/4) + J(-s/4,s/4) + J(-s/4,-s/4) (alpha' = 1), complex s allowed."""
    s = np.atleast_1d(np.asarray(s, dtype=complex))
    p = ALPHA_P * s / 4
    P = np.concatenate([p, -p, -p])
    Q = np.concatenate([-p, p, -p])
    if route == "boundary":
        J = j_vec_c(P, Q, beta)
    elif route == "2d":
        J = j_2d_c(P, Q, beta)
    else:
        raise ValueError(route)
    return J.reshape(3, -1).sum(axis=0)


def F_frozen(s: np.ndarray, beta: float, route: str = "boundary") -> np.ndarray:
    """F(s,0,0) = 4 beta^{8 - alpha' s/2} G(s)."""
    s = np.atleast_1d(np.asarray(s, dtype=complex))
    return (
        4.0
        * np.exp((8.0 - ALPHA_P * s / 2.0) * math.log(beta))
        * G_frozen(s, beta, route)
    )


# ---------------------------------------------------------------------------------------
# Argument principle, subdivision, Newton
# ---------------------------------------------------------------------------------------
def winding(fun, x0: float, x1: float, y0: float, y1: float, n: int = 400) -> int:  # noqa: ANN001
    """
    Winding number of ``fun`` around the rectangle [x0,x1] x [y0,y1]i.

    The boundary is sampled with n points per edge, doubled until every phase step is
    below pi/2 (so the unwrapping is unambiguous); the count is round(sum of steps / 2 pi).
    """
    while True:
        tt = np.linspace(0.0, 1.0, n, endpoint=False)
        pts = np.concatenate(
            [
                x0 + (x1 - x0) * tt + 1j * y0,
                x1 + 1j * (y0 + (y1 - y0) * tt),
                x1 - (x1 - x0) * tt + 1j * y1,
                x0 + 1j * (y1 - (y1 - y0) * tt),
            ]
        )
        vals = fun(pts)
        if np.any(vals == 0):
            raise ZeroDivisionError("zero on the contour")
        steps = np.angle(np.roll(vals, -1) / vals)
        if np.max(np.abs(steps)) < 0.5 * math.pi or n >= 25600:
            break
        n *= 2
    return int(round(float(np.sum(steps)) / (2 * math.pi)))


def locate_zeros(fun, x0, x1, y0, y1, min_size=0.05):  # noqa: ANN001, ANN201
    """Quadtree subdivision on the winding number down to ``min_size`` cells; list of (centre, count)."""
    out = []
    stack = [(x0, x1, y0, y1, winding(fun, x0, x1, y0, y1))]
    while stack:
        a, b, c, d, w = stack.pop()
        if w == 0:
            continue
        if (b - a) < min_size and (d - c) < min_size:
            out.append((complex(0.5 * (a + b), 0.5 * (c + d)), w))
            continue
        xm, ym = 0.5 * (a + b), 0.5 * (c + d)
        # shift the split lines slightly off symmetric positions (the real axis is a zero
        # line of Im F, not of F, so no zero sits on it unless G has a real zero)
        cells = [(a, xm, c, ym), (xm, b, c, ym), (a, xm, ym, d), (xm, b, ym, d)]
        ws = [winding(fun, *cell) for cell in cells]
        if sum(ws) != w:
            raise RuntimeError(f"winding not additive on {(a, b, c, d)}: {w} vs {ws}")
        stack.extend([(*cell, wc) for cell, wc in zip(cells, ws, strict=True)])
    return out


def newton(fun, z: complex, iters: int = 60, h: float = 1e-6) -> complex:  # noqa: ANN001
    """Newton refinement with a central-difference derivative (fun is vectorised)."""
    for _ in range(iters):
        v = fun(np.array([z, z + h, z - h]))
        d = (v[1] - v[2]) / (2 * h)
        step = v[0] / d
        z = z - step
        if abs(step) < 1e-14 * max(1.0, abs(z)):
            break
    return z


def scan(
    beta: float, x0: float, x1: float, y0: float, y1: float, route: str = "boundary"
):  # noqa: ANN201
    """Return (winding of the rectangle, list of (zero, multiplicity, |F| at zero))."""

    def fun(z: np.ndarray) -> np.ndarray:
        return F_frozen(z, beta, route)

    w_total = winding(fun, x0, x1, y0, y1)
    cells = locate_zeros(fun, x0, x1, y0, y1)
    zeros = []
    for centre, count in cells:
        z = newton(fun, centre)
        r = 1e-3
        mult = winding(fun, z.real - r, z.real + r, z.imag - r, z.imag + r, n=200)
        zeros.append((z, mult, abs(complex(fun(np.array([z]))[0])), count))
    return w_total, zeros


def lattice_distance(z: complex) -> tuple[float, float]:
    """Distance of alpha' s = z to the plumbing lattice {4, 0, -4, -8, ...} (nearest point, distance)."""
    n = max(0, round((4.0 - z.real) / 4.0))
    pt = 4.0 - 4.0 * n
    return pt, abs(z - pt)


# ---------------------------------------------------------------------------------------
def group_c5(rng: np.random.Generator) -> None:  # noqa: PLR0915
    """Record 051 section 18c.5: C1–C4 and the break leg."""
    x0, x1, y0, y1 = -40.0, 20.0, -10.0, 10.0

    # --- C1: reduction to three J's against the six-tile contact_F of R50 -------------
    s_real = np.concatenate([[0.0, 4.0, 16.0 / 3.0, -10.0], rng.uniform(-40, 20, 3)])
    ok1, worst1 = True, 0.0
    for beta in (1.5, 2.0):
        mine = F_frozen(s_real, beta).real
        ref = np.array(
            [
                jcf.contact_F(
                    float(s),
                    0.0,
                    0.0,
                    beta,
                    lambda p, q, b: jcf.J_boundary_cheb(p, q, b)[0],
                )
                for s in s_real
            ]
        )
        err = float(np.max(np.abs(mine - ref) / np.abs(ref)))
        worst1 = max(worst1, err)
        ok1 = ok1 and err < 1e-10
    f000 = float(F_frozen(np.array([0.0]), 1.5)[0].real)
    anchor = 833.995861147076
    ok1 = ok1 and abs(f000 - anchor) < 1e-9 * anchor
    check(
        "C1",
        ok1,
        f"max rel vs contact_F {worst1:.2e}; F(0,0,0) = {f000:.9f} vs {anchor}",
    )

    # --- C2: complex-exponent evaluator ------------------------------------------------
    pq = np.array([[3.7, -5.2], [30.0, -70.0], [-40.0, 90.0], [120.0, -250.0]])
    pq = np.vstack([pq, rng.uniform(-60, 60, size=(3, 2))])
    err = 0.0
    for beta in (1.5, 2.0):
        mine = j_vec_c(pq[:, 0], pq[:, 1], beta)
        ref = kpk.j_vec(pq[:, 0], pq[:, 1], beta)
        err = max(err, float(np.max(np.abs(mine - ref) / np.abs(ref))))
    check("C2-real", err < 1e-11, f"complex path at real exponents vs j_vec: {err:.2e}")

    # complex exponents of the tiles of G on the strip: p = s/4, |Im p| <= 2.5
    sc = rng.uniform(-40, 20, 6) + 1j * rng.uniform(-10, 10, 6)
    sc = np.concatenate([sc, [5.0 + 10.0j, -30.0 - 10.0j]])
    pc = sc / 4
    P = np.concatenate([pc, -pc, -pc])
    Q = np.concatenate([-pc, pc, -pc])
    err2d, errcond = 0.0, 0.0
    for beta in (1.5, 2.0):
        mine = j_vec_c(P, Q, beta)
        ref = j_2d_c(P, Q, beta, n=120)
        ref2 = j_2d_c(P, Q, beta, n=240)
        conv = float(np.max(np.abs(ref - ref2) / np.abs(ref2)))
        e = np.abs(mine - ref2) / np.abs(ref2)
        err2d = max(err2d, float(np.max(e[np.abs(np.imag(P)) < 2.0])))
        errcond = max(errcond, float(np.max(e)))
        print(
            f"    beta={beta}: 2D rule n=120 vs 240: {conv:.1e}; boundary vs 2D: {np.max(e):.1e}"
        )
    check(
        "C2-2d", err2d < 1e-7, f"boundary vs 2D quadrature at |Im s| < 8: {err2d:.2e}"
    )
    check(
        "C2-cond",
        errcond < 1e-6,
        f"including |Im s| = 10 (digit loss ~ exp(pi |Im s|/2) ~ 7 digits): {errcond:.2e}",
    )
    errh = 0.0
    # generic (p, q): at p + q = -2 (a - b integer in the 2F1) mpmath's transformation for
    # |Z| > 1 hits its perturbation branch, which does not accept complex parameters; the
    # tiles with p = -q are covered against the 2D route (C2-2d) instead
    for p, q in [
        (1.3 + 2.1j, -0.9 - 1.7j),
        (-7.0 - 1.5j, 6.3 + 2.2j),
        (-2.5 + 2.5j, -2.5 + 2.5j),
    ]:
        mine = complex(j_vec_c(np.array([p]), np.array([q]), 1.5)[0])
        ref = j_hyp_c(p, q, 1.5)
        errh = max(errh, abs(mine - ref) / abs(ref))
    check(
        "C2-hyp",
        errh < 1e-9,
        f"vs continued mpmath 2F1 route at 3 complex pairs: {errh:.2e}",
    )

    # growth bound |J(p,q)| <= J(Re p, Re q), sharp: ratio < 1 off the real axis
    ratio = np.abs(j_2d_c(P, Q, 1.5)) / j_2d_c(P.real + 0j, Q.real + 0j, 1.5).real
    check(
        "C2-growth",
        bool(np.all(ratio <= 1.0 + 1e-12))
        and bool(np.all(ratio[np.abs(P.imag) > 0.5] < 0.999)),
        f"max ratio {np.max(ratio):.4f}, min {np.min(ratio):.2e} (049 (1.5)'s exp(pi|Im s|/2) is not needed for J)",
    )

    # --- C3 / C4: the scan -----------------------------------------------------------
    for label, beta in (("C3", 1.5), ("C4", 2.0)):
        t0 = time.time()
        xs = np.linspace(x0, x1, 1201)
        g = G_frozen(xs, beta).real
        check(
            f"{label}-real",
            bool(np.all(g > 0)),
            f"min G on [-40,20] = {np.min(g):.4e} at s = {xs[np.argmin(g)]:.2f}; no real zero",
        )
        w_total, zeros = scan(beta, x0, x1, y0, y1)
        n_found = sum(m for _, m, _, _ in zeros)
        check(
            f"{label}-wind",
            w_total == n_found,
            f"beta={beta}: winding of [-40,20]x[-10,10]i = {w_total}, zeros found (with mult.) = {n_found}",
        )
        typical = float(np.median(np.abs(F_frozen(xs, beta))))
        okn = all(m >= 1 and fz < 1e-9 * typical for _, m, fz, _ in zeros)
        check(
            f"{label}-newton",
            okn or not zeros,
            f"{len(zeros)} zero(s), residuals below 1e-9 median|F|",
        )
        print(
            f"    zero table beta={beta} (alpha' s, multiplicity, |F|, nearest lattice pt, dist):"
        )
        for z, m, fz, _ in sorted(zeros, key=lambda t: (t[0].real, t[0].imag)):
            pt, dist = lattice_distance(z)
            print(
                f"      {z.real:+.10f} {z.imag:+.10f}i   m={m}  |F|={fz:.1e}  lattice {pt:+.0f}  dist {dist:.4f}"
            )
        print(f"    ({time.time() - t0:.0f} s)")

        # informational: the first zeros above the strip (2D route: no digit loss)
        t0 = time.time()
        w_wide, zeros_wide = scan(beta, x0, x1, 10.0, 40.0, route="2d")
        n_wide = sum(m for _, m, _, _ in zeros_wide)
        check(
            f"{label}-wide",
            w_wide == n_wide,
            f"beta={beta}: winding of [-40,20]x[10,40]i = {w_wide}, zeros found = {n_wide} (2D route; conjugates below)",
        )
        for z, m, fz, _ in sorted(zeros_wide, key=lambda t: (t[0].imag, t[0].real)):
            pt, dist = lattice_distance(z)
            print(
                f"      {z.real:+.6f} {z.imag:+.6f}i   m={m}  |F|/typ={fz / typical:.1e}  nearest lattice {pt:+.0f}"
            )
        print(f"    ({time.time() - t0:.0f} s)")

    # --- BREAK-C3-plant: a planted zero must raise the count by one ----------------------
    s1 = complex(rng.uniform(-35, 15), rng.uniform(-8, 8))

    def fun_plant(z: np.ndarray) -> np.ndarray:
        return F_frozen(z, 1.5) * (z - s1)

    def fun_plain(z: np.ndarray) -> np.ndarray:
        return F_frozen(z, 1.5)

    w_plain = winding(fun_plain, x0, x1, y0, y1)
    w_plant = winding(fun_plant, x0, x1, y0, y1)
    check(
        "BREAK-C3-plant",
        w_plant == w_plain + 1,
        f"planted zero at {s1:.3f}: winding {w_plain} -> {w_plant} (must increase by one)",
    )


# ---------------------------------------------------------------------------------------
# Group c6a: tabulation of F in complex s on the Nystrom nodes (record 051 Blocks 8-10)
# ---------------------------------------------------------------------------------------
# The 2D rule of ``_rule_2d`` parametrises y = b sin(theta) and meets the unit circle
# (x = -sqrt(1 - y^2)) with a square-root endpoint singularity at y = 1: it converges only
# as n^{-1} (2e-7 at n = 120 at the design exponents).  ``_rule_2d_smooth`` parametrises
# y = sin(psi) on y <= 1 (the circle abscissa is cos(psi), smooth) and y = b sin(theta)
# above: spectral convergence, 6e-13 at n = 60 against ``j_vec`` (check C6-2d-real).
_RULE2DS: dict[tuple[float, int], tuple] = {}


def _rule_2d_smooth(beta: float, n: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Nodes (ln|Z|, ln|1-Z|) and weights of the smooth-parametrised 2D rule on R."""
    key = (beta, n)
    if key in _RULE2DS:
        return _RULE2DS[key]
    a, b = jcf.axes(beta)
    gt, wt = np.polynomial.legendre.leggauss(n)
    gx, wx = np.polynomial.legendre.leggauss(n)
    panels = (
        ("psi", 0.0, math.pi / 3),  # y in [0, sqrt3/2]: one segment (x_left, -cos psi)
        ("psi", math.pi / 3, math.pi / 2),  # y in [sqrt3/2, 1]: plus (cos psi, 1/2)
        ("th", math.asin(1.0 / b), math.pi / 2),  # y in [1, b]: (x_left, 1/2)
    )
    lz_all, lo_all, w_all = [], [], []
    for kind, t0, t1 in panels:
        tt = 0.5 * (t1 - t0) * gt + 0.5 * (t1 + t0)
        wtt = 0.5 * (t1 - t0) * wt
        for t, w in zip(tt, wtt, strict=True):
            if kind == "psi":
                y, jac, r = math.sin(t), math.cos(t), math.cos(t)
                x_left = 0.5 - a * math.sqrt(1.0 - (y / b) ** 2)
                segs = [(x_left, -r)]
                if r <= 0.5:
                    segs.append((r, 0.5))
            else:
                y, jac = b * math.sin(t), b * math.cos(t)
                segs = [(0.5 - a * math.cos(t), 0.5)]
            for x0, x1 in segs:
                if x1 <= x0:
                    continue
                xs = 0.5 * (x1 - x0) * gx + 0.5 * (x1 + x0)
                wxs = 0.5 * (x1 - x0) * wx
                lz_all.append(0.5 * np.log(xs * xs + y * y))
                lo_all.append(0.5 * np.log((1.0 - xs) ** 2 + y * y))
                w_all.append(w * jac * wxs)
    out = (np.concatenate(lz_all), np.concatenate(lo_all), np.concatenate(w_all))
    _RULE2DS[key] = out
    return out


def j_2d_s(p: np.ndarray, q: np.ndarray, beta: float, n: int = 60) -> np.ndarray:
    """J(p,q) at complex exponents by the smooth 2D rule (chunked; ~0.3 ms per J)."""
    p = np.asarray(p, dtype=complex)
    q = np.asarray(q, dtype=complex)
    lz, lo, w = _rule_2d_smooth(beta, n)
    out = np.empty(p.shape, dtype=complex)
    chunk = 512
    for a in range(0, p.size, chunk):
        sl = slice(a, a + chunk)
        out[sl] = np.exp(p[sl, None] * lz[None, :] + q[sl, None] * lo[None, :]) @ w
    return out


# Tile types by s-dependence (record 051 (8.1)): I = (s,t,u),(s,u,t); II = (t,s,u),(u,s,t);
# III = (t,u,s),(u,t,s).  Exponent pairs (p,q) = ((x-y-z)/4, (y-x-z)/4), alpha' = 1.
def type_sums(
    s: complex, t: np.ndarray, u: np.ndarray, beta: float, route: str, n2d: int = 60
) -> np.ndarray:
    """
    The three type sums J_X(s) = sum of the two tiles of type X, shape (3, n_entries).

    ``route``: "2d" (smooth 2D rule, complex s) or "boundary" (``j_vec``, real s only).
    """
    t = np.asarray(t, dtype=float)
    u = np.asarray(u, dtype=float)
    ss = s * np.ones_like(t, dtype=complex)
    tiles = {
        0: [(ss, t, u), (ss, u, t)],
        1: [(t, ss, u), (u, ss, t)],
        2: [(t, u, ss), (u, t, ss)],
    }
    P, Q = [], []
    for k in range(3):
        for x, y, z in tiles[k]:
            P.append(ALPHA_P * (x - y - z) / 4)
            Q.append(ALPHA_P * (y - x - z) / 4)
    P = np.concatenate(P)
    Q = np.concatenate(Q)
    if route == "2d":
        J = j_2d_s(P, Q, beta, n2d)
    elif route == "boundary":
        if abs(complex(s).imag) > 0:
            raise ValueError("boundary route: real s only in this group")
        J = kpk.j_vec(P.real, Q.real, beta).astype(complex)
    else:
        raise ValueError(route)
    return J.reshape(6, -1).reshape(3, 2, -1).sum(axis=1)


def type_centres(beta: float) -> np.ndarray:
    """Centring exponents c_X of (8.2): the midpoints of the ranges (8.1)."""
    a, _b = jcf.axes(beta)
    return np.array([-math.log(2) / 8, math.log(2) / 8, -math.log(a * a - 0.25) / 8])


def f_from_types(s: complex, t: np.ndarray, u: np.ndarray, beta: float, JX: np.ndarray):
    """F(s,t,u) = 2 beta^{8 - (s+t+u)/2} sum_X J_X (A3), from the type sums."""
    return 2.0 * np.exp((8.0 - ALPHA_P * (s + t + u) / 2.0) * math.log(beta)) * JX.sum(0)


def design_nodes(n_r: int, lam: float, n_th: int) -> dict:
    """Nystrom node triples (i <= j, x_k > 0) of a design, as in ``_kn_job`` of 18c.3."""
    xg, wg = np.polynomial.legendre.leggauss(n_r)
    rho = 0.5 * lam * (xg + 1.0)
    wr = 0.5 * lam * wg
    x, w = kpk.angular_rule(n_th)
    pos = x > 0
    xp, wp = x[pos], 2.0 * w[pos]
    iu, ju = np.triu_indices(n_r)
    r2 = rho[iu] ** 2 + rho[ju] ** 2
    rl = rho[iu] * rho[ju]
    t = r2[:, None] + 2 * rl[:, None] * xp[None, :]
    u = r2[:, None] - 2 * rl[:, None] * xp[None, :]
    return {
        "n_r": n_r, "lam": lam, "n_th": n_th, "rho": rho, "wr": wr, "xp": xp, "wp": wp,
        "iu": iu, "ju": ju, "t": t.ravel(), "u": u.ravel(), "shape": t.shape,
    }


# Panels and ellipses (record 051 (8.3)): real intervals [-40,-20], [-20,0], [0,20];
# s = s_c + i h x, x = (w + 1/w)/2, |w| = r; real semi-axis A = h (r - 1/r)/2, imaginary
# semi-axis B = h (r + 1/r)/2.
PANEL_CENTRES = (-30.0, -10.0, 10.0)
PANEL_HALF = 10.0
ELL_A, ELL_B = 19.0, 48.0
N_ELL = 104  # nodes per ellipse; Chebyshev degree N_ELL/2 = 52 (record 051 (8.3))


def ellipse_params(A: float = ELL_A, B: float = ELL_B) -> tuple[float, float]:
    """(h, r) of the Joukowski image with semi-axes A (real) and B (imaginary)."""
    r = math.sqrt((B + A) / (B - A))
    h = 2.0 * B / (r + 1.0 / r)
    return h, r


def ellipse_nodes(s_c: float, n: int, A: float = ELL_A, B: float = ELL_B) -> np.ndarray:
    """The n nodes s_j = s_c + i h x(r e^{i phi_j}), phi_j = 2 pi j / n."""
    h, r = ellipse_params(A, B)
    phi = 2.0 * np.pi * np.arange(n) / n
    w = r * np.exp(1j * phi)
    return s_c + 1j * h * 0.5 * (w + 1.0 / w)


def cheb_from_ellipse(samples: np.ndarray, r: float) -> np.ndarray:
    """
    Chebyshev coefficients a_k (k = 0..n/2) of g(x) from samples on the ellipse |w| = r.

    samples[j] = g(x(r e^{i phi_j})), phi_j = 2 pi j / n, along axis 0.  FFT: c_m =
    (1/n) sum_j g_j e^{-i m phi_j} = b_m r^m + (alias), a_m = 2 c_m r^{-m} (m >= 1),
    a_0 = c_0.  The coefficients are real when g(conj x) = conj g(x); the imaginary parts
    are returned to the caller as the check C6-coef-real.

    Symmetry: s -> conj(s) is x -> -conj(x) (s = s_c + i h x), so g(-conj x) = conj g(x)
    and a_k is real for even k, imaginary for odd k: a_k i^{-k} is real (C6-coef-real).
    """
    n = samples.shape[0]
    c = np.fft.fft(samples, axis=0) / n
    m = np.arange(n // 2 + 1)
    a = c[: n // 2 + 1] * (2.0 * r ** (-m.astype(float)))[(slice(None),) + (None,) * (samples.ndim - 1)]
    a[0] /= 2.0
    a[n // 2] = c[n // 2] * 2.0 / (r ** (n / 2) + r ** (-n / 2))  # both aliases
    return a


def cheb_eval_complex(a: np.ndarray, x: complex) -> np.ndarray:
    """sum_k a_k T_k(x) at complex x, T_k = (w^k + w^-k)/2 with w = x + sqrt(x^2-1), |w| >= 1."""
    w = x + np.sqrt(x * x - 1.0)
    if abs(w) < 1.0:
        w = 1.0 / w
    k = np.arange(a.shape[0])
    T = 0.5 * (w**k + w ** (-k.astype(float)))
    return np.tensordot(T, a, axes=([0], [0]))


def _ellipse_job(args: tuple) -> tuple:
    """One node: the three type sums on all node triples (2D route, or boundary if real)."""
    j, s, t, u, beta, n2d = args
    t0 = time.time()
    if abs(s.imag) < 1e-12:
        JX = type_sums(s.real, t, u, beta, "boundary")
    else:
        JX = type_sums(s, t, u, beta, "2d", n2d)
    return j, JX, time.time() - t0


def tabulate(
    nodes: dict, beta: float, n_ell: int = N_ELL, workers: int = 4, n2d: int = 60,
    log=print,  # noqa: ANN001
) -> dict:
    """
    Tabulate the centred type sums h_X on the three panel ellipses (record 051 (8.3)).

    Returns ``a[panel, type, k, entry]`` = a_k i^{-k} (real; the Chebyshev coefficient
    of h_X in x = (s - s_c)/(i h) is a_k = a[...,k,...] i^k), plus the raw samples.
    """
    t, u = nodes["t"], nodes["u"]
    cX = type_centres(beta)
    h, r = ellipse_params()
    a_all = np.zeros((3, 3, n_ell // 2 + 1, t.size))
    im_max = 0.0
    samples_all = []
    jobs = []
    for ip, s_c in enumerate(PANEL_CENTRES):
        s_nodes = ellipse_nodes(s_c, n_ell)
        for j in range(n_ell):
            if s_nodes[j].imag >= -1e-12:  # upper half incl. the two real nodes
                jobs.append((ip * n_ell + j, s_nodes[j], t, u, beta, n2d))
    log(f"tabulate: {len(jobs)} evaluations of F on {t.size} node triples, {workers} workers")
    results = {}
    t_start = time.time()
    ctx = multiprocessing.get_context("spawn")  # never fork a process with BLAS threads
    with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as ex:
        for j, JX, dt in ex.map(_ellipse_job, jobs, chunksize=1):
            results[j] = JX
            if len(results) % 10 == 0:
                log(f"  {len(results)}/{len(jobs)} done, last {dt:.1f} s, elapsed {time.time() - t_start:.0f} s", flush=True)
    for ip, s_c in enumerate(PANEL_CENTRES):
        s_nodes = ellipse_nodes(s_c, n_ell)
        samp = np.zeros((n_ell, 3, t.size), dtype=complex)
        for j in range(n_ell):
            if s_nodes[j].imag >= -1e-12:
                JX = results[ip * n_ell + j]
            else:  # conjugate node (n_ell/2 - j) mod n_ell, C2.1 entrywise
                JX = np.conj(results[ip * n_ell + (n_ell // 2 - j) % n_ell])
            samp[j] = np.exp(-cX[:, None] * s_nodes[j]) * JX
        a = cheb_from_ellipse(samp, r)  # (n/2+1, 3, n_entries)
        a = a * (1j ** (-np.arange(a.shape[0], dtype=float)))[:, None, None]  # real by symmetry
        scale = np.max(np.abs(a), axis=0)
        im_max = max(im_max, float(np.max(np.abs(a.imag) / scale)))
        a_all[ip] = np.transpose(a.real, (1, 0, 2))
        samples_all.append(samp)
    return {
        "a": a_all, "beta": beta, "cX": cX, "h": h, "r": r, "n_ell": n_ell,
        "centres": np.array(PANEL_CENTRES), "half": PANEL_HALF, "A": ELL_A, "B": ELL_B,
        "im_max": im_max, "samples": samples_all, "wall": time.time() - t_start,
    }


def tab_eval(tab: dict, nodes: dict, s: complex, panel: int | None = None, n_coef: int | None = None):
    """F(s,t,u) on all node triples from the tabulation (the matrix-free evaluation)."""
    if panel is None:
        panel = int(np.clip(np.searchsorted(tab["centres"] + tab["half"], s.real), 0, 2))
    x = (s - tab["centres"][panel]) / (1j * tab["h"])
    a = tab["a"][panel] if n_coef is None else tab["a"][panel][:, :n_coef]
    a = a * (1j ** np.arange(a.shape[1], dtype=float))[None, :, None]
    hX = np.stack([cheb_eval_complex(a[k], x) for k in range(3)])
    JX = np.exp(tab["cX"][:, None] * s) * hX
    return f_from_types(s, nodes["t"], nodes["u"], tab["beta"], JX)


def matrices_from_entries(fvals: np.ndarray, nodes: dict, n_list=(0, 2)) -> dict:
    """Symmetrised Nystrom matrices M^{(n)} (complex-symmetric) from the entries on the triples."""
    fv = fvals.reshape(nodes["shape"])
    P = kpr.gegen_norm(max(n_list), nodes["xp"])
    kn_tri = kpk.sphere_area(kpk.D - 2) * (fv @ (P * nodes["wp"][None, :]).T)
    dvec = np.sqrt(nodes["wr"] * nodes["rho"] ** (kpk.D - 1))
    n_r = nodes["n_r"]
    out = {}
    for n in n_list:
        k = np.zeros((n_r, n_r), dtype=complex)
        k[nodes["iu"], nodes["ju"]] = kn_tri[:, n]
        k[nodes["ju"], nodes["iu"]] = kn_tri[:, n]
        out[n] = dvec[:, None] * k * dvec[None, :]
    return out


def leading_eigs(M: np.ndarray, k: int = 4) -> np.ndarray:
    """The k eigenvalues of largest modulus of a complex-symmetric matrix (``eig``)."""
    ev = np.linalg.eigvals(M)
    return ev[np.argsort(-np.abs(ev))][:k]


def group_c6a(rng: np.random.Generator, design=(16, 8.0, 24), workers: int = 6) -> None:  # noqa: PLR0915
    """Validation of the tabulation on the reduced design (record 051 Block 9)."""
    beta = 2.0
    n_r, lam, n_th = design
    nodes = design_nodes(n_r, lam, n_th)
    t, u = nodes["t"], nodes["u"]
    print(f"group c6a: beta = {beta}, design {design}, {t.size} node triples, "
          f"panels {PANEL_CENTRES} +- {PANEL_HALF}, ellipse (A,B) = ({ELL_A},{ELL_B}), n_ell = {N_ELL}")
    h, r = ellipse_params()
    print(f"  Joukowski h = {h:.4f}, r = {r:.4f}; c_X = {type_centres(beta)}")

    # --- the 2D rule: against the boundary route at real s, and its own convergence
    for s_real in (-59.0, -10.0, 39.0):
        JX_b = type_sums(s_real, t, u, beta, "boundary")
        JX_2 = type_sums(s_real, t, u, beta, "2d", 60)
        err = np.max(np.abs(JX_2 - JX_b) / np.abs(JX_b))
        check(f"C6-2d-real[s={s_real:g}]", err < 1e-10, f"max rel {err:.2e} (n = 60 vs j_vec)")
    # --- test points: seeded, spread over the region incl. both real ends and Im near 40
    pts = []
    for _ in range(8):
        pts.append(complex(rng.uniform(-40, 20), rng.uniform(-40, 40)))
    pts += [complex(-40, 39.5), complex(20, -39.0), complex(-39.5, 0.7), complex(19.5, -2.0),
            complex(-1.7, 5.74), complex(-20.0, 25.0)]
    pts = np.array(pts)
    for s in (pts[np.argmax(np.abs(pts.imag))], complex(-39.0, -38.0)):
        JX_60 = type_sums(s, t, u, beta, "2d", 60)
        JX_90 = type_sums(s, t, u, beta, "2d", 90)
        scale = np.abs(type_sums(s.real, t, u, beta, "2d", 60))
        err = np.max(np.abs(JX_60 - JX_90) / scale)
        check(f"C6-2d-conv[s={s:.1f}]", err < 1e-11, f"n = 60 vs 90: {err:.2e} rel. to J_X(Re s)")
    s_low = complex(-3.0, 4.0)
    JX_2 = type_sums(s_low, t, u, beta, "2d", 60)
    P, Q = [], []
    ss = s_low * np.ones_like(t, dtype=complex)
    for x, y, z in [(ss, t, u), (ss, u, t), (t, ss, u), (u, ss, t), (t, u, ss), (u, t, ss)]:
        P.append((x - y - z) / 4)
        Q.append((y - x - z) / 4)
    JX_b = j_vec_c(np.concatenate(P), np.concatenate(Q), beta).reshape(3, 2, -1).sum(1)
    err = np.max(np.abs(JX_2 - JX_b) / np.abs(JX_b))
    check("C6-2d-bnd", err < 1e-9, f"smooth 2D vs j_vec_c at s = {s_low}: {err:.2e} (loss e^(pi Im s/2) = {math.exp(math.pi * 2):.0f})")

    # --- the tabulation
    tab = tabulate(nodes, beta, N_ELL, workers)
    print(f"  tabulation wall {tab['wall']:.0f} s")
    check("C6-coef-real", tab["im_max"] < 1e-12, f"max |Im a_k i^-k| / max_k |a_k| = {tab['im_max']:.2e}")
    a = tab["a"]
    tail = np.max(np.abs(a[:, :, -3:, :]) * r ** np.arange(a.shape[2] - 3, a.shape[2])[None, None, :, None]
                  / np.max(np.abs(a) * r ** np.arange(a.shape[2])[None, None, :, None], axis=2, keepdims=True))
    check("C6-tail", tail < 1e-10, f"last three |a_k| r^k relative to the largest: {tail:.2e}")

    # --- interpolation error per entry and on the eigenvalues at the test points
    worst_e, worst_b, worst_eig, worst_own, worst_floor, worst_ratio_own = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for s in pts:
        F_dir = f_from_types(s, t, u, beta, type_sums(s, t, u, beta, "2d", 60))
        F_tab = tab_eval(tab, nodes, s)
        F_bnd = f_from_types(s.real, t, u, beta, type_sums(s.real, t, u, beta, "2d", 60)).real
        e_ent = np.max(np.abs(F_tab - F_dir) / np.abs(F_dir))
        e_bnd = np.max(np.abs(F_tab - F_dir) / np.abs(F_bnd))
        M_dir = matrices_from_entries(F_dir, nodes)
        M_tab = matrices_from_entries(F_tab, nodes)
        # the evaluator's own floor: the direct matrix at n = 60 against n = 90 (2D rule)
        M_90 = matrices_from_entries(
            f_from_types(s, t, u, beta, type_sums(s, t, u, beta, "2d", 90)), nodes
        )
        e_eig, e_own, e_floor, ratio, e_expl = 0.0, 0.0, 0.0, 1.0, 0.0
        for n in (0, 2):
            ed, et, e9 = leading_eigs(M_dir[n]), leading_eigs(M_tab[n]), leading_eigs(M_90[n])
            e_eig = max(e_eig, float(np.max(np.abs(ed - et)) / np.abs(ed[0])))
            e_own = max(e_own, float(np.max(np.abs(ed - et) / np.abs(ed))))
            e_floor = max(e_floor, float(np.max(np.abs(ed - e9) / np.abs(ed))))
            ratio = min(ratio, float(np.abs(ed[3]) / np.abs(ed[0])))
            # own-relative error explained by the absolute error e_eig |mu_0| on each mu_j
            e_expl = max(e_expl, float(np.max(np.abs(ed - et)) / np.abs(ed[0]) / np.min(np.abs(ed) / np.abs(ed[0]))))
        print(f"    s = {s:+.3f}: entry rel {e_ent:.2e}, rel. to F(Re s) {e_bnd:.2e}; eig rel. to mu_0 "
              f"{e_eig:.2e}, own-rel {e_own:.2e} (evaluator floor n=60 vs 90: {e_floor:.2e}, "
              f"|mu_3/mu_0| = {ratio:.1e}); mu_0 = {leading_eigs(M_dir[0])[0]:.6e}")
        worst_e, worst_b = max(worst_e, e_ent), max(worst_b, e_bnd)
        worst_eig, worst_own, worst_floor = max(worst_eig, e_eig), max(worst_own, e_own), max(worst_floor, e_floor)
        worst_ratio_own = max(worst_ratio_own, e_own / e_expl) if e_expl > 0 else worst_ratio_own
    check("C6-interp-entry", worst_e < 1e-8, f"max over {len(pts)} points of the per-entry relative error: {worst_e:.2e}")
    check("C6-interp-bound", worst_b < 1e-8, f"relative to the bound F(Re s,t,u): {worst_b:.2e}")
    check("C6-interp-eig", worst_eig < 1e-8, f"four leading eigenvalues of M^(0), M^(2), relative to |mu_0|: {worst_eig:.2e}")
    check("C6-interp-eig-own", worst_ratio_own <= 1.0 and worst_own < 1e-5,
          f"each eigenvalue relative to itself: {worst_own:.2e} (|mu_3/mu_0| down to 1e-7 at large |Im s|), "
          f"at most {worst_ratio_own:.2f} x the absolute matrix error e_eig |mu_0| / |mu_j|; "
          f"the direct evaluator's own floor (n = 60 vs 90) is {worst_floor:.2e}")
    # --- overlap of the panels
    s_ov = complex(-20.0, 25.0)
    F1, F2 = tab_eval(tab, nodes, s_ov, panel=0), tab_eval(tab, nodes, s_ov, panel=1)
    err = np.max(np.abs(F1 - F2) / np.abs(F2))
    check("C6-overlap", err < 1e-8, f"panels 1 and 2 at s = {s_ov}: {err:.2e}")

    # --- break legs: too few nodes (every second / fourth node of the same ellipses)
    for sub in (2, 4):
        n_sub = N_ELL // sub
        a_sub = np.zeros((3, 3, n_sub // 2 + 1, t.size))
        for ip in range(3):
            samp = tab["samples"][ip][::sub]
            a_s = cheb_from_ellipse(samp, r)
            a_s = a_s * (1j ** (-np.arange(a_s.shape[0], dtype=float)))[:, None, None]
            a_sub[ip] = np.transpose(a_s.real, (1, 0, 2))
        tab_sub = dict(tab, a=a_sub, n_ell=n_sub)
        worst = 0.0
        for s in pts[-6:]:
            F_dir = f_from_types(s, t, u, beta, type_sums(s, t, u, beta, "2d", 60))
            F_sub = tab_eval(tab_sub, nodes, s)
            worst = max(worst, float(np.max(np.abs(F_sub - F_dir) / np.abs(F_dir))))
        check(f"BREAK-C6-degree[n_ell={n_sub}]", worst > 1e-8, f"per-entry error {worst:.2e} (must exceed 1e-8)")
    # --- the plan's scheme: real-interval Chebyshev on [-40,20], continued to Im s = 40
    n_cheb = 72
    xk = np.cos(np.pi * (np.arange(n_cheb) + 0.5) / n_cheb)
    s_k = -10.0 + 30.0 * xk
    cX = type_centres(beta)
    samp = np.array([np.exp(-cX[:, None] * sk) * type_sums(sk, t, u, beta, "boundary").real for sk in s_k])
    # direct DCT-based coefficients (Chebyshev points of the first kind)
    theta = np.pi * (np.arange(n_cheb) + 0.5) / n_cheb
    T = np.cos(np.outer(np.arange(n_cheb), theta))  # (k, j)
    coef = (2.0 / n_cheb) * np.tensordot(T, samp, axes=([1], [0]))
    coef[0] /= 2.0
    s_test = complex(-1.7, 40.0)
    x = (s_test + 10.0) / 30.0
    hX = np.stack([cheb_eval_complex(coef[:, k, :], x) for k in range(3)])
    F_real_cheb = f_from_types(s_test, t, u, beta, np.exp(cX[:, None] * s_test) * hX)
    F_dir = f_from_types(s_test, t, u, beta, type_sums(s_test, t, u, beta, "2d", 60))
    err = np.max(np.abs(F_real_cheb - F_dir) / np.abs(F_dir))
    check("BREAK-C6-real-cheb", err > 1e-8, f"real-interval Chebyshev (N = {n_cheb}) at s = {s_test}: {err:.2e}")


# ---------------------------------------------------------------------------------------
# Group c6b: eigenvalue-branch zeros in complex s and their isotropy (record 051 Block 11)
# ---------------------------------------------------------------------------------------
# Branches are followed by continuity of the eigenvector: at each step the eigenpair of the
# new matrix with the largest Hermitian overlap |v_prev^dagger v| with the previous vector
# is taken, and the step is halved until the overlap exceeds OV_MIN and the phase step of
# the eigenvalue is below PH_MAX (unambiguous unwrapping).  A complex-symmetric matrix has
# bilinearly orthogonal eigenvectors (v_a^T v_b = 0 for mu_a != mu_b), not Hermitian ones,
# so two distinct branches can have a large Hermitian overlap; the criterion below is
# therefore the *best* overlap close to one under step refinement, and a point where the
# two best overlaps are both above OV_AMB is flagged as ambiguous (near an exceptional
# point, where two eigenvectors coalesce; Kato VII section 1).
OV_MIN, OV_AMB, PH_MAX = 0.995, 0.9, 0.25 * math.pi


def load_tab(path: Path) -> tuple[dict, dict]:
    """Load a tabulation of format (10.4) and rebuild its node dictionary."""
    z = np.load(path)
    tab = {k: z[k] for k in z.files}
    for k in ("beta", "h", "r", "half"):
        tab[k] = float(tab[k])
    nodes = design_nodes(int(tab["design"][0]), float(tab["design"][1]), int(tab["design"][2]))
    if not (np.allclose(nodes["t"], tab["t"]) and np.allclose(nodes["u"], tab["u"])):
        raise ValueError("node triples of the tabulation do not match its design")
    return tab, nodes


def tab_eval_d(tab: dict, nodes: dict, s: complex, n_coef: int | None = None) -> tuple:
    """(F, dF/ds) on all node triples from the tabulation (analytic derivative, ``chebder``)."""
    panel = int(np.clip(np.searchsorted(tab["centres"] + tab["half"], s.real), 0, 2))
    x = (s - tab["centres"][panel]) / (1j * tab["h"])
    a = tab["a"][panel] if n_coef is None else tab["a"][panel][:, :n_coef]
    a = a * (1j ** np.arange(a.shape[1], dtype=float))[None, :, None]
    hX = np.stack([cheb_eval_complex(a[k], x) for k in range(3)])
    dhX = np.stack([cheb_eval_complex(C.chebder(a[k], axis=0), x) for k in range(3)]) / (1j * tab["h"])
    cX = tab["cX"]
    e = np.exp(cX[:, None] * s)
    JX, dJX = e * hX, e * (cX[:, None] * hX + dhX)
    lb = math.log(tab["beta"])
    pref = 2.0 * np.exp((8.0 - ALPHA_P * (s + nodes["t"] + nodes["u"]) / 2.0) * lb)
    return pref * JX.sum(0), pref * (dJX.sum(0) - 0.5 * ALPHA_P * lb * JX.sum(0))


class BranchTracker:
    """Eigenpairs of M^(n)(s) from the tabulation, with a small cache, and overlap matching."""

    def __init__(self, tab: dict, nodes: dict, n: int, n_coef: int | None = None) -> None:
        """Wave n of the tabulation ``tab`` on ``nodes``; ``n_coef`` truncates the Chebyshev degree."""
        self.tab, self.nodes, self.n, self.n_coef = tab, nodes, n, n_coef
        self.cache: dict[complex, tuple] = {}
        self.n_eval = 0

    def matrix(self, s: complex) -> np.ndarray:
        """M^(n)(s) from the tabulation."""
        return matrices_from_entries(tab_eval(self.tab, self.nodes, s, n_coef=self.n_coef), self.nodes, (self.n,))[self.n]

    def dmatrix(self, s: complex) -> tuple[np.ndarray, np.ndarray]:
        """(M^(n)(s), dM^(n)/ds) from the tabulation and its analytic derivative."""
        F, dF = tab_eval_d(self.tab, self.nodes, s, self.n_coef)
        return (matrices_from_entries(F, self.nodes, (self.n,))[self.n],
                matrices_from_entries(dF, self.nodes, (self.n,))[self.n])

    def eigpairs(self, s: complex) -> tuple[np.ndarray, np.ndarray]:
        """(eigenvalues, unit eigenvectors as columns) of M^(n)(s), cached."""
        s = complex(s)
        if s not in self.cache:
            ev, V = np.linalg.eig(self.matrix(s))
            V = V / np.linalg.norm(V, axis=0)
            if len(self.cache) > 4000:
                self.cache.clear()
            self.cache[s] = (ev, V)
            self.n_eval += 1
        return self.cache[s]

    def anchor(self, s_real: float, k: int = 4) -> np.ndarray:
        """Eigenvectors of the k eigenvalues of largest modulus at a real anchor."""
        ev, V = self.eigpairs(complex(s_real, 0.0))
        return V[:, np.argsort(-np.abs(ev))[:k]]

    def match(self, v: np.ndarray, s: complex) -> tuple[complex, np.ndarray, float, float]:
        """(mu, vector, best overlap, second-best overlap) of the eigenpair at s closest to v."""
        ev, V = self.eigpairs(s)
        ov = np.abs(v.conj() @ V)
        i = int(np.argmax(ov))
        ov2 = ov.copy()
        ov2[i] = 0.0
        return ev[i], V[:, i], float(ov[i]), float(ov2.max())


class Branch:
    """State of one tracked branch: the point s, the eigenvalue mu, the unit eigenvector v."""

    def __init__(self, s: complex, mu: complex, v: np.ndarray) -> None:
        """Branch at s with eigenvalue mu and unit eigenvector v."""
        self.s, self.mu, self.v = complex(s), complex(mu), v


def carry(tr: BranchTracker, br: Branch, pts: np.ndarray, amb: list | None = None) -> tuple[Branch, float, int, float]:
    """
    Follow the branch ``br`` (at pts[0]) along the polyline ``pts`` with adaptive steps.

    Returns (branch at pts[-1], unwrapped phase change of mu, ambiguous points, minimal
    accepted best overlap).  A step is halved (down to 2^-8 of the segment) until the best
    overlap is >= OV_MIN and the eigenvalue phase step is below PH_MAX; a point where that
    fails at the smallest step, or where the second-best overlap exceeds OV_AMB, is counted
    as ambiguous and appended to ``amb`` as (s, best, second, |mu|).
    """
    v, mu, phase, n_amb, ov_min = br.v, br.mu, 0.0, 0, 1.0
    for a, b in zip(pts[:-1], pts[1:], strict=True):
        tt = 0.0
        while tt < 1.0 - 1e-12:
            step = 1.0 - tt
            while True:
                s_new = a + (b - a) * (tt + step)
                mu_new, v_new, ov, ov2 = tr.match(v, s_new)
                dph = float(np.angle(mu_new / mu))
                if (ov >= OV_MIN and abs(dph) < PH_MAX) or step < 2.0**-8:
                    break
                step *= 0.5
            if ov < OV_MIN or ov2 > OV_AMB:
                n_amb += 1
                if amb is not None:
                    amb.append((complex(s_new), ov, ov2, abs(mu_new)))
            ov_min = min(ov_min, ov)
            phase += dph
            v, mu, tt = v_new, mu_new, tt + step
    return Branch(pts[-1], mu, v), phase, n_amb, ov_min


def rect_pts(x0: float, x1: float, y0: float, y1: float, h: float) -> np.ndarray:
    """Counter-clockwise closed polyline of the rectangle, vertices spaced by at most h."""
    def seg(a: complex, b: complex) -> np.ndarray:
        m = max(1, int(math.ceil(abs(b - a) / h)))
        return a + (b - a) * np.arange(m) / m
    c = [complex(x0, y0), complex(x1, y0), complex(x1, y1), complex(x0, y1)]
    return np.concatenate([seg(c[i], c[(i + 1) % 4]) for i in range(4)] + [np.array([c[0]])])


def branch_winding(tr: BranchTracker, br: Branch, x0, x1, y0, y1, h=0.25):  # noqa: ANN001
    """
    Winding number of one branch around the rectangle [x0,x1] x [y0,y1]i.

    The branch is first carried from br.s to the corner (x0, y0) along a straight segment.
    Returns (winding, closure overlap |v_end^dagger v_corner|, ambiguous points, minimal
    accepted overlap, branch at the corner).  A closure overlap below OV_MIN means the
    branch did not return to itself (monodromy: an exceptional point inside).
    """
    amb: list = []
    br_c, _, _, ov0 = carry(tr, br, np.array([br.s, complex(x0, y0)]), amb)
    br_e, phase, _, ov1 = carry(tr, br_c, rect_pts(x0, x1, y0, y1, h), amb)
    closure = float(abs(br_e.v.conj() @ br_c.v))
    return int(round(phase / (2 * math.pi))), closure, amb, min(ov0, ov1), br_c


def newton_branch(tr: BranchTracker, br: Branch, iters: int = 40) -> tuple[Branch, float, int]:
    """
    Newton on the branch, mu' = v^T M' v / v^T v (Hellmann-Feynman, complex-symmetric family).

    The eigenpair at each iterate is the one of largest overlap with the previous vector.
    Returns (branch at the zero, |last step|, iterations).
    """
    s, v = br.s, br.v
    n_it = 0
    for _ in range(iters):
        n_it += 1
        M, dM = tr.dmatrix(s)
        ev, V = np.linalg.eig(M)
        V = V / np.linalg.norm(V, axis=0)
        i = int(np.argmax(np.abs(v.conj() @ V)))
        mu, v = ev[i], V[:, i]
        dmu = (v @ dM @ v) / (v @ v)
        step = mu / dmu
        s = s - step
        if abs(step) < 1e-13 * max(1.0, abs(s)):
            break
    M = tr.matrix(s)
    ev, V = np.linalg.eig(M)
    V = V / np.linalg.norm(V, axis=0)
    i = int(np.argmax(np.abs(v.conj() @ V)))
    return Branch(s, ev[i], V[:, i]), abs(step), n_it


def isotropy(v: np.ndarray) -> float:
    """|v^T v| / v^dagger v: 1 for a real vector (up to a phase), 0 for an isotropic one."""
    return float(abs(v @ v) / np.vdot(v, v).real)


# The 050 anchors (record 050 (2.1), design (44,8,24), and (3.4)); the tabulation's error
# is <= 1.4e-10 relative (record 051 Block 9), 050 prints eight figures.
ANCHOR_050 = {
    16.0 / 3.0: (1.1328230e7, 4.6320173e5, 5.2701594e4, 5.6353611e3),
    4.0: (2.7574361e7, 9.1735626e5, 9.5198752e4, 1.0392241e4),
}
RATIO_050_N2 = 2.092e-2  # mu_{2,0}/mu_{0,0} at alpha' s = 4, record 050 (3.4)
# Cells of the set-winding exploration (output/c6b-drive4.log) where a winding was
# read but no branch vanishes: Newton from every one of the 8 leading anchor branches must
# not converge inside the region (record 051 (11.3)); the planted zero shows it can.
# The loop of mu_{2,3} on [-30,-20] x [30,40]i does not close (closure 0.03): the branch is
# at 3e-9 of mu_{2,0} there, within a decade of the floor 1e-11 (record 051 (9.3), (11.3)(c)),
# and is not counted in the negative claim.
FLOOR_LOOPS = {(2, 3, -30.0, 30.0)}
NEWTON_CELLS = (complex(3.4375, 9.6875), complex(3.4375, 31.5625), complex(2.8125, 19.6875))


def in_region(s: complex) -> bool:
    """Membership in the region S = [-40, 20] x [-40, 40]i."""
    return -40.0 <= s.real <= 20.0 and abs(s.imag) <= 40.0


def group_c6b(rng: np.random.Generator, tab_path: Path) -> None:  # noqa: PLR0915
    """Record 051 section 18c.6b (Block 11): tabulation re-validation, branches, windings."""
    t_all = time.time()
    tab, nodes = load_tab(tab_path)
    print(f"c6b: tabulation {tab_path}, design {tuple(tab['design'])}, {nodes['t'].size} triples")
    # --- C7.1: C6-tail on the full coefficients, anchors of 050
    a, r = tab["a"], tab["r"]
    kk = np.arange(a.shape[2], dtype=float)
    mag = np.abs(a) * (r**kk)[None, None, :, None]
    tail = float(np.max(mag[:, :, -3:, :].max(2) / mag.max(2)))
    check("C7.1-tail", tail < 1e-10, f"last three |a_k| r^k relative to the largest (full design): {tail:.2e}")
    worst = 0.0
    for s_r, ref in ANCHOR_050.items():
        M = matrices_from_entries(tab_eval(tab, nodes, complex(s_r, 0.0)), nodes)
        e0 = leading_eigs(M[0], 4)
        worst = max(worst, float(np.max(np.abs(e0.real - np.array(ref)) / np.array(ref))), float(np.max(np.abs(e0.imag) / np.abs(e0))))
        if s_r == 4.0:
            ratio = float(leading_eigs(M[2], 1)[0].real / e0[0].real)
    check("C7.1-anchor-n0", worst < 1e-7, f"four leading eigenvalues of M^(0) at s = 16/3 and 4 against 050 (2.1): rel {worst:.2e}")
    check("C7.1-anchor-n2", abs(ratio - RATIO_050_N2) < 5e-6, f"mu_(2,0)/mu_(0,0) at s = 4: {ratio:.5e} (050 (3.4): {RATIO_050_N2})")
    # --- C7.2: reflection, analytic derivative, Hellmann-Feynman
    pts = [complex(rng.uniform(-40, 20), rng.uniform(-40, 40)) for _ in range(3)]
    e_ref, e_der, e_hf = 0.0, 0.0, 0.0
    h = 1e-4
    for s in pts:
        Fp, Fm = tab_eval(tab, nodes, s + h), tab_eval(tab, nodes, s - h)
        F, dF = tab_eval_d(tab, nodes, s)
        e_der = max(e_der, float(np.max(np.abs(dF - (Fp - Fm) / (2 * h)) / np.abs(dF))))
        Fc = tab_eval(tab, nodes, s.conjugate())
        e_ref = max(e_ref, float(np.max(np.abs(Fc - F.conj()) / np.abs(F))))
        for n in (0, 2):
            tr = BranchTracker(tab, nodes, n)
            M, dM = tr.dmatrix(s)
            ev, V = np.linalg.eig(M)
            o = np.argsort(-np.abs(ev))[:2]
            for j in o:
                v = V[:, j]
                hf = (v @ dM @ v) / (v @ v)
                bp, _, _, _ = carry(tr, Branch(s, ev[j], v), np.array([s, s + h]))
                bm, _, _, _ = carry(tr, Branch(s, ev[j], v), np.array([s, s - h]))
                fd = (bp.mu - bm.mu) / (2 * h)
                e_hf = max(e_hf, abs(hf - fd) / abs(fd))
    check("C7.2-reflect", e_ref < 1e-10, f"F(conj s) = conj F(s) entrywise at 3 seeded points: {e_ref:.2e}")
    check("C7.2-deriv", e_der < 1e-7, f"analytic dF/ds against the centred difference (h = 1e-4): {e_der:.2e}")
    check("C7.2-HF", e_hf < 1e-6, f"Hellmann-Feynman mu' = v^T M' v / v^T v against the tracked difference, two leading branches, n = 0, 2: {e_hf:.2e}")
    # --- C7.3-left: the twelve rectangles with Re s <= -20, four branches, both waves
    for n in (0, 2):
        tr = BranchTracker(tab, nodes, n)
        ev, V = tr.eigpairs(complex(16.0 / 3.0, 0.0))
        V = V / np.linalg.norm(V, axis=0)
        o = np.argsort(-np.abs(ev))[:4]
        anchors = [Branch(complex(16.0 / 3.0, 0.0), ev[o[k]], V[:, o[k]]) for k in range(4)]
        t0 = time.time()
        wmax, clmin, amb_max, failed = 0, 1.0, 0, []
        for x0 in (-40.0, -30.0):
            for y0 in (0.0, 10.0, 20.0, 30.0):
                for k in range(4):
                    w, cl, amb, _, _ = branch_winding(tr, anchors[k], x0, x0 + 10.0, y0, y0 + 10.0, 0.5)
                    if (n, k, x0, y0) in FLOOR_LOOPS:
                        print(f"    excluded loop n={n} j={k} [{x0:.0f},{x0 + 10:.0f}]x[{y0:.0f},{y0 + 10:.0f}]i: "
                              f"winding {w}, closure {cl:.3f}, ambiguous {len(amb)} (branch at the floor, not counted)")
                        continue
                    if w != 0 or cl < 0.99 or len(amb) > 3:
                        failed.append((k, x0, y0, w, round(cl, 3), len(amb)))
                    wmax, clmin, amb_max = max(wmax, abs(w)), min(clmin, cl), max(amb_max, len(amb))
        check(f"C7.3-left[n={n}]", not failed,
              f"{32 - sum(1 for f in FLOOR_LOOPS if f[0] == n)} loops of [-40,-20]x[0,40]i, branches j <= 3: max |winding| {wmax}, "
              f"min closure {clmin:.4f}, max ambiguous points per loop {amb_max}; failed loops {failed} "
              f"({time.time() - t0:.0f} s, {tr.n_eval} matrices)")
        if n == 0:
            # BREAK-C7-plant: a planted zero of the branch (mu -> mu (s - s1)) must wind once
            s1 = complex(rng.uniform(-38, -22), rng.uniform(2, 18))
            br_c, _, _, _ = carry(tr, anchors[1], np.array([anchors[1].s, complex(-40.0, 0.0)]))
            pts_r = rect_pts(-40.0, -20.0, 0.0, 20.0, 0.5)
            phase, mu, v = 0.0, br_c.mu * (br_c.s - s1), br_c.v
            for s in pts_r[1:]:
                mu_new, v, _, _ = tr.match(v, s)
                mu_new = mu_new * (s - s1)
                phase += float(np.angle(mu_new / mu))
                mu = mu_new
            w_plant = int(round(phase / (2 * math.pi)))
            check("BREAK-C7-plant-wind", w_plant == 1, f"planted zero at {s1:.3f} on the branch mu_(0,1): winding {w_plant} (must be 1)")
            # BREAK-C7-plant-newton: Newton on the planted branch converges to s1 from 0.4 away
            s, v = s1 + complex(0.3, -0.25), None
            for _ in range(40):
                M, dM = tr.dmatrix(s)
                ev_, V_ = np.linalg.eig(M)
                V_ = V_ / np.linalg.norm(V_, axis=0)
                i = int(np.argmax(np.abs(ev_))) if v is None else int(np.argmax(np.abs(v.conj() @ V_)))
                mu, v = ev_[i], V_[:, i]
                dmu = (v @ dM @ v) / (v @ v)
                step = mu * (s - s1) / (dmu * (s - s1) + mu)
                s = s - step
                if abs(step) < 1e-13 * abs(s):
                    break
            check("BREAK-C7-plant-newton", abs(s - s1) < 1e-9, f"Newton on mu (s - s1) from 0.4 away: |s - s1| = {abs(s - s1):.1e}")
    # --- C7.3-newton-none: no branch among the 8 leading anchor branches vanishes near the
    #     cells where the set winding was read (output/c6b-drive4.log)
    tr = BranchTracker(tab, nodes, 0)
    ev, V = tr.eigpairs(complex(16.0 / 3.0, 0.0))
    V = V / np.linalg.norm(V, axis=0)
    o = np.argsort(-np.abs(ev))[:8]
    n_conv, min_ratio = 0, 1.0
    for sc in NEWTON_CELLS:
        evc, _ = tr.eigpairs(sc)
        mx = float(np.max(np.abs(evc)))
        for k in range(8):
            b, _, _, _ = carry(tr, Branch(complex(16.0 / 3.0, 0.0), ev[o[k]], V[:, o[k]]), np.array([complex(16.0 / 3.0, 0.0), complex(sc.real, 0.0), sc]))
            min_ratio = min(min_ratio, abs(b.mu) / mx)
            bz, last, _ = newton_branch(tr, b, 40)
            if in_region(bz.s) and last < 1e-8:
                n_conv += 1
                print(f"    converged zero from branch {k} at cell {sc}: {bz.s}")
    check("C7.3-newton-none", n_conv == 0 and min_ratio > 1e-7,
          f"Newton from the 8 leading anchor branches at {len(NEWTON_CELLS)} cell centres: {n_conv} converged zeros in S; "
          f"smallest |mu|/max at the centres {min_ratio:.1e} (all branches resolvable, none small)")
    # --- BREAK-C7-order: value-order labelling mis-tracks where the modulus order changes
    tr = BranchTracker(tab, nodes, 0)
    col = complex(3.0, 0.0) + 1j * np.arange(0.0, 40.01, 0.5)
    ev, V = tr.eigpairs(col[0])
    V = V / np.linalg.norm(V, axis=0)
    br = Branch(col[0], ev[np.argmax(np.abs(ev))], V[:, np.argmax(np.abs(ev))])
    n_mis, first = 0, None
    for s in col[1:]:
        br, _, _, _ = carry(tr, br, np.array([br.s, s]))
        ev, _ = tr.eigpairs(s)
        if abs(br.mu) < 0.999 * np.max(np.abs(ev)):
            n_mis += 1
            first = first or s
    check("BREAK-C7-order", n_mis > 0,
          f"column Re s = 3: the overlap-tracked leading branch is not the largest modulus at {n_mis} of {len(col) - 1} points "
          f"(first at {first}); value-order labelling would switch branches there")
    print(f"  c6b wall {time.time() - t_all:.0f} s")


# ---------------------------------------------------------------------------------------
# 18c.6c (record 051 Block 12, C7.6): label-free zero count by the projected determinant
# ---------------------------------------------------------------------------------------
# d_K(s) = prod of the K eigenvalues of largest modulus of M^(n)(s) = det(P^T M P)/det(P^T P)
# for any basis P of their invariant subspace (bilinear Gram; P from ``eig``).  It is a
# symmetric function of the K-set, hence needs no branch labels; on a contour along which the
# modulus gap |mu_(K-1)|/|mu_(K)| >= GAP_MIN the K-set is the same set at every point and d_K
# is continuous, so its winding is an integer; the winding counts the zeros inside of the K
# leading branches (continued from the contour) when no exceptional point inside joins the
# K-set to its complement -- a coalescence which would bring the gap to 1 at that point, and is
# tested by the same gap at interior sample points (record 051 (12.1)).  The phase step
# |Delta arg d_K| < pi/2 between consecutive contour points is enforced by bisection.

C6C_FLOOR = 1e-9  # |mu_(K-1)| >= floor * |mu_(0)| on the whole contour (record 051 (9.3), (11.5))
C6C_GAP = 3.0  # minimal modulus gap |mu_(K-1)|/|mu_(K)| along the contour and at interior samples
C6C_H0 = 0.25  # initial contour step
C6C_HMIN = C6C_H0 / 2**8  # smallest bisection step
C6C_MAXLEV = 4  # quadrisection depth of unresolved cells (fix pass: was 2 in run1)
C6C_DESIGN2 = (44, 8.0, 24)  # the second design of the design-stability test (12.6)
C6C_DIRECT = (complex(3.2266, 9.4609), 1 / 32, 5)  # centre, half-side, points per side of the direct contour
_C6C_CACHE: dict = {}


class SpecCache:
    """Eigenvalues (sorted by decreasing modulus) of M^(0), M^(2) at s from the tabulation, cached."""

    def __init__(self, tab: dict, nodes: dict, n_coef: int | None = None) -> None:
        """Tabulation ``tab`` on ``nodes``; ``n_coef`` truncates the Chebyshev degree (falsifier)."""
        self.tab, self.nodes, self.n_coef = tab, nodes, n_coef
        self.cache: dict[complex, dict] = {}
        self.n_eval = 0

    def spec(self, s: complex) -> dict:
        """{n: eigenvalues of M^(n)(s) sorted by decreasing modulus}."""
        s = complex(s)
        if s not in self.cache:
            M = matrices_from_entries(tab_eval(self.tab, self.nodes, s, n_coef=self.n_coef), self.nodes)
            out = {}
            for n, Mn in M.items():
                ev = np.linalg.eigvals(Mn)
                out[n] = ev[np.argsort(-np.abs(ev))]
            if len(self.cache) > 20000:
                self.cache.clear()
            self.cache[s] = out
            self.n_eval += 1
        return self.cache[s]


def proj_det(M: np.ndarray, K: int) -> tuple[complex, complex]:
    """(det(P^T M P)/det(P^T P), prod of the K leading eigenvalues), P the ``eig`` vectors."""
    ev, V = np.linalg.eig(M)
    o = np.argsort(-np.abs(ev))[:K]
    P = V[:, o]
    return np.linalg.det(P.T @ M @ P) / np.linalg.det(P.T @ P), np.prod(ev[o])


def choose_K(specs: list, floor: float = C6C_FLOOR, gap_min: float = C6C_GAP) -> tuple[int | None, float]:
    """
    Largest K with |mu_(K-1)| >= floor*|mu_(0)| and gap |mu_(K-1)|/|mu_(K)| >= gap_min at all points.

    Returns (K, its minimal gap over the points); (None, best gap) when no K qualifies.
    """
    mods = np.abs(np.array(specs))
    rel = (mods / mods[:, :1]).min(0)
    gap = (mods[:, :-1] / mods[:, 1:]).min(0)  # gap[k-1] is the gap of K = k
    ok = [k for k in range(1, mods.shape[1]) if rel[k - 1] >= floor and gap[k - 1] >= gap_min]
    if not ok:
        adm = [k for k in range(1, mods.shape[1]) if rel[k - 1] >= floor]
        return None, float(max(gap[k - 1] for k in adm)) if adm else 0.0
    K = max(ok)
    return K, float(gap[K - 1])


def _logd(ev: np.ndarray, K: int, s: complex, plant: complex | None) -> complex:
    """log d_K(s) (a branch of it), with the planted factor (s - plant) if requested."""
    val = complex(np.sum(np.log(ev[:K])))
    return val + (np.log(s - plant) if plant is not None else 0.0)


def cell_winding(sc: SpecCache, n: int, x0: float, x1: float, y0: float, y1: float, K: int,
                 h0: float = C6C_H0, h_min: float = C6C_HMIN, gap_min: float = C6C_GAP,
                 plant: complex | None = None) -> dict:
    """
    Winding of d_K around the cell with step control |Delta arg| < pi/2 (bisection to h_min).

    Returns {wind, n_pts, min_gap, step_fail, gap_fail}: ``gap_fail`` is set when the K-gap
    falls below gap_min at any contour point (the K-set is then not the same set along the
    contour and the winding is not a count); ``step_fail`` when a phase step >= pi/2 survives
    at h_min.
    """
    pts = list(rect_pts(x0, x1, y0, y1, h0))
    evs = [sc.spec(s)[n] for s in pts]
    total, i, step_fail, min_gap = 0.0, 0, 0, np.inf
    while i < len(pts) - 1:
        e0, e1 = evs[i], evs[i + 1]
        d = (_logd(e1, K, pts[i + 1], plant) - _logd(e0, K, pts[i], plant)).imag
        d = (d + math.pi) % (2 * math.pi) - math.pi
        if abs(d) >= math.pi / 2 and abs(pts[i + 1] - pts[i]) > h_min * 1.001:
            sm = 0.5 * (pts[i] + pts[i + 1])
            pts.insert(i + 1, sm)
            evs.insert(i + 1, sc.spec(sm)[n])
            continue
        if abs(d) >= math.pi / 2:
            step_fail += 1
        total += d
        i += 1
    mods = np.abs(np.array(evs))
    if K < mods.shape[1]:
        min_gap = float((mods[:, K - 1] / mods[:, K]).min())
    return {"wind": int(round(total / (2 * math.pi))), "resid": abs(total / (2 * math.pi) - round(total / (2 * math.pi))),
            "n_pts": len(pts), "min_gap": min_gap, "step_fail": step_fail, "gap_fail": bool(min_gap < gap_min)}


def count_cell(sc: SpecCache, n: int, x0: float, x1: float, y0: float, y1: float, K: int | None = None,
               floor: float = C6C_FLOOR, gap_min: float = C6C_GAP, h0: float = C6C_H0, plant: complex | None = None) -> dict:
    """
    K chosen from the contour (step h0) and a 2 x 2 interior sample, then the winding of d_K.

    ``status``: 'ok' (winding is a count), 'nogap' (no admissible K: subdivide or report),
    'gapfail' (the gap failed at an inserted point), 'stepfail'.
    """
    cont = list(rect_pts(x0, x1, y0, y1, h0))
    inner = [complex(x0 + (x1 - x0) * a, y0 + (y1 - y0) * b) for a in (1 / 3, 2 / 3) for b in (1 / 3, 2 / 3)]
    specs = [sc.spec(s)[n] for s in cont + inner]
    Kc, gap = choose_K(specs, floor, gap_min)
    if K is None:
        K = Kc
    if K is None:
        return {"cell": (x0, x1, y0, y1), "n": n, "K": None, "gap": gap, "status": "nogap", "wind": None}
    w = cell_winding(sc, n, x0, x1, y0, y1, K, h0=h0, gap_min=gap_min, plant=plant)
    mods = np.abs(np.array(specs))
    gap_all = float(min(w["min_gap"], (mods[:, K - 1] / mods[:, K]).min()))
    status = "ok"
    if w["gap_fail"] or gap_all < gap_min:
        status = "gapfail"
    elif w["step_fail"]:
        status = "stepfail"
    return {"cell": (x0, x1, y0, y1), "n": n, "K": K, "gap": gap_all, "status": status, "wind": w["wind"],
            "resid": w["resid"], "n_pts": w["n_pts"]}


def _c6c_worker(args: tuple) -> list:
    """Count the cells of one strip (both waves); subdivides 'nogap' cells twice."""
    tab_path, xs, y0, y1, side = args
    if "sc" not in _C6C_CACHE:
        tab, nodes = load_tab(Path(tab_path))
        _C6C_CACHE["sc"] = SpecCache(tab, nodes)
    sc = _C6C_CACHE["sc"]
    out = []
    for x0 in xs:
        for n in (0, 2):
            stack = [(x0, x0 + side, yy, yy + side, 0) for yy in np.arange(y0, y1 - 1e-9, side)]
            while stack:
                a, b, c, d, lev = stack.pop()
                r = count_cell(sc, n, a, b, c, d, h0=min(C6C_H0, (b - a) / 4))  # sub-cells sampled at >= 4 points per side
                if r["status"] in ("nogap", "gapfail") and lev < C6C_MAXLEV:
                    m1, m2 = 0.5 * (a + b), 0.5 * (c + d)
                    stack += [(a, m1, c, m2, lev + 1), (m1, b, c, m2, lev + 1), (a, m1, m2, d, lev + 1), (m1, b, m2, d, lev + 1)]
                    continue
                r["level"] = lev
                out.append(r)
    return out


def refine_zero(sc: SpecCache, n: int, cell: tuple, K_parent: int, min_side: float = 1 / 16) -> dict:
    """
    Gap-respecting refinement of a winding cell (record 051 (12.2), (12.6)): quadrisection with K
    re-chosen per sub-cell (``count_cell`` with ``K=None``), every sub-cell that is unresolved or
    carries a winding being subdivided again, down to ``min_side``.

    Returns {status, cells, Ks}: 'persists' when a resolved sub-cell of side min_side carries the
    winding (listed in ``cells`` with its K and gap); 'unresolved' when a sub-cell of side min_side
    fails the gap (listed); 'dissolved' when every leaf is resolved with winding 0 and its K-set
    contains the parent's (K >= K_parent); 'dissolved-weak' when every leaf is resolved with
    winding 0 but some leaf's K is below the parent's, so that its K-set may not contain the
    branch that carried the parent winding — the tabulation then does not decide the cell.
    """
    stack = [cell]
    leaves, Ks = [], set()
    while stack:
        a, b, c, d = stack.pop()
        m1, m2 = 0.5 * (a + b), 0.5 * (c + d)
        for q in [(a, m1, c, m2), (m1, b, c, m2), (a, m1, m2, d), (m1, b, m2, d)]:
            r = count_cell(sc, n, *q, h0=(m1 - a) / 4)
            small = (m1 - a) <= min_side * 1.001
            if r["status"] == "ok" and r["wind"] == 0:
                leaves.append(("zero", q, r["K"], r["gap"]))
                Ks.add(r["K"])
            elif small:
                leaves.append(("persists" if r["status"] == "ok" else "unresolved", q, r["K"], r["gap"]))
                if r["K"]:
                    Ks.add(r["K"])
            else:
                stack.append(q)
    kinds = {k for k, *_ in leaves}
    if "persists" in kinds:
        status = "persists"
    elif "unresolved" in kinds:
        status = "unresolved"
    else:
        status = "dissolved" if min(Ks) >= K_parent else "dissolved-weak"
    return {"status": status, "cells": [lf for lf in leaves if lf[0] != "zero"], "Ks": sorted(Ks), "n_leaves": len(leaves)}


def newton_floor(tr: BranchTracker, s0: complex, K: int, iters: int = 8, floor: float = C6C_FLOOR) -> dict:
    """
    Floor-aware Newton on the tabulation: from the smallest of the K leading eigenvalues at s0,
    Hellmann-Feynman steps (analytic dM/ds of the tabulation), the branch followed by maximal
    bilinear eigenvector overlap; steps capped at 0.02.

    Returns {status, s, dist, mu_rel, iota}: 'converged' (last step < 1e-6), 'floor' (the
    followed eigenvalue sits below 10*floor of the largest at every iterate: the tabulation
    cannot resolve the zero, (12.2)), else 'diverged'.
    """
    s, vprev, dist, mu_rel, steps, iotas = s0, None, 0.0, [], [], []
    for _ in range(iters):
        M, dM = tr.dmatrix(s)
        ev, V = np.linalg.eig(M)
        o = np.argsort(-np.abs(ev))
        if vprev is None:
            j = o[np.argmin(np.abs(ev[o[:K]]))]
        else:
            j = int(np.argmax(np.abs(V.T @ vprev) / np.sqrt(np.abs(np.sum(V * V, axis=0)))))
        v, mu = V[:, j], ev[j]
        vprev = v
        step = -mu / ((v @ dM @ v) / (v @ v))
        mu_rel.append(abs(mu) / abs(ev[o[0]]))
        iotas.append(isotropy(v))
        steps.append(abs(step))
        if abs(step) > 0.02:
            step *= 0.02 / abs(step)
        s = s + step
        dist = max(dist, abs(s - s0))
    status = "converged" if steps[-1] < 1e-6 else ("floor" if max(mu_rel) < 10 * floor and dist < 0.05 else "diverged")
    return {"status": status, "s": s, "dist": dist, "mu_rel": mu_rel, "iota": iotas, "steps": steps}


def _direct_job(args: tuple) -> tuple:
    """One direct (non-tabulated) evaluation of M^(0), M^(2) at s on a design (record 051 (12.6))."""
    s, design = args
    nodes = design_nodes(*design)
    JX = type_sums(s, nodes["t"], nodes["u"], 2.0, "2d", 60)
    M = matrices_from_entries(f_from_types(s, nodes["t"], nodes["u"], 2.0, JX), nodes)
    return s, M[0], M[2]


def square_points(centre: complex, half: float, n_side: int) -> tuple[list, list]:
    """Counter-clockwise contour points (n_side per side) and the 2 x 2 interior samples of a square."""
    x0, x1, y0, y1 = centre.real - half, centre.real + half, centre.imag - half, centre.imag + half
    ts = np.arange(n_side) / n_side
    pts = [complex(x0 + (x1 - x0) * t, y0) for t in ts] + [complex(x1, y0 + (y1 - y0) * t) for t in ts]
    pts += [complex(x1 - (x1 - x0) * t, y1) for t in ts] + [complex(x0, y1 - (y1 - y0) * t) for t in ts]
    inner = [complex(x0 + (x1 - x0) * a, y0 + (y1 - y0) * b) for a in (1 / 3, 2 / 3) for b in (1 / 3, 2 / 3)]
    return pts, inner


def direct_contour(design: tuple, centre: complex, half: float, n_side: int, workers: int, cache: Path | None = None) -> dict:
    """
    M^(0) by direct evaluation on the square contour and its interior samples (6 workers, spawn).

    ``cache``: an .npz written by ``output/c6d-direct.py`` with the same design, centre
    and half-side is reused (the same evaluator, run in the background); otherwise computed.
    """
    pts, inner = square_points(centre, half, n_side)
    if cache is not None and cache.exists():
        d = np.load(cache)
        if tuple(d["design"]) == tuple(design) and abs(complex(d["centre"]) - centre) < 1e-12 and abs(float(d["half"]) - half) < 1e-12 \
                and int(d["n_cont"]) == len(pts) and int(d["n_inner"]) == len(inner):
            return {"s": d["s"][: len(pts) + len(inner)], "M0": d["M0"][: len(pts) + len(inner)], "n_cont": len(pts), "source": str(cache)}
    ctx = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as ex:
        res = list(ex.map(_direct_job, [(s, design) for s in pts + inner], chunksize=1))
    return {"s": np.array([r[0] for r in res]), "M0": np.array([r[1] for r in res]), "n_cont": len(pts), "source": "computed"}


def direct_windings(dc: dict, Ks=range(8, 14), gap_min: float = C6C_GAP, plant: complex | None = None) -> dict:
    """Winding of d_K on the direct contour for each K, with the gap on contour + interior and the max phase step."""
    ev = []
    for M in dc["M0"]:
        e = np.linalg.eigvals(M)
        ev.append(e[np.argsort(-np.abs(e))])
    ev = np.array(ev)
    nc = dc["n_cont"]
    mods = np.abs(ev)
    gap = mods[:, :-1] / mods[:, 1:]
    out = {}
    for K in Ks:
        logd = np.array([_logd(ev[i], K, dc["s"][i], plant) for i in range(nc)])
        dphi = np.diff(np.concatenate([logd.imag, logd.imag[:1]]))
        dphi = (dphi + np.pi) % (2 * np.pi) - np.pi
        w = dphi.sum() / (2 * np.pi)
        out[K] = {"wind": int(round(w)), "resid": abs(w - round(w)), "dphi_max": float(np.abs(dphi).max()),
                  "gap": float(gap[:, K - 1].min()), "rel": float((mods[:nc, K - 1] / mods[:nc, 0]).min()),
                  "ok": bool(gap[:, K - 1].min() >= gap_min and np.abs(dphi).max() < np.pi / 2)}
    out["ladder"] = (mods[nc:, :14] / mods[nc:, :1]).min(0)
    return out


def group_c6c(rng: np.random.Generator, tab_path: Path, workers: int = 6, side: float = 1.0) -> None:  # noqa: PLR0915
    """Record 051 section 18c.6c (Block 12): label-free zero count on [-20,20] x [0,40]i at beta = 2."""
    t_all = time.time()
    tab, nodes = load_tab(tab_path)
    sc = SpecCache(tab, nodes)
    # --- C7.6-tool-proj: det(P^T M P)/det(P^T P) equals the product of the K leading eigenvalues
    worst = 0.0
    for _ in range(3):
        s = complex(rng.uniform(-20, 20), rng.uniform(0, 40))
        M = matrices_from_entries(tab_eval(tab, nodes, s), nodes)
        for n in (0, 2):
            for K in (3, 6, 9):
                a, b = proj_det(M[n], K)
                worst = max(worst, abs(a - b) / abs(b))
    # tolerance 1e-7: the K=9 factor sits 1-2 decades above the floor (9.3), its own relative error is ~1e-8
    check("C7.6-tool-proj", worst < 1e-7, f"det(P^T M P)/det(P^T P) against prod of the K leading eigenvalues, K in (3,6,9), 3 seeded points: rel {worst:.1e}")
    # --- C7.6-tool-sampling: winding independent of the sampling once the step control holds (EP-band cell)
    cell = (2.0, 3.0, 9.0, 10.0)
    r0 = count_cell(sc, 0, *cell)
    K = r0["K"]
    ws = [r0["wind"]] + [cell_winding(sc, 0, *cell, K, h0=h)["wind"] for h in (0.5, 0.125, 1 / 32)]
    wf = cell_winding(sc, 0, *cell, K, h0=1 / 64, h_min=1 / 64)["wind"]  # fixed fine step, no bisection
    check("C7.6-tool-sampling", len(set(ws + [wf])) == 1 and r0["status"] == "ok",
          f"cell {cell}, n=0, K={K}, gap {r0['gap']:.1f}: windings {ws} (h0 = 1/4, 1/2, 1/8, 1/32, adaptive) and {wf} (fixed 1/64)")
    # --- BREAK-C7.6-plant: a planted zero is counted once, and not in the neighbouring cell
    s1 = complex(2.37, 9.61)
    rp = count_cell(sc, 0, *cell, plant=s1)
    rq = count_cell(sc, 0, 3.0, 4.0, 9.0, 10.0, plant=s1)
    check("BREAK-C7.6-plant", rp["wind"] == r0["wind"] + 1 and rq["wind"] == count_cell(sc, 0, 3.0, 4.0, 9.0, 10.0)["wind"],
          f"d_K (s - s1), s1 = {s1}: winding {rp['wind']} on the cell (unplanted {r0['wind']}), {rq['wind']} on the neighbour")
    # --- BREAK-C7.6-straddle: a K straddling a modulus crossing is flagged, not counted
    specs = [sc.spec(s)[0] for s in rect_pts(*cell, 0.25)]
    mods = np.abs(np.array(specs))
    gaps = (mods[:, :-1] / mods[:, 1:]).min(0)
    Kbad = int(np.argmin(gaps[:12])) + 1
    rb = count_cell(sc, 0, *cell, K=Kbad)
    check("BREAK-C7.6-straddle", rb["status"] == "gapfail" and rb["gap"] < 1.5,
          f"forced K = {Kbad} (contour gap {rb['gap']:.2f}): status '{rb['status']}'")
    # --- C7.6-count: the census on [-20,20] x [0,40]i, both waves, strips in parallel
    xs_all = np.arange(-20.0, 20.0 - 1e-9, side)
    strips = [xs_all[i::workers] for i in range(workers)]
    jobs = [(str(tab_path), list(xs), 0.0, 40.0, side) for xs in strips]
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        results = [r for part in ex.map(_c6c_worker, jobs) for r in part]
    print(f"  census: {len(results)} cells in {time.time() - t0:.0f} s")
    zeros = []
    for n in (0, 2):
        rs = [r for r in results if r["n"] == n]
        ok = [r for r in rs if r["status"] == "ok"]
        bad = [r for r in rs if r["status"] != "ok"]
        Ks = np.array([r["K"] for r in ok])
        area_ok = sum((r["cell"][1] - r["cell"][0]) ** 2 for r in ok)
        total = sum(r["wind"] for r in ok)
        nz = [r for r in ok if r["wind"]]
        print(f"  n={n}: {len(ok)} resolved cells (area {area_ok:.2f} of 1600), K in [{Ks.min()},{Ks.max()}] (median {int(np.median(Ks))}), "
              f"min gap {min(r['gap'] for r in ok):.2f}, max |resid| {max(r['resid'] for r in ok):.2e}, "
              f"{len(bad)} unresolved cells: {[(r['cell'], r['status'], round(r['gap'], 2)) for r in bad][:12]}")
        lev = {}
        for r in ok:
            lev[r["level"]] = lev.get(r["level"], 0) + 1
        print(f"        cells by level (side 1, 1/2, 1/4): {lev}; total winding {total}; nonzero cells {[(r['cell'], r['wind'], r['K']) for r in nz]}")
        for r in nz:
            rf = refine_zero(sc, n, r["cell"], r["K"])
            print(f"        refined (free K per sub-cell, {rf['n_leaves']} leaves): {rf['status']}, leaf K in {rf['Ks']}, non-zero leaves {[(k, tuple(round(float(x), 5) for x in q), K, round(g, 2)) for k, q, K, g in rf['cells']]}")
            zeros.append((n, r["cell"], rf))
        check(f"C7.6-count[n={n}]", len(bad) == 0 and all(r["resid"] < 0.05 for r in ok),
              f"census on [-20,20] x [0,40]i: total winding {total} over {len(ok)} resolved cells, {len(bad)} unresolved")
    # --- C7.6-refine: every winding cell is settled by the gap-respecting refinement (dissolved or persists)
    check("C7.6-refine", all(rf["status"] in ("dissolved", "persists") for _, _, rf in zeros),
          f"{sum(rf['status'] == 'dissolved' for _, _, rf in zeros)} dissolved, {sum(rf['status'] == 'dissolved-weak' for _, _, rf in zeros)} dissolved-weak (sub-cell K below the parent's), {sum(rf['status'] == 'persists' for _, _, rf in zeros)} persist, "
          f"{sum(rf['status'] == 'unresolved' for _, _, rf in zeros)} unresolved")
    # --- C7.6-Kdep / C7.6-newton-floor: on every persisting cell, the winding is K-independent above the
    #     branch's rank, and Newton on the tabulation converges or stalls at the floor (record 051 (12.2))
    for n, parent, rf in zeros:
        if rf["status"] != "persists":
            continue
        _, (a, b, c, d), K_leaf, _ = rf["cells"][0]
        rf["K"] = K_leaf
        zc = complex(0.5 * (a + b), 0.5 * (c + d))
        rows = []
        for side, cell in ((b - a, (a, b, c, d)), (4 * (b - a), (zc.real - 2 * (b - a), zc.real + 2 * (b - a), zc.imag - 2 * (b - a), zc.imag + 2 * (b - a))), (1.0, parent)):
            for K in range(rf["K"] - 2, rf["K"] + 1):
                r = count_cell(sc, n, *cell, K=K, h0=side / 8)
                rows.append((side, K, r["wind"], r["status"], round(r["gap"], 2)))
        okrows = [r for r in rows if r[3] == "ok"]
        print(f"        K-dependence n={n} at {zc:.4f}: (side, K, wind, status, gap) = {rows}")
        check(f"C7.6-Kdep[n={n},{zc:.2f}]", len(okrows) >= 3 and len({r[2] for r in okrows}) == 1,
              f"winding {sorted({r[2] for r in okrows})} on every gap-respecting (side, K) pair, {len(okrows)} of {len(rows)}")
        tr = BranchTracker(tab, nodes, n)
        nf = newton_floor(tr, zc, rf["K"])
        print(f"        tabulation Newton n={n}: {nf['status']}, final {nf['s']:.6f}, max distance {nf['dist']:.3f}, |mu|/max {min(nf['mu_rel']):.1e}-{max(nf['mu_rel']):.1e}, iota {min(nf['iota']):.2f}-{max(nf['iota']):.2f}, steps {[f'{x:.1e}' for x in nf['steps']]}")
        check(f"C7.6-newton-floor[n={n},{zc:.2f}]", nf["status"] in ("converged", "floor"),
              f"Newton on the tabulation: {nf['status']} (converged, or stalled at the double-precision floor within 0.05)")
    # --- C7.6-direct: the candidate by direct evaluation (no tabulation) on both designs (record 051 (12.6))
    centre, half, n_side = C6C_DIRECT
    designs = ((nodes["n_r"], nodes["lam"], nodes["n_th"]), C6C_DESIGN2)
    winds = {}
    for des in designs:
        cache = Path(f"output/c6d-direct-{des[0]}.npz")
        dc = direct_contour(des, centre, half, n_side, workers, cache)
        dw = direct_windings(dc)
        okK = [K for K in range(8, 14) if dw[K]["ok"]]
        winds[des] = {K: dw[K]["wind"] for K in okK}
        print(f"    direct contour {des} ({dc['source']}): ladder |mu_(k)|/max at interior samples k=6..13 {np.array2string(dw['ladder'][6:14], precision=2)}")
        for K in range(8, 14):
            print(f"      K={K}: wind {dw[K]['wind']} (resid {dw[K]['resid']:.1e}, max dphi {dw[K]['dphi_max']:.2f}), gap {dw[K]['gap']:.2f}, min |mu_(K-1)|/max {dw[K]['rel']:.1e}, {'ok' if dw[K]['ok'] else 'gapfail/stepfail'}")
        check(f"C7.6-direct[{des[0]}]", len(okK) >= 2 and len(set(winds[des].values())) == 1,
              f"winding {sorted(set(winds[des].values()))} of d_K on the side-{2 * half:.4g} contour around {centre}, gap-respecting K in {okK}")
        if des == designs[0]:
            dwp = direct_windings(dc, Ks=(max(okK),), plant=centre) if okK else None
            check("BREAK-C7.6-direct-plant", dwp is not None and dwp[max(okK)]["wind"] == dw[max(okK)]["wind"] + 1,
                  f"planted (s - centre): winding {dwp[max(okK)]['wind'] if dwp else None} (unplanted {dw[max(okK)]['wind'] if okK else None}) at K={max(okK) if okK else None}")
    w0 = set(winds[designs[0]].values())
    w1 = set(winds[designs[1]].values())
    check("C7.6-direct-stable", len(w0) == 1 and w0 == w1,
          f"direct windings {sorted(w0)} on {designs[0]} and {sorted(w1)} on {designs[1]}: the count is design-stable")
    # --- 18c.6e (record 051 (12.9)-(12.11)): interior grid, analytic-derivative Newton, the four cells
    grid = Path("output/c6e-grid-56.npz")
    if grid.exists():
        g = np.load(grid)
        mods = np.array([np.sort(np.abs(np.linalg.eigvals(M)))[::-1] for M in g["M0"]])
        rel = mods / mods[:, :1]
        gap11, gap13 = mods[:, 10] / mods[:, 11], mods[:, 12] / mods[:, 13]
        near = np.argmin(np.abs(g["s"] - complex(g["centre"])))
        others = np.ones(len(g["s"]), bool)
        others[near] = False
        min_kset = rel[:, :13].min()
        print(f"    interior grid ({len(g['s'])} points, spacing {2 * float(g['half']) / (int(g['n']) - 1):.4f}): gap11 at the moment point {gap11[near]:.2f}, elsewhere min {gap11[others].min():.2f}; "
              f"gap13 {gap13[near]:.2f} / {gap13[others].min():.2f}; smallest of the K=13 set over the grid {min_kset:.2e} |mu_(0)|, rank-13 ladder elsewhere {rel[others, 13].min():.1e}-{rel[others, 13].max():.1e}")
        check("C7.6-grid", min_kset > 5e-12 and gap11[near] < 2 and gap13[near] < 2 and gap11[others].min() >= 3 and gap13[others].min() >= 3,
              "no eigenvalue of the K-set dips below 5e-12 |mu_(0)| on the grid (no zero), and the gaps gamma_11, gamma_13 collapse below 2 at the moment point only (exceptional-point island of (12.1)(ii), record 051 (12.9))")
    else:
        check("C7.6-grid", False, f"{grid} missing")
    # analytic tile derivative (12.10a) against a centred difference, on the reduced design (formula check)
    des_r = (16, 8.0, 24)
    s_chk = complex(3.224, 9.462)
    M_a, dM_a = direct_M_dM(s_chk, des_r)
    h = 1e-4
    dM_c = (_direct_job((s_chk + h, des_r))[1] - _direct_job((s_chk - h, des_r))[1]) / (2 * h)
    err = np.abs(dM_a - dM_c).max() / np.abs(dM_a).max()
    lf_a, lf_c = logdet_deriv(M_a, dM_a, 13), logdet_deriv(M_a, dM_c, 13)
    check("C7.6-newton-analytic", err < 1e-7 and abs(lf_a - lf_c) / abs(lf_a) < 1e-3,
          f"analytic M'(s) vs centred difference h={h} on {des_r} at {s_chk}: entrywise {err:.1e}, (log d_13)' rel {abs(lf_a - lf_c) / abs(lf_a):.1e} (record 051 (12.10))")
    # BREAK: Newton with the analytic derivative on d_4 (s - s_p), planted at a regular point, must converge
    s_p = complex(-10.3, 5.7)
    s_it, steps = s_p + 0.02 + 0.01j, []
    for _ in range(8):
        if abs(s_it - s_p) < 1e-12:  # landed on the planted zero exactly
            break
        M_i, dM_i = direct_M_dM(s_it, des_r)
        lf = logdet_deriv(M_i, dM_i, 4) + 1.0 / (s_it - s_p)
        step = -1.0 / lf
        s_it += step
        steps.append(abs(step))
        if abs(step) < 1e-10:
            break
    check("BREAK-C7.6-newton-plant", abs(s_it - s_p) < 1e-8 and len(steps) <= 6,
          f"planted zero at {s_p}: analytic-derivative Newton on d_4 (s - s_p) reaches |s - s_p| = {abs(s_it - s_p):.1e} in {len(steps)} steps")
    # the four undecided parent cells (12.11): direct evaluation on the parent contour, gap-respecting K >= 9
    cells = (("-1.5-9.5", 0), ("3.5-19.5", 0), ("3.5-31.5", 0), ("-1.5-20.5", 2))
    for tag, n in cells:
        f = Path(f"output/c6e-cell-{tag}.npz")
        if not f.exists():
            check(f"C7.6-cells-direct[n={n},{tag}]", False, f"{f} missing (job not finished)")
            continue
        d = np.load(f)
        dc = {"s": d["s"], "M0": d["M0"] if n == 0 else d["M2"], "n_cont": int(d["n_cont"])}
        dw = direct_windings(dc, Ks=range(9, 14))
        okK = [K for K in range(9, 14) if dw[K]["ok"]]
        print(f"    cell {tag} n={n}: " + "; ".join(f"K={K}: wind {dw[K]['wind']} gap {dw[K]['gap']:.2f} dphi {dw[K]['dphi_max']:.2f} {'ok' if dw[K]['ok'] else 'fail'}" for K in range(9, 14)))
        check(f"C7.6-cells-direct[n={n},{tag}]", len(okK) >= 1 and all(dw[K]["wind"] == 0 for K in okK),
              f"winding {[dw[K]['wind'] for K in okK]} of d_K on the direct parent contour at gap-respecting K in {okK} (dissolved if all 0)")
    print(f"  c6c wall {time.time() - t_all:.0f} s; evaluations in the main process {sc.n_eval}")


# Tile derivatives of record 051 (12.10a): (p', q') per type I, II, III (alpha' = 1).
_DP = np.array([0.25, -0.25, -0.25])
_DQ = np.array([-0.25, 0.25, -0.25])


def direct_M_dM(s: complex, design: tuple, n2d: int = 60) -> tuple[np.ndarray, np.ndarray]:
    """
    M^(0)(s) and its analytic s-derivative by direct evaluation (record 051 (12.10a)).

    dJ/ds = int (p' ln|Z| + q' ln|1-Z|) |Z|^p |1-Z|^q d^2Z on the smooth 2D rule (one exp per node);
    F' = -(ln beta / 2) F + 2 beta^{8 - S/2} sum_X J_X'.
    """
    nodes = design_nodes(*design)
    t, u = nodes["t"], nodes["u"]
    ss = s * np.ones_like(t, dtype=complex)
    tiles = [[(ss, t, u), (ss, u, t)], [(t, ss, u), (u, ss, t)], [(t, u, ss), (u, t, ss)]]
    lz, lo, w = _rule_2d_smooth(2.0, n2d)
    J = np.zeros((3, t.size), dtype=complex)
    dJ = np.zeros((3, t.size), dtype=complex)
    for k in range(3):
        for x, y, z in tiles[k]:
            p, q = ALPHA_P * (x - y - z) / 4, ALPHA_P * (y - x - z) / 4
            for a in range(0, p.size, 512):
                sl = slice(a, a + 512)
                E = np.exp(p[sl, None] * lz[None, :] + q[sl, None] * lo[None, :])
                J[k, sl] += E @ w
                dJ[k, sl] += E @ (ALPHA_P * (_DP[k] * lz + _DQ[k] * lo) * w)
    pref = 2.0 * np.exp((8.0 - ALPHA_P * (s + t + u) / 2.0) * math.log(2.0))
    fv = pref * J.sum(0)
    dfv = -(ALPHA_P * math.log(2.0) / 2) * fv + pref * dJ.sum(0)
    return matrices_from_entries(fv, nodes)[0], matrices_from_entries(dfv, nodes)[0]


def logdet_deriv(M: np.ndarray, dM: np.ndarray, K: int) -> complex:
    """(log d_K)' = sum_{k<K} lambda_k^T M' lambda_k / (lambda_k^T lambda_k mu_k), record 051 (12.10b)."""
    ev, V = np.linalg.eig(M)
    o = np.argsort(-np.abs(ev))[:K]
    return complex(sum((V[:, j] @ dM @ V[:, j]) / (V[:, j] @ V[:, j]) / ev[j] for j in o))


def tabulate_full(design: tuple, out: Path, workers: int) -> None:
    """Write the full tabulation (record 051 Block 10) to ``out`` (.npz)."""
    n_r, lam, n_th = design
    nodes = design_nodes(n_r, lam, n_th)
    print(f"full tabulation: beta = 2, design {design}, {nodes['t'].size} node triples -> {out}")
    tab = tabulate(nodes, 2.0, N_ELL, workers)
    np.savez_compressed(
        out, a=tab["a"], beta=2.0, cX=tab["cX"], h=tab["h"], r=tab["r"], n_ell=N_ELL,
        centres=tab["centres"], half=PANEL_HALF, A=ELL_A, B=ELL_B, design=np.array(design),
        rho=nodes["rho"], wr=nodes["wr"], xp=nodes["xp"], wp=nodes["wp"], t=nodes["t"], u=nodes["u"],
        shape=np.array(nodes["shape"]), im_max=tab["im_max"], wall=tab["wall"],
    )
    print(f"written {out}; max |Im a_k|/max|a_k| = {tab['im_max']:.2e}; wall {tab['wall']:.0f} s")


# ---------------------------------------------------------------------------------------------
# group c6f – record 051 (12.13)-(12.17): zero vs exceptional point by branch continuation
# ---------------------------------------------------------------------------------------------
def _eig_sorted(m: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    w, V = np.linalg.eig(m)
    o = np.argsort(-np.abs(w))
    return w[o], V[:, o] / np.linalg.norm(V[:, o], axis=0)


def loop_monodromy(Ms: list, nb: int = 18) -> tuple[np.ndarray, np.ndarray, float]:
    """
    Continue the nb leading eigen-branches along a closed loop of matrices by eigenvector overlap.

    Branches are matched between neighbours by maximal |v^H v'| (Hungarian assignment), not by modulus
    rank (record 051 (12.13)).  Returns the continued values (n_pts x nb), the monodromy permutation
    (start label -> label reached after one turn) and the smallest matched overlap.

    """
    from scipy.optimize import linear_sum_assignment

    w0, V0 = _eig_sorted(Ms[0])
    vals, Vp, mo = [w0[:nb]], V0[:, :nb], 1.0
    for m in Ms[1:]:
        w, V = _eig_sorted(m)
        C = np.abs(Vp.conj().T @ V[:, : nb + 4])
        r, c = linear_sum_assignment(-C)
        mo = min(mo, float(C[r, c].min()))
        vals.append(w[c])
        Vp = V[:, c]
    perm = np.abs(V0[:, :nb].conj().T @ Vp).argmax(axis=1)
    return np.array(vals), perm, mo


def loop_classify(Ms: list, K: int) -> tuple[list, float]:
    """(moved labels < K, winding of the product of the K continued leading branches) on a closed loop."""
    vals, perm, _ = loop_monodromy(Ms)
    ph = np.unwrap(np.angle(np.prod(vals[:, :K], axis=1)))
    return [b for b in range(K) if perm[b] != b], float((ph[-1] - ph[0]) / (2 * np.pi))


def _toy_family(s: complex, kind: str) -> np.ndarray:
    """Complex-symmetric 8x8 ladder family: 'zero' (branch 4 = 1e-4 (s - s0)) or 'ep' (2x2 block with EPs)."""
    rng = np.random.default_rng(7)
    Q, _ = np.linalg.qr(rng.normal(size=(8, 8)))  # real orthogonal: Q^T D Q complex symmetric, spectrum of D
    lam = np.array([10.0 ** (-k) for k in range(8)], dtype=complex) * (1 + 0.1 * s)
    D = np.diag(lam)
    if kind == "zero":
        D[4, 4] = 1e-4 * (s - 0.01 - 0.02j)
    elif kind == "ep":  # eigenvalues 1e-4 [1.5 +- sqrt(0.25 + (s/0.02)^2)]: EPs at s = +-0.01 i
        D[4:6, 4:6] = 1e-4 * np.array([[2.0, s / 0.02], [s / 0.02, 1.0]])
    return Q.T @ D @ Q


def group_c6f() -> None:  # noqa: PLR0915
    """
    Record 051 (12.13)-(12.17): the candidate at 3.224+9.462i by continuation (cached direct matrices).

    Checks: C7.6-ladder (no extra rung: the count of eigenvalues per decade is constant over the 34 stored
    points), C7.6-monodromy[coarse|fine] (non-trivial monodromy = branch points inside; winding of the
    continued head set), C7.6-ep-separation (smallest relative separation over ranks 0-13 at the stored
    points), C7.6-newton-branch (cached Newton logs: convergence yes/no), BREAK-C7.6-deflate (a real
    branch deflated to zero at a grid point: trivial monodromy change, winding +1, a rung at the floor),
    BREAK-C7.6-planted-ep / BREAK-C7.6-toy-zero (analytic toy families: EP -> swap and winding 0; zero ->
    no swap and winding 1).  Not checked: the tail ranks >= 15 (below the double-precision floor).

    """
    sc = _CODES_DIR / "output"
    g = np.load(sc / "c6e-grid-56.npz")
    f = np.load(sc / "c6e-grid-fine-56.npz")
    Mg, Mf = list(g["M0"]), list(f["M0"])
    idx = lambda i, j: 5 * j + i  # noqa: E731
    big = [idx(i, 0) for i in range(5)] + [idx(4, j) for j in range(1, 5)] + [idx(i, 4) for i in range(3, -1, -1)]
    big += [idx(0, j) for j in range(3, 0, -1)] + [idx(0, 0)]
    small = [0, 1, 2, 5, 8, 7, 6, 3, 0]
    # C7.6-ladder: a branch dipping below its rung removes one rung above rank 14 and adds one below, so the
    # rank-14 value drops to the rank-15 level (a decade lower); the regular ladder keeps it within a factor ~3.
    r14 = np.array([np.sort(np.abs(np.linalg.eigvals(m)))[::-1][14] / np.abs(np.linalg.eigvals(m)).max() for m in Mg + Mf])
    check("C7.6-ladder", bool(r14.max() / r14.min() < 5),
          f"|mu_(14)|/mu0 over the 34 stored points in [{r14.min():.2e}, {r14.max():.2e}] (ratio {r14.max() / r14.min():.1f} < 5)")
    for tag, Ms, loop in (("coarse", Mg, big), ("fine", Mf, small)):
        vals, perm, mo = loop_monodromy([Ms[k] for k in loop])
        moved = [b for b in range(15) if perm[b] != b]
        ph = np.unwrap(np.angle(np.prod(vals[:, :14], axis=1)))
        w = (ph[-1] - ph[0]) / (2 * np.pi)
        check(f"C7.6-monodromy[{tag}]", bool(moved) and abs(w - 1) < 0.1,
              f"moved {moved} -> {[int(perm[b]) for b in moved]}, winding of continued ranks 0-13 {w:+.3f}, "
              f"min overlap {mo:.2f} (PASS = non-trivial monodromy AND winding 1)")
    seps = []
    for m in Mg + Mf:
        ev = _eig_sorted(m)[0][:14]
        D = np.abs(ev[:, None] - ev[None, :]) / np.abs(ev)[:, None]
        np.fill_diagonal(D, np.inf)
        seps.append(D.min())
    check("C7.6-ep-separation", True, f"min relative separation over ranks 0-13 at 34 points: {min(seps):.2f} "
          "(no sampled point within the sqrt-neighbourhood of an EP; data, not a pass condition)")
    conv = {}
    for name in ("branch", "d9", "d12"):
        p = sc / f"c6f-newton-{name}.log"
        steps = [float(x.split("|ds|=")[1].split()[0]) for x in p.read_text().splitlines() if "|ds|=" in x] if p.exists() else []
        conv[name] = (len(steps), steps[-1] if steps else np.nan, bool(steps) and steps[-1] < 1e-6)
    check("C7.6-newton-branch", all(n >= 3 for n, _, _ in conv.values()),
          "; ".join(f"{k}: {n} it, last |ds| {d:.1e}, converged {c}" for k, (n, d, c) in conv.items()))
    # BREAK-C7.6-deflate: deflate the rank-6 branch of the moment point (grid index 12) at every grid point
    w12, V12 = _eig_sorted(Mg[12])
    v = V12[:, 6]
    P = w12[6] * np.outer(v, v) / (v @ v)
    Mp = [m - P for m in Mg]
    r12 = np.abs(np.linalg.eigvals(Mp[12]))
    _, wdef = loop_classify([Mp[k] for k in big], 14)
    _, wref = loop_classify([Mg[k] for k in big], 14)
    check("BREAK-C7.6-deflate", r12.min() / r12.max() < 1e-13 and abs(wdef - wref - 1) < 0.1,
          f"deflated: smallest |mu| at s_p {r12.min() / r12.max():.1e} mu0, winding ranks 0-13 {wref:+.2f} -> {wdef:+.2f}")
    ts = np.exp(2j * np.pi * np.arange(33) / 32)
    mv_z, w_z = loop_classify([_toy_family(0.01 + 0.02j + 0.005 * t, "zero") for t in ts], 8)
    mv_e, w_e = loop_classify([_toy_family(0.01j + 0.005 * t, "ep") for t in ts], 8)
    check("BREAK-C7.6-toy-zero", not mv_z and abs(w_z - 1) < 0.05, f"moved {mv_z}, winding {w_z:+.3f}")
    check("BREAK-C7.6-planted-ep", mv_e == [4, 5] and abs(w_e) < 0.05, f"moved {mv_e}, winding {w_e:+.3f}")


# ---------------------------------------------------------------------------------------------
# group c6g – record 051 (12.19)-(12.23): the candidate in extended precision (double-double M^(0))
# ---------------------------------------------------------------------------------------------
def group_c6g() -> None:  # noqa: PLR0915
    """
    Record 051 (12.19)-(12.23), from the cached DD matrices ``output/c6g-M-*.npy`` (``c6g-mp-direct.py``).

    C7.6-mp-validate: DD M^(0) at the centre against the stored double matrix (entries to 1e-13 relative).
    C7.6-mp-monodromy: 34 continued branches on the fine loop (half-side 1/256): the only non-trivial cycles
    are the 5-cycle of ranks 8-12 (winding +1) and the 13-14 swap (winding 0); ranks 15-33 fixed, winding 0.
    C7.6-mp-det-winding: winding of det M^(0) = det D^2 det K on the fine loop is +1, no sampled phase step is altered
    by a relative 1e-30 entry perturbation: noise < 0.5 and max step + 2 arcsin(noise) < pi (same criterion as
    C7.6.6-r90-winding; fix pass 3; not a sampling certificate, the max step exceeds pi/2).
    C7.6-mp-newton: |det| at the det-fit zero zB is < 0.1 of its value 2e-4 away (zC, zD), the two
    finite-difference derivatives agree (Cauchy-Riemann) to 10%.
    BREAK-C7.6-mp-deflate (re-specified 18c.6h, (12.28)): a zero planted at the loop centre by M - c w w^T, w the
    rank-22 centre eigenvector made bilinearly orthogonal to the pencil null vector v at s** (so the original zero
    stays at s**), must raise the det winding to +2 on the 16-point loop (DD midpoints c6g-M-m*.npy); the
    unorthogonalised plant (the 18c.6g leg) is reported as control (winding 1, original zero pushed out).
    BREAK-C7.6-mp-planted-ep: an EP planted between the centre ranks 12/13 must leave the det winding at +1.
    C7.6-mp-det44 (c6g-det44.py, (12.22)(ii)): on the (44,8,24) design |det| at zB is < 0.02 of its values at
    three points 1e-3 away and the linear-fit zero is within 5e-5 of s*.
    C7.6.5-zero (c6g-iso-check.py, (12.26)): the pencil zero s** from bases s* and zB agrees to 1e-8, the det drop
    |det(s*)|/|det(t)| (t = zC, zD) matches |s**-s*|/|s**-t| to 5%, and every regularisation of (12.27) keeps the
    zero within 1e-6.  C7.6.5-isotropy (INFO line, not tallied; (12.27), undecided form): iota >= 0.5 in every regularisation and the
    null vector is not resolved -- each regularisation's vector has its maximum within 3 nodes of an edge of its node range
    and the [8,56) and [8,50) truncations give different vectors (overlap < 0.1) at the same zero.  A resolved interior null
    vector would fail the second clause.  BREAK-C7.6.5-isotropy-plant: an isotropic null vector planted on the
    [8,56) truncation (M_p = M - y y^T / w^T y, y = M(s_p) w, (12.29)) is returned by the same pipeline with iota < 1e-6
    and overlap > 0.999.
    Not checked: the (44,8,24) design beyond the four points of (12.22); the branch identity of the zero; the
    isotropy of a resolved null function (not available at double-double precision, (12.27)).

    """
    import subprocess

    sc = _CODES_DIR / "output"
    py = sys.executable
    run = lambda *a: subprocess.run([py, *a], cwd=sc, capture_output=True, text=True, check=False).stdout  # noqa: E731
    Mref = np.load(sc / "c6e-grid-fine-56.npz")["M0"][4]
    A = np.load(sc / "c6g-M-f4.npy")
    parse = lambda x: complex(x.replace(" ", "").strip("()"))  # noqa: E731
    Md = np.array([[parse(x) for x in row] for row in A])
    dev = np.abs(Md - Mref).max() / np.abs(Mref).max()
    check("C7.6-mp-validate", dev < 1e-13, f"max relative entry difference DD vs double at 3.224+9.462i: {dev:.1e}")
    loop = ["f0", "f1", "f2", "f5", "f8", "f7", "f6", "f3", "f0"]
    out = run("c6g-analyse.py", "34", *loop)
    cyc = [ln for ln in out.splitlines() if ln.startswith("cycle")]
    nontriv = [ln for ln in cyc if "," in ln.split(":")[0]]
    w5 = [ln for ln in cyc if ln.startswith("cycle [8, 9, 11, 12, 10]")]
    tailw = [ln for ln in cyc if int(ln.split("[")[1].split("]")[0].split(",")[0]) >= 15]
    ok = len(nontriv) == 2 and bool(w5) and "+1.000" in w5[0] and all("+0.000" in ln or "-0.000" in ln for ln in tailw) and len(tailw) == 19
    check("C7.6-mp-monodromy", ok, f"non-trivial cycles {[ln.split(':')[0] for ln in nontriv]}; 5-cycle {w5[0].split(':')[1].strip() if w5 else '-'}; "
          f"ranks 15-33 fixed with winding 0: {len(tailw)} branches")
    out = run("c6g-plantdet.py")
    wind = {ln.split(":")[0]: float(ln.split("winding of det ")[1].split(",")[0]) for ln in out.splitlines() if "winding of det" in ln}
    steps = {ln.split(":")[0]: eval(ln.split("phase steps ")[1]) for ln in out.splitlines() if "phase steps" in ln}  # noqa: S307
    out2 = run("c6g-det.py", *loop)
    noise = [float(ln.split("noise ")[1].split()[0]) for ln in out2.splitlines() if "noise" in ln]
    # same criterion as C7.6.6-r90-winding ((13.6)): no sampled phase step is altered by the 1e-30 entry noise,
    # max step + 2 arcsin(noise) < pi (a relative change eps < 1 moves a phase by at most arcsin(eps)); not a sampling certificate
    mstep = max(map(abs, steps.get("none", [9])))
    check("C7.6-mp-det-winding", abs(wind.get("none", 0) - 1) < 1e-6 and max(noise) < 0.5 and mstep + 2 * math.asin(max(noise)) < math.pi,
          f"winding of det M^(0) on the fine loop {wind.get('none')}, max phase step {mstep:.2f}, "
          f"max relative det change under 1e-30 entry noise {max(noise):.3f} (step + 2 arcsin(noise) < pi)")
    import pickle

    tags = ["f0", "f1", "f2", "f5", "f8", "f7", "f6", "f3", "f4", "nA", "zA", "g0", "g1", "g2", "g3", "zB", "zC", "zD"]
    run("c6g-det.py", *tags)
    dd = {o[0]: o[1] for o in pickle.load(open(sc / "c6g-det-f0-18.pkl", "rb"))}  # noqa: SIM115
    sB, sC, sD = 3.223106 + 9.464523j, 3.223306 + 9.464523j, 3.223106 + 9.464723j
    dx, dy = (dd["zC"] - dd["zB"]) / (sC - sB), (dd["zD"] - dd["zB"]) / (sD - sB)
    s1 = sB - dd["zB"] / ((dx + dy) / 2)
    r = max(abs(dd["zB"]) / abs(dd["zC"]), abs(dd["zB"]) / abs(dd["zD"]))
    check("C7.6-mp-newton", r < 0.1 and abs(dx - dy) / abs(dx) < 0.1,
          f"|det(zB)|/|det(zC,zD)| <= {r:.3f}; Cauchy-Riemann mismatch {abs(dx - dy) / abs(dx):.3f}; Newton zero s* = {s1:.6f} "
          f"(step {abs(s1 - sB):.1e})")
    out3 = run("c6g-deflate2.py", "16")
    dfl = {ln.split()[1].rstrip(":"): ln for ln in out3.splitlines() if ln.startswith("deflate2 orth") or ln.startswith("deflate2 plain")}
    w_or = float(dfl["orth"].split("winding ")[1].split()[0]) if "orth" in dfl else float("nan")
    st_or = float(dfl["orth"].split("max|step| ")[1].split()[0]) if "orth" in dfl else float("nan")
    rz_or = float(dfl["orth"].split("|det_p(zS)|/|det_p(zC)|=")[1].split()[0]) if "orth" in dfl else float("nan")
    w_pl = float(dfl["plain"].split("winding ")[1].split()[0]) if "plain" in dfl else float("nan")
    rz_pl = float(dfl["plain"].split("|det_p(zS)|/|det_p(zC)|=")[1].split()[0]) if "plain" in dfl else float("nan")
    check("BREAK-C7.6-mp-deflate", abs(w_or - 2) < 1e-3 and st_or < 2.5 and rz_or < 0.01,
          f"orthogonal plant, 16-point loop: det winding {w_or:+.3f} (max step {st_or:.2f}), original zero kept "
          f"(|det_p(s*)|/|det_p(zC)| = {rz_or:.1e}); control, unorthogonalised plant (18c.6g leg): winding {w_pl:+.3f}, "
          f"ratio {rz_pl:.2f} (original zero pushed out, (12.22)(iii))")
    out4 = run("c6g-det44.py")
    fit = [ln for ln in out4.splitlines() if ln.startswith("linear fit")]
    if fit:
        root = complex(fit[0].split("predicted zero ")[1].split(" ;")[0].strip("()").replace(" ", ""))
        rat = [float(x) for x in __import__("re").findall(r"\d*\.\d+(?:e[-+]?\d+)?", fit[0].split("=")[1].split(";")[0])]
    else:
        root, rat = complex("nan"), [float("nan")]
    check("C7.6-mp-det44", max(rat) < 0.02 and abs(root - (3.223113 + 9.464523j)) < 5e-5,
          f"(44,8,24): |det(zB)|/|det(3 points 1e-3 away)| = {[round(x, 4) for x in rat]}; linear-fit zero {root:.6f} "
          f"({abs(root - (3.223113 + 9.464523j)):.1e} from s*)")
    out5 = run("c6g-iso-check.py")
    L = out5.splitlines()
    z0 = [ln for ln in L if ln.startswith("zero s**")]
    dd_ = [ln for ln in L if ln.startswith("zero detdrop")]
    rg = [ln for ln in L if ln.startswith("reg ")]
    rov = [float(ln.split()[-1]) for ln in L if ln.startswith("regov")]
    pl = [ln for ln in L if ln.startswith("plant")]
    ok_z = bool(z0) and float(z0[0].split("=")[-1]) < 1e-8 and len(dd_) == 2 and all(
        abs(float(ln.split("ratio=")[1].split()[0]) / float(ln.split("pred=")[1]) - 1) < 0.05 for ln in dd_) and len(rg) == 5 and all(
        float(ln.split("|s**-s**full|=")[1].split()[0]) < 1e-6 for ln in rg)
    check("C7.6.5-zero", ok_z, f"{z0[0][5:] if z0 else '-'}; det drop vs pencil: "
          f"{[(ln.split('ratio=')[1].split()[0], ln.split('pred=')[1]) for ln in dd_]}; max regularisation shift "
          f"{max(float(ln.split('|s**-s**full|=')[1].split()[0]) for ln in rg) if rg else float('nan'):.1e}")
    io = [float(ln.split("iota=")[1].split()[0]) for ln in rg]
    edge = []
    for ln in rg:
        am = int(ln.split("argmax=")[1].split()[0]); lo_, hi_ = map(int, ln.split("range=")[1].split("-"))
        edge.append(min(am - lo_, hi_ - 1 - am) <= 3)
    ok_i = len(io) == 5 and min(io) >= 0.5 and all(edge) and len(rov) == 3 and rov[0] < 0.1
    # INFO line (fix pass 3): a sentinel on the [GAP] of C7.6.4, not a test of a claim; printed, not tallied
    print(f"[INFO] C7.6.5-isotropy  (sentinel flag {'set' if ok_i else 'NOT set'})  undecided form: iota over the regularisations {[round(x, 4) for x in io]} (min >= 0.5: no isotropy "
          f"seen); argmax within 3 nodes of the range edge {edge}; overlaps [8,56)/[8,50), [8,56)/head46, [8,50)/head46 "
          f"{[f'{x:.1e}' for x in rov]} (first < 0.1: the vector follows the edge, not resolved)")
    if pl:
        ip = float(pl[0].split("iota=")[1].split()[0]); op = float(pl[0].split("overlap(v,w)=")[1].split()[0])
        dp = float(pl[0].split("|s**-s_p|=")[1].split()[0])
    else:
        ip, op, dp = float("nan"), float("nan"), float("nan")
    check("BREAK-C7.6.5-isotropy-plant", ip < 1e-6 and op > 0.999 and dp < 1e-8,
          f"planted isotropic null vector: returned iota {ip:.1e}, overlap {op:.6f}, |s**-s_p| {dp:.1e}")
    check("BREAK-C7.6-mp-planted-ep", abs(wind.get("ep", 0) - 1) < 1e-6,
          f"det winding with an EP planted at the centre: {wind.get('ep')} (EP adds no zero -> 1)")


# ---------------------------------------------------------------------------------------------
# group c6j – record 051 Block 13 (13.1)-(13.x): the zero s** under n2d = 60 -> 90 and Lambda = 8 -> 10
# ---------------------------------------------------------------------------------------------
C6J_SREF = 3.2231132495 + 9.4645233020j  # (12.26), design (56,8,24), n2d = 60
C6J_TOL = 1e-6  # "the zero stays": the scale of the n_r and regularisation shifts, 2.8e-7 / 3.6e-7 ((12.26)-(12.27))
C6J_PLANT = 1e-5  # planted shift of the break leg, ten times C6J_TOL


def _c6j_stays(res: dict, bases=("zS", "zC", "zD")) -> tuple[bool, str]:
    """Position test of C7.6.6: the pencil bases agree to 1e-7 and s**(base zS) is within C6J_TOL of C6J_SREF."""
    pen = res.get("pencil", {})
    if any(b not in pen for b in bases):
        return False, "pencil missing"
    s = {b: complex(pen[b]["s"]) for b in bases}
    spread = max(abs(s[b] - s["zS"]) for b in s)
    shift = abs(s["zS"] - C6J_SREF)
    conv = pen["zS"]["conv"]
    ok = spread < 1e-7 and shift < C6J_TOL and conv < 1e-12
    return ok, f"s** = {s['zS']:.10f}, shift from (12.26) {shift:.2e}, spread over bases {list(bases)} {spread:.1e}, conv {conv:.0e}"


def group_c6j() -> None:  # noqa: PLR0915
    """
    Record 051 Block 13: the deciding tests for the location of the det zero s** of M^(0) (critic-051 iter. 2 #3, #4).

    Reads the DD matrices ``output/c6j-M-{r90,L10}-<tag>.npy`` (``c6j-mp.py``: set r90 = design (56,8,24)
    with the 2D rule n2d = 90; set L10 = design (70,10,24), n2d = 60) and the reference ``c6g-M-<tag>.npy``
    ((56,8,24), n2d = 60), at the fine loop f0..f8 (half-side 1/256 about 3.224+9.462i) and the pencil points
    zS, zC, zD of (12.26); runs ``c6j-analyse.py`` (pencil (12.25) at dps 60, det by elimination, winding of
    det M on the fine loop, the (12.27)(b) truncation line), ``c6j-noise.py`` and ``c6j-head.py`` (determinant
    compressed on the m leading eigenvectors of M(f4)) and reads their ``c6j-*.pkl`` / output.

    C7.6.6-rule-applied: the r90 entries at f4 and zS differ from the n2d = 60 ones by more than 1e-20 relative
    (max) -- the rule change is actually applied, far above the DD rounding -- and by less than 1e-11 ((13.3)).
    C7.6.6-r90-position: the pencil zero from the three bases zS, zC, zD agrees to 1e-7, base zS converged, and lies
    within C6J_TOL = 1e-6 of s** (12.26).  C7.6.6-r120-position ((13.9), ``c6j-mixed.py``): one DD matrix at zS with
    n2d = 120, M'(zS) from the n2d = 60 set; the zero within C6J_TOL of s** (12.26), the same construction on r90
    reproducing its three-point zero to 1e-9.  C7.6.6-r90-detdrop (independent of the pencil): |det M(zS)|/|det M(t)|,
    t = zC, zD, equals the pencil's |s**-zS|/|s**-t| to 5 %.  C7.6.6-r90-winding: det M^(0) winds +1 on the fine
    loop, no sampled step altered by the noise (relative change < 0.5 under a relative 1e-30 entry
    perturbation and max step + 2 arcsin(change) < pi; set after the 0.21 was measured, (13.6); not a sampling
    certificate).
    C7.6.6-L10-design: the L10 matrices are 70 x 70.  C7.6.6-L10-resolution ((13.4)(ii)): det K is resolved at DD
    on r90 (1e-30 noise response < 0.5) and not on L10 (> 10) -- the reason the L10 position rests on base zS and
    the L10 count on the compressed determinant.  C7.6.6-L10-position: the base-zS pencil zero converged, within
    C6J_TOL of s** (12.26), within 1e-7 of the nS = 9 truncated zero, and moved < 1e-7 by entry noise 1e-30..1e-25
    and by the choice of M' (``c6j-noise.py``).  C7.6.6-head-control: on the n2d = 60 reference the compressed
    determinant g_m (m = 29, 33, 37, 41) winds +1 on the fine loop, noise response < 1e-3, and its pencil zero
    converges to the full zero (12.26) (distances strictly decreasing in m, last < 5e-7).  C7.6.6-L10-head: on L10,
    g_m winds +1 for m = 29, 33, 37, 41, 45 (noise response < 1e-3; the count of g_m, which is the count of det M
    only if the tail Schur complement carries no net zero in the square -- shown on r90 only) and the m = 45 compressed pencil zero is within 5e-7 of
    the full L10 zero.  BREAK-C7.6.6-plant-shift: the r90 matrices with a planted shift M_p(s) = M(s) + DELTA M'_fd
    (DELTA = 1e-5, the zero moved by ~ -DELTA) must fail the position test and return the shift to 10 %.
    Informational (no assertion): the isotropy line of (12.27)(b) on each set -- iota and the node of the maximum
    of the truncated pencil vector (edge localisation).
    Not checked: the isotropy of a resolved null function (not available at DD precision); n2d > 90 in DD; Lambda > 10;
    the full-determinant count at Lambda = 10 (not resolved at DD).

    """
    import pickle
    import subprocess

    import mpmath as mpm

    sc = _CODES_DIR / "output"
    py = sys.executable

    def run(*a: str) -> str:
        return subprocess.run([py, *a], cwd=sc, capture_output=True, text=True, check=False).stdout

    def analyse(*a: str) -> dict:
        run("c6j-analyse.py", *a)
        tag = a[0] + ("-plant" if "--plant" in a else "")
        p = sc / f"c6j-res-{tag}.pkl"
        return pickle.load(open(p, "rb")) if p.exists() else {}  # noqa: SIM115

    def parse_mp(path: Path) -> list:
        mpm.mp.dps = 40
        out = []
        for row in np.load(path):
            for x in row:
                x = x.strip("()").replace(" ", "")
                k = max(k for k in range(1, len(x)) if x[k] in "+-" and x[k - 1] != "e")
                out.append(mpm.mpc(x[:k], x[k:-1]))
        return out

    devs = []
    for t in ("f4", "zS"):
        a, b = sc / f"c6j-M-r90-{t}.npy", sc / f"c6g-M-{t}.npy"
        if a.exists() and b.exists():
            ea, eb = parse_mp(a), parse_mp(b)
            devs.append(float(max(abs(x - y) / abs(y) for x, y in zip(ea, eb, strict=True) if y != 0)))
    check("C7.6.6-rule-applied", len(devs) == 2 and min(devs) > 1e-20 and max(devs) < 1e-11,
          f"max relative entry difference n2d 90 vs 60 (DD) at f4, zS: {[f'{x:.2e}' for x in devs]}")
    res = {k: analyse(k) for k in ("r90", "L10")}
    ok, msg = _c6j_stays(res["r90"])
    check("C7.6.6-r90-position", ok, msg)
    dd = res["r90"].get("detdrop", {})
    check("C7.6.6-r90-detdrop", len(dd) == 2 and all(abs(r / p - 1) < 0.05 for r, p in dd.values()),
          "; ".join(f"|det(zS)|/|det({t})| = {r:.3e} vs pencil {p:.3e}" for t, (r, p) in dd.items()))
    w = res["r90"].get("winding", {})
    # bound of (13.6): a relative change eps < 1 moves a phase by at most arcsin(eps), so no sampled step is altered
    # by the noise if max step + 2 arcsin(noise) < pi (same criterion as C7.6-mp-det-winding in c6g)
    check("C7.6.6-r90-winding", bool(w) and abs(w["w"] - 1) < 1e-6 and w["noise"] < 0.5 and w["max_step"] + 2 * math.asin(w["noise"]) < math.pi,
          f"winding {w.get('w', float('nan')):+.4f}, max phase step {w.get('max_step', float('nan')):.2f}, "
          f"1e-30 noise response {w.get('noise', float('nan')):.3f}")
    n10 = np.load(sc / "c6j-M-L10-zS.npy").shape[0] if (sc / "c6j-M-L10-zS.npy").exists() else 0
    check("C7.6.6-L10-design", n10 == 70, f"L10 matrix dimension {n10}")
    w10 = res["L10"].get("winding", {})
    check("C7.6.6-L10-resolution", bool(w) and bool(w10) and w["noise"] < 0.5 and w10["noise"] > 10,
          f"1e-30 noise response of det K on the fine loop: r90 {w.get('noise', float('nan')):.2e} (resolved), "
          f"L10 {w10.get('noise', float('nan')):.2e} (not resolved; L10 full-det winding reads {w10.get('w', float('nan')):+.3f}, "
          f"not used)")
    okz, msgz = _c6j_stays(res["L10"], bases=("zS",))
    tr = res["L10"].get("trunc", {})
    dtr = abs(complex(tr["s"]) - complex(res["L10"]["pencil"]["zS"]["s"])) if tr and res["L10"].get("pencil") else float("nan")
    nz = [float(ln.split("|ds**|=")[1].split()[0]) for ln in run("c6j-noise.py", "L10").splitlines() if "|ds**|=" in ln]
    check("C7.6.6-L10-position", okz and dtr < 1e-7 and len(nz) == 10 and max(nz) < 1e-7,
          f"{msgz}; truncated (nS={tr.get('nS')}) zero {dtr:.1e} away; max shift under noise / choice of M' "
          f"{max(nz) if nz else float('nan'):.1e} over {len(nz)} variants")
    run("c6j-head.py", "g60", "29", "33", "37", "41")
    hg = pickle.load(open(sc / "c6j-head-g60.pkl", "rb")) if (sc / "c6j-head-g60.pkl").exists() else {}  # noqa: SIM115
    # convergence of the compressed zero in m (13.5)(i): distance to the full zero (12.26) strictly decreasing, last < 5e-7
    dg = [abs(hg[m]["s"] - C6J_SREF) for m in (29, 33, 37, 41) if m in hg and "s" in hg[m]]
    conv_m = len(dg) == 4 and all(x > y for x, y in zip(dg, dg[1:], strict=False)) and dg[-1] < 5e-7
    check("C7.6.6-head-control", len(hg) == 4 and all(abs(v.get("winding", 0) - 1) < 1e-6 and v["noise"] < 1e-3 for v in hg.values()) and conv_m,
          "n2d = 60 reference, g_m winding on the fine loop: " + ", ".join(
              f"m={m}: {v.get('winding', float('nan')):+.3f} (noise {v.get('noise', float('nan')):.0e})" for m, v in hg.items())
          + f"; compressed zero from the full one {[f'{x:.1e}' for x in dg]} (decreasing, last < 5e-7)")
    run("c6j-head.py", "L10", "29", "33", "37", "41", "45")
    hl = pickle.load(open(sc / "c6j-head-L10.pkl", "rb")) if (sc / "c6j-head-L10.pkl").exists() else {}  # noqa: SIM115
    s10 = complex(res["L10"]["pencil"]["zS"]["s"]) if res["L10"].get("pencil") else complex("nan")
    d45 = abs(hl[45]["s"] - s10) if 45 in hl and "s" in hl[45] else float("nan")
    check("C7.6.6-L10-head", len(hl) == 5 and set(hl) == {29, 33, 37, 41, 45} and all(abs(v.get("winding", 0) - 1) < 1e-6 and v["noise"] < 1e-3 for v in hl.values()) and d45 < 5e-7,
          "L10, g_m winding on the fine loop: " + ", ".join(
              f"m={m}: {v.get('winding', float('nan')):+.3f} (noise {v.get('noise', float('nan')):.0e})" for m, v in hl.items())
          + f"; m = 45 compressed zero {d45:.1e} from the full L10 zero")
    for k in ("r90", "L10"):
        tr = res[k].get("trunc", {})
        pz = res[k].get("pencil", {}).get("zS", {})
        print(f"[INFO] C7.6.6-{k}-isotropy-line  full pencil iota {pz.get('iota', float('nan')):.6f} argmax node {pz.get('argmax', -1)}; "
              f"truncated nS={tr.get('nS')}: iota {tr.get('iota', float('nan')):.6f}, argmax node {tr.get('argmax')} "
              f"(rho = {tr.get('rho_argmax', float('nan')):.3f}, {tr.get('edge_dist')} nodes from the range edge)")
    mx = {ln.split()[1].rstrip(":"): complex(ln.split("s**=")[1].split()[0]) for ln in run("c6j-mixed.py", "r90", "r120").splitlines()
          if ln.startswith("mixed")}
    s90 = complex(res["r90"]["pencil"]["zS"]["s"]) if res["r90"].get("pencil") else complex("nan")
    check("C7.6.6-r120-position", "r120" in mx and "r90" in mx and abs(mx["r90"] - s90) < 1e-9 and abs(mx["r120"] - C6J_SREF) < C6J_TOL,
          f"n2d = 120 (one DD matrix at zS, M' from the n2d = 60 set): s** = {mx.get('r120', complex('nan')):.10f}, shift from (12.26) "
          f"{abs(mx.get('r120', complex('nan')) - C6J_SREF):.2e}; the same construction on r90 reproduces its three-point zero to "
          f"{abs(mx.get('r90', complex('nan')) - s90):.1e}")
    rp = analyse("r90", "--plant", str(C6J_PLANT))
    okp, msgp = _c6j_stays(rp)
    sh = abs(complex(rp["pencil"]["zS"]["s"]) - complex(res["r90"]["pencil"]["zS"]["s"])) if rp.get("pencil") and res["r90"].get("pencil") else float("nan")
    check("BREAK-C7.6.6-plant-shift", (not okp) and abs(sh / C6J_PLANT - 1) < 0.1,
          f"planted shift {C6J_PLANT:.0e}: position test {'passes (BAD)' if okp else 'fails (as it must)'} -- {msgp}; returned shift {sh:.2e}")


def main() -> int:
    """Run the requested check groups; return 1 on any FAIL."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default="all", help="check group: c5, c6a, c6b, c6c, tab (default all = c5 + c6a)")
    parser.add_argument("--design", default="16,8,24", help="n_r,Lam,n_th of the Nystrom design (c6a, tab)")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--out", default="output/kp-tab-beta2.npz", help="output of --only tab")
    parser.add_argument("--tab", default="output/kp-tab-beta2-56-8-24.npz", help="tabulation read by c6b")
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    print(f"seed = {SEED}; groups = {args.only}")
    t_start = time.time()
    design = tuple(float(v) if i == 1 else int(v) for i, v in enumerate(args.design.split(",")))
    if args.only in ("all", "c5"):
        group_c5(rng)
    if args.only in ("all", "c6a"):
        group_c6a(rng, design, args.workers)
    if args.only == "c6b":
        group_c6b(rng, Path(args.tab))
    if args.only == "c6f":
        group_c6f()
    if args.only == "c6g":
        group_c6g()
    if args.only == "c6j":
        group_c6j()
    if args.only == "c6c":
        group_c6c(rng, Path(args.tab), args.workers)
    if args.only == "tab":
        tabulate_full(design, Path(args.out), args.workers)
        return 0
    n_fail = sum(1 for _, ok in _RESULTS if not ok)
    print(
        f"\n{len(_RESULTS) - n_fail}/{len(_RESULTS)} PASS, {n_fail} FAIL; {time.time() - t_start:.0f} s"
    )
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
