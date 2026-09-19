"""
PRIE — SPV Version & Canonical Feature Schema
Module: spv_version.py

Authoritative source of truth for SPV_VERSION and the invariant 22-dimensional
Student Profile Vector (SPV) feature specification.

Traceability:
  - 05_PRIE_Architecture/Student_Profile_Vector_Architecture.md
  - 04_Research_Evidence/Feature_Traceability.md

Scientific Integrity:
  EPISTEMOLOGICAL_STATUS tags are preserved on every feature per Phase 06 Quality Gate G16.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Literal, Optional

# ── Version ──────────────────────────────────────────────────────────────────
SPV_VERSION: str = "v1"
SPV_DIMENSION: int = 22

EpistemologicalStatus = Literal[
    "DIRECTLY_SUPPORTED",
    "PARTIALLY_SUPPORTED",
    "PROPOSED",
    "IMPLEMENTATION_DERIVED",
]


@dataclass(frozen=True)
class SPVFeature:
    """Immutable specification of one SPV feature dimension."""
    id: str                          # e.g. "F01"
    name: str                        # canonical Python identifier
    label: str                       # human-readable label
    domain: str                      # native range description
    normalization: str               # formula description
    missing_strategy: str            # imputation approach
    epistemological_status: EpistemologicalStatus
    downstream_modules: List[str]
    literature: List[str]


# ── Canonical 22-Dimensional Feature Specification ───────────────────────────
SPV_FEATURES: List[SPVFeature] = [
    SPVFeature(
        id="F01", name="cgpa", label="Cumulative GPA",
        domain="0.0–10.0", normalization="f/10.0",
        missing_strategy="MANDATORY — hard block on missing",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M07", "M12"],
        literature=["Paper01", "Paper04", "Paper06", "Paper08", "Paper22"],
    ),
    SPVFeature(
        id="F02", name="dsa_score", label="DSA Mastery Score",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="Branch-median imputation until quiz completed",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M07", "M08"],
        literature=["Paper03", "Paper04", "Paper14", "Paper28", "Paper38"],
    ),
    SPVFeature(
        id="F03", name="dbms_score", label="DBMS Competency Score",
        domain="0.0–100.0", normalization="0.4*SIS + 0.6*Quiz → /100",
        missing_strategy="MICE using cgpa and related CS subjects",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M08"],
        literature=["Paper04", "Paper08", "Paper10", "Paper24"],
    ),
    SPVFeature(
        id="F04", name="os_score", label="Operating Systems Score",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="MICE imputation",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M08"],
        literature=["Paper04", "Paper08", "Paper10", "Paper24"],
    ),
    SPVFeature(
        id="F05", name="cn_score", label="Computer Networks Score",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="MICE imputation",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M08"],
        literature=["Paper04", "Paper08", "Paper10", "Paper24"],
    ),
    SPVFeature(
        id="F06", name="programming_score", label="Programming Proficiency",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="Initialize 0.5 cohort baseline until first session",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M07", "M08"],
        literature=["Paper03", "Paper04", "Paper28", "Paper38", "Paper41"],
    ),
    SPVFeature(
        id="F07", name="aptitude_score", label="Quantitative Aptitude Score",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="Institutional mean if un-attempted",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06"],
        literature=["Paper01", "Paper04", "Paper06", "Paper09", "Paper22"],
    ),
    SPVFeature(
        id="F08", name="soft_skills_score", label="Interpersonal & Communication Score",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="Cohort baseline 0.60 until first interview",
        epistemological_status="PARTIALLY_SUPPORTED",
        downstream_modules=["M06", "M07", "M12"],
        literature=["Paper01", "Paper06", "Paper07", "Paper14", "Paper15"],
    ),
    SPVFeature(
        id="F09", name="project_count", label="Completed Projects Count",
        domain="0–20", normalization="min(f,10)/10.0",
        missing_strategy="Set to 0 if no projects listed",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M07"],
        literature=["Paper04", "Paper11", "Paper17", "Paper28", "Paper36"],
    ),
    SPVFeature(
        id="F10", name="project_quality_score", label="Project Architectural Quality",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="0.0 if project_count==0; else 40.0 baseline",
        epistemological_status="PROPOSED",
        downstream_modules=["M04", "M06", "M07"],
        literature=["Paper11", "Paper17", "Paper36", "Paper42"],
    ),
    SPVFeature(
        id="F11", name="has_internship", label="Industrial Internship Flag",
        domain="{0, 1}", normalization="identity binary",
        missing_strategy="Default 0 (no internship)",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M07", "M12"],
        literature=["Paper01", "Paper06", "Paper07", "Paper09", "Paper22"],
    ),
    SPVFeature(
        id="F12", name="certifications_count", label="Verified Certifications Count",
        domain="0–15", normalization="min(f,5)/5.0",
        missing_strategy="Default 0",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M07"],
        literature=["Paper04", "Paper12", "Paper17", "Paper24", "Paper37"],
    ),
    SPVFeature(
        id="F13", name="resume_ats_score", label="Resume ATS Parseability Score",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="0.0 until resume uploaded",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M01", "M06", "M07", "M08"],
        literature=["Paper11", "Paper12", "Paper17", "Paper36", "Paper42"],
    ),
    SPVFeature(
        id="F14", name="cosine_similarity", label="Resume–JD Semantic Similarity",
        domain="0.0–1.0", normalization="already bounded",
        missing_strategy="0.5 generic baseline if no JD specified",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M07", "M12"],
        literature=["Paper11", "Paper12", "Paper13", "Paper35", "Paper37"],
    ),
    SPVFeature(
        id="F15", name="gap_score", label="Normalized Competency Deficit",
        domain="0.0–1.0", normalization="1 - competency_match_ratio",
        missing_strategy="Computed from F02–F06 and F14",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M07", "M08"],
        literature=["Paper04", "Paper13", "Paper16", "Paper35", "Paper41"],
    ),
    SPVFeature(
        id="F16", name="consistency_score", label="Longitudinal Habit Persistence",
        domain="0.0–1.0", normalization="EMA(alpha=0.3)",
        missing_strategy="Initialize 0.5 for new students",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M11", "M12"],
        literature=["Paper02", "Paper05", "Paper33", "Paper44"],
    ),
    SPVFeature(
        id="F17", name="branch_encoded", label="Academic Branch Encoding",
        domain="0.0–1.0", normalization="target-encoded by placement rate",
        missing_strategy="Non-null DB constraint",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M07"],
        literature=["Paper01", "Paper06", "Paper09", "Paper10", "Paper22"],
    ),
    SPVFeature(
        id="F18", name="target_role_encoded", label="Target Role Complexity Weight",
        domain="0.0–1.0", normalization="static lookup rubric",
        missing_strategy="0.5 generic developer default",
        epistemological_status="PARTIALLY_SUPPORTED",
        downstream_modules=["M04", "M06", "M07", "M08"],
        literature=["Paper13", "Paper17", "Paper35", "Paper41"],
    ),
    SPVFeature(
        id="F19", name="assessment_attempts", label="Cumulative Practice Attempts",
        domain="0–100", normalization="min(f,100)/100.0",
        missing_strategy="Initialize 0",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M11", "M12"],
        literature=["Paper02", "Paper05", "Paper33", "Paper44"],
    ),
    SPVFeature(
        id="F20", name="behavior_score", label="Interview Composure & Non-Verbal Score",
        domain="0.0–100.0", normalization="f/100.0",
        missing_strategy="Cohort median 0.65 until first interview",
        epistemological_status="PARTIALLY_SUPPORTED",
        downstream_modules=["M06", "M07", "M12"],
        literature=["Paper03", "Paper14", "Paper15", "Paper28", "Paper30"],
    ),
    SPVFeature(
        id="F21", name="engagement_score", label="Composite Learning Engagement",
        domain="0.0–1.0", normalization="cohort-percentile scaled",
        missing_strategy="Initialize 0.5 median baseline",
        epistemological_status="DIRECTLY_SUPPORTED",
        downstream_modules=["M06", "M11", "M12"],
        literature=["Paper02", "Paper05", "Paper33", "Paper44"],
    ),
    SPVFeature(
        id="F22", name="roadmap_completion_rate", label="Remediation Milestone Completion",
        domain="0.0–1.0", normalization="completed/total milestones",
        missing_strategy="0.0 for new roadmaps",
        epistemological_status="PARTIALLY_SUPPORTED",
        downstream_modules=["M06", "M07", "M12"],
        literature=["Paper13", "Paper16", "Paper41", "Paper44"],
    ),
]

# Assertion: exactly 22 features
assert len(SPV_FEATURES) == SPV_DIMENSION, (
    f"SPV schema invariant violated: expected {SPV_DIMENSION} features, got {len(SPV_FEATURES)}"
)

# Canonical ordered feature name list (for numpy array ordering)
SPV_FEATURE_NAMES: List[str] = [f.name for f in SPV_FEATURES]
SPV_FEATURE_IDS: List[str] = [f.id for f in SPV_FEATURES]
SPV_ID_TO_NAME: dict[str, str] = {f.id: f.name for f in SPV_FEATURES}
SPV_NAME_TO_ID: dict[str, str] = {f.name: f.id for f in SPV_FEATURES}

# Immutable features that must be locked in DiCE counterfactual optimization
IMMUTABLE_FEATURES: List[str] = ["branch_encoded"]  # F17 per DD-003

# Features initialized from imputation (confidence mask = 0 initially)
IMPUTED_DEFAULTS: dict = {
    "dsa_score": 50.0,
    "dbms_score": 60.0,
    "os_score": 60.0,
    "cn_score": 60.0,
    "programming_score": 55.0,
    "aptitude_score": 60.0,
    "soft_skills_score": 60.0,
    "project_quality_score": 40.0,
    "resume_ats_score": 0.0,
    "cosine_similarity": 0.5,
    "behavior_score": 65.0,
    "engagement_score": 0.5,
    "consistency_score": 0.5,
    "roadmap_completion_rate": 0.0,
    "gap_score": 0.5,
    "assessment_attempts": 0.0,
}

# Native raw range boundaries (min, max) for raw profile features
SPV_RAW_BOUNDS: dict[str, tuple[float, float]] = {
    "cgpa": (0.0, 10.0),
    "dsa_score": (0.0, 100.0),
    "dbms_score": (0.0, 100.0),
    "os_score": (0.0, 100.0),
    "cn_score": (0.0, 100.0),
    "programming_score": (0.0, 100.0),
    "aptitude_score": (0.0, 100.0),
    "soft_skills_score": (0.0, 100.0),
    "project_count": (0.0, 50.0),
    "project_quality_score": (0.0, 100.0),
    "has_internship": (0.0, 1.0),
    "certifications_count": (0.0, 30.0),
    "resume_ats_score": (0.0, 100.0),
    "cosine_similarity": (0.0, 1.0),
    "gap_score": (0.0, 1.0),
    "consistency_score": (0.0, 1.0),
    "branch_encoded": (0.0, 1.0),
    "target_role_encoded": (0.0, 1.0),
    "assessment_attempts": (0.0, 1000.0),
    "behavior_score": (0.0, 100.0),
    "engagement_score": (0.0, 1.0),
    "roadmap_completion_rate": (0.0, 1.0),
}


class SPVValidationError(ValueError):
    """Raised when an SPV vector or dictionary fails schema, dimension, or range validation."""
    pass


class SPVSchemaMismatchError(KeyError):
    """Raised when an unexpected or legacy SPV feature name is encountered."""
    pass


def validate_spv_vector(
    vector: Any,
    normalized: bool = True,
    raise_exception: bool = False,
) -> tuple[bool, Optional[str]]:
    """
    Validate a 22-dimensional SPV vector.
    
    Args:
        vector: Array-like or list of numbers
        normalized: If True, features are expected in [0.0, 1.0] (except potential z-scores)
        raise_exception: If True, raises SPVValidationError on failure
        
    Returns:
        (is_valid, error_message)
    """
    import numpy as np

    if vector is None:
        msg = "SPV vector cannot be None"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    try:
        arr = np.asarray(vector, dtype=np.float64)
    except (ValueError, TypeError) as e:
        msg = f"SPV vector contains non-numeric data: {e}"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    if arr.ndim != 1:
        msg = f"SPV vector must be 1-dimensional, got ndim={arr.ndim} with shape {arr.shape}"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    if arr.shape[0] != SPV_DIMENSION:
        msg = f"SPV vector dimensionality invariant violated: expected {SPV_DIMENSION}, got {arr.shape[0]}"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    if np.isnan(arr).any():
        nan_indices = np.where(np.isnan(arr))[0].tolist()
        nan_features = [SPV_FEATURE_NAMES[i] for i in nan_indices]
        msg = f"SPV vector contains NaN values at indices {nan_indices} ({nan_features})"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    if np.isinf(arr).any():
        inf_indices = np.where(np.isinf(arr))[0].tolist()
        inf_features = [SPV_FEATURE_NAMES[i] for i in inf_indices]
        msg = f"SPV vector contains infinite values at indices {inf_indices} ({inf_features})"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    if normalized:
        # Check standard normalized bounds [0.0, 1.0] with small floating point tolerance
        out_of_bounds = []
        for i, val in enumerate(arr):
            if val < -1e-5 or val > 1.0 + 1e-5:
                out_of_bounds.append((SPV_FEATURE_NAMES[i], float(val)))
        if out_of_bounds:
            msg = f"Normalized SPV vector values outside [0.0, 1.0]: {out_of_bounds}"
            if raise_exception:
                raise SPVValidationError(msg)
            return False, msg

    return True, None


def validate_spv_dict(
    data: dict,
    allow_missing: bool = False,
    raise_exception: bool = False,
) -> tuple[bool, Optional[str]]:
    """
    Validate a dictionary of SPV features against canonical names and ranges.
    
    Args:
        data: Feature name -> value dictionary
        allow_missing: If False, all 22 canonical features must be present
        raise_exception: If True, raises SPVValidationError or SPVSchemaMismatchError
    """
    import math

    if not isinstance(data, dict):
        msg = f"SPV data must be a dictionary, got {type(data).__name__}"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    # Check for legacy divergent features
    legacy_features = {"backlogs", "internship_months", "skill_count"}
    encountered_legacy = set(data.keys()) & legacy_features
    if encountered_legacy:
        msg = (
            f"Divergent legacy features rejected in canonical SPV: {list(encountered_legacy)}. "
            f"Use canonical schema F01-F22."
        )
        if raise_exception:
            raise SPVSchemaMismatchError(msg)
        return False, msg

    canonical_set = set(SPV_FEATURE_NAMES)
    input_keys = set(data.keys())

    # Check for extra unknown features
    unknown_keys = input_keys - canonical_set
    if unknown_keys:
        msg = f"Unknown features in SPV dictionary: {list(unknown_keys)}"
        if raise_exception:
            raise SPVSchemaMismatchError(msg)
        return False, msg

    if not allow_missing:
        missing_keys = canonical_set - input_keys
        if missing_keys:
            msg = f"Missing required SPV features: {list(missing_keys)}"
            if raise_exception:
                raise SPVValidationError(msg)
            return False, msg

    # Validate value types, NaNs, and raw ranges
    for key, val in data.items():
        if val is None:
            continue
        if not isinstance(val, (int, float)):
            msg = f"Feature '{key}' has non-numeric value: {val} ({type(val).__name__})"
            if raise_exception:
                raise SPVValidationError(msg)
            return False, msg

        if math.isnan(val) or math.isinf(val):
            msg = f"Feature '{key}' contains NaN or Inf value: {val}"
            if raise_exception:
                raise SPVValidationError(msg)
            return False, msg

        if key in SPV_RAW_BOUNDS:
            min_val, max_val = SPV_RAW_BOUNDS[key]
            if val < min_val - 1e-5 or val > max_val + 1e-5:
                msg = f"Feature '{key}' value {val} outside valid native range [{min_val}, {max_val}]"
                if raise_exception:
                    raise SPVValidationError(msg)
                return False, msg

    return True, None


def validate_observation_mask(
    mask: Any,
    raise_exception: bool = False,
) -> tuple[bool, Optional[str]]:
    """Validate binary observation mask m in {0, 1}^22."""
    import numpy as np

    if mask is None:
        msg = "Observation mask cannot be None"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    try:
        arr = np.asarray(mask, dtype=int)
    except Exception as e:
        msg = f"Invalid observation mask type: {e}"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    if arr.shape != (SPV_DIMENSION,):
        msg = f"Observation mask shape mismatch: expected ({SPV_DIMENSION},), got {arr.shape}"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    invalid_vals = set(arr.tolist()) - {0, 1}
    if invalid_vals:
        msg = f"Observation mask must be strictly binary {0, 1}, found invalid values: {invalid_vals}"
        if raise_exception:
            raise SPVValidationError(msg)
        return False, msg

    return True, None
