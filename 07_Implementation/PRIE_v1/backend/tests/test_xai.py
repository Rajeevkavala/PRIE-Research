"""
Unit tests for Module M07: Prescriptive XAI Engine.
Verifies TreeSHAP attribution, DiCE constrained counterfactual recourse,
immutable feature enforcement (F17: branch_encoded), and sparsity constraints.
"""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from spv_version import SPV_FEATURE_NAMES, SPV_DIMENSION, IMMUTABLE_FEATURES
from modules.m06_placement_predictor import PlacementPredictor
from modules.m07_prescriptive_xai import PrescriptiveXAIEngine


@pytest.fixture
def predictor():
    return PlacementPredictor()


@pytest.fixture
def low_readiness_spv():
    """SPV vector representing an at-risk student needing recourse."""
    return np.array([
        0.55,  # F01: cgpa (5.5/10)
        0.35,  # F02: dsa_score (35/100)
        0.40,  # F03: dbms_score (40/100)
        0.35,  # F04: os_score (35/100)
        0.30,  # F05: cn_score (30/100)
        0.40,  # F06: programming_score (40/100)
        0.45,  # F07: aptitude_score (45/100)
        0.50,  # F08: soft_skills_score (50/100)
        0.10,  # F09: project_count (1/10)
        0.30,  # F10: project_quality_score (30/100)
        0.00,  # F11: has_internship (0)
        0.00,  # F12: certifications_count (0)
        0.40,  # F13: resume_ats_score (40/100)
        0.35,  # F14: cosine_similarity (0.35)
        0.65,  # F15: gap_score (0.65)
        0.40,  # F16: consistency_score (0.40)
        0.75,  # F17: branch_encoded (0.75) -> IMMUTABLE
        0.75,  # F18: target_role_encoded (0.75)
        0.10,  # F19: assessment_attempts (10/100)
        0.45,  # F20: behavior_score (45/100)
        0.40,  # F21: engagement_score (0.40)
        0.15,  # F22: roadmap_completion_rate (0.15)
    ], dtype=np.float32)


def test_shap_explanation(predictor, low_readiness_spv):
    """Test TreeSHAP attribution output and top barriers."""
    engine = PrescriptiveXAIEngine(predictor=predictor)
    explanation = engine.explain_prediction(low_readiness_spv)

    assert "attribution_table" in explanation
    assert len(explanation["attribution_table"]) == SPV_DIMENSION
    assert "top_barriers" in explanation
    assert "top_strengths" in explanation
    assert explanation["epistemological_status"].startswith("ESTABLISHED_BY_RESEARCH")

    # Verify immutable feature is flagged
    branch_attr = next(a for a in explanation["attribution_table"] if a["feature"] == "branch_encoded")
    assert branch_attr["is_immutable"] is True


def test_dice_counterfactual_recourse(predictor, low_readiness_spv):
    """Verify counterfactual recourse obeys all constraints."""
    engine = PrescriptiveXAIEngine(predictor=predictor)
    recourse = engine.generate_counterfactual(
        low_readiness_spv,
        target_prob=0.75,
        max_features_changed=3,
    )

    assert recourse["status"] in ("VALID_RECOURSE_GENERATED", "STUDENT_ALREADY_MEETS_TARGET")
    assert recourse["sparsity"] <= 3

    # Check that immutable feature F17 was NOT altered
    branch_idx = SPV_FEATURE_NAMES.index("branch_encoded")
    orig_branch = float(low_readiness_spv[branch_idx])
    cf_branch = float(recourse["counterfactual_vector"][branch_idx])
    assert np.isclose(orig_branch, cf_branch, atol=1e-5), "F17 branch_encoded MUST remain invariant!"

    # Check feasibility flags
    assert recourse["feasibility_checks"]["immutable_features_unchanged"] is True
    assert recourse["feasibility_checks"]["bounds_respected"] is True
    assert recourse["feasibility_checks"]["monotonicity_respected"] is True

    # Check that distance is non-negative
    assert recourse["distance_l1"] >= 0.0
    assert recourse["distance_l2"] >= 0.0


def test_prescriptive_narrative_generation(predictor, low_readiness_spv):
    """Verify natural-language narrative synthesizes predictions and recourse."""
    engine = PrescriptiveXAIEngine(predictor=predictor)
    pred_res = predictor.predict(low_readiness_spv)
    shap_res = engine.explain_prediction(low_readiness_spv)
    recourse_res = engine.generate_counterfactual(low_readiness_spv, target_prob=0.75)

    narrative = engine.generate_narrative(pred_res, shap_res, recourse_res)
    assert isinstance(narrative, str)
    assert len(narrative) > 50
    assert "Placement Readiness Score" in narrative
