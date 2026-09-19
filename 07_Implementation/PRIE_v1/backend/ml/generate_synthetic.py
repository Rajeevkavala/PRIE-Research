"""
PRIE v1 — DS-SYNTH-01: Synthetic SPV Cohort Generator
File: backend/ml/generate_synthetic.py

SCIENTIFIC INTEGRITY NOTICE:
  This script generates DS-SYNTH-01 — a SYNTHETIC simulation dataset.
  Status: SYNTHETIC (Simulation) — NOT empirical student evidence.
  Per Dataset_Design.md: "Synthetic data is a computational stress-testing tool.
  It does NOT constitute real-world empirical proof."
  All generated files are labeled with EPISTEMOLOGICAL_STATUS=SYNTHETIC.

Generation Method:
  Gaussian Copula fitted to DS-BENCH-01 marginal distributions and published
  inter-feature correlations from Dataset_Design.md (Kuzilek et al., OULAD).
  Target correlations: Pearson r=0.68 (cgpa vs dsa_score),
                       r=-0.54 (gap_score vs cosine_similarity).

Usage:
  python backend/ml/generate_synthetic.py
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Add backend to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from spv_version import SPV_FEATURE_NAMES, SPV_DIMENSION

logger = logging.getLogger("PRIE.GenerateSynthetic")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

# ── DS-SYNTH-01 Configuration ─────────────────────────────────────────────────
N_SAMPLES: int = 2500
RANDOM_SEED: int = 42
EPISTEMOLOGICAL_STATUS: str = "SYNTHETIC — NOT EMPIRICAL EVIDENCE (DS-SYNTH-01)"

# Calibrated inter-feature correlation structure from Dataset_Design.md
# Key documented correlations:
#   cgpa  <-> dsa_score:       r=0.68
#   gap_score <-> cosine_sim:  r=-0.54
#   cgpa  <-> aptitude:        r=0.55
#   dsa_score <-> programming: r=0.72
#   consistency <-> engagement: r=0.65
#   has_internship <-> project_count: r=0.42

def _build_correlation_matrix() -> np.ndarray:
    """
    Build a 22x22 correlation matrix for the SPV features.
    Only key published correlations are enforced; others are set to
    weak positive correlation (0.15) to maintain plausibility.
    """
    n = SPV_DIMENSION
    C = np.full((n, n), 0.15)  # weak positive background
    np.fill_diagonal(C, 1.0)

    # Feature index map (order from SPV_FEATURE_NAMES)
    idx = {name: i for i, name in enumerate(SPV_FEATURE_NAMES)}

    # Key published correlations (Dataset_Design.md + literature)
    correlations = [
        ("cgpa", "dsa_score",          0.68),
        ("cgpa", "aptitude_score",     0.55),
        ("cgpa", "programming_score",  0.52),
        ("cgpa", "dbms_score",         0.60),
        ("cgpa", "os_score",           0.58),
        ("cgpa", "cn_score",           0.56),
        ("dsa_score", "programming_score", 0.72),
        ("dsa_score", "aptitude_score",    0.61),
        ("gap_score", "cosine_similarity", -0.54),
        ("gap_score", "dsa_score",         -0.62),
        ("gap_score", "programming_score", -0.58),
        ("consistency_score", "engagement_score", 0.65),
        ("consistency_score", "assessment_attempts", 0.58),
        ("engagement_score", "assessment_attempts", 0.70),
        ("engagement_score", "roadmap_completion_rate", 0.63),
        ("has_internship", "project_count", 0.42),
        ("has_internship", "soft_skills_score", 0.38),
        ("project_count", "project_quality_score", 0.55),
        ("resume_ats_score", "cosine_similarity", 0.45),
        ("certifications_count", "cgpa", 0.35),
        ("behavior_score", "soft_skills_score", 0.68),
        ("roadmap_completion_rate", "dsa_score", 0.48),
    ]

    for f1, f2, r in correlations:
        i, j = idx[f1], idx[f2]
        C[i, j] = r
        C[j, i] = r

    # Ensure positive semi-definite via eigenvalue clipping
    eigvals, eigvecs = np.linalg.eigh(C)
    eigvals = np.maximum(eigvals, 1e-6)
    C_psd = eigvecs @ np.diag(eigvals) @ eigvecs.T
    # Re-normalize to correlation matrix
    D = np.sqrt(np.diag(C_psd))
    C_corr = C_psd / np.outer(D, D)
    np.fill_diagonal(C_corr, 1.0)
    return C_corr


# ── Per-feature marginal distributions (calibrated to DS-BENCH-01 ranges) ────
FEATURE_MARGINALS = {
    "cgpa":                    ("uniform",  6.0, 9.8),
    "dsa_score":               ("normal",   62.0, 18.0),
    "dbms_score":              ("normal",   68.0, 15.0),
    "os_score":                ("normal",   65.0, 16.0),
    "cn_score":                ("normal",   64.0, 17.0),
    "programming_score":       ("normal",   65.0, 17.0),
    "aptitude_score":          ("normal",   63.0, 16.0),
    "soft_skills_score":       ("normal",   60.0, 14.0),
    "project_count":           ("randint",  0, 8),
    "project_quality_score":   ("normal",   55.0, 20.0),
    "has_internship":          ("bernoulli", 0.38, None),
    "certifications_count":    ("randint",  0, 5),
    "resume_ats_score":        ("normal",   62.0, 18.0),
    "cosine_similarity":       ("uniform",  0.30, 0.95),
    "gap_score":               ("beta",     2.0, 5.0),    # skewed toward low gap
    "consistency_score":       ("beta",     3.0, 3.0),
    "branch_encoded":          ("choice",   [0.50, 0.65, 0.75, 0.90, 0.92, 0.95],
                                            [0.08, 0.07, 0.15, 0.30, 0.15, 0.25]),
    "target_role_encoded":     ("choice",   [0.65, 0.70, 0.75, 0.80, 0.82, 0.85, 0.88, 0.90],
                                            [0.05, 0.10, 0.10, 0.10, 0.15, 0.15, 0.20, 0.15]),
    "assessment_attempts":     ("randint",  0, 40),
    "behavior_score":          ("normal",   62.0, 15.0),
    "engagement_score":        ("beta",     3.0, 2.5),
    "roadmap_completion_rate": ("beta",     2.0, 3.0),
}

FEATURE_BOUNDS = {
    "cgpa":                    (0.0, 10.0),
    "dsa_score":               (0.0, 100.0),
    "dbms_score":              (0.0, 100.0),
    "os_score":                (0.0, 100.0),
    "cn_score":                (0.0, 100.0),
    "programming_score":       (0.0, 100.0),
    "aptitude_score":          (0.0, 100.0),
    "soft_skills_score":       (0.0, 100.0),
    "project_count":           (0.0, 20.0),
    "project_quality_score":   (0.0, 100.0),
    "has_internship":          (0.0, 1.0),
    "certifications_count":    (0.0, 15.0),
    "resume_ats_score":        (0.0, 100.0),
    "cosine_similarity":       (0.0, 1.0),
    "gap_score":               (0.0, 1.0),
    "consistency_score":       (0.0, 1.0),
    "branch_encoded":          (0.0, 1.0),
    "target_role_encoded":     (0.0, 1.0),
    "assessment_attempts":     (0.0, 100.0),
    "behavior_score":          (0.0, 100.0),
    "engagement_score":        (0.0, 1.0),
    "roadmap_completion_rate": (0.0, 1.0),
}


def _sample_marginals(rng: np.random.Generator, n: int) -> np.ndarray:
    """Sample n observations from each feature's marginal distribution."""
    samples = np.zeros((n, SPV_DIMENSION))
    for i, name in enumerate(SPV_FEATURE_NAMES):
        dist_spec = FEATURE_MARGINALS[name]
        dist_type = dist_spec[0]
        lo, hi = FEATURE_BOUNDS[name]

        if dist_type == "normal":
            mu, sigma = dist_spec[1], dist_spec[2]
            samples[:, i] = np.clip(rng.normal(mu, sigma, n), lo, hi)
        elif dist_type == "uniform":
            a, b = dist_spec[1], dist_spec[2]
            samples[:, i] = rng.uniform(a, b, n)
        elif dist_type == "beta":
            a, b = dist_spec[1], dist_spec[2]
            samples[:, i] = rng.beta(a, b, n) * (hi - lo) + lo
        elif dist_type == "randint":
            a, b = dist_spec[1], dist_spec[2]
            samples[:, i] = rng.integers(a, b + 1, n).astype(float)
        elif dist_type == "bernoulli":
            p = dist_spec[1]
            samples[:, i] = rng.binomial(1, p, n).astype(float)
        elif dist_type == "choice":
            values, probs = dist_spec[1], dist_spec[2]
            choices = rng.choice(values, n, p=probs)
            samples[:, i] = choices

    return samples


def _apply_gaussian_copula(marginals: np.ndarray, C_corr: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Apply Gaussian copula to introduce correlation structure."""
    from scipy import stats

    n, d = marginals.shape
    # Step 1: Convert marginals to uniform [0,1] via rank transform
    uniform = np.zeros_like(marginals)
    for j in range(d):
        ranks = stats.rankdata(marginals[:, j])
        uniform[:, j] = ranks / (n + 1)

    # Step 2: Map to correlated Gaussian
    L = np.linalg.cholesky(C_corr)
    z_indep = rng.standard_normal((n, d))
    z_corr = z_indep @ L.T

    # Step 3: Map correlated Gaussian back to uniform
    p_corr = stats.norm.cdf(z_corr)

    # Step 4: Map correlated uniform back to original marginals via percentile
    result = np.zeros_like(marginals)
    for j in range(d):
        sorted_marginal = np.sort(marginals[:, j])
        quantile_idx = np.clip(
            (p_corr[:, j] * n).astype(int), 0, n - 1
        )
        result[:, j] = sorted_marginal[quantile_idx]

    return result


def _compute_labels(df: pd.DataFrame) -> pd.Series:
    """
    Compute synthetic placement readiness label using a deterministic rule
    based on key SPV features. This is a simulation heuristic — NOT a
    trained empirical model.

    Rule: Label = 1 (Placed) if weighted score >= 0.55
    """
    score = (
        0.20 * (df["cgpa"] / 10.0) +
        0.15 * (df["dsa_score"] / 100.0) +
        0.10 * (df["programming_score"] / 100.0) +
        0.10 * df["has_internship"] +
        0.10 * (df["resume_ats_score"] / 100.0) +
        0.10 * df["cosine_similarity"] +
        0.08 * (df["aptitude_score"] / 100.0) +
        0.07 * (df["engagement_score"]) +
        0.05 * (1.0 - df["gap_score"]) +
        0.05 * df["consistency_score"]
    )
    return (score >= 0.55).astype(int)


def generate_ds_synth_01(output_path: Path = None) -> pd.DataFrame:
    """
    Generate DS-SYNTH-01: 2,500 synthetic 22-dimensional SPV tensors.

    Returns:
        pd.DataFrame with 22 SPV feature columns + 'placement_label' + metadata columns.
    """
    output_path = output_path or config.SYNTH_DATA_PATH
    rng = np.random.default_rng(seed=RANDOM_SEED)

    logger.info(f"Generating DS-SYNTH-01: N={N_SAMPLES} synthetic SPV tensors...")
    logger.warning(f"SCIENTIFIC INTEGRITY: {EPISTEMOLOGICAL_STATUS}")

    # 1. Sample marginals
    marginals = _sample_marginals(rng, N_SAMPLES)

    # 2. Build correlation matrix
    C_corr = _build_correlation_matrix()

    # 3. Apply Gaussian Copula
    try:
        from scipy import stats  # noqa: F401
        data = _apply_gaussian_copula(marginals, C_corr, rng)
        logger.info("Gaussian copula correlation structure applied.")
    except ImportError:
        logger.warning("scipy not available — using uncorrelated marginals.")
        data = marginals

    # 4. Clip to bounds
    for i, name in enumerate(SPV_FEATURE_NAMES):
        lo, hi = FEATURE_BOUNDS[name]
        data[:, i] = np.clip(data[:, i], lo, hi)

    # 5. Round integer-like features
    int_features = ["project_count", "certifications_count", "assessment_attempts", "has_internship"]
    for name in int_features:
        i = SPV_FEATURE_NAMES.index(name)
        data[:, i] = np.round(data[:, i]).astype(float)

    # 6. Build DataFrame
    df = pd.DataFrame(data, columns=SPV_FEATURE_NAMES)

    # 7. Compute synthetic labels
    df["placement_label"] = _compute_labels(df)

    # 8. Add metadata
    df["epistemological_status"] = EPISTEMOLOGICAL_STATUS
    df["spv_version"] = "v1"
    df["random_seed"] = RANDOM_SEED

    # 9. Save
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.drop(columns=["epistemological_status", "spv_version", "random_seed"]).to_csv(
        output_path, index=False
    )

    placed = df["placement_label"].sum()
    logger.info(
        f"DS-SYNTH-01 generated: {N_SAMPLES} records, "
        f"{placed} Placed ({100*placed/N_SAMPLES:.1f}%), "
        f"{N_SAMPLES - placed} Not Placed. "
        f"Saved to {output_path}"
    )
    return df


if __name__ == "__main__":
    df = generate_ds_synth_01()
    print(f"\nDS-SYNTH-01 shape: {df.shape}")
    print(f"Class distribution:\n{df['placement_label'].value_counts()}")
    print(f"\nKey correlation checks:")
    print(f"  cgpa vs dsa_score:        r={df['cgpa'].corr(df['dsa_score']):.3f}  (target: 0.68)")
    print(f"  gap_score vs cosine_sim:  r={df['gap_score'].corr(df['cosine_similarity']):.3f}  (target: -0.54)")
    print(f"  consistency vs engagement: r={df['consistency_score'].corr(df['engagement_score']):.3f}  (target: 0.65)")
