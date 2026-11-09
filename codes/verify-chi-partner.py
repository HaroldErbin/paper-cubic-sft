#!/usr/bin/env python3
"""
verify-chi-partner.py — the wrong-sign (Liouville-type) partner chi at O(g_s^4).

Claim (Fable session 2026-07-07, from Harold's 2d-gravity analogy S = R Delta^{-1} R):
the R17 feedback +(g^4/600) v V4^{-1} v — the induced nonlocal action of the Sigma_2
deviation, exactly of the Liouville R*Delta^{-1}*R form with R <-> v, Delta <-> K_Psi,
phi <-> deviation — can be RE-LOCALISED by a second Sym^2 auxiliary chi with a
WRONG-SIGN elementary V4 kinetic term and an elementary cubic coupling V5(chi,Sigma,Psi):

    S_chi = + a_chi (g^2/4!) V4(chi,chi) + b_chi (g^3/5!) V5(chi, Sigma, Psi),

with the on-shell coefficient matching FORCING b_chi^2 / a_chi = 4, i.e. (a,b)=(1,2)
(the same 1:2 HS normalisation as every other pair). Consequence: the PURE GEOMETRIC
sextic c6=1 closes at O(g^4) — no composite W6, no Sigma_3 — with field content
(Psi, Sigma_2, chi). This evades R20's no-go (whose content was Sigma_2 + Sigma_3 only)
via an indefinite-signature Sym^2 pair, supporting the T6-bis reading (chi ~ the
gauge-fixed "up" partner of an unconstrained two-string field).

Method: generic symmetric tensors T2..T6 (NO L_infty input), joint Newton saddle for
(Sigma, chi), Richardson extrapolation of the on-shell mismatch
D(g) = [S_cubic(saddle) - S_eff(g)] / g^4  as g -> 0.
The on-shell action at generic off-shell Psi is the generating function of all tree
diagrams, so this tests contact reproduction AND exchange-class cancellation at once.

Checks:
 (1) baseline, no chi:            D(g) -> + vV4^{-1}v / 600  (the R19/R20 residual)
 (2) chi with (a,b)=(1,2):        D(g) -> 0                  (closure)
 (3) chi with b=1 (wrong coeff):  D(g) -> (1 - b^2/4) vV4^{-1}v / 600 (forcing)
 (4) O(g^3) safety, chi present:  D3(g) = [S-S_eff]/g^3 -> 0 (no 5-pt contamination)
 (5) seed robustness: (1)+(2) on a second seed.
"""

import numpy as np
from scipy.optimize import root

N = 4  # dim H_0


def sym_tensor(rng, k):
    t = rng.standard_normal((N,) * k)
    # full symmetrisation
    from itertools import permutations
    s = np.zeros_like(t)
    perms = list(permutations(range(k)))
    for p in perms:
        s += np.transpose(t, p)
    return s / len(perms)


def build(seed):
    rng = np.random.default_rng(seed)
    T2 = sym_tensor(rng, 2)
    T3 = sym_tensor(rng, 3)
    T4 = sym_tensor(rng, 4)
    T5 = sym_tensor(rng, 5)
    T6 = sym_tensor(rng, 6)
    Psi = rng.standard_normal(N)
    return T2, T3, T4, T5, T6, Psi


def actions(T2, T3, T4, T5, T6, Psi, a_chi, b_chi, with_chi):
    P = np.outer(Psi, Psi)

    def S_eff(g):
        return (0.5 * np.einsum('ij,i,j', T2, Psi, Psi)
                + g / 6 * np.einsum('ijk,i,j,k', T3, Psi, Psi, Psi)
                + g**2 / 24 * np.einsum('ijkl,i,j,k,l', T4, Psi, Psi, Psi, Psi)
                + g**3 / 120 * np.einsum('ijklm,i,j,k,l,m', T5, Psi, Psi, Psi, Psi, Psi)
                + g**4 / 720 * np.einsum('ijklmn,i,j,k,l,m,n', T6, Psi, Psi, Psi, Psi, Psi, Psi))

    def S_cub(S, C, g):
        val = (0.5 * np.einsum('ij,i,j', T2, Psi, Psi)
               + g / 6 * np.einsum('ijk,i,j,k', T3, Psi, Psi, Psi)
               - g**2 / 24 * np.einsum('ijkl,ij,kl', T4, S, S)
               + g**2 / 12 * np.einsum('ijkl,ij,kl', T4, S, P)
               + g**3 / 120 * np.einsum('ijklm,ij,kl,m', T5, S, S, Psi)
               + g**4 / 720 * np.einsum('ijklmn,ij,kl,mn', T6, S, S, S))
        if with_chi:
            val += (a_chi * g**2 / 24 * np.einsum('ijkl,ij,kl', T4, C, C)
                    + b_chi * g**3 / 120 * np.einsum('ijklm,ij,kl,m', T5, C, S, Psi))
        return val

    def grad(x, g):
        S = x[:N * N].reshape(N, N)
        C = x[N * N:].reshape(N, N)
        gS = (-g**2 / 12 * np.einsum('ijkl,kl->ij', T4, S)
              + g**2 / 12 * np.einsum('ijkl,kl->ij', T4, P)
              + g**3 / 60 * np.einsum('ijklm,kl,m->ij', T5, S, Psi)
              + g**4 / 240 * np.einsum('ijklmn,kl,mn->ij', T6, S, S))
        if with_chi:
            gS += b_chi * g**3 / 120 * np.einsum('ijklm,kl,m->ij', T5, C, Psi)
            gC = (a_chi * g**2 / 12 * np.einsum('ijkl,kl->ij', T4, C)
                  + b_chi * g**3 / 120 * np.einsum('ijklm,kl,m->ij', T5, S, Psi))
        else:
            gC = C  # force C = 0
        # rescale to O(1) so the root-finder tolerances are meaningful at small g
        return np.concatenate([gS.ravel(), gC.ravel()]) / g**2

    # parametrise on the symmetric subspace (the full-matrix Jacobian is singular
    # along antisymmetric directions, which degrades hybr's convergence)
    iu = np.triu_indices(N)
    wt = np.where(iu[0] == iu[1], 1.0, 2.0)  # chain-rule weight d/dy of off-diag pairs

    def y_to_mats(y):
        d = len(iu[0])
        S = np.zeros((N, N)); C = np.zeros((N, N))
        S[iu] = y[:d]; S += np.triu(S, 1).T
        C[iu] = y[d:]; C += np.triu(C, 1).T
        return S, C

    def grad_red(y, g):
        S, C = y_to_mats(y)
        gfull = grad(np.concatenate([S.ravel(), C.ravel()]), g)
        gS = gfull[:N * N].reshape(N, N)
        gC = gfull[N * N:].reshape(N, N)
        return np.concatenate([gS[iu] * wt, gC[iu] * wt])

    def saddle_value(g):
        d = len(iu[0])
        y0 = np.concatenate([np.outer(Psi, Psi)[iu], np.zeros(d)])
        sol = root(lambda y: grad_red(y, g), y0, method='hybr', tol=1e-14)
        gr = np.max(np.abs(grad_red(sol.x, g)))
        assert gr < 1e-10, f"saddle not converged at g={g}: scaled grad {gr}"
        S, C = y_to_mats(sol.x)
        return S_cub(S, C, g)

    return S_eff, saddle_value


def vV4inv_v(T4, T5, Psi):
    """v_{ij} = T5_{ijklm} Psi_k Psi_l Psi_m ; solve (T4 X)_{ij}=v_{ij} on Sym^2; return <v,X>."""
    v = np.einsum('ijklm,k,l,m->ij', T5, Psi, Psi, Psi)
    A = T4.reshape(N * N, N * N)  # symmetric operator; kernel = antisym matrices
    # v is symmetric, so the minimum-norm lstsq solution is the Sym^2 inverse image
    X = np.linalg.lstsq(A, v.ravel(), rcond=1e-10)[0]
    return float(v.ravel() @ X)


def richardson_limit(f, g0=1e-2):
    """f(g) = D0 + c1 g + O(g^2): 2-point Richardson, 2 f(g0/2) - f(g0)."""
    return 2 * f(g0 / 2) - f(g0)


def loglog_slope(f, g0=3e-2):
    """Fit the scaling exponent of |f(g)| over the window [g0/5, g0]
    (kept above the float-noise floor of the g^-4-amplified mismatch)."""
    gs = g0 * np.array([1.0, 0.7, 0.5, 0.35, 0.2])
    vals = np.array([abs(f(g)) for g in gs])
    return np.polyfit(np.log(gs), np.log(vals), 1)[0]


def run(seed, verbose=True):
    T2, T3, T4, T5, T6, Psi = build(seed)
    target = vV4inv_v(T4, T5, Psi) / 600.0
    results = {}

    for tag, (a, b, wc) in {
        'no-chi': (1.0, 0.0, False),
        'chi(1,2)': (1.0, 2.0, True),
        'chi(1,1)': (1.0, 1.0, True),
    }.items():
        S_eff, sv = actions(T2, T3, T4, T5, T6, Psi, a, b, wc)
        D4 = lambda g: (sv(g) - S_eff(g)) / g**4
        results[tag] = richardson_limit(D4)

    # O(g^3) safety with chi present
    S_eff, sv = actions(T2, T3, T4, T5, T6, Psi, 1.0, 2.0, True)
    D3 = lambda g: (sv(g) - S_eff(g)) / g**3
    results['g3-safety'] = richardson_limit(D3)

    # scaling exponent of the residual with chi(1,2): should be ~1 (residual = O(g^5))
    S_eff, sv = actions(T2, T3, T4, T5, T6, Psi, 1.0, 2.0, True)
    D4c = lambda g: (sv(g) - S_eff(g)) / g**4
    results['chi-slope'] = loglog_slope(D4c)

    if verbose:
        print(f"--- seed {seed} ---")
        print(f"  target vV4^-1 v / 600           = {target:+.6e}")
        print(f"  (1) no-chi mismatch/g^4  -> {results['no-chi']:+.6e}"
              f"   (rel err vs target {abs(results['no-chi']-target)/abs(target):.2e})")
        print(f"  (2) chi(a=1,b=2)         -> {results['chi(1,2)']:+.6e}"
              f"   (|.|/|target| = {abs(results['chi(1,2)'])/abs(target):.2e})")
        pred_11 = (1 - 1.0 / 4) * target
        print(f"  (3) chi(a=1,b=1)         -> {results['chi(1,1)']:+.6e}"
              f"   (predicted (1-b^2/4)*target = {pred_11:+.6e},"
              f" rel err {abs(results['chi(1,1)']-pred_11)/abs(pred_11):.2e})")
        print(f"  (4) O(g^3) mismatch/g^3  -> {results['g3-safety']:+.6e} (should be ~0)")
        print(f"  (5) chi(1,2) residual scaling exponent = {results['chi-slope']:.3f}"
              f" (should be ~1: mismatch = O(g^5))")
    return results, target


if __name__ == '__main__':
    npass = 0
    ntot = 0

    for seed in (7, 23):
        res, target = run(seed)
        scale = abs(target)

        checks = [
            ('(1) no-chi residual = vV4^-1v/600 (1% level)',
             abs(res['no-chi'] - target) / scale < 1e-2),
            ('(2) chi(1,2) closes (residual < 1% of target)',
             abs(res['chi(1,2)']) / scale < 1e-2),
            ('(3) coefficient forced: b=1 leaves (1-b^2/4)*residual (1%)',
             abs(res['chi(1,1)'] - 0.75 * target) / scale < 1e-2),
            ('(4) no O(g^3) contamination',
             abs(res['g3-safety']) < 1e-3 * max(1.0, scale)),
            ('(5) chi(1,2) residual is O(g^5): scaling exponent in [0.7,1.5]',
             0.7 < res['chi-slope'] < 1.5),
        ]
        for name, ok in checks:
            ntot += 1
            npass += ok
            print(f"  [{'PASS' if ok else 'FAIL'}] seed {seed}: {name}")

    print(f"\n{npass}/{ntot} checks PASS")
    raise SystemExit(0 if npass == ntot else 1)
