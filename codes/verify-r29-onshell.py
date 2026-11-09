"""
On-shell limit of the level-0 Sigma-exchange (record 050, Addendum 2026-09-26, nodes C5.x).

What is verified
----------------
At the symmetric on-shell point of four tachyons (alpha' = 1, beta = 2, C = +1, sister
normalisation, Euclidean relative momenta of 045 A6 / PH25),

    |l0| = |l0'| = rho0(s),  rho0^2 = 4 - s/4,  x = cos(l0, l0') = 0,  s -> s* = 16/3,

the level-0 Sigma-exchange in the eigenbasis of K_P(s) (record 050 eq. (A.1), (R-b)),

    E_delta(s) = sum_{n even} dim Y_n P_n(x) / |S^25| sum_{j: mu_nj(s) > delta} mu_nj psi_nj(rho0)^2,

is evaluated from the Nystrom spectra of the partial-wave kernels (record 049 (1.3),
record 050 (8.4)) on the design (n_r, Lam, n_th) = (56, 8, 24), waves n <= 22 (exact
projectors on that angular rule, record 050 C2.2), at s in {s* - eps, s*, s* + eps}.

Checks (named after the nodes of the addendum):
  C5.2-value[s]        the resolved eigen-sum equals the direct evaluator
                       C F(s, 2 rho0^2, 2 rho0^2) (independent: no eigenvectors) to 1e-6;
  C5.3-fd-curvature    the second finite difference in s of the eigen-sum (moving on-shell
                       point included) equals that of the direct evaluator to 1e-2 relative
                       (the first difference vanishes at the symmetric point: F is S_3-
                       symmetric and s + t + u is fixed on shell, so dF/ds = 0 there; run 1
                       compared first differences, which are rounding noise, and failed);
  BREAK-C5.3-offshell  the same curvature with the radius frozen at rho0(s*) (an off-shell
                       path) must differ from the on-shell one by more than 1e-2;
  C5.3-gap-smooth      with a threshold delta in a spectral gap of K_P(s*), the truncation
                       E_delta has second difference in s at the eps^2 scale (smooth);
  BREAK-C5.3-threshold with delta placed on an eigenvalue of K_P(s*) the same second-
                       difference test must fail (a whole term enters on one side only).
  INFO (R-c)           partial sums of the propagator element sum mu^{-1} psi^2 grow as the
                       threshold is lowered: the representation carrying mu^{-1} has no
                       pointwise value at the external data.

What is not verified
--------------------
The analytic statements of the addendum (Mercer at every s, uniform convergence on
compacts, Riesz-projection analyticity) are proven in the record, not tested here; the
check covers one design, one point (x = 0), waves n <= 22, and eps = 1e-3.
"""

from __future__ import annotations

import importlib.util
import math
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "4")

import numpy as np  # noqa: E402

_CODES = Path(__file__).resolve().parent
SEED = 20260926  # no random points are drawn; printed for the record


def _load(name: str, filename: str):  # noqa: ANN202
    spec = importlib.util.spec_from_file_location(name, _CODES / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


krs = _load("verify_kp_real_s", "verify-kp-real-s.py")
kpk = krs.kpk

BETA = 2.0
S_STAR = 16.0 / 3.0
EPS = 1e-3
DESIGN = (56, 8.0, 24)
N_MAX = 22
X0 = 0.0  # symmetric point s = t = u
RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    """Print and record one named PASS/FAIL line."""
    RESULTS.append((name, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)


def rho0(s: float) -> float:
    """On-shell relative radius, alpha' rho0^2 = 4 - alpha' s / 4 (record 050 (8.5))."""
    return math.sqrt(4.0 - s / 4.0)


def spectra(s: float, radius: float | None = None) -> dict:
    """Per-wave (mu_nj, psi_nj(r)) on DESIGN, all j; r = rho0(s) and r = radius (if given)."""
    n_r, lam, n_th = DESIGN
    xg, wg = np.polynomial.legendre.leggauss(n_r)
    rho = 0.5 * lam * (xg + 1.0)
    wr = 0.5 * lam * wg
    x, w = kpk.angular_rule(n_th)
    pos = x > 0
    xp, wp = x[pos], 2.0 * w[pos]
    P = krs.gegen_norm(N_MAX, xp)
    proj = kpk.sphere_area(kpk.D - 2) * (P * wp[None, :]).T
    iu, ju = np.triu_indices(n_r)
    kn_tri = krs._c8_fgrid(s, rho[iu], rho[ju], xp, pairwise=True) @ proj
    radii = [rho0(s)] + ([radius] if radius is not None else [])
    krow = krs._c8_fgrid(s, np.array(radii), rho, xp) @ proj  # (n_radii, n_r, N_MAX+1)
    dvec = np.sqrt(wr * rho ** (kpk.D - 1))
    out = {}
    for n in range(0, N_MAX + 1, 2):
        k = np.zeros((n_r, n_r))
        k[iu, ju] = kn_tri[:, n]
        k[ju, iu] = kn_tri[:, n]
        ev, V = np.linalg.eigh(dvec[:, None] * k * dvec[None, :])
        # psi(r) = mu^{-1} int k_n(r, .) psi (Nystrom interpolation)
        psis = [(krow[i, :, n] * dvec) @ V / ev for i in range(len(radii))]
        out[n] = (ev, psis[0])
        out[("frozen", n)] = (ev, psis[-1])
    return out


def e_sum(sp: dict, delta: float, power: int = 1, frozen: bool = False) -> float:
    """sum_n dim Y_n P_n(X0)/|S^25| sum_{mu > delta} mu^power psi^2 (power -1: (R-c))."""
    pn = krs.gegen_norm(N_MAX, np.array([X0]))[:, 0]
    area = kpk.sphere_area(kpk.D - 1)
    tot = 0.0
    for key, (ev, psi) in sp.items():
        if isinstance(key, tuple) != frozen:
            continue
        n = key[1] if frozen else key
        keep = ev > delta
        tot += (
            krs.dim_y(n)
            * pn[n]
            / area
            * float(np.sum(ev[keep] ** power * psi[keep] ** 2))
        )
    return tot


def f_direct(s: float) -> float:
    """C F(s, t, u) at the on-shell point, direct evaluator (no spectra)."""
    r2 = rho0(s) ** 2
    return float(
        kpk.f_vec(
            s, np.array([2 * r2 * (1 + X0)]), np.array([2 * r2 * (1 - X0)]), BETA
        )[0]
    )


def main() -> int:
    """Run the checks of the addendum; exit code 1 on any FAIL."""
    print(
        f"seed {SEED}; design {DESIGN}; n <= {N_MAX}; x = {X0}; eps = {EPS}", flush=True
    )
    s_vals = (S_STAR - EPS, S_STAR, S_STAR + EPS)
    sp = {s: spectra(s, rho0(S_STAR)) for s in s_vals}
    mu00 = sp[S_STAR][0][0][-1]
    floor = 1e-13 * mu00  # resolved spectrum (record 050 C2.8 projection floor)
    E = {s: e_sum(sp[s], floor) for s in s_vals}
    F = {s: f_direct(s) for s in s_vals}
    for s in s_vals:
        rel = abs(E[s] - F[s]) / abs(F[s])
        check(
            f"C5.2-value[s={s:.6f}]",
            rel < 1e-6,
            f"E={E[s]:.10e} F={F[s]:.10e} rel={rel:.1e}",
        )

    def d2(v: dict) -> float:
        return (v[s_vals[2]] - 2 * v[s_vals[1]] + v[s_vals[0]]) / EPS**2

    d1E = (E[s_vals[2]] - E[s_vals[0]]) / (2 * EPS)
    print(
        f"INFO first differences (stationary point): dE/ds={d1E:.3e}, "
        f"relative {d1E / E[S_STAR]:.1e}",
        flush=True,
    )
    rel_c = abs(d2(E) - d2(F)) / abs(d2(F))
    check(
        "C5.3-fd-curvature",
        rel_c < 1e-2,
        f"d2E={d2(E):.6e} d2F={d2(F):.6e} rel={rel_c:.1e}",
    )
    Efr = {s: e_sum(sp[s], floor, frozen=True) for s in s_vals}
    rel_b = abs(d2(Efr) - d2(F)) / abs(d2(F))
    check(
        "BREAK-C5.3-offshell",
        rel_b > 1e-2,
        f"frozen radius: d2={d2(Efr):.6e} vs d2F={d2(F):.6e} rel={rel_b:.1e} (must exceed 1e-2)",
    )

    def second_diff(delta: float) -> tuple[float, list[float]]:
        vals = [e_sum(sp[s], delta) for s in s_vals]
        return abs(vals[2] - 2 * vals[1] + vals[0]) / abs(vals[1]), vals

    # smooth scale: second difference of the direct evaluator
    d2F = abs(F[s_vals[2]] - 2 * F[s_vals[1]] + F[s_vals[0]]) / abs(F[s_vals[1]])
    tol = max(100 * d2F, 1e-9)
    ev0 = np.sort(sp[S_STAR][0][0])[::-1]
    # delta in the gap between mu_{0,4} and mu_{0,5} of the s-wave at s*, checked against
    # every wave's spectrum at all three s (no eigenvalue within a factor 1.2 of delta)
    delta_gap = math.sqrt(ev0[3] * ev0[4])
    near = min(
        abs(math.log(abs(e) / delta_gap))
        for s in s_vals
        for ev, _ in sp[s].values()
        for e in ev
        if e > 0
    )
    d2, vals = second_diff(delta_gap)
    check(
        "C5.3-gap-smooth",
        d2 < tol and near > math.log(1.2),
        f"delta/mu00={delta_gap / mu00:.3e} d2={d2:.2e} tol={tol:.2e} (d2F={d2F:.2e}) "
        f"log-dist to spectrum={near:.2f} tail/F={(F[S_STAR] - vals[1]) / F[S_STAR]:.3e}",
    )
    delta_on = float(ev0[3])  # on an eigenvalue of K_P(s*)
    d2b, _ = second_diff(delta_on)
    check(
        "BREAK-C5.3-threshold",
        not (d2b < tol),
        f"delta=mu_03(s*): d2={d2b:.2e} vs tol={tol:.2e} (must exceed)",
    )
    rc = [e_sum(sp[S_STAR], d * mu00, power=-1) for d in (1e-2, 1e-4, 1e-6, 1e-8)]
    print(
        "INFO (R-c) partial sums of sum mu^-1 psi^2 at thresholds 1e-2..1e-8 mu00: "
        + ", ".join(f"{v:.3e}" for v in rc),
        flush=True,
    )
    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(
        f"SUMMARY: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS, {n_fail} FAIL",
        flush=True,
    )
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
