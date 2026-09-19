"""
PRIE ML — Probability Calibration & Reliability Assessment
File: backend/ml/calibration.py

MODULE: M06 — Placement Readiness Prediction Engine
TRACEABILITY: Phase 06 Model Calibration Methodology; RQ1; H1 (Brier <= 0.08)

Implements:
  - Platt Scaling (Sigmoid CalibratedClassifierCV)
  - Isotonic Regression Calibration
  - Brier Score calculation & decomposition
  - Reliability curve calibration coordinates
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Literal, Optional, Tuple

import numpy as np
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn.metrics import brier_score_loss

from ml.baselines import calculate_ece

logger = logging.getLogger("PRIE.ML.Calibration")

CalibrationMethod = Literal["sigmoid", "isotonic"]


class CalibratedModelWrapper:
    """
    Wraps a base classifier (e.g. XGBoost) with a post-hoc probability calibrator
    fitted on a distinct validation split to prevent target and scaling leakage.
    """

    def __init__(
        self,
        base_estimator: Any,
        method: CalibrationMethod = "sigmoid",
    ) -> None:
        self.base_estimator = base_estimator
        self.method = method
        self.calibrated_classifier: Optional[CalibratedClassifierCV] = None

    def fit_calibration(self, X_val: np.ndarray, y_val: np.ndarray) -> CalibratedClassifierCV:
        """
        Fit calibration parameters on the validation partition using prefit base estimator.
        """
        self.calibrated_classifier = CalibratedClassifierCV(
            estimator=self.base_estimator,
            method=self.method,
            cv="prefit",
        )
        self.calibrated_classifier.fit(X_val, y_val)
        logger.info(f"Fitted {self.method} calibration on {len(X_val)} validation instances.")
        return self.calibrated_classifier

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Return calibrated probabilities P(y=1 | X)."""
        if self.calibrated_classifier is None:
            raise RuntimeError("Calibrator has not been fitted. Call fit_calibration first.")
        return self.calibrated_classifier.predict_proba(X)

    def evaluate_calibration(
        self,
        X_test: np.ndarray,
        y_test: np.ndarray,
        n_bins: int = 10,
    ) -> Dict[str, Any]:
        """
        Evaluate calibration fidelity on held-out test data.
        """
        probs = self.predict_proba(X_test)[:, 1]
        brier = float(brier_score_loss(y_test, probs))
        ece = calculate_ece(y_test, probs, n_bins=n_bins)

        prob_true, prob_pred = calibration_curve(y_test, probs, n_bins=n_bins, strategy="uniform")

        return {
            "calibration_method": self.method,
            "brier_score": round(brier, 4),
            "ece": round(ece, 4),
            "h1_target_met": brier <= 0.08,
            "reliability_curve": {
                "prob_true": [round(float(v), 4) for v in prob_true],
                "prob_pred": [round(float(v), 4) for v in prob_pred],
            },
        }
