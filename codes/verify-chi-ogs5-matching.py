#!/usr/bin/env python3
"""
verify-chi-ogs5-matching.py — harness for the chi-scheme O(g_s^5) matching (record 048).

Sub-task 1 (2026-09-22): model, joint Newton saddle in (Sigma_2, chi, Sigma_3), Richardson
extrapolation, calibration on the O(g_s^3) and O(g_s^4) legs, and the projection basis
{V7(Psi^7), S1, S2, S3}. Nothing is fitted here: (a_chi, b_chi) = (1, 2) is R24's value,
(c6, c_Sigma3) = (0, 1) is the pinned split (038 section 6.1), c_chi = d_chi = a7 = 0.

Model (as in codes/verify-chi-partner.py, extended): H_0 = R^N with N = 4, fully symmetric
random tensors V2..V7, random off-shell Psi. Action S^chi_5 of 038 section 6.1, eq. (1.1) of
record 048:

    S = 1/2 V2(Psi^2) + g/3! V3(Psi^3)
        - g^2/4! V4(S,S) + k_sp g^2/4! V4(S,P) + g^3/5! V5(S,S,Psi)
        + a g^2/4! V4(C,C) + b g^3/5! V5(C,S,Psi) + c g^3/5! V5(C,C,Psi)
        + c6 g^4/6! V6(S,S,S) + c3 g^4/6! [-V6(T,T) + 2 V6(T,S,Psi)] + d g^4/6! V6(C,S,S)
        + a7 g^5/7! V7(T,T,Psi) + bp g^3/5! V5(C,T),

with S = Sigma_2, C = chi, T = Sigma_3, P = Psi Psi, k_sp = 2 nominal (break-leg knob),
bp = b'_chi = 0 nominal (break leg of the continuation). Target: the tree effective action
S_eff(g) = sum_k g^(k-2)/k! V_k(Psi^k), k = 2..7. Mismatch D_n(g) = [S(saddle) - S_eff]/g^n,
Richardson 2 D_n(g0/2) - D_n(g0).

Checks (named after the claim-tree nodes of record 048):
  C0.1  analytic gradient of S against central finite differences (+ BREAK: a wrong factor
        in one gradient term is detected).
  C0.2  O(g_s^3) leg: D3 -> 0 (+ BREAK: k_sp = 1.9 leaves an O(g^2) mismatch).
  C0.3  O(g_s^4) leg: D4 -> 0 at c6 = 0, 1/2, 1 (the Sigma_3 HS pair supplies the sextic
        contact); no-chi -> v V4^{-1} v / 600 and chi(1,1) -> 3/4 of it (R24 values; these
        are the break legs of closure and are checked against predicted nonzero values).
  C0.4  with chi(1,2) the residual is O(g^5): log-log slope of D4 in [0.7, 1.5].
  C0.5  Gram matrix of {V7(Psi^7), S1, S2, S3} on random Psi probes is non-singular
        (+ BREAK: appending the redundant V7|_{322} column lowers the rank deficit to 1).

Sub-task 2 (2026-09-22; C6/C3-N4/C2 sensitivity and the ladder study added on the fix pass
after critic iteration 1, agent/reports/critic-048-20260922T163000.md): the O(g_s^5)
coefficient itself. The mismatch is fitted as
S(saddle) - S_eff = sum_{k=4..7} c_k g^k on a probe-adapted window (record 048 section 7.1),
and 7! c5 is projected on {V7(Psi^7), S1, S2, S3}. Predictions derived in 048 section 7.2
BEFORE any measurement, and used as the gates:

    7! c5 = -V7(Psi^7) + alpha S1 + beta(c6) S2
            + a7 V7(Psi^7) + (7!/3000) c_chi S1 - (7!/3600) d_chi S2,
    alpha = -42/25,   beta(c6) = 7 (2 + c6) / 5   [038 (3.3d)],

so closure at (c_chi, d_chi, a7) = (1, 2 + c6, 1).

  C1  diagonality: c_chi moves only S1, d_chi only S2, a7 only V7, by 42/25, -7/5, 1.
  C2  no S3 (N3) and nothing orthogonal to the four columns (N3'); V7 coefficient = -1
      (+ BREAK: an injected S3 admixture at 20% of ||7! c5|| is detected; + the 5% gate
      translated into the smallest out-of-span COEFFICIENT it detects, gamma_min, in the
      normalisation where the V7 coefficient of the deficit is 1).
  C3  Sigma_3 kinetic normalisation (N4): T -> mu T with kinetic mu^2, source mu, a7 mu^2
      leaves c5 unchanged (+ BREAK: rescaling the kinetic alone does move it); the one
      M^{-1} composite X^T L^T M^{-1} L X has log-log slope 6, i.e. is O(g_s^6); and the
      falsifiable form, M -> M + eps Delta with Delta p_3 = 0 (leading saddle and O(g_s^4)
      contact untouched) leaves c5 unchanged (+ BREAK: Delta p_3 != 0 moves it).
  C4  the three couplings, each fitted from its own direction only, and an out-of-sample
      check at a Psi not in the fitted probe set. Reported as DERIVED: each is a corollary
      of C4-alpha/C4-beta/C2-V7 and the matching C1-size check.
  C5  O(g_s^3) and O(g_s^4) legs untouched at the fitted point; log-log slope of
      |S - S_eff| >= 6 after the fit (+ BREAK: it is 5 before).
  C6  falsification leg: b'_chi != 0 produces a component outside the span. Scanned in b'
      with the COMPENSATED coupling b = 2 - b' (switching b' on at fixed b is, at leading
      order, the reparametrisation b_eff = b + b' of the O(g_s^4) sector), and gated on the
      absolute out-of-span coefficient against gamma_min, not on a share.
  C7  sextic split scan c6 in {0, 1/2, 1}: beta(c6) = 7(2+c6)/5, alpha c6-independent.
  C8  the extrapolator: convergence study over three ladder settings, baseline and C6, and
      the stopping rule (shift of alpha, beta below the gate width).

NOT verified here: N > 4, more than three seeds, O(g_s^6), the b'_chi branch beyond linear
response, and anything above the finite-dimensional algebraic layer.
"""

from __future__ import annotations

import sys
from itertools import combinations_with_replacement, permutations

import numpy as np
from scipy.optimize import root

N = 4
SEEDS = (7, 23, 11)
NPSI = 40

failures: list[str] = []
tally: dict[str, int] = {"CHECK": 0, "BREAK": 0, "DERIVED": 0}
fallbacks = {
    "n": 0
}  # windows chosen by the fallback branch of choose_window (no window above the snr guard)


def report(name: str, ok: bool, detail: str, kind: str = "CHECK") -> None:
    """Print one PASS/FAIL line and record failures."""
    tally[kind] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] ({kind}) {name}: {detail}")
    if not ok:
        failures.append(name)


def sym_tensor(rng: np.random.Generator, k: int) -> np.ndarray:
    """Fully symmetric random k-tensor (same construction as verify-chi-partner.py)."""
    t = rng.standard_normal((N,) * k)
    s = np.zeros_like(t)
    perms = list(permutations(range(k)))
    for p in perms:
        s += np.transpose(t, p)
    return s / len(perms)


class SymSpace:
    """
    Parametrisation of Sym^k(R^N) by its independent components.

    y (length dim) <-> full tensor via `full`; a gradient with respect to the full tensor
    (entries treated as independent) is pulled back by `reduce`, which sums over the
    distinct permutations of each index multiset (the chain rule of the embedding).
    """

    def __init__(self, k: int) -> None:
        """Index multisets of Sym^k and their distinct permutations."""
        self.k = k
        self.idx = list(combinations_with_replacement(range(N), k))
        self.dim = len(self.idx)
        self.perms = [sorted(set(permutations(t))) for t in self.idx]

    def full(self, y: np.ndarray) -> np.ndarray:
        """Embed the independent components into the full symmetric tensor."""
        t = np.zeros((N,) * self.k)
        for yi, ps in zip(y, self.perms, strict=True):
            for p in ps:
                t[p] = yi
        return t

    def reduce(self, grad_full: np.ndarray) -> np.ndarray:
        """Pull a full-tensor gradient back to the independent components."""
        return np.array([sum(grad_full[p] for p in ps) for ps in self.perms])


SYM2 = SymSpace(2)
SYM3 = SymSpace(3)
D2, D3 = SYM2.dim, SYM3.dim

NOMINAL = {
    "a": 1.0,
    "b": 2.0,
    "c": 0.0,
    "c6": 0.0,
    "c3": 1.0,
    "d": 0.0,
    "a7": 0.0,
    "bp": 0.0,
    "k_sp": 2.0,
    "mu_kin": 1.0,  # Sigma_3 field redefinition T -> mu T: kinetic and V7 slots (mu^2)
    "mu_src": 1.0,  # ... and the V6(T, Sigma, Psi) source slot (mu^1)
    "dM": 0.0,  # perturbation of the Sigma_3 kinetic form M only (N4 test, C3-N4)
}


def build(seed: int):
    """Random symmetric vertices V2..V7 and an off-shell Psi."""
    rng = np.random.default_rng(seed)
    t = {k: sym_tensor(rng, k) for k in range(2, 8)}
    psi = rng.standard_normal(N)
    return t, psi


def s_eff(t, psi, g: float) -> float:
    """Tree effective action of the toy: the contacts through V7."""
    e = np.einsum
    return (
        0.5 * e("ij,i,j", t[2], psi, psi)
        + g / 6 * e("ijk,i,j,k", t[3], psi, psi, psi)
        + g**2 / 24 * e("ijkl,i,j,k,l", t[4], psi, psi, psi, psi)
        + g**3 / 120 * e("ijklm,i,j,k,l,m", t[5], psi, psi, psi, psi, psi)
        + g**4 / 720 * e("ijklmn,i,j,k,l,m,n", t[6], psi, psi, psi, psi, psi, psi)
        + g**5 / 5040 * e("ijklmno,i,j,k,l,m,n,o", t[7], *([psi] * 7))
    )


def action(t, psi, g: float, s, c, t3, co, with_chi=True) -> float:
    """S^chi_5 of eq. (1.1) at full tensors (s, c, t3) = (Sigma_2, chi, Sigma_3)."""
    e = np.einsum
    p = np.outer(psi, psi)
    val = (
        0.5 * e("ij,i,j", t[2], psi, psi)
        + g / 6 * e("ijk,i,j,k", t[3], psi, psi, psi)
        - g**2 / 24 * e("ijkl,ij,kl", t[4], s, s)
        + co["k_sp"] * g**2 / 24 * e("ijkl,ij,kl", t[4], s, p)
        + g**3 / 120 * e("ijklm,ij,kl,m", t[5], s, s, psi)
        + co["c6"] * g**4 / 720 * e("ijklmn,ij,kl,mn", t[6], s, s, s)
        + co["c3"]
        * g**4
        / 720
        * (
            -co["mu_kin"] * e("ijklmn,ijk,lmn", t[6] + co.get("dM", 0.0), t3, t3)
            + 2 * co["mu_src"] * e("ijklmn,ijk,lm,n", t[6], t3, s, psi)
        )
        + co["mu_kin"]
        * co["a7"]
        * g**5
        / 5040
        * e("ijklmno,ijk,lmn,o", t[7], t3, t3, psi)
    )
    if with_chi:
        val += (
            co["a"] * g**2 / 24 * e("ijkl,ij,kl", t[4], c, c)
            + co["b"] * g**3 / 120 * e("ijklm,ij,kl,m", t[5], c, s, psi)
            + co["c"] * g**3 / 120 * e("ijklm,ij,kl,m", t[5], c, c, psi)
            + co["d"] * g**4 / 720 * e("ijklmn,ij,kl,mn", t[6], c, s, s)
            + co["bp"] * g**3 / 120 * e("ijklm,ij,klm", t[5], c, t3)
        )
    return val


def grads(t, psi, g: float, s, c, t3, co, with_chi=True, bug=False):
    """Gradients of `action` w.r.t. the full tensors (entries treated as independent)."""
    e = np.einsum
    p = np.outer(psi, psi)
    gs = (
        -(g**2) / 12 * e("ijkl,kl->ij", t[4], s)
        + co["k_sp"] * g**2 / 24 * e("ijkl,kl->ij", t[4], p)
        + g**3 / 60 * e("ijklm,kl,m->ij", t[5], s, psi)
        + co["c6"] * g**4 / 240 * e("ijklmn,kl,mn->ij", t[6], s, s)
        + co["c3"]
        * co["mu_src"]
        * 2
        * g**4
        / 720
        * e("ijklmn,ijk,n->lm", t[6], t3, psi)
    )
    gt = (
        -co["c3"]
        * co["mu_kin"]
        * g**4
        / 360
        * e("ijklmn,lmn->ijk", t[6] + co.get("dM", 0.0), t3)
        + co["c3"] * co["mu_src"] * 2 * g**4 / 720 * e("ijklmn,lm,n->ijk", t[6], s, psi)
        + co["mu_kin"] * co["a7"] * g**5 / 2520 * e("ijklmno,lmn,o->ijk", t[7], t3, psi)
    )
    if with_chi:
        gs += co["b"] * g**3 / 120 * e("ijklm,kl,m->ij", t[5], c, psi) + co[
            "d"
        ] * g**4 / (180 if bug else 360) * e("ijklmn,kl,mn->ij", t[6], c, s)
        gc = (
            co["a"] * g**2 / 12 * e("ijkl,kl->ij", t[4], c)
            + co["b"] * g**3 / 120 * e("ijklm,kl,m->ij", t[5], s, psi)
            + co["c"] * g**3 / 60 * e("ijklm,kl,m->ij", t[5], c, psi)
            + co["d"] * g**4 / 720 * e("ijklmn,kl,mn->ij", t[6], s, s)
            + co["bp"] * g**3 / 120 * e("ijklm,klm->ij", t[5], t3)
        )
        gt += co["bp"] * g**3 / 120 * e("ijklm,ij->klm", t[5], c)
    else:
        gc = c  # forces chi = 0
    return gs, gc, gt


def unpack(y):
    """Split the reduced vector into the full tensors (Sigma_2, chi, Sigma_3)."""
    return SYM2.full(y[:D2]), SYM2.full(y[D2 : 2 * D2]), SYM3.full(y[2 * D2 :])


def reduced_grad(t, psi, g, y, co, with_chi=True, bug=False, scale=True):
    """Gradient in the reduced coordinates, rescaled per sector for the root-finder."""
    s, c, t3 = unpack(y)
    gs, gc, gt = grads(t, psi, g, s, c, t3, co, with_chi, bug)
    r = np.concatenate([SYM2.reduce(gs), SYM2.reduce(gc), SYM3.reduce(gt)])
    if scale:
        # Sigma_2 and chi kinetics are O(g^2), the Sigma_3 kinetic is O(g^4)
        r[: 2 * D2] /= g**2
        r[2 * D2 :] /= g**4
    return r


def saddle(t, psi, g, co, with_chi=True):
    """Joint Newton saddle (hybr) in (Sigma_2, chi, Sigma_3); returns (y, action value)."""
    p = np.outer(psi, psi)
    p3 = np.einsum("i,j,k->ijk", psi, psi, psi)
    y0 = np.concatenate(
        [p[tuple(np.array(SYM2.idx).T)], np.zeros(D2), p3[tuple(np.array(SYM3.idx).T)]]
    )
    sol = root(
        lambda y: reduced_grad(t, psi, g, y, co, with_chi), y0, method="hybr", tol=1e-14
    )
    gr = np.max(np.abs(reduced_grad(t, psi, g, sol.x, co, with_chi)))
    assert gr < 1e-9, f"saddle not converged at g={g}: scaled grad {gr:.2e}"
    s, c, t3 = unpack(sol.x)
    return sol.x, action(t, psi, g, s, c, t3, co, with_chi)


def mismatch(t, psi, co, n: int, with_chi=True):
    """D_n(g) = [S(saddle) - S_eff]/g^n."""
    return lambda g: (saddle(t, psi, g, co, with_chi)[1] - s_eff(t, psi, g)) / g**n


def richardson_limit(f, g0=1e-2):
    """f(g) = D0 + c1 g + O(g^2): 2 f(g0/2) - f(g0)."""
    return 2 * f(g0 / 2) - f(g0)


def loglog_slope(f, g0=3e-2):
    """Scaling exponent of |f| over [g0/5, g0] (as in verify-chi-partner.py)."""
    gs = g0 * np.array([1.0, 0.7, 0.5, 0.35, 0.2])
    vals = np.array([abs(f(g)) for g in gs])
    return float(np.polyfit(np.log(gs), np.log(vals), 1)[0])


def v4_inv(t4, x):
    """Sym^2 inverse image under V4 (minimum-norm lstsq, as in the sister scripts)."""
    a = t4.reshape(N * N, N * N)
    sol, *_ = np.linalg.lstsq(a, x.reshape(N * N), rcond=None)
    sol = sol.reshape(N, N)
    return 0.5 * (sol + sol.T)


def vV4inv_v(t4, t5, psi) -> float:
    """R24 residual invariant v^T V4^{-1} v with v = V5(., Psi^3)."""
    v = np.einsum("ijklm,k,l,m->ij", t5, psi, psi, psi)
    return float(np.einsum("ij,ij", v, v4_inv(t4, v)))


def basis(t, psi) -> dict[str, float]:
    """
    Order-7 projection basis.

    Copied from codes/verify-chi-ogs5-count.py `invariants`
    (same normalisation, so the fitted coefficients of the continuation are comparable).
    """
    e = np.einsum
    p = np.outer(psi, psi)
    p3 = e("i,j,k->ijk", psi, psi, psi)
    v = e("ijklm,kl,m->ij", t[5], p, psi)
    w = e("ijklm,m->ijkl", t[5], psi)
    g6 = e("ijklmn,kl,mn->ij", t[6], p, p)
    x = v4_inv(t[4], v)
    a_ten = e("ijkla,kl->ija", t[5], p)
    b_ten = np.stack([v4_inv(t[4], a_ten[:, :, a]) for a in range(N)], axis=2)
    return {
        "V7d": e("ijklmno,i,j,k,l,m,n,o", t[7], *([psi] * 7)),
        "S1": e("ijkl,ij,kl", w, x, x),
        "S2": e("ij,ij", g6, x),
        "S3": e("ija,ijb,ab", b_ten, a_ten, x),
        "V7_322": e("ijklmno,ijk,lm,no", t[7], p3, p, p),  # redundant (break leg)
    }


def gram(cols: list[np.ndarray]):
    """Gram matrix, eigenvalues and numerical rank of normalised sampled columns."""
    m = np.stack(cols, axis=1)
    m = m / np.linalg.norm(m, axis=0)
    gm = m.T @ m
    ev = np.linalg.eigvalsh(gm)
    rank = int((ev > 1e-8 * ev[-1]).sum())
    return gm, ev, rank


def run(seed: int) -> None:
    """Run every check for one random-tensor seed."""
    print(f"\n=== seed {seed} (N={N}) ===")
    t, psi = build(seed)
    rng = np.random.default_rng(seed + 500)
    co = dict(NOMINAL)

    # --- C0.1: gradient against central finite differences at a generic point ---
    g_fd = 0.3
    co_fd = {
        **co,
        "c": 0.7,
        "d": -0.9,
        "a7": 1.3,
        "c6": 0.4,
        "bp": 0.6,
    }  # every term on
    y = rng.standard_normal(2 * D2 + D3)

    def fd_grad(bug=False):
        h = 1e-5
        out = np.zeros_like(y)
        for i in range(len(y)):
            yp, ym = y.copy(), y.copy()
            yp[i] += h
            ym[i] -= h
            out[i] = (
                action(t, psi, g_fd, *unpack(yp), co_fd)
                - action(t, psi, g_fd, *unpack(ym), co_fd)
            ) / (2 * h)
        return out

    fd = fd_grad()
    an = reduced_grad(t, psi, g_fd, y, co_fd, scale=False)
    err = np.max(np.abs(an - fd)) / np.max(np.abs(fd))
    report("C0.1-gradient", err < 1e-7, f"max rel |analytic - FD| = {err:.2e}")
    an_bug = reduced_grad(t, psi, g_fd, y, co_fd, scale=False, bug=True)
    err_b = np.max(np.abs(an_bug - fd)) / np.max(np.abs(fd))
    report(
        "C0.1-gradient",
        err_b > 1e-3,
        f"a factor-2 error in the d_chi term of dS/dSigma is seen: rel dev {err_b:.2e}",
        kind="BREAK",
    )

    # --- C0.2: O(g^3) leg ---
    scale = abs(vV4inv_v(t[4], t[5], psi)) / 600.0
    d3 = richardson_limit(mismatch(t, psi, co, 3))
    report("C0.2-D3", abs(d3) < 1e-3 * max(1.0, scale), f"R[D3] = {d3:+.3e} (expect 0)")
    d3b = richardson_limit(mismatch(t, psi, {**co, "k_sp": 1.9}, 3))
    report(
        "C0.2-D3",
        abs(d3b) > 1e-2,
        f"k_sp = 1.9 (wrong HS source) gives R[D3] = {d3b:+.3e}",
        kind="BREAK",
    )

    # --- C0.3: O(g^4) leg ---
    for c6 in (0.0, 0.5, 1.0):
        coc = {**co, "c6": c6, "c3": 1.0 - c6}
        d4 = richardson_limit(mismatch(t, psi, coc, 4))
        report(
            f"C0.3-D4-closure[c6={c6}]",
            abs(d4) / scale < 1e-2,
            f"R[D4]/|vV4^-1v/600| = {abs(d4) / scale:.2e} (expect 0)",
        )
    d4_nochi = richardson_limit(mismatch(t, psi, co, 4, with_chi=False))
    tgt = vV4inv_v(t[4], t[5], psi) / 600.0
    report(
        "C0.3-D4-nochi",
        abs(d4_nochi - tgt) / scale < 1e-2,
        f"R[D4] = {d4_nochi:+.4e}, R24 value vV4^-1v/600 = {tgt:+.4e}",
    )
    d4_b1 = richardson_limit(mismatch(t, psi, {**co, "b": 1.0}, 4))
    report(
        "C0.3-D4-chi(1,1)",
        abs(d4_b1 - 0.75 * tgt) / scale < 1e-2,
        f"R[D4] = {d4_b1:+.4e}, R24 value (1-b^2/4) vV4^-1v/600 = {0.75 * tgt:+.4e}",
    )

    # --- C0.4: residual with the O(g^4) action is O(g^5) ---
    sl = loglog_slope(mismatch(t, psi, co, 4))
    report(
        "C0.4-slope", 0.7 < sl < 1.5, f"log-log slope of D4 on [6e-3, 3e-2] = {sl:.3f}"
    )

    # diagnostic for the continuation (not a check): stability of R[D5] at c=d=a7=0
    d5a = richardson_limit(mismatch(t, psi, co, 5), g0=1e-2)
    d5b = richardson_limit(mismatch(t, psi, co, 5), g0=2e-2)
    print(
        f"  diag: R[D5](g0=1e-2) = {d5a:+.6e}, R[D5](g0=2e-2) = {d5b:+.6e}, "
        f"rel spread {abs(d5a - d5b) / max(abs(d5a), 1e-300):.2e}"
    )

    # --- C0.5: projection basis Gram matrix ---
    psis = [rng.standard_normal(N) for _ in range(NPSI)]
    rows = [basis(t, p) for p in psis]
    col = {k: np.array([r[k] for r in rows]) for k in rows[0]}
    gm, ev, rank = gram([col["V7d"], col["S1"], col["S2"], col["S3"]])
    report(
        "C0.5-gram",
        rank == 4,
        f"rank {rank} (expect 4), cond(G) = {ev[-1] / ev[0]:.2e}, "
        f"min eigenvalue {ev[0]:.2e}",
    )
    _, ev5, rank5 = gram([col["V7d"], col["S1"], col["S2"], col["S3"], col["V7_322"]])
    report(
        "C0.5-gram",
        rank5 == 4,
        f"with the redundant V7|_322 column appended: rank {rank5} (expect 4, not 5), "
        f"min eigenvalue {ev5[0]:.2e} -> the rank test detects degeneracy",
        kind="BREAK",
    )
    np.set_printoptions(precision=3, suppress=True)
    print("  Gram matrix (normalised columns V7d, S1, S2, S3):")
    print("  " + str(gm).replace("\n", "\n  "))


# ---------------------------------------------------------------------------
# Sub-task 2: the O(g_s^5) coefficient, its projection, and tests C1-C7
# ---------------------------------------------------------------------------

GFIT = np.geomspace(5e-3, 5e-2, 8)
# Ladder of one-decade fit windows, spaced every half decade. The g-expansion of the saddle value has a
# probe-dependent radius (the effective parameter is g ||V4^{-1} v||, and ||x|| ranges
# over four decades on the probe sample, record 048 section 5), so the window is chosen
# per probe by the SELF-CONTAINED criterion of section 7: smallest relative residual of
# the order fit. That criterion never looks at the predicted alpha, beta.
GLADDER = tuple(np.geomspace(a, 10 * a, 8) for a in (5e-3, 1.5e-3, 5e-4, 1.5e-4, 5e-5))
# The two coarser extrapolator settings of record 048 section 8.7, kept so that the
# convergence study (baseline AND the C6 response) can be re-run from this script.
LADDER_COARSE = (
    ("one window [5e-3, 5e-2]", None),
    (
        "ladder of 3 decades",
        tuple(np.geomspace(a, 10 * a, 8) for a in (5e-3, 5e-4, 5e-5)),
    ),
)
ORDERS = (4, 5, 6, 7)
SNR_MIN = 1e3  # round-off floor guard for a fit window (measured floors are 0 or > 4e4)
RES_MAX = 1e-5  # above this the cached window is re-chosen for that configuration
FACT7 = 5040.0
ALPHA_PRED = -42.0 / 25.0  # rows 1 + 3 of 038 section 3.3, carrying the 1/n! prefactors
NPSI2 = 40
BP = 0.5  # b'_chi of the C6 falsification leg (the value of the superseded design)
BPS = 0.1  # small b' of the C6 scan: O(b'^2) compensation defect ~0.3 % of the chi kinetic
# The C6 gate is stated in section 7.3 as an absolute coefficient: the compensated leg's
# out-of-span component, in V7-column units, must exceed gamma_min, the smallest
# out-of-span coefficient the C2-perp gate detects on the same seed (perp_sensitivity) --
# the exact complement of C2-perp, and the gate the code applies (run2, C6-outside).
# An earlier draft of this comment said "10 x gamma_min"; that factor was never in the
# code, never in the section 7.3 gate table and never in the record. It is recorded as a
# discrepancy in record 048 section 8.5, together with the verdict under BOTH readings:
# at 1 x the three seeds clear the gate (10.7, 3.5, 33.9 gamma_min), at 10 x seed 23
# (3.5 gamma_min) would not. What the statistic MEASURES is settled separately, by the
# order diagnostic of section 8.8 (c6_diagnostic below), on the same numbers under either
# factor.
BCOLS = ("V7d", "S1", "S2", "S3")


def beta_pred(c6: float) -> float:
    """038 (3.3d): beta(c6) = 7(2+c6)/5, the S2 coefficient of the O(g_s^5) deficit."""
    return 7.0 * (2.0 + c6) / 5.0


def order_coeffs(t, psi, co, with_chi=True, gs=GFIT, orders=ORDERS):
    """
    Coefficients c_k of S(saddle) - S_eff = sum_k c_k g^k, k in `orders`.

    Least-squares fit on `gs` (column-scaled). Replaces the two-point Richardson of
    sub-task 1 for the O(g^5) coefficient: Richardson only removes the O(g) term of
    D_5, which leaves an O(g^2) truncation error, and amplifies float noise by g^-5.
    Returns (dict k -> c_k, relative fit residual, signal-to-noise of the window,
    condition number of the column-scaled design matrix):
    `snr` is min_g |S - S_eff| divided by the round-off floor of that difference, and
    must be large or the window fits round-off (the fit has four parameters for eight
    points, so a noise-dominated window can still show a small residual). The floor is
    eps * max_g |S - S_free|, with S_free = V2(Psi^2)/2 + g V3(Psi^3)/6: those two terms
    are the same expression in `action` and in `s_eff` and cancel to the last bit, so
    they carry no round-off and must not enter the noise scale.
    """
    e = np.einsum
    sv = np.array([saddle(t, psi, g, co, with_chi)[1] for g in gs])
    free = np.array(
        [
            0.5 * e("ij,i,j", t[2], psi, psi)
            + g / 6 * e("ijk,i,j,k", t[3], psi, psi, psi)
            for g in gs
        ]
    )
    f = sv - np.array([s_eff(t, psi, g) for g in gs])
    a = np.array([[g**k for k in orders] for g in gs])
    sc = np.abs(a).max(axis=0)
    sol, *_ = np.linalg.lstsq(a / sc, f, rcond=None)
    sol = sol / sc
    res = float(np.linalg.norm(f - a @ sol) / max(np.linalg.norm(f), 1e-300))
    snr = float(
        np.min(np.abs(f))
        / (np.finfo(float).eps * max(float(np.max(np.abs(sv - free))), 1e-300))
    )
    cond = float(np.linalg.cond(a / sc))
    return dict(zip(orders, sol, strict=True)), res, snr, cond


def choose_window(t, psi, co, with_chi=True, ladder=None):
    """
    Pick the fit window of `GLADDER` with the smallest relative order-fit residual.

    Two criteria, both internal to the fit and neither looking at the predicted
    coefficients: the window must be above the round-off floor (snr > SNR_MIN), and among
    those it is the one with the smallest relative residual. Without the first criterion
    the ladder happily picks a window where the four-parameter fit is fitting round-off.
    """
    ok, fallback = [], None
    for gs in GLADDER if ladder is None else ladder:
        try:
            _, r, snr, _ = order_coeffs(t, psi, co, with_chi, gs=gs)
        except AssertionError:
            continue
        if fallback is None or snr > fallback[0]:
            fallback = (snr, gs, r)
        if snr > SNR_MIN:
            ok.append((r, gs))
    if ok:
        r, gs = min(ok, key=lambda q: q[0])
        return gs, r
    if fallback is None:
        raise RuntimeError("no fit window converged")
    fallbacks["n"] += (
        1  # no window passed the snr guard: logged, record section 8 header
    )
    return fallback[1], fallback[2]


def deficit(t, psis, co, wins, with_chi=True, ladder=None):
    """
    7! times the O(g^5) coefficient, one entry per probe Psi (the quantity of (3.1)).

    Returns (7! c5 per probe, worst relative fit residual, number of re-windowed probes,
    worst condition number of the order fit, 7! c4 per probe). c4 must be consistent with
    zero: the O(g_s^4) leg closes (C0.3), so the mismatch starts at g^5.
    """
    out, resid, redone, conds, c4 = [], [], 0, [], []
    for p, gs in zip(psis, wins, strict=True):
        c, r, _, cd = order_coeffs(t, p, co, with_chi, gs=gs)
        if (
            r > RES_MAX
        ):  # the window cached at the nominal couplings does not serve here
            gs2, r2 = choose_window(t, p, co, with_chi, ladder=ladder)
            if r2 < r:
                cc = order_coeffs(t, p, co, with_chi, gs=gs2)
                c, r, cd, redone = cc[0], r2, cc[3], redone + 1
        out.append(FACT7 * c[5])
        c4.append(FACT7 * c[4])
        resid.append(r)
        conds.append(cd)
    return (
        np.array(out),
        float(np.max(resid)),
        redone,
        float(np.max(conds)),
        np.array(c4),
    )


def basis_matrix(t, psis) -> np.ndarray:
    """Rows [V7(Psi^7), S1, S2, S3] for each probe."""
    return np.array([[basis(t, p)[k] for k in BCOLS] for p in psis])


def project(y: np.ndarray, a: np.ndarray, keep=None):
    """
    Weighted least squares of y on the four basis columns.

    Each equation is normalised by the norm of its basis row (the heavy tail of
    V4^{-1} v otherwise lets two or three probes dominate, record 048 section 5), and
    the columns are scaled before the solve. Returns (coefficients, fraction of the
    weighted signal carried by S3, fraction orthogonal to the four columns,
    condition number of the weighted design, per-column contribution fractions).
    """
    if keep is not None:
        y, a = y[keep], a[keep]
    w = 1.0 / np.linalg.norm(a, axis=1)
    aw, yw = a * w[:, None], y * w
    cs = np.abs(aw).max(axis=0)
    sol, *_ = np.linalg.lstsq(aw / cs, yw, rcond=None)
    coef = sol / cs
    ny = max(float(np.linalg.norm(yw)), 1e-300)
    frac = np.array([np.linalg.norm(coef[i] * aw[:, i]) / ny for i in range(4)])
    perp = float(np.linalg.norm(yw - aw @ coef) / ny)
    return coef, float(frac[3]), perp, float(np.linalg.cond(aw / cs)), frac


def perp_coeff(y, a) -> float:
    """
    Out-of-span component of y, in units of the weighted norm of the V7(Psi^7) column.

    An absolute statistic, unlike the `perp` share returned by `project`, which divides by
    the norm of y and is therefore diluted whenever y also has a large in-span part. Same
    normalisation as `perp_sensitivity`, so the two are directly comparable: a value of
    gamma here means "an out-of-span admixture with coefficient gamma in the normalisation
    where the V7 coefficient of the deficit is 1".
    """
    w = 1.0 / np.linalg.norm(a, axis=1)
    aw, yw = a * w[:, None], y * w
    cs = np.abs(aw).max(axis=0)
    sol, *_ = np.linalg.lstsq(aw / cs, yw, rcond=None)
    return float(np.linalg.norm(yw - aw @ (sol / cs)) / np.linalg.norm(aw[:, 0]))


def perp_sensitivity(y, a, rng, gate=0.05):
    """
    Smallest coefficient of an out-of-span direction that the C2-perp gate detects.

    The 5 % gate of C2-perp is relative to the weighted deficit norm, which is dominated by
    S1 and S2; it is only informative once translated into a bound on the coefficient of a
    named alternative. A fourth invariant of the S4 type (038 section 3.1.4) is not
    constructed here, so its stand-in is a random probe-space direction orthogonal to the
    four columns, normalised to the weighted norm of the V7(Psi^7) column. Since the V7
    coefficient of the deficit is -1, the returned gamma is directly a coefficient bound in
    the normalisation "V7 coefficient = 1".

    Returns (gamma_min, perp share at gamma_min).
    """
    w = 1.0 / np.linalg.norm(a, axis=1)
    aw = a * w[:, None]
    r = rng.standard_normal(len(y))
    sol, *_ = np.linalg.lstsq(aw, r, rcond=None)
    r = r - aw @ sol
    r = r / np.linalg.norm(r) * np.linalg.norm(aw[:, 0])
    ru = r / w  # back to unweighted probe space, where y lives
    lo, hi = 1e-6, 1e3
    for _ in range(60):
        mid = np.sqrt(lo * hi)
        if project(y + mid * ru, a)[2] > gate:
            hi = mid
        else:
            lo = mid
    return hi, project(y + hi * ru, a)[2]


def x_norms(t, psis) -> np.ndarray:
    """||V4^{-1} v|| per probe: the heavy-tailed quantity used for trimming."""
    out = []
    for p in psis:
        v = np.einsum("ijklm,k,l,m->ij", t[5], p, p, p)
        out.append(np.linalg.norm(v4_inv(t[4], v)))
    return np.array(out)


def m3_inv(t6: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Sym^3 inverse image under M = V6|_{Sym^3 x Sym^3} (minimum-norm lstsq)."""
    a = t6.reshape(N**3, N**3)
    sol, *_ = np.linalg.lstsq(a, x.reshape(N**3), rcond=None)
    sol = sol.reshape(N, N, N)
    return SYM3.full(SYM3.reduce(sol) / np.array([len(q) for q in SYM3.perms]))


def m_inv_piece(t, psi, g, co):
    """
    Evaluate the one M^{-1} composite of 038 row 4: (c3 g^4/720) X^T L^T M^{-1} L X at the saddle.

    038 section 3.3 predicts it is O(g^6), i.e. invisible at O(g_s^5) (lemma N4).
    """
    y, _ = saddle(t, psi, g, co)
    sfull, _, _ = unpack(y)
    x = sfull - np.outer(psi, psi)
    lx = np.einsum("ijklmn,lm,n->ijk", t[6], x, psi)
    return co["c3"] * g**4 / 720 * float(np.einsum("ijk,ijk", lx, m3_inv(t[6], lx)))


def ladder_study(t, psis, amat, co, production):
    """
    Convergence study of record 048 section 8.7, for the baseline AND the C6 response.

    "Refinement of the extrapolator removes only truncation" has a falsifier: a genuine
    out-of-span component must be FLAT across the ladder, as seed 7's baseline is, while a
    truncation artefact shrinks. The C6 (compensated) orthogonal share is that flat
    quantity, so it is reported at the same three settings as the baseline.
    `production` is the six-tuple (alpha, beta, S3 share, baseline perp share, C6
    out-of-span coefficient, baseline out-of-span coefficient) already measured on the
    production ladder, appended as the last row instead of being recomputed.
    """
    rows = []
    for name, ladder in LADDER_COARSE:
        lad = (GFIT,) if ladder is None else ladder
        wins_l = [choose_window(t, p, co, ladder=lad)[0] for p in psis]
        yl, _, _, _, _ = deficit(t, psis, co, wins_l, ladder=lad)
        cl, s3l, pl, _, _ = project(yl, amat)
        pcl = perp_coeff(yl, amat)
        cob = {**co, "bp": BP, "b": 2.0 - BP}
        yb, _, _, _, _ = deficit(t, psis, cob, wins_l, ladder=lad)
        rows.append((name, cl[1], cl[2], s3l, pl, perp_coeff(yb - yl, amat), pcl))
    rows.append(("ladder of 5 half-decades (production)", *production))
    print(
        "  section 8.7 convergence study "
        "(alpha, beta, S3 share, baseline perp share, C6 perp coefficient):"
    )
    for nm, al, be, s3l, pl, pbl, pcl in rows:
        print(
            f"    {nm:38s} alpha {al:+.4f}  beta {be:+.4f}  S3 {s3l:.2e}  "
            f"perp share {pl:.2e}  perp coeff {pcl:.4f}  C6 perp coeff {pbl:.4f}"
        )
    c6v = [r[5] for r in rows]
    # Flatness is asserted on the two settings the stopping rule calls converged; the
    # coarsest setting is reported but is not a valid measurement of anything (its alpha
    # shift exceeds the gate width, C8-stop).
    spread = max(c6v[-2:]) / max(min(c6v[-2:]), 1e-300)
    bspread = max(r[4] for r in rows[-2:]) / max(min(r[4] for r in rows[-2:]), 1e-300)
    report(
        "C6-ladder",
        spread < 3.0,
        f"compensated C6 out-of-span coefficient at the three extrapolator settings: "
        f"{', '.join(f'{v:.4f}' for v in c6v)}; max/min over the two converged settings "
        f"= {spread:.2f} (gate < 3: a genuine out-of-span component is flat under "
        f"refinement, a truncation artefact is not; the baseline out-of-span coefficient "
        f"moves by {bspread:.1f}x over the same two settings)",
    )
    shift_a = abs(rows[-1][1] - rows[-2][1])
    shift_b = abs(rows[-1][2] - rows[-2][2])
    report(
        "C8-stop",
        shift_a < 0.05 * abs(ALPHA_PRED) and shift_b < 0.05 * beta_pred(0.0),
        f"stopping rule: |d alpha| = {shift_a:.3f} (< {0.05 * abs(ALPHA_PRED):.3f}) and "
        f"|d beta| = {shift_b:.3f} (< {0.05 * beta_pred(0.0):.3f}) between the last two "
        f"ladder settings, i.e. below the gate width",
    )


def run2(seed: int) -> None:
    """Run tests C1-C7 for one random-tensor seed."""
    print(f"\n=== seed {seed}: O(g_s^5) tests C1-C7 ===")
    t, psi0 = build(seed)
    rng = np.random.default_rng(seed + 500)
    psis = [rng.standard_normal(N) for _ in range(NPSI2)]
    co = dict(NOMINAL)
    amat = basis_matrix(t, psis)
    xn = x_norms(t, psis)
    keep = np.argsort(xn)[: int(0.9 * NPSI2)]  # trimmed set: drop the 10% heaviest
    wins = [choose_window(t, p, co)[0] for p in psis]
    win0, _ = choose_window(t, psi0, co)
    hi = {float(w[-1]) for w in wins}
    print(f"  fit windows chosen per probe (upper ends): {sorted(hi)}")

    # ---------- C2: projection of the raw deficit (nothing fitted) ----------
    y0, fres, fre, fcond, c4 = deficit(t, psis, co, wins)
    print(
        f"  order fit: max rel residual {fres:.2e}, {fre} probes re-windowed, "
        f"max cond(design) {fcond:.2e}, {fallbacks['n']} fallback-branch windows so far"
    )
    print(
        f"  c4 (must be consistent with zero: the O(g^4) leg closes): "
        f"max |7! c4| = {np.max(np.abs(c4)):.3e}, median = {np.median(np.abs(c4)):.3e}, "
        f"rms |7! c5| = {np.sqrt(np.mean(y0**2)):.3e}"
    )
    coef, f_s3, f_perp, pcond, frac = project(y0, amat)
    ctr, s3tr, ptr, _, _ = project(y0, amat, keep)
    print(
        f"  C2 coefficients (V7, S1, S2, S3) = {np.array2string(coef, precision=4)}, "
        f"cond {pcond:.2e}; trimmed {np.array2string(ctr, precision=4)}"
    )
    report(
        "C2-V7",
        abs(coef[0] + 1.0) < 0.03,
        f"V7(Psi^7) coefficient = {coef[0]:+.4f} (predicted -1 exactly)",
    )
    report(
        "C4-alpha",
        abs(coef[1] - ALPHA_PRED) / abs(ALPHA_PRED) < 0.05,
        f"alpha = {coef[1]:+.4f} vs 038 rows 1+3: {ALPHA_PRED:+.4f} "
        f"(rel {abs(coef[1] - ALPHA_PRED) / abs(ALPHA_PRED):.2e})",
    )
    report(
        "C4-beta",
        abs(coef[2] - beta_pred(0.0)) / beta_pred(0.0) < 0.05,
        f"beta(0) = {coef[2]:+.4f} vs 038 (3.3d): {beta_pred(0.0):+.4f} "
        f"(rel {abs(coef[2] - beta_pred(0.0)) / beta_pred(0.0):.2e})",
    )
    report(
        "C2-S3",
        f_s3 < 0.05,
        f"S3 share of the deficit = {f_s3:.2e} (N3; trimmed {s3tr:.2e}), "
        f"coefficient {coef[3]:+.3e}",
    )
    report(
        "C2-perp",
        f_perp < 0.05,
        f"share orthogonal to span{{V7,S1,S2,S3}} = {f_perp:.2e} "
        f"(N3'; trimmed {ptr:.2e})",
    )
    gmin, pmin = perp_sensitivity(y0, amat, np.random.default_rng(seed + 700))
    report(
        "C2-perp",
        pmin > 0.05,
        f"the 5 % gate detects an out-of-span admixture of coefficient "
        f"gamma = {gmin:.3f} in the normalisation where the V7(Psi^7) coefficient is 1 "
        f"(share {pmin:.2e}); this is the coefficient bound the gate asserts",
        kind="BREAK",
    )
    yb = y0 + 0.2 * np.linalg.norm(y0) / np.linalg.norm(amat[:, 3]) * amat[:, 3]
    _, f_s3b, _, _, _ = project(yb, amat)
    report(
        "C2-S3",
        f_s3b > 0.05,
        f"injecting an S3 admixture at 20% of ||deficit|| is seen: share {f_s3b:.2e}",
        kind="BREAK",
    )

    # ---------- C1/C4: the three response directions ----------
    resp, rcoef = {}, {}
    for key, cod in (
        ("c_chi", {**co, "c": 1.0}),
        ("d_chi", {**co, "d": 1.0}),
        ("a7", {**co, "a7": 1.0}),
    ):
        yk, rk, fre, _, _ = deficit(t, psis, cod, wins)
        print(f"  {key} config: max order-fit residual {rk:.2e}, {fre} re-windowed")
        resp[key] = yk - y0
        rcoef[key] = project(resp[key], amat)
    for key, slot, pred in (
        ("c_chi", 1, 42 / 25),
        ("d_chi", 2, -7 / 5),
        ("a7", 0, 1.0),
    ):
        c, _, pp, _, fr = rcoef[key]
        off = max([fr[i] for i in range(4) if i != slot] + [pp])
        print(
            f"  C1 response to {key}: {np.array2string(c, precision=4)}, perp {pp:.2e}"
        )
        report(
            f"C1-diag[{key}]",
            off < 0.05,
            f"largest off-direction share of d(deficit)/d({key}) = {off:.2e} "
            f"(shares {np.array2string(fr, precision=3)}, perp {pp:.2e})",
        )
        report(
            f"C1-size[{key}]",
            abs(c[slot] - pred) / abs(pred) < 0.05,
            f"on-direction response {c[slot]:+.4f} vs predicted {pred:+.4f}",
        )

    fit = {
        "a7": -coef[0] / rcoef["a7"][0][0],
        "c_chi": -coef[1] / rcoef["c_chi"][0][1],
        "d_chi": -coef[2] / rcoef["d_chi"][0][2],
    }
    print(f"  C4 fitted couplings: { {k: round(v, 5) for k, v in fit.items()} }")
    for key, pred in (("a7", 1.0), ("c_chi", 1.0), ("d_chi", 2.0)):
        report(
            f"C4-fit[{key}]",
            abs(fit[key] - pred) / pred < 0.05,
            f"{key} = {fit[key]:+.5f} vs 038 (5.1) value {pred:+.3f} "
            f"(derived: corollary of C4-alpha/C4-beta/C2-V7 and C1-size[{key}])",
            kind="DERIVED",
        )
    cofit = {**co, "c": fit["c_chi"], "d": fit["d_chi"], "a7": fit["a7"]}
    ck, _, _, _ = order_coeffs(t, psi0, cofit, gs=win0)
    c0raw, _, _, _ = order_coeffs(t, psi0, co, gs=win0)
    raw = abs(FACT7 * c0raw[5])
    report(
        "C4-outofsample",
        abs(FACT7 * ck[5]) < 0.05 * raw,
        f"at a Psi outside the fitted sample the O(g^5) coefficient drops from "
        f"{raw:.4e} to {abs(FACT7 * ck[5]):.4e} (ratio "
        f"{abs(FACT7 * ck[5]) / raw:.2e}); the three couplings are not per-probe",
    )

    # ---------- C5: lower legs and the closure slope ----------
    d3 = richardson_limit(mismatch(t, psi0, cofit, 3))
    scale = abs(vV4inv_v(t[4], t[5], psi0)) / 600.0
    report(
        "C5-D3",
        abs(d3) < 1e-3 * max(1.0, scale),
        f"R[D3] at the fitted couplings = {d3:+.3e} (expect 0)",
    )
    d4 = richardson_limit(mismatch(t, psi0, cofit, 4))
    report(
        "C5-D4",
        abs(d4) / scale < 1e-2,
        f"R[D4]/|vV4^-1v/600| at the fitted couplings = {abs(d4) / scale:.2e}",
    )
    gtop = float(win0[-1])
    sl = loglog_slope(
        lambda g: saddle(t, psi0, g, cofit)[1] - s_eff(t, psi0, g), g0=gtop
    )
    report(
        "C5-slope",
        sl > 5.7,
        f"log-log slope of |S - S_eff| after the fit = {sl:.3f} (expect >= 6)",
    )
    sl0 = loglog_slope(lambda g: saddle(t, psi0, g, co)[1] - s_eff(t, psi0, g), g0=gtop)
    report(
        "C5-slope",
        sl0 < 5.3,
        f"without the fitted couplings the same slope is {sl0:.3f} (expect 5)",
        kind="BREAK",
    )

    # ---------- C3: Sigma_3 kinetic normalisation ----------
    mu = 1.7
    co_mu = {**cofit, "mu_kin": mu**2, "mu_src": mu}
    cm, _, _, _ = order_coeffs(t, psi0, co_mu, gs=win0)
    cn, _, _, _ = order_coeffs(t, psi0, cofit, gs=win0)
    rel = abs(cm[5] - cn[5]) / max(abs(cn[5]), 1e-300)
    report(
        "C3-reparam",
        rel < 1e-3,
        f"T -> {mu} T (kinetic mu^2, source mu): O(g^5) coefficient changes by "
        f"rel {rel:.2e}",
    )
    co_bad = {**cofit, "mu_kin": mu**2, "mu_src": 1.0}
    cb, _, _, _ = order_coeffs(t, psi0, co_bad, gs=win0)
    relb = abs(cb[5] - cn[5]) / max(abs(cn[5]), 1e-300)
    report(
        "C3-reparam",
        relb > 1e-2,
        f"rescaling the kinetic alone (not a field redefinition) moves it by "
        f"rel {relb:.2e}",
        kind="BREAK",
    )
    slm = loglog_slope(lambda g: m_inv_piece(t, psi0, g, cofit), g0=gtop)
    report(
        "C3-Minv",
        slm > 5.7,
        f"log-log slope of the M^{{-1}} composite X^T L^T M^{{-1}} L X = {slm:.3f} "
        f"(038 row 4: O(g^6), invisible at O(g_s^5))",
    )

    # C3-N4: perturb the Sigma_3 kinetic form M -> M + eps Delta with Delta p_3 = 0.
    # Then (M + eps Delta) p_3 = M p_3 = u, so the leading saddle T_* = p_3 and the
    # O(g_s^4) sextic contact are untouched, and the only Delta-dependence of the saddle
    # value is (c3 g^4/720) (L X)^T (M + eps Delta)^{-1} (L X) = O(g^6) by N4. A visible
    # M^{-1} at O(g_s^5) would move c5. Break leg: the same Delta without the p_3
    # projection removed (Delta p_3 != 0) does move it.
    rngd = np.random.default_rng(seed + 900)
    z_raw = sym_tensor(rngd, 3)
    p3v = np.einsum("i,j,k->ijk", psi0, psi0, psi0)
    z = z_raw - p3v * float(np.einsum("ijk,ijk", z_raw, p3v)) / float(
        np.einsum("ijk,ijk", p3v, p3v)
    )
    eps = 0.3

    def dm_of(zz):
        """Delta_{ijklmn} = zz_{ijk} zz_{lmn}, scaled to eps ||V6||."""
        d = np.einsum("ijk,lmn->ijklmn", zz, zz)
        return eps * np.linalg.norm(t[6]) / np.linalg.norm(d) * d

    # normalised against the UNFITTED deficit c0raw[5]: at the fitted couplings c5 is
    # zero by construction (closure), so a relative change there has no scale.
    cnr = c0raw[5]
    cd_, _, _, _ = order_coeffs(t, psi0, {**co, "dM": dm_of(z)}, gs=win0)
    reln4 = abs(cd_[5] - cnr) / max(abs(cnr), 1e-300)
    report(
        "C3-N4",
        reln4 < 1e-4,
        f"M -> M + eps Delta with Delta p_3 = 0 (eps = {eps}, ||Delta|| = eps ||V6||): "
        f"O(g^5) coefficient changes by rel {reln4:.2e} (N4: M^{{-1}} invisible at "
        f"O(g_s^5))",
    )
    cdb, _, _, _ = order_coeffs(t, psi0, {**co, "dM": dm_of(z_raw)}, gs=win0)
    relb4 = abs(cdb[5] - cnr) / max(abs(cnr), 1e-300)
    report(
        "C3-N4",
        relb4 > 1e-3,
        f"the same perturbation with Delta p_3 != 0 (leading saddle moved) changes it by "
        f"rel {relb4:.2e}",
        kind="BREAK",
    )

    # ---------- C6: the b'_chi falsification leg ----------
    # C6 is the leg that calibrates C2-perp: it must show that the projection DOES see an
    # out-of-span component when the count says there is one. Two design points, both
    # forced by the elimination of Sigma_3 (record 048 section 8.5, rewritten after critic
    # iteration 1):
    #   (i) the chi source is (b + b') v/120 at leading order, so switching b' on at fixed
    #       b is a reparametrisation b_eff = b + b' of the O(g_s^4) sector; it is
    #       compensated here by b = 2 - b';
    #   (ii) compensation is exact only at O(b'), because M T = (u + LX) + (3b'/(c3 g))
    #       N^T chi shifts the chi kinetic operator by (b'^2/(40 c3)) N M^{-1} N^T at the
    #       SAME order g^2 -- an M^{-1} object. Hence the scan in b': the residual O(g_s^4)
    #       breaking falls as b'^2 while the leading out-of-span response falls as b'.
    # The gate is on the ABSOLUTE out-of-span coefficient (V7-column units), not on the
    # share: the share divides by the response norm, which the in-span reparametrisation
    # response inflates.
    # Gate, stated before the numbers: the C2-perp gate certifies "no out-of-span
    # coefficient above gamma_min"; C6 must produce one ABOVE gamma_min, i.e. exactly the
    # complementary statement. The factor by which it exceeds gamma_min is reported.
    print("  C6 falsification leg, scan in b' (gate: perp coefficient > gamma_min):")
    c6_perp = {}
    for bpv, comp in ((BPS, True), (BPS, False), (BP, True), (BP, False)):
        cod = {**co, "bp": bpv, "b": (2.0 - bpv) if comp else 2.0}
        ybp, _, _, _, c4b = deficit(t, psis, cod, wins)
        dbp = ybp - y0
        cbp, _, pbp_share, _, _ = project(dbp, amat)
        pabs = perp_coeff(dbp, amat)
        c6_perp[(bpv, comp)] = (cbp, pabs, pbp_share)
        tag = f"b' = {bpv}, b = {cod['b']}" + ("" if comp else "  [SUPERSEDED design]")
        print(
            f"    {tag}: response {np.array2string(cbp, precision=4)}, "
            f"perp coeff {pabs:.4f} (= {pabs / max(gmin, 1e-300):.1f} gamma_min), "
            f"perp share {pbp_share:.3f}, max |7! c4| {np.max(np.abs(c4b)):.2e}"
        )
        if comp and bpv == BP:
            report(
                "C6-outside",
                pabs > gmin,
                f"compensated b' = {bpv}: out-of-span coefficient {pabs:.4f} in "
                f"V7-column units, against the C2-perp detection threshold "
                f"gamma_min = {gmin:.4f} (gate > gamma_min: C2-perp certifies that no "
                f"out-of-span coefficient above gamma_min is present at b' = 0, where "
                f"the deficit has {perp_coeff(y0, amat):.4f}; C6 must produce one above "
                f"it)",
            )
    # The response must GROW with b' (linear at leading order, b'^2 corrections on top):
    # a fixed background would not. Gate > 3 for the ratio at b' = 0.5 over b' = 0.1,
    # where exact linearity would give 5.
    ratio = c6_perp[(BP, True)][1] / max(c6_perp[(BPS, True)][1], 1e-300)
    report(
        "C6-scan",
        ratio > 3.0,
        f"compensated out-of-span coefficient grows from {c6_perp[(BPS, True)][1]:.4f} "
        f"at b' = {BPS} to {c6_perp[(BP, True)][1]:.4f} at b' = {BP}: ratio {ratio:.2f} "
        f"(gate > 3; exact linearity in b' would give {BP / BPS:.0f})",
    )

    # Diagnosis of the superseded design, run at the small b' of the scan where the
    # neglected O(b'^2) corrections are ~0.3 % of the chi kinetic: at leading order in b',
    # switching b' on at fixed b is the reparametrisation b_eff = 2 + b', whose S1
    # signature is 7! [ (2+b')^2 - 4 ] / (-6000). That is what the old design measured.
    s1_pred = FACT7 * (
        (1.0 / 3000 - (2.0 + BPS) ** 2 / 6000) - (1.0 / 3000 - 4.0 / 6000)
    )
    s1_meas = c6_perp[(BPS, False)][0][1] - c6_perp[(BPS, True)][0][1]
    report(
        "C6-artefact",
        abs(s1_meas - s1_pred) / abs(s1_pred) < 0.10,
        f"at b' = {BPS}, the S1 response of the uncompensated leg minus that of the "
        f"compensated leg = {s1_meas:+.4f}, against the reparametrisation prediction "
        f"{s1_pred:+.4f}: the uncompensated design's response is dominated by "
        f"b_eff -> {2.0 + BPS}, not by the Sigma_3 mixing (this is why the superseded "
        f"0.10 share gate was mis-specified)",
    )
    pbp = c6_perp[(BP, True)][1]

    # ---------- C7: the sextic split ----------
    print("  C7 scan of the sextic split:")
    alphas = []
    for c6 in (0.0, 0.5, 1.0):
        cc = {**co, "c6": c6, "c3": 1.0 - c6}
        yc, rc_, _, _, _ = deficit(t, psis, cc, wins)
        cf, _, pc, _, _ = project(yc, amat)
        alphas.append(cf[1])
        dchi = -cf[2] / rcoef["d_chi"][0][2]
        print(
            f"    c6 = {c6}: alpha = {cf[1]:+.4f}, beta = {cf[2]:+.4f} "
            f"(predicted {beta_pred(c6):+.4f}), d_chi(c6) = {dchi:+.4f}, perp {pc:.2e}, "
            f"fit resid {rc_:.1e}"
        )
        report(
            f"C7-beta[c6={c6}]",
            abs(cf[2] - beta_pred(c6)) / beta_pred(c6) < 0.05,
            f"beta({c6}) = {cf[2]:+.4f} vs 7(2+c6)/5 = {beta_pred(c6):+.4f}",
        )
    spread = (max(alphas) - min(alphas)) / abs(np.mean(alphas))
    report(
        "C7-alpha",
        spread < 0.02,
        f"alpha over c6 in {{0, 1/2, 1}}: spread {spread:.2e} "
        f"(values {np.array2string(np.array(alphas), precision=4)}; expect c6-independent)",
    )

    # ---------- section 8.7: the extrapolator ladder, baseline and C6 ----------
    ladder_study(
        t, psis, amat, co, (coef[1], coef[2], f_s3, f_perp, pbp, perp_coeff(y0, amat))
    )


def c6_diagnostic(seed: int) -> None:
    """
    Which order does the C6 out-of-span statistic measure? (record 048 section 8.8)

    Critic iteration 2 observed that the superseded/compensated ratio of the out-of-span
    coefficient at b' = 0.5 is 1.5625, 1.556, 1.562 on the three seeds, i.e. (2.5/2)^2 --
    a b_eff^2 law. The two candidate sources scale differently in b_eff at FIXED b':

      * the O(g_s^5) out-of-span structures of (8.2) carry at most ONE power of b_eff
        (the b_eff b' N M^{-1} L X_1 source cross term; the K'-correction terms carry
        b_chi b'^2 and b'^3, i.e. at most linear in b_eff = b_chi + b'), so p <= 1.2;
      * the O(g_s^4) compensation defect is -1/2 J K^{-1} J with J proportional to b_eff
        and K carrying the b'^2 M^{-1} composite, hence proportional to b_eff^2 b'^2:
        p >= 1.8.

    GATE, STATED BEFORE THE NUMBERS. Fit p in |perp coeff of 7! c5| ~ b_eff^p over
    b_eff in {1.5, 2.0, 2.5, 3.0} at b' = 0.5 (b_chi = b_eff - b'). Verdict:
      p <= 1.2  -> the leg measures the O(g_s^5) mixing (C6 is an O(g_s^5) statement);
      p >= 1.8  -> the leg measures the O(g_s^4) compensation defect (C6 is NOT an
                   O(g_s^5) statement and is not established);
      otherwise -> mixed, undecided.
    POSTSCRIPT (written after the run, record 048 section 8.8): the premise of this gate is
    wrong -- eq. (8.3) has an O(g_s^5) out-of-span structure carrying b_eff^2 b'^2 as well.
    Gate 1 is kept and reported as stated, its verdict is recorded as VOID, and the order
    in g is settled by gate 2 in part (d) below.
    Controls printed with it, none of them tuned:
      * the same exponent for the out-of-span coefficient of the leg's 7! c4, which is
        PURE O(g_s^4) defect: it must come out near 2, which is what makes the estimator
        falsifiable (the sample can produce the value that would condemn c5);
      * the exponent in b' at compensated b_chi = 2 - b' (O(g_s^5) -> ~1, defect -> ~2);
      * the superseded/compensated ratio at b' = 0.1 (b_eff^2 predicts 1.1025, b_eff^1
        predicts 1.05).
    """
    print(f"\n=== seed {seed}: C6 order diagnostic (record 048 section 8.8) ===")
    t, _ = build(seed)
    rng = np.random.default_rng(seed + 500)
    psis = [rng.standard_normal(N) for _ in range(NPSI2)]
    co = dict(NOMINAL)
    amat = basis_matrix(t, psis)
    wins = [choose_window(t, p, co)[0] for p in psis]
    y0, _, _, _, c40 = deficit(t, psis, co, wins)
    gmin, _ = perp_sensitivity(y0, amat, np.random.default_rng(seed + 700))
    print(
        f"  baseline: perp coeff(7! c5) {perp_coeff(y0, amat):.4f}, "
        f"perp coeff(7! c4) {perp_coeff(c40, amat):.4f}, gamma_min {gmin:.4f}, "
        f"rms |7! c5| {np.sqrt(np.mean(y0**2)):.3e}, max |7! c4| {np.max(np.abs(c40)):.3e}"
    )

    def leg(bpv: float, bv: float):
        """(perp coeff of 7! c5, perp coeff of 7! c4, max |7! c4|) of the leg response."""
        cod = {**co, "bp": bpv, "b": bv}
        ybp, _, _, _, c4b = deficit(t, psis, cod, wins)
        return (
            perp_coeff(ybp - y0, amat),
            perp_coeff(c4b - c40, amat),
            float(np.max(np.abs(c4b))),
        )

    # (a) b_eff scan at fixed b' = 0.5 -- the decisive leg.
    beffs = (1.5, 2.0, 2.5, 3.0)
    p5, p4, m4 = [], [], []
    for be in beffs:
        a, b, c = leg(BP, be - BP)
        p5.append(a)
        p4.append(b)
        m4.append(c)
        print(
            f"  b' = {BP}, b = {be - BP:.1f} (b_eff = {be}): perp(c5) {a:.4f} "
            f"(= {a / max(gmin, 1e-300):.1f} gamma_min), perp(c4) {b:.4f}, "
            f"max |7! c4| {c:.2e}"
        )
    lb = np.log(np.array(beffs))
    exp5 = float(np.polyfit(lb, np.log(np.array(p5)), 1)[0])
    exp4 = float(np.polyfit(lb, np.log(np.array(p4)), 1)[0])
    print(
        f"  EXPONENT in b_eff at b' = {BP}: c5 out-of-span p = {exp5:.2f} "
        f"(gate: <= 1.2 O(g_s^5), >= 1.8 O(g_s^4) defect); "
        f"c4 out-of-span (control, expect ~2) p = {exp4:.2f}"
    )
    verdict = (
        "O(g_s^5)" if exp5 <= 1.2 else ("O(g_s^4) defect" if exp5 >= 1.8 else "UNDECIDED")
    )
    print(
        f"  GATE 1 seed {seed}: fires on the {verdict} side -- BUT THIS VERDICT IS VOID: "
        "eq. (8.3) of record 048 section 8.8 exhibits an O(g_s^5) out-of-span structure "
        "with the SAME b_eff^2 b'^2 law (the b'^2 composite in K^{-1} dresses the S1 "
        "direction too), which the enumeration behind gate 1 missed. What the exponent "
        "does establish is that the leg's out-of-span content is dominated by the "
        "b_eff^2 b'^2 composite dressing, not by the b_eff b' Sigma_3-mixing source. "
        "The order in g is settled by gate 2 below, not here."
    )

    # (b) b' scan at compensated b_chi = 2 - b'.
    bps = (0.1, 0.2, 0.35, 0.5)
    q5 = []
    for bp in bps:
        a, b, c = leg(bp, 2.0 - bp)
        q5.append(a)
        print(
            f"  b' = {bp}, b = {2.0 - bp:.2f} (compensated): perp(c5) {a:.4f} "
            f"(= {a / max(gmin, 1e-300):.1f} gamma_min), perp(c4) {b:.4f}, "
            f"max |7! c4| {c:.2e}"
        )
    expb = float(np.polyfit(np.log(np.array(bps)), np.log(np.array(q5)), 1)[0])
    print(
        f"  EXPONENT in b' (compensated): p = {expb:.2f} "
        f"(O(g_s^5) response ~1, O(g_s^4) defect ~2)"
    )

    # (c) superseded/compensated ratio at b' = 0.1.
    up, _, _ = leg(BPS, 2.0)
    print(
        f"  superseded/compensated ratio at b' = {BPS}: {up / max(q5[0], 1e-300):.4f} "
        f"(b_eff^2 predicts {(2.1 / 2.0) ** 2:.4f}, b_eff^1 predicts {2.1 / 2.0:.4f})"
    )

    # (d) ORDER-IN-g test. The b_eff exponent alone does NOT separate the two candidates:
    # eq. (8.3) of record 048 section 8.8 shows that the O(g_s^5) out-of-span response
    # ALSO carries a b_eff^2 b'^2 structure (2 b_eff^2 g v^T V4^{-1} kappa V4^{-1} V5_1,
    # kappa = (3b'^2/10 c3 a) N M^{-1} N^T), with the same law as the O(g_s^4) defect.
    # Only the power of g separates them, and the order fit already carries g^4 and g^5 as
    # independent columns -- so the question is whether the fitted c5 is contaminated.
    #
    # GATE, STATED BEFORE THE NUMBERS. Refit the production leg (b' = 0.5, b = 1.5) on the
    # per-probe window scaled by 1, 1/3, 1/10. A genuine O(g_s^5) coefficient is window
    # independent (the contamination from the untruncated orders >= 8 SHRINKS as the window
    # moves down). A leakage of the O(g_s^4) defect into the g^5 column grows as 1/g, i.e.
    # by about 3 and 10 over the same shifts. Verdict:
    #   max/min < 2 over the three windows          -> genuine O(g_s^5);
    #   growth tracking 1/g (>= 3 per decade down)  -> leakage of the O(g_s^4) defect.
    # Control (not tuned): the leg's out-of-span coefficient AT ORDER 4 must itself be
    # window independent, and the baseline alpha must stay within the C4 gate. If the
    # order-4 control moves, the window shift is not clean and the test is void.
    print("  (d) order-in-g test: production leg refitted on scaled windows")
    row5, row4 = [], []
    for sc in (1.0, 1.0 / 3.0, 0.1):
        wsc = [np.array(w) * sc for w in wins]
        yb, rb, _, _, c4b = deficit(t, psis, {**co, "bp": BP, "b": 1.5}, wsc)
        ya, ra, _, _, c4a = deficit(t, psis, co, wsc)
        ca, _, _, _, _ = project(ya, amat)
        pc5 = perp_coeff(yb - ya, amat)
        pc4 = perp_coeff(c4b - c4a, amat)
        row5.append(pc5)
        row4.append(pc4)
        print(
            f"    window x {sc:.3f}: perp(c5) {pc5:.4f}, perp(c4) {pc4:.4f}, "
            f"baseline alpha {ca[1]:+.4f}, max rel fit residual {max(rb, ra):.1e}"
        )
    g5 = max(row5) / max(min(row5), 1e-300)
    g4 = max(row4) / max(min(row4), 1e-300)
    print(
        f"  ORDER-IN-g: perp(c5) max/min over the three windows = {g5:.2f} "
        f"(gate < 2 genuine O(g_s^5); ~10 = leakage of the O(g_s^4) defect); "
        f"order-4 control max/min = {g4:.2f}"
    )


def main() -> int:
    """Run all seeds; nonzero exit code on any failure."""
    print(__doc__.splitlines()[1])
    print(f"seeds {SEEDS}")
    for seed in SEEDS:
        run(seed)
    for seed in SEEDS:
        run2(seed)
    print(
        f"\nCHECK COUNT: {tally['CHECK']} independent checks + {tally['DERIVED']} derived "
        f"checks (corollaries of others) + {tally['BREAK']} break legs; "
        f"{fallbacks['n']} windows came from the fallback branch of choose_window"
    )
    print(
        f"SUMMARY: {'ALL CHECKS PASS' if not failures else 'FAILURES: ' + ', '.join(failures)}"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    if "--c6-diagnostic" in sys.argv:
        # Diagnostic of record 048 section 8.8, run on its own (it does not add checks to
        # the tally and does not change the verdict of any C-check).
        for _s in SEEDS:
            c6_diagnostic(_s)
        sys.exit(0)
    sys.exit(main())
