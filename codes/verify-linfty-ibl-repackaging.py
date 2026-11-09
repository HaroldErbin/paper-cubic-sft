"""
Toy verification for derivation 026 (L_infty => genus-zero IBL_infty repackaging).

STATE AFTER SUB-TASK 7c: part A table added (class Doubled, part_a_table; record 026 Sec. 4).
FINDING 7c: the augmented relation (0.3) FAILS for all k, l >= 2 (R = M/2 != 0 on every
sector, both conventions) and HOLDS for min(k, l) = 1 in the tilde convention; see Sec. 4.5.
Run the table with --maxr 5 --sigs 2:2,1:3,3:1,1:4,2:3,3:2 (about 6 min).
STATE AFTER SUB-TASK 7d (2026-09-08): 81/81 PASS at the default invocation (73 inherited +
8 part-B checks B1a-g, B3: Koszul braces of an order-k operator on a commutative test
algebra, identities (5.4), (5.12), (5.13) of record 026 Sec. 5, break-on-purpose leg, and the
two-contraction term (5.17) on the generator vs the free theory).  NOT verified: the
operator form of p_hat on bare physical polynomials (record W11), Koszul signs of the braces
on odd inputs, the non-cyclicity obstruction (5.27)-(5.28) (hand computation).

STATE AFTER SUB-TASK B'a (2026-09-13): 92/92 PASS; new block part_b_parity_checks (P0-P5').
STATE AFTER SUB-TASK B'd (2026-09-14): 99/99 PASS; W5/W5' added (critic 026C's quantifier
counterexample D = theta d_theta on Lambda(theta); corrected criterion over A (x) Lambda(eta)).
What is machine-checked for Theorem B': the identity (B'.1) (W1, W1', W3), the free theory
(P4a-e), the counterexamples (P5, W2, W5), (5'.10) (W4).  The multilinear iff itself is proven
(record 026 Sec. 5'.3), not machine-checked.
STATE AFTER SUB-TASK 7a: 48/48 PASS (seed 20260908, toy (2,4,4,2), maxr 6); R16 legs also
PASS at --mult 3,5,5,3 --maxr 4.  Findings recorded in record 026 Working notes W3:
(i) the antibracket-derived products are ell'_n = W . Delta o V_{n+1} = Dt o V_{n+1} with the
graded-symmetric bivector Dt^{ab} = (-1)^{eps_a} Delta^{ab} and Q' = W Q, uniformly in n
(checks 3a-3e) -- this is R16's weight W; (ii) the (2,2,0) relation holds end to end on the
even sector for a genuine cyclic L_infty algebra (R16/Linfty legs); (iii) the odd-sector
inertness of the mixed term is convention-dependent (6b' diagnostics).  What this file provides:

  1. A finite-dimensional graded toy space with an odd non-degenerate pairing
     omega_1 (saturating at N_gh sum 5), Delta = omega_1^{-1}, and a cyclic,
     nilpotent, contractible Q -- the same construction as codes/verify-220-relation.py
     (derivation 010 / R16), with the ghost-number multiplicities parametrised.
  2. Graded-polynomial machinery: graded-symmetric tensors <-> polynomials in
     Grassmann-graded coordinates psi^a (parity eps_a = N_gh(e_a) mod 2, so that the
     superfield Psi = psi^a e_a is even); product = Koszul-signed shuffle
     symmetrisation; BV antibracket (F,G) = (-1)^{eps_a} d_a F Delta^{ab} d_b G
     (left derivatives, record 026 eq. (1.5)).
  3. THE GENERATOR (choice documented in record 026 Sec. 1.5, inherited by 7b-7d):
     canonical-transformation twist of the free action,
         S = exp(ad_G) S_0,   S_0 = (1/2) omega_1(Psi, Q Psi),   ad_G = (G, .),
     with G = G_3 + G_4 a random ODD polynomial whose rank-r tensor saturates at
     ghost number 2r+1.  Since exp(ad_G) is an automorphism of the antibracket,
     (S,S) = 0 exactly; truncating S at rank 6 gives V_2..V_6, i.e. ell_1..ell_5,
     satisfying every L_infty relation through (5,1,0) exactly (the degree-N part of
     (S,S) only involves V_i, V_j with i+j = N+2 <= 8).
  4. The general raising map p_{k,l} = Delta^{(x)l} o V_{k+l}, record eq. (1.6),
     with the shifted-parity output symmetry (1.7) checked.
  5. Checks (named PASS/FAIL, seed printed, nonzero exit on failure):
     - generator non-hollow (all V_n and all relation terms O(1)),
     - L_infty relations (n,1,0), n = 1..5, via the rank-N parts of (S,S)
       (break-on-purpose leg: a random symmetric perturbation of V_4 must FAIL),
     - output symmetry (1.7) of p_{k,l} for several (k,l),
     - R16 reproduction: Lemma A, Lemma B1, the even-sector (2,2,0) assembly and the
       inertness of the coderivation term, on GENERIC (unconstrained) cyclic data as
       in 010, and additionally on the generator's L_infty data.

NOT verified here (7c/7b): the general (k,l,0) relations for k+l >= 5; the
mixed-configuration cancellation of record 026 eq. (0.5) beyond (2,2); any statement
about the odd input sector beyond the raw R1 dressing of eq. (1.8).  Nothing here is
an independent check of CFL Prop. 7.2 (the (0.1) <=> (0.3) dictionary).

Usage:  uv run python codes/verify-linfty-ibl-repackaging.py [--mult 2,4,4,2] [--seed N]
"""

from __future__ import annotations

import argparse
import sys
import math
from itertools import combinations, combinations_with_replacement, permutations, product
from math import factorial

import numpy as np

TOL = 1e-9
RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one named PASS/FAIL check (never raises; summary at the end)."""
    RESULTS.append((name, bool(ok)))
    line = f"[{'PASS' if ok else 'FAIL'}] {name}"
    if detail:
        line += f"  --  {detail}"
    print(line)


# ===========================================================================
# 1. Graded toy space: N_gh multiplicities (m1, m2, m3, m4) for N_gh = 1,2,3,4.
#    omega_1 pairs N_gh 1<->4 and 2<->3 (antisymmetric); Q: 1->2, 2->3 (partly), 3->4.
#    Construction copied from verify-220-relation.py (010), generalised in size.
# ===========================================================================
class Toy:
    def __init__(self, mult: tuple[int, int, int, int]) -> None:
        m1, m2, m3, m4 = mult
        if m1 != m4 or m2 != m3 or m2 < m1 + 2:
            raise ValueError("need m1 == m4, m2 == m3, m2 >= m1 + 2 (contractible Q)")
        self.NGH = np.array([1] * m1 + [2] * m2 + [3] * m3 + [4] * m4)
        self.PAR = self.NGH % 2
        self.N = len(self.NGH)
        N = self.N
        Gs = list(range(0, m1))
        Fs = list(range(m1, m1 + m2))
        As = list(range(m1 + m2, m1 + m2 + m3))
        Hs = list(range(m1 + m2 + m3, N))
        # omega_1: antisymmetric, saturating at N_gh sum 5
        W = np.zeros((N, N))
        for x, y in list(zip(Gs, Hs)) + list(zip(Fs, As)):
            W[x, y] = 1.0
            W[y, x] = -1.0
        self.W = W
        self.Delta = np.linalg.inv(W)
        # Q: g_i -> f_i, a_i -> h_i (i < m1); the remaining f's pair up f_j -> a_{j'}
        # so that Q is cyclic (V2 = W Q graded symmetric), Q^2 = 0, contractible.
        Q = np.zeros((N, N))
        for i in range(m1):
            Q[Fs[i], Gs[i]] = 1.0
            Q[Hs[i], As[i]] = 1.0
        rest = list(range(m1, m2))  # indices into Fs/As not used above
        # pair them up: f_{rest[2j]} -> a_{rest[2j+1]}, f_{rest[2j+1]} -> a_{rest[2j]}
        for j in range(0, len(rest) - 1, 2):
            Q[As[rest[j + 1]], Fs[rest[j]]] = 1.0
            Q[As[rest[j]], Fs[rest[j + 1]]] = 1.0
        self.Q = Q
        self.sgn = (-1.0) ** self.PAR

    # ---- Koszul machinery on graded-symmetric tensors --------------------------
    def koszul_perm(self, idx: tuple[int, ...], perm: tuple[int, ...]) -> float:
        sign = 1.0
        m = len(perm)
        for i in range(m):
            for j in range(i + 1, m):
                if perm[i] > perm[j] and self.PAR[idx[perm[i]]] and self.PAR[idx[perm[j]]]:
                    sign = -sign
        return sign

    def sym_unit(self, idx: tuple[int, ...]) -> np.ndarray | None:
        r = len(idx)
        T = np.zeros((self.N,) * r)
        for perm in permutations(range(r)):
            pidx = tuple(idx[perm[t]] for t in range(r))
            T[pidx] += self.koszul_perm(idx, perm)
        if np.abs(T).max() < 1e-12:
            return None
        return T / np.abs(T).max()

    def vertex_basis(self, rank: int, target: int) -> list[np.ndarray]:
        """Basis of graded-symmetric rank-`rank` tensors saturating at N_gh `target`."""
        out = []
        for idx in combinations_with_replacement(range(self.N), rank):
            if sum(self.NGH[list(idx)]) != target:
                continue
            T = self.sym_unit(idx)
            if T is not None:
                out.append(T)
        return out

    def random_sym(self, rank: int, target: int, rng: np.random.Generator) -> np.ndarray:
        basis = self.vertex_basis(rank, target)
        if not basis:
            raise ValueError(f"empty basis for rank {rank}, N_gh {target}")
        return sum(c * B for c, B in zip(rng.standard_normal(len(basis)), basis))

    def is_graded_symmetric(self, T: np.ndarray) -> float:
        """Max defect of graded symmetry under adjacent transpositions."""
        r = T.ndim
        d = 0.0
        for i in range(r - 1):
            axes = list(range(r))
            axes[i], axes[i + 1] = axes[i + 1], axes[i]
            Ts = np.transpose(T, axes)
            # Koszul sign for swapping slots i, i+1: (-1)^{eps_a eps_b}
            shape = [1] * r
            shape[i] = self.N
            pa = self.PAR.reshape(shape)
            shape = [1] * r
            shape[i + 1] = self.N
            pb = self.PAR.reshape(shape)
            s = (-1.0) ** (pa * pb)
            d = max(d, np.abs(T - s * Ts).max())
        return d

    # ---- graded polynomials: product and antibracket ---------------------------
    def shuffle_sign(self, rank: int, fpos: tuple[int, ...]) -> np.ndarray:
        """Koszul sign tensor for placing F's indices at positions fpos (sorted) and
        G's at the rest, starting from the order (F indices, then G indices).
        sign = prod over pairs (G-index at q) < (F-index at p), q < p, of (-1)^{eps_q eps_p}."""
        gpos = [q for q in range(rank) if q not in fpos]
        expo = np.zeros((self.N,) * rank)
        for p in fpos:
            for q in gpos:
                if q < p:
                    sp = [1] * rank
                    sp[p] = self.N
                    sq = [1] * rank
                    sq[q] = self.N
                    expo = expo + self.PAR.reshape(sp) * self.PAR.reshape(sq)
        return (-1.0) ** expo

    def poly_product(self, F: np.ndarray, G: np.ndarray) -> np.ndarray:
        """Coefficient tensor of the polynomial F(psi) G(psi), convention
        F(psi) = (1/r!) F_{b1..br} psi^{b1}...psi^{br}: H = sum_shuffles Koszul (F (x) G)."""
        r, s = F.ndim, G.ndim
        n = r + s
        FG = np.multiply.outer(F, G) if r and s else (F * G)
        H = np.zeros((self.N,) * n)
        for fpos in combinations(range(n), r):
            gpos = [q for q in range(n) if q not in fpos]
            axes = [0] * n
            for t, p in enumerate(fpos):
                axes[p] = t
            for t, q in enumerate(gpos):
                axes[q] = r + t
            # np.transpose(FG, axes)[i_0..i_{n-1}] = FG[j] with j[axes[t]] = i_t,
            # i.e. F's t-th index is read at output position fpos[t].
            H += self.shuffle_sign(n, fpos) * np.transpose(FG, axes)
        return H

    def left_deriv(self, F: np.ndarray) -> np.ndarray:
        """(d_a F)_{b2..br} = F_{a b2 .. br}: left derivative = contract first index
        (no sign for a graded-symmetric coefficient tensor; record 026 Sec. 1.5)."""
        return F

    def antibracket(self, F: np.ndarray, G: np.ndarray) -> np.ndarray:
        """(F,G) = (-1)^{eps_a} (d_a F) Delta^{ab} (d_b G) for EVEN F (eq. (1.5));
        for odd F the weight is (-1)^{eps_a (eps_F + 1)} = 1 (right-vs-left derivative)."""
        r, s = F.ndim, G.ndim
        parF = self.parity_of(F)
        w = self.sgn if parF == 0 else np.ones(self.N)
        # X_{c...} = sum_a w_a F_{a c...} Delta^{ab}  -> Y^{b}_{c...}; then contract with G_{b d...}
        Fw = np.einsum("a,a...->a...", w, F)
        X = np.tensordot(Fw, self.Delta, axes=([0], [0]))  # (c..., b)
        X = np.moveaxis(X, -1, 0)  # (b, c...)
        FG = np.tensordot(X, G, axes=([0], [0]))  # (c..., d...)
        # now symmetrise as the product of the two polynomials d_aF and d_bG
        return self.poly_product_from_split(FG, r - 1, s - 1)

    def poly_product_from_split(self, FG: np.ndarray, r: int, s: int) -> np.ndarray:
        """Shuffle-symmetrise a tensor whose first r indices are 'F-type' and last s 'G-type'."""
        n = r + s
        if n == 0:
            return FG
        H = np.zeros((self.N,) * n)
        for fpos in combinations(range(n), r):
            gpos = [q for q in range(n) if q not in fpos]
            axes = [0] * n
            for t, p in enumerate(fpos):
                axes[p] = t
            for t, q in enumerate(gpos):
                axes[q] = r + t
            H += self.shuffle_sign(n, fpos) * np.transpose(FG, axes)
        return H

    def parity_of(self, F: np.ndarray) -> int:
        """Parity of a homogeneous graded-symmetric tensor (sum of slot parities on support)."""
        r = F.ndim
        idx = np.argwhere(np.abs(F) > 1e-12)
        if len(idx) == 0:
            return 0
        p = int(self.PAR[idx[0]].sum() % 2)
        return p

    def saturation_of(self, F: np.ndarray) -> set[int]:
        idx = np.argwhere(np.abs(F) > 1e-12)
        return set(int(self.NGH[i].sum()) for i in idx)


# ===========================================================================
# 2. The generator: S = exp(ad_G) S_0 truncated at rank MAXR (record 026 Sec. 1.5)
# ===========================================================================
def build_generator(
    toy: Toy, rng: np.random.Generator, maxr: int = 6
) -> tuple[dict[int, np.ndarray], tuple[np.ndarray, np.ndarray]]:
    """Return {n: V_n} for n = 2..maxr with (S,S) = 0 exactly through rank maxr.

    S_0 = (1/2) V2_{ab} psi^a psi^b with V2 = omega_1 Q (graded symmetric by cyclicity);
    G = G_3 + G_4 random odd polynomials (rank r saturating at N_gh 2r+1);
    S = sum_m (1/m!) ad_G^m S_0, ad_G = (G, .); terms of rank > maxr dropped
    (they never feed back into lower ranks since ad_G raises the rank by >= 1).
    """
    V2 = toy.W @ toy.Q
    G3 = toy.random_sym(3, 7, rng)
    G4 = toy.random_sym(4, 9, rng)
    total: dict[int, np.ndarray] = {2: V2.copy()}
    current: dict[int, np.ndarray] = {2: V2}
    for m in range(1, maxr):
        new: dict[int, np.ndarray] = {}
        for r, T in current.items():
            for Gr in (G3, G4):
                rr = r + Gr.ndim - 2
                if rr > maxr:
                    continue
                B = toy.antibracket(Gr, T)
                new[rr] = new.get(rr, 0.0) + B
        if not new:
            break
        current = new
        for rr, T in new.items():
            total[rr] = total.get(rr, 0.0) + T / factorial(m)
    return total, (G3, G4)


def ss_rank(toy: Toy, V: dict[int, np.ndarray], n: int) -> np.ndarray:
    """Rank-n part of (S,S): sum over i+j = n+2 of (V_i, V_j) (polynomial convention)."""
    out = 0.0
    for i in V:
        j = n + 2 - i
        if j in V:
            out = out + toy.antibracket(V[i], V[j])
    return out


# ===========================================================================
# 3. ell_n from V_{n+1}; 010's independent commutator/Jacobiator formulas (physical
#    Koszul signs), used as a cross-check of the antibracket convention.
# ===========================================================================
def ell_from_V(toy: Toy, Vn1: np.ndarray) -> np.ndarray:
    """ell_n^b(A1..An) = Delta^{ba} V_{n+1}(e_a, A1..An), the PLAIN-Delta (Zwiebach)
    raising; record eq. (1.4) (post critic-026B) is the Dtilde-weighted version, see
    ell_from_V's use at 3c (plain Delta, negative control) vs the weighted L2p/L3p."""
    return np.tensordot(toy.Delta, Vn1, axes=([1], [0]))


def q_l2_commutator(toy: Toy, L2: np.ndarray) -> np.ndarray:
    Q, sgn = toy.Q, toy.sgn
    t1 = np.einsum("bc,cjk->bjk", Q, L2)
    t2 = np.einsum("bck,cj->bjk", L2, Q)
    t3 = np.einsum("bjc,j,ck->bjk", L2, sgn, Q)
    return t1 + t2 + t3


def q_l3_commutator(toy: Toy, L3: np.ndarray) -> np.ndarray:
    Q, sgn = toy.Q, toy.sgn
    t1 = np.einsum("bc,cxyz->bxyz", Q, L3)
    t2 = np.einsum("bcyz,cx->bxyz", L3, Q)
    t3 = np.einsum("bxcz,x,cy->bxyz", L3, sgn, Q)
    t4 = np.einsum("bxyc,x,y,cz->bxyz", L3, sgn, sgn, Q)
    return t1 + t2 + t3 + t4


def jac2(toy: Toy, L2: np.ndarray) -> np.ndarray:
    """Graded Jacobiator (ell_2 o_1 ell_2)(x,y,z), Koszul signs in PAR (010)."""
    N, PAR = toy.N, toy.PAR
    t1 = np.einsum("bcz,cxy->bxyz", L2, L2)
    t2 = np.zeros((N,) * 4)
    t3 = np.zeros((N,) * 4)
    for x in range(N):
        for y in range(N):
            for z in range(N):
                s2 = (-1.0) ** (PAR[y] * PAR[z])
                s3 = (-1.0) ** (PAR[x] * (PAR[y] + PAR[z]))
                t2[:, x, y, z] = s2 * np.einsum("bc,c->b", L2[:, :, y], L2[:, x, z])
                t3[:, x, y, z] = s3 * np.einsum("bc,c->b", L2[:, :, x], L2[:, y, z])
    return t1 + t2 + t3


# ===========================================================================
# 4. General raising map p_{k,l} (record eq. (1.6)) and output-symmetry test (1.7)
# ===========================================================================
def raise_map(toy: Toy, V: np.ndarray, ell: int, weighted: bool = False) -> np.ndarray:
    """P[a_1..a_l, A_1..A_k] = D^{a_1 b_1} ... D^{a_l b_l} V[b_1..b_l, A_1..A_k], with
    D = Delta (bare, weighted=False, the negative-control/Zwiebach-bracket case) or
    the graded-SYMMETRIC weighted bivector Dt^{ab} = (-1)^{eps_a} Delta^{ab}
    (weighted=True; record eq. (1.6) post critic-026B is this Dt case; the BV / DeWitt raising, see
    check 3 in main and record 026 Working notes: the antibracket products are
    ell'_n = W . Delta o V_{n+1} = Dt o V_{n+1})."""
    D = np.einsum("a,ab->ab", toy.sgn, toy.Delta) if weighted else toy.Delta
    P = V
    for i in range(ell):
        # contract leg b_{i+1} (currently at axis i, after i outputs were prepended);
        # tensordot prepends the new output, so the outputs come out in reverse order
        P = np.tensordot(D, P, axes=([1], [i]))
    k = V.ndim - ell
    perm = list(range(ell))[::-1] + list(range(ell, ell + k))
    return np.transpose(P, perm)


def swap_defect(toy: Toy, T: np.ndarray, i: int, j: int, rule: str) -> float:
    """Defect of graded symmetry of T under the swap of output axes i, j with Koszul
    rule 'std' ((-1)^{eps eps}) or 'shifted' ((-1)^{(eps+1)(eps+1)})."""
    r = T.ndim
    axes = list(range(r))
    axes[i], axes[j] = axes[j], axes[i]
    Ts = np.transpose(T, axes)
    si = [1] * r
    si[i] = toy.N
    sj = [1] * r
    sj[j] = toy.N
    pa = toy.PAR.reshape(si)
    pb = toy.PAR.reshape(sj)
    s = (-1.0) ** (pa * pb) if rule == "std" else (-1.0) ** ((pa + 1) * (pb + 1))
    return float(np.abs(T - s * Ts).max())


# ===========================================================================
# 5. R16 reproduction on the (2,2,0) sector (010's tensors, physical grading)
# ===========================================================================
def r16_checks(toy: Toy, L2: np.ndarray, L3: np.ndarray, tag: str, expect_assembly: bool) -> None:
    N, Delta, Q, sgn, PAR = toy.N, toy.Delta, toy.Q, toy.sgn, toy.PAR
    M2 = np.einsum("ai,bijk->abjk", Delta, L3)  # p_{2,2,0} (010 leg order)
    P = np.einsum("ai,bij->abj", Delta, L2)  # p_{1,2,0}
    QL3 = q_l3_commutator(toy, L3)
    JAC = jac2(toy, L2)
    MQ = np.einsum("ai,bijk->abjk", Delta, QL3)
    MJ = np.einsum("ai,bijk->abjk", Delta, JAC)
    Wt = lambda T: np.einsum("a,abjk->abjk", sgn, T)

    def qhat_out(T, sh):
        return np.einsum("ac,cbjk->abjk", Q, T) + ((-1.0) ** sh) * np.einsum(
            "a,bc,acjk->abjk", sgn, Q, T
        )

    def qhat_in(T, sh):
        return np.einsum("abck,cj->abjk", T, Q) + ((-1.0) ** sh) * np.einsum(
            "abjc,j,ck->abjk", T, sgn, Q
        )

    # Lemma A dressing search (010 check 5a)
    winA = []
    for sh1 in (0, 1):
        for sh2 in (0, 1):
            for s2 in (1, -1):
                for sA in (1, -1):
                    for w in (0, 1):
                        tgt = MQ if w == 0 else Wt(MQ)
                        R = qhat_out(M2, sh1) + s2 * qhat_in(M2, sh2) - sA * tgt
                        if np.abs(R).max() < TOL:
                            winA.append((sh1, sh2, s2, sA, w))
    check(f"R16/{tag} Lemma A: [Qhat, m2] = W.(Delta o [Q,ell_3]) with a unique dressing",
          len(winA) == 1, f"(sh1,sh2,s2,sA,w) = {winA}")
    if not winA:
        return
    sh1, sh2, s2, sA, w = winA[0]
    QM = qhat_out(M2, sh1) + s2 * qhat_in(M2, sh2)  # = Qhat m2 - m2 Qhat (010 signs)

    # Lemma B1 (010 check 6a): W.MJ = sY W.Y + sT3 T3
    T3 = np.einsum("abm,mjk->abjk", P, L2)
    Y1 = np.einsum("ai,bmk,mij->abjk", Delta, L2, L2)
    Y2 = np.einsum("ai,bmj,mik->abjk", Delta, L2, L2)
    for j in range(N):
        for kk in range(N):
            Y2[:, :, j, kk] *= (-1.0) ** (PAR[j] * PAR[kk])
    Y = Y1 + Y2
    winB = [(sY, sT) for sY in (1, -1) for sT in (1, -1)
            if np.abs(Wt(MJ) - sY * Wt(Y) - sT * T3).max() < TOL]
    check(f"R16/{tag} Lemma B1: W.(Delta o (ell_2 o_1 ell_2)) = sY W.Y + sT3 (p o ell_2), unique",
          len(winB) == 1, f"(sY, sT3) = {winB}")

    # E_2 output projector in the shifted parity; even-input mask
    Pout = np.zeros((N,) * 4)
    for a in range(N):
        for b in range(N):
            Pout[a, b, a, b] += 0.5
            Pout[a, b, b, a] += 0.5 * (-1.0) ** ((PAR[a] + 1) * (PAR[b] + 1))
    proj = lambda T: np.einsum("abcd,cdjk->abjk", Pout, T)
    EV = ((PAR[:, None] + PAR[None, :]) % 2 == 0).astype(float)
    even = lambda T: np.einsum("abjk,jk->abjk", T, EV)

    # 6b: inertness of the chain term W.Y on the even sector of E_2 (mixed configuration)
    raw, prj = np.abs(even(Wt(Y))).max(), np.abs(even(proj(Wt(Y)))).max()
    check(f"R16/{tag} 6b: mixed chain term W.Y is INERT on the even sector of E_2 (raw != 0)",
          raw > 1e-3 and prj < TOL, f"raw {raw:.2f} -> projected {prj:.1e}")
    # off the even sector it is NOT inert (the T1 residual, record Sec. 1.3)
    odd = lambda T: T - even(T)
    prj_odd = np.abs(odd(proj(Wt(Y)))).max()
    # 7a FINDING (diagnostic, always PASS; the number is the content): for ell_2 = Delta o V_3
    # (plain raising, 010's convention) W.Y is inert on the ODD input sector too, at both toy
    # sizes; for the BV-consistent products ell'_2 = Dt o V_3 (check 3) it is NOT.  The
    # odd-sector fate of the mixed term is convention-dependent -- record 026 Sec. 1.3, 7b.
    check(f"R16/{tag} 6b' (diagnostic) odd-sector projected norm of W.Y recorded",
          True, f"projected odd-sector norm {prj_odd:.1e} (raw odd-sector {np.abs(odd(Wt(Y))).max():.2f})")

    # even-sector (2,2,0) assembly: Qhat m2 - m2 Qhat - p o ell_2 = W.Delta o ([Q,l3] + l2 o l2)
    # assembly (010 eq. in Result): the three-term identity on the even sector
    assembly = even(proj(QM - T3))
    target = even(proj(Wt(MQ) + Wt(MJ)))
    d_id = np.abs(assembly - target).max()
    check(f"R16/{tag} (2,2,0) even-sector identity: Qhat m2 - m2 Qhat - p o ell_2 == W.Delta o ([Q,l3] + l2 o l2)",
          d_id < TOL, f"|difference| = {d_id:.1e} (both sides {np.abs(target).max():.2f})")
    if expect_assembly:
        # 7b (record 026 Sec. 3.3, check E6): on the L_infty data the three terms are each
        # bar-eps-ANTIsymmetric on the even sector, so this identity is 0 = 0 after projection;
        # the former non-hollowness guard used the UNprojected norm.  Kept as a diagnostic.
        check(f"R16/{tag} (2,2,0) even-sector assembly vanishes -- HOLLOW: each term projects to zero (026 Sec. 3.3, E6)",
              np.abs(assembly).max() < TOL,
              f"|assembly| = {np.abs(assembly).max():.1e}, projected |Qhat m2 - m2 Qhat| = {np.abs(even(proj(QM))).max():.1e}, "
              f"unprojected {np.abs(even(QM)).max():.2f}")
    else:
        check(f"R16/{tag} (2,2,0) assembly is NONZERO on generic (non-L_infty) data (non-hollow)",
              np.abs(assembly).max() > 1e-3, f"|assembly| = {np.abs(assembly).max():.2f}")


# ===========================================================================
# 7. Sub-task 7b: checks E1-E7 for record 026 Sec. 3 (proof of (0.5), the obstruction
#    M_{k,l} = -2 P_{k,l}, the dg-Lie criterion (3.18)-(3.19), the R16 adjudication (3.23)-(3.25)).
# ===========================================================================
def ce_example(f: np.ndarray, name: str) -> float:
    """Record 026 eq. (3.19): Chevalley-Eilenberg cyclic dg Lie algebra g_(1) (+) g*_(4).

    Built the BV way so that cyclicity holds by construction: basis c^a (ghost 1, odd) and
    c*_a (ghost 4, even), omega_1(c, c*) = <c*, c>, master action S = 1/2 <c*, [c, c]>,
    i.e. V_3[a*, b, c] = f_bc^a and its graded-symmetric reorderings (even-odd swaps: +).
    Products ell'_2 = Dt o V_3 (eq. (1.4) with the weighted bivector, W3.2), Q = 0.
    Checks: graded Jacobi for ell'_2 (Koszul signs as in 7a check 3b) and returns
    |Theta|, Theta[mu nu rho sigma] = omega_1(ell'_2(e_mu,e_nu), ell'_2(e_rho,e_sigma)),
    which by (3.18) vanishes iff ell_2 o_1 ell_2 = 0 (2-step nilpotent g).
    """
    n = f.shape[0]
    N = 2 * n
    par = np.array([1] * n + [0] * n)
    W = np.zeros((N, N))
    W[:n, n:] = np.eye(n)
    W[n:, :n] = -np.eye(n)
    V3 = np.zeros((N, N, N))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                V3[n + a, b, c] = V3[b, n + a, c] = V3[b, c, n + a] = f[b, c, a]
    # graded symmetry of V3 (all adjacent transpositions, Koszul signs in par)
    sym = 0.0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                sym = max(sym, abs(V3[i, j, k] - (-1.0) ** (par[i] * par[j]) * V3[j, i, k]),
                          abs(V3[i, j, k] - (-1.0) ** (par[j] * par[k]) * V3[i, k, j]))
    Delta = np.linalg.inv(W)  # omega_ab Delta^bc = delta_a^c  (Delta = W^{-1} as matrices)
    Dt = np.einsum("a,ab->ab", (-1.0) ** par, Delta)
    L2 = np.tensordot(Dt, V3, axes=([1], [0]))  # ell'_2^c(e_a, e_b) = Dt^{cd} V3[d, a, b]
    J = np.zeros((N,) * 4)
    for x in range(N):
        for y in range(N):
            for z in range(N):
                J[:, x, y, z] = (L2[:, :, z] @ L2[:, x, y]
                                 + (-1.0) ** (par[y] * par[z]) * (L2[:, :, y] @ L2[:, x, z])
                                 + (-1.0) ** (par[x] * (par[y] + par[z])) * (L2[:, :, x] @ L2[:, y, z]))
    theta = np.einsum("cd,cmn,drs->mnrs", W, L2, L2)
    check(f"E3/{name}: CE algebra g_(1)+g*_(4) from S = 1/2<c*,[c,c]>: V_3 graded symmetric, ell'_2 non-hollow, graded Jacobi",
          sym < TOL and np.abs(J).max() < TOL and np.abs(L2).max() > 0.5,
          f"sym defect {sym:.1e}, |Jac| = {np.abs(J).max():.1e}, |ell_2| = {np.abs(L2).max():.1f}")
    return float(np.abs(theta).max())


def part_b7_checks(toy: Toy, V: dict[int, np.ndarray], toyp: Toy, L2p: np.ndarray, L3p: np.ndarray) -> None:
    N, PAR, sgn, Delta = toy.N, toy.PAR, toy.sgn, toy.Delta
    Dt = np.einsum("a,ab->ab", sgn, Delta)
    # E1: W8 counting
    ok = True
    for k in range(1, 5):
        for ell in range(1, 5):
            tup = [(i, j, k - i, ell - j) for i in range(k + 1) for j in range(ell + 1)
                   if (i, j) != (0, 0) and (k - i, ell - j) != (0, 0)]
            nB, nR = len(tup), sum(1 for (i, j, m, n) in tup if j >= 1 and m >= 1)
            nM = sum(1 for (i, j, m, n) in tup if min(i, j, m, n) >= 1)
            ok &= nB == (k + 1) * (ell + 1) - 2 and nR == k * ell and nM == (k - 1) * (ell - 1)
            ok &= all((n >= 1 and i >= 1) or (j >= 1 and m >= 1) for (i, j, m, n) in tup)  # no class outside R
    check("E1 W8 counts: |B| = (k+1)(l+1)-2, |R| = kl, |M| = (k-1)(l-1), every class meets R (k,l <= 4)", ok)
    # E2/E4: mirror symmetry C(A|B) = C(B|A) from individually computed configurations, (3.6)
    for conv, want in (("tilde", 1.0), ("plain", -1.0)):
        d = Doubled(toy, conv)
        cf = d.configs(V, 2, 2)
        mirror = {(1, 1, 2, 2): (3, 1, 0, 2), (2, 2, 1, 1): (2, 0, 1, 3), (1, 2, 2, 1): (3, 0, 0, 3)}
        dm = max(np.abs(cf[a] - want * cf[b]).max() for a, b in mirror.items())
        dm_wrong = max(np.abs(cf[a] + want * cf[b]).max() for a, b in mirror.items())
        B = d.select(cf, "B", cf[(1, 1, 2, 2)].shape)
        P = d.select(cf, "P", B.shape)
        M = d.select(cf, "M", B.shape)
        d36 = np.abs(B - 2 * P - M).max()
        tag = "E2" if conv == "tilde" else "E4 (break-on-purpose, plain Delta)"
        check(f"{tag}: mirror configurations satisfy C(A|B) = {want:+.0f} C(B|A) at (2,2) (3.3), hence B = 2P + M (3.6)"
              + ("" if conv == "tilde" else " -- and (3.6) FAILS there"),
              dm < TOL and dm_wrong > 1e-3 and ((d36 < TOL) if conv == "tilde" else (d36 > 1e-3)),
              f"mirror defect {dm:.1e} (opposite sign {dm_wrong:.2f}), |B - 2P - M| = {d36:.1e}")
        if conv == "tilde":
            # E5: the pure sum on inputs at ghost (2,2) only (physical sector proper)
            NGHd = d.NGH
            mask = np.zeros(B.shape, dtype=bool)
            for idx in np.argwhere(np.abs(P) > 1e-12):
                psi = [q for q in idx if q < N]
                if len(psi) == 2 and all(NGHd[q] == 2 for q in psi):
                    mask[tuple(idx)] = True
            check("E5 pure sum P_{2,2} (= -M/2) is O(10) on inputs at N_gh = (2,2), while B_{2,2} = 0 there",
                  np.abs(P[mask]).max() > 1.0 and np.abs(B[mask]).max() < TOL,
                  f"|P| = {np.abs(P[mask]).max():.2f}, |B| = {np.abs(B[mask]).max():.1e}")
            A3 = cf[(1, 2, 2, 1)][:N, :N, N:, N:]
    # E3: dg Lie criterion (3.18)-(3.19)
    eps = np.zeros((3, 3, 3))
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1.0
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1.0
    heis = np.zeros((3, 3, 3))
    heis[0, 1, 2], heis[1, 0, 2] = 1.0, -1.0
    th_sl2 = ce_example(eps, "sl2")
    th_heis = ce_example(heis, "heisenberg")
    check("E3 (3.18)-(3.19): Theta = omega_1(l2(.,.), l2(.,.)) nonzero for sl2, zero for the Heisenberg algebra",
          th_sl2 > 0.5 and th_heis < TOL, f"|Theta| sl2 = {th_sl2:.2f}, Heisenberg = {th_heis:.1e}")
    # E6/E7: R16 hollowness (3.23)-(3.25) and the dictionary p o ell_2 <-> T(0,2|2,0)
    Q = toyp.Q
    M2 = np.einsum("ai,bijk->abjk", Delta, L3p)
    Pm = np.einsum("ai,bij->abj", Delta, L2p)
    qhat_out = lambda T, sh: np.einsum("ac,cbjk->abjk", Q, T) + ((-1.0) ** sh) * np.einsum("a,bc,acjk->abjk", sgn, Q, T)
    qhat_in = lambda T, sh: np.einsum("abck,cj->abjk", T, Q) + ((-1.0) ** sh) * np.einsum("abjc,j,ck->abjk", T, sgn, Q)
    QM = qhat_out(M2, 0) - qhat_in(M2, 0)
    T3 = np.einsum("abm,mjk->abjk", Pm, L2p)
    Y1 = np.einsum("ai,bmk,mij->abjk", Delta, L2p, L2p)
    Y2 = np.einsum("ai,bmj,mik->abjk", Delta, L2p, L2p)
    for j in range(N):
        for kk in range(N):
            Y2[:, :, j, kk] *= (-1.0) ** (PAR[j] * PAR[kk])
    WY = np.einsum("a,abjk->abjk", sgn, Y1 + Y2)
    Pout = np.zeros((N,) * 4)
    for a in range(N):
        for b in range(N):
            Pout[a, b, a, b] += 0.5
            Pout[a, b, b, a] += 0.5 * (-1.0) ** ((PAR[a] + 1) * (PAR[b] + 1))
    proj = lambda T: np.einsum("abcd,cdjk->abjk", Pout, T)
    EV = ((PAR[:, None] + PAR[None, :]) % 2 == 0).astype(float)
    even = lambda T: np.einsum("abjk,jk->abjk", T, EV)
    S = (-1.0) ** ((PAR[:, None] + 1) * (PAR[None, :] + 1))
    anti = lambda T: np.abs(T + np.einsum("abjk,ab->abjk", np.transpose(T, (1, 0, 2, 3)), S)).max()
    ok6 = all(np.abs(even(T)).max() > 1.0 and anti(even(T)) < TOL and np.abs(proj(even(T))).max() < TOL
              for T in (QM, T3, WY))
    check("E6 (3.23)-(3.24): 7a's R16 terms [Q,m2], p o l2, W.Y (mixed Delta x Dt raising) are bar-eps-ANTIsymmetric "
          "on the even sector and vanish after projection: the even-sector (2,2,0) identity of W3.3 is 0 = 0",
          ok6, "even raw norms " + ", ".join(f"{np.abs(even(T)).max():.1f}" for T in (QM, T3, WY))
          + "; projected " + ", ".join(f"{np.abs(proj(even(T))).max():.0e}" for T in (QM, T3, WY)))
    M2t = np.einsum("ai,bijk->abjk", Dt, L3p)
    Pt = np.einsum("ai,bij->abj", Dt, L2p)
    QMt = qhat_out(M2t, 1) - qhat_in(M2t, 1)
    T3t = np.einsum("abm,mjk->abjk", Pt, L2p)
    ok6b = all(anti(even(T)) > 1.0 and np.abs(proj(even(T))).max() > 1.0 for T in (QMt, T3t))
    check("E6' falsification: with UNIFORM Dt x Dt raising the same terms are bar-eps-symmetric and O(20) after projection",
          ok6b, f"projected even norms {np.abs(proj(even(QMt))).max():.1f}, {np.abs(proj(even(T3t))).max():.1f}")
    A3r = np.einsum("am,bn,jkmn->abjk", Dt, Dt, A3)
    # even input sector: the two forms agree elementwise; on the odd input sectors they differ
    # by the input-parity dressings of rule R1 (record Sec. 1.3, eq. (1.8)) -- reported, not tested.
    d7 = min(np.abs(even(T3t - s * A3r)).max() for s in (1.0, -1.0))
    d7_all = min(np.abs(T3t - s * A3r).max() for s in (1.0, -1.0))
    check("E7 (3.20)/(3.25): p~ o ell'_2 (map form) == +-Dt x Dt-raised T(0,2|2,0) (doubled form), elementwise on the even sector",
          d7 < TOL and np.abs(even(A3r)).max() > 1.0,
          f"|diff|_even = {d7:.1e} (norm {np.abs(even(A3r)).max():.1f}); all sectors |diff| = {d7_all:.1f} (R1 dressings on odd inputs)")


# ===========================================================================
# 6. Main
# ===========================================================================
# ===========================================================================
# 6. Sub-task 7c: the generating-function relation (0.3) on the doubled space
#    H_d = H (+) H (record 026 Sec. 4.1, eqs. (4.1)-(4.5)).
# ===========================================================================
class Doubled(Toy):
    """Polynomials in (Psi, chi) as graded-symmetric tensors on H (+) H.

    Indices 0..N-1 are Psi-slots, N..2N-1 chi-slots, parities (eps, eps) (both
    superfields even).  The bivector is the off-diagonal block Delta_d^{a, N+alpha}
    = Delta^{a alpha}, so that `antibracket(F, G)` = w_a d_{Psi^a}F Delta^{a alpha}
    d_{chi^alpha}G, eq. (4.2), with the weight w_a chosen by `conv`:
    'tilde' -> w_a = (-1)^{eps_a}  (BV-consistent, eq. (1.5));
    'plain' -> w_a = 1;
    'flip'  -> w_a = (-1)^{eps_a} * (-1 on N_gh in {2,3}): relative sign of the
               two pairing blocks flipped (falsification leg).
    """

    def __init__(self, toy: Toy, conv: str = "tilde") -> None:  # noqa: D107
        self.base = toy
        self.N0 = toy.N
        self.N = 2 * toy.N
        self.NGH = np.concatenate([toy.NGH, toy.NGH])
        self.PAR = self.NGH % 2
        D = np.zeros((self.N, self.N))
        D[: self.N0, self.N0 :] = toy.Delta
        self.Delta = D
        if conv == "tilde":
            w = (-1.0) ** self.PAR
        elif conv == "plain":
            w = np.ones(self.N)
        elif conv == "flip":
            w = (-1.0) ** self.PAR * np.where(np.isin(self.NGH, [2, 3]), -1.0, 1.0)
        else:
            raise ValueError(conv)
        self.sgn = w
        self.conv = conv
        self.is_psi = (np.arange(self.N) < self.N0).astype(int)
        self.is_odd_psi = self.is_psi * self.PAR

    def lift(self, V: np.ndarray) -> np.ndarray:
        """V_n on H -> tilde V_n on H_d: tilde V[I..] = V[I mod N ..]  (eq. 4.1)."""
        idx = np.arange(self.N) % self.N0
        return V[np.ix_(*([idx] * V.ndim))]

    def _count(self, vec: np.ndarray, rank: int) -> np.ndarray:
        c = np.zeros((self.N,) * rank, dtype=int)
        for ax in range(rank):
            sh = [1] * rank
            sh[ax] = self.N
            c = c + vec.reshape(sh)
        return c

    def bidegree(self, F: np.ndarray, k: int, ell: int) -> np.ndarray:
        """Piece of F with exactly k Psi-indices and ell chi-indices."""
        if F.ndim != k + ell:
            raise ValueError("rank mismatch")
        return F * (self._count(self.is_psi, F.ndim) == k)

    def sector_norms(self, R: np.ndarray, k: int) -> list[float]:
        """max|R| over components with m odd Psi-indices, m = 0..k (record Sec. 4.1)."""
        odd = self._count(self.is_odd_psi, R.ndim)
        return [float(np.abs(R * (odd == m)).max()) for m in range(k + 1)]

    def config(self, V: dict[int, np.ndarray], k1: int, l1: int, k2: int, l2: int) -> np.ndarray:
        """C_D(k1,l1 | k2,l2), eq. (4.3); zero if a vertex rank is < 2 or not generated."""
        n1, n2 = k1 + l1, k2 + l2
        if n1 < 2 or n2 < 2 or n1 not in V or n2 not in V:
            return None
        A = self.bidegree(self.lift(V[n1]), k1, l1)
        B = self.bidegree(self.lift(V[n2]), k2, l2)
        return self.antibracket(A, B)

    def configs(self, V: dict[int, np.ndarray], k: int, ell: int) -> dict[tuple, np.ndarray]:
        """All configurations C_D(k1,l1|k2,l2) at bidegree (k, ell) with k1 >= 1, l2 >= 1
        (each computed once), keyed by (k1, l1, k2, l2)."""
        out = {}
        for k1 in range(1, k + 2):
            k2 = k + 1 - k1
            for l2 in range(1, ell + 2):
                l1 = ell + 1 - l2
                C = self.config(V, k1, l1, k2, l2)
                if C is not None:
                    out[(k1, l1, k2, l2)] = C
        return out

    @staticmethod
    def select(cf: dict[tuple, np.ndarray], which: str, shape: tuple) -> np.ndarray:
        """Sum of configurations, eq. (4.4)-(4.5): which = 'R' (all k1,l1,k2,l2 >= 1),
        'B' (all with k1 >= 1, l2 >= 1), 'M' (mixed: k1 >= 2 and l2 >= 2 within R),
        'P' (R minus M)."""
        out = np.zeros(shape)
        for (k1, l1, k2, l2), C in cf.items():
            in_R = l1 >= 1 and k2 >= 1
            mixed = in_R and k1 >= 2 and l2 >= 2
            if which == "B" or (which == "R" and in_R) or (which == "M" and mixed) \
                    or (which == "P" and in_R and not mixed):
                out = out + C
        return out

    def config_sum(self, V: dict[int, np.ndarray], k: int, ell: int, which: str) -> np.ndarray:
        return self.select(self.configs(V, k, ell), which, (self.N,) * (k + ell))

    def genus1_term(self, V: dict[int, np.ndarray], n: int) -> np.ndarray:
        """H_1 piece from V_n: (1/2) tilde Delta^{ab} tilde V_n[a, b, ...] (BV self-contraction)."""
        Dt = np.einsum("a,ab->ab", self.base.sgn, self.base.Delta)
        T = np.tensordot(Dt, V[n], axes=([0, 1], [0, 1])) / 2.0
        return self.lift(T)


# ===========================================================================
# 8. Part B (record 026 Sec. 5, sub-task 7d): Koszul braces of an order-k operator
#    p_hat on a commutative test algebra (Lemma B1, eqs. (5.2)-(5.7), (5.12)-(5.13)),
#    and the two-contraction term (5.17) on the toy generator (Theorem B (iii)).
#    NOT checked here: the operator form of p_hat on bare physical polynomials (needs the
#    odd-hbar sign dressing of Sec. 1.3/4.6 (i)); the s = 1 relation in operator form.
# ===========================================================================
class EvenPoly:
    """Polynomials in NV commuting variables, truncated at total degree DMAX, stored as
    exponent arrays of shape (DMAX+1,)*NV.  Order-k operators p_hat f = (1/k!) sum_a
    P_a d^a f with symmetric P_a (a k-tuple), P_a a polynomial: this is eq. (5.1) in the
    commutative case (p(x^{b_1}..x^{b_k}) = P_{b_1..b_k})."""

    def __init__(self, nv: int, dmax: int) -> None:  # noqa: D107
        self.nv, self.dmax = nv, dmax
        self.shape = (dmax + 1,) * nv

    def zero(self) -> np.ndarray:
        return np.zeros(self.shape)

    def one(self) -> np.ndarray:
        f = self.zero()
        f[(0,) * self.nv] = 1.0
        return f

    def var(self, a: int) -> np.ndarray:
        f = self.zero()
        e = [0] * self.nv
        e[a] = 1
        f[tuple(e)] = 1.0
        return f

    def mul(self, f: np.ndarray, g: np.ndarray) -> np.ndarray:
        h = self.zero()
        for ef in zip(*np.nonzero(f)):
            for eg in zip(*np.nonzero(g)):
                e = tuple(i + j for i, j in zip(ef, eg))
                if sum(e) <= self.dmax:
                    h[e] += f[ef] * g[eg]
        return h

    def deriv(self, f: np.ndarray, a: int) -> np.ndarray:
        h = self.zero()
        for ef in zip(*np.nonzero(f)):
            if ef[a] > 0:
                e = list(ef)
                e[a] -= 1
                h[tuple(e)] += ef[a] * f[ef]
        return h

    def random(self, deg: int, rng: np.random.Generator) -> np.ndarray:
        f = self.zero()
        for e in product(range(deg + 1), repeat=self.nv):
            if sum(e) <= deg:
                f[e] = rng.normal()
        return f

    def power(self, f: np.ndarray, m: int) -> np.ndarray:
        out = self.one()
        for _ in range(m):
            out = self.mul(out, f)
        return out


class OrderKOp:
    """p_hat_{k,l}: f -> (1/k!) sum_{a_1..a_k} P_{a_1..a_k} d_{a_1}..d_{a_k} f with
    P symmetric in its k indices, each P_a a polynomial of degree l."""

    def __init__(self, alg: EvenPoly, k: int, ell: int, rng: np.random.Generator) -> None:  # noqa: D107
        self.alg, self.k, self.ell = alg, k, ell
        self.P: dict[tuple[int, ...], np.ndarray] = {}
        for a in combinations_with_replacement(range(alg.nv), k):
            self.P[a] = alg.random(ell, rng)

    def p(self, a: tuple[int, ...]) -> np.ndarray:
        return self.P[tuple(sorted(a))]

    def __call__(self, f: np.ndarray) -> np.ndarray:
        out = self.alg.zero()
        for a in product(range(self.alg.nv), repeat=self.k):
            g = f
            for ai in a:
                g = self.alg.deriv(g, ai)
            out += self.alg.mul(self.p(a), g)
        return out / math.factorial(self.k)


def brace(alg: EvenPoly, D, inputs: list[np.ndarray]) -> np.ndarray:
    """Koszul brace Phi^n_D(a_1..a_n), eq. (5.2), commutative case (all signs +)."""
    n = len(inputs)
    out = alg.zero()
    for r in range(n + 1):
        for I in combinations(range(n), r):
            aI = alg.one()
            for i in I:
                aI = alg.mul(aI, inputs[i])
            rest = alg.one()
            for i in range(n):
                if i not in I:
                    rest = alg.mul(rest, inputs[i])
            out += (-1.0) ** (n - r) * alg.mul(D(aI), rest)
    return out


def part_b_checks(toy: Toy, V: dict[int, np.ndarray], rng: np.random.Generator) -> None:
    """Record 026 Sec. 5: Lemma B1 (5.6)-(5.7), identities (5.12)-(5.13), term (5.17)."""
    print("--- part B (7d): braces of an order-k operator; two-contraction term ---")
    alg = EvenPoly(nv=3, dmax=7)
    xs = [alg.var(a) for a in range(alg.nv)]
    k, ell = 2, 2
    D = OrderKOp(alg, k, ell, rng)
    # B1a: order k  <=>  Phi^{k+1} = 0 on arbitrary (multi-string) inputs
    m1, m2, m3 = alg.mul(xs[0], xs[1]), xs[2], alg.mul(alg.mul(xs[0], xs[0]), xs[2])
    ok = nrm(brace(alg, D, [m1, m2, m3])) < 1e-12
    check("B1a (5.5): Phi^{k+1} of an order-k operator vanishes on multi-string inputs", ok)
    # B1b: single-string inputs: Phi^k(x^{b_1}..x^{b_k}) = p(b), Phi^{n<k} = 0, Phi^0 = D(1)
    ok = True
    for b in product(range(alg.nv), repeat=k):
        ok &= nrm(brace(alg, D, [xs[i] for i in b]) - D.p(b)) < 1e-12
    ok1 = all(nrm(brace(alg, D, [xs[b]])) < 1e-12 for b in range(alg.nv))
    ok0 = nrm(brace(alg, D, []) - D(alg.one())) < 1e-12 and nrm(D(alg.one())) < 1e-12
    check("B1b (5.7): Phi^k on single strings == p_{k,l}; Phi^{n<k} == 0 there; Phi^0 = D(1) = 0 for k >= 1",
          ok and ok1 and ok0)
    # B1c: multi-string inputs (5.6): Phi^2(x0 x1, x2) = sum over 2-subsets touching both inputs
    lhs = brace(alg, D, [m1, m2])
    rhs = alg.mul(D.p((0, 2)), xs[1]) + alg.mul(D.p((1, 2)), xs[0])
    check("B1c (5.6): Phi^2(x0 x1, x2) == p(x0,x2) x1 + p(x1,x2) x0 (one strand from each input)",
          nrm(lhs - rhs) < 1e-12, f"|Phi^2| = {nrm(lhs):.2f}")
    # B1d: identities (5.12)-(5.13) for a curved operator D' = D + (multiplication by c) + D1,
    #      i.e. D'(1) != 0, on the truncated exponential e^{t a} (orders t^0..t^3)
    c = alg.random(2, rng)
    D1 = OrderKOp(alg, 1, 2, rng)
    Dp = lambda f: D(f) + alg.mul(c, f) + D1(f)  # noqa: E731
    a = alg.random(1, rng)
    a[(0,) * alg.nv] = 0.0  # no constant term (keeps the degree filtration clean)
    T = 4
    # F_t = e^{-ta} D'(e^{ta}) as a polynomial in t (list of coefficients)
    def series_conj(op, upto: int) -> list[np.ndarray]:
        Dm = [op(alg.power(a, j)) / math.factorial(j) for j in range(upto + 1)]
        return [sum((-1.0) ** i / math.factorial(i) * alg.mul(alg.power(a, i), Dm[m - i])
                    for i in range(m + 1)) for m in range(upto + 1)]
    F = series_conj(Dp, T)
    # generating identity (5.4): t^m coefficient == Phi^m(a^m)/m!
    ok = all(nrm(F[m] - brace(alg, Dp, [a] * m) / math.factorial(m)) < 1e-10 for m in range(T + 1))
    check("B1d (5.4): e^{-ta} D'(e^{ta}) == sum_m t^m/m! Phi^m_{D'}(a^m) through t^4 (curved D')", ok)
    # (5.12): e^{-ta} D'(e^{ta} b) == sum_n t^n/n! [Phi^{n+1}(a^n, b) + Phi^n(a^n) b]
    b = alg.random(2, rng)
    Dmb = [Dp(alg.mul(alg.power(a, j), b)) / math.factorial(j) for j in range(T + 1)]
    L = [sum((-1.0) ** i / math.factorial(i) * alg.mul(alg.power(a, i), Dmb[m - i])
             for i in range(m + 1)) for m in range(T + 1)]
    R = [(brace(alg, Dp, [a] * n + [b]) + alg.mul(brace(alg, Dp, [a] * n), b)) / math.factorial(n)
         for n in range(T + 1)]
    check("B1e (5.12): e^{-ta} D'(e^{ta} b) == sum_n t^n/n! [Phi^{n+1}(a^n,b) + Phi^n(a^n) b] through t^4",
          all(nrm(L[n] - R[n]) < 1e-10 for n in range(T + 1)))
    # (5.13) first equality: e^{-ta} D'^2(e^{ta}) == sum_n t^n/n! Phi^{n+1}(a^n, F_t) + F_t^2
    # (commutative algebra: F^2 != 0, so the identity is tested WITH the F^2 term; the
    # graded case only adds F^2 = 0 for odd F)
    L2 = series_conj(lambda f: Dp(Dp(f)), T)
    R2 = []
    for m in range(T + 1):
        acc = alg.zero()
        for n in range(m + 1):
            acc += brace(alg, Dp, [a] * n + [F[m - n]]) / math.factorial(n)
        for i in range(m + 1):
            acc += alg.mul(F[i], F[m - i])
        R2.append(acc)
    check("B1f (5.13): e^{-ta} D'^2(e^{ta}) == sum_n t^n/n! Phi^{n+1}(a^n, F_t) + F_t^2 through t^4",
          all(nrm(L2[m] - R2[m]) < 1e-9 for m in range(T + 1)))
    # break-on-purpose: dropping the curvature term D'(1) a b from Phi^2 breaks (5.4) at t^2
    bad = brace(alg, Dp, [a, a]) - alg.mul(alg.mul(Dp(alg.one()), a), a)
    check("B1g break-on-purpose: Phi^2 without the D(1) a b term violates (5.4) at t^2",
          nrm(F[2] - bad / 2.0) > 1e-3, f"defect = {nrm(F[2] - bad / 2.0):.2f}")
    # B3: two-contraction term (5.17) at bidegree (1,1) from V_3 on the generator vs free theory
    Dt = np.einsum("a,ab->ab", toy.sgn, toy.Delta)  # tilde Delta
    V3 = V[3]
    A2 = 0.5 * np.einsum("abc,aA,bB,ABd->cd", V3, Dt, Dt, V3)
    V2 = toy.W @ toy.Q  # omega(., Q .) as a bilinear (graded symmetric on support)
    A2free = 0.5 * np.einsum("ab,aA,bB,AB->", V2, Dt, Dt, V2)
    check("B3 (5.17): two-contraction term A^(2) at (1,1) is O(1) on the generator (one-loop bubble), "
          "and the free-theory constant (1/2) V2 Dt Dt V2 vanishes",
          nrm(A2) > 1e-3 and abs(A2free) < 1e-9, f"|A2_(1,1)| = {nrm(A2):.2f}, A2_free = {A2free:.1e}")


class GPoly:
    """Graded-commutative polynomial algebra on nv variables of given parities (0/1),
    truncated at total degree dmax. Polynomials are dicts {exponent tuple: coefficient};
    odd variables have exponent <= 1. Used by part_b_parity_checks (record 026 Sec. 5')."""

    def __init__(self, par: list[int], dmax: int) -> None:  # noqa: D107
        self.par = [int(x) for x in par]
        self.nv, self.dmax = len(par), dmax

    def zero(self) -> dict:
        return {}

    def one(self) -> dict:
        return {(0,) * self.nv: 1.0}

    def var(self, a: int) -> dict:
        e = [0] * self.nv
        e[a] = 1
        return {tuple(e): 1.0}

    def scal(self, c: float, f: dict) -> dict:
        return {m: c * v for m, v in f.items()}

    def add(self, f: dict, g: dict, cg: float = 1.0) -> dict:
        out = dict(f)
        for m, v in g.items():
            out[m] = out.get(m, 0.0) + cg * v
        return {m: v for m, v in out.items() if abs(v) > 1e-15}

    def parity(self, m: tuple[int, ...]) -> int:
        return sum(e * p for e, p in zip(m, self.par)) % 2

    def is_homogeneous(self, f: dict, par: int) -> bool:
        return all(self.parity(m) == par for m in f)

    def _mono_mul(self, m1: tuple[int, ...], m2: tuple[int, ...]) -> tuple[tuple[int, ...] | None, float]:
        # Koszul sign: each odd variable of m2 jumps over the odd variables of m1 with larger index
        sign = 1.0
        for j in range(self.nv):
            if m2[j] and self.par[j]:
                if m1[j]:
                    return None, 0.0
                cnt = sum(m1[i] for i in range(j + 1, self.nv) if self.par[i])
                if cnt % 2:
                    sign = -sign
        m = tuple(x + y for x, y in zip(m1, m2))
        if sum(m) > self.dmax:
            return None, 0.0
        return m, sign

    def mul(self, f: dict, g: dict) -> dict:
        out: dict = {}
        for m1, v1 in f.items():
            for m2, v2 in g.items():
                m, sg = self._mono_mul(m1, m2)
                if m is not None:
                    out[m] = out.get(m, 0.0) + sg * v1 * v2
        return {m: v for m, v in out.items() if abs(v) > 1e-15}

    def deriv(self, f: dict, a: int) -> dict:
        """Left derivative d/dx_a (moves x_a to the front, then removes it)."""
        out: dict = {}
        for m, v in f.items():
            if m[a] == 0:
                continue
            sign = 1.0
            if self.par[a]:
                if sum(m[i] for i in range(a) if self.par[i]) % 2:
                    sign = -1.0
            e = list(m)
            e[a] -= 1
            out[tuple(e)] = out.get(tuple(e), 0.0) + sign * m[a] * v
        return {m: v for m, v in out.items() if abs(v) > 1e-15}

    def norm(self, f: dict) -> float:
        return math.sqrt(sum(v * v for v in f.values()))

    def power(self, f: dict, m: int) -> dict:
        out = self.one()
        for _ in range(m):
            out = self.mul(out, f)
        return out

    def random_hom(self, deg: int, par: int, rng: np.random.Generator, nvars: int | None = None) -> dict:
        """Random element of exact degree deg and parity par (no constant term unless deg = 0)."""
        nvars = self.nv if nvars is None else nvars
        out: dict = {}
        for e in product(range(deg + 1), repeat=nvars):
            if sum(e) != deg or any(e[i] > 1 and self.par[i] for i in range(nvars)):
                continue
            m = tuple(e) + (0,) * (self.nv - nvars)
            if self.parity(m) == par:
                out[m] = rng.normal()
        return out

    def derivation(self, Qmat: np.ndarray):
        """Odd/even derivation f -> sum_a (Q x_a) d^L_a f with (Q x_a) = sum_b Q[b,a] x_b."""
        images = [{tuple(1 if i == b else 0 for i in range(self.nv)): Qmat[b, a]
                   for b in range(self.nv) if abs(Qmat[b, a]) > 1e-15} for a in range(self.nv)]

        def op(f: dict) -> dict:
            out = self.zero()
            for a in range(self.nv):
                if images[a]:
                    out = self.add(out, self.mul(images[a], self.deriv(f, a)))
            return out
        return op


def gbrace(alg: GPoly, D, inputs: list[dict], pars: list[int], koszul: bool = True) -> dict:
    """Koszul brace Phi^n_D(a_1..a_n), eq. (5.2), with the Koszul sign eps(I) of moving a_I
    to the left of a_{I^c} (inputs homogeneous of parities pars). koszul=False drops eps(I)
    (parity-blind, the old `brace`): the break-on-purpose variant."""
    n = len(inputs)
    out = alg.zero()
    for r in range(n + 1):
        for I in combinations(range(n), r):
            sign = (-1.0) ** (n - r)
            if koszul:
                Ic = [j for j in range(n) if j not in I]
                sign *= (-1.0) ** sum(pars[i] * pars[j] for i in I for j in Ic if j < i)
            aI = alg.one()
            for i in I:
                aI = alg.mul(aI, inputs[i])
            rest = alg.one()
            for j in range(n):
                if j not in I:
                    rest = alg.mul(rest, inputs[j])
            out = alg.add(out, alg.mul(D(aI), rest), sign)
    return out


def part_b_parity_checks(toy: Toy, V: dict[int, np.ndarray], rng: np.random.Generator) -> None:
    """Record 026 Sec. 5' (B'a): (5'.2) sign of (1.4); ghost-number support of the raised
    tensors (R23); Theta = p_{0,2} dies in S_eps H and lives in S_epsbar H; the free-theory
    test (5'.3)-(5'.9) on S_epsbar H with odd inputs present; critic's counterexample."""
    print("--- part B' (B'a): parity table and free-theory falsifier ---")
    Dt = np.einsum("a,ab->ab", toy.sgn, toy.Delta)  # Dt^{ab} = (-1)^{eps_a} Delta^{ab}
    V2 = toy.W @ toy.Q
    # P1: omega_1(e_c, ell_n(...)) == -(-1)^{eps_c} V_{n+1}(e_c, ...) for ell_n = Dt o V_{n+1}
    ok = True
    for n, Vn1 in ((1, V2), (2, V[3]), (3, V[4])):
        ell = np.tensordot(Dt, Vn1, axes=([1], [0]))          # ell^b_{...} = Dt^{ba} V_{a...}
        lhs = np.tensordot(toy.W, ell, axes=([1], [0]))       # omega_{cb} ell^b
        rhs = -np.einsum("c,c...->c...", toy.sgn, Vn1)
        ok &= np.allclose(lhs, rhs) and np.abs(lhs).max() > 0.1
    check("P1 (5'.2): omega(e_c, Dt o V_{n+1}) == -(-1)^{eps_c} V_{n+1}(e_c,..) for n=1,2,3", ok)
    # P2: raised tensors p_{k,l} supported on sum_out n - sum_in n == 3l - 2k (R23, g=0)
    ok = True
    for k, ell in ((1, 1), (2, 1), (3, 1), (2, 2), (1, 2), (0, 2), (3, 0), (4, 0)):
        Vn = V2 if k + ell == 2 else V[k + ell]
        P = raise_map(toy, Vn, ell, weighted=True)
        sup = np.argwhere(np.abs(P) > 1e-12)
        if sup.size:
            ng = toy.NGH[sup[:, :ell]].sum(1) - toy.NGH[sup[:, ell:]].sum(1)
            ok &= bool(np.all(ng == 3 * ell - 2 * k))
        else:
            ok = False
    check("P2 (R23): every p_{k,l} in {(1,1),(2,1),(3,1),(2,2),(1,2),(0,2),(3,0),(4,0)} has N_gh = 3l-2k", ok)
    # --- free theory on a smaller toy (polynomial algebra) ---------------------------------
    st = Toy((1, 3, 3, 1))
    Dts = np.einsum("a,ab->ab", st.sgn, st.Delta)
    V2s = st.W @ st.Q
    Th = np.einsum("aA,bB,AB->ab", Dts, Dts, V2s)            # Theta^{ab} = Dt Dt V2, eq. (1.6)
    Qt = -np.einsum("ba,a->ba", st.Q, st.sgn)                # tilde Q = -(-1)^eps Q = Dt o V2
    check("P0 tilde Q == Dt o V2, odd, squares to zero",
          np.allclose(np.tensordot(Dts, V2s, axes=([1], [0])), Qt) and np.allclose(Qt @ Qt, 0))

    def theta_in(alg: GPoly) -> dict:
        out = alg.zero()
        for a in range(st.N):
            for b in range(st.N):
                if abs(Th[a, b]) > 1e-12:
                    out = alg.add(out, alg.mul(alg.var(a), alg.var(b)), 0.5 * Th[a, b])
        return out
    W_eps = GPoly(list(st.PAR), 8)
    W_bar = GPoly(list(1 - st.PAR), 8)
    th_eps, th_bar = theta_in(W_eps), theta_in(W_bar)
    check("P3 Theta = p_{0,2} projects to 0 in S_eps H and is a nonzero even element of S_epsbar H",
          W_eps.norm(th_eps) < 1e-12 and W_bar.norm(th_bar) > 0.5 and W_bar.is_homogeneous(th_bar, 0),
          f"|Theta|_eps = {W_eps.norm(th_eps):.1e}, |Theta|_epsbar = {W_bar.norm(th_bar):.2f}")
    alg, Th_p = W_bar, th_bar
    Qh = alg.derivation(Qt)
    D = lambda f: alg.add(Qh(f), alg.mul(Th_p, f))  # noqa: E731  D = Qhat + Theta.
    # P4a: Qhat Theta = 0 (the (0,2) relation), Qhat^2 = 0 on a random element
    f = alg.add(alg.random_hom(2, 0, rng), alg.random_hom(1, 1, rng))
    check("P4a (5'.4): Qhat(Theta) == 0 and Qhat^2 == 0", alg.norm(Qh(Th_p)) < 1e-12 and alg.norm(Qh(Qh(f))) < 1e-12)
    # P4b: D^2 f == 2 Theta Qhat f + Theta^2 f  != 0
    d2 = D(D(f))
    pred = alg.add(alg.scal(2.0, alg.mul(Th_p, Qh(f))), alg.mul(alg.mul(Th_p, Th_p), f))
    check("P4b (5'.3)-(5'.4): D^2 f == 2 Theta Qhat f + Theta^2 f, and D^2 != 0 (Theta^2 != 0)",
          alg.norm(alg.add(d2, pred, -1.0)) < 1e-10 and alg.norm(d2) > 1e-3
          and alg.norm(alg.mul(Th_p, Th_p)) > 1e-3, f"|D^2 f| = {alg.norm(d2):.2f}")
    # P4c: braces with odd inputs present: l0 = Theta, l1(a) = Qhat a, l2(a,b) = 0 for all parity mixes
    ae, ao = alg.random_hom(2, 0, rng), alg.random_hom(1, 1, rng)
    be, bo = alg.random_hom(1, 0, rng), alg.random_hom(2, 1, rng)
    ok = alg.norm(alg.add(gbrace(alg, D, [], []), Th_p, -1.0)) < 1e-12
    for a, pa in ((ae, 0), (ao, 1)):
        ok &= alg.norm(alg.add(gbrace(alg, D, [a], [pa]), Qh(a), -1.0)) < 1e-12
        for b, pb in ((be, 0), (bo, 1)):
            ok &= alg.norm(gbrace(alg, D, [a, b], [pa, pb])) < 1e-12
    # the parity-blind brace of the odd derivation does NOT vanish on two odd inputs
    bad = alg.norm(gbrace(alg, Qh, [ao, bo], [1, 1], koszul=False))
    check("P4c (5'.5): l0 = Theta, l1 = Qhat, l2 = 0 on even/odd inputs (Koszul braces); parity-blind l2(odd,odd) != 0",
          ok and bad > 1e-3, f"parity-blind |Phi^2_Q(odd,odd)| = {bad:.2f}")
    # P4d/e: F = e^{-a} D e^{a}, F^2, e^{-a} D^2 e^{a} for an even a (degree 2, no constant), via series
    a = ae
    def conj(op, upto: int = 3) -> dict:
        ea = alg.zero()
        for j in range(upto + 1):
            ea = alg.add(ea, alg.power(a, j), 1.0 / math.factorial(j))
        ema = alg.zero()
        for j in range(upto + 1):
            ema = alg.add(ema, alg.power(a, j), (-1.0) ** j / math.factorial(j))
        return alg.mul(ema, op(ea))
    def trunc(f: dict, deg: int) -> dict:
        return {m: v for m, v in f.items() if sum(m) <= deg}
    F = trunc(conj(D), 4)
    F_pred = alg.add(Qh(a), Th_p)
    F2 = trunc(alg.mul(F, F), 4)
    check("P4d (5'.7): F = Qhat a + Theta, F^2 = Theta^2 + 2 Theta Qhat a != 0",
          alg.norm(alg.add(F, F_pred, -1.0)) < 1e-10 and alg.norm(F2) > 1e-3
          and alg.norm(alg.add(F2, alg.add(alg.mul(Th_p, Th_p), alg.scal(2.0, alg.mul(Th_p, Qh(a)))), -1.0)) < 1e-10,
          f"|F^2| = {alg.norm(F2):.2f}")
    L = trunc(conj(lambda g: D(D(g))), 4)
    Linf = alg.zero()                      # sum_n 1/n! Phi^{n+1}(a^n, F): the curved L_infty relation
    for n in range(3):
        Linf = alg.add(Linf, gbrace(alg, D, [a] * n + [F], [0] * (n + 1)), 1.0 / math.factorial(n))
    Linf = trunc(Linf, 4)
    check("P4e (5'.8)-(5'.9): curved L_infty relations hold (residual 0), e^{-a} D^2 e^{a} == F^2 != 0, "
          "and the old (5.13) form e^{-a} D^2 e^{a} == residual FAILS",
          alg.norm(Linf) < 1e-10 and alg.norm(alg.add(L, F2, -1.0)) < 1e-10 and alg.norm(L) > 1e-3,
          f"|e^-a D^2 e^a| = {alg.norm(L):.2f}, |L_infty residual| = {alg.norm(Linf):.1e}")
    # P5: critic's counterexample, D = d_{theta1} d_{theta2} on two odd variables, a = t theta1 theta2
    t = 0.7
    for koszul, par in ((True, [1, 1]), (False, [0, 0])):
        g = GPoly(par, 6)
        Dc = lambda h: g.deriv(g.deriv(h, 1), 0)  # noqa: E731
        ac = g.scal(t, g.mul(g.var(0), g.var(1)))
        ea = g.zero(); ema = g.zero()
        for j in range(4):
            ea = g.add(ea, g.power(ac, j), 1.0 / math.factorial(j))
            ema = g.add(ema, g.power(ac, j), (-1.0) ** j / math.factorial(j))
        Fc = g.mul(ema, Dc(ea))
        Fc_crit = g.add({(0, 0): -t}, ac, t)                                  # -t + t a
        res = g.add(gbrace(g, Dc, [Fc], [0], koszul), gbrace(g, Dc, [ac, Fc], [0, 0], koszul))
        okc = (g.norm(g.add(Fc, Fc_crit, -1.0)) < 1e-12 and g.norm(g.add(res, g.mul(Fc, Fc))) < 1e-12
               and g.norm(g.mul(Fc, Fc)) > 1e-3 and g.norm(Dc(Dc(ea))) < 1e-12)
        if koszul:
            check("P5 critic's counterexample: D = d1 d2 even, D^2 = 0, F = -t + t a, F^2 != 0, L_infty residual == -F^2",
                  okc, f"|F^2| = {g.norm(g.mul(Fc, Fc)):.3f}")
        else:
            check("P5' break-on-purpose: the same leg with the parity dressing removed (theta even) FAILS", not okc)
    # ---- B'b: Lemma W (W.7) and Theorem B' (B'.1)-(B'.4), record 026 Sec. 5'.3 -----------------
    def make_op(g: GPoly, rng: np.random.Generator, maxord: int = 2, nterms: int = 4, cpar: int | None = None):
        """Random normal-ordered differential operator sum_I c_I(x) d^I of order <= maxord,
        coefficients of mixed (or fixed) parity and degree <= 2. Returns (op, terms)."""
        terms = []
        for _ in range(nterms):
            r = int(rng.integers(0, maxord + 1))
            I = tuple(int(i) for i in rng.integers(0, g.nv, size=r))
            if any(I.count(i) > 1 and g.par[i] for i in I):
                continue
            par = int(rng.integers(0, 2)) if cpar is None else cpar
            deg = int(rng.integers(0, 3))
            c = g.random_hom(deg, par, rng)
            if c:
                terms.append((c, I))

        def op(f: dict) -> dict:
            out = g.zero()
            for c, I in terms:
                h = f
                for i in reversed(I):
                    h = g.deriv(h, i)
                out = g.add(out, g.mul(c, h))
            return out
        return op, terms

    def exp_conj(g: GPoly, a: dict, op, upto: int = 4, deg: int = 4) -> dict:
        ea, ema = g.zero(), g.zero()
        for j in range(upto + 1):
            ea = g.add(ea, g.power(a, j), 1.0 / math.factorial(j))
            ema = g.add(ema, g.power(a, j), (-1.0) ** j / math.factorial(j))
        return {m: v for m, v in g.mul(ema, op(ea)).items() if sum(m) <= deg}

    def lemma_w_residual(g: GPoly, a: dict, D1, D2, koszul: bool = True, deg: int = 4) -> tuple[dict, dict]:
        """(lhs, rhs) of (W.7): e^{-a} D1 D2 e^a - F1 F2  vs  sum_n 1/n! Phi^{n+1}_{D1}(a^n, F2)."""
        F1, F2 = exp_conj(g, a, D1, deg=deg), exp_conj(g, a, D2, deg=deg)
        lhs = g.add(exp_conj(g, a, lambda f: D1(D2(f)), deg=deg), g.mul(F1, F2), -1.0)
        lhs = {m: v for m, v in lhs.items() if sum(m) <= deg}
        # F2 is inhomogeneous: split by parity so that the Koszul brace sign is defined per piece
        rhs = g.zero()
        for par in (0, 1):
            F2p = {m: v for m, v in F2.items() if g.parity(m) == par}
            if not F2p:
                continue
            for n in range(3):
                rhs = g.add(rhs, gbrace(g, D1, [a] * n + [F2p], [0] * n + [par], koszul), 1.0 / math.factorial(n))
        rhs = {m: v for m, v in rhs.items() if sum(m) <= deg}
        return lhs, rhs
    gw = GPoly([0, 0, 1, 1], 8)      # two even, two odd generators
    a_w = gw.random_hom(2, 0, rng)   # even, degree 2 (contains odd-odd and even-even monomials)
    ok_w, ok_break, nz = True, True, 0.0
    for trial in range(3):
        D1, _ = make_op(gw, rng)
        D2, _ = make_op(gw, rng)
        lhs, rhs = lemma_w_residual(gw, a_w, D1, D2)
        ok_w &= gw.norm(gw.add(lhs, rhs, -1.0)) < 1e-9
        nz = max(nz, gw.norm(lhs))
        # break-on-purpose: the product order F2 F1 instead of F1 F2 (differs by the Koszul sign of the odd parts)
        F1, F2 = exp_conj(gw, a_w, D1), exp_conj(gw, a_w, D2)
        lhs_b = gw.add(exp_conj(gw, a_w, lambda f: D1(D2(f))), gw.mul(F2, F1), -1.0)
        ok_break &= gw.norm(gw.add(lhs_b, rhs, -1.0)) < 1e-9
    check("W1 Lemma W (W.7) on random order<=2 operators of mixed parity, odd generators present, 3 trials", ok_w and nz > 1e-3,
          f"max |e^-a D1 D2 e^a - F1 F2| = {nz:.2f}")
    check("W1' break-on-purpose: (W.7) with the sign dressing of F1 F2 changed (order F2 F1) FAILS", not ok_break)
    # W2: D = p_{2,0} = (1/2) V2^{ab} d_a d_b on S_eps H (constant coefficients: symbol s>=1 part is empty)
    ge = GPoly(list(st.PAR), 8)
    def p20(f: dict) -> dict:
        out = ge.zero()
        for x in range(st.N):
            for y in range(st.N):
                if abs(V2s[x, y]) > 1e-12:
                    out = ge.add(out, ge.deriv(ge.deriv(f, y), x), 0.5 * V2s[x, y])
        return out
    a4 = ge.random_hom(4, 0, rng, nvars=st.N)
    l1l1 = p20(p20(a4))
    F20 = exp_conj(ge, a4, p20, deg=8)
    R20 = ge.add(exp_conj(ge, a4, lambda f: p20(p20(f)), deg=8), ge.mul(F20, F20), -1.0)
    check("W2 counterexample to WB1's symbol form: D = p_{2,0} (even, constant coefficients, (D*D)_{s>=1} = 0) "
          "has l1 l1 != 0 on quartic a, and L_infty residual R(a) != 0",
          ge.norm(l1l1) > 1e-3 and ge.norm(R20) > 1e-3 and ge.norm(p20(ge.one())) < 1e-12,
          f"|l1 l1 a| = {ge.norm(l1l1):.2f}, |R(a)| = {ge.norm(R20):.2f}")
    # W3: Theorem B' (B'.1): the L_infty residual sum_n 1/n! Phi^{n+1}_D(a^n, F) equals F_{D^2} - F_D^2
    # for a random inhomogeneous D (odd generators present); and it vanishes for the free theory D (P4e)
    ok3, nz3 = True, 0.0
    for trial in range(3):
        Dm, _ = make_op(gw, rng, nterms=5)
        lhs, rhs = lemma_w_residual(gw, a_w, Dm, Dm)
        ok3 &= gw.norm(gw.add(lhs, rhs, -1.0)) < 1e-9
        nz3 = max(nz3, gw.norm(lhs))
    check("W3 Theorem B' (B'.1): L_infty residual == F_{D^2} - F_D^2 for random inhomogeneous D, 3 trials (nonzero)",
          ok3 and nz3 > 1e-3, f"max |residual| = {nz3:.2f}")
    # W4 (B'c, record 026 Sec. 5'.4): critic's one-line test "HS (b) is not the brace structure of its own
    # differential": D = ell^(b)_1 = Q on E_1, -(1/12) m_2 on E_2, zero elsewhere (no Q-hat on Sigma, R11);
    # Phi^2_D(Psi,Psi) = -(1/12) m_2(Psi Psi) - 2 Psi Q Psi  !=  ell^(b)_2(Psi,Psi) = ell_2(Psi,Psi) + (1/6) m_2(Psi Psi).
    # Host S_eps H of the 12-strand toy (physical even Psi on N_gh = 2 strands): m_2(Psi Psi) projects to 0 there (P3),
    # so the mismatch seen is ell_2(Psi,Psi) in E_1 against -2 Psi Q Psi in E_2.
    gh = GPoly(list(toy.PAR), 4)
    M2 = raise_map(toy, V[4], 2, weighted=True)               # m_2^{o1 o2}_{a b}
    L2 = np.tensordot(Dt, V[3], axes=([1], [0]))              # ell_2^b_{a1 a2} = Dt o V_3
    Qhat = gh.derivation(toy.Q)
    phys = [i for i in range(toy.N) if toy.NGH[i] == 2]
    cP = rng.normal(size=toy.N) * np.isin(np.arange(toy.N), phys)
    Psi = gh.zero()
    for a in range(toy.N):
        if abs(cP[a]) > 1e-15:
            Psi = gh.add(Psi, gh.var(a), cP[a])

    def m2hat(f: dict) -> dict:                               # coderivation m_2 on the degree-2 part of f (even strands only used)
        out = gh.zero()
        for m, v in f.items():
            if sum(m) != 2:
                continue
            idx = [i for i in range(toy.N) for _ in range(m[i])]
            a, b = idx
            for o1 in range(toy.N):
                for o2 in range(toy.N):
                    if abs(M2[o1, o2, a, b]) > 1e-12:
                        out = gh.add(out, gh.mul(gh.var(o1), gh.var(o2)), v * M2[o1, o2, a, b])
        return out

    def ell2(f: dict, g: dict) -> dict:
        out = gh.zero()
        for m1, v1 in f.items():
            for m2, v2 in g.items():
                a, b = m1.index(1), m2.index(1)
                for o in range(toy.N):
                    if abs(L2[o, a, b]) > 1e-12:
                        out = gh.add(out, gh.var(o), v1 * v2 * L2[o, a, b])
        return out

    def D_hs(f: dict) -> dict:
        f1 = {m: v for m, v in f.items() if sum(m) == 1}
        return gh.add(Qhat(f1), m2hat(f), -1.0 / 12.0)

    phi2 = gbrace(gh, D_hs, [Psi, Psi], [0, 0])
    PP = gh.mul(Psi, Psi)
    expected = gh.add(gh.scal(-1.0 / 12.0, m2hat(PP)), gh.mul(Psi, Qhat(Psi)), -2.0)
    hs2 = gh.add(ell2(Psi, Psi), m2hat(PP), 1.0 / 6.0)
    dev = gh.norm(gh.add(phi2, expected, -1.0))
    gap = gh.norm(gh.add(phi2, hs2, -1.0))
    check("W4 (critic's test, 5'.4): Phi^2_{ell^(b)_1}(Psi,Psi) == -(1/12) m_2(Psi Psi) - 2 Psi Q Psi, and != ell^(b)_2(Psi,Psi)",
          dev < 1e-9 and gap > 1e-3 and gh.norm(phi2) > 1e-3,
          f"|Phi^2 - expected| = {dev:.1e}, |Phi^2 - ell^(b)_2| = {gap:.2f}, |m_2(Psi Psi)|_(S_eps) = {gh.norm(m2hat(PP)):.1e}")
    # W5 (B'd, critic 026C): the quantifier of Theorem B'.  A = Lambda(theta), D = theta d_theta (even, order 1,
    # a derivation: l_0 = 0, l_1 = D, l_{>=2} = 0).  Even a in A are constants, on which F_D = F_{D^2} = 0, so the
    # old criterion "F_{D^2}(a) = F_D(a)^2 for all even a in A" holds vacuously -- yet (l_1)^2 theta = D^2 theta =
    # theta != 0.  The corrected criterion quantifies over even a in A (x) Lambda(eta), eta an auxiliary odd
    # parameter: a = eta theta gives F_D(a) = a, F_{D^2}(a) = a, F_D(a)^2 = 0, residual a != 0, as it must.
    # Break-on-purpose W5': the same corrected leg for D' = d_theta (odd, D'^2 = 0, genuine L_infty braces):
    # the residual vanishes, so a test asserting a nonzero residual FAILS.
    g5 = GPoly([1, 1], 4)                               # generator 0 = theta (odd), generator 1 = eta (odd, auxiliary)
    th, eta = g5.var(0), g5.var(1)
    D5 = lambda f: g5.mul(th, g5.deriv(f, 0))            # theta d_theta (even)
    D5odd = lambda f: g5.deriv(f, 0)                     # d_theta (odd, squares to zero)
    a_const = g5.scal(0.7, g5.one())                     # the only even elements of A = Lambda(theta): constants
    old_res = g5.add(exp_conj(g5, a_const, lambda f: D5(D5(f))), g5.mul(exp_conj(g5, a_const, D5), exp_conj(g5, a_const, D5)), -1.0)
    l1l1_th = D5(D5(th))
    a_ext = g5.mul(eta, th)                              # even element of A (x) Lambda(eta)
    def crit_res(D) -> dict:
        FD = exp_conj(g5, a_ext, D)
        return g5.add(exp_conj(g5, a_ext, lambda f: D(D(f))), g5.mul(FD, FD), -1.0)
    new_res = crit_res(D5)
    check("W5 (critic 026C) quantifier of Theorem B': D = theta d_theta on Lambda(theta): old criterion (even a in A) holds "
          "vacuously while (l_1)^2 theta != 0; corrected criterion (even a in A (x) Lambda(eta)) fails as it must",
          g5.norm(old_res) < 1e-12 and g5.norm(l1l1_th) > 1e-3 and g5.norm(new_res) > 1e-3
          and g5.norm(g5.add(new_res, a_ext, -1.0)) < 1e-12,
          f"|old residual| = {g5.norm(old_res):.1e}, |l1 l1 theta| = {g5.norm(l1l1_th):.2f}, |R(eta theta)| = {g5.norm(new_res):.2f} (= |eta theta|)")
    check("W5' break-on-purpose: the corrected criterion for D' = d_theta (odd, D'^2 = 0) has zero residual, so "
          "asserting a nonzero residual FAILS", not (g5.norm(crit_res(D5odd)) > 1e-3))


def nrm(T: np.ndarray) -> float:
    return float(np.abs(T).max())


def part_a_table(toy: Toy, V: dict[int, np.ndarray], rng: np.random.Generator,
                 sigs: list[tuple[int, int]]) -> None:
    """Record 026 Sec. 4.2-4.3: the (k,l,0) relation (0.3) per signature, convention, sector."""
    print("--- part A table: signature | conv | sector norms of R | |M| | |P| ---")
    SS = {n: ss_rank(toy, V, n) for n in range(2, max(k + l for k, l in sigs) + 1)}
    for (k, ell) in sigs:
        n = k + ell
        if n not in V:
            print(f"  ({k},{ell}) skipped: V_{n} not generated (raise --maxr)")
            continue
        # perturbed data for leg (iii): perturb the highest vertex V_{k+l}
        Vp = dict(V)
        Vp[n] = V[n] + 0.3 * toy.random_sym(n, 2 * n, rng)
        SSp = ss_rank(toy, Vp, n)
        shape = (2 * toy.N,) * n
        for conv in ("tilde", "plain"):
            d = Doubled(toy, conv)
            cf = d.configs(V, k, ell)
            R, M, P, B = (d.select(cf, w, shape) for w in ("R", "M", "P", "B"))
            sec = d.sector_norms(R, k)
            secM = d.sector_norms(M, k)
            tag = f"({k},{ell}) {conv:5s}"
            print(f"  {tag}: |R| by sector m=0..{k}: {[f'{x:.1e}' for x in sec]};"
                  f" |M| by sector: {[f'{x:.1e}' for x in secM]}; |P| = {nrm(P):.1e}; |B| = {nrm(B):.1e}")
            cfg = [nrm(C) for (k1, l1, k2, l2), C in cf.items() if l1 >= 1 and k2 >= 1]
            check(f"7c-{k}{ell}-{conv} individual configurations O(1) (non-hollow)",
                  max(cfg) > 1e-2, f"max |C| = {max(cfg):.2f}")
            # Mixed configurations exist only for k, l >= 2 (they need k1 >= 2, l2 >= 2 with
            # k2, l1 >= 1).  For min(k, l) = 1 the relation reduces to B/2 and HOLDS on all
            # sectors in the tilde convention.  On the EVEN sector of a (k,1) relation the
            # contracted leg has a fixed ghost number (saturation), so the plain and tilde
            # weights, and the block flip, are global signs there: plain R_even = 0 and
            # R_flip = 0 at (k,1) are expected and carry no information (record Sec. 4.2).
            has_mixed = k >= 2 and ell >= 2
            if conv == "tilde" and not has_mixed:
                check(f"7c-{k}{ell}-{conv} relation (0.3) HOLDS on ALL sectors (no mixed configuration at min(k,l)=1)",
                      nrm(R) < TOL and nrm(M) == 0.0, f"|R| by sector = {[f'{x:.1e}' for x in sec]}")
            elif conv == "tilde":
                check(f"7c-{k}{ell}-{conv} FINDING: R != 0 on the even sector and R == M/2 (Statement A, form (0.3), FAILS)",
                      sec[0] > 1e-3 and nrm(R - M / 2) < TOL,
                      f"|R|_even = {sec[0]:.2f}, |M|_even = {secM[0]:.2f}, |R - M/2| = {nrm(R - M/2):.1e}")
            elif ell == 1:
                check(f"7c-{k}{ell}-{conv} plain bracket at (k,1): R_even = 0 (global sign there) but R != 0 on odd sectors",
                      nrm(M) < TOL and sec[0] < TOL and max(sec[1:]) > 1e-3,
                      f"|R| by sector = {[f'{x:.1e}' for x in sec]}")
            else:
                check(f"7c-{k}{ell}-{conv} FINDING: M == 0 identically but R = P != 0 on the even sector (fails)",
                      nrm(M) < TOL and sec[0] > 1e-3 and nrm(R - P) < TOL,
                      f"|M| = {nrm(M):.1e}, |R|_even = {sec[0]:.2f}")
            # D1 / D1': vertex-exchange (anti)symmetry configuration by configuration
            dmax = 0.0
            sgn_mirror = 1.0 if conv == "tilde" else -1.0
            for (k1, l1, k2, l2), C in cf.items():
                mirror = (k2 + 1, l2 - 1, k1 - 1, l1 + 1)  # free legs exchanged
                if mirror in cf:
                    dmax = max(dmax, nrm(C - sgn_mirror * cf[mirror]))
            check(f"7c-{k}{ell}-{conv} D1: C(A|B) == {'+' if conv == 'tilde' else '-'}C(B|A) for every configuration",
                  dmax < TOL, f"max defect = {dmax:.1e}")
            if conv == "tilde":
                check(f"7c-{k}{ell}-{conv} (0.5) R = B/2 + M/2 on L_infty data", nrm(R - B / 2 - M / 2) < TOL,
                      f"|R - B/2 - M/2| = {nrm(R - B/2 - M/2):.1e}")
                check(f"7c-{k}{ell}-{conv} polarised L_infty B(u,u) = 0 (doubled machinery)", nrm(B) < TOL,
                      f"|B| = {nrm(B):.1e}")
                # leg (ii): relative sign flip of the pairing blocks (all sectors)
                df = Doubled(toy, "flip")
                Rf = df.config_sum(V, k, ell, "R")
                # at (k,1) the even-sector value is 0 by saturation (global sign); the odd
                # sectors make the leg decisive there
                check(f"7c-{k}{ell}-{conv} sign-flip leg: R_flip != 0 (all sectors)"
                      + (" (decisive: R == 0)" if not has_mixed else " (weak: R != 0 already)"),
                      nrm(Rf) > 1e-3, f"|R_flip| = {nrm(Rf):.2f}, even sector {df.sector_norms(Rf, k)[0]:.2f}")
            # leg (iii): L_infty perturbed; prediction R_pert - R = (1/2) SS_pert|_(k,l)
            Rp = d.config_sum(Vp, k, ell, "R")
            ref = d.bidegree(d.lift(SSp), k, ell)
            diff = Rp - R
            ratio = nrm(diff - ref / 2)
            check(f"7c-{k}{ell}-{conv} L_infty-perturbed leg: residual nonzero", nrm(diff) > 1e-3,
                  f"|R_pert - R| = {nrm(diff):.2f}, |(S,S)_pert| = {nrm(ref):.2f}")
            if conv == "tilde":
                check(f"7c-{k}{ell}-{conv} proportionality R_pert - R = (1/2)(S,S)_pert|(k,l) elementwise",
                      ratio < TOL * max(1.0, nrm(ref)), f"|diff - ref/2| = {ratio:.1e}")
            else:
                check(f"7c-{k}{ell}-{conv} (diagnostic) plain bracket: R_pert - R is NOT (1/2)(S,S)_pert (B_plain == 0)",
                      True, f"|diff - ref/2| = {ratio:.2f}, |B_plain| = {nrm(B):.1e}")
            # leg (iv): genus-1 self-contraction term added to H_0 (tilde only; the plain
            # self-contraction of a graded-symmetric vertex vanishes identically)
            if conv == "tilde":
                H1 = {m: d.genus1_term(V, m + 2) for m in range(2, n + 1) if (m + 2) in V}
                Vg = dict(V)
                for m, T in H1.items():
                    Vg[m] = Vg[m] + T[np.ix_(*([np.arange(toy.N)] * m))]
                Rg = d.config_sum(Vg, k, ell, "R")
                check(f"7c-{k}{ell}-{conv} genus-1 self-contraction term breaks the genus-0 relation",
                      nrm(Rg - R) > 1e-3, f"|R(H0+H1) - R(H0)| = {nrm(Rg - R):.2f}")
        # D0: doubled machinery vs ss_rank on perturbed data (independent code path)
        d = Doubled(toy, "tilde")
        Bp = d.config_sum(Vp, k, ell, "B")
        check(f"7c-{k}{ell} D0: B(u,u)|(k,l) from doubled bracket == lifted ss_rank (perturbed data)",
              nrm(Bp - d.bidegree(d.lift(SSp), k, ell)) < TOL * max(1.0, nrm(Bp)),
              f"|B_pert| = {nrm(Bp):.2f}, diff = {nrm(Bp - d.bidegree(d.lift(SSp), k, ell)):.1e}")


def phat_op(alg: GPoly, P: np.ndarray, k: int, l: int, rule: str, eps: np.ndarray):
    """Extension (5'.11) of a raised tensor P[o_1..o_l, a_1..a_k] to a differential operator on alg:

        f -> 1/(k! l!) sum_{o,a} s_rule(a) P[o,a] chi_{o_1}..chi_{o_l} d_{a_k} ... d_{a_1} f

    (left derivatives, first input slot innermost, so on a monomial the tensor is evaluated on the
    variables in the order written = the coderivation (5.1)).  Rules (record 026 Sec. 5'.5):
      'a' naive, s = 1;
      'b' left decalage on inputs, s = (-1)^{sum_i (i-1) eps_{a_i}};
      'c' right decalage on inputs, s = (-1)^{sum_i (k-i) eps_{a_i} + k(k-1)/2};
    eps = physical parities of the strands (toy.PAR), independent of the host's variable parities.
    Derivatives are memoised over prefixes of the input tuple (cost sum_j N^j deriv calls per f)."""
    norm = factorial(k) * factorial(l)
    terms: list[tuple[dict, tuple[int, ...], float]] = []
    for idx in np.argwhere(np.abs(P) > 1e-12):
        o, a = tuple(int(x) for x in idx[:l]), tuple(int(x) for x in idx[l:])
        e = [int(eps[x]) for x in a]
        if rule == "a":
            sg = 1.0
        elif rule == "b":
            sg = (-1.0) ** sum(i * ei for i, ei in enumerate(e))
        elif rule == "c":
            sg = (-1.0) ** (sum((k - 1 - i) * ei for i, ei in enumerate(e)) + k * (k - 1) // 2)
        else:
            raise ValueError(rule)
        mono = alg.one()
        for x in o:
            mono = alg.mul(mono, alg.var(x))
        terms.append((mono, a, sg * float(P[tuple(idx)]) / norm))

    def op(f: dict) -> dict:
        memo: dict[tuple[int, ...], dict] = {(): f}

        def dv(a: tuple[int, ...]) -> dict:
            if a not in memo:
                g = dv(a[:-1])
                memo[a] = alg.deriv(g, a[-1]) if g else {}
            return memo[a]
        out = alg.zero()
        for mono, a, c in terms:
            g = dv(a)
            if g:
                out = alg.add(out, alg.mul(mono, g), c)
        return out
    return op


def part_b_decalage_checks(toy: Toy, V: dict[int, np.ndarray], rng: np.random.Generator) -> None:
    """Record 026 Sec. 5'.5 (WB2 (c)): which sign rule makes Q^, l2^, l3^ (Dt-raised family of the
    (S,S)=0 generator) satisfy the L_infty relations as graded commutators of differential operators,
    on host (i) S_eps H (GPoly(PAR)) and host (ii) S_epsbar H (GPoly(1-PAR)).  W6a: (5'.11) with rule
    'a' is the coderivation (5.1) on monomials.  W6: surviving rule.  W6': break-on-purpose (rejected
    rules, plain-Delta family).  W6'': host (ii) degeneracy (equal-parity input pairs killed)."""
    print("--- part B' (WB2 (c)): decalage signs of p^_{k,l} on GPoly ---")
    N, eps = toy.N, toy.PAR
    V2 = toy.W @ toy.Q
    fam = {1: raise_map(toy, V2, 1, weighted=True), 2: raise_map(toy, V[3], 1, weighted=True),
           3: raise_map(toy, V[4], 1, weighted=True)}
    fam_plain = {1: raise_map(toy, V2, 1), 2: raise_map(toy, V[3], 1), 3: raise_map(toy, V[4], 1)}
    hosts = {"i": GPoly(list(eps), 4), "ii": GPoly(list(1 - eps), 4)}
    phys = [i for i in range(N) if toy.NGH[i] == 2]

    def rand_elem(alg: GPoly, r: np.random.Generator) -> dict:
        f = alg.zero()
        for d in (1, 2, 3):
            for par in (0, 1):
                f = alg.add(f, alg.random_hom(d, par, r), r.normal())
        return f

    def psi_elem(alg: GPoly, r: np.random.Generator) -> dict:
        out = alg.zero()
        for a in phys:
            out = alg.add(out, alg.var(a), r.normal())
        return out

    # W6a: rule 'a' on host (i) reproduces the tensor on monomials (order written), incl. equal parities
    gi = hosts["i"]
    l2a = phat_op(gi, fam[2], 2, 1, "a", eps)
    l3a = phat_op(gi, fam[3], 3, 1, "a", eps)
    oka, tested = True, 0
    for a, b in [(1, 2), (2, 3), (0, 5), (7, 8), (3, 3)]:
        f = l2a(gi.mul(gi.var(a), gi.var(b)))
        vec = np.array([f.get(tuple(1 if i == o else 0 for i in range(N)), 0.0) for o in range(N)])
        oka &= np.allclose(vec, fam[2][:, a, b])
        tested += np.abs(fam[2][:, a, b]).max() > 1e-9
    f = l3a(gi.mul(gi.mul(gi.var(1), gi.var(4)), gi.var(9)))
    vec = np.array([f.get(tuple(1 if i == o else 0 for i in range(N)), 0.0) for o in range(N)])
    oka &= np.allclose(vec, fam[3][:, 1, 4, 9]) and np.abs(vec).max() > 1e-9
    check("W6a (5'.11) rule a on S_eps H is the coderivation (5.1): l2^(x_a x_b) == l2(e_a,e_b), l3^ likewise",
          oka and tested >= 3, f"{tested} nonzero l2 pairs tested")

    results: dict[tuple[str, str, str], dict[str, float]] = {}
    for hname, alg in hosts.items():
        hpar = np.array(alg.par)
        for famname, F in (("Dt", fam), ("plain", fam_plain)):
            for rule in ("a", "b", "c"):
                if famname == "plain" and (rule != "a" or hname != "i"):
                    continue
                ops = {k: phat_op(alg, F[k], k, 1, rule, eps) for k in (1, 2, 3)}
                # operator parities in the host: parity of chi_o + sum of parities of d_a, from any nonzero entry
                opar = {}
                for k in (1, 2, 3):
                    idx = np.argwhere(np.abs(F[k]) > 1e-12)[0]
                    opar[k] = int(sum(hpar[x] for x in idx) % 2)
                Q, L2, L3 = ops[1], ops[2], ops[3]
                mx = {"R2c": 0.0, "R3c": 0.0, "R2s": 0.0, "R3s": 0.0, "L2L2": 0.0, "L2f": 0.0, "L2PsiPsi": 0.0}
                for seed in range(3):
                    r = np.random.default_rng(int(rng.integers(1 << 30)) + seed)
                    f = rand_elem(alg, r)
                    QL2, L2Q = Q(L2(f)), L2(Q(f))
                    QL3, L3Q, L2L2 = Q(L3(f)), L3(Q(f)), L2(L2(f))
                    s12 = (-1.0) ** (opar[1] * opar[2])
                    s13 = (-1.0) ** (opar[1] * opar[3])
                    s22 = (-1.0) ** (opar[2] * opar[2])
                    R2c = alg.add(QL2, L2Q, -s12)
                    R3c = alg.add(alg.add(QL3, L3Q, -s13), L2L2, 0.5 * (1 - s22))
                    R2s = alg.add(QL2, L2Q, 1.0)
                    R3s = alg.add(alg.add(QL3, L3Q, 1.0), L2L2, 1.0)
                    Psi = psi_elem(alg, r)
                    for key, val in (("R2c", R2c), ("R3c", R3c), ("R2s", R2s), ("R3s", R3s), ("L2L2", L2L2),
                                     ("L2f", L2(f)), ("L2PsiPsi", L2(alg.mul(Psi, Psi)))):
                        mx[key] = max(mx[key], alg.norm(val))
                mx["par"] = f"Q{opar[1]}l2:{opar[2]}l3:{opar[3]}"
                results[(hname, famname, rule)] = mx
                print(f"    host {hname:2s} {famname:5s} rule {rule}: parities {mx['par']}  "
                      f"|[Q,l2]|={mx['R2c']:.1e} |[Q,l3]+1/2[l2,l2]|={mx['R3c']:.1e}  "
                      f"|Ql2+l2Q|={mx['R2s']:.1e} |Ql3+l3Q+l2l2|={mx['R3s']:.1e}  "
                      f"|l2l2 f|={mx['L2L2']:.2f} |l2 f|={mx['L2f']:.2f} |l2(PsiPsi)|={mx['L2PsiPsi']:.1e}")
    w = results[("i", "Dt", "a")]
    check("W6 surviving rule: host S_eps H, rule a (naive coderivation signs): [Q^,l2^] = 0 and "
          "[Q^,l3^] + 1/2 [l2^,l2^] = 0 as graded commutators (all odd), 3 seeds, degree <= 3, odd generators present",
          w["R2c"] < 1e-10 and w["R3c"] < 1e-10 and w["L2L2"] > 1e-3 and w["L2PsiPsi"] > 1e-3,
          f"|[Q,l2]| = {w['R2c']:.1e}, |[Q,l3]+1/2[l2,l2]| = {w['R3c']:.1e}, |l2l2 f| = {w['L2L2']:.2f} (non-vacuous)")
    rej = {key: results[key] for key in (("i", "Dt", "b"), ("i", "Dt", "c"), ("i", "plain", "a"))}
    check("W6' break-on-purpose: on S_eps H the decalage-dressed rules b, c and the plain-Delta family each give a "
          "nonzero commutator",
          all(max(v["R2c"], v["R3c"]) > 1e-3 for v in rej.values()),
          "; ".join(f"{k[2]}/{k[1]}: |[Q,l2]|={v['R2c']:.2f}, |R3|={v['R3c']:.2f}" for k, v in rej.items()))
    d2 = {rule: results[("ii", "Dt", rule)] for rule in ("a", "b", "c")}
    check("W6'' host S_epsbar H is degenerate for inputs: l2^(Psi Psi) = 0 for physical Psi under all three rules "
          "(equal-parity input pairs killed, Sec. 5'.5), while nonzero on S_eps H",
          all(v["L2PsiPsi"] < 1e-12 for v in d2.values()) and w["L2PsiPsi"] > 1e-3,
          "; ".join(f"rule {r}: |l2(PsiPsi)|={v['L2PsiPsi']:.1e}, |Ql2+l2Q|={v['R2s']:.2f}, |Ql3+l3Q+l2l2|={v['R3s']:.2f}"
                    for r, v in d2.items()))



def phat_terms(alg: GPoly, P: np.ndarray, k: int, l: int) -> list[tuple[dict, tuple[int, ...], float]]:
    """Term list (chi-monomial, input tuple, coefficient) of (5'.11)/(5'.12) with rule 'a' (no dressing):
    f -> 1/(k! l!) sum_{o,a} P[o,a] chi_{o_1}..chi_{o_l} d_{a_k}..d_{a_1} f.  Same construction as phat_op
    (rule 'a'); returned as data so that several components can share one derivative memo."""
    norm = factorial(k) * factorial(l)
    terms: list[tuple[dict, tuple[int, ...], float]] = []
    for idx in np.argwhere(np.abs(P) > 1e-12):
        o, a = tuple(int(x) for x in idx[:l]), tuple(int(x) for x in idx[l:])
        mono = alg.one()
        for x in o:
            mono = alg.mul(mono, alg.var(x))
        if mono:
            terms.append((mono, a, float(P[tuple(idx)]) / norm))
    return terms


def apply_terms(alg: GPoly, terms: list[tuple[dict, tuple[int, ...], float]], f: dict) -> dict:
    """Apply a term list (phat_terms) to f: terms are grouped by input tuple a into one chi-polynomial
    coefficient C_a = sum_o c P[o,a] chi_o; out = sum_a C_a . (d_{a_k}..d_{a_1} f), derivatives memoised
    over prefixes of a (only tuples whose derivative of f is nonzero cost a multiplication)."""
    memo: dict[tuple[int, ...], dict] = {(): f}

    def dv(a: tuple[int, ...]) -> dict:
        if a not in memo:
            g = dv(a[:-1])
            memo[a] = alg.deriv(g, a[-1]) if g else {}
        return memo[a]
    groups: dict[tuple[int, ...], dict] = {}
    for mono, a, c in terms:
        groups[a] = alg.add(groups.get(a, {}), mono, c)
    out: dict = {}
    for a, Ca in groups.items():
        g = dv(a)
        if g and Ca:
            prod = alg.mul(Ca, g)
            for m, v in prod.items():
                out[m] = out.get(m, 0.0) + v
    return {m: v for m, v in out.items() if abs(v) > 1e-15}


def part_b_multistring_checks(toy: Toy, V: dict[int, np.ndarray], rng: np.random.Generator) -> None:
    """Record 026 Sec. 5'.6 (WB2 (b)): first falsifier of "A' => curved L_infty to leading order in hbar on
    multi-string inputs", on host (i) S_eps H with the (5'.12) extension of all k+l <= 4 components of the
    Dt-raised family, weights hbar^{k-1} (CFL input count).  The hbar-order is tracked without a formal
    parameter: the Theorem B' residual R(a) = F_{D^2}(a) - F_D(a)^2 is computed pair by pair
    (D_{k1} D_{k2}, D_k := sum_l p^_{k,l}) and binned by k1 + k2 - 2; the brace arity n is tracked by an
    auxiliary even variable t (a -> t a, coefficient of t^n).  The hbar^{n-1} coefficient at arity n is
    C_n := sum_{k1+k2 = n+1} [t^n] R_{k1 k2}(t a).  Checks: W7a (new components on monomials; l >= 3 and
    equal-parity output pairs vanish on host (i), P3), W7c (Lemma W: [t^{k1+k2}] R = 0, the s_W = 0 part
    cancels), W7 (finding: C_n != 0, n = 1..3, on even a of strand degree 2 and 3 with odd
    strands, 3 seeds; the l = 1 sub-family gives 0 as control), W7' (break-on-purpose on the control: V_4
    perturbed), W7'' (finding: on a physical single string C_1(Psi) != 0 because the eps-projection does not
    commute with Q^ -- host (i) is inconsistent for l >= 2, so W7's nonzero says nothing about the full family).  The comparison with the s_W10 = 1 contraction alone is through A' (7c): A' makes
    that part vanish, so C_n is the s_W = 1, s_W10 = 0 remainder the open question of Sec. 5'.3 asks about."""
    import time as _time
    t0 = _time.time()
    print("--- part B' (WB2 (b)): multi-string leading order on host (i) ---")
    N, eps = toy.N, toy.PAR
    TV = N                      # index of the auxiliary even variable t
    alg = GPoly(list(eps) + [0], 24)
    NMAX = 3                    # brace arities tested: n = 1..NMAX (needs e^{ta} through a^NMAX)
    comps = [(1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (0, 4), (2, 0), (3, 0), (4, 0)]
    Vfam = dict(V)
    Vfam[2] = toy.W @ toy.Q

    def family(Vd: dict[int, np.ndarray]) -> dict[int, list]:
        """D_k term lists, k = 0..4, from the tensors Vd (outputs raised with Dt, inputs bare)."""
        fam: dict[int, list] = {k: [] for k in range(5)}
        for k, l in comps:
            P = raise_map(toy, Vd[k + l], l, weighted=True)
            fam[k] += phat_terms(alg, P, k, l)
        return fam

    def trunc_t(f: dict, nmax: int) -> dict:
        return {m: v for m, v in f.items() if m[TV] <= nmax}

    def coef_t(f: dict, n: int) -> dict:
        return {m[:TV] + (0,) + m[TV + 1:]: v for m, v in f.items() if m[TV] == n}

    def residual_bins(fam: dict[int, list], a: dict) -> dict[tuple[int, int, int], float]:
        """|[t^n] R_{k1 k2}(t a)| for all pairs and n = 0..NMAX (exact through t^NMAX)."""
        ta = alg.mul(alg.var(TV), a)
        ea, ema = alg.zero(), alg.zero()
        for j in range(NMAX + 1):
            ea = alg.add(ea, alg.power(ta, j), 1.0 / factorial(j))
            ema = alg.add(ema, alg.power(ta, j), (-1.0) ** j / factorial(j))
        Dea = {k: trunc_t(apply_terms(alg, fam[k], ea), NMAX) for k in fam}
        F = {k: trunc_t(alg.mul(ema, Dea[k]), NMAX) for k in fam}
        out: dict[tuple[int, int, int], float] = {}
        for k1 in fam:
            for k2 in fam:
                if k1 + k2 > NMAX + 1 or not fam[k1] or not fam[k2]:
                    continue
                DD = trunc_t(apply_terms(alg, fam[k1], Dea[k2]), NMAX)
                R = alg.add(trunc_t(alg.mul(ema, DD), NMAX), trunc_t(alg.mul(F[k1], F[k2]), NMAX), -1.0)
                for n in range(NMAX + 1):
                    out[(k1, k2, n)] = coef_t(R, n)
        return out

    def C_n(bins: dict, n: int) -> float:
        """|sum_{k1+k2=n+1} [t^n] R_{k1k2}|: the polynomials are summed first (Q^ l2^ and l2^ Q^ cancel only
        in the sum), then the norm is taken."""
        tot = alg.zero()
        for (k1, k2, m), f in bins.items():
            if m == n and k1 + k2 == n + 1:
                tot = alg.add(tot, f)
        return alg.norm(tot)

    fam = family(Vfam)
    print(f"    term counts per k: {{k: len(fam[k]) for k in fam}} = { {k: len(fam[k]) for k in fam} }")

    # --- W7a: new components on monomials (l = 2, l = 0), and the P3 projection of l >= 3 / equal parities
    ok7a, tested_opp, tested_eq = True, 0, 0
    for k, l in [(0, 2), (1, 2), (2, 2)]:
        P = raise_map(toy, Vfam[k + l], l, weighted=True)
        op = phat_op(alg, P, k, l, "a", eps)
        for idx in np.argwhere(np.abs(P) > 1e-9):
            o1, o2, a = int(idx[0]), int(idx[1]), tuple(int(x) for x in idx[2:])
            if o1 >= o2 or (tested_opp >= 4 and tested_eq >= 4):
                continue
            mono = alg.one()
            for x in a:
                mono = alg.mul(mono, alg.var(x))
            f = op(mono)
            target = tuple(1 if i in (o1, o2) else 0 for i in range(N + 1))
            c = f.get(target, 0.0)
            if eps[o1] != eps[o2]:
                ok7a &= abs(c - P[tuple(idx)]) < 1e-9
                tested_opp += 1
            else:
                ok7a &= abs(c) < 1e-12
                tested_eq += 1
    # l = 0: p^_{2,0}(chi_a chi_b) == V_2[a,b] (scalar), incl. an odd-odd pair
    P20 = Vfam[2]
    op20 = phat_op(alg, P20, 2, 0, "a", eps)
    n20 = 0
    for a in range(N):
        for b in range(a + 1, N):
            if abs(P20[a, b]) > 1e-9 and n20 < 6:
                f = op20(alg.mul(alg.var(a), alg.var(b)))
                ok7a &= abs(f.get((0,) * (N + 1), 0.0) - P20[a, b]) < 1e-9 and len(f) == 1
                n20 += 1
    # l >= 3 components vanish identically on host (i) (every output triple has an equal-parity pair)
    zero_l3 = all(not phat_terms(alg, raise_map(toy, Vfam[k + l], l, weighted=True), k, l) or
                  alg.norm(apply_terms(alg, phat_terms(alg, raise_map(toy, Vfam[k + l], l, weighted=True), k, l),
                                       alg.add(alg.one(), alg.var(0)))) < 1e-12
                  for k, l in [(0, 3), (1, 3), (0, 4)])
    check("W7a new components on host (i): p^_{k,2} on monomials == P[o1,o2,a] for opposite-parity output pairs, "
          "== 0 for equal-parity pairs (P3); p^_{2,0}(x_a x_b) == V_2[a,b]; p^_{0,3}, p^_{1,3}, p^_{0,4} vanish "
          "identically (every output triple has an equal-parity pair)",
          ok7a and tested_opp >= 3 and tested_eq >= 3 and n20 >= 3 and zero_l3,
          f"{tested_opp} opposite-parity, {tested_eq} equal-parity, {n20} scalar instances; l>=3 zero: {zero_l3}")

    # --- test elements: even, strand degree 2 and 3, odd strands present (first 4 strands: N_gh 1,1,2,2)
    NV = 4
    odd_in = [i for i in range(NV) if eps[i]]
    def test_elem(r: np.random.Generator) -> dict:
        a = alg.add(alg.random_hom(2, 0, r, nvars=NV), alg.random_hom(3, 0, r, nvars=NV))
        return a
    phys = [i for i in range(N) if toy.NGH[i] == 2]

    allbins: list[dict] = []
    for seed in range(3):
        r = np.random.default_rng(int(rng.integers(1 << 30)) + seed)
        a = test_elem(r)
        has_odd = any(m[i] for m in a for i in odd_in)
        bins = residual_bins(fam, a)
        allbins.append(bins)
        cn = [C_n(bins, n) for n in range(1, NMAX + 1)]
        big = {key: alg.norm(v) for key, v in bins.items() if alg.norm(v) > 1e-8}
        print(f"    seed {seed}: |a|={alg.norm(a):.2f} odd strands {has_odd}; C_n (n=1,2,3) = "
              f"{[f'{x:.2e}' for x in cn]}; nonzero bins (k1,k2,n): "
              f"{ {k: f'{v:.2e}' for k, v in big.items()} }")
    lemW = max(alg.norm(v) for bins in allbins for (k1, k2, n), v in bins.items() if n == k1 + k2)
    check("W7c Lemma W on the family: [t^{k1+k2}] R_{k1k2} = 0 for every pair (the s_W = 0 part F_1 F_2 cancels)",
          lemW < 1e-9, f"max = {lemW:.1e}")
    Cmax = {n: max(C_n(bins, n) for bins in allbins) for n in range(1, NMAX + 1)}
    # control: the l = 1 sub-family (Q^, l2^, l3^; verified closed, W6) must give C_n = 0 on the same elements
    def family_l1(Vd: dict[int, np.ndarray]) -> dict[int, list]:
        fam1: dict[int, list] = {k: [] for k in range(5)}
        for k in (1, 2, 3):
            fam1[k] = phat_terms(alg, raise_map(toy, Vd[k + 1], 1, weighted=True), k, 1)
        return fam1
    fam1 = family_l1(Vfam)
    r = np.random.default_rng(int(rng.integers(1 << 30)))
    a_ctrl = test_elem(r)
    bins1 = residual_bins(fam1, a_ctrl)
    c1 = [C_n(bins1, n) for n in range(1, NMAX + 1)]
    check("W7 FINDING: hbar^{n-1} coefficient C_n = sum_{k1+k2=n+1} [t^n] R_{k1k2}(ta) of the B' residual is NONZERO on "
          "host (i) for the projected k+l<=4 family at n = 1, 2, 3 (even a, strand degree 2-3, odd strands, 3 seeds), "
          "while the l = 1 sub-family Q^+hbar l2^+hbar^2 l3^ gives C_n = 0 on the same kind of element (control)",
          all(v > 1e-6 for v in Cmax.values()) and max(c1) < 1e-9,
          f"full: C_1 = {Cmax[1]:.2e}, C_2 = {Cmax[2]:.2e}, C_3 = {Cmax[3]:.2e}; l=1 control: {[f'{x:.1e}' for x in c1]}")
    # --- W7': break on purpose on the control: V_4 perturbed (L_infty relations fail) -> l=1 family C_n != 0
    Vbad = dict(Vfam)
    Vbad[4] = Vfam[4] + 0.1 * toy.random_sym(4, 8, rng)
    bins_bad = residual_bins(family_l1(Vbad), a_ctrl)
    cb = [C_n(bins_bad, n) for n in range(1, NMAX + 1)]
    check("W7' break-on-purpose (control): with V_4 perturbed the l = 1 sub-family has C_3 != 0 "
          "([Q,l3] + l2 l2 fails at t^3, hbar^2)", cb[2] > 1e-6 and max(cb[:2]) < 1e-9,
          f"C_n = {[f'{x:.2e}' for x in cb]}")
    # --- W7'': physical even Psi (single string): l >= 2 components vanish (P3) but C_1(Psi) != 0 --
    # the projection does not commute with Q^: p^_{1,2} Q^ Psi survives (outputs (3,4), opposite parity)
    # while Q^ p^_{1,2} Psi and m2^(Theta, Psi) are projected out.  Lemma B1 + A' give C_n(Psi) = 0 for the
    # unprojected family, so this nonzero is an artefact of host (i): the projected family is not a
    # consistent truncation and its residual carries no information about the full family.
    r = np.random.default_rng(int(rng.integers(1 << 30)))
    Psi = alg.zero()
    for i in phys:
        Psi = alg.add(Psi, alg.var(i), r.normal())
    PsiPsi = alg.mul(Psi, Psi)
    Qh = phat_op(alg, raise_map(toy, Vfam[2], 1, weighted=True), 1, 1, "a", eps)
    m2 = phat_op(alg, raise_map(toy, Vfam[4], 2, weighted=True), 2, 2, "a", eps)
    p12 = phat_op(alg, raise_map(toy, Vfam[3], 2, weighted=True), 1, 2, "a", eps)
    th = phat_op(alg, raise_map(toy, Vfam[2], 2, weighted=True), 0, 2, "a", eps)
    l2 = phat_op(alg, raise_map(toy, Vfam[3], 1, weighted=True), 2, 1, "a", eps)
    bins_psi = residual_bins(fam, Psi)
    cp = [C_n(bins_psi, n) for n in range(1, NMAX + 1)]
    bins_psi1 = residual_bins(fam1, Psi)
    cp1 = [C_n(bins_psi1, n) for n in range(1, NMAX + 1)]
    nQp, npQ = alg.norm(Qh(p12(Psi))), alg.norm(p12(Qh(Psi)))
    check("W7'' FINDING (host (i) is inconsistent, not merely lossy): physical single string Psi: m2^(Psi Psi) = "
          "p^_{1,2} Psi = Theta = 0 (P3), l2^(Psi Psi) != 0, l=1 family C_n(Psi) = 0, but full projected family "
          "C_1(Psi) != 0 with p^_{1,2} Q^ Psi != 0 and Q^ p^_{1,2} Psi = 0: the eps-projection does not commute with Q^",
          alg.norm(m2(PsiPsi)) < 1e-12 and alg.norm(p12(Psi)) < 1e-12 and alg.norm(th(alg.one())) < 1e-12
          and alg.norm(l2(PsiPsi)) > 1e-3 and max(cp1) < 1e-9 and cp[0] > 1e-6 and npQ > 1e-6 and nQp < 1e-12,
          f"|m2(PsiPsi)| = {alg.norm(m2(PsiPsi)):.1e}, |p12 Psi| = {alg.norm(p12(Psi)):.1e}, "
          f"|l2(PsiPsi)| = {alg.norm(l2(PsiPsi)):.2f}, C_n(Psi) full = {[f'{x:.1e}' for x in cp]}, "
          f"l=1 = {[f'{x:.1e}' for x in cp1]}, |p12 Q Psi| = {npQ:.2f}, |Q p12 Psi| = {nQp:.1e}")
    print(f"    (WB2 (b) block: {_time.time() - t0:.0f} s)")



def part_b_host3_checks(toy: Toy, V: dict[int, np.ndarray], rng: np.random.Generator) -> None:
    """Record 026 Sec. 5'.7 (WB2 (b2)): the multi-string leading-order test on host (iii), C[chi]_{eps-bar}
    (variables of parity 1 - eps_a, plus the auxiliary even t), with EVERY slot Dt-raised:
    p^_{k,l} from raise_map(V[k+l], k+l, weighted=True), first l raised slots read as outputs.
    Ordered legs, stop at the first failure: W8a constructor/parity (all p^_{k,l} even; monomial values;
    equal-parity output AND input pairs nonzero), W8b single-string control C_n(chi_c) = 0 at N_gh(c) = 3
    (Lemma B1 + A' on a faithful host), W8b' diagnosis of the control (the delta-contraction of two raised
    indices is Dt.Dt = 1, so the single contraction on this host is the BARE index sum V.V, not V Dt V),
    W8c convention check and W8 multi-string test only if W8b passes."""
    import time as _time
    t0 = _time.time()
    print("--- part B' (WB2 (b2)): host (iii), all slots raised ---")
    N, eps = toy.N, toy.PAR
    TV = N
    alg = GPoly([1 - int(e) for e in eps] + [0], 24)
    NMAX = 3
    comps = [(1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (0, 4), (2, 0), (3, 0), (4, 0)]
    Vfam = dict(V)
    Vfam[2] = toy.W @ toy.Q

    def family(Vd: dict[int, np.ndarray], keep=None) -> dict[int, list]:
        fam: dict[int, list] = {k: [] for k in range(5)}
        for k, l in comps:
            if keep is not None and (k, l) not in keep:
                continue
            P = raise_map(toy, Vd[k + l], k + l, weighted=True)
            fam[k] += phat_terms(alg, P, k, l)
        return fam

    def trunc_t(f: dict, nmax: int) -> dict:
        return {m: v for m, v in f.items() if m[TV] <= nmax}

    def coef_t(f: dict, n: int) -> dict:
        return {m[:TV] + (0,) + m[TV + 1:]: v for m, v in f.items() if m[TV] == n}

    def residual_bins(fam: dict[int, list], a: dict) -> dict:
        ta = alg.mul(alg.var(TV), a)
        ea, ema = alg.zero(), alg.zero()
        for j in range(NMAX + 1):
            ea = alg.add(ea, alg.power(ta, j), 1.0 / factorial(j))
            ema = alg.add(ema, alg.power(ta, j), (-1.0) ** j / factorial(j))
        Dea = {k: trunc_t(apply_terms(alg, fam[k], ea), NMAX) for k in fam}
        F = {k: trunc_t(alg.mul(ema, Dea[k]), NMAX) for k in fam}
        out: dict = {}
        for k1 in fam:
            for k2 in fam:
                if k1 + k2 > NMAX + 1 or not fam[k1] or not fam[k2]:
                    continue
                DD = trunc_t(apply_terms(alg, fam[k1], Dea[k2]), NMAX)
                R = alg.add(trunc_t(alg.mul(ema, DD), NMAX), trunc_t(alg.mul(F[k1], F[k2]), NMAX), -1.0)
                for n in range(NMAX + 1):
                    out[(k1, k2, n)] = coef_t(R, n)
        return out

    def C_n(bins: dict, n: int) -> float:
        tot = alg.zero()
        for (k1, k2, m), f in bins.items():
            if m == n and k1 + k2 == n + 1:
                tot = alg.add(tot, f)
        return alg.norm(tot)

    # --- W8a: parity of every term, monomial values, equal-parity pairs nonzero --------------------------
    ok_par, ok_mono, n_eq_out, n_eq_in, n_tested = True, True, 0, 0, 0
    for k, l in comps:
        P = raise_map(toy, Vfam[k + l], k + l, weighted=True)
        terms = phat_terms(alg, P, k, l)
        for mono, a, c in terms:
            # parity of the term chi_o1..chi_ol d_ak..d_a1 = parity(monomial) + sum of input-variable parities
            ok_par &= (sum(alg.par[x] for x in a) + (alg.parity(next(iter(mono))) if mono else 0)) % 2 == 0
        if l > 0:
            op = phat_op(alg, P, k, l, "a", eps)
            n_comp = 0
            for idx in np.argwhere(np.abs(P) > 1e-9):
                o, a = tuple(int(x) for x in idx[:l]), tuple(int(x) for x in idx[l:])
                if list(o) != sorted(o) or len(set(o)) < l or len(set(a)) < k:
                    continue
                if n_comp >= 8:
                    break
                n_comp += 1
                mono = alg.one()
                for x in a:
                    mono = alg.mul(mono, alg.var(x))
                f = op(mono)
                target = tuple(1 if i in o else 0 for i in range(N + 1))
                ok_mono &= abs(f.get(target, 0.0) - P[tuple(idx)]) < 1e-9
                n_tested += 1
                if l >= 2 and eps[o[0]] == eps[o[1]]:
                    n_eq_out += 1
                if k >= 2 and eps[a[0]] == eps[a[1]]:
                    n_eq_in += 1
    check("W8a host (iii) constructor: every p^_{k,l} (k+l<=4) is EVEN on C[chi]_{eps-bar}; on monomials the value "
          "is the fully raised tensor in the order written, incl. equal-parity output pairs and equal-parity "
          "input pairs (both nonzero here, unlike host (i))",
          ok_par and ok_mono and n_eq_out >= 3 and n_eq_in >= 3 and n_tested >= 20,
          f"parity ok {ok_par}, monomials ok {ok_mono}, {n_tested} instances ({n_eq_out} equal-parity output pairs, "
          f"{n_eq_in} equal-parity input pairs)")

    # --- W8b: single-string control, chi_c at N_gh(c) = 3 (image of physical Psi under Dt) -------------
    fam = family(Vfam)
    fam1 = family(Vfam, keep=[(1, 1), (2, 1), (3, 1)])
    strands3 = [i for i in range(N) if toy.NGH[i] == 3]
    cn_all, cn_l1, bins_last = [], [], None
    for seed in range(3):
        r = np.random.default_rng(int(rng.integers(1 << 30)) + seed)
        a = alg.zero()
        for i in strands3:
            a = alg.add(a, alg.var(i), r.normal())
        bins = residual_bins(fam, a)
        bins_last = bins
        cn_all.append([C_n(bins, n) for n in range(1, NMAX + 1)])
        cn_l1.append([C_n(residual_bins(fam1, a), n) for n in range(1, NMAX + 1)])
        big = {key: alg.norm(v) for key, v in bins.items() if alg.norm(v) > 1e-8}
        print(f"    seed {seed}: single string |a|={alg.norm(a):.2f}; C_n = {[f'{x:.2e}' for x in cn_all[-1]]}; "
              f"l=1 family: {[f'{x:.2e}' for x in cn_l1[-1]]}; nonzero bins: { {k: f'{v:.2e}' for k, v in big.items()} }")
    Cmax = [max(c[n] for c in cn_all) for n in range(NMAX)]
    w8b = max(Cmax) < 1e-9
    check("W8b FINDING (host (iii) is NOT faithful): the single-string control C_n(chi_c), n = 1,2,3, chi_c at "
          "N_gh = 3, is NONZERO on the all-slots-raised host, where Lemma B1 + A' require 0 on a faithful host; "
          "already the (1,0,0) bin Q^ Theta and the (1,1,1) bin Q^ Q^ chi_c are O(10^3) (diagnosis: W8b')",
          max(Cmax) > 1e-6 and alg.norm(bins_last[(1, 0, 0)]) > 1e-6 and alg.norm(bins_last[(1, 1, 1)]) > 1e-6,
          f"max C_n = {[f'{x:.2e}' for x in Cmax]}; l=1 sub-family max = "
          f"{[f'{max(c[n] for c in cn_l1):.2e}' for n in range(NMAX)]}; |Q^ Theta| = {alg.norm(bins_last[(1, 0, 0)]):.2e}")
    # --- W8b': diagnosis. Dt.Dt = 1, so the (1,1) bin at t^1 is Q^ Q^ chi_c with matrix Dt (V2 V2) Dt.
    Dt = np.einsum("a,ab->ab", toy.sgn, toy.Delta)
    DtDt = Dt @ Dt
    M = Dt @ Vfam[2] @ Dt          # matrix of Q^ on host (iii): Q^ chi_c = sum_o M[o, c] chi_o  (P[o,c])
    P11 = raise_map(toy, Vfam[2], 2, weighted=True)
    same = np.abs(P11 - M).max()
    M2 = M @ M
    bare = np.abs(Dt @ (Vfam[2] @ Vfam[2]) @ Dt - M2).max()
    # machine value of Q^ Q^ chi_c against M2 (independent path: differential operator vs matrix)
    Qh = phat_op(alg, P11, 1, 1, "a", eps)
    r = np.random.default_rng(int(rng.integers(1 << 30)))
    coef = r.normal(size=N)
    a = alg.zero()
    for i in strands3:
        a = alg.add(a, alg.var(i), coef[i])
    QQa = Qh(Qh(a))
    vec = np.zeros(N)
    for m, v in QQa.items():
        vec[[i for i in range(N) if m[i]][0]] = v
    pred = M2 @ np.array([coef[i] if i in strands3 else 0.0 for i in range(N)])
    check("W8b' diagnosis (convention, proven by hand): Dt.Dt = +1, so the delta-contraction of two raised indices "
          "is the BARE index sum: Q^ Q^ chi_c on host (iii) equals Dt (V2 V2) Dt chi_c != 0 (V2 V2 = W Q W Q != 0), "
          "not Dt (V2 Dt V2) Dt = 0 -- the single contraction on host (iii) is not A''s bracket",
          np.abs(DtDt - np.eye(N)).max() < 1e-12 and same < 1e-12 and bare < 1e-12
          and np.abs(vec - pred).max() < 1e-9 and np.abs(M2).max() > 0.5
          and np.abs(Dt @ Vfam[2] @ Dt @ Vfam[2] @ Dt).max() < 1e-12,
          f"|Dt Dt - 1| = {np.abs(DtDt - np.eye(N)).max():.1e}, |Q^Q^ chi - Dt V2 V2 Dt chi| = {np.abs(vec - pred).max():.1e}, "
          f"|V2 V2| = {np.abs(Vfam[2] @ Vfam[2]).max():.2f}, |V2 Dt V2| = {np.abs(Vfam[2] @ Dt @ Vfam[2]).max():.1e}")
    if not w8b:
        print("    W8b control fails on host (iii): legs W8c and W8 not run (brief: stop at the first failing leg).")
    else:
        print("    W8b control passed (unexpected, see W8b'): W8c / W8 not implemented in this run.")
    print(f"    (WB2 (b2) block: {_time.time() - t0:.0f} s)")


# ===========================================================================
# 7. Harold's convention (record 026 Sec. 8): sign dictionary and the map-form
#    (2,2) and (1,l) relations.  Checks H1-H3.
# ===========================================================================
def _par_tensor(toy: Toy, rank: int, ax: int) -> np.ndarray:
    """PAR broadcast along axis `ax` of a rank-`rank` tensor."""
    sh = [1] * rank
    sh[ax] = toy.N
    return toy.PAR.reshape(sh)


def h_config_tensor(toy: Toy, V: dict[int, np.ndarray], i: int, j: int, m: int, n: int) -> np.ndarray:
    """Coefficient tensor of the ordered configuration T(i,j|m,n) of record 026 (3.3),
    slots ordered (chi_1..chi_{j+n}, psi_1..psi_{i+m}).

    T(i,j|m,n) = 1/(i!j!m!n!) V(e_a, Psi^i, chi^j) Dt^{ab} V(e_b, Psi^m, chi^n),
    Dt^{ab} = (-1)^{eps_a} Delta^{ab}.  Built here directly from the vertices, with
    (a) the Koszul sign of the reordering (Psi^i chi^j Psi^m chi^n) -> (chi chi Psi Psi)
        of record 026 Sec. 8.3, and
    (b) the shuffle-symmetrisation of the two variable blocks (the polynomial-product
        convention of `poly_product`: F = (1/r!) F_{b..} psi^{b..}).
    No doubled-space code path is used.
    """
    Dt = np.einsum("a,ab->ab", toy.sgn, toy.Delta)
    V1, V2 = V[i + j + 1], V[m + n + 1]
    # contract the first slot of each vertex through Dt
    W1 = np.tensordot(Dt, V1, axes=([0], [0]))          # [b, psi^i, chi^j]
    R = np.tensordot(W1, V2, axes=([0], [0]))           # [psi^i, chi^j, psi^m, chi^n]
    rank = i + j + m + n
    # (a) Koszul sign of (x.., c.., y.., d..) -> (c.., d.., x.., y..)
    xs = list(range(0, i))
    cs = list(range(i, i + j))
    ys = list(range(i + j, i + j + m))
    ds = list(range(i + j + m, rank))
    expo = np.zeros((toy.N,) * rank)
    for a in xs:
        for b in cs + ds:
            expo = expo + _par_tensor(toy, rank, a) * _par_tensor(toy, rank, b)
    for a in ys:
        for b in ds:
            expo = expo + _par_tensor(toy, rank, a) * _par_tensor(toy, rank, b)
    R = (-1.0) ** expo * R
    # reorder slots to (chi-block, psi-block)
    R = np.transpose(R, cs + ds + xs + ys)
    # (b) shuffle-symmetrise each block; here each block has at most two slots
    nchi = j + n
    def shuffle_block(T, off, r, s):
        """Shuffle-symmetrise the block of r + s slots starting at `off` (first r of
        F-type, last s of G-type), with the Koszul signs of `Toy.shuffle_sign`."""
        if r == 0 or s == 0:
            return T
        b, rk = r + s, T.ndim
        out = np.zeros_like(T)
        for fpos in combinations(range(b), r):
            gpos = [q for q in range(b) if q not in fpos]
            axes = list(range(rk))
            for tt, pp in enumerate(fpos):
                axes[off + pp] = off + tt
            for tt, qq in enumerate(gpos):
                axes[off + qq] = off + r + tt
            expo = np.zeros((toy.N,) * rk)
            for pp in fpos:
                for qq in gpos:
                    if qq < pp:
                        expo = expo + (_par_tensor(toy, rk, off + pp)
                                       * _par_tensor(toy, rk, off + qq))
            out = out + (-1.0) ** expo * np.transpose(T, axes)
        return out
    R = shuffle_block(R, 0, j, n)
    R = shuffle_block(R, nchi, i, m)
    return R


def h_tuples(k: int, ell: int, kind: str) -> list[tuple[int, int, int, int]]:
    """Ordered tuples (i,j,m,n) of the sum B (non-augmented) or R (augmented), (3.4)."""
    out = []
    for i in range(k + 1):
        for j in range(ell + 1):
            m, n = k - i, ell - j
            if (i, j) == (0, 0) or (m, n) == (0, 0):
                continue
            if kind == "R" and not (j >= 1 and m >= 1):
                continue
            out.append((i, j, m, n))
    return out


def part_h_checks(toy: Toy, V: dict[int, np.ndarray]) -> None:
    """Record 026 Sec. 8: Harold's sign-free convention.

    H1 -- the dictionary (8.6)/(8.9)/(8.10) against the DEFINING pairing identities
          (8.2)/(8.3)-(8.4), at l = 1 and l = 2, elementwise, with break legs.
    H2 -- the non-augmented (2,2) relation in map form, (8.19)/(8.21): the seven
          configurations of the Sec. 8.3 table sum to zero, with break legs.
    H3 -- the (1,2) and (1,3) relations (8.24)/(8.25), augmented and non-augmented.
    """
    N, PAR, sgn, W, Delta = toy.N, toy.PAR, toy.sgn, toy.W, toy.Delta
    Dt = np.einsum("a,ab->ab", sgn, Delta)
    V3, V4 = V[3], V[4]

    # ---- H1a: one leg.  <e_c, l^H_n(A)> = V_{n+1}(e_c, A);  <e_c, l_n(A)> = -(-1)^{eps_c} V.
    for name, Vn1 in (("l^H_2 / l_2 (from V_3)", V3), ("l^H_3 / l_3 (from V_4)", V4)):
        LH = np.tensordot(Delta, Vn1, axes=([1], [0]))       # plain raising (8.5)
        LT = np.tensordot(Dt, Vn1, axes=([1], [0]))          # Dt raising (1.4)
        pairH = np.tensordot(W, LH, axes=([1], [0]))         # <e_c, l^H(A)> = omega_{cd} l^d
        pairT = np.tensordot(W, LT, axes=([1], [0]))
        d_free = np.abs(pairH - Vn1).max()
        d_sgn = np.abs(pairT + np.einsum("c,c...->c...", sgn, Vn1)).max()
        d_wrong = np.abs(pairT - Vn1).max()                   # break leg: sign-free for l_n
        check(f"H1a {name}: <e_c, l^H> = V (sign-free) and <e_c, l> = -(-1)^eps_c V  (8.2), (8.6)",
              d_free < TOL and d_sgn < TOL and d_wrong > 1e-3,
              f"|free| {d_free:.1e}, |signed| {d_sgn:.1e}, break leg {d_wrong:.2f}")

    # ---- H1b: two legs.  p_{2,2} from (1.6); p^H_{2,2} from the dictionary (8.10);
    #          test p^H against the DEFINING two-fold pairing (8.3)-(8.4).
    P22 = raise_map(toy, V4, 2, weighted=True)                # [c1, c2, a1, a2]
    e1 = PAR.reshape(N, 1, 1, 1)
    e2 = PAR.reshape(1, N, 1, 1)
    sig1 = (-1.0) ** (e1 + e2)                                # one -(-1)^eps per raised leg
    sig2 = (-1.0) ** (e1 * (e2 + 1))                          # interleaving sign of (8.4)
    PH22 = P22 / (sig1 * sig2)                                # (8.10) solved for p^H
    # rebuild V_4 from p^H through (8.3)-(8.4): V(e_b1,e_b2,B) = (-1)^{eps_c1 eps_b2} w w p^H
    kos = (-1.0) ** (PAR.reshape(N, 1, 1, 1) * PAR.reshape(1, N, 1, 1))   # (c1, b2)
    def rebuild(PH, koszul: bool) -> np.ndarray:
        X = np.einsum("cdij,ed->ceij", PH, W)
        if koszul:
            X = kos * X
        return np.einsum("fc,ceij->feij", W, X)
    d_ok = np.abs(rebuild(PH22, True) - V4).max()
    d_break = np.abs(rebuild(PH22, False) - V4).max()          # drop the interleaving sign
    d_break2 = np.abs(rebuild(P22, True) - V4).max()           # use the Dt-raised p instead
    check("H1b two legs: p^H_{2,2} of the dictionary (8.10) satisfies the defining pairing "
          "V_4(e_b1,e_b2,B) = <e_b1 (x) e_b2, p^H(B)>_2 with (8.4)",
          d_ok < TOL and d_break > 1e-3 and d_break2 > 1e-3,
          f"|resid| {d_ok:.1e}; break legs: no interleaving sign {d_break:.2f}, Dt-raised p {d_break2:.2f}")

    # ---- H1c: physical-sector reading (8.11)-(8.12)
    phys = (toy.NGH == 2)
    L2t = np.tensordot(Dt, V3, axes=([1], [0]))
    L2h = np.tensordot(Delta, V3, axes=([1], [0]))
    blk = np.ix_(np.arange(N), np.where(phys)[0], np.where(phys)[0])
    d1 = np.abs(L2t[blk] + L2h[blk]).max()                     # p_{k,1} = - l^H_k
    blk2 = np.ix_(np.arange(N), np.arange(N), np.where(phys)[0], np.where(phys)[0])
    d2 = np.abs(P22[blk2] - PH22[blk2]).max()                  # p_{k,2} = + p^H_{k,2}
    d2all = np.abs(P22 - PH22).max()
    check("H1c physical inputs (8.11)-(8.12): p_{k,1} = -l^H_k and p_{k,2} = +p^H_{k,2} "
          "on N_gh = 2 inputs (and the two differ off that block)",
          d1 < TOL and d2 < TOL and d2all > 1e-3 and np.abs(P22[blk2]).max() > 1e-3,
          f"|l defect| {d1:.1e}, |p_2 defect on phys| {d2:.1e}, all sectors {d2all:.2f}")

    # ---- H1d: output symmetry (8.13): p^H_{2,2} is eps-ANTIsymmetric, p_{2,2} bar-eps-symmetric
    sw = np.transpose(PH22, (1, 0, 2, 3))
    kk = (-1.0) ** (PAR.reshape(N, 1, 1, 1) * PAR.reshape(1, N, 1, 1))
    d_anti = np.abs(PH22 + kk * sw).max()
    d_sym = np.abs(PH22 - kk * sw).max()
    check("H1d (8.13): the two outputs of p^H_{2,2} are graded ANTIsymmetric in the physical "
          "parity (the symmetry type of omega_1), not symmetric",
          d_anti < TOL and d_sym > 1e-3, f"|anti defect| {d_anti:.1e}, |sym defect| {d_sym:.2f}")

    # ---- H2: the non-augmented (2,2) relation, map form (8.19)/(8.21)
    cfg = {tp: h_config_tensor(toy, V, *tp) for tp in h_tuples(2, 2, "B")}
    check("H2a the (2,2) sum has 7 ordered configurations (Sec. 8.3 table)", len(cfg) == 7,
          f"tuples {sorted(cfg)}")
    tot = sum(cfg.values())
    mixed = cfg[(1, 1, 1, 1)]
    indiv = max(np.abs(T).max() for T in cfg.values())
    d_tot = np.abs(tot).max()
    d_drop = np.abs(tot - mixed).max()          # break leg 1: drop the mixed term A_4
    d_aug = np.abs(tot - 0.5 * mixed).max()     # break leg 2: augmented weight for A_4
    check("H2b (8.19)/(8.21): the seven map-form terms of the non-augmented (2,2) relation "
          "sum to zero elementwise, on all input-parity sectors",
          d_tot < TOL and indiv > 1.0,
          f"|sum| = {d_tot:.1e}, largest single term {indiv:.2f}")
    check("H2c break-on-purpose: dropping the mixed term A_4 (= M_{2,2}), or giving it the "
          "augmented weight 1/2, leaves an O(10) residual",
          d_drop > 1.0 and d_aug > 1.0, f"|sum - A_4| = {d_drop:.2f}, |sum - A_4/2| = {d_aug:.2f}")
    # evaluated on (Psi, Psi): even (N_gh = 2) and odd (N_gh = 3) test inputs
    # NOTE: a numeric test vector supported on odd N_gh does not represent a Grassmann-odd
    # superfield; it is an elementwise probe of the tensor identity restricted to those slots.
    rngh = np.random.default_rng(20260914)
    # two INDEPENDENT test vectors: on the odd sector the inputs of A_4 are graded
    # symmetric in eps, i.e. antisymmetric for two odd slots, so u (x) u annihilates it.
    for tag, par in (("even", 0), ("odd", 1)):
        u = np.where(toy.PAR == par, rngh.standard_normal(N), 0.0)
        v = np.where(toy.PAR == par, rngh.standard_normal(N), 0.0)
        ev = lambda T: np.einsum("cdxy,x,y->cd", T, u, v)
        check(f"H2d (2,2) relation contracted with a random {tag} input pair "
              "pair (seed 20260914): sum = 0, individual terms nonzero",
              np.abs(ev(tot)).max() < TOL and max(np.abs(ev(T)).max() for T in cfg.values()) > 1e-3,
              f"|sum| = {np.abs(ev(tot)).max():.1e}, "
              f"|A_4| = {np.abs(ev(mixed)).max():.2f}")
    # mirror symmetry of the table (3.3), i.e. A_i' = A_i
    dm = max(np.abs(cfg[(i, j, m, n)] - cfg[(m, n, i, j)]).max()
             for (i, j, m, n) in cfg if (m, n, i, j) in cfg)
    check("H2e mirror rows of the Sec. 8.3 table are equal, A_i' = A_i (3.3), hence "
          "B_{2,2} = 2(A_1+A_2+A_3) + A_4", dm < TOL, f"|mirror defect| = {dm:.1e}")

    # ---- H3: the (1,2) and (1,3) relations (8.24)/(8.25)
    for ell, eq in ((2, "8.24"), (3, "8.25")):
        cB = {tp: h_config_tensor(toy, V, *tp) for tp in h_tuples(1, ell, "B")}
        cR = {tp: h_config_tensor(toy, V, *tp) for tp in h_tuples(1, ell, "R")}
        sB = sum(cB.values())
        sR = sum(cR.values())
        big = max(np.abs(T).max() for T in cR.values())
        one = list(cR)[0]
        sR_bad = sR - 2 * cR[one]               # break leg: flip the sign of one term
        check(f"H3 ({1},{ell}) relation ({eq}): augmented sum ({len(cR)} terms) and "
              f"non-augmented sum ({len(cB)} terms) both vanish elementwise",
              np.abs(sR).max() < TOL and np.abs(sB).max() < TOL and big > 1.0
              and len(cR) == ell and len(cB) == 2 * ell,
              f"|R| = {np.abs(sR).max():.1e}, |B| = {np.abs(sB).max():.1e}, "
              f"largest term {big:.2f}")
        check(f"H3' ({1},{ell}) break-on-purpose: flipping the sign of one term leaves O(10)",
              np.abs(sR_bad).max() > 1.0, f"|resid| = {np.abs(sR_bad).max():.2f}")


def part_h2_named_maps(toy: Toy, V: dict[int, np.ndarray], seed2: int = 20260919) -> None:
    """Record 026 Sec. 8.7: the seven (2,2) configurations as NAMED map compositions.

    Definitions (026 (8.26)-(8.29)), fixed once for all rows:
      D1  Qhat_out = Q (x) 1 + 1 (x) Q with the Koszul sign of the strand passed in the
          SHIFTED parity (8.26); plain toy Q (not Q' = (-1)^eps Q).
      D2  Sym_out / Sym_in: NORMALISED graded symmetrisers (1/2)(1 + tau); "(x) 1"
          means strand 1 of the symmetric tensor is fed into slot 1 of the receiving map.
      D3  chi-test of a map F at (Psi, Psi): (1/2!) wt wt F chi chi Psi Psi with
          wt = (-1)^eps omega (8.14); the coefficient tensor of that polynomial in the
          convention of `h_config_tensor` is C[F] = 2 Sym_out Sym_in (wt (x) wt . F) (8.29).
    Each row is built from named maps (raise_map, Q, V_2, V_3 -- NOT h_config_tensor),
    dressed by the R1 sign tensor sigma(c,d,x,y) derived in Sec. 8.7.2 (a function of
    the parities of the four lowered slots), and compared elementwise with the
    configuration tensor.  Verified: the coefficient of every row; the corrected
    identity (8.30) sums to zero; break legs (factor 2, sign) fail; two seeds; the
    even/odd input probes of H2d; the (1,2) coefficient of Qhat p_{1,2} (8.24) is 1;
    the graded-commutator step p22 Qhat_in (Psi,Psi) = 2 p22(Q Psi, Psi) on even Psi,
    used to pass from (8.31) to (8.32).
    Not verified: (1,3) and other (k,l) rows; the dressings off the (2,2) signature.

    Note on the per-row dressings: the sign tensors `sigma` are defined modulo the four
    factors (-1)^eps_i (their product is -1 on this support), so only coef * sigma is
    measured per row, not the individual signs; the physical-sector form (8.31), built
    with l^H and no sign tensors, carries no such ambiguity (026 Sec. 8.7.1).
    The "second toy seed" check below re-draws the VERTICES only: the toy (parities,
    multiplicities, Q, omega) is unchanged; the genuine second toy is `--seed 20260919`.
    """
    N, PAR, sgn, W = toy.N, toy.PAR, toy.sgn, toy.W
    Wt = np.einsum("c,cd->cd", sgn, W)                        # tilde-omega (8.14)
    Q = toy.Q
    p = lambda k, l: raise_map(toy, V[k + l], l, weighted=True)
    P22, P12, P13, P02, P03 = p(2, 2), p(1, 2), p(1, 3), p(0, 2), p(0, 3)
    L2, L3 = p(2, 1), p(3, 1)
    V2, V3 = V[2], V[3]
    E = [_par_tensor(toy, 4, i) for i in range(4)]            # eps of lowered slots c,d,x,y

    def sym01(F: np.ndarray, shifted: bool) -> np.ndarray:
        e0, e1 = (1 - E[0], 1 - E[1]) if shifted else (E[0], E[1])
        return 0.5 * (F + (-1.0) ** (e0 * e1) * np.swapaxes(F, 0, 1))

    def sym23(F: np.ndarray) -> np.ndarray:
        return 0.5 * (F + (-1.0) ** (E[2] * E[3]) * np.swapaxes(F, 2, 3))

    def qhat_out(F: np.ndarray, shifted: bool = True) -> np.ndarray:  # (8.26)
        e0 = 1 - E[0] if shifted else E[0]
        return np.einsum("cC,Cdxy->cdxy", Q, F) + (-1.0) ** e0 * np.einsum("dD,cDxy->cdxy", Q, F)

    def lower(F: np.ndarray) -> np.ndarray:
        return np.einsum("cC,dD,CDxy->cdxy", Wt, Wt, F)

    def C_of(F: np.ndarray, sigma: np.ndarray | float = 1.0) -> np.ndarray:  # (8.29) + dressing
        return 2.0 * sym01(sym23(sigma * lower(F)), shifted=False)

    def ratio(Crow: np.ndarray, Cmap: np.ndarray) -> tuple[float, float]:
        """(constant ratio, spread) over the common support; spread > 0 or a support
        mismatch means 'not proportional'."""
        sup = np.abs(Crow) > 1e-9
        if (np.abs(Cmap[~sup]) > 1e-9).any() or (np.abs(Cmap[sup]) < 1e-12).any():
            return float("nan"), float("inf")
        r = Crow[sup] / Cmap[sup]
        return float(r[0]), float(np.abs(r - r[0]).max())

    one = np.ones((N,) * 4)
    # named single-strand maps F (before Sym), R1 dressing sigma, expected coefficient
    rows = {
        "A1  (0,1|2,1)  Qhat_out p22":                 ((0, 1, 2, 1), qhat_out(P22), one, -0.5),
        "A2  (1,2|1,0)  p22(Q.,.)":                    ((1, 2, 1, 0), np.einsum("cdXy,Xx->cdxy", P22, Q), (-1.0) ** E[3], 1.0),
        "A3  (0,2|2,0)  p12 o l2":                     ((0, 2, 2, 0), np.einsum("cdA,Axy->cdxy", P12, L2), (-1.0) ** (E[0] + E[1]), 0.5),
        "A4  (1,1|1,1)  (l2 x 1)(p12 x 1)":            ((1, 1, 1, 1), np.einsum("cAy,Adx->cdxy", L2, P12), (-1.0) ** E[0], 2.0),
        "A1' (2,1|0,1)  (l3 x 1) p02":                 ((2, 1, 0, 1), np.einsum("cAxy,Ad->cdxy", L3, P02), (-1.0) ** E[0], 1.0),
        "A2' (1,0|1,2)  (V2 x 1 x 1) p13":             ((1, 0, 1, 2), np.einsum("xA,Acdy->cdxy", V2, P13), (-1.0) ** (E[2] * (1 - E[3])), 1.0),
        "A3' (2,0|0,2)  (V3 x 1 x 1) p03":             ((2, 0, 0, 2), np.einsum("xyA,Acd->cdxy", V3, P03), (-1.0) ** (E[0] + E[1]), -0.5),
    }
    total = np.zeros((N,) * 4)
    for name, (tp, F, sig, coef) in rows.items():
        Crow = h_config_tensor(toy, V, *tp)
        Cmap = C_of(F, sig)
        r, spread = ratio(Crow, Cmap)
        # break legs: factor 2 and sign on the named-map side must break the row
        d_ok = np.abs(Crow - coef * Cmap).max()
        d_fac = np.abs(Crow - 2 * coef * Cmap).max()
        d_sgn = np.abs(Crow + coef * Cmap).max()
        check(f"H2N row {name}: ratio row / C[F] = {coef:+.1f} uniform on all sectors",
              spread < TOL and abs(r - coef) < TOL and d_ok < TOL and d_fac > 1.0 and d_sgn > 1.0,
              f"ratio {r:+.3f}, spread {spread:.1e}, |row| {np.abs(Crow).max():.2f}, "
              f"break legs x2: {d_fac:.2f}, sign: {d_sgn:.2f}")
        total += coef * Cmap
    check("H2N (8.30): the seven named-map terms with the corrected coefficients sum to zero "
          "(assembled from named maps only, no h_config_tensor)",
          np.abs(total).max() < TOL, f"|sum| = {np.abs(total).max():.1e}")
    # the record's (8.21) coefficient for the Qhat-term: 1 instead of 1/2 -> fails
    tot_wrong = total - (-0.5) * C_of(qhat_out(P22)) + (-1.0) * C_of(qhat_out(P22))
    check("H2N break-on-purpose: coefficient 1 on Qhat p22 (as in (8.21)) instead of 1/2 leaves O(10)",
          np.abs(tot_wrong).max() > 1.0, f"|resid| = {np.abs(tot_wrong).max():.2f}")
    # D1 alternatives: eps-Koszul coderivation, or Q' inside, do not reproduce A1
    Crow1 = h_config_tensor(toy, V, 0, 1, 2, 1)
    r_eps, s_eps = ratio(Crow1, C_of(qhat_out(P22, shifted=False)))
    Qp = np.diag(sgn) @ Q
    F_qp = np.einsum("cC,Cdxy->cdxy", Qp, P22) + (-1.0) ** (1 - E[0]) * np.einsum("dD,cDxy->cdxy", Qp, P22)
    r_qp, s_qp = ratio(Crow1, C_of(F_qp))
    check("H2N D1 alternatives rejected: eps-Koszul Qhat or Q' = (-1)^eps Q inside Qhat are not "
          "proportional to A1", not (s_eps < TOL) and not (s_qp < TOL),
          f"eps-Koszul spread {s_eps:.1e}, Q' spread {s_qp:.1e}")
    # physical sector: dressings reduce to the ell^H form (8.31); test on N_gh = 2 inputs
    phys = np.where(toy.NGH == 2)[0]
    blk = np.ix_(np.arange(N), np.arange(N), phys, phys)
    LH2 = np.tensordot(toy.Delta, V3, axes=([1], [0]))          # Harold's l^H_2 = Delta o V_3
    LH3 = np.tensordot(toy.Delta, V[4], axes=([1], [0]))
    F_phys = (-0.5 * C_of(qhat_out(P22))
              + C_of(np.einsum("cdXy,Xx->cdxy", P22, Q))
              - 0.5 * C_of(np.einsum("cdA,Axy->cdxy", P12, L2))
              - 2.0 * C_of(np.einsum("cAy,Adx->cdxy", LH2, P12))
              - C_of(np.einsum("cAxy,Ad->cdxy", LH3, P02))
              + C_of(np.einsum("xA,Acdy->cdxy", V2, P13))
              + 0.5 * C_of(np.einsum("xyA,Acd->cdxy", V3, P03)))
    big = max(np.abs(C_of(qhat_out(P22))[blk]).max(), 1.0)
    check("H2N (8.31) physical-sector form (l^H_2, l^H_3 in the two dressed rows, plain Q, "
          "no sign tensors) vanishes on N_gh = 2 inputs and NOT off that block",
          np.abs(F_phys[blk]).max() < TOL and np.abs(F_phys).max() > 1.0,
          f"|phys block| = {np.abs(F_phys[blk]).max():.1e}, off-block {np.abs(F_phys).max():.2f}, "
          f"|Qhat p22| on block {big:.2f}")
    # even / odd input probes of H2d, on the named-map assembly
    rngh = np.random.default_rng(20260914)
    for tag, par in (("even", 0), ("odd", 1)):
        u = np.where(PAR == par, rngh.standard_normal(N), 0.0)
        v = np.where(PAR == par, rngh.standard_normal(N), 0.0)
        ev = lambda T: np.einsum("cdxy,x,y->cd", T, u, v)
        a1 = np.abs(ev(-0.5 * C_of(qhat_out(P22)))).max()
        check(f"H2N named-map assembly contracted with a random {tag} input pair (seed 20260914): "
              "sum = 0, Qhat-term nonzero", np.abs(ev(total)).max() < TOL and a1 > 1e-3,
              f"|sum| = {np.abs(ev(total)).max():.1e}, |Qhat p22 term| = {a1:.2f}")
    # the graded-commutator step used to pass from (8.31) to (8.32):
    #   p_{2,2} Qhat_in (Psi, Psi) = 2 p_{2,2}(Q Psi, Psi)   on even Psi   (026 Sec. 8.7.3)
    # with Qhat_in the input-side coderivation (8.27).  Falsifiable: the factor 2 is tested
    # (factor 1 must fail), and the identity must FAIL for two independent even vectors,
    # i.e. it is a property of the diagonal evaluation at (Psi, Psi), not of the tensor.
    A_in = np.einsum("cdXy,Xx->cdxy", P22, Q)                 # p22(Q ., .)
    B_in = np.einsum("cdxY,Yy->cdxy", P22, Q)                 # p22(., Q .)
    Qhat_in = A_in + (-1.0) ** E[2] * B_in                    # (8.27)
    u_e = np.where(PAR == 0, rngh.standard_normal(N), 0.0)
    w_e = np.where(PAR == 0, rngh.standard_normal(N), 0.0)
    ev2 = lambda T, a, b: np.einsum("cdxy,x,y->cd", T, a, b)  # noqa: E731
    d_step = np.abs(ev2(Qhat_in, u_e, u_e) - 2.0 * ev2(A_in, u_e, u_e)).max()
    d_step_fac = np.abs(ev2(Qhat_in, u_e, u_e) - 1.0 * ev2(A_in, u_e, u_e)).max()
    d_step_off = np.abs(ev2(Qhat_in, u_e, w_e) - 2.0 * ev2(A_in, u_e, w_e)).max()
    check("H2N graded-commutator step (8.31) -> (8.32): p22 Qhat_in (Psi,Psi) = 2 p22(Q Psi, Psi) "
          "on even Psi (break legs: factor 1, and two independent even vectors)",
          d_step < TOL and d_step_fac > 1e-3 and d_step_off > 1e-3,
          f"|defect| = {d_step:.1e}, factor-1 leg {d_step_fac:.2f}, off-diagonal leg {d_step_off:.2f}")
    # (1,2): the same reading rule gives coefficient 1 on Qhat p12 and on p12(Q Psi) (8.24)
    def C1(F: np.ndarray, sigma: np.ndarray | float = 1.0) -> np.ndarray:
        """coefficient tensor of (1/2!) wt wt F chi chi Psi for a map H -> H(x)H (no factor 2)."""
        X = sigma * np.einsum("cC,dD,CDx->cdx", Wt, Wt, F)
        e0, e1 = _par_tensor(toy, 3, 0), _par_tensor(toy, 3, 1)
        return 0.5 * (X + (-1.0) ** (e0 * e1) * np.swapaxes(X, 0, 1))
    e0, e1 = _par_tensor(toy, 3, 0), _par_tensor(toy, 3, 1)
    Qh12 = np.einsum("cC,Cdx->cdx", Q, P12) + (-1.0) ** (1 - e0) * np.einsum("dD,cDx->cdx", Q, P12)
    r1, s1 = ratio(h_config_tensor(toy, V, 0, 1, 1, 1), C1(Qh12))
    r2, s2 = ratio(h_config_tensor(toy, V, 0, 2, 1, 0), C1(np.einsum("cdX,Xx->cdx", P12, Q)))
    check("H2N (1,2) control: (0,1|1,1) = -1 x Qhat_out p12 (coefficient 1, not 1/2) and "
          "(0,2|1,0) = +1 x p12(Q Psi), no dressing: (8.24) is [Qhat, p12] = 0 with plain Q",
          s1 < TOL and abs(r1 + 1) < TOL and s2 < TOL and abs(r2 - 1) < TOL,
          f"Qhat p12 ratio {r1:+.3f} (spread {s1:.1e}), p12(Q.) ratio {r2:+.3f} (spread {s2:.1e})")
    # second seed: rebuild the generator and repeat the row ratios
    rng2 = np.random.default_rng(seed2)
    V2nd, _ = build_generator(toy, rng2, 4)
    P22b, P12b, P13b, P02b, P03b = (raise_map(toy, V2nd[k + l], l, weighted=True)
                                    for k, l in ((2, 2), (1, 2), (1, 3), (0, 2), (0, 3)))
    L2b, L3b = raise_map(toy, V2nd[3], 1, weighted=True), raise_map(toy, V2nd[4], 1, weighted=True)
    rows_b = {
        (0, 1, 2, 1): (qhat_out(P22b), one, -0.5),
        (1, 2, 1, 0): (np.einsum("cdXy,Xx->cdxy", P22b, Q), (-1.0) ** E[3], 1.0),
        (0, 2, 2, 0): (np.einsum("cdA,Axy->cdxy", P12b, L2b), (-1.0) ** (E[0] + E[1]), 0.5),
        (1, 1, 1, 1): (np.einsum("cAy,Adx->cdxy", L2b, P12b), (-1.0) ** E[0], 2.0),
        (2, 1, 0, 1): (np.einsum("cAxy,Ad->cdxy", L3b, P02b), (-1.0) ** E[0], 1.0),
        (1, 0, 1, 2): (np.einsum("xA,Acdy->cdxy", V2nd[2], P13b), (-1.0) ** (E[2] * (1 - E[3])), 1.0),
        (2, 0, 0, 2): (np.einsum("xyA,Acd->cdxy", V2nd[3], P03b), (-1.0) ** (E[0] + E[1]), -0.5),
    }
    worst = 0.0
    for tp, (F, sig, coef) in rows_b.items():
        r, spread = ratio(h_config_tensor(toy, V2nd, *tp), C_of(F, sig))
        worst = max(worst, spread, abs(r - coef))
    check(f"H2N second toy seed {seed2}: all seven row coefficients and dressings reproduced",
          worst < TOL, f"worst deviation {worst:.1e}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mult", default="2,4,4,2", help="N_gh multiplicities m1,m2,m3,m4")
    ap.add_argument("--seed", type=int, default=20260908)
    ap.add_argument("--maxr", type=int, default=6, help="highest vertex rank generated")
    ap.add_argument("--sigs", default="2:2", help="part A signatures k:l, comma separated")
    args = ap.parse_args()
    mult = tuple(int(x) for x in args.mult.split(","))
    rng = np.random.default_rng(args.seed)
    print(f"seed = {args.seed}, multiplicities = {mult}, maxr = {args.maxr}")
    toy = Toy(mult)
    N = toy.N

    # --- 1. toy space sanity (010 checks 1a-1e) --------------------------------
    check("1a omega_1 . Delta = id", np.allclose(toy.W @ toy.Delta, np.eye(N)))
    check("1b Q^2 = 0", np.allclose(toy.Q @ toy.Q, 0))
    V2 = toy.W @ toy.Q
    check("1c Q cyclic (V2 graded symmetric)", toy.is_graded_symmetric(V2) < TOL)
    QmD = toy.Q @ toy.Delta - np.einsum("aj,a,bj->ab", toy.Delta, toy.sgn, toy.Q)
    QpD = toy.Q @ toy.Delta + np.einsum("aj,a,bj->ab", toy.Delta, toy.sgn, toy.Q)
    check("1e odd-pairing Q-move (1.3): Q u.v - (-)^u u.Qv = 0, naive form nonzero",
          np.allclose(QmD, 0) and np.abs(QpD).max() > 0.5)

    # --- 2. generator ----------------------------------------------------------
    V, (G3, G4) = build_generator(toy, rng, args.maxr)
    for n, T in V.items():
        check(f"2a V_{n} graded symmetric and saturating at N_gh {2*n}",
              toy.is_graded_symmetric(T) < TOL and toy.saturation_of(T) <= {2 * n},
              f"|V_{n}| = {np.abs(T).max():.3f}, saturation {sorted(toy.saturation_of(T))}")
    check("2b generator non-hollow: all V_3..V_maxr nonzero",
          all(np.abs(V[n]).max() > 1e-3 for n in range(3, args.maxr + 1)))
    # L_infty relations = rank-n parts of (S,S), n = 2..maxr  <=> (n-1,1,0) relations
    for n in range(2, args.maxr + 1):
        R = ss_rank(toy, V, n)
        # non-hollowness: individual terms O(1)
        terms = [np.abs(toy.antibracket(V[i], V[n + 2 - i])).max()
                 for i in V if (n + 2 - i) in V and i >= 3 and n + 2 - i >= 3]
        check(f"2c (S,S) rank {n} = 0  [L_infty relation ({n-1},1,0)]", np.abs(R).max() < TOL,
              f"|resid| = {np.abs(R).max():.1e}; individual ell.ell terms {[f'{t:.2f}' for t in terms]}")
    # break on purpose: perturb V_4 by a random symmetric tensor (same saturation)
    Vbad = dict(V)
    Vbad[4] = V[4] + 0.1 * toy.random_sym(4, 8, rng)
    Rb = ss_rank(toy, Vbad, 4)
    check("2d break-on-purpose: perturbed V_4 violates the (3,1,0) relation",
          np.abs(Rb).max() > 1e-3, f"|resid| = {np.abs(Rb).max():.2f}")

    # --- 3. independent cross-check of the antibracket convention (010 formulas) ---
    # FINDING (7a): the products derived from S through the antibracket (1.5) are NOT
    # ell_n = Delta o V_{n+1} but ell'_n = W . Delta o V_{n+1}, W = (-1)^F on the output,
    # uniformly in n (including Q' = W Q = ell'_1).  Equivalently: raise with the
    # graded-symmetric bivector Dt^{ab} = (-1)^{eps_a} Delta^{ab} (MS/DeWitt _ie = (-1)^i e_i).
    # With the plain Delta the operator-form relations of 010 FAIL (3c).
    L2 = ell_from_V(toy, V[3])
    L3 = ell_from_V(toy, V[4])
    Wo = lambda T: np.einsum("a,a...->a...", toy.sgn, T)
    import copy as _copy
    toyp = _copy.copy(toy)
    toyp.Q = np.diag(toy.sgn) @ toy.Q  # Q' = W Q
    L2p, L3p = Wo(L2), Wo(L3)
    check("3a [Q', ell'_2] = 0 via 010's commutator formula, ell' = W.Delta o V, Q' = W Q",
          np.abs(q_l2_commutator(toyp, L2p)).max() < TOL,
          f"|resid| = {np.abs(q_l2_commutator(toyp, L2p)).max():.1e}")
    Jp = q_l3_commutator(toyp, L3p) + jac2(toyp, L2p)
    check("3b [Q', ell'_3] + ell'_2 o_1 ell'_2 = 0 via 010's formulas (independent), terms O(1)",
          np.abs(Jp).max() < TOL and np.abs(jac2(toyp, L2p)).max() > 1e-3,
          f"|resid| = {np.abs(Jp).max():.1e}, |ell'_2 o ell'_2| = {np.abs(jac2(toyp, L2p)).max():.2f}")
    J0 = q_l3_commutator(toy, L3) + jac2(toy, L2)
    check("3c with the PLAIN Delta-raising (no W) the operator-form relations FAIL (W is load-bearing)",
          np.abs(q_l2_commutator(toy, L2)).max() > 1e-3 and np.abs(J0).max() > 1e-3,
          f"|[Q,l2]| = {np.abs(q_l2_commutator(toy, L2)).max():.2f}, |[Q,l3]+l2l2| = {np.abs(J0).max():.2f}")
    check("3d Q' = W Q is nilpotent, cyclic and satisfies the odd-pairing Q-move (1.3)",
          np.allclose(toyp.Q @ toyp.Q, 0)
          and toy.is_graded_symmetric(toy.W @ toyp.Q) < TOL
          and np.allclose(toyp.Q @ toy.Delta - np.einsum("aj,a,bj->ab", toy.Delta, toy.sgn, toyp.Q), 0))
    check("3e weighted raising reproduces ell': Dt o V_3 == ell'_2, Dt o V_4 == ell'_3",
          np.allclose(raise_map(toy, V[3], 1, weighted=True), L2p)
          and np.allclose(raise_map(toy, V[4], 1, weighted=True), L3p))

    # --- 4. raising map and output symmetry (1.7) -------------------------------
    for (k, ell) in [(1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (1, 4), (2, 4)]:
        n = k + ell
        if n not in V:
            continue
        for wtd in (False, True):
            P = raise_map(toy, V[n], ell, weighted=wtd)
            # adjacent transpositions generate S_ell; non-adjacent swaps carry extra Koszul factors
            d_sh = max(swap_defect(toy, P, i, i + 1, "shifted") for i in range(ell - 1))
            d_st = max(swap_defect(toy, P, i, i + 1, "std") for i in range(ell - 1))
            check(f"4a p_{{{k},{ell}}}{'~' if wtd else ''} outputs graded symmetric in the SHIFTED parity only (eq. 1.7)",
                  d_sh < TOL and d_st > 1e-3 and np.abs(P).max() > 1e-3,
                  f"shifted defect {d_sh:.1e}, physical-parity defect {d_st:.2f}")
    # p_{k,1} = ell_k consistency with (1.4)
    check("4b p_{2,1} == ell_2 and p_{3,1} == ell_3 (plain-Delta/Zwiebach raising, cf. eq. 1.4)",
          np.allclose(raise_map(toy, V[3], 1), L2) and np.allclose(raise_map(toy, V[4], 1), L3))

    # --- 5. R16 reproduction: generic data (as in 010) and the generator's data ------
    rng2 = np.random.default_rng(args.seed + 1)
    V3g = toy.random_sym(3, 6, rng2)
    V4g = toy.random_sym(4, 8, rng2)
    r16_checks(toy, ell_from_V(toy, V3g), ell_from_V(toy, V4g), "generic", expect_assembly=False)
    r16_checks(toyp, L2p, L3p, "Linfty", expect_assembly=True)

    # --- 5b. sub-task 7b: checks E1-E7 (record 026 Sec. 3) ---------------------------
    part_b7_checks(toy, V, toyp, L2p, L3p)
    part_b_checks(toy, V, np.random.default_rng(args.seed + 3))
    part_b_parity_checks(toy, V, np.random.default_rng(args.seed + 4))
    part_b_decalage_checks(toy, V, np.random.default_rng(args.seed + 5))
    part_b_multistring_checks(toy, V, np.random.default_rng(args.seed + 6))
    part_b_host3_checks(toy, V, np.random.default_rng(args.seed + 7))

    # --- 6. sub-task 7c: part A table (record 026 Sec. 4) --------------------------
    sigs = [tuple(int(x) for x in t.split(":")) for t in args.sigs.split(",")]
    part_a_table(toy, V, np.random.default_rng(args.seed + 2), sigs)

    # --- 7. record 026 Sec. 8: Harold's convention (H1-H3) -------------------------
    part_h_checks(toy, V)
    part_h2_named_maps(toy, V)

    n_fail = sum(not ok for _, ok in RESULTS)
    print(f"summary: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS (seed {args.seed})")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
