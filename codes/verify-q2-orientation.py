"""
Verification of derivation record 042 (Q2: orientation of the off-shell measure).

What is verified
----------------
- (4.2) `Q2-N1-ETA-LITERAL`: the antiholomorphic contour integral
  oint dw̄/(2 pi i) w̄^{-n-2} over an *anticlockwise circle in w*, with dw̄ the honest
  differential of w̄, equals -delta_{n,-1}; the holomorphic one equals +delta_{n,-1}.
  Numerical quadrature, several radii and several n. This is the value eta = -1 of the
  record, i.e. bar{B} = -bar b_{-1}.
- (4.3)-(4.4) `Q2-N2-B-DECOMPOSITION`, `Q2-N3-BXBY`: with
  B_x = b_{-1} + eta bar b_{-1},  B_y = i (b_{-1} - eta bar b_{-1}),
  the product is B_x B_y = -2 i eta b_{-1} bar b_{-1}, for both eta = +1 and eta = -1.
  Checked in an explicit finite-dimensional (Jordan-Wigner) representation of the ghost
  zero-mode algebra {b_m, c_n} = delta_{m+n,0}, not by re-running the record's algebra.
- (4.5) `Q2-N4-GHOST-STRIP`: b_{-1} bar b_{-1} c_1 bar c_1 |0> = -|0>.
- (4.6)-(4.7) `Q2-N4B-ONSHELL-FACTOR`: <B_x B_y ...> = 2 i eta <... V_4>, hence
  int omega_2 = (kappa i eta / 2 pi) A^FP_{0,4}  (using d^2 z = 2 dx dy, Erbin
  `bos_path_integral_closed_complex.tex` l. 124-126).
- (5.2) `Q2-N5-PURE-POWER`: for N = 5 (two independent puncture moduli) the factor is the
  pure square (2 i eta)^2, with no extra sign from Grassmann reordering; the two B-pairs
  commute. Four-mode representation.
- (5.3) `Q2-REALITY`: kappa i eta is real iff kappa = ±i; the four readings of the record's
  table give chi = kappa i eta = ±1 as tabulated.
- `Q2-TABLE`: the four (prefactor, contour-convention) readings and their chi, including
  the statement that book+literal and BZ+Res give the same chi.

What is NOT verified
--------------------
- The *value* of chi (node N6 of the record). The on-shell anchor fixes |chi| = 1 and the
  reality of chi, not its sign; the sign is inherited from SL(2,C) R37 (039 §6-§7) and is
  not re-derived, here or anywhere in this script.
- Anything about genus > 0, non-trivial local coordinates, or off-shell external states.

References
----------
- Erbin, H. (2023), *String Field Theory: A Modern Introduction*, arXiv:2301.01686,
  eqs. `bos:eq:B-form-V`, `bos:eq:beltrami-form`, `bos:eq:omega-p`.
- Belopolsky, A. & Zwiebach, B., eq. 4.10 (transcription only; no copy consulted).

"""

from __future__ import annotations

import sys

import numpy as np

SEED = 20260922
rng = np.random.default_rng(SEED)

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print a labelled PASS/FAIL check."""
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)
    return ok


# --------------------------------------------------------------------------- #
# Fermionic (Jordan-Wigner) representation of the ghost modes
# --------------------------------------------------------------------------- #

A = np.array([[0.0, 1.0], [0.0, 0.0]])  # annihilation: a|1> = |0>
Z = np.diag([1.0, -1.0])
I2 = np.eye(2)


def jw_modes(n_modes: int) -> list[np.ndarray]:
    """
    Jordan-Wigner annihilation operators for n_modes fermionic modes.

    Args:
        n_modes: number of modes.

    Returns:
        list: a_k as dense matrices, satisfying {a_j, a_k^dag} = delta_{jk} and
        {a_j, a_k} = 0.

    """
    ops = []
    for k in range(n_modes):
        factors = [Z] * k + [A] + [I2] * (n_modes - k - 1)
        m = factors[0]
        for f in factors[1:]:
            m = np.kron(m, f)
        ops.append(m)
    return ops


def anticomm(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Anticommutator x y + y x."""
    return x @ y + y @ x


# Two modes per puncture: (b_{-1}, c_1) and (bar b_{-1}, bar c_1).
a1, a2 = jw_modes(2)
b, bbar = a1, a2  # b_{-1}, bar b_{-1}
c, cbar = a1.T, a2.T  # c_1,   bar c_1
dim2 = b.shape[0]
vac2 = np.zeros(dim2)
vac2[0] = 1.0  # |0>: annihilated by b and bbar

ok = (
    np.allclose(anticomm(b, c), np.eye(dim2))
    and np.allclose(anticomm(bbar, cbar), np.eye(dim2))
    and np.allclose(anticomm(b, cbar), 0)
    and np.allclose(anticomm(b, bbar), 0)
    and np.allclose(b @ vac2, 0)
    and np.allclose(bbar @ vac2, 0)
)
check("Q2-REP-ALGEBRA", ok, "{b_m,c_n}=delta, all other (anti)commutators vanish")


# --------------------------------------------------------------------------- #
# (4.2) eta from the literal anticlockwise contour
# --------------------------------------------------------------------------- #


def contour_holo(n: int, radius: float, npts: int = 20000) -> complex:
    """Contour integral dw/(2 pi i) w^{-n-2} on an anticlockwise circle |w| = radius."""
    th = np.linspace(0.0, 2.0 * np.pi, npts, endpoint=False)
    w = radius * np.exp(1j * th)
    dw = 1j * w * (2.0 * np.pi / npts)
    return complex(np.sum(dw * w ** (-n - 2)) / (2.0 * np.pi * 1j))


def contour_antiholo(n: int, radius: float, npts: int = 20000) -> complex:
    """Contour integral dw̄/(2 pi i) w̄^{-n-2} on the *same* anticlockwise circle in w."""
    th = np.linspace(0.0, 2.0 * np.pi, npts, endpoint=False)
    w = radius * np.exp(1j * th)
    wb = np.conj(w)
    dwb = -1j * wb * (2.0 * np.pi / npts)
    return complex(np.sum(dwb * wb ** (-n - 2)) / (2.0 * np.pi * 1j))


radii = [0.37, 1.0, 2.9] + list(rng.uniform(0.5, 3.0, size=2))
ns = [-3, -2, -1, 0, 1]
holo_ok = all(
    abs(contour_holo(n, r) - (1.0 if n == -1 else 0.0)) < 1e-9
    for n in ns
    for r in radii
)
anti_ok = all(
    abs(contour_antiholo(n, r) - (-1.0 if n == -1 else 0.0)) < 1e-9
    for n in ns
    for r in radii
)
check(
    "Q2-N1-ETA-LITERAL",
    holo_ok and anti_ok,
    f"holo = +delta, antiholo = -delta over n in {ns}, {len(radii)} radii ⇒ eta = -1",
)

# Break leg: if eta were +1 the antiholomorphic integral would be +delta_{n,-1}.
check(
    "Q2-N1-BREAKLEG",
    abs(contour_antiholo(-1, 1.0) - (+1.0)) > 0.5,
    "check would FAIL if the literal integral gave +1 (it gives -1)",
)


# --------------------------------------------------------------------------- #
# (4.3)-(4.4) B_x B_y = -2 i eta b_{-1} bar b_{-1}
# --------------------------------------------------------------------------- #


def bx_by(eta: int) -> tuple[np.ndarray, np.ndarray]:
    """B_x and B_y of eq. (4.3) for the modulus z_4 = x + i y."""
    bx = b + eta * bbar
    by = 1j * (b - eta * bbar)
    return bx, by


decomp_ok = True
for eta in (+1, -1):
    bx, by = bx_by(eta)
    # B_x, B_y are Grassmann odd and square to zero (a structural consequence of (4.3)).
    decomp_ok &= np.allclose(bx @ bx, 0) and np.allclose(by @ by, 0)
check("Q2-N2-B-DECOMPOSITION", decomp_ok, "B_x^2 = B_y^2 = 0 for eta = ±1")

bxby_ok = True
for eta in (+1, -1):
    bx, by = bx_by(eta)
    bxby_ok &= np.allclose(bx @ by, -2j * eta * (b @ bbar))
check("Q2-N3-BXBY", bxby_ok, "B_x B_y = -2 i eta b_{-1} bar b_{-1}, eta = ±1")

# Break leg: the opposite sign must fail.
bx, by = bx_by(+1)
check(
    "Q2-N3-BREAKLEG",
    not np.allclose(bx @ by, +2j * (b @ bbar)),
    "check would FAIL for +2 i eta b bbar",
)

# Cross-check against 039's stated form 2 i bar b_{-1} b_{-1} at eta = +1.
check(
    "Q2-N3-VS-039",
    np.allclose(bx @ by, 2j * (bbar @ b)),
    "at eta=+1, B_xB_y = 2 i bar b_{-1} b_{-1} (039 §7.5 footnote form)",
)


# --------------------------------------------------------------------------- #
# (4.5) ghost stripping, and (4.6) the on-shell factor
# --------------------------------------------------------------------------- #

state = c @ cbar @ vac2  # c_1 bar c_1 |0>
stripped = b @ bbar @ state
check(
    "Q2-N4-GHOST-STRIP",
    np.allclose(stripped, -vac2),
    "b_{-1} bar b_{-1} c_1 bar c_1 |0> = -|0>",
)
check(
    "Q2-N4-BREAKLEG",
    not np.allclose(stripped, +vac2),
    "check would FAIL for the opposite sign",
)

onshell_ok = True
for eta in (+1, -1):
    bx, by = bx_by(eta)
    onshell_ok &= np.allclose(bx @ by @ state, 2j * eta * vac2)
check(
    "Q2-N4B-ONSHELL-FACTOR",
    onshell_ok,
    "B_x B_y (c_1 bar c_1 |0>) = 2 i eta |0>, eta = ±1",
)


# --------------------------------------------------------------------------- #
# (5.2) N = 5: the pure power, and commutativity of the pairs
# --------------------------------------------------------------------------- #

m = jw_modes(4)
b4, bb4, b5, bb5 = m
c4, cb4, c5, cb5 = (x.T for x in m)
dim4 = b4.shape[0]
vac4 = np.zeros(dim4)
vac4[0] = 1.0


def pair(eta: int, bh: np.ndarray, ba: np.ndarray) -> np.ndarray:
    """B_x B_y for one puncture, eq. (4.3)-(4.4), in the four-mode representation."""
    bx = bh + eta * ba
    by = 1j * (bh - eta * ba)
    return bx @ by


state5 = c4 @ cb4 @ c5 @ cb5 @ vac4
power_ok = True
comm_ok = True
for eta in (+1, -1):
    p4 = pair(eta, b4, bb4)
    p5 = pair(eta, b5, bb5)
    power_ok &= np.allclose(p4 @ p5 @ state5, (2j * eta) ** 2 * vac4)
    comm_ok &= np.allclose(p4 @ p5, p5 @ p4)
check(
    "Q2-N5-PURE-POWER",
    power_ok,
    "(B_x4 B_y4)(B_x5 B_y5) |c c̄ c c̄> = (2 i eta)^2 |0>, no extra sign",
)
check("Q2-N5-PAIRS-COMMUTE", comm_ok, "the two B-pairs commute (both Grassmann even)")

# Break leg: an odd number of extra transpositions would flip the N=5 sign.
check(
    "Q2-N5-BREAKLEG",
    not np.allclose(pair(1, b4, bb4) @ pair(1, b5, bb5) @ state5, -((2j) ** 2) * vac4),
    "check would FAIL for an extra (-1) at N = 5",
)


# --------------------------------------------------------------------------- #
# (5.3) reality, and the table of §4
# --------------------------------------------------------------------------- #

# The prefactor per complex modulus is kappa/(2 pi); the on-shell reduction (4.7) gives
# the real ratio chi = kappa i eta. Scan generic phases: only kappa = ±i is admissible.
phases = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, size=200))
bad = [p for p in phases if abs((p * 1j * 1).imag) < 1e-12]
check(
    "Q2-REALITY",
    len(bad) == 0 and abs((1j * 1j * 1).imag) < 1e-15 and abs((-1j * 1j).imag) < 1e-15,
    "kappa i eta real ⇒ kappa = ±i (200 seeded generic phases all excluded)",
)

table = {
    ("BZ", "literal"): (1j, -1),
    ("BZ", "res"): (1j, +1),
    ("book", "literal"): (-1j, -1),
    ("book", "res"): (-1j, +1),
}
chis = {k: (v[0] * 1j * v[1]).real for k, v in table.items()}
check(
    "Q2-TABLE",
    np.isclose(chis[("BZ", "literal")], +1)
    and np.isclose(chis[("BZ", "res")], -1)
    and np.isclose(chis[("book", "literal")], -1)
    and np.isclose(chis[("book", "res")], +1),
    f"chi values {chis}",
)
check(
    "Q2-NO-CONFLICT",
    np.isclose(chis[("book", "literal")], chis[("BZ", "res")]),
    "book read with its own contour rule and BZ read with 039's O3 give the same chi",
)


# --------------------------------------------------------------------------- #

print(f"\nseed = {SEED}")
if FAILURES:
    print(f"SUMMARY: {len(FAILURES)} FAIL — {', '.join(FAILURES)}")
    sys.exit(1)
print("SUMMARY: all checks PASS")
