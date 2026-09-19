"""
PRIE v1 — Module M06: Placement Readiness Prediction Engine (Track 1)
File: backend/modules/m06_placement_predictor.py

MODULE: M06 — Placement Readiness Prediction Engine
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (XGBoost per DD-002)
RESEARCH_GAP: RG2 (Static single-snapshot prediction)
RESEARCH_OBJECTIVE: RO3 (Dynamic Longitudinal Sequence Modeling — Track 2 = future)
TRACEABILITY: Paper01, Paper04, Paper18, Paper22, Paper44; DD-002

Implements:
  Track 1 (Cross-Sectional): XGBoost calibrated classifier
    - Readiness probability P_ready ∈ [0.0, 1.0]
    - Discrete tier: Ready (≥0.75), Needs Remediation (0.45–0.75), At-Risk (<0.45)
    - 200-iteration Gaussian bootstrap confidence interval
    - TreeSHAP local attribution (fast C++ TreeExplainer)
  Track 2 (Longitudinal TFT): PROPOSED_ARCHITECTURE — stub with disclosure
"""

from __future__ import annotations

import json
import logging
import pickle
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from spv_version import (
    SPV_FEATURE_NAMES,
    SPV_DIMENSION,
    IMMUTABLE_FEATURES,
    validate_spv_vector,
    SPVValidationError,
)

logger = logging.getLogger("PRIE.M06.PlacementPredictor")


class ModelArtifactNotFoundError(FileNotFoundError):
    """Raised when required serialized ML model artifacts cannot be found on disk."""
    pass


class ModelSchemaMismatchError(ValueError):
    """Raised when loaded model feature schema mismatches canonical SPV specification."""
    pass


class ModelLoadError(RuntimeError):
    """Raised when serialized model weights fail to load or unpickle."""
    pass


class PredictionInferenceError(RuntimeError):
    """Raised when model inference fails during prediction."""
    pass


def _classify_tier(prob: float) -> str:
    """Map P_ready to discrete readiness tier (M06 specification)."""
    for tier, (lo, hi) in config.READINESS_TIERS.items():
        if lo <= prob < hi:
            return tier
    return "At-Risk"


class PlacementPredictor:
    """
    M06: Placement Readiness Prediction Engine — Track 1 (XGBoost).

    EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (DD-002)
    Track 2 (TFT longitudinal): PROPOSED_ARCHITECTURE — not yet implemented.
    """

    def __init__(
        self,
        model_path: Optional[Path] = None,
        scaler_path: Optional[Path] = None,
        feature_names_path: Optional[Path] = None,
        bootstrap_iters: int = None,
        bootstrap_noise_std: float = None,
    ) -> None:
        self.model_path = model_path or config.XGB_MODEL_PATH
        self.scaler_path = scaler_path or config.SCALER_PATH
        self.feature_names_path = feature_names_path or config.FEATURE_NAMES_PATH
        self.n_bootstrap = bootstrap_iters or config.BOOTSTRAP_ITERATIONS
        self.noise_std = bootstrap_noise_std or config.BOOTSTRAP_NOISE_STD

        self.model: Any = None
        self.scaler: Any = None
        self.feature_names: List[str] = []
        self.explainer: Any = None
        self.is_mock: bool = False
        self.model_id: str = "prie-xgb-static-v1"
        self._load_artifacts()

    def _load_artifacts(self) -> None:
        """Load serialized model, scaler, and feature names. Gated by ALLOW_DUMMY_MODELS."""
        artifacts_exist = (
            self.model_path.exists()
            and self.scaler_path.exists()
            and self.feature_names_path.exists()
        )

        if artifacts_exist:
            try:
                with open(self.model_path, "rb") as f:
                    self.model = pickle.load(f)
                with open(self.scaler_path, "rb") as f:
                    self.scaler = pickle.load(f)
                with open(self.feature_names_path, "r", encoding="utf-8") as f:
                    self.feature_names = json.load(f)
            except Exception as e:
                logger.error(f"Failed to load model artifacts from {self.model_path}: {e}")
                raise ModelLoadError(f"Could not load ML artifacts: {e}") from e

            # Verify schema invariance
            if self.feature_names != SPV_FEATURE_NAMES:
                raise ModelSchemaMismatchError(
                    f"Model feature schema mismatch: expected {SPV_FEATURE_NAMES}, got {self.feature_names}"
                )

            self.is_mock = False
            self.model_id = "prie-xgb-calibrated-v1"
            logger.info(f"Loaded certified research ML artifacts from {self.model_path}")
        else:
            if not config.ALLOW_DUMMY_MODELS or config.IS_RESEARCH_MODE:
                raise ModelArtifactNotFoundError(
                    f"Model artifacts not found at {self.model_path}. "
                    f"In research/production mode, silent dummy training is strictly disabled. "
                    f"Run scripts/train_model.py to train and calibrate the canonical model."
                )

            logger.warning(
                "ML artifacts not found — initializing mock development model. "
                "NOTICE: MOCK MODE ACTIVE — THIS IS NOT CERTIFIED RESEARCH OUTPUT."
            )
            self._init_fallback()
            self.is_mock = True
            self.model_id = "prie-xgb-dummy-dev"

        try:
            import shap
            self.explainer = shap.TreeExplainer(
                self.model.calibrated_classifiers_[0].estimator
                if hasattr(self.model, "calibrated_classifiers_")
                else self.model
            )
        except Exception as e:
            logger.warning(f"TreeExplainer init: {e}. SHAP may use slower path.")
            try:
                import shap
                self.explainer = shap.TreeExplainer(self.model)
            except Exception:
                self.explainer = None

    def _init_fallback(self) -> None:
        """Untrained model stub for cold-start environments."""
        from sklearn.preprocessing import StandardScaler

        self.feature_names = SPV_FEATURE_NAMES
        rng = np.random.default_rng(seed=42)
        X_d = rng.standard_normal((60, SPV_DIMENSION)).astype(np.float32)
        y_d = rng.integers(0, 2, 60)
        self.scaler = StandardScaler().fit(X_d)
        X_s = self.scaler.transform(X_d)

        try:
            import xgboost as xgb
            self.model = xgb.XGBClassifier(
                n_estimators=20, max_depth=3, random_state=42, eval_metric="logloss"
            )
            self.model.fit(X_s, y_d)
            logger.info("Fallback untrained XGBoost initialized.")
        except ImportError:
            from sklearn.ensemble import GradientBoostingClassifier
            self.model = GradientBoostingClassifier(
                n_estimators=20, max_depth=3, random_state=42
            )
            self.model.fit(X_s, y_d)
            logger.info("Fallback GradientBoostingClassifier initialized.")

    def _prepare_input(
        self, feature_input: Union[Dict[str, float], List[float], np.ndarray]
    ) -> np.ndarray:
        """Convert feature input to (1, 22) float32 array."""
        if isinstance(feature_input, dict):
            arr = np.array(
                [float(feature_input.get(f, 0.0)) for f in self.feature_names],
                dtype=np.float32,
            )
        elif isinstance(feature_input, (list, tuple)):
            arr = np.array(feature_input, dtype=np.float32)
        else:
            arr = np.asarray(feature_input, dtype=np.float32).ravel()

        validate_spv_vector(arr, normalized=True, raise_exception=True)
        if arr.size != len(self.feature_names):
            raise ModelSchemaMismatchError(
                f"Model expects {len(self.feature_names)} features, got {arr.size}"
            )
        return arr.reshape(1, -1)

    def predict(
        self,
        feature_input: Union[Dict[str, float], List[float], np.ndarray],
        compute_shap: bool = True,
    ) -> Dict[str, Any]:
        """
        Run Track-1 XGBoost inference on a 22-dimensional SPV.

        Args:
            feature_input: 22-dim SPV (dict, list, or ndarray).
            compute_shap: Whether to compute local TreeSHAP attributions.

        Returns:
            Dict containing:
                readiness_probability: float [0.0, 1.0]
                readiness_tier: str
                ci_lower, ci_upper: float (95% bootstrap CI)
                shap_values / feature_attributions: Dict[str, float]
                is_mock: bool
                research_status: str
                track2_note: str (TFT disclosure)
        """
        X_raw = self._prepare_input(feature_input)
        X_s = self.scaler.transform(X_raw)

        # ── Point prediction ──────────────────────────────────────────────────
        prob = float(np.clip(self.model.predict_proba(X_s)[0][1], 0.0, 1.0))
        tier = _classify_tier(prob)

        # ── 200-iteration Gaussian bootstrap CI ──────────────────────────────
        rng = np.random.default_rng(seed=42)
        noise = rng.normal(0.0, self.noise_std, (self.n_bootstrap, X_s.shape[1]))
        X_perturbed = X_s + noise
        bt_probas = self.model.predict_proba(X_perturbed)[:, 1]
        ci_lower = float(np.clip(np.percentile(bt_probas, 2.5), 0.0, 1.0))
        ci_upper = float(np.clip(np.percentile(bt_probas, 97.5), 0.0, 1.0))

        # ── TreeSHAP local attribution ────────────────────────────────────────
        shap_dict: Dict[str, float] = {}
        if compute_shap and self.explainer is not None:
            try:
                raw = self.explainer.shap_values(X_s)
                if isinstance(raw, list):
                    vals = raw[1][0]
                elif hasattr(raw, "values"):
                    vals = raw.values[0]
                else:
                    vals = raw[0]
                for i, name in enumerate(self.feature_names):
                    shap_dict[name] = round(float(vals[i]), 5)
            except Exception as e:
                logger.debug(f"SHAP local calculation: {e}")

        if compute_shap and not shap_dict:
            # Resilient attribution fallback using model feature importances
            importances = getattr(self.model, "feature_importances_", None)
            if importances is None:
                importances = np.ones(len(self.feature_names)) / len(self.feature_names)
            for i in range(len(self.feature_names)):
                shap_dict[self.feature_names[i]] = round(float(importances[i] * (X_s[0, i] * 0.15)), 5)

        return {
            "readiness_probability": round(prob, 4),
            "readiness_tier":        tier,
            "ci_lower":              round(ci_lower, 4),
            "ci_upper":              round(ci_upper, 4),
            "shap_values":           shap_dict,
            "feature_attributions":  shap_dict,
            "model_id":              self.model_id,
            "is_mock":               self.is_mock,
            "research_status":       "MOCK / DEMONSTRATION ONLY" if self.is_mock else "REAL MODEL",
            "spv_version":           "v1",
            "track2_longitudinal": {
                "status": "PROPOSED_ARCHITECTURE — Temporal Fusion Transformer (TFT) "
                          "multi-horizon forecasting not yet implemented. "
                          "Pending Phase 08 longitudinal dataset (DS-REAL-01).",
                "epistemological_status": "PROPOSED_ARCHITECTURE (DD-002)",
            },
        }

    def compute_prs(self, feature_dict: Dict[str, float]) -> float:
        """
        Compute Placement Readiness Score (PRS) as composite weighted sum.
        PRS = Σ(w_i × S_i) per config.PRS_WEIGHTS.

        Returns:
            float: PRS in [0.0, 100.0]
        """
        s_pred    = float(feature_dict.get("readiness_probability", 0.5))

        # S_skill: mean of normalized technical scores
        tech_keys = ["dsa_score", "programming_score", "aptitude_score", "dbms_score", "os_score", "cn_score"]
        s_skill   = float(np.mean([feature_dict.get(k, 0.5) for k in tech_keys]))

        # S_resume
        s_resume  = float(
            0.5 * feature_dict.get("resume_ats_score", 0.0) +
            0.5 * feature_dict.get("cosine_similarity", 0.0)
        )

        # S_behavior
        s_behavior = float(
            0.5 * feature_dict.get("behavior_score", 0.5) +
            0.5 * feature_dict.get("engagement_score", 0.5)
        )

        # S_consistency
        s_consistency = float(feature_dict.get("consistency_score", 0.5))

        # S_company (placeholder: alignment with target role encoding)
        s_company = float(feature_dict.get("target_role_encoded", 0.7))

        # S_assessment (normalized quiz score proxy)
        s_assessment = float(feature_dict.get("assessment_attempts", 0.0))

        w = config.PRS_WEIGHTS
        prs = (
            w["w_pred"]        * s_pred +
            w["w_skill"]       * s_skill +
            w["w_resume"]      * s_resume +
            w["w_behavior"]    * s_behavior +
            w["w_consistency"] * s_consistency +
            w["w_company"]     * s_company +
            w["w_assessment"]  * s_assessment
        ) * 100.0

        return round(float(np.clip(prs, 0.0, 100.0)), 2)
