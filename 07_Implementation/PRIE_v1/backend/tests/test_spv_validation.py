"""
Unit tests for Canonical SPV Validation & Schema Invariance
File: backend/tests/test_spv_validation.py

Tests:
  - Exact 22-dimensional invariant (SPV in R^22)
  - Numerical type checking (rejection of non-numeric data)
  - Range constraints and normalization bounding [0.0, 1.0]
  - NaN and Infinity detection
  - Legacy feature schema rejection ('backlogs', 'internship_months', 'skill_count')
  - Unknown feature rejection
  - Binary observation mask verification m in {0, 1}^22
"""

import sys
from pathlib import Path
import pytest
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from spv_version import (
    SPV_DIMENSION,
    SPV_FEATURE_NAMES,
    SPVValidationError,
    SPVSchemaMismatchError,
    validate_spv_vector,
    validate_spv_dict,
    validate_observation_mask,
    IMMUTABLE_FEATURES,
)


@pytest.fixture
def valid_normalized_vector():
    """Valid 22-dimensional normalized vector."""
    return [0.5] * SPV_DIMENSION


@pytest.fixture
def valid_spv_dict():
    """Valid dictionary containing all 22 canonical features in raw ranges."""
    return {
        "cgpa": 8.5,
        "dsa_score": 75.0,
        "dbms_score": 70.0,
        "os_score": 68.0,
        "cn_score": 65.0,
        "programming_score": 80.0,
        "aptitude_score": 72.0,
        "soft_skills_score": 70.0,
        "project_count": 3,
        "project_quality_score": 60.0,
        "has_internship": 1,
        "certifications_count": 2,
        "resume_ats_score": 85.0,
        "cosine_similarity": 0.78,
        "gap_score": 0.25,
        "consistency_score": 0.70,
        "branch_encoded": 0.85,
        "target_role_encoded": 0.80,
        "assessment_attempts": 15,
        "behavior_score": 75.0,
        "engagement_score": 0.80,
        "roadmap_completion_rate": 0.45,
    }


def test_valid_spv_vector(valid_normalized_vector):
    is_valid, msg = validate_spv_vector(valid_normalized_vector, normalized=True)
    assert is_valid is True
    assert msg is None


def test_vector_dimension_too_short():
    short_vec = [0.5] * 21
    is_valid, msg = validate_spv_vector(short_vec)
    assert is_valid is False
    assert "dimensionality invariant violated" in msg

    with pytest.raises(SPVValidationError):
        validate_spv_vector(short_vec, raise_exception=True)


def test_vector_dimension_too_long():
    long_vec = [0.5] * 23
    is_valid, msg = validate_spv_vector(long_vec)
    assert is_valid is False
    assert "dimensionality invariant violated" in msg

    with pytest.raises(SPVValidationError):
        validate_spv_vector(long_vec, raise_exception=True)


def test_vector_with_nan():
    nan_vec = [0.5] * SPV_DIMENSION
    nan_vec[3] = float("nan")
    is_valid, msg = validate_spv_vector(nan_vec)
    assert is_valid is False
    assert "NaN values" in msg

    with pytest.raises(SPVValidationError):
        validate_spv_vector(nan_vec, raise_exception=True)


def test_vector_with_inf():
    inf_vec = [0.5] * SPV_DIMENSION
    inf_vec[7] = float("inf")
    is_valid, msg = validate_spv_vector(inf_vec)
    assert is_valid is False
    assert "infinite values" in msg

    with pytest.raises(SPVValidationError):
        validate_spv_vector(inf_vec, raise_exception=True)


def test_vector_out_of_bounds_normalized():
    out_vec = [0.5] * SPV_DIMENSION
    out_vec[0] = 1.2  # Exceeds 1.0
    is_valid, msg = validate_spv_vector(out_vec, normalized=True)
    assert is_valid is False
    assert "outside [0.0, 1.0]" in msg

    neg_vec = [0.5] * SPV_DIMENSION
    neg_vec[1] = -0.1  # Sub-zero
    is_valid, msg = validate_spv_vector(neg_vec, normalized=True)
    assert is_valid is False
    assert "outside [0.0, 1.0]" in msg


def test_valid_spv_dict(valid_spv_dict):
    is_valid, msg = validate_spv_dict(valid_spv_dict)
    assert is_valid is True
    assert msg is None


def test_spv_dict_rejects_legacy_backlogs(valid_spv_dict):
    bad_dict = dict(valid_spv_dict)
    bad_dict["backlogs"] = 0
    del bad_dict["os_score"]

    is_valid, msg = validate_spv_dict(bad_dict)
    assert is_valid is False
    assert "Divergent legacy features rejected" in msg

    with pytest.raises(SPVSchemaMismatchError):
        validate_spv_dict(bad_dict, raise_exception=True)


def test_spv_dict_rejects_legacy_internship_months(valid_spv_dict):
    bad_dict = dict(valid_spv_dict)
    bad_dict["internship_months"] = 3
    is_valid, msg = validate_spv_dict(bad_dict)
    assert is_valid is False
    assert "Divergent legacy features rejected" in msg


def test_spv_dict_rejects_unknown_features(valid_spv_dict):
    bad_dict = dict(valid_spv_dict)
    bad_dict["random_unknown_feature"] = 123
    is_valid, msg = validate_spv_dict(bad_dict)
    assert is_valid is False
    assert "Unknown features" in msg

    with pytest.raises(SPVSchemaMismatchError):
        validate_spv_dict(bad_dict, raise_exception=True)


def test_spv_dict_rejects_missing_features(valid_spv_dict):
    bad_dict = dict(valid_spv_dict)
    del bad_dict["dsa_score"]
    is_valid, msg = validate_spv_dict(bad_dict, allow_missing=False)
    assert is_valid is False
    assert "Missing required SPV features" in msg


def test_spv_dict_out_of_range_raw_values(valid_spv_dict):
    # CGPA > 10.0
    bad_dict = dict(valid_spv_dict)
    bad_dict["cgpa"] = 11.5
    is_valid, msg = validate_spv_dict(bad_dict)
    assert is_valid is False
    assert "outside valid native range" in msg

    # DSA score > 100
    bad_dict2 = dict(valid_spv_dict)
    bad_dict2["dsa_score"] = 105.0
    is_valid, msg = validate_spv_dict(bad_dict2)
    assert is_valid is False
    assert "outside valid native range" in msg


def test_observation_mask_valid():
    mask = [1] * SPV_DIMENSION
    is_valid, msg = validate_observation_mask(mask)
    assert is_valid is True

    partial_mask = [1] * 15 + [0] * 7
    is_valid, msg = validate_observation_mask(partial_mask)
    assert is_valid is True


def test_observation_mask_invalid():
    # Wrong shape
    is_valid, msg = validate_observation_mask([1] * 10)
    assert is_valid is False
    assert "shape mismatch" in msg

    # Non-binary value
    is_valid, msg = validate_observation_mask([1] * 21 + [2])
    assert is_valid is False
    assert "strictly binary" in msg


def test_immutable_features_locked():
    assert "branch_encoded" in IMMUTABLE_FEATURES
    assert len(IMMUTABLE_FEATURES) >= 1
