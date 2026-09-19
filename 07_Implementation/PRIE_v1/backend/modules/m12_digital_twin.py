"""
PRIE v1 — Module M12: Digital Twin & What-If Forward Simulation Engine
File: backend/modules/m12_digital_twin.py

MODULE: M12 — Digital Twin & What-If Sensitivity Simulator
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (What-If Feature Perturbation Simulation, DD-012)
RESEARCH_GAP: RG5 (Black-box feedback lacking interactive recourse exploration)
RESEARCH_OBJECTIVE: RO5 (Prescriptive Explainability & Forward Scenario Analysis)
TRACEABILITY: Paper19, Paper20, Paper30, Paper31; DD-012

Conceptual Pipeline:
  Current SPV -> Feature Perturbation (delta) -> Forward Model Inference ->
  Readiness Response Delta -> Marginal Sensitivity Gradient Matrix

CRITICAL RESEARCH RULE:
  Clearly labeled as: SIMULATION — not actual future prediction.
  F17 (branch_encoded) is strictly IMMUTABLE.
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from spv_version import SPV_FEATURE_NAMES, SPV_DIMENSION, IMMUTABLE_FEATURES, validate_spv_vector
from database import db_manager, queries

logger = logging.getLogger("PRIE.M12.DigitalTwin")


class DigitalTwin:
    """
    M12: Digital Twin What-If Forward Simulation & Sensitivity Engine.
    Enables counterfactual exploration by perturbing SPV features and observing model response.
    """

    def __init__(self, predictor: Optional[Any] = None, db_path: Optional[Path] = None) -> None:
        self.predictor = predictor
        self.db_path = db_path

    def get_twin_state(self, student_id: int) -> Dict[str, Any]:
        """Return the most recent SPV snapshot as the active digital twin baseline."""
        row = db_manager.dict_row(
            db_manager.execute_single(
                queries.GET_LATEST_SPV_SNAPSHOT, (student_id,), self.db_path
            )
        )
        if not row:
            return {"status": "NO_SNAPSHOT", "student_id": student_id}

        feature_vector = [
            float(row.get(f"f{str(i+1).zfill(2)}_{SPV_FEATURE_NAMES[i]}", 0.0))
            for i in range(len(SPV_FEATURE_NAMES))
        ]

        return {
            "student_id": student_id,
            "spv_version": row.get("spv_version", "v1"),
            "computed_at": row.get("computed_at"),
            "feature_vector": feature_vector,
            "feature_names": SPV_FEATURE_NAMES,
            "confidence_mask": json.loads(row.get("confidence_mask_json", "[]")),
            "readiness_probability": row.get("readiness_probability"),
            "readiness_tier": row.get("readiness_tier"),
            "twin_status": "SYNCHRONIZED_WITH_DATABASE",
        }

    def simulate_what_if(
        self,
        base_spv: np.ndarray,
        perturbations: Dict[str, float],
    ) -> Dict[str, Any]:
        """
        Execute forward what-if simulation by applying feature perturbations.

        Args:
            base_spv: Current 22D normalized SPV vector.
            perturbations: Dict mapping feature name to delta change (e.g. {'dsa_score': +0.15}).

        Returns:
            Simulation result dict comparing baseline to simulated outcome.
        """
        validate_spv_vector(base_spv)

        # 1. Strict Immutability Check
        for imm_feat in IMMUTABLE_FEATURES:
            if imm_feat in perturbations and abs(perturbations[imm_feat]) > 1e-6:
                raise ValueError(
                    f"Immutability constraint violated: Feature '{imm_feat}' is strictly locked "
                    f"and cannot be modified in What-If simulations."
                )

        # 2. Apply Perturbations
        sim_spv = base_spv.copy()
        delta_summary = {}

        for feat_name, delta in perturbations.items():
            if feat_name in SPV_FEATURE_NAMES:
                idx = SPV_FEATURE_NAMES.index(feat_name)
                curr_val = float(base_spv[idx])
                # Clip to valid normalized range [0.0, 1.0]
                new_val = float(np.clip(curr_val + delta, 0.0, 1.0))
                sim_spv[idx] = new_val
                delta_summary[feat_name] = {
                    "original": round(curr_val, 3),
                    "simulated": round(new_val, 3),
                    "delta": round(new_val - curr_val, 3),
                }

        # 3. Model Inference on Baseline and Simulated Points
        base_prob = 0.50
        base_tier = "Needs Remediation"
        sim_prob = 0.50
        sim_tier = "Needs Remediation"

        if self.predictor is not None:
            base_res = self.predictor.predict(base_spv)
            base_prob = base_res["readiness_probability"]
            base_tier = base_res["readiness_tier"]

            sim_res = self.predictor.predict(sim_spv)
            sim_prob = sim_res["readiness_probability"]
            sim_tier = sim_res["readiness_tier"]

        prob_delta = round(sim_prob - base_prob, 4)

        return {
            "simulation_type": "WHAT_IF_FORWARD_PERTURBATION",
            "baseline": {
                "readiness_probability": round(base_prob, 4),
                "readiness_tier": base_tier,
            },
            "simulated": {
                "readiness_probability": round(sim_prob, 4),
                "readiness_tier": sim_tier,
            },
            "readiness_probability_delta": prob_delta,
            "perturbation_breakdown": delta_summary,
            "epistemological_status": "ESTABLISHED_BY_RESEARCH (What-If Simulation per DD-012)",
            "scientific_integrity_disclaimer": (
                "SIMULATION ONLY — Forward mathematical projection based on statistical model parameters. "
                "Does NOT guarantee actual future student placement outcomes."
            ),
        }

    def compute_sensitivity_matrix(
        self,
        base_spv: np.ndarray,
        step_size: float = 0.10,
    ) -> List[Dict[str, Any]]:
        """
        Compute marginal sensitivity gradient for all actionable features:
          gradient_i = (P(x + step * e_i) - P(x)) / step
        Ranks actionable features by leverage for this specific student profile.
        """
        validate_spv_vector(base_spv)

        base_prob = 0.50
        if self.predictor is not None:
            base_prob = self.predictor.predict(base_spv)["readiness_probability"]

        sensitivities = []
        for i, feat_name in enumerate(SPV_FEATURE_NAMES):
            if feat_name in IMMUTABLE_FEATURES:
                continue

            curr_val = float(base_spv[i])
            if curr_val >= 0.99:
                continue  # already at ceiling

            # Perturb forward
            perturbed_spv = base_spv.copy()
            new_val = min(1.0, curr_val + step_size)
            actual_step = new_val - curr_val
            if actual_step < 1e-4:
                continue
            perturbed_spv[i] = new_val

            sim_prob = base_prob
            if self.predictor is not None:
                sim_prob = self.predictor.predict(perturbed_spv)["readiness_probability"]

            marginal_gain = sim_prob - base_prob
            sensitivity_rate = marginal_gain / actual_step

            sensitivities.append({
                "feature": feat_name,
                "current_value": round(curr_val, 3),
                "simulated_value": round(new_val, 3),
                "marginal_readiness_gain": round(marginal_gain, 4),
                "sensitivity_gradient": round(sensitivity_rate, 4),
            })

        sensitivities.sort(key=lambda x: x["marginal_readiness_gain"], reverse=True)
        return sensitivities
