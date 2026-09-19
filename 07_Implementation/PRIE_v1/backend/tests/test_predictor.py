"""
Unit tests for M06 Placement Predictor.
Tests strict SPV validation, real artifact loading, error modes, and calibration bounds.
"""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from spv_version import (
    SPV_FEATURE_NAMES,
    SPV_DIMENSION,
    SPVValidationError,
    SPVSchemaMismatchError,
)
from modules.m06_placement_predictor import (
    PlacementPredictor,
    ModelArtifactNotFoundError,
    ModelLoadError,
    PredictionInferenceError,
)


@pytest.fixture
def valid_spv_vector():
    """Create a canonical 22-dimensional valid normalized SPV vector."""
    return np.array([
        0.82,  # F01: cgpa (8.2/10)
        0.75,  # F02: dsa_score (75/100)
        0.80,  # F03: dbms_score (80/100)
        0.70,  # F04: os_score (70/100)
        0.65,  # F05: cn_score (65/100)
        0.85,  # F06: programming_score (85/100)
        0.78,  # F07: aptitude_score (78/100)
        0.80,  # F08: soft_skills_score (80/100)
        0.30,  # F09: project_count (3/10)
        0.75,  # F10: project_quality_score (75/100)
        1.00,  # F11: has_internship (1.0)
        0.40,  # F12: certifications_count (2/5)
        0.82,  # F13: resume_ats_score (82/100)
        0.78,  # F14: cosine_similarity (0.78)
        0.25,  # F15: gap_score (0.25)
        0.88,  # F16: consistency_score (0.88)
        0.75,  # F17: branch_encoded (0.75)
        0.80,  # F18: target_role_encoded (0.80)
        0.35,  # F19: assessment_attempts (35/100)
        0.75,  # F20: behavior_score (75/100)
        0.82,  # F21: engagement_score (0.82)
        0.70,  # F22: roadmap_completion_rate (0.70)
    ], dtype=np.float32)


def test_predictor_valid_prediction(valid_spv_vector):
    """Test standard prediction with valid 22D vector."""
    predictor = PlacementPredictor()
    result = predictor.predict(valid_spv_vector)

    assert "readiness_probability" in result
    assert 0.0 <= result["readiness_probability"] <= 1.0
    assert result["readiness_tier"] in ["At-Risk", "Needs Remediation", "Placement-Ready", "Advanced Readiness"]
    assert "ci_lower" in result
    assert "ci_upper" in result
    assert result["ci_lower"] <= result["readiness_probability"] <= result["ci_upper"]
    assert "feature_attributions" in result
    assert "research_status" in result


def test_predictor_rejects_wrong_dimension():
    """Predictor must strictly reject non-22D vectors."""
    predictor = PlacementPredictor()
    wrong_vector = np.array([0.5] * 20, dtype=np.float32)

    with pytest.raises(SPVValidationError):
        predictor.predict(wrong_vector)


def test_predictor_rejects_out_of_bounds():
    """Predictor must reject features outside [0.0, 1.0]."""
    predictor = PlacementPredictor()
    invalid_vector = np.array([0.5] * 22, dtype=np.float32)
    invalid_vector[0] = 1.5  # CGPA normalized above 1.0

    with pytest.raises(SPVValidationError):
        predictor.predict(invalid_vector)


def test_predictor_rejects_nan_values():
    """Predictor must reject NaN values in SPV."""
    predictor = PlacementPredictor()
    invalid_vector = np.array([0.5] * 22, dtype=np.float32)
    invalid_vector[5] = np.nan

    with pytest.raises(SPVValidationError):
        predictor.predict(invalid_vector)


def test_research_mode_disallows_dummy_fallback(monkeypatch, valid_spv_vector):
    """In research mode, missing artifacts must raise ModelArtifactNotFoundError, not fallback."""
    fake_model_path = Path("models/non_existent_model.pkl")
    fake_scaler_path = Path("models/non_existent_scaler.pkl")
    fake_features_path = Path("models/non_existent_features.json")

    # Simulate research mode
    monkeypatch.setattr(config, "ALLOW_DUMMY_MODELS", False)
    monkeypatch.setattr(config, "IS_RESEARCH_MODE", True)

    with pytest.raises(ModelArtifactNotFoundError):
        PlacementPredictor(
            model_path=fake_model_path,
            scaler_path=fake_scaler_path,
            feature_names_path=fake_features_path,
        )
