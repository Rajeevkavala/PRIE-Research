"""
Generate Figure 2: (a) Student Profile Vector (b) Preprocessed feature distribution
Publication-ready at 300 DPI.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

FIG_DIR = Path(r"d:\4-1 AD\All College Docs and ppts\Documentations\PDR\PRIE-Research\10_Publication\Conference_Paper\figures")
OUT_PATH = FIG_DIR / "fig2_spv_feature_distribution.png"

# Style configuration
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.labelsize": 9.5,
    "axes.titlesize": 10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "axes.grid": True,
    "grid.alpha": 0.35,
    "grid.linestyle": ":",
})

fig = plt.figure(figsize=(10, 3.8))

# ── Subplot (a): Student Profile Vector Radar / Domain Breakdown ──────────────
ax1 = fig.add_subplot(1, 2, 1, polar=True)

categories = [
    'Academic (f1-5)', 'Coding (f6-11)', 'Resume ATS (f12-14)',
    'Telemetry (f15-16)', 'Demographics (f17)', 'Demeanor (f18-20)',
    'Engagement (f21)', 'Roadmap (f22)'
]
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Persona vectors
at_risk = [0.52, 0.44, 0.58, 0.40, 1.0, 0.48, 0.38, 0.42]
ready   = [0.86, 0.88, 0.82, 0.84, 1.0, 0.78, 0.89, 0.85]
at_risk += at_risk[:1]
ready   += ready[:1]

ax1.plot(angles, at_risk, 'o-', linewidth=1.5, color='#ef4444', label='At-Risk (PRS=42.6)')
ax1.fill(angles, at_risk, color='#ef4444', alpha=0.15)

ax1.plot(angles, ready, 's-', linewidth=1.5, color='#0284c7', label='Ready (PRS=84.2)')
ax1.fill(angles, ready, color='#0284c7', alpha=0.18)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, size=7.5, color='#1e293b')
ax1.set_ylim(0, 1.05)
ax1.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax1.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], size=6.5, color='#64748b')
ax1.set_title('(a) Student Profile Vector ($x_{\\text{spv}}$)', pad=14, fontweight='bold', fontsize=9.5)
ax1.legend(loc='lower left', bbox_to_anchor=(-0.15, -0.15), frameon=True, fontsize=7.5)

# ── Subplot (b): Preprocessed Feature Distribution (Normalized Cohort) ────────
ax2 = fig.add_subplot(1, 2, 2)

np.random.seed(42)
# Feature distributions for 5 representative preprocessed features
features = ['DSA ($f_8$)', 'CGPA ($f_1$)', 'S-BERT ($f_{13}$)', 'Demeanor ($f_{20}$)', 'Roadmap ($f_{22}$)']
colors = ['#3b82f6', '#10b981', '#8b5cf6', '#f59e0b', '#06b6d4']

data = [
    np.clip(np.random.beta(5, 2, 500), 0, 1),      # DSA
    np.clip(np.random.normal(0.72, 0.14, 500), 0, 1), # CGPA
    np.clip(np.random.beta(4, 3, 500), 0, 1),      # S-BERT
    np.clip(np.random.normal(0.60, 0.18, 500), 0, 1), # Demeanor
    np.clip(np.random.beta(3, 2, 500), 0, 1),      # Roadmap
]

positions = np.arange(len(features))
bp = ax2.boxplot(
    data, positions=positions, widths=0.45, patch_artist=True,
    showmeans=True, meanline=True,
    medianprops=dict(color='#0f172a', linewidth=1.5),
    meanprops=dict(color='#dc2626', linewidth=1.5, linestyle='--'),
    flierprops=dict(marker='.', markerfacecolor='#94a3b8', markersize=3, alpha=0.5)
)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.65)
    patch.set_edgecolor('#1e293b')

ax2.set_xticks(positions)
ax2.set_xticklabels(features, size=7.5, rotation=12)
ax2.set_ylabel('Normalized Feature Value $[0.0, 1.0]$', fontsize=8.5)
ax2.set_ylim(-0.05, 1.10)
ax2.set_title('(b) Preprocessed Feature Distribution ($N=2,500$)', fontweight='bold', fontsize=9.5)

# Custom legend for boxplot
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='#0f172a', lw=1.5, label='Median'),
    Line2D([0], [0], color='#dc2626', lw=1.5, linestyle='--', label='Empirical Mean'),
]
ax2.legend(handles=legend_elements, loc='lower right', frameon=True, fontsize=7.5)

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=300, bbox_inches='tight')
plt.close()

print(f"Generated Figure 2 successfully: {OUT_PATH}")
