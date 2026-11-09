"""
Paper figure fig:ws:region (sect. 6): the plumbing q-plane of the s-circle gluing.

Left panel of codes/plot-circle-gluing-covering.py (record 074, R80), redrawn alone
for the paper at beta = 3/2.

Geometry copied (not imported) from codes/plot-circle-gluing-covering.py:
Z(q) = (q + 4 beta^2)^2 / (16 beta^2 q) (eq:ws:cross-ratio), membership of
V_{0,4} = min(|q_t|, |q_u|) > 1, ray marching for sigma_V(theta), so that
R_V = {1 < |q| < e^{sigma_V(theta)}} (eq:ws:region).
Square point (eq:ws:square-point): q_sq = -4 beta^2 (sqrt 2 - 1)^2, checked to give Z = -1.

Drawn: unit disc (s-channel Feynman region), R_V, outer annulus
e^{sigma_V} <= |q| < 4 beta^2 (t- and u-channel regions), circle |q| = 4 beta^2 dashed
with the two fold arcs thick, q_sq on the ray theta = pi.

Output: paper/images/ws_q_plane.pdf.
Run: nice -n 19 .venv/bin/python codes/plot-ws-q-plane.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BETA = 1.5
B2 = BETA**2
LN_COLL = np.log(4 * B2)  # collision (fold) circle |q| = 4 beta^2

OUT = Path(__file__).resolve().parent / "output" / "figures"


# ---------------------------------------------------------------------------
# Geometry (copied from plot-circle-gluing-covering.py)
# ---------------------------------------------------------------------------
def z_of_q(q):
    """s-channel puncture location: Z = (q + 4 beta^2)^2 / (16 beta^2 q)."""
    return (q + 4 * B2) ** 2 / (16 * B2 * q)


def q_of_zs(zs):
    """Root of q^2 + (8 b^2 - 16 b^2 zs) q + 16 b^4 = 0 with |q| < 4 b^2."""
    b = 8 * B2 - 16 * B2 * zs
    disc = np.sqrt(b * b - 4 * 16 * B2**2 + 0j)
    r1 = (-b + disc) / 2
    r2 = (-b - disc) / 2
    return np.where(np.abs(r1) < np.abs(r2), r1, r2)


def min_tu(z):
    """min(|q_t|, |q_u|)."""
    qt = q_of_zs(z / (z - 1))
    qu = q_of_zs(1 - 1 / z)
    return np.minimum(np.abs(qt), np.abs(qu))


# ---------------------------------------------------------------------------
# Ray marching: sigma_V(theta), refined by bisection
# ---------------------------------------------------------------------------
n_theta, n_sigma = 720, 2000  # n_theta even: index n_theta // 2 is theta = pi
thetas = np.linspace(0, 2 * np.pi, n_theta, endpoint=False)
sigmas = np.linspace(1e-4, LN_COLL - 1e-4, n_sigma)
TH, SG = np.meshgrid(thetas, sigmas, indexing="ij")
inside = min_tu(z_of_q(np.exp(SG + 1j * TH))) > 1.0
prefix_len = np.argmin(inside, axis=1)
prefix_len = np.where(inside.all(axis=1), n_sigma, prefix_len)
at_cap = prefix_len == n_sigma
assert not np.array([inside[i, prefix_len[i] :].any() for i in range(n_theta)]).any(), (
    "re-entry: R_V not star-shaped"
)

lo = sigmas[np.clip(prefix_len - 1, 0, n_sigma - 1)]
hi = sigmas[np.clip(prefix_len, 0, n_sigma - 1)]
for _ in range(40):
    mid = 0.5 * (lo + hi)
    ok = min_tu(z_of_q(np.exp(mid + 1j * thetas))) > 1.0
    lo = np.where(ok, mid, lo)
    hi = np.where(ok, hi, mid)
sigma_V = np.where(at_cap, LN_COLL, 0.5 * (lo + hi))


def sigma_of_theta(th):
    """sigma_V at arbitrary theta, linear interpolation of the ray data (2 pi-periodic)."""
    return np.interp(
        np.mod(th, 2 * np.pi),
        np.append(thetas, 2 * np.pi),
        np.append(sigma_V, sigma_V[0]),
    )


# Fold-arc endpoints: scan a fine theta grid on [0, pi] just inside the fold circle.
th_f = np.linspace(0, np.pi, 400001)
ok_f = min_tu(z_of_q(np.exp((LN_COLL - 1e-6) + 1j * th_f))) > 1.0
idx = np.flatnonzero(ok_f)
th1_num, th2_num = th_f[idx[0]], th_f[idx[-1]]
sig_pi = float(sigma_V[n_theta // 2])

# Square point, eq:ws:square-point
Q_SQ = -4 * B2 * (np.sqrt(2) - 1) ** 2
z_sq = complex(z_of_q(Q_SQ + 0j))

print(f"sigma_V(pi) = {sig_pi:.6f}   ln(9/4) = {np.log(9 / 4):.6f}")
print(
    f"fold arc: cos theta_1 = {np.cos(th1_num):.5f}, cos theta_2 = {np.cos(th2_num):.5f}"
    f"  (7/25 = {7 / 25:.5f})"
)
print(f"q_square = {Q_SQ:.6f}   Z(q_square) = {z_sq:.6f}")
assert abs(sig_pi - np.log(9 / 4)) < 1e-6
assert abs(np.cos(th1_num) - 7 / 25) < 1e-4 and abs(np.cos(th2_num) + 7 / 25) < 1e-4
assert abs(z_sq + 1) < 1e-12
assert 1 < abs(Q_SQ) < np.exp(sig_pi)  # strictly inside R_V on theta = pi

# ---------------------------------------------------------------------------
# Figure (grayscale-readable: disc dark gray, R_V mid blue, annulus light gray)
# ---------------------------------------------------------------------------
C_BLUE, C_SKY, C_VERM = "#0072B2", "#56B4E9", "#D55E00"
C_DISC, C_ANN = "#9a9a9a", "#ececec"

plt.rcParams.update(
    {
        "font.size": 8,
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "font.serif": ["cmr10"],
        "axes.formatter.use_mathtext": True,
    }
)
fig, ax = plt.subplots(figsize=(3.3, 3.3), constrained_layout=True)

R = 4 * B2 * 1.12
th_fill = np.linspace(0, 2 * np.pi, 2001)
sV_fill = sigma_of_theta(th_fill)
xo, yo = np.exp(sV_fill) * np.cos(th_fill), np.exp(sV_fill) * np.sin(th_fill)
xi, yi = np.cos(th_fill), np.sin(th_fill)
xc, yc = 4 * B2 * np.cos(th_fill), 4 * B2 * np.sin(th_fill)

ax.fill(xc, yc, color=C_ANN, lw=0, zorder=0)  # outer annulus (under R_V)
ax.fill(
    np.concatenate([xo, xi[::-1]]),
    np.concatenate([yo, yi[::-1]]),
    color=C_SKY,
    alpha=0.65,
    lw=0,
    zorder=1,
)
ax.add_patch(plt.Circle((0, 0), 1, fc=C_DISC, ec="none", zorder=1))
ax.plot(xi, yi, color="k", lw=0.8, zorder=4)
ax.plot(xo, yo, color=C_BLUE, lw=1.1, zorder=4)
ax.plot(xc, yc, color="k", lw=0.8, ls=(0, (5, 3)), zorder=3)
for a, b in [(th1_num, th2_num), (-th2_num, -th1_num)]:
    t = np.linspace(a, b, 200)
    ax.plot(
        4 * B2 * np.cos(t),
        4 * B2 * np.sin(t),
        color=C_VERM,
        lw=3.0,
        zorder=6,
        solid_capstyle="butt",
    )

# square point on the ray theta = pi
ax.plot(Q_SQ, 0, "s", ms=4.5, mfc="white", mec="k", mew=0.9, zorder=7)

box = dict(fc="white", ec="none", alpha=0.85, pad=1.2)
arrow = dict(arrowstyle="-", lw=0.5, color="k")
ax.text(0, 5.2, r"$\mathcal{R}_V$", ha="center", va="center", fontsize=11, zorder=7)
ax.text(
    5.6,
    0,
    "$t$- and $u$-\nchannel\nregions",
    ha="center",
    va="center",
    fontsize=7,
    linespacing=1.1,
    zorder=7,
)
ax.annotate(
    "$s$-channel\nFeynman disc\n$|q| \\leq 1$",
    (-0.45, 0.45),
    xytext=(-5.4, 3.4),
    ha="center",
    va="center",
    fontsize=7,
    linespacing=1.1,
    bbox=box,
    arrowprops=arrow,
    zorder=8,
)
ax.annotate(
    "$q_□$",
    (Q_SQ, 0),
    xytext=(-4.8, -2.6),
    ha="center",
    va="center",
    fontsize=9,
    bbox=box,
    arrowprops=arrow,
    zorder=8,
)
ax.annotate(
    r"$|q| = \mathrm{e}^{\sigma_V(\theta)}$",
    (np.exp(sigma_of_theta(np.pi / 4)) / np.sqrt(2),) * 2,
    xytext=(7.4, 8.6),
    ha="center",
    va="center",
    fontsize=7,
    bbox=box,
    arrowprops=arrow,
    zorder=8,
)
ax.annotate(
    r"$|q| = 4\beta^2$",
    (4 * B2 * np.cos(-np.pi / 4), 4 * B2 * np.sin(-np.pi / 4)),
    xytext=(8.0, -9.0),
    ha="center",
    va="center",
    fontsize=7,
    bbox=box,
    arrowprops=arrow,
    zorder=8,
)

ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
ax.set_aspect("equal")
ax.set_xlabel(r"$\mathrm{Re}\,q$")
ax.set_ylabel(r"$\mathrm{Im}\,q$")
ax.set_xticks([-8, -4, 0, 4, 8])
ax.set_yticks([-8, -4, 0, 4, 8])

OUT.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT / "ws_q_plane.pdf")
print("saved", OUT / "ws_q_plane.pdf")
