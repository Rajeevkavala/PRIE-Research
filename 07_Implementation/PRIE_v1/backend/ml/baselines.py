"""
PRIE ML — Predictive Baselines & Metric Calculators
File: backend/ml/baselines.py

MODULE: M06 — Placement Readiness Prediction Engine
TRACEABILITY: Phase 06 Baseline Methodology; DD-002

Provides standard benchmark baselines:
  - BL-01: Logistic Regression with L2 regularization
  - BL-02: Random Forest Classifier
  - BL-03: Uncalibrated XGBoost Baseline

Metrics:
  - Accuracy, Precision, Recall, Macro-F1
  - ROC-AUC, PR-AUC
  - Brier Score: (1/N) * sum((p - y)^2)
  - Expected Calibration Error (ECE)
"""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional, Tuple

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
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

logger = logging.getLogger("PRIE.ML.Baselines")


def calculate_ece(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> float:
    """
    Calculate Expected Calibration Error (ECE).
    
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


def evaluate_binary_predictions(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    threshold: float = 0.5,
) -> Dict[str, Any]:
    """
    Compute full evaluation metrics on binary classification predictions.
    """
    y_pred = (y_prob >= threshold).astype(int)

    acc = float(accuracy_score(y_true, y_pred))
    prec = float(precision_score(y_true, y_pred, zero_division=0))
    rec = float(recall_score(y_true, y_pred, zero_division=0))
    f1 = float(f1_score(y_true, y_pred, average="macro", zero_division=0))

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
    ece = calculate_ece(y_true, y_prob)
    cm = confusion_matrix(y_true, y_pred).tolist()

    return {
        "accuracy": round(acc, 4),
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "macro_f1": round(f1, 4),
        "roc_auc": round(roc_auc, 4),
        "pr_auc": round(pr_auc, 4),
        "brier_score": round(brier, 4),
        "ece": round(ece, 4),
        "confusion_matrix": cm,
    }


class BaselineSuite:
    """Manages baseline models training and evaluation."""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.log_reg = LogisticRegression(max_iter=1000, random_state=random_state)
        self.rf = RandomForestClassifier(n_estimators=100, random_state=random_state)

    def train_and_evaluate(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_test: np.ndarray,
        y_test: np.ndarray,
    ) -> Dict[str, Dict[str, Any]]:
        """Train standard baselines and evaluate on test set."""
        results = {}

        # 1. Logistic Regression
        self.log_reg.fit(X_train, y_train)
        lr_probs = self.log_reg.predict_proba(X_test)[:, 1]
        results["logistic_regression"] = evaluate_binary_predictions(y_test, lr_probs)

        # 2. Random Forest
        self.rf.fit(X_train, y_train)
        rf_probs = self.rf.predict_proba(X_test)[:, 1]
        results["random_forest"] = evaluate_binary_predictions(y_test, rf_probs)

        return results
