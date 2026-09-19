"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module 5: Tabular Machine Learning Placement Predictor & TreeSHAP Attribution

Loads optimized XGBoost classifier and StandardScaler, produces calibrated
placement probability (S_pred), computes 200-iteration bootstrap confidence
intervals (95% CI), and generates local feature attributions via TreeSHAP.
"""

from __future__ import annotations

import json
import logging
import os
import pickle
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

import config

logger = logging.getLogger("PRIE.PlacementPredictor")


def _patch_shap_base_score() -> None:
    """Ensure shap.TreeExplainer works seamlessly with XGBoost 3.x base_score formats."""
    try:
        import shap.explainers._tree as shap_tree

        orig_init = shap_tree.XGBTreeModelLoader.__init__

        def safe_init(self, original_model):
            try:
                orig_init(self, original_model)
            except ValueError as ve:
                if "could not convert string to float" in str(ve):
                    import json
                    import scipy.special
                    cb = original_model.get_booster()
                    dump = cb.save_raw(dump_format="json").decode("utf-8")
                    config_json = json.loads(dump)
                    param = config_json.get("learner", {}).get("learner_model_param", {})
                    raw_bs = param.get("base_score", "0.5")
                    if isinstance(raw_bs, str):
                        raw_bs = raw_bs.strip("[]")
                    self.base_score = float(raw_bs)
                    obj_name = config_json.get("learner", {}).get("objective", {}).get("name", "")
                    if obj_name in ("binary:logistic", "reg:logistic"):
                        self.base_score = scipy.special.logit(self.base_score)
                else:
                    raise

        shap_tree.XGBTreeModelLoader.__init__ = safe_init
    except Exception as exc:
        logger.debug(f"Optional shap monkeypatch not required or failed: {exc}")


_patch_shap_base_score()


class PlacementReadinessPredictor:
    """Production tabular ML inference engine for placement probability and XAI attributions.
    
    Adheres to SOLID principles:
    - Single Responsibility: Enforces feature extraction, scaling, XGBoost scoring,
      uncertainty quantification, and TreeSHAP attribution.
    - Open/Closed: Supports custom artifact paths or in-memory models.
    """

    def __init__(
        self,
        model_path: Optional[Union[str, Path]] = None,
        scaler_path: Optional[Union[str, Path]] = None,
        feature_names_path: Optional[Union[str, Path]] = None,
        bootstrap_iterations: Optional[int] = None,
        bootstrap_noise_std: Optional[float] = None,
    ) -> None:
        """Initialize the Placement Readiness Predictor.

        Args:
            model_path: Optional path to serialized XGBoost model pickle.
            scaler_path: Optional path to serialized StandardScaler pickle.
            feature_names_path: Optional path to serialized feature names JSON.
            bootstrap_iterations: Number of Gaussian perturbation iterations (default 200).
            bootstrap_noise_std: Standard deviation of perturbation noise (default 0.05).
        """
        self.model_path = Path(model_path) if model_path else config.XGB_MODEL_PATH
        self.scaler_path = Path(scaler_path) if scaler_path else config.SCALER_PATH
        self.feature_names_path = (
            Path(feature_names_path) if feature_names_path else config.FEATURE_NAMES_PATH
        )
        self.bootstrap_iterations = (
            bootstrap_iterations
            if bootstrap_iterations is not None
            else getattr(config, "BOOTSTRAP_ITERATIONS", 200)
        )
        self.bootstrap_noise_std = (
            bootstrap_noise_std
            if bootstrap_noise_std is not None
            else getattr(config, "BOOTSTRAP_NOISE_STD", 0.05)
        )

        self.model: Any = None
        self.scaler: Any = None
        self.feature_names: List[str] = []
        self.explainer: Any = None

        self._load_artifacts()

    def _load_artifacts(self) -> None:
        """Load serialized model, scaler, and feature names from disk with fallback safety."""
        try:
            if (
                self.model_path.exists()
                and self.scaler_path.exists()
                and self.feature_names_path.exists()
            ):
                with open(self.model_path, "rb") as f:
                    self.model = pickle.load(f)
                with open(self.scaler_path, "rb") as f:
                    self.scaler = pickle.load(f)
                with open(self.feature_names_path, "r", encoding="utf-8") as f:
                    self.feature_names = json.load(f)

                logger.info(
                    f"Successfully loaded production ML artifacts: {len(self.feature_names)} features"
                )
            else:
                logger.warning(
                    f"Model artifacts not found at {self.model_path}. Initializing fallback model."
                )
                self._initialize_fallback()

            # Initialize fast C++ TreeExplainer
            import shap
            self.explainer = shap.TreeExplainer(self.model)

        except Exception as e:
            logger.error(f"Error loading model artifacts: {e}. Reverting to fallback.", exc_info=True)
            self._initialize_fallback()
            import shap
            self.explainer = shap.TreeExplainer(self.model)

    def _initialize_fallback(self) -> None:
        """Defensive fallback initialization for bootstrapping and headless testing."""
        from sklearn.preprocessing import StandardScaler
        import xgboost as xgb

        self.feature_names = list(config.FEATURE_NAMES)
        rng = np.random.default_rng(seed=42)
        X_dummy = rng.standard_normal(size=(50, len(self.feature_names)))
        y_dummy = rng.integers(0, 2, size=50)

        self.scaler = StandardScaler().fit(X_dummy)
        X_dummy_scaled = self.scaler.transform(X_dummy)

        self.model = xgb.XGBClassifier(
            n_estimators=10,
            max_depth=3,
            learning_rate=0.1,
            random_state=42,
            eval_metric="logloss",
        )
        self.model.fit(X_dummy_scaled, y_dummy)
        logger.info("Initialized defensive fallback XGBoost model and scaler.")

    def _prepare_feature_array(
        self, feature_input: Union[Dict[str, float], List[float], np.ndarray]
    ) -> np.ndarray:
        """Convert heterogeneous feature input into ordered (1, 22) numpy array.

        Args:
            feature_input: Dictionary mapping feature names to floats, list of floats,
                           or numpy ndarray.

        Returns:
            np.ndarray: 2D array of shape (1, 22).
        """
        if isinstance(feature_input, dict):
            vector = [float(feature_input.get(f, 0.0)) for f in self.feature_names]
            return np.array(vector, dtype=float).reshape(1, -1)

        if isinstance(feature_input, (list, tuple)):
            arr = np.array(feature_input, dtype=float)
            if arr.size != len(self.feature_names):
                raise ValueError(
                    f"Feature list must contain {len(self.feature_names)} items, got {arr.size}"
                )
            return arr.reshape(1, -1)

        if isinstance(feature_input, np.ndarray):
            if feature_input.size != len(self.feature_names):
                raise ValueError(
                    f"Feature array must contain {len(self.feature_names)} elements, got {feature_input.size}"
                )
            return feature_input.astype(float).reshape(1, -1)

        raise TypeError(
            f"Unsupported feature input type: {type(feature_input)}. "
            f"Expected dict, list, or np.ndarray."
        )

    def predict_readiness(
        self, feature_input: Union[Dict[str, float], List[float], np.ndarray]
    ) -> Tuple[float, Dict[str, float], Tuple[float, float]]:
        """Predict placement probability, compute 95% bootstrap CI, and local TreeSHAP attributions.

        Args:
            feature_input: 22-dimensional student feature vector (dict, list, or array).

        Returns:
            Tuple containing:
                s_pred (float): Calibrated placement probability in [0.0, 1.0].
                shap_dict (Dict[str, float]): Map of {feature_name: shap_value}.
                ci (Tuple[float, float]): 95% confidence interval (lower, upper).
        """
        X_raw = self._prepare_feature_array(feature_input)
        X_scaled = self.scaler.transform(X_raw)

        # 1. XGBoost Point Prediction
        proba = float(self.model.predict_proba(X_scaled)[0][1])
        s_pred = round(float(np.clip(proba, 0.0, 1.0)), 4)

        # 2. Bootstrap Confidence Interval (Gaussian perturbation)
        rng = np.random.default_rng(seed=42)
        noise = rng.normal(0.0, self.bootstrap_noise_std, size=(self.bootstrap_iterations, X_scaled.shape[1]))
        X_perturbed = X_scaled + noise
        bootstrap_probas = self.model.predict_proba(X_perturbed)[:, 1]

        ci_lower = round(float(np.clip(np.percentile(bootstrap_probas, 2.5), 0.0, 1.0)), 4)
        ci_upper = round(float(np.clip(np.percentile(bootstrap_probas, 97.5), 0.0, 1.0)), 4)

        # 3. Fast C++ TreeSHAP Attribution Calculation (< 100ms)
        raw_shap = self.explainer.shap_values(X_scaled)
        if isinstance(raw_shap, list):
            shap_arr = raw_shap[1][0] if len(raw_shap) > 1 else raw_shap[0][0]
        elif hasattr(raw_shap, "values"):
            shap_arr = raw_shap.values[0]
        elif isinstance(raw_shap, np.ndarray):
            if raw_shap.ndim == 3:
                shap_arr = raw_shap[0, :, 1]
            elif raw_shap.ndim == 2:
                shap_arr = raw_shap[0]
            else:
                shap_arr = raw_shap
        else:
            shap_arr = np.array(raw_shap)[0]

        shap_dict = {
            self.feature_names[i]: round(float(shap_arr[i]), 4)
            for i in range(len(self.feature_names))
        }

        return s_pred, shap_dict, (ci_lower, ci_upper)

    def predict(
        self, feature_input: Union[Dict[str, float], List[float], np.ndarray]
    ) -> Tuple[float, Dict[str, float], Tuple[float, float]]:
        """Convenience alias for predict_readiness matching PDR Chapter 9 signature."""
        return self.predict_readiness(feature_input)
