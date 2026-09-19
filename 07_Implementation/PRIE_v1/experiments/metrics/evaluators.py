"""
PRIE Research Experiment Framework — Evaluation Metrics Calculator
File: experiments/metrics/evaluators.py

TRACEABILITY: Phase 06 Evaluation Metrics Protocol
Implements:
  - Accuracy, Precision, Recall, Macro-F1
  - Area Under ROC (ROC-AUC) & PR Curve (PR-AUC)
  - Strictly proper scoring rule: Brier Score (MSE of predicted probability)
  - Expected Calibration Error (ECE) with uniform binning
  - Confusion matrix & calibration reliability curves
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    precision_recall_curve,
    auc,
    brier_score_loss,
    confusion_matrix,
    classification_report,
)
from sklearn.calibration import calibration_curve

logger = logging.getLogger("PRIE.Experiments.Metrics")


def compute_ece(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> float:
    """
    Calculate Expected Calibration Error:
      ECE = sum_{m=1}^M (|B_m| / N) * |acc(B_m) - conf(B_m)|
    """
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    bin_indices = np.digitize(y_prob, bins) - 1
    bin_indices = np.clip(bin_indices, 0, n_bins - 1)

    n_samples = len(y_true)
    ece = 0.0

    for m in range(n_bins):
        mask = bin_indices == m
        bin_count = np.sum(mask)
        if bin_count > 0:
            bin_acc = np.mean(y_true[mask])
            bin_conf = np.mean(y_prob[mask])
            ece += (bin_count / n_samples) * np.abs(bin_acc - bin_conf)

    return float(ece)


def evaluate_classifier_predictions(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    threshold: float = 0.5,
    n_bins: int = 10,
) -> Dict[str, Any]:
    """
    Comprehensive evaluation for binary placement prediction models.
    """
    y_pred = (y_prob >= threshold).astype(int)

    acc = float(accuracy_score(y_true, y_pred))
    prec = float(precision_score(y_true, y_pred, zero_division=0))
    rec = float(recall_score(y_true, y_pred, zero_division=0))
    macro_f1 = float(f1_score(y_true, y_pred, average="macro", zero_division=0))

    try:
        roc_auc = float(roc_auc_score(y_true, y_prob))
    except ValueError:
        roc_auc = 0.5

    try:
        p_curve, r_curve, _ = precision_recall_curve(y_true, y_prob)
        pr_auc = float(auc(r_curve, p_curve))
    except Exception:
        pr_auc = 0.0

    brier = float(brier_score_loss(y_true, y_prob))
    ece = compute_ece(y_true, y_prob, n_bins=n_bins)
    cm = confusion_matrix(y_true, y_pred).tolist()

    prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy="uniform")

    return {
        "accuracy": round(acc, 4),
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "macro_f1": round(macro_f1, 4),
        "roc_auc": round(roc_auc, 4),
        "pr_auc": round(pr_auc, 4),
        "brier_score": round(brier, 4),
        "ece": round(ece, 4),
        "h1_brier_target_met": bool(brier <= 0.08),
        "h1_ece_target_met": bool(ece <= 0.05),
        "confusion_matrix": cm,
        "calibration_curve": {
            "fraction_of_positives": [round(float(v), 4) for v in prob_true],
            "mean_predicted_value": [round(float(v), 4) for v in prob_pred],
        },
    }
