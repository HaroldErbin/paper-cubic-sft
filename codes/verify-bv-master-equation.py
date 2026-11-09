"""
Verify the truncated classical BV master equation in a finite cyclic L_infty model.

Record: agent/derivations/058-bv-master-equation.md (Part B, node C4).

Model. Parent DGLA L = A (x) End(W): A = span(1, eps), deg eps = 3, eps^2 = 0,
integral int eps = 1 (a finite stand-in for H^*(S^3)); W graded with a random
differential D (D^2 = 0); product with Koszul sign, graded commutator, Q = [1(x)D, .],
cyclic pairing <x, y> = tau(x y), tau(a (x) E_ij) = int(a) delta_ij (-1)^{w_i}
(degree -3). Its BV action is the matrix Chern-Simons action
    S(Phi) = tau( 1/2 Phi Q Phi + g/3 Phi Phi Phi ),
Phi = sum_s e_s phi^s of total degree 1 (coordinate phi^s of parity 1 - deg e_s),
i.e. the string field of all ghost numbers (Zwiebach 1993, (3.33)-(3.35)), with
degree = N_gh - 1.

Transfer. A symplectic Hodge decomposition L = H + I + C (I = im Q, C Lagrangian
complement, H their omega-orthogonal) is built degree by degree; the massive pairs
(I'', C'') in a chosen set of degrees are integrated out at tree level:
Phi = iota psi + chi, chi = -g h''(Phi Phi), h'' = (Q|C'')^{-1} P_{I''}, and
S_eff(psi) = S(Phi(psi)) = sum_n g^{n-2} S_n. This is the tree-level BV pushforward;
its Taylor coefficients S_n are the cyclic transferred brackets, with S_4 != 0
(the l_3^tr of the brief).

Checks (named after the claim-tree nodes of record 058):
  C4-B0   anchor: parent CS action satisfies (S,S) = 0 (fixes the antibracket sign
          convention on objects not under test).
  C4-B1   untransferred-out, untruncated S_eff: [g^m](S,S) = 0 for m <= M.
  C4-B2   truncations k = 2, 3: [g^m](S^(k),S^(k)) = 0 for m <= k, and
          [g^{k+1}] = -2 (S_2, S_{k+3}) = sum_{a+b=k+5, 3<=a,b<=k+2} (S_a,S_b)
          (truncation lemma (2.5)/(2.8)); remainder nonzero.
  C4-B3   S_BV = S^(k) - g^2/4! p(Yh,Yh) with a contractible pair (Yh even, Yh+ odd):
          (S_BV,S_BV) = (S^(k),S^(k)) at every order (056 lemma (e)).
  Break legs (must FAIL the identity): sign of S_4 flipped; antifield terms dropped
  from S_3; terms quadratic in antifields dropped from S_4 (antifield number two, the
  terms the transferred l_3 generates; falls back to S_5 if S_4 has none); S_4 -> 0
  (l_3^tr -> 0); random non-L_infty quartic on S_4's support; B3 with a psi-dependent
  Yh+ term.

Independent content vs bookkeeping (critic-058, 2026-09-26). B0 and B1 (with
B1-nontrivial) are the independent checks; the break legs are their falsifiers.
B2-* are rearrangements of the same coefficient table as B1 (lhs - rhs = J_{k+1} of
the full action, i.e. B1 at m = k+1; B2-vanish is B1 at m <= k) and B3 tests record
056's lemma (e) on a toy pair: both are BOOKKEEPING and are tallied separately in the
summary line.

Not verified: the string-theory vertices themselves (the model is a finite cyclic
L_infty algebra, not the worldsheet one); the quantum master equation; k = 4 with
Sigma_3; level truncation.

"""

from __future__ import annotations

import itertools
import sys

import numpy as np

M_ORDER = 4  # g-order kept (needs S_n up to n = 6)
TOL = 1e-9
failures: list[str] = []
tally = {"independent": 0, "falsifier": 0, "bookkeeping": 0}


def kind_of(name: str) -> str:
    """Classify: independent (B0, B1), falsifier of B1 (break legs), bookkeeping.

    B2-* and B3-* checks, including their own break legs, are bookkeeping.

    """
    if name.startswith(("C4-B2", "C4-B3")):
        return "bookkeeping"
    if "break" in name or "control" in name:
        return "falsifier"
    return "independent"


def report(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    tally[kind_of(name)] += 1
    if not ok:
        failures.append(name)


# ------------------------------------------------ Grassmann polynomials in (psi, g)
class GP:
    """Polynomial in even/odd variables and a nilpotent even parameter g (g^{M+1}=0).

    Key: (gpow, even-vars sorted tuple with repetition, odd-vars strictly sorted
    tuple); the monomial is written g^gpow * prod(even) * odd_1 odd_2 ... in order.

    """

    par: list[int] = []

    def __init__(self, t: dict | None = None) -> None:
        self.t = t if t is not None else {}

    @staticmethod
    def var(i: int, c: float = 1.0) -> GP:
        if GP.par[i]:
            return GP({(0, (), (i,)): c})
        return GP({(0, (i,), ()): c})

    def __add__(self, o: GP) -> GP:
        t = dict(self.t)
        for k, v in o.t.items():
            t[k] = t.get(k, 0.0) + v
        return GP(t)

    def scale(self, c: float) -> GP:
        return GP({k: c * v for k, v in self.t.items()}) if c != 0 else GP()

    def gshift(self, n: int) -> GP:
        return GP({(k[0] + n, k[1], k[2]): v for k, v in self.t.items() if k[0] + n <= M_ORDER})

    def __mul__(self, o: GP) -> GP:
        t: dict = {}
        for (ga, ea, oa), ca in self.t.items():
            for (gb, eb, ob), cb in o.t.items():
                if ga + gb > M_ORDER:
                    continue
                if oa and ob and set(oa) & set(ob):
                    continue
                inv = sum(1 for i in oa for j in ob if i > j)
                k = (ga + gb, tuple(sorted(ea + eb)), tuple(sorted(oa + ob)))
                t[k] = t.get(k, 0.0) + (-ca * cb if inv % 2 else ca * cb)
        return GP(t)

    def deriv(self, i: int, side: str) -> GP:
        t: dict = {}
        for (g, e, o), c in self.t.items():
            if GP.par[i]:
                if i not in o:
                    continue
                p = o.index(i)
                s = p if side == "l" else len(o) - 1 - p
                k = (g, e, o[:p] + o[p + 1 :])
                t[k] = t.get(k, 0.0) + (-c if s % 2 else c)
            else:
                n = e.count(i)
                if n == 0:
                    continue
                j = e.index(i)
                k = (g, e[:j] + e[j + 1 :], o)
                t[k] = t.get(k, 0.0) + n * c
        return GP(t)

    def gpart(self, m: int) -> GP:
        return GP({k: v for k, v in self.t.items() if k[0] == m})

    def maxabs(self) -> float:
        return max((abs(v) for v in self.t.values()), default=0.0)

    def degree_part(self, n: int) -> GP:
        return GP({k: v for k, v in self.t.items() if len(k[1]) + len(k[2]) == n})


def antibracket(F: GP, G: GP, P: np.ndarray, nvar: int) -> GP:
    """(F,G) = sum_{a,b} d_r F/dx^a P^{ab} d_l G/dx^b."""
    dF = [F.deriv(a, "r") for a in range(nvar)]
    dG = [G.deriv(b, "l") for b in range(nvar)]
    out = GP()
    for a, b in zip(*np.nonzero(np.abs(P) > 1e-14)):
        if dF[a].t and dG[b].t:
            out = out + (dF[a] * dG[b]).scale(P[a, b])
    return out


# ------------------------------------------------ parent DGLA A (x) End(W)
def build_parent(wdeg: list[int], rng: np.random.Generator):
    m = len(wdeg)
    basis = [(a, i, j) for a in (0, 1) for i in range(m) for j in range(m)]
    idx = {b: n for n, b in enumerate(basis)}
    deg = np.array([3 * a + wdeg[i] - wdeg[j] for (a, i, j) in basis])
    N = len(basis)
    prod = np.zeros((N, N, N))  # e_s e_t = sum_u prod[s,t,u] e_u
    for s, (a, i, j) in enumerate(basis):
        for t, (b, k, l) in enumerate(basis):
            if j != k or a + b > 1:
                continue
            sign = (-1) ** (((wdeg[i] - wdeg[j]) * 3 * b) % 2)
            prod[s, t, idx[(a + b, i, l)]] += sign
    tau = np.array([1.0 * (a == 1 and i == j) * (-1) ** wdeg[i] for (a, i, j) in basis])
    G = np.einsum("stu,u->st", prod, tau)
    # random differential on W: degree +1, D^2 = 0
    for _ in range(1000):
        D = np.zeros((m, m))
        for i in range(m):
            for j in range(m):
                if wdeg[i] == wdeg[j] + 1:
                    D[i, j] = rng.standard_normal()
        # impose D^2 = 0 by projecting later maps onto kernel of earlier ones
        for d in sorted(set(wdeg)):
            rows = [i for i in range(m) if wdeg[i] == d + 1]
            cols = [j for j in range(m) if wdeg[j] == d]
            prev = [j for j in range(m) if wdeg[j] == d - 1]
            if rows and cols and prev:
                Dprev = D[np.ix_(cols, prev)]
                Pk = np.eye(len(cols)) - Dprev @ np.linalg.pinv(Dprev)
                D[np.ix_(rows, cols)] = D[np.ix_(rows, cols)] @ Pk
        if np.allclose(D @ D, 0):
            break
    Dhat = np.zeros(N)
    for i in range(m):
        for j in range(m):
            if D[i, j]:
                Dhat[idx[(0, i, j)]] = D[i, j]
    # Q e_t = Dhat e_t - (-1)^{deg t} e_t Dhat ;  Q[u, t]
    Q = np.einsum("s,stu->ut", Dhat, prod) - np.einsum(
        "t,tsu,s->ut", (-1.0) ** deg, prod, Dhat
    )
    return basis, deg, prod, G, Q, D


def nullspace(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    if A.shape[0] == 0:
        return np.eye(A.shape[1])
    u, s, vt = np.linalg.svd(A)
    r = int((s > tol).sum())
    return vt[r:].T


def colspace(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    u, s, vt = np.linalg.svd(A)
    r = int((s > tol).sum())
    return u[:, :r]


def hodge(deg, G, Q, rng):
    """Symplectic Hodge decomposition, degree by degree: dict d -> (H, I, C) bases."""
    N = len(deg)
    out = {}
    degs = sorted(set(deg.tolist()))
    K, I, C = {}, {}, {}
    for d in degs:
        sd = np.where(deg == d)[0]
        emb = np.eye(N)[:, sd]
        Kd = emb @ nullspace(Q @ emb)
        prev = np.where(deg == d - 1)[0]
        Id = colspace(Q @ np.eye(N)[:, prev]) if len(prev) else np.zeros((N, 0))
        # random complement of K_d in L_d
        R = emb @ rng.standard_normal((len(sd), len(sd)))
        Pk = Kd @ np.linalg.pinv(Kd) if Kd.shape[1] else np.zeros((N, N))
        Cd = colspace((np.eye(N) - Pk) @ R)[:, : len(sd) - Kd.shape[1]]
        K[d], I[d], C[d] = Kd, Id, Cd
    for d in degs:  # isotropise C_d against C_{3-d} for d < 3 - d
        dp = 3 - d
        if d < dp and dp in C and C[d].shape[1] and C[dp].shape[1]:
            # find k(c) = I_d X with <c + I_d X, c'> = 0  for c' in C_dp
            A = I[d].T @ G @ C[dp]  # (dimI, dimC')
            B = C[d].T @ G @ C[dp]  # (dimC, dimC')
            X = -np.linalg.solve(A.T, B.T)  # (dimI, dimC)
            C[d] = C[d] + I[d] @ X
    for d in degs:
        dp = 3 - d
        Cp = C.get(dp, np.zeros((N, 0)))
        if Cp.shape[1] and K[d].shape[1]:
            H = K[d] @ nullspace(Cp.T @ G @ K[d])
        else:
            H = K[d]
        out[d] = (H, I[d], C[d])
    return out


# ------------------------------------------------ superfield algebra
def sf_prod(X, Y, px, py, deg, prod):
    """Superfield product (sum e_s x^s)(sum e_t y^t); px, py: parities of x^s, y^t."""
    N = len(deg)
    out = [GP() for _ in range(N)]
    nz = np.argwhere(np.abs(prod) > 0)
    for s, t, u in nz:
        if not X[s].t or not Y[t].t:
            continue
        sign = (-1) ** ((px[s] * deg[t]) % 2)
        out[u] = out[u] + (X[s] * Y[t]).scale(sign * prod[s, t, u])
    return out


def sf_tau(X, tau_vec):
    out = GP()
    for s, c in enumerate(tau_vec):
        if c and X[s].t:
            out = out + X[s].scale(c)
    return out


def run_model(seed: int, wdeg: list[int], cut_degs: tuple[int, ...]):
    rng = np.random.default_rng(seed)
    basis, deg, prod, G, Q, D = build_parent(wdeg, rng)
    N = len(deg)
    tau = np.array([1.0 * (a == 1 and i == j) * (-1) ** wdeg[i] for (a, i, j) in basis])
    dec = hodge(deg, G, Q, rng)
    # retract: H + (I', C') ; integrate out C'' in degrees cut_degs and I'' = Q C''
    keep, Iint, Cint = [], [], []
    for d, (H, I, C) in dec.items():
        keep += [H[:, c] for c in range(H.shape[1])]
    for d, (H, I, C) in dec.items():
        for c in range(C.shape[1]):
            v = C[:, c]
            (Cint if d in cut_degs else keep).append(v)
            (Iint if d in cut_degs else keep).append(Q @ v)
    B = np.column_stack(keep + Iint + Cint)
    nk, ni = len(keep), len(Iint)
    if np.linalg.matrix_rank(B, tol=1e-9) != N:
        raise ValueError("decomposition not a basis")
    Binv = np.linalg.inv(B)
    PI = B[:, nk : nk + ni] @ Binv[nk : nk + ni]  # projector on I''
    Cm = np.column_stack(Cint) if Cint else np.zeros((N, 0))
    Im = Q @ Cm
    hpp = Cm @ np.linalg.pinv(Im) @ PI if Cint else np.zeros((N, N))
    Kb = np.column_stack(keep)
    kdeg = np.array([int(round(deg[np.argmax(np.abs(v))])) for v in keep])
    for a, v in enumerate(keep):  # degree homogeneity
        assert np.allclose(v[deg != kdeg[a]], 0)
    om = Kb.T @ G @ Kb
    return dict(deg=deg, prod=prod, G=G, Q=Q, tau=tau, Kb=Kb, kdeg=kdeg, hpp=hpp,
                om=om, nk=nk, nint=len(Cint), N=N)


def cs_action(Phi, par, mod, g_on=True):
    deg, prod, Q, tau = mod["deg"], mod["prod"], mod["Q"], mod["tau"]
    N = len(deg)
    QPhi = [GP() for _ in range(N)]
    for u in range(N):
        for t in np.nonzero(np.abs(Q[u]) > 1e-14)[0]:
            if Phi[t].t:
                QPhi[u] = QPhi[u] + Phi[t].scale(Q[u, t])
    parQ = [(1 + 1 - deg[u]) % 2 for u in range(N)]  # QPhi total degree 2
    S2 = sf_tau(sf_prod(Phi, QPhi, par, parQ, deg, prod), tau).scale(0.5)
    PP = sf_prod(Phi, Phi, par, par, deg, prod)
    par2 = [(2 - deg[u]) % 2 for u in range(N)]
    S3 = sf_tau(sf_prod(Phi, PP, par, par2, deg, prod), tau).scale(1.0 / 3.0)
    return S2 + S3.gshift(1), PP


def effective_action(mod):
    deg, prod, Kb, hpp = mod["deg"], mod["prod"], mod["Kb"], mod["hpp"]
    N, nk = mod["N"], mod["nk"]
    GP.par = [int((1 - mod["kdeg"][a]) % 2) for a in range(nk)] + [0] * 8
    par = [int((1 - deg[u]) % 2) for u in range(N)]
    base = [GP() for _ in range(N)]
    for u in range(N):
        for a in range(nk):
            if abs(Kb[u, a]) > 1e-14:
                base[u] = base[u] + GP.var(a, Kb[u, a])
    Phi = base
    for _ in range(M_ORDER + 1):  # chi = -g h''(Phi Phi), iterate to order g^M
        PP = sf_prod(Phi, Phi, par, par, deg, prod)
        chi = [GP() for _ in range(N)]
        for u in range(N):
            for v in np.nonzero(np.abs(hpp[u]) > 1e-14)[0]:
                if PP[v].t:
                    chi[u] = chi[u] + PP[v].scale(-hpp[u, v])
        Phi = [base[u] + chi[u].gshift(1) for u in range(N)]
    S, _ = cs_action(Phi, par, mod)
    return S


def S_by_n(S: GP) -> dict[int, GP]:
    """S = sum_n g^{n-2} S_n: split by g-power, check homogeneity n = gpow + 2."""
    out = {}
    for m in range(M_ORDER + 1):
        Sm = S.gpart(m)
        Sm_h = GP({(0, k[1], k[2]): v for k, v in Sm.t.items()})
        if Sm_h.t and any(len(k[1]) + len(k[2]) != m + 2 for k in Sm_h.t):
            raise ValueError("S_eff not homogeneous of degree gpow + 2")
        out[m + 2] = Sm_h
    return out


def bv_poisson(om: np.ndarray, kdeg: np.ndarray) -> np.ndarray:
    """Antibracket matrix P^{ab} in (F,G) = d_rF/dx^a P^{ab} d_lG/dx^b.

    P = om^{-1} diag((-1)^deg). om_ab = <b_a, b_b> is a symmetric matrix (its support
    has deg_a + deg_b = 3, so one degree is even), hence P is antisymmetric, the form
    required by C2 (P^{x x+} = -P^{x+ x}); the overall sign is irrelevant for (S,S).

    """
    return np.linalg.inv(om) @ np.diag((-1.0) ** kdeg)


def pair_table(Sn: dict[int, GP], P: np.ndarray, nk: int, nmax: int) -> dict:
    tab = {}
    for a in range(2, nmax + 1):
        for b in range(2, nmax + 1):
            if a + b - 4 <= M_ORDER:
                tab[(a, b)] = antibracket(Sn[a], Sn[b], P, nk)
    return tab


def J(tab: dict, m: int, allowed=lambda a, b: True) -> GP:
    out = GP()
    for (a, b), v in tab.items():
        if a + b - 4 == m and allowed(a, b):
            out = out + v
    return out


def scale_of(Sn: dict, P: np.ndarray, m: int) -> float:
    """Natural size of [g^m](S,S): max over pairs of |S_a| |S_b| |P| (a+b-4 = m)."""
    pmax = np.abs(P).max()
    vals = [Sn[a].maxabs() * Sn[b].maxabs() * pmax
            for a in Sn for b in Sn if a + b - 4 == m]
    return max(vals + [1e-300])


def rel(x: GP, sc: float) -> float:
    return x.maxabs() / sc


def one_seed(seed: int, wdeg: list[int], cut: tuple[int, ...]) -> None:
    print(f"\n=== seed {seed}: W degrees {wdeg} (m = dim W = {len(wdeg)}), "
          f"integrated-out C'' degrees {cut}")
    # ---- B0 anchor: parent CS action, nothing integrated out
    mod0 = run_model(seed, wdeg, ())
    S0 = S_by_n(effective_action(mod0))
    P0 = bv_poisson(mod0["om"], mod0["kdeg"])
    t0 = pair_table(S0, P0, mod0["nk"], 3)
    r0 = [rel(J(t0, m), scale_of(S0, P0, m)) for m in range(3)]
    report(f"C4-B0 seed {seed}: parent matrix-CS (S,S)=0 at g^0,g^1,g^2",
           max(r0) < TOL, f"dim L = {mod0['N']}, rel = {max(r0):.1e}")
    # ---- transferred model
    mod = run_model(seed, wdeg, cut)
    nk = mod["nk"]
    S = effective_action(mod)
    Sn = S_by_n(S)
    P = bv_poisson(mod["om"], mod["kdeg"])
    print(f"    retract dim {nk} (parent {mod['N']}, integrated pairs {mod['nint']}); "
          f"|S_n| = " + ", ".join(f"{n}:{Sn[n].maxabs():.2e}" for n in sorted(Sn)))
    report(f"C4-B1-nontrivial seed {seed}: transferred S_4 != 0 (l_3^tr != 0)",
           Sn[4].maxabs() > 1e-6, f"|S_4| = {Sn[4].maxabs():.2e}")
    tab = pair_table(Sn, P, nk, M_ORDER + 2)
    r1 = [rel(J(tab, m), scale_of(Sn, P, m)) for m in range(M_ORDER + 1)]
    report(f"C4-B1 seed {seed}: untruncated [g^m](S,S)=0, m<= {M_ORDER}",
           max(r1) < TOL, "rel = " + ", ".join(f"{x:.1e}" for x in r1))
    # ---- B2 truncation lemma
    for k in (2, 3):
        keep = lambda a, b, k=k: a <= k + 2 and b <= k + 2  # noqa: E731
        rk = [rel(J(tab, m, keep), scale_of(Sn, P, m)) for m in range(k + 1)]
        report(f"C4-B2-vanish k={k} seed {seed}: [g^m](S^(k),S^(k))=0 for m<=k",
               max(rk) < TOL, "rel = " + ", ".join(f"{x:.1e}" for x in rk))
        lhs = J(tab, k + 1, keep)
        rhs = (tab[(2, k + 3)] + tab[(k + 3, 2)]).scale(-1.0)
        sc = scale_of(Sn, P, k + 1)
        report(f"C4-B2-rem k={k} seed {seed}: [g^(k+1)](S^(k),S^(k)) = -2(S_2,S_(k+3))",
               rel(lhs + rhs.scale(-1.0), sc) < TOL,
               f"|remainder| rel = {rel(lhs, sc):.2e}, mismatch = "
               f"{rel(lhs + rhs.scale(-1.0), sc):.1e}")
        if Sn[k + 3].maxabs() > 1e-12:
            report(f"C4-B2-rem-nonzero k={k} seed {seed}: remainder != 0 (S_(k+3) != 0)",
                   rel(lhs, sc) > 1e-6, f"rel {rel(lhs, sc):.2e}")
            # falsifier of the lemma's coefficient: -1 x (S_2,S_{k+3}) must fail
            wrong = rhs.scale(0.5)
            report(f"C4-B2-rem-break k={k} seed {seed}: coefficient -1 instead of -2 "
                   "fails", rel(lhs + wrong.scale(-1.0), sc) > 1e-6)
        else:
            print(f"    [n/a] k={k} seed {seed}: transferred tower terminates "
                  f"(S_{k + 3} = 0): truncation exact, remainder 0 as predicted")
    # ---- break legs on the truncated k=3 action (must fail at order <= k)
    def trunc_J(Sb: dict, m: int) -> float:
        tb = pair_table(Sb, P, nk, 5)
        return rel(J(tb, m, lambda a, b: a <= 5 and b <= 5), scale_of(Sb, P, m))

    Sb = dict(Sn)
    Sb[4] = Sn[4].scale(-1.0)
    x = trunc_J(Sb, 2)
    report(f"C4-break-sign seed {seed}: S_4 -> -S_4 fails at g^2", x > 1e-6, f"rel {x:.2e}")
    Sb = dict(Sn)
    Sb[4] = GP()
    x = trunc_J(Sb, 2)
    report(f"C4-break-l3 seed {seed}: S_4 -> 0 (l_3^tr -> 0) fails at g^2 (Jacobiator)",
           x > 1e-6, f"rel {x:.2e}")
    Sb = dict(Sn)
    anti = {a for a in range(nk) if mod["kdeg"][a] >= 2}
    Sb[3] = GP({k_: c for k_, c in Sn[3].t.items()
                if sum(1 for a in k_[1] + k_[2] if a in anti) != 1})
    x = trunc_J(Sb, 1)
    report(f"C4-break-antifield seed {seed}: terms linear in antifields dropped from S_3 "
           "fail at g^1",
           x > 1e-6, f"rel {x:.2e}")
    # antifield number two: drop the monomials with exactly two antifield coordinates
    # from S_4 (the transferred l_3 generates them: the open-algebra Psi+Psi+cc type
    # terms, 056 C3.3); fall back to S_5 if S_4 has none. Must fail where S_n enters.
    def n_anti(k_: tuple) -> int:
        return sum(1 for a in k_[1] + k_[2] if a in anti)

    done2 = False
    for n2 in (4, 5):
        quad = [k_ for k_ in Sn[n2].t if n_anti(k_) == 2 and abs(Sn[n2].t[k_]) > 1e-12]
        if not quad:
            continue
        Sb = dict(Sn)
        Sb[n2] = GP({k_: c for k_, c in Sn[n2].t.items() if n_anti(k_) != 2})
        x = trunc_J(Sb, n2 - 2)
        report(f"C4-break-antifield2 seed {seed}: {len(quad)} terms quadratic in "
               f"antifields dropped from S_{n2} fail at g^{n2 - 2}",
               x > 1e-6, f"rel {x:.2e}")
        done2 = True
        break
    if not done2:
        print(f"    [n/a] break-antifield2 seed {seed}: S_4, S_5 have no terms quadratic "
              "in antifields")
    rng = np.random.default_rng(seed + 1000)
    Sb = dict(Sn)
    Sb[4] = GP({k_: rng.standard_normal() * Sn[4].maxabs() for k_ in Sn[4].t})
    x = trunc_J(Sb, 2)
    report(f"C4-control seed {seed}: random non-L_infty quartic on S_4's support fails "
           "at g^2", x > 1e-6, f"rel {x:.2e}")
    # ---- B3 contractible pair: add Yh (even) and Yh+ (odd), 2 of each
    ny = 2
    GP.par = GP.par[:nk] + [0] * ny + [1] * ny
    pY = rng.standard_normal((ny, ny))
    pY = pY + pY.T
    PY = np.zeros((nk + 2 * ny, nk + 2 * ny))
    PY[:nk, :nk] = P
    for i in range(ny):  # C2: P^{Y Y+} = 1, P^{Y+ Y} = -1
        PY[nk + i, nk + ny + i] = 1.0
        PY[nk + ny + i, nk + i] = -1.0
    Ypair = GP()
    for i in range(ny):
        for j in range(ny):
            Ypair = Ypair + (GP.var(nk + i) * GP.var(nk + j)).scale(-pY[i, j] / 24.0)
    for k in (2, 3):
        Sk = GP()
        for n in range(2, k + 3):
            Sk = Sk + Sn[n].gshift(n - 2)
        SBV = Sk + Ypair.gshift(2)
        d = antibracket(SBV, SBV, PY, nk + 2 * ny) + antibracket(Sk, Sk, PY, nk + 2 * ny).scale(-1.0)
        sc = max(antibracket(Sk, Sk, PY, nk + 2 * ny).maxabs(), 1.0)
        report(f"C4-B3 k={k} seed {seed}: (S_BV,S_BV) = (S^(k),S^(k)) with the (Yh,Yh+) pair",
               d.maxabs() / sc < TOL, f"mismatch {d.maxabs() / sc:.1e}")
        odd_psi = next(a for a in range(nk) if GP.par[a] == 1)
        bad = SBV + (GP.var(nk + ny) * GP.var(odd_psi)).gshift(2)
        d = antibracket(bad, bad, PY, nk + 2 * ny) + antibracket(Sk, Sk, PY, nk + 2 * ny).scale(-1.0)
        report(f"C4-B3-break k={k} seed {seed}: a psi-dependent Yh+ term spoils it",
               d.maxabs() / sc > 1e-6, f"mismatch {d.maxabs() / sc:.1e}")


if __name__ == "__main__":
    runs = [(11, [0, 1, 2], (-1, 3)), (12, [0, 1, 2], (-1, 3)), (13, [0, 1, 2], (-1, 3)),
            (16, [0, 1, 2], (-1, 3, 0, 2))]
    for seed, w, cut in runs:
        one_seed(seed, w, cut)
    ntot = sum(tally.values())
    print(f"\nchecks: {ntot} total = {tally['independent']} independent + "
          f"{tally['falsifier']} falsifiers of B1 (break legs) + "
          f"{tally['bookkeeping']} bookkeeping (B2, B3 and their break legs)")
    print(f"SUMMARY: {len(failures)} failure(s)" + (f": {failures}" if failures else ""))
    sys.exit(1 if failures else 0)
