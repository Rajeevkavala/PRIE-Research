"""
Unit tests for Module M11 (Company Matcher) and Module M12 (Digital Twin Simulator).
Tests multi-criteria company readiness evaluation, what-if forward simulation,
immutability constraints on F17, and marginal sensitivity matrix calculations.
"""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from spv_version import SPV_FEATURE_NAMES, IMMUTABLE_FEATURES
from modules.m06_placement_predictor import PlacementPredictor
from modules.m11_company_matcher import CompanyBenchmarkMatcher
from modules.m12_digital_twin import DigitalTwin


@pytest.fixture
def predictor():
    return PlacementPredictor()


@pytest.fixture
def sample_spv():
    """Canonical 22D test vector."""
    return np.array([
        0.75,  # F01: cgpa
        0.70,  # F02: dsa_score
        0.65,  # F03: dbms_score
        0.60,  # F04: os_score
        0.55,  # F05: cn_score
        0.70,  # F06: programming_score
        0.65,  # F07: aptitude_score
        0.70,  # F08: soft_skills_score
        0.30,  # F09: project_count
        0.60,  # F10: project_quality_score
        1.00,  # F11: has_internship
        0.20,  # F12: certifications_count
        0.70,  # F13: resume_ats_score
        0.70,  # F14: cosine_similarity
        0.35,  # F15: gap_score
        0.75,  # F16: consistency_score
        0.75,  # F17: branch_encoded -> IMMUTABLE
        0.75,  # F18: target_role_encoded
        0.30,  # F19: assessment_attempts
        0.70,  # F20: behavior_score
        0.75,  # F21: engagement_score
        0.50,  # F22: roadmap_completion_rate
    ], dtype=np.float32)


def test_company_matcher_evaluation():
    """Verify company benchmark matching, eligibility, and dimensional gaps."""
    matcher = CompanyBenchmarkMatcher()
    spv_dict = {SPV_FEATURE_NAMES[i]: 0.70 for i in range(22)}
    student_skills = ["python", "data structures", "sql", "git"]

    evaluations = matcher.evaluate_student(
        student_cgpa=8.0,
        student_skills=student_skills,
        spv_dict=spv_dict,
    )

    assert len(evaluations) > 0
    top_comp = evaluations[0]
    assert "company_name" in top_comp
    assert "is_eligible" in top_comp
    assert top_comp["is_eligible"] is True
    assert 0.0 <= top_comp["overall_compatibility_score"] <= 100.0
    assert "dimensional_gaps" in top_comp
    assert "scientific_integrity_note" in top_comp


def test_digital_twin_what_if_simulation(predictor, sample_spv):
    """Verify forward what-if simulation computes valid delta."""
    twin = DigitalTwin(predictor=predictor)
    perturbations = {
        "dsa_score": +0.15,
        "project_quality_score": +0.20,
    }
    result = twin.simulate_what_if(sample_spv, perturbations)

    assert result["simulation_type"] == "WHAT_IF_FORWARD_PERTURBATION"
    assert "baseline" in result
    assert "simulated" in result
    assert "readiness_probability_delta" in result
    assert "scientific_integrity_disclaimer" in result


def test_digital_twin_rejects_immutable_perturbation(predictor, sample_spv):
    """Digital Twin must strictly reject perturbation on F17 branch_encoded."""
    twin = DigitalTwin(predictor=predictor)
    illegal_perturbation = {
        "branch_encoded": +0.25,  # Strictly forbidden
    }
    with pytest.raises(ValueError, match="Immutability constraint violated"):
        twin.simulate_what_if(sample_spv, illegal_perturbation)


def test_digital_twin_sensitivity_matrix(predictor, sample_spv):
    """Verify marginal sensitivity gradient calculations."""
    twin = DigitalTwin(predictor=predictor)
    sensitivities = twin.compute_sensitivity_matrix(sample_spv, step_size=0.10)

    assert len(sensitivities) > 0
    for s in sensitivities:
        assert "feature" in s
        assert s["feature"] not in IMMUTABLE_FEATURES
        assert "marginal_readiness_gain" in s
        assert "sensitivity_gradient" in s
