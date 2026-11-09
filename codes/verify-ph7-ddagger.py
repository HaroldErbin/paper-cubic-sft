"""
Verify PH7: the reality conjugation squares to +1 on Grassmann-odd states.

Record: agent/derivations/028-reality-tower.md, addendum 2026-09-26 (PH7).

Setting. Truncated closed-string ghost Fock space built on the SL(2,C)
vacuum |0> by the six creation modes c_1, c_0, c_{-1}, cb_1, cb_0, cb_{-1};
their conjugates b_{-1}, b_0, b_1 (and barred) are the annihilators,
{b_m, c_n} = delta_{m+n,0}. Jordan-Wigner matrices on the 2^6 = 64-dim space.
Bras are row vectors; the out-vacuum <0| is kappa * e_full^T.

Conventions (Erbin 2023, live LaTeX commit 1dbb7217; Zwiebach 1993,
hep-th/9206084):
- hc of states: (lam A_1...A_n|0>)^hc = lam^* <0| A_n^dag ... A_1^dag with
  c_n^dag = c_{-n}, b_n^dag = b_{-n} (formulas.tex l.193; Zwiebach (2.33)-(2.34)).
- BPZ of states: (lam A_1...A_n|0>)^t = lam <0| A_1^t ... A_n^t (order kept);
  closed string I^+: c_n^t = -c_{-n}, b_n^t = b_{-n} (bos_worldsheet_cft.tex
  l.1159-1184); I^- variant c_n^t = (-1)^(n-1) c_{-n}, b_n^t = (-1)^n b_{-n}
  (conventions ledger C1(ii)). Both from phi_n^t = (-1)^h (+-1)^n phi_{-n}.
- Normalisation <0|c_{-1} cb_{-1} c_0 cb_0 c_1 cb_1|0> = -1
  (bos:eq:ws-closed-vacuum-normalization).
- ddagger(v) := eta * bpz^{-1}(hc(v)), eta = +1 (plain) or -1 (Zwiebach (3.6)).
  Matrix form: hc(v) = conj(v) @ G, bpz(v) = v @ P, ddagger(v) = eta K conj(v)
  with K = (P^T)^{-1} G^T; ddagger^2 = K conj(K).

Verified (named after the addendum's labels P.x):
- N1, N2: the -1/2 normalisation in the c_0^pm form (independent path from
  the c_0 cb_0 form) and the anti-hermiticity (A,B)^* = -(B,A) (Zwiebach 2.37).
- C1: BPZ mode tables = general formula (transcription check).
- H1, B1: the word rules are consistent with the Clifford algebra on all
  twelve modes (hc ungraded anti-automorphism, BPZ graded anti-automorphism,
  equal to the order-kept rule on creation words).
- P7.1-P7.6: ddagger on the even control alpha c_1 cb_1|0> and on the odd state
  beta c_0^+ c_1 cb_1|0>, complex coefficients; ddagger^2 = 1 exhaustively on
  the 64-dim space for I^+ and I^-; K diagonal with the predicted signs;
  I^+ / I^- agreement on level-matched states; kappa-independence.
- R1 (positive checks, not a break leg): order-reversing BPZ changes ddagger by
  (-1)^(k(k-1)/2) per k-mode word, ddagger^2 does not. Its break leg is
  break-B1-order-reversing-bpz.
- Gr1, Gr2: Grassmann-coefficient layer (two extra odd generators th, thb):
  involutive coefficient conjugation gives ddagger^2 = 1; the graded
  convention th^{**} = -th gives ddagger^2 = (-1)^{|coefficient|} (break leg).
- S1, S2: omega_1(A,B) = <bpz A| c_0^- |B> reproduces ledger C1 (-1/2) and its
  equivariance sign under ddagger (-1 on every pair for constant eta, +1 for
  ddagger' = (-1)^(N_gh+1) bpz^{-1} o hc); S3: Zwiebach's constant sign eta = -1
  on the Grassmann-even total field induces ddagger' on worldsheet components.

Not verified: matter sector, momentum, higher ghost oscillators (the
truncation keeps n in {-1, 0, 1}); the argument of the addendum (P.3) covers
them because star conjugation maps every mode to a real multiple of itself
(up to p -> -p), which the truncation illustrates but does not prove.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np

SEED = 20260926
TOL = 1e-12

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, info: str = "") -> bool:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, bool(ok), info))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {info}")
    return bool(ok)


# ---------------------------------------------------------------------------
# Fock space and modes
# ---------------------------------------------------------------------------

GHOST_CREATION = [
    ("c", 1, 0),
    ("c", 0, 0),
    ("c", -1, 0),
    ("c", 1, 1),
    ("c", 0, 1),
    ("c", -1, 1),
]
GRASSMANN = [("th", 0, 0), ("th", 0, 1)]  # coefficient generators th, thb


class Fock:
    """Jordan-Wigner Fock space on a list of creation labels."""

    def __init__(self, creation: list[tuple[str, int, int]]) -> None:
        """Build creation matrices, vacua, canonical words and their signs."""
        self.labels = creation
        self.n = len(creation)
        self.dim = 2**self.n
        self.index = {lab: i for i, lab in enumerate(creation)}
        self.adag = []
        for i in range(self.n):
            m = np.zeros((self.dim, self.dim))
            for s in range(self.dim):
                if not (s >> i) & 1:
                    sign = (-1) ** bin(s & ((1 << i) - 1)).count("1")
                    m[s | (1 << i), s] = sign
            self.adag.append(m)
        self.e0 = np.zeros(self.dim)
        self.e0[0] = 1.0
        self.efull = np.zeros(self.dim)
        self.efull[-1] = 1.0
        self.parity = np.array([bin(s).count("1") % 2 for s in range(self.dim)])
        self.words = [
            [creation[i] for i in range(self.n) if (s >> i) & 1]
            for s in range(self.dim)
        ]
        self.sigma = np.array(
            [(self.word(self.words[s]) @ self.e0)[s] for s in range(self.dim)]
        )
        assert np.allclose(np.abs(self.sigma), 1.0)

    def mat(self, lab: tuple[str, int, int]) -> np.ndarray:
        """Matrix of a mode: c_n, th = creation; b_m = annihilator of c_{-m}."""
        kind, n, bar = lab
        if kind in ("c", "th"):
            return self.adag[self.index[lab]]
        if kind == "b":
            return self.adag[self.index[("c", -n, bar)]].T
        raise ValueError(lab)

    def word(self, word: list[tuple[str, int, int]]) -> np.ndarray:
        """Ordered product of mode matrices (leftmost acts last)."""
        out = np.eye(self.dim)
        for lab in word:
            out = out @ self.mat(lab)
        return out

    def ket(self, word: list, coef: complex = 1.0) -> np.ndarray:
        """State coef * word |0>."""
        return coef * (self.word(word) @ self.e0).astype(complex)

    def ghost_number(self, s: int) -> int:
        """Ghost number of a basis monomial (only c-modes: +1 each)."""
        return sum(1 for lab in self.words[s] if lab[0] == "c")

    def level_matched(self, s: int) -> bool:
        """L_0 = bar L_0 for a monomial: c_n carries weight -n."""
        w = self.words[s]
        return sum(-lab[1] for lab in w if lab[0] == "c" and lab[2] == 0) == sum(
            -lab[1] for lab in w if lab[0] == "c" and lab[2] == 1
        )


def ghost_modes() -> list[tuple[str, int, int]]:
    """All twelve ghost modes b_n, c_n, bar b_n, bar c_n with n in {-1,0,1}."""
    return [(k, n, bar) for k in ("b", "c") for n in (-1, 0, 1) for bar in (0, 1)]


# ---------------------------------------------------------------------------
# Conjugation rules on modes: label -> (coefficient, image label)
# ---------------------------------------------------------------------------


def rule_dag(lab, graded_theta: bool = False):
    """Hermitian conjugation of modes: c_n^dag = c_{-n}, b_n^dag = b_{-n}; th <-> thb."""
    kind, n, bar = lab
    if kind == "th":
        if bar == 0:
            return 1.0, ("th", 0, 1)
        return (-1.0 if graded_theta else 1.0), ("th", 0, 0)
    return 1.0, (kind, -n, bar)


def bpz_general(lab, sign: int):
    """phi_n^t = (-1)^h (sign)^n phi_{-n}, h_c = -1, h_b = 2 (cft:eq:chiral-modes-bpz)."""
    kind, n, bar = lab
    if kind == "th":
        return 1.0, lab  # c-numbers untouched by BPZ
    h = -1 if kind == "c" else 2
    return float((-1) ** (h % 2) * sign ** (n % 2)), (kind, -n, bar)


def rule_bpz_plus(lab):
    """Book closed-string table (I^+): c_n^t = -c_{-n}, b_n^t = b_{-n}."""
    kind, n, bar = lab
    if kind == "th":
        return 1.0, lab
    return (-1.0 if kind == "c" else 1.0), (kind, -n, bar)


def rule_bpz_minus(lab):
    """Ledger C1(ii) (I^-): c_n^t = (-1)^(n-1) c_{-n}, b_n^t = (-1)^n b_{-n}."""
    kind, n, bar = lab
    if kind == "th":
        return 1.0, lab
    if kind == "c":
        return (1.0 if (n - 1) % 2 == 0 else -1.0), (kind, -n, bar)
    return (1.0 if n % 2 == 0 else -1.0), (kind, -n, bar)


# ---------------------------------------------------------------------------
# Conjugation matrices
# ---------------------------------------------------------------------------


def bra_word(F: Fock, bra0: np.ndarray, word, rule, reverse: bool) -> np.ndarray:
    """Row vector <0| R(O_1) R(O_2) ... (or reversed order) for the image modes."""
    seq = list(reversed(word)) if reverse else list(word)
    row = bra0.astype(complex)
    for lab in seq:
        c, img = rule(lab)
        row = c * (row @ F.mat(img))
    return row


def hc_matrix(F: Fock, bra0, rule=rule_dag, graded: bool = False) -> np.ndarray:
    """Rows = hc of basis kets: sigma_s <0| O_k^dag ... O_1^dag (reversal)."""
    rows = []
    for s in range(F.dim):
        w = F.words[s]
        k = len(w)
        extra = (-1) ** (k * (k - 1) // 2) if graded else 1
        rows.append(F.sigma[s] * extra * bra_word(F, bra0, w, rule, reverse=True))
    return np.array(rows)


def bpz_matrix(F: Fock, bra0, rule, reverse: bool = False) -> np.ndarray:
    """Rows = BPZ of basis kets: sigma_s <0| O_1^t ... O_k^t (order kept)."""
    return np.array(
        [
            F.sigma[s] * bra_word(F, bra0, F.words[s], rule, reverse=reverse)
            for s in range(F.dim)
        ]
    )


def ddagger_K(G: np.ndarray, P: np.ndarray) -> np.ndarray:
    """K with ddagger(v) = eta K conj(v): solves bpz(v^dd) = eta hc(v)."""
    return np.linalg.solve(P.T, G.T)


def apply_dd(K: np.ndarray, v: np.ndarray, eta: int = 1) -> np.ndarray:
    """ddagger(v) = eta K conj(v) (antilinear)."""
    return eta * (K @ np.conj(v))


def main() -> int:
    """Run all checks; return process exit code."""
    rng = np.random.default_rng(SEED)
    print(f"seed = {SEED}")
    F = Fock(GHOST_CREATION)

    # --- out-vacuum: kappa fixed from the c_0 cb_0 form (book normalisation) ---
    X0 = [
        ("c", -1, 0),
        ("c", -1, 1),
        ("c", 0, 0),
        ("c", 0, 1),
        ("c", 1, 0),
        ("c", 1, 1),
    ]
    kappa = -1.0 / (F.efull @ F.word(X0) @ F.e0)
    bra0 = kappa * F.efull
    c0p = 0.5 * (F.mat(("c", 0, 0)) + F.mat(("c", 0, 1)))
    c0m = 0.5 * (F.mat(("c", 0, 0)) - F.mat(("c", 0, 1)))
    cm1, cbm1, c1, cb1 = (
        F.mat(("c", -1, 0)),
        F.mat(("c", -1, 1)),
        F.mat(("c", 1, 0)),
        F.mat(("c", 1, 1)),
    )

    # N1: -1/2 in the c_0^- c_0^+ ordering, via the c_0^pm definitions (independent path)
    val = bra0 @ cm1 @ cbm1 @ c0m @ c0p @ c1 @ cb1 @ F.e0
    check(
        "N1-normalisation-c0pm",
        abs(val + 0.5) < TOL,
        f"<c-1 cb-1 c0- c0+ c1 cb1> = {val:+.3f} (target -1/2)",
    )
    val_b = bra0 @ cm1 @ cbm1 @ c0p @ c0m @ c1 @ cb1 @ F.e0
    check(
        "break-N1-order-c0p-c0m",
        abs(val_b + 0.5) > 0.1,
        f"c0+ c0- ordering gives {val_b:+.3f} != -1/2",
    )
    # out-vacuum annihilated by b_n (n <= 1) acting to the left; |0> by b_n (n >= -1)
    ok = all(
        np.allclose(bra0 @ F.mat(("b", n, bar)), 0)
        for n in (-1, 0, 1)
        for bar in (0, 1)
    )
    ok &= all(
        np.allclose(F.mat(("b", n, bar)) @ F.e0, 0)
        for n in (-1, 0, 1)
        for bar in (0, 1)
    )
    check("N0-vacua", ok, "<0| b_n = 0 and b_n |0> = 0 for n in {-1,0,1}")

    # C1: tables = general formula phi_n^t = (-1)^h (+-1)^n phi_{-n}
    ok = all(rule_bpz_plus(m) == bpz_general(m, +1) for m in ghost_modes())
    ok &= all(rule_bpz_minus(m) == bpz_general(m, -1) for m in ghost_modes())
    check(
        "C1-mode-tables",
        ok,
        "I^+ table (book closed) and I^- table (ledger C1(ii)) match the general formula",
    )

    G = hc_matrix(F, bra0)
    # N2: (A,B)^* = -(B,A)  <=>  G^H = -G  (Zwiebach 2.37; book formulas.tex l.202)
    check(
        "N2-hc-antihermitian", np.allclose(G.conj().T, -G), "G^H = -G: (A,B)^* = -(B,A)"
    )
    G_i = hc_matrix(F, 1j * bra0)
    check(
        "break-N2-with-i",
        np.allclose(G_i.conj().T, G_i),
        "with an i in the normalisation G^H = +G",
    )

    # H1: hc rule (built on creation words) is the ungraded anti-automorphism on all 12 modes
    def hc_ok(Gm: np.ndarray) -> bool:
        return all(
            np.allclose(
                F.mat(m).conj().T @ Gm, Gm @ (rule_dag(m)[0] * F.mat(rule_dag(m)[1]))
            )
            for m in ghost_modes()
        )

    check(
        "H1-hc-intertwines-all-modes",
        hc_ok(G),
        "hc(Xv) = hc(v) X^dag for all 12 modes incl. b_n",
    )
    check(
        "break-H1-graded-hc",
        not hc_ok(hc_matrix(F, bra0, graded=True)),
        "graded-reversal hc fails the Clifford test",
    )

    # B1: BPZ order-kept on creation words = graded anti-automorphism on all 12 modes
    D = np.diag((-1.0) ** F.parity)

    def bpz_graded_ok(Pm: np.ndarray, rule) -> bool:
        return all(
            np.allclose(F.mat(m).T @ Pm, D @ Pm @ (rule(m)[0] * F.mat(rule(m)[1])))
            for m in ghost_modes()
        )

    def bpz_ungraded_ok(Pm: np.ndarray, rule) -> bool:
        return all(
            np.allclose(F.mat(m).T @ Pm, Pm @ (rule(m)[0] * F.mat(rule(m)[1])))
            for m in ghost_modes()
        )

    Pp = bpz_matrix(F, bra0, rule_bpz_plus)
    Pm_ = bpz_matrix(F, bra0, rule_bpz_minus)
    check(
        "B1-bpz-graded-antiautomorphism",
        bpz_graded_ok(Pp, rule_bpz_plus) and bpz_graded_ok(Pm_, rule_bpz_minus),
        "bpz(Xv) = (-1)^|v| bpz(v) X^t for all 12 modes, I^+ and I^-",
    )
    Prev = bpz_matrix(F, bra0, rule_bpz_plus, reverse=True)
    check(
        "break-B1-order-reversing-bpz",
        not bpz_graded_ok(Prev, rule_bpz_plus)
        and not bpz_ungraded_ok(Prev, rule_bpz_plus),
        "order-reversing BPZ is neither a graded nor an ungraded anti-automorphism",
    )

    Kp = ddagger_K(G, Pp)
    Km = ddagger_K(G, Pm_)

    # named states
    A1 = F.ket([("c", 1, 0), ("c", 1, 1)])
    B1 = (c0p @ c1 @ cb1 @ F.e0).astype(complex)
    alpha = complex(*rng.normal(size=2))
    beta = complex(*rng.normal(size=2))
    print(f"alpha = {alpha:.6f}, beta = {beta:.6f}")
    b0m = F.mat(("b", 0, 0)) - F.mat(("b", 0, 1))
    check(
        "P7.0-states-in-kernel-b0m",
        np.allclose(b0m @ A1, 0) and np.allclose(b0m @ B1, 0),
        "b_0^- A1 = b_0^- B1 = 0",
    )

    # P7.1 even control
    Ad = apply_dd(Kp, alpha * A1)
    Add = apply_dd(Kp, Ad)
    check(
        "P7.1-even-control",
        np.allclose(Ad, -np.conj(alpha) * A1) and np.allclose(Add, alpha * A1),
        "(alpha c1 cb1|0>)^dd = -alpha^* c1 cb1|0>, dd^2 = +1",
    )
    check(
        "break-P7.1-wrong-sign",
        not np.allclose(Ad, np.conj(alpha) * A1),
        "the value +alpha^* is rejected",
    )
    # P7.2 odd state
    Bd = apply_dd(Kp, beta * B1)
    Bdd = apply_dd(Kp, Bd)
    check(
        "P7.2-odd-state",
        np.allclose(Bd, np.conj(beta) * B1) and np.allclose(Bdd, beta * B1),
        "(beta c0+ c1 cb1|0>)^dd = +beta^* c0+ c1 cb1|0>, dd^2 = +1",
    )
    check(
        "break-P7.2-wrong-sign",
        not np.allclose(Bd, -np.conj(beta) * B1),
        "the value -beta^* is rejected",
    )
    for eta in (1, -1):
        ok = np.allclose(apply_dd(Kp, apply_dd(Kp, B1 * beta, eta), eta), beta * B1)
        ok &= np.allclose(apply_dd(Kp, apply_dd(Kp, A1 * alpha, eta), eta), alpha * A1)
        check(
            f"P7.2b-eta={eta:+d}", ok, "dd^2 = +1 on both states for this overall sign"
        )

    # P7.3 exhaustive involution, both BPZ conventions, both parity sectors
    eye = np.eye(F.dim)
    for name, K in (("I+", Kp), ("I-", Km)):
        ok = np.allclose(K @ K.conj(), eye)
        for par in (0, 1):
            for _ in range(5):
                v = (rng.normal(size=F.dim) + 1j * rng.normal(size=F.dim)) * (
                    F.parity == par
                )
                ok &= np.allclose(apply_dd(K, apply_dd(K, v)), v)
        check(
            f"P7.3-involution-exhaustive-{name}",
            ok,
            "K conj(K) = 1 on all 64 states; random complex even/odd vectors",
        )

    # P7.4 K diagonal with the predicted sign (-1)^{k(k-1)/2} prod(star coefficients)
    def star_coef(lab, rule_t) -> float:
        c1_, img1 = rule_dag(lab)
        c2_, img2 = rule_t(img1)
        assert img2 == lab
        return c1_ * c2_

    for name, K, rule_t in (("I+", Kp, rule_bpz_plus), ("I-", Km, rule_bpz_minus)):
        pred = np.array(
            [
                (-1) ** (len(F.words[s]) * (len(F.words[s]) - 1) // 2)
                * np.prod([star_coef(lab, rule_t) for lab in F.words[s]])
                for s in range(F.dim)
            ]
        )
        check(
            f"P7.4-diagonal-sign-{name}",
            np.allclose(K, np.diag(pred)),
            "K = diag((-1)^{k(k-1)/2} prod star-coef)",
        )

    # P7.5 I^+ vs I^-: same on level-matched states, differ elsewhere
    lm = [s for s in range(F.dim) if F.level_matched(s)]
    nlm = [s for s in range(F.dim) if not F.level_matched(s)]
    same = all(np.isclose(Kp[s, s], Km[s, s]) for s in lm)
    differ = any(not np.isclose(Kp[s, s], Km[s, s]) for s in nlm)
    check(
        "P7.5-Iplus-vs-Iminus",
        same and differ,
        f"agree on {len(lm)} level-matched monomials, differ on some of {len(nlm)} others",
    )

    # P7.6 kappa independence (normalisation, incl. the 'no i' choice, does not enter dd)
    k2 = 3.7j
    K2 = ddagger_K(hc_matrix(F, k2 * bra0), bpz_matrix(F, k2 * bra0, rule_bpz_plus))
    check(
        "P7.6-kappa-independence",
        np.allclose(K2, Kp),
        "K unchanged under <0| -> 3.7i <0|",
    )

    # R1 positive checks (break leg: break-B1-order-reversing-bpz): order-reversing BPZ changes dd by (-1)^{k(k-1)/2}, not dd^2
    Krev = ddagger_K(G, Prev)
    rev_sign = np.array([(-1) ** (len(w) * (len(w) - 1) // 2) for w in F.words])
    check(
        "R1a-reversal-changes-dd",
        np.allclose(Krev, np.diag(rev_sign) @ Kp),
        "K_rev = diag((-1)^{k(k-1)/2}) K",
    )
    check(
        "R1b-B1-flips",
        np.allclose(apply_dd(Krev, B1), -B1) and np.allclose(apply_dd(Krev, A1), A1),
        "under reversal B1 becomes imaginary and A1 real",
    )
    check(
        "R1c-reversal-keeps-dd2",
        np.allclose(Krev @ Krev.conj(), eye),
        "dd_rev^2 = +1: the flip does not touch dd^2",
    )

    # Gr: Grassmann-coefficient layer, coefficients on the right (Zwiebach 3.18 placement)
    E = Fock(GHOST_CREATION + GRASSMANN)
    ebra = E.efull.copy()  # any nonzero normalisation (kappa independence)
    PE = bpz_matrix(E, ebra, rule_bpz_plus)
    B1t = (
        0.5
        * (E.mat(("c", 0, 0)) + E.mat(("c", 0, 1)))
        @ E.mat(("c", 1, 0))
        @ E.mat(("c", 1, 1))
        @ E.mat(("th", 0, 0))
        @ E.e0
    ).astype(complex)
    B1tb = (
        0.5
        * (E.mat(("c", 0, 0)) + E.mat(("c", 0, 1)))
        @ E.mat(("c", 1, 0))
        @ E.mat(("c", 1, 1))
        @ E.mat(("th", 0, 1))
        @ E.e0
    ).astype(complex)
    nth = np.array([sum(1 for lab in w if lab[0] == "th") for w in E.words])
    for graded in (False, True):
        GE = hc_matrix(
            E, ebra, rule=lambda lab, g=graded: rule_dag(lab, graded_theta=g)
        )
        KE = ddagger_K(GE, PE)
        KK = KE @ KE.conj()
        if not graded:
            ok = np.allclose(KK, np.eye(E.dim))
            ok &= np.allclose(apply_dd(KE, B1t), -B1tb)
            check(
                "Gr1-grassmann-standard",
                ok,
                "th^** = th: dd^2 = +1 on all 256 states; (B1 th)^dd = -B1 thb",
            )
            # (P.6): dd(W th|0>) = (-1)^k d_W W thb|0>, d_W = dd-eigenvalue of W|0>
            pred_ok = True
            for s_gh in range(F.dim):
                W = F.words[s_gh]
                lhs = apply_dd(KE, E.ket(W + [("th", 0, 0)]))
                rhs = (-1) ** len(W) * Kp[s_gh, s_gh].real * E.ket(W + [("th", 0, 1)])
                pred_ok &= np.allclose(lhs, rhs)
            check(
                "Gr1b-coefficient-sign-formula",
                pred_ok,
                "dd(W th|0>) = (-1)^k d_W W thb|0> on all 64 ghost words",
            )
        else:
            pred = np.where(nth == 1, -1.0, 1.0)
            ok = np.allclose(KK, np.diag(pred))
            ok &= np.allclose(apply_dd(KE, apply_dd(KE, B1t)), -B1t)
            check(
                "Gr2-grassmann-graded-break",
                ok,
                "th^** = -th: dd^2 = (-1)^{|coefficient|}; dd^2(B1 th) = -B1 th",
            )

    # S: pairing omega_1(A,B) = <bpz A| c_0^- |B> and its equivariance sign
    def omega(Pm, a, b):
        return (a @ Pm) @ c0m @ b

    wab, wba = omega(Pp, A1, B1), omega(Pp, B1, A1)
    check(
        "S1-omega1-ledger-C1",
        abs(wab + 0.5) < TOL and abs(wba + 0.5) < TOL,
        f"omega1(A1,B1) = {wab.real:+.3f}, omega1(B1,A1) = {wba.real:+.3f}",
    )
    sig = {}
    sig_p = {}
    Nop = np.array([F.ghost_number(s) for s in range(F.dim)])
    Kprime = np.diag((-1.0) ** (Nop + 1)) @ Kp
    for s, t in itertools.product(range(F.dim), repeat=2):
        a = np.zeros(F.dim, complex)
        b = np.zeros(F.dim, complex)
        a[s] = 1.0
        b[t] = 1.0
        w = omega(Pp, a, b)
        if abs(w) > 1e-9:
            key = (F.ghost_number(s), F.ghost_number(t))
            sig.setdefault(key, set()).add(
                round((omega(Pp, apply_dd(Kp, a), apply_dd(Kp, b)) / np.conj(w)).real)
            )
            sig_p.setdefault(key, set()).add(
                round(
                    (
                        omega(Pp, apply_dd(Kprime, a), apply_dd(Kprime, b)) / np.conj(w)
                    ).real
                )
            )
    check(
        "S2a-equivariance-sign-constant-eta",
        all(v == {-1} for v in sig.values()),
        f"omega1(A^dd,B^dd) = -omega1(A,B)^* on all (gA,gB): {dict(sorted(sig.items()))}",
    )
    check(
        "S2b-equivariance-sign-graded-eta",
        all(v == {1} for v in sig_p.values()),
        "with dd' = (-1)^(N_gh+1) dd: +1 on every pair",
    )
    check(
        "S2c-ddprime-involution", np.allclose(Kprime @ Kprime.conj(), eye), "dd'^2 = +1"
    )

    # S3: Zwiebach's constant eta = -1 on the Grassmann-EVEN total field induces dd'
    # on worldsheet components (odd states carry odd coefficients, placed right)
    GE0 = hc_matrix(E, ebra)
    KZ = ddagger_K(GE0, PE)  # eta applied below
    ok = True
    for s_gh in range(F.dim):
        W = F.words[s_gh]
        dprime = (-1.0) ** (F.ghost_number(s_gh) + 1) * Kp[s_gh, s_gh].real
        if len(W) % 2 == 0:  # even state, ordinary complex coefficient
            ok &= np.allclose(apply_dd(KZ, E.ket(W), eta=-1), dprime * E.ket(W))
        else:  # odd state, odd coefficient th -> th^dag = thb
            lhs = apply_dd(KZ, E.ket(W + [("th", 0, 0)]), eta=-1)
            ok &= np.allclose(lhs, dprime * E.ket(W + [("th", 0, 1)]))
    check(
        "S3-zwiebach-total-even-field-is-ddprime",
        ok,
        "-bpz^-1 hc on |phi> psi (total even) = (dd' |phi>) psi^dag for all 64 ghost words",
    )
    ok_b = all(
        np.allclose(
            apply_dd(KZ, E.ket(F.words[s] + [("th", 0, 0)]), eta=-1),
            (-1.0) * Kp[s, s].real * E.ket(F.words[s] + [("th", 0, 1)]),
        )
        for s in range(F.dim)
        if len(F.words[s]) % 2 == 1
    )
    # Comment: dropping the odd-coefficient sign is Zwiebach's (3.18) sign for commuting
    # coefficients (gauge parameter Lambda, Lambda^{dd'} = -Lambda); the leg fails for odd
    # coefficients only, and is not wrong physics for commuting ones.
    check(
        "break-S3-ignore-coefficient-sign",
        not ok_b,
        "dropping the (-1)^k from moving the odd coefficient fails",
    )

    n_fail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"\nSUMMARY: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS (seed {SEED})")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
