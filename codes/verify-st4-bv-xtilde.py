#!/usr/bin/env python3
"""
verify-st4-bv-xtilde.py — machine checks for ST4 (derivation 016): the BV taxonomy
of the homogeneous auxiliary-rotation term of the O(g_s^3) corrected gauge law,

    delta_h Xt = (g/10) K^{-1} V5(., Xt, dPsi)        (011 §4 eq. B.8)

The DECISIVE claim tested here is NOT a restatement of B.8, but the classification:
the effective trivial-symmetry generator mu (writing delta_h Xt = mu . E_Xt on the
Xt-EOM E_Xt ∝ K Xt) is graded-SYMMETRIC, hence NOT the antisymmetric generator that
a Henneaux–Teitelboim trivial gauge symmetry would require for even fields; and the
Grassmann parity of dPsi cannot antisymmetrise it (dPsi is a spectator in the swap of
the two Sym^2 slots of V5).

Finite-dimensional model, physical grading (all fields Grassmann-even, as in
R14/R17 / verify-b1-quintic.py): H0 = R^N, V4/V5 generic totally symmetric tensors,
work in an orthonormal Sym^2 basis Lambda_I (Frobenius) where the symmetric identity
is delta_IJ.

Conventions (match 011 §4 / R17):
  K_Psi(A,B) = V4(A,B) - (g/5) V5(A,B,Psi)                    dressed kernel
  W_{dPsi}   : (W_{dPsi})_{IJ} = V5(Lam_I, Lam_J, dPsi)       linear map on Sym^2
  E_Xt       = -(g^2/12) K Xt                                 Xt-EOM (from -(g^2/4!)K(Xt,Xt))
  delta_h Xt = (g/10) K^{-1} W_{dPsi} Xt = mu E_Xt,
  mu         = -(6/(5g)) K^{-1} W_{dPsi} K^{-1}               effective generator

Checks
  (1) reduction: delta_h Xt (from B.8) == mu E_Xt with the mu above
  (2) DECISIVE: mu is symmetric, NOT antisymmetric; distance to nearest antisym > 0
  (3) W_{dPsi} symmetric + linear in dPsi (sign-flip leg only — a sign flip does
      NOT model a Grassmann-odd dPsi; the parity-spectator claim is carried by
      the analytic argument of 016 §3.2) [reworded per critic M4]
  (4) not a standalone symmetry: E_Xt^T mu E_Xt = -(g^3/120) V5(Xt,Xt,dPsi) != 0
  (5) compensation: 2 K(delta_h Xt, Xt) + (delta K)(Xt,Xt) = 0   (full-transf invariance)
  (6) Psi-dependent kernel -> rotation != 0 (delta Xt / delta Y2 corner), mu
      symmetric in both corners; the Psi-INDEPENDENT zero-rotation leg is
      ILLUSTRATIVE only (0 = 0 by construction: dK is set to zero) — it
      illustrates the delta Y3 corner, it does not test it [labelled per C3]

All checks PASS/FAIL; exit code = number of failures.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

rng = np.random.default_rng(20260706)
np.set_printoptions(precision=6, suppress=True)

N = 3  # dim H0
DS = N * (N + 1) // 2  # dim Sym^2 = 6
TOL = 1e-9

failures: list[int] = []


def report(num: int, name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] check ({num}) {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(num)


def sym_tensor(shape: tuple[int, ...]) -> np.ndarray:
    """Totally symmetric random tensor."""
    T = rng.standard_normal(shape)
    S = np.zeros_like(T)
    k = len(shape)
    for perm in itertools.permutations(range(k)):
        S += np.transpose(T, perm)
    return S / math.factorial(k)


# ---------------------------------------------------------------- setup
V4 = sym_tensor((N,) * 4)
V5 = sym_tensor((N,) * 5)

# orthonormal Sym^2 basis Lambda_I (Frobenius)
Lam = []
for a in range(N):
    E = np.zeros((N, N))
    E[a, a] = 1.0
    Lam.append(E)
for a in range(N):
    for b in range(a + 1, N):
        E = np.zeros((N, N))
        E[a, b] = E[b, a] = 1 / np.sqrt(2)
        Lam.append(E)
Lam = np.array(Lam)  # (DS, N, N)

V4S = np.einsum("abcd,Iab,Jcd->IJ", V4, Lam, Lam)  # (DS,DS) symmetric
V5S = np.einsum("abcde,Iab,Jcd->IJe", V5, Lam, Lam)  # (DS,DS,N) sym in IJ


def sym_coords(M: np.ndarray) -> np.ndarray:
    return np.einsum("Iab,ab->I", Lam, (M + M.T) / 2)


def Kmat(psi: np.ndarray, g: float, dressed: bool = True) -> np.ndarray:
    """Dressed kernel K_Psi (dressed=True) or bare V4 (dressed=False)."""
    if dressed:
        return V4S - (g / 5.0) * np.einsum("IJe,e->IJ", V5S, psi)
    return V4S.copy()


def Wmap(chi: np.ndarray) -> np.ndarray:
    """(W_chi)_{IJ} = V5(Lam_I, Lam_J, chi)."""
    return np.einsum("IJe,e->IJ", V5S, chi)


# random common data
g = rng.uniform(0.05, 0.4)
psi = rng.standard_normal(N)
dpsi = rng.standard_normal(N)
Xt = rng.standard_normal(DS)  # off-shell deviation
K = Kmat(psi, g, dressed=True)
Kinv = np.linalg.inv(K)

# ---------------------------------------------------------------- check 1
# delta_h Xt from B.8, and via mu E_Xt
W = Wmap(dpsi)
dXt_B8 = (g / 10.0) * Kinv @ (W @ Xt)
E_Xt = -(g**2 / 12.0) * (K @ Xt)
mu = -(6.0 / (5.0 * g)) * Kinv @ W @ Kinv
dXt_mu = mu @ E_Xt
d1 = np.abs(dXt_B8 - dXt_mu).max()
report(1, "reduction delta_h Xt = mu E_Xt (16.3)", d1 < TOL, f"max dev {d1:.1e}")

# ---------------------------------------------------------------- check 2
asym = 0.5 * (mu - mu.T)
symp = 0.5 * (mu + mu.T)
is_sym = np.abs(asym).max() < TOL
dist_to_antisym = np.linalg.norm(symp)  # nearest antisym matrix is asym; residual = symp
report(
    2,
    "DECISIVE: mu symmetric, NOT antisymmetric (16.4)",
    is_sym and dist_to_antisym > 1e-3,
    f"|mu-mu^T|={np.abs(asym).max():.1e}, dist-to-antisym={dist_to_antisym:.3f}",
)

# ---------------------------------------------------------------- check 3
# W_{dPsi} symmetry for +dPsi and -dPsi. HONEST SCOPE [critic M4]: a sign flip
# of dpsi does NOT model a Grassmann-odd dPsi (there is no odd variable in this
# real-vector toy); what this leg confirms numerically is only linearity of
# W in dPsi plus symmetry of W for either sign. The claim that the PARITY of
# dPsi cannot antisymmetrise mu is carried by the ANALYTIC spectator argument
# (016 §3.2: dPsi sits in the untouched third V5 slot, so its parity never
# enters the I<->J exchange sign), which needs no numerical companion.
Wp = Wmap(dpsi)
Wm = Wmap(-dpsi)
sym_p = np.abs(Wp - Wp.T).max()
sym_m = np.abs(Wm - Wm.T).max()
report(
    3,
    "W_{dPsi} symmetric, linear in dPsi (sign-flip leg; the parity-spectator claim is analytic, 016 §3.2)",
    sym_p < TOL and sym_m < TOL,
    f"|W-W^T|(+)={sym_p:.1e}, |W-W^T|(-)={sym_m:.1e}",
)

# ---------------------------------------------------------------- check 4
# not a standalone symmetry: E^T mu E = -(g^3/120) V5(Xt,Xt,dPsi), generically != 0
dS_frozen = E_Xt @ (mu @ E_Xt)
V5_xxd = np.einsum("IJe,I,J,e->", V5S, Xt, Xt, dpsi)
predicted = -(g**3 / 120.0) * V5_xxd
report(
    4,
    "not a standalone symmetry: E^T mu E = -(g^3/120)V5(Xt,Xt,dPsi) != 0 (16.5)",
    abs(dS_frozen - predicted) < TOL * max(1, abs(predicted)) and abs(predicted) > 1e-6,
    f"dS_frozen={dS_frozen:.4e}, predicted={predicted:.4e}",
)

# ---------------------------------------------------------------- check 5
# compensation: full-transformation invariance of the dressed quadratic form
dK = -(g / 5.0) * Wmap(dpsi)  # delta K_Psi = -(g/5) V5(.,.,dPsi)
comp = 2.0 * (dXt_B8 @ K @ Xt) + (Xt @ dK @ Xt)
report(
    5,
    "compensation 2K(dXt,Xt)+(dK)(Xt,Xt)=0 (16.6; full-transf invariance)",
    abs(comp) < TOL,
    f"residual {comp:.1e}",
)

# ---------------------------------------------------------------- check 6
# field-dependence toggles the forced rotation; mu symmetric in both corners.
#   Psi-dependent kernel  -> anomaly dK != 0 -> forced rotation delta_h Xt != 0  (Xt/Y2)
#   Psi-independent kernel (bare V4) -> dK = 0 -> forced rotation = 0            (Y3)
# The "forced rotation" is the unique dXt cancelling the anomaly:
#   2 Kbar dXt . Xt = -(dKbar)(Xt,Xt).  With dKbar=0 the solution consistent with
#   the homogeneous ansatz dXt = (g/10) Kbar^{-1} W_bar Xt collapses because W enters
#   the kernel dressing; switching the dressing off sets both dK and the ansatz source.
detail6 = []
ok6 = True
# dependent corner
Kdep = Kmat(psi, g, dressed=True)
dKdep = -(g / 5.0) * Wmap(dpsi)
rot_dep = (g / 10.0) * np.linalg.solve(Kdep, Wmap(dpsi) @ Xt)
mu_dep = -(6.0 / (5.0 * g)) * np.linalg.inv(Kdep) @ Wmap(dpsi) @ np.linalg.inv(Kdep)
ok6 &= np.linalg.norm(rot_dep) > 1e-3  # nonzero rotation
ok6 &= np.abs(mu_dep - mu_dep.T).max() < TOL  # mu symmetric
detail6.append(f"dep: |rot|={np.linalg.norm(rot_dep):.3f}, |mu-mu^T|={np.abs(mu_dep-mu_dep.T).max():.1e}")
# independent corner: kernel = bare V4, no Psi in the kinetic -> dK = 0 -> forced rotation 0.
# ILLUSTRATIVE, NOT A TEST [critic C3]: dKind is set to the zero matrix BY
# DEFINITION of a Psi-independent kernel, so rot_ind = solve(2K, 0) = 0 is
# 0 = 0 by construction — this leg ILLUSTRATES the delta Y3 corner (R21) rather
# than testing it. (The genuine delta Y3 = 0 machine test is check 3 of
# verify-b5-ogs4-gauge-eom-ibl.py, rewritten 2026-07-09.) The decisive legs of
# THIS check are the nonzero rot_dep and mu symmetric in both corners.
Kind = Kmat(psi, g, dressed=False)  # = V4S, Psi-independent
dKind = np.zeros((DS, DS))  # delta of a Psi-independent kernel (zero by definition)
rot_ind = np.linalg.solve(2.0 * Kind, -(dKind @ Xt))  # = 0 by construction
# effective mu in this corner still symmetric (K^{-1} W K^{-1}, W symmetric)
mu_ind = -(6.0 / (5.0 * g)) * np.linalg.inv(Kind) @ Wmap(dpsi) @ np.linalg.inv(Kind)
ok6 &= np.linalg.norm(rot_ind) < TOL  # zero rotation (delta Y3 corner)
ok6 &= np.abs(mu_ind - mu_ind.T).max() < TOL  # mu symmetric
detail6.append(f"ind: |rot|={np.linalg.norm(rot_ind):.1e}, |mu-mu^T|={np.abs(mu_ind-mu_ind.T).max():.1e}")
report(
    6,
    "rotation nonzero in Psi-dep corner + mu symmetric both corners (zero-rotation leg illustrative only)",
    ok6,
    "; ".join(detail6),
)

# ---------------------------------------------------------------- summary
print()
if failures:
    print(f"{len(failures)} FAILURE(S): checks {failures}")
else:
    print("ALL 6 CHECKS PASS")
raise SystemExit(len(failures))
