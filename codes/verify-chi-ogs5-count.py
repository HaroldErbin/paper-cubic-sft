#!/usr/bin/env python3
"""
Machine checks for derivation 038 — the O(g_s^5) counting argument.

Counting argument for the wrong-sign-partner (chi) scheme of R24/017.

Every printed line is tagged by its kind, and the kinds are counted separately at the
end, because they carry very different evidential weight:

  (CHECK)  a falsifiable test: a concrete wrong result would make it FAIL.
  (DUP)    a falsifiable statement that is IMPLIED by a CHECK printed above it, hence
           carries no evidence beyond that check. Printed because it states the claim
           in the language of the claim-tree node it belongs to.
  (IDENT)  a bookkeeping identity that CANNOT fail. For a fully symmetric tensor,
           contracting four indices with Psi is the same einsum however the four are
           grouped as (P,P) or (p3,Psi); such a line records the index bookkeeping of
           the Veronese collapse and is reported as an identity, not as evidence.
  (BREAK)  a deliberate wrong input that must make the corresponding check FAIL.
  (WEAK)   a break leg that is logically implied by the CHECK it accompanies, so it
           cannot fail while that check passes. Kept for readability, counted apart.

WHAT IS VERIFIED, falsifiably (each check is named after a claim-tree node of 038):

  N1     ORDER FORMULA (2.1), by log-log slope at a JOINT Newton saddle in
         (Sigma, chi): the on-shell contribution of the chi sector scales as g^4,
         of c_chi V5(chi,chi,Psi) and d_chi V6(chi,Sigma,Sigma) as g^5, and of
         e_chi V6(chi,chi,Sigma) as g^6 — four DISTINCT predicted exponents.
  N2     SADDLE ORDERS: |chi_*| = O(g) (o(chi) = 1, the mechanism of the scheme),
         |Sigma_* - P| = O(g) (o(Sigma) = 0), and the leading chi saddle equals
         eq. (2.2) of 038 INCLUDING its coefficient,
         chi_* -> -(g b_chi / (10 a_chi)) V4^{-1} v, measured at a_chi = 1.
  N3/A7  the four order-7 invariants {V7(Psi^7), S1, S2, S3} are independent as
         functions of Psi, and the strand-split S3 is not in span{S1,S2} — this is
         what makes the strand-locality lemma (038 section 3.2) load-bearing.
  N6e    DIAGONALITY / the closure count proper: the three leading on-shell values
         {V5(chi*,chi*,Psi), V6(chi*,P,P), V7(Psi^7)} of the three generators are
         LINEARLY INDEPENDENT as functions of Psi (rank 3). If any two coincided —
         which is exactly what happens for the redundant partitions of N6c/N6d —
         the count of 038 section 5 would collapse and the outcome would not be
         "enough freedom".
  N9-R20 the O(g_s^4) falsifier, negative leg: with content (Psi, Sigma_2, Sigma_3)
         the ord = 4 generators have rank 1 < the deficit rank 2, and adding the chi
         direction raises the rank to 2. R20's no-go reproduced by the count.
  N9-R24 the O(g_s^4) falsifier, positive leg: chi supplies the second direction,
         V4(chi*,chi*) = v^T V4^{-1} v, independent of V6(Psi^6). The count PREDICTS
         017's closure, which is the brief's falsifier: a count predicting failure at
         O(g_s^4) would be wrong.

REPORTED AS IDENTITIES (cannot fail; they document the Veronese collapse):
  N6c, N6d (partition redundancies), the generator-label lines, the N9-R20 collapse.

WHAT IS NOT VERIFIED HERE:
  - the values (alpha, beta) of the O(g_s^5) deficit 7! A_5^chi = alpha S1 + beta S2.
    That is the matching computation, deliberately out of scope for a counting brief
    (038 section 6.2 lists what the matching must test).
  - the strand-locality lemma (038 section 3.2) and the spanning lemma N3'
    (038 section 3.1.5) are combinatorial statements about which contractions a
    whole-slot tree expansion can produce; they are proved by hand, not machine-checked.
    What is checked here is their discriminating consequence (S3 genuinely outside
    span{S1,S2}).
  - the Sigma_3 sector is absent from the scaling module, so the predicted ord = 5 of
    V7(Sigma_3,Sigma_3,Psi) is not measured; the couplings measured are the chi ones,
    which are the ones the count turns on.
  - everything above the finite-dimensional algebraic layer (standing carve-out A4).

Conventions: chi* = V4^{-1} v is used up to the overall factor -g b_chi/10 of eq. (2.2)
of 038; all checks are ratio/rank statements, insensitive to that normalisation.
References: 017 (R24), 018 section 2-5 (R25), R23 (ghost/strand bookkeeping).
"""

from __future__ import annotations

import sys
from itertools import permutations

import numpy as np

N = 4  # dim H_0
NPSI = 12  # number of random Psi probes
SEEDS = (11, 29, 7)  # seed 7 added 2026-09-21 as a third measurement of the g^5 slopes

failures: list[str] = []
tally: dict[str, int] = {'CHECK': 0, 'DUP': 0, 'IDENT': 0, 'BREAK': 0, 'WEAK': 0}


def report(name: str, ok: bool, detail: str, kind: str = 'CHECK') -> None:
    """
    Print one PASS/FAIL line and record failures.

    Args:
        name: check name, prefixed by the claim-tree node it tests.
        ok: outcome.
        detail: the quantity tested and its value.
        kind: 'CHECK' for a falsifiable test, 'DUP' for one implied by an earlier
            check, 'IDENT' for a bookkeeping identity that cannot fail (index
            bookkeeping on a fully symmetric tensor), 'BREAK' for a
            deliberate-failure leg, 'WEAK' for a break leg implied by its check.

    """
    tally[kind] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] ({kind}) {name}: {detail}")
    if not ok:
        failures.append(name)


def sym_tensor(rng: np.random.Generator, k: int) -> np.ndarray:
    """Fully symmetric random k-tensor on an N-dimensional space."""
    t = rng.standard_normal((N,) * k)
    s = np.zeros_like(t)
    perms = list(permutations(range(k)))
    for p in perms:
        s += np.transpose(t, p)
    return s / len(perms)


def v4_inv(t4: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Sym^2 inverse image of a symmetric matrix x under V4.

    V4 viewed as an N^2 x N^2 operator annihilates antisymmetric matrices, so the
    minimum-norm least-squares solution is the inverse on Sym^2 (same device as
    codes/verify-chi-partner.py).
    """
    a = t4.reshape(N * N, N * N)
    sol, *_ = np.linalg.lstsq(a, x.reshape(N * N), rcond=None)
    sol = sol.reshape(N, N)
    return 0.5 * (sol + sol.T)


def invariants(t4, t5, t6, t7, psi):
    """
    All order-7 (and the auxiliary order-6) invariants used by the count.

    Returns a dict with:
      V7d  = V7(Psi^7)                       (the contact)
      S1   = v^T V4^{-1} W V4^{-1} v         (strand-local, two propagators)
      S2   = g6^T V4^{-1} v                  (strand-local, one propagator)
      S3   = strand-split representative: the two indices of X = V4^{-1} v routed
             into two different V5 blocks (038 section 3.2 corollary)
      plus the generator values and the O(g_s^4) objects.
    """
    p = np.outer(psi, psi)
    p3 = np.einsum('i,j,k->ijk', psi, psi, psi)

    # v_{ij} = V5(., P, Psi);  W_{ij,kl} = V5(.,.,Psi);  g6_{ij} = V6(., P, P)
    v = np.einsum('ijklm,kl,m->ij', t5, p, psi)
    w = np.einsum('ijklm,m->ijkl', t5, psi)
    g6 = np.einsum('ijklmn,kl,mn->ij', t6, p, p)

    x = v4_inv(t4, v)  # chi* (up to normalisation), and the Sigma_2 deviation direction

    s1 = np.einsum('ijkl,ij,kl', w, x, x)
    s2 = np.einsum('ij,ij', g6, x)

    # strand-split S3: A[i,j,a] = V5(.,P,a) with one FREE strand a (not set to Psi)
    a_ten = np.einsum('ijkla,kl->ija', t5, p)
    b_ten = np.stack([v4_inv(t4, a_ten[:, :, a]) for a in range(N)], axis=2)
    s3 = np.einsum('ija,ijb,ab', b_ten, a_ten, x)

    v7d = np.einsum('ijklmno,i,j,k,l,m,n,o', t7, psi, psi, psi, psi, psi, psi, psi)

    return {
        'V7d': v7d,
        'S1': s1,
        'S2': s2,
        'S3': s3,
        # generators, evaluated at the leading saddles (038 section 4.2)
        'gen_S1': np.einsum('ijkl,ij,kl', w, x, x),            # V5(chi,chi,Psi)
        'gen_S2': np.einsum('ijklmn,ij,kl,mn', t6, x, p, p),   # V6(chi,Sigma,Sigma)
        'gen_S2_alt': np.einsum('ijklmn,ij,klm,n', t6, x, p3, psi),  # V6(chi,Sigma_3,Psi)
        'gen_V7_331': np.einsum('ijklmno,ijk,lmn,o', t7, p3, p3, psi),
        'gen_V7_322': np.einsum('ijklmno,ijk,lm,no', t7, p3, p, p),
        # O(g_s^4) objects for the R20/R24 falsifier
        'V6d': np.einsum('ijklmn,i,j,k,l,m,n', t6, psi, psi, psi, psi, psi, psi),
        'o4_V6SSS': np.einsum('ijklmn,ij,kl,mn', t6, p, p, p),
        'o4_V6S3S2Psi': np.einsum('ijklmn,ijk,lm,n', t6, p3, p, psi),
        'o4_V6S3S3': np.einsum('ijklmn,ijk,lmn', t6, p3, p3),
        'o4_chi': np.einsum('ijkl,ij,kl', t4, x, x),           # V4(chi*,chi*) = v V4^{-1} v
        # break-leg ingredient: a WRONG composite direction
        'bad_S1': np.einsum('ijkl,ij,kl', w, v4_inv(t4, g6), v4_inv(t4, g6)),
        # kept for the break legs (a matrix, excluded from the scalar columns below)
        'x': x,
    }


def column_rank(cols: list[np.ndarray], tol: float = 1e-8) -> tuple[int, np.ndarray]:
    """Numerical rank of a set of sampled functions, after per-column normalisation."""
    m = np.stack(cols, axis=1)
    norms = np.linalg.norm(m, axis=0)
    norms[norms == 0] = 1.0
    m = m / norms
    sv = np.linalg.svd(m, compute_uv=False)
    return int((sv > tol * sv[0]).sum()), sv


def run(seed: int) -> None:
    """Run every check for one random-tensor seed."""
    print(f"\n=== seed {seed} (N={N}, {NPSI} random Psi probes) ===")
    rng = np.random.default_rng(seed)
    t4 = sym_tensor(rng, 4)
    t5 = sym_tensor(rng, 5)
    t6 = sym_tensor(rng, 6)
    t7 = sym_tensor(rng, 7)

    psis = [rng.standard_normal(N) for _ in range(NPSI)]
    data = [invariants(t4, t5, t6, t7, psi) for psi in psis]
    col = {k: np.array([d[k] for d in data]) for k in data[0] if k != 'x'}

    def relerr(a, b):
        return float(np.max(np.abs(a - b)) / max(np.max(np.abs(a)), 1e-300))

    # --- N3/A7: independence of the order-7 basis, and S3 outside span{S1,S2} ---
    r4, sv4 = column_rank([col['V7d'], col['S1'], col['S2'], col['S3']])
    report('N3/A7-independence', r4 == 4,
           f"rank{{V7(Psi^7),S1,S2,S3}} = {r4} (expect 4), sv ratio "
           f"{sv4[-1] / sv4[0]:.2e}")
    r3, _ = column_rank([col['S1'], col['S2'], col['S3']])
    report('N3-S3-outside-span', r3 == 3,
           f"rank{{S1,S2,S3}} = {r3} (expect 3): the strand-split invariant is a "
           "genuinely new direction, so the lemma excluding it has content")

    # --- N6c: Veronese redundancy of the two chi couplings ---
    # IDENTITY, not a test: for a FULLY SYMMETRIC t6, contracting two indices with x
    # and four with Psi is the same einsum whether the four are grouped as (P,P) or
    # as (p3,Psi). It records the bookkeeping, it cannot fail.
    e = relerr(col['gen_S2'], col['gen_S2_alt'])
    report('N6c-chi-partition-redundancy', e < 1e-12,
           f"max rel |V6(chi*,P,P) - V6(chi*,p3,Psi)| = {e:.2e} "
           "(index bookkeeping on a symmetric tensor; cannot fail)", kind='IDENT')

    # --- N6d: Veronese redundancy of the two V7 couplings (same status) ---
    e1 = relerr(col['gen_V7_331'], col['V7d'])
    e2 = relerr(col['gen_V7_322'], col['V7d'])
    report('N6d-V7-partition-redundancy', max(e1, e2) < 1e-12,
           f"max rel dev of V7(p3,p3,Psi), V7(p3,P,P) from V7(Psi^7) = "
           f"{max(e1, e2):.2e} (index bookkeeping; cannot fail)", kind='IDENT')

    # --- N6e: DIAGONALITY, the closure count proper ---
    # DUPLICATE: the same three columns are a subset of the four whose rank was found
    # to be 4 in N3/A7-independence above, so rank 3 here is implied by that check.
    # Printed because it is the statement N6e makes, in N6e's language.
    rg, svg = column_rank([col['gen_V7_331'], col['gen_S1'], col['gen_S2']])
    report('N6e-generator-rank', rg == 3,
           f"rank of the three generator values = {rg} (expect 3), sv ratio "
           f"{svg[-1] / svg[0]:.2e} -> the 3x3 matching system is nonsingular "
           "(implied by N3/A7-independence)", kind='DUP')
    # and the generators really are the claimed invariants (S1, S2), not each other's.
    # Both legs are the same contraction written twice (definitional); their evidential
    # content is supplied by BREAK-wrong-composite and BREAK-wrong-tensor below.
    e3 = relerr(col['gen_S1'], col['S1'])
    report('N6e-generator-labels', e3 < 1e-12,
           f"V5(chi*,chi*,Psi) == S1 to {e3:.2e}; V6(chi*,P,P) == S2 to "
           f"{relerr(col['gen_S2'], col['S2']):.2e} (both definitional)", kind='IDENT')

    # --- N9-R20: the O(g_s^4) falsifier, negative leg ---
    # The COLLAPSE leg (all three ord=4 generators equal V6(Psi^6)) is again index
    # bookkeeping on a symmetric t6; the RANK leg is the substantive statement, since
    # rank 1 < 2 is what reproduces R20's no-go.
    e4 = max(relerr(col['o4_V6SSS'], col['V6d']),
             relerr(col['o4_V6S3S2Psi'], col['V6d']),
             relerr(col['o4_V6S3S3'], col['V6d']))
    report('N9-R20-collapse', e4 < 1e-12,
           f"ord=4 generators all equal V6(Psi^6) (max rel dev {e4:.2e}; bookkeeping)",
           kind='IDENT')
    r20, _ = column_rank([col['o4_V6SSS'], col['o4_V6S3S2Psi'], col['o4_V6S3S3'],
                          col['o4_chi']])
    r20a, _ = column_rank([col['o4_V6SSS'], col['o4_V6S3S2Psi'], col['o4_V6S3S3']])
    report('N9-R20-rank1', r20a == 1 and r20 == 2,
           f"rank of the ord=4 generators WITHOUT chi = {r20a} (expect 1) < deficit "
           f"rank 2; adding the chi direction raises it to {r20} (expect 2). The pair "
           "of ranks is falsifiable: a 2 on the left would break R20's no-go")

    # --- N9-R24: the O(g_s^4) falsifier, positive leg ---
    # DUPLICATE: given the collapse identity above (the three ord=4 generators all equal
    # V6(Psi^6)), these are the same two columns as the r20 = 2 leg of N9-R20-rank1.
    r24, sv24 = column_rank([col['V6d'], col['o4_chi']])
    report('N9-R24-rank2', r24 == 2,
           f"rank{{V6(Psi^6), V4(chi*,chi*) = v V4^{{-1}} v}} = {r24} (expect 2), "
           f"sv ratio {sv24[-1] / sv24[0]:.2e} -> chi supplies the missing direction, "
           "the count predicts 017's closure (implied by N9-R20-rank1)", kind='DUP')

    # --- BREAK LEGS: the checks must be able to fail ---
    bad = relerr(col['bad_S1'], col['S1'])
    report('BREAK-wrong-composite', bad > 1e-3,
           f"replacing chi* = V4^{{-1}}v by V4^{{-1}}g6 breaks the S1 identification "
           f"(rel dev {bad:.2e}) -> N6e-generator-labels is not tautological",
           kind='BREAK')
    # replaces the former BREAK-perturbed-S2 (which multiplied a column by 1.0001 and
    # so tested floating-point arithmetic): here the S2 leg is recomputed with an
    # INDEPENDENT sextic tensor, a wrong physical input rather than a wrong last digit.
    rng_bad = np.random.default_rng(seed + 1000)
    t6_bad = sym_tensor(rng_bad, 6)
    gen_s2_wrong = []
    for d, psi_d in zip(data, psis, strict=True):
        p_d = np.outer(psi_d, psi_d)
        gen_s2_wrong.append(np.einsum('ijklmn,ij,kl,mn', t6_bad, d['x'], p_d, p_d))
    e_bad2 = relerr(np.array(gen_s2_wrong), col['S2'])
    report('BREAK-wrong-tensor', e_bad2 > 1e-3,
           f"computing V6(chi*,P,P) with an independent sextic tensor breaks the S2 "
           f"identification (rel dev {e_bad2:.2e}) -> the S2 leg is sensitive to the "
           "vertex, not only to the index pattern", kind='BREAK')
    r_bad, _ = column_rank([col['gen_V7_331'], col['gen_V7_322'], col['gen_S1']])
    report('BREAK-degenerate-generators', r_bad == 2,
           f"using the two REDUNDANT V7 partitions as if independent gives rank "
           f"{r_bad} (expect 2, not 3) -> the rank test in N6e can detect degeneracy",
           kind='BREAK')


# ---------------------------------------------------------------------------
# Scaling test of the order formula (2.1) and of the saddle orders (N1, N2, N6, N8).
#
# Instrument copied (NOT imported: codes/verify-chi-partner.py is left untouched)
# from codes/verify-chi-partner.py: generic symmetric tensors, a JOINT Newton saddle
# in (Sigma, chi) on the symmetric subspace, and a log-log slope fit. Extended here
# with the two O(g_s^5) couplings c_chi V5(chi,chi,Psi), d_chi V6(chi,Sigma,Sigma)
# and with e_chi V6(chi,chi,Sigma) (predicted ord = 6).
#
# Predictions of (2.1), ord = (sum_i s_i - 2) + sum_i o_i with o(chi) = 1:
#   chi sector [a_chi V4(chi,chi) + b_chi V5(chi,Sigma,Psi)]        ord = 4
#   c_chi V5(chi,chi,Psi)                                           ord = 5
#   d_chi V6(chi,Sigma,Sigma)                                       ord = 5
#   e_chi V6(chi,chi,Sigma)                                         ord = 6
# and N2: |chi_*| = O(g) with chi_* -> -(g b_chi / 10) V4^{-1} v   (eq. 2.2),
#         |Sigma_* - P| = O(g)                                     (o(Sigma) = 0).
# The four predicted exponents are distinct, so the test discriminates: a coupling
# landing one order lower or higher than (2.1) says would be seen.
# ---------------------------------------------------------------------------


def _saddle(t4, t5, t6, psi, g, coeff):
    """
    Joint Newton saddle for (Sigma, chi) at coupling g.

    Args:
        t4: generic symmetric quartic vertex.
        t5: generic symmetric quintic vertex.
        t6: generic symmetric sextic vertex.
        psi: off-shell Psi.
        g: string coupling.
        coeff: dict with a_chi, b_chi, c_chi, d_chi, e_chi.

    Returns:
        (S, C, value) with value the cubic action at the saddle.

    """
    from scipy.optimize import root

    p = np.outer(psi, psi)
    a, b, c, d, e = (coeff[k] for k in ('a_chi', 'b_chi', 'c_chi', 'd_chi', 'e_chi'))

    def s_cub(s_mat, c_mat):
        # the Psi-only terms (T2, T3) are common to every branch compared below and
        # cancel in every difference taken, so they are omitted
        val = (- g**2 / 24 * np.einsum('ijkl,ij,kl', t4, s_mat, s_mat)
               + g**2 / 12 * np.einsum('ijkl,ij,kl', t4, s_mat, p)
               + g**3 / 120 * np.einsum('ijklm,ij,kl,m', t5, s_mat, s_mat, psi)
               + g**4 / 720 * np.einsum('ijklmn,ij,kl,mn', t6, s_mat, s_mat, s_mat))
        val += (a * g**2 / 24 * np.einsum('ijkl,ij,kl', t4, c_mat, c_mat)
                + b * g**3 / 120 * np.einsum('ijklm,ij,kl,m', t5, c_mat, s_mat, psi)
                + c * g**3 / 120 * np.einsum('ijklm,ij,kl,m', t5, c_mat, c_mat, psi)
                + d * g**4 / 720 * np.einsum('ijklmn,ij,kl,mn', t6, c_mat, s_mat, s_mat)
                + e * g**4 / 720 * np.einsum('ijklmn,ij,kl,mn', t6, c_mat, c_mat, s_mat))
        return val

    def grads(s_mat, c_mat):
        gs = (-g**2 / 12 * np.einsum('ijkl,kl->ij', t4, s_mat)
              + g**2 / 12 * np.einsum('ijkl,kl->ij', t4, p)
              + g**3 / 60 * np.einsum('ijklm,kl,m->ij', t5, s_mat, psi)
              + g**4 / 240 * np.einsum('ijklmn,kl,mn->ij', t6, s_mat, s_mat)
              + b * g**3 / 120 * np.einsum('ijklm,kl,m->ij', t5, c_mat, psi)
              + d * g**4 / 360 * np.einsum('ijklmn,kl,mn->ij', t6, c_mat, s_mat)
              + e * g**4 / 720 * np.einsum('ijklmn,kl,mn->ij', t6, c_mat, c_mat))
        gc = (a * g**2 / 12 * np.einsum('ijkl,kl->ij', t4, c_mat)
              + b * g**3 / 120 * np.einsum('ijklm,kl,m->ij', t5, s_mat, psi)
              + c * g**3 / 60 * np.einsum('ijklm,kl,m->ij', t5, c_mat, psi)
              + d * g**4 / 720 * np.einsum('ijklmn,kl,mn->ij', t6, s_mat, s_mat)
              + e * g**4 / 360 * np.einsum('ijklmn,kl,mn->ij', t6, c_mat, s_mat))
        return gs, gc

    iu = np.triu_indices(N)
    nd = len(iu[0])
    wt = np.where(iu[0] == iu[1], 1.0, 2.0)

    def unpack(y):
        s_mat = np.zeros((N, N))
        c_mat = np.zeros((N, N))
        s_mat[iu] = y[:nd]
        s_mat += np.triu(s_mat, 1).T
        c_mat[iu] = y[nd:]
        c_mat += np.triu(c_mat, 1).T
        return s_mat, c_mat

    def f(y):
        gs, gc = grads(*unpack(y))
        return np.concatenate([gs[iu] * wt, gc[iu] * wt]) / g**2

    y0 = np.concatenate([p[iu], np.zeros(nd)])
    sol = root(f, y0, method='hybr', tol=1e-14)
    assert np.max(np.abs(f(sol.x))) < 1e-9, f"saddle not converged at g={g}"
    s_mat, c_mat = unpack(sol.x)
    return s_mat, c_mat, s_cub(s_mat, c_mat)


def _slope(fun, g0: float = 1.5e-2) -> float:
    """Log-log slope of |fun(g)| over [g0/5, g0] (as in codes/verify-chi-partner.py)."""
    gs = g0 * np.array([1.0, 0.7, 0.5, 0.35, 0.2])
    vals = np.array([abs(fun(g)) for g in gs])
    return float(np.polyfit(np.log(gs), np.log(vals), 1)[0])


def run_scaling(seed: int) -> None:
    """Numerical test of the order formula (2.1) and of the saddle orders."""
    print(f"\n=== seed {seed}: scaling test of the order formula (2.1) ===")
    rng = np.random.default_rng(seed)
    t4 = sym_tensor(rng, 4)
    t5 = sym_tensor(rng, 5)
    t6 = sym_tensor(rng, 6)
    psi = rng.standard_normal(N)

    base = {'a_chi': 1.0, 'b_chi': 0.0, 'c_chi': 0.0, 'd_chi': 0.0, 'e_chi': 0.0}
    chi = {**base, 'b_chi': 2.0}

    def val(coeff):
        return lambda g: _saddle(t4, t5, t6, psi, g, coeff)[2]

    # --- N2 / eq. (2.2): o(chi) = 1 and the predicted leading coefficient ---
    v = np.einsum('ijklm,k,l,m->ij', t5, psi, psi, psi)
    chi_pred = -(2.0 / 10.0) * v4_inv(t4, v)  # -(b_chi/10) V4^{-1} v, eq. (2.2)
    sl_chi = _slope(lambda g: np.linalg.norm(_saddle(t4, t5, t6, psi, g, chi)[1]))
    report('N2-o(chi)=1', 0.8 < sl_chi < 1.2,
           f"|chi_*| scales as g^{sl_chi:.3f} (expect 1: o(chi) = 1, not 0)")
    sl_c2 = _slope(lambda g: np.linalg.norm(
        _saddle(t4, t5, t6, psi, g, chi)[1] / g - chi_pred))
    report('N2-eq(2.2)-coefficient', sl_c2 > 0.8,
           f"|chi_*/g + (b_chi/10) V4^{{-1}} v| scales as g^{sl_c2:.3f} (expect >= 1: "
           "the LEADING chi saddle equals eq. (2.2) including its coefficient)")
    sl_x = _slope(lambda g: np.linalg.norm(
        _saddle(t4, t5, t6, psi, g, chi)[0] - np.outer(psi, psi)))
    report('N2-o(Sigma)=0', 0.8 < sl_x < 1.2,
           f"|Sigma_* - P| scales as g^{sl_x:.3f} (expect 1: Veronese saddle, o = 0, "
           "with an O(g) deviation X)")

    # --- N1 / N6 / N8: the order of each coupling's on-shell contribution ---
    for name, coeff, ref, pred in (
        ('chi-sector [V4(chi,chi)+V5(chi,Sigma,Psi)]', chi, base, 4),
        ('c_chi V5(chi,chi,Psi)', {**chi, 'c_chi': 1.0}, chi, 5),
        ('d_chi V6(chi,Sigma,Sigma)', {**chi, 'd_chi': 1.0}, chi, 5),
        ('e_chi V6(chi,chi,Sigma)', {**chi, 'e_chi': 1.0}, chi, 6),
    ):
        f_on, f_off = val(coeff), val(ref)
        def diff(g, f_on=f_on, f_off=f_off):
            return f_on(g) - f_off(g)
        sl = _slope(diff)
        # Second, lower fit window: an O(g^(pred+1)) contamination of the measured
        # exponent must shrink when the window is pushed down, a wrong leading order
        # must not. This is what separates the two explanations of a slope offset.
        sl_low = _slope(diff, g0=5e-3)
        report(f'N1-ord[{name}]', abs(sl - pred) < 0.3,
               f"on-shell contribution scales as g^{sl:.3f} on [3e-3, 1.5e-2] and "
               f"g^{sl_low:.3f} on [1e-3, 5e-3], (2.1) predicts g^{pred}")
        if pred == 5:
            # WEAK: implied by the check above (|sl - 5| < 0.3 forces |sl - 4| > 0.5).
            report(f'WEAK-ord[{name}]-not-4', abs(sl - 4) > 0.5,
                   f"the measured exponent {sl:.3f} is NOT 4 (implied by the check "
                   "above; kept as a readability restatement of the discrimination)",
                   kind='WEAK')


def main() -> int:
    """Run all seeds and return a nonzero exit code on any failure."""
    print(__doc__.splitlines()[1])
    for seed in SEEDS:
        run(seed)
        run_scaling(seed)
    total = sum(tally.values())
    print(f"\nCHECK COUNT: {tally['CHECK']} independent falsifiable checks + "
          f"{tally['DUP']} implied checks + {tally['IDENT']} bookkeeping identities + "
          f"{tally['BREAK']} break legs + {tally['WEAK']} weak break legs = {total}")
    print(f"SUMMARY: {'ALL CHECKS PASS' if not failures else 'FAILURES: ' + ', '.join(failures)}")
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
