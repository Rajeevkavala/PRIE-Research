"""
PRIE v1 — Module M04: Skill Gap Analysis & Distance Engine
File: backend/modules/m04_skill_gap_engine.py

MODULE: M04 — Skill Gap Analysis & Distance Engine
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH
RESEARCH_GAP: RG1 (Unimodal silos), RG7 (Cold-start career pathway)
RESEARCH_OBJECTIVE: RO4 (Prescriptive Career Remediation)
TRACEABILITY: Paper04, Paper13, Paper16, Paper35, Paper41; DD-008

Implements:
  - Weighted Euclidean distance: D(x, r) = sqrt(sum(w_i * (x_i - r_i)^2))
  - F15 (gap_score) computation: 1.0 - competency_match_ratio
  - Ranked missing-competency list with criticality weights
  - Directional deficit vector for DiCE counterfactual seeding
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from spv_version import SPV_FEATURE_NAMES

logger = logging.getLogger("PRIE.M04.SkillGapEngine")

# ── Market criticality weights for M04 gap computation ───────────────────────
# Higher weight = more critical for placement; derived from Phase 04 evidence
SKILL_CRITICALITY_WEIGHTS: Dict[str, float] = {
    "dsa_score":               0.22,  # Highest: all tech interviews test DSA
    "programming_score":       0.18,  # Practical coding ability
    "aptitude_score":          0.12,  # Round-1 gating in campus drives
    "has_internship":          0.12,  # Strong signal per Paper01, Paper09
    "resume_ats_score":        0.08,
    "cosine_similarity":       0.08,
    "dbms_score":              0.06,
    "os_score":                0.05,
    "cn_score":                0.04,
    "project_count":           0.03,
    "certifications_count":    0.02,
}

# ── Reference role profiles (target vectors in SPV space) ────────────────────
# Values are in the NORMALIZED [0,1] space matching SPV output
ROLE_PROFILES: Dict[str, Dict[str, float]] = {
    "Software Development Engineer": {
        "cgpa":               0.70,
        "dsa_score":          0.80,
        "programming_score":  0.80,
        "aptitude_score":     0.70,
        "dbms_score":         0.60,
        "os_score":           0.60,
        "cn_score":           0.55,
        "has_internship":     0.50,
        "project_count":      0.50,
        "resume_ats_score":   0.70,
        "cosine_similarity":  0.75,
        "certifications_count": 0.20,
        "soft_skills_score":  0.60,
    },
    "Data Scientist": {
        "cgpa":               0.72,
        "dsa_score":          0.70,
        "programming_score":  0.78,
        "aptitude_score":     0.72,
        "dbms_score":         0.70,
        "os_score":           0.50,
        "cn_score":           0.40,
        "has_internship":     0.50,
        "project_count":      0.60,
        "resume_ats_score":   0.68,
        "cosine_similarity":  0.75,
        "certifications_count": 0.40,
        "soft_skills_score":  0.65,
    },
    "DevOps Engineer": {
        "cgpa":               0.65,
        "dsa_score":          0.60,
        "programming_score":  0.70,
        "aptitude_score":     0.65,
        "dbms_score":         0.55,
        "os_score":           0.80,
        "cn_score":           0.78,
        "has_internship":     0.60,
        "project_count":      0.55,
        "resume_ats_score":   0.65,
        "cosine_similarity":  0.70,
        "certifications_count": 0.60,
        "soft_skills_score":  0.60,
    },
    "QA Engineer": {
        "cgpa":               0.60,
        "dsa_score":          0.55,
        "programming_score":  0.60,
        "aptitude_score":     0.60,
        "dbms_score":         0.60,
        "os_score":           0.50,
        "cn_score":           0.45,
        "has_internship":     0.30,
        "project_count":      0.30,
        "resume_ats_score":   0.60,
        "cosine_similarity":  0.65,
        "certifications_count": 0.20,
        "soft_skills_score":  0.65,
    },
}

# Default: generic SDE if role not found
_DEFAULT_ROLE = "Software Development Engineer"


class SkillGapEngine:
    """
    M04: Skill Gap Analysis & Distance Engine.

    Computes weighted Euclidean distance between student SPV and target
    role vector, yielding F15 (gap_score) and a ranked deficit list.
    """

    def compute_gap(
        self,
        spv_vector: np.ndarray,
        target_role: str = _DEFAULT_ROLE,
        feature_names: Optional[List[str]] = None,
    ) -> Tuple[float, List[Dict], np.ndarray]:
        """
        Compute the skill gap between candidate and target role.

        Args:
            spv_vector: Normalized 22-dim SPV array (F01–F22 in [0,1]).
            target_role: Role name string.
            feature_names: Feature name list (defaults to SPV_FEATURE_NAMES).

        Returns:
            Tuple of:
                gap_score (float): F15, in [0.0, 1.0]. Higher = larger gap.
                deficit_ranking (List[Dict]): Ranked list of missing competencies.
                deficit_vector (np.ndarray): Signed directional deficit (target - candidate).
        """
        names = feature_names or SPV_FEATURE_NAMES
        assert len(spv_vector) == len(names), "SPV dimension mismatch"

        # Map to normalized candidate values
        candidate: Dict[str, float] = {
            names[i]: float(spv_vector[i]) for i in range(len(names))
        }

        # Look up role profile (closest match)
        role_key = self._match_role(target_role)
        role_profile = ROLE_PROFILES[role_key]

        # Weighted Euclidean distance (M04 formula, DD-008)
        sq_sum = 0.0
        deficit_list = []

        for feat, req_val in role_profile.items():
            if feat not in candidate:
                continue
            cand_val = candidate[feat]
            w = SKILL_CRITICALITY_WEIGHTS.get(feat, 0.03)
            diff = req_val - cand_val  # positive = deficit

            if diff > 0.01:   # threshold: ignore negligible gaps
                deficit_list.append({
                    "feature":       feat,
                    "current_value": round(cand_val, 4),
                    "target_value":  round(req_val, 4),
                    "deficit":       round(diff, 4),
                    "criticality":   round(w, 4),
                    "weighted_deficit": round(w * diff, 4),
                })

            sq_sum += w * max(diff, 0.0) ** 2

        # F15 = normalized gap distance
        gap_score = float(np.clip(np.sqrt(sq_sum), 0.0, 1.0))

        # Rank by weighted_deficit descending
        deficit_list.sort(key=lambda x: x["weighted_deficit"], reverse=True)

        # Directional deficit vector (full 22-dim)
        deficit_vector = np.zeros(len(names), dtype=np.float32)
        for item in deficit_list:
            if item["feature"] in names:
                i = names.index(item["feature"])
                deficit_vector[i] = item["deficit"]

        return gap_score, deficit_list, deficit_vector

    def compute_f15(
        self,
        spv_vector: np.ndarray,
        target_role: str = _DEFAULT_ROLE,
    ) -> float:
        """Convenience: return only F15 gap_score."""
        g, _, _ = self.compute_gap(spv_vector, target_role)
        return g

    def get_role_profile(self, role: str) -> Dict[str, float]:
        """Return the reference role profile vector."""
        return ROLE_PROFILES[self._match_role(role)]

    def available_roles(self) -> List[str]:
        """Return list of supported target roles."""
        return list(ROLE_PROFILES.keys())

    @staticmethod
    def _match_role(role: str) -> str:
        """Match role string to nearest key in ROLE_PROFILES."""
        role_lower = role.strip().lower()
        for key in ROLE_PROFILES:
            if key.lower() in role_lower or role_lower in key.lower():
                return key
        return _DEFAULT_ROLE
