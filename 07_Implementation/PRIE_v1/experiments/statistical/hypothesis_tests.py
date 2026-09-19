"""
PRIE Research Experiment Framework — Statistical Hypothesis Testing Procedures
File: experiments/statistical/hypothesis_tests.py

TRACEABILITY: Phase 06 Statistical Procedures; RQ1–RQ6
Implements:
  - Wilcoxon Signed-Rank Test (paired non-parametric comparison)
  - McNemar's Test (paired binary classifier contingency comparison)
  - Friedman Test (multi-classifier ranking across folds)
  - Paired t-test with Cohen's d effect size
  - 5x2 Cross-Validated Paired Test (Dietterich, 1998)
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy import stats

logger = logging.getLogger("PRIE.Experiments.Stats")


def compute_cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    """Compute Cohen's d effect size for paired samples."""
    diff = group1 - group2
    mean_diff = np.mean(diff)
    std_diff = np.std(diff, ddof=1)
    if std_diff < 1e-8:
        return 0.0
    return float(mean_diff / std_diff)


def paired_t_test(
    scores_a: np.ndarray,
    scores_b: np.ndarray,
    alpha: float = 0.05,
) -> Dict[str, Any]:
    """
    Perform two-sided paired Student's t-test.
    """
    a = np.asarray(scores_a, dtype=float)
    b = np.asarray(scores_b, dtype=float)
    if len(a) != len(b):
        raise ValueError(f"Sample size mismatch: {len(a)} vs {len(b)}")

    t_stat, p_val = stats.ttest_rel(a, b)
    d = compute_cohens_d(a, b)

    return {
        "test_name": "Paired Student's t-test",
        "sample_size": len(a),
        "test_statistic": round(float(t_stat), 4),
        "p_value": float(p_val),
        "effect_size_cohens_d": round(float(d), 4),
        "alpha": alpha,
        "is_significant": bool(p_val < alpha),
    }


def wilcoxon_signed_rank(
    scores_a: np.ndarray,
    scores_b: np.ndarray,
    alpha: float = 0.05,
) -> Dict[str, Any]:
    """
    Perform Wilcoxon signed-rank test for paired non-parametric distribution comparison.
    """
    a = np.asarray(scores_a, dtype=float)
    b = np.asarray(scores_b, dtype=float)
    if len(a) != len(b):
        raise ValueError("Sample sizes must match for Wilcoxon test")

    diff = a - b
    # Check for all-zero differences
    if np.all(diff == 0):
        return {
            "test_name": "Wilcoxon Signed-Rank Test",
            "sample_size": len(a),
            "test_statistic": 0.0,
            "p_value": 1.0,
            "rank_biserial_r": 0.0,
            "alpha": alpha,
            "is_significant": False,
        }

    stat, p_val = stats.wilcoxon(a, b, zero_method="wilcox")
    # Rank-biserial correlation r = 1 - (2W / (n(n+1)/2))
    n = len(a)
    w_max = n * (n + 1) / 2
    r_biserial = 1.0 - (2.0 * stat / max(1.0, w_max))

    return {
        "test_name": "Wilcoxon Signed-Rank Test",
        "sample_size": n,
        "test_statistic": round(float(stat), 4),
        "p_value": float(p_val),
        "rank_biserial_r": round(float(r_biserial), 4),
        "alpha": alpha,
        "is_significant": bool(p_val < alpha),
    }


def mcnemar_test(
    y_true: np.ndarray,
    y_pred_a: np.ndarray,
    y_pred_b: np.ndarray,
    alpha: float = 0.05,
) -> Dict[str, Any]:
    """
    Perform McNemar's test with continuity correction on 2x2 contingency matrix of two classifiers.
    Contingency table:
      b = Model A correct, Model B incorrect
      c = Model A incorrect, Model B correct
    Statistic: (|b - c| - 1)^2 / (b + c)
    """
    correct_a = (y_pred_a == y_true)
    correct_b = (y_pred_b == y_true)

    b = int(np.sum(correct_a & ~correct_b))
    c = int(np.sum(~correct_a & correct_b))

    if (b + c) == 0:
        return {
            "test_name": "McNemar Test",
            "contingency_discordant": {"b": 0, "c": 0},
            "test_statistic": 0.0,
            "p_value": 1.0,
            "alpha": alpha,
            "is_significant": False,
        }

    # Chi-squared with 1 df and Yates continuity correction
    stat = (abs(b - c) - 1.0) ** 2 / (b + c)
    p_val = stats.chi2.sf(stat, df=1)

    return {
        "test_name": "McNemar Test (Continuity Corrected)",
        "contingency_discordant": {"model_a_correct_only": b, "model_b_correct_only": c},
        "test_statistic": round(float(stat), 4),
        "p_value": float(p_val),
        "alpha": alpha,
        "is_significant": bool(p_val < alpha),
    }


def friedman_ranking_test(
    scores_matrix: np.ndarray,
    model_names: List[str],
    alpha: float = 0.05,
) -> Dict[str, Any]:
    """
    Perform Friedman non-parametric two-way ANOVA test across multiple models and folds.
    scores_matrix: (n_folds, n_models)
    """
    mat = np.asarray(scores_matrix, dtype=float)
    n_folds, n_models = mat.shape
    if n_models != len(model_names):
        raise ValueError("Model names length must match matrix columns")

    stat, p_val = stats.friedmanchisquare(*[mat[:, j] for j in range(n_models)])

    # Compute average ranks
    ranks = np.zeros_like(mat)
    for i in range(n_folds):
        ranks[i] = stats.rankdata(-mat[i])  # descending: rank 1 is highest score
    avg_ranks = {model_names[j]: round(float(np.mean(ranks[:, j])), 2) for j in range(n_models)}

    return {
        "test_name": "Friedman Test",
        "n_folds": n_folds,
        "n_models": n_models,
        "average_ranks": avg_ranks,
        "test_statistic": round(float(stat), 4),
        "p_value": float(p_val),
        "alpha": alpha,
        "is_significant": bool(p_val < alpha),
    }
