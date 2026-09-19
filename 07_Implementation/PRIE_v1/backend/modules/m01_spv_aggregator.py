"""
PRIE v1 — Module M01: Student Profile Vector (SPV) Aggregator & Harmonizer
File: backend/modules/m01_spv_aggregator.py

MODULE: M01 — SPV Aggregator & Harmonizer
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH
RESEARCH_GAP: RG1 (Fragmented unimodal data silos)
RESEARCH_OBJECTIVE: RO1 (Multimodal Feature Synthesis)
TRACEABILITY: Paper01, Paper04, Paper06, Paper08, Paper10, Paper22; DD-001

Implements:
  - Assembly of the invariant 22-dimensional SPV tensor (F01–F22)
  - Binary observation confidence mask m ∈ {0,1}^22
  - Per-feature normalization formulas from Student_Profile_Vector_Architecture.md
  - MICE median fallback for missing features (full MICE requires Phase 08 training data)
  - Profile completeness scoring
  - SPV snapshot persistence to spv_snapshots table
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from spv_version import SPV_FEATURE_NAMES, SPV_DIMENSION, IMPUTED_DEFAULTS, IMMUTABLE_FEATURES
from database import db_manager, queries

logger = logging.getLogger("PRIE.M01.SPVAggregator")

# ── Branch encoding table (F17 — target-encoded on historical placement rates) ─
BRANCH_PLACEMENT_RATES: Dict[str, float] = {
    "computer science":                0.95,
    "computer science & engineering":  0.95,
    "computer science and engineering": 0.95,
    "cse":                             0.95,
    "information technology":          0.90,
    "it":                              0.90,
    "artificial intelligence":         0.92,
    "ai & ds":                         0.92,
    "ai and data science":             0.92,
    "electronics & communication":     0.75,
    "electronics and communication":   0.75,
    "electronics":                     0.75,
    "ece":                             0.75,
    "electrical & electronics":        0.65,
    "electrical and electronics":      0.65,
    "electrical":                      0.65,
    "eee":                             0.65,
    "mechanical":                      0.50,
    "mechanical engineering":          0.50,
    "mech":                            0.50,
    "civil":                           0.45,
    "civil engineering":               0.45,
}

# ── Role encoding table (F18 — role complexity weight) ───────────────────────
ROLE_COMPLEXITY_WEIGHTS: Dict[str, float] = {
    "software development engineer": 0.90,
    "software engineer":             0.90,
    "sde":                           0.90,
    "sde-1":                         0.90,
    "full stack developer":          0.88,
    "backend developer":             0.88,
    "machine learning engineer":     0.88,
    "frontend developer":            0.82,
    "devops engineer":               0.82,
    "data scientist":                0.85,
    "cloud engineer":                0.80,
    "security analyst":              0.78,
    "data analyst":                  0.75,
    "business analyst":              0.70,
    "qa engineer":                   0.65,
    "quality assurance":             0.65,
}


class SPVAggregator:
    """
    M01: Student Profile Vector (SPV) Aggregator & Harmonizer.

    Assembles the invariant 22-dimensional feature tensor from heterogeneous
    database sources, applies per-feature normalization, computes the binary
    observation mask, and persists a versioned snapshot.
    """

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self.db_path = db_path

    # ── Encoding helpers ─────────────────────────────────────────────────────

    def encode_branch(self, branch: Optional[str]) -> float:
        """F17: target-encode academic branch via historical placement rate."""
        if not branch:
            return 0.70   # unknown branch default
        key = branch.strip().lower()
        return BRANCH_PLACEMENT_RATES.get(key, 0.70)

    def encode_role(self, role: Optional[str]) -> float:
        """F18: encode target role via empirical difficulty weight."""
        if not role:
            return 0.75   # generic SDE default
        key = role.strip().lower()
        return ROLE_COMPLEXITY_WEIGHTS.get(key, 0.75)

    # ── Per-feature normalizers (exact formulas from SPV_Architecture.md) ────

    @staticmethod
    def _norm_cgpa(v: float) -> float:
        """F01: f/10.0"""
        return float(np.clip(v / 10.0, 0.0, 1.0))

    @staticmethod
    def _norm_score_100(v: float) -> float:
        """F02–F08, F20: f/100.0"""
        return float(np.clip(v / 100.0, 0.0, 1.0))

    @staticmethod
    def _norm_project_count(v: float) -> float:
        """F09: min(f,10)/10.0"""
        return float(np.clip(min(v, 10.0) / 10.0, 0.0, 1.0))

    @staticmethod
    def _norm_certifications(v: float) -> float:
        """F12: min(f,5)/5.0"""
        return float(np.clip(min(v, 5.0) / 5.0, 0.0, 1.0))

    @staticmethod
    def _norm_assessment_attempts(v: float) -> float:
        """F19: min(f,100)/100.0"""
        return float(np.clip(min(v, 100.0) / 100.0, 0.0, 1.0))

    # ── Assessment score aggregation ─────────────────────────────────────────

    def _aggregate_assessment_scores(
        self, student_id: int
    ) -> Tuple[Dict[str, float], int, int]:
        """
        Compute per-subject mastery scores from assessment history.
        Returns (scores_dict, total_attempts, correct_count).
        """
        rows = db_manager.execute_query(
            queries.GET_STUDENT_ASSESSMENTS, (student_id,), self.db_path
        )
        assessments = db_manager.dict_rows(rows)

        subject_scores: Dict[str, List[float]] = {
            "dsa": [], "dbms": [], "os": [], "cn": [],
            "programming": [], "aptitude": [], "soft_skills": [],
        }
        total, correct = 0, 0

        for a in assessments:
            topic = str(a.get("topic", "")).lower()
            tq = max(int(a.get("total_questions", 1)), 1)
            sc = int(a.get("score", 0))
            pct = (sc / tq) * 100.0
            total += 1
            correct += int(a.get("is_correct", 0))

            if any(k in topic for k in ["dsa", "data structure", "algorithm"]):
                subject_scores["dsa"].append(pct)
            elif any(k in topic for k in ["dbms", "database", "sql"]):
                subject_scores["dbms"].append(pct)
            elif any(k in topic for k in ["operating system", "os ", "process", "memory"]):
                subject_scores["os"].append(pct)
            elif any(k in topic for k in ["computer network", "networking", "cn"]):
                subject_scores["cn"].append(pct)
            elif any(k in topic for k in ["programming", "python", "java", "c++", "coding"]):
                subject_scores["programming"].append(pct)
            elif "aptitude" in topic:
                subject_scores["aptitude"].append(pct)
            elif any(k in topic for k in ["soft skill", "communication", "hr"]):
                subject_scores["soft_skills"].append(pct)

        def mean_or_default(lst: List[float], default: float) -> Tuple[float, int]:
            if lst:
                return float(np.mean(lst)), 1
            return default, 0

        dsa,   m_dsa   = mean_or_default(subject_scores["dsa"],          IMPUTED_DEFAULTS["dsa_score"])
        dbms,  m_dbms  = mean_or_default(subject_scores["dbms"],         IMPUTED_DEFAULTS["dbms_score"])
        os_,   m_os    = mean_or_default(subject_scores["os"],            IMPUTED_DEFAULTS["os_score"])
        cn,    m_cn    = mean_or_default(subject_scores["cn"],            IMPUTED_DEFAULTS["cn_score"])
        prog,  m_prog  = mean_or_default(subject_scores["programming"],   IMPUTED_DEFAULTS["programming_score"])
        apt,   m_apt   = mean_or_default(subject_scores["aptitude"],      IMPUTED_DEFAULTS["aptitude_score"])
        soft,  m_soft  = mean_or_default(subject_scores["soft_skills"],   IMPUTED_DEFAULTS["soft_skills_score"])

        scores = {
            "dsa_score":        dsa,  "dsa_observed":   m_dsa,
            "dbms_score":       dbms, "dbms_observed":  m_dbms,
            "os_score":         os_,  "os_observed":    m_os,
            "cn_score":         cn,   "cn_observed":    m_cn,
            "programming_score": prog, "prog_observed": m_prog,
            "aptitude_score":   apt,  "apt_observed":   m_apt,
            "soft_skills_score": soft, "soft_observed": m_soft,
        }
        return scores, total, correct

    # ── Main assembly ─────────────────────────────────────────────────────────

    def assemble(self, student_id: int) -> Tuple[np.ndarray, np.ndarray, float]:
        """
        Assemble the 22-dimensional normalized SPV tensor for a student.

        Args:
            student_id: Primary key of student.

        Returns:
            Tuple of:
                feature_vector: np.ndarray shape (22,) — normalized F01–F22
                confidence_mask: np.ndarray shape (22,) — 1=observed, 0=imputed
                completeness: float in [0.0, 1.0]

        Raises:
            ValueError: If student not found in database.
        """
        row = db_manager.dict_row(
            db_manager.execute_single(queries.GET_STUDENT_BY_ID, (student_id,), self.db_path)
        )
        if not row:
            raise ValueError(f"Student {student_id} not found.")

        # Resume data
        resume = db_manager.dict_row(
            db_manager.execute_single(queries.GET_LATEST_RESUME, (student_id,), self.db_path)
        )

        # Assessment scores
        subj, total_attempts, _ = self._aggregate_assessment_scores(student_id)

        # Roadmap progress
        completed_rows = db_manager.execute_single(
            queries.COUNT_COMPLETED_MILESTONES, (student_id,), self.db_path
        )
        total_rows = db_manager.execute_single(
            queries.COUNT_TOTAL_MILESTONES, (student_id,), self.db_path
        )
        n_completed = int(completed_rows["cnt"]) if completed_rows else 0
        n_total     = int(total_rows["cnt"]) if total_rows else 0
        roadmap_rate = (n_completed / n_total) if n_total > 0 else 0.0

        # Telemetry (lazy import to avoid circular)
        try:
            from modules.m11_behavioral_telemetry import BehavioralTelemetry
            tel = BehavioralTelemetry(self.db_path)
            consistency = tel.compute_consistency_score(student_id)
            engagement  = tel.compute_engagement_score(student_id)
            con_obs = 1
            eng_obs = 1
        except Exception:
            consistency = IMPUTED_DEFAULTS["consistency_score"]
            engagement  = IMPUTED_DEFAULTS["engagement_score"]
            con_obs = eng_obs = 0

        # ── Raw values ────────────────────────────────────────────────────────
        cgpa                = float(row.get("cgpa", 0.0) or 0.0)
        dsa_raw             = subj["dsa_score"]
        dbms_raw            = subj["dbms_score"]
        os_raw              = subj["os_score"]
        cn_raw              = subj["cn_score"]
        prog_raw            = subj["programming_score"]
        apt_raw             = subj["aptitude_score"]
        soft_raw            = subj["soft_skills_score"]
        proj_count          = float(row.get("project_count", 0) or 0)
        proj_quality        = float(row.get("project_quality_score", 40.0) or 40.0)
        has_internship      = float(row.get("has_internship", 0) or 0)
        certs               = float(row.get("certifications_count", 0) or 0)
        ats_raw             = float((resume or {}).get("ats_score", 0.0) or 0.0)
        cosine_raw          = float((resume or {}).get("cosine_similarity", 0.5) or 0.5)
        branch_enc          = self.encode_branch(row.get("branch"))
        role_enc            = self.encode_role(row.get("target_role"))
        behavior_raw        = float(IMPUTED_DEFAULTS["behavior_score"])  # M05 not yet live

        # F15: gap_score = 1 - competency_match_ratio
        tech_scores = [dsa_raw, prog_raw, apt_raw, dbms_raw, os_raw, cn_raw]
        competency_match = (np.mean(tech_scores) / 100.0) * 0.6 + cosine_raw * 0.4
        gap_score = float(np.clip(1.0 - competency_match, 0.0, 1.0))

        # ── Normalize (exact formulas from SPV_Architecture.md) ──────────────
        f = [
            self._norm_cgpa(cgpa),                    # F01
            self._norm_score_100(dsa_raw),            # F02
            self._norm_score_100(dbms_raw),           # F03
            self._norm_score_100(os_raw),             # F04
            self._norm_score_100(cn_raw),             # F05
            self._norm_score_100(prog_raw),           # F06
            self._norm_score_100(apt_raw),            # F07
            self._norm_score_100(soft_raw),           # F08
            self._norm_project_count(proj_count),     # F09
            self._norm_score_100(proj_quality),       # F10
            float(np.clip(has_internship, 0.0, 1.0)), # F11 — binary
            self._norm_certifications(certs),         # F12
            self._norm_score_100(ats_raw),            # F13
            float(np.clip(cosine_raw, 0.0, 1.0)),     # F14
            float(np.clip(gap_score, 0.0, 1.0)),      # F15
            float(np.clip(consistency, 0.0, 1.0)),    # F16
            float(np.clip(branch_enc, 0.0, 1.0)),     # F17 — IMMUTABLE
            float(np.clip(role_enc, 0.0, 1.0)),       # F18
            self._norm_assessment_attempts(float(total_attempts)),  # F19
            self._norm_score_100(behavior_raw),       # F20
            float(np.clip(engagement, 0.0, 1.0)),     # F21
            float(np.clip(roadmap_rate, 0.0, 1.0)),   # F22
        ]

        assert len(f) == SPV_DIMENSION, f"SPV assembly error: got {len(f)} features"
        vector = np.array(f, dtype=np.float32)

        # ── Confidence mask ───────────────────────────────────────────────────
        mask = np.array([
            1 if cgpa > 0 else 0,                     # F01
            subj["dsa_observed"],                      # F02
            subj["dbms_observed"],                     # F03
            subj["os_observed"],                       # F04
            subj["cn_observed"],                       # F05
            subj["prog_observed"],                     # F06
            subj["apt_observed"],                      # F07
            subj["soft_observed"],                     # F08
            1 if proj_count > 0 else 0,               # F09
            1 if row.get("project_quality_score") else 0,  # F10
            1,                                         # F11 — always known
            1 if certs > 0 else 0,                    # F12
            1 if resume else 0,                        # F13
            1 if resume else 0,                        # F14
            1,                                         # F15 — computed
            con_obs,                                   # F16
            1,                                         # F17 — always known
            1 if row.get("target_role") else 0,       # F18
            1 if total_attempts > 0 else 0,           # F19
            0,                                         # F20 — M05 not live
            eng_obs,                                   # F21
            1 if n_total > 0 else 0,                  # F22
        ], dtype=np.int8)

        assert len(mask) == SPV_DIMENSION

        # ── Completeness score ────────────────────────────────────────────────
        completeness = self._compute_completeness(row, resume, total_attempts)

        return vector, mask, completeness

    def _compute_completeness(
        self,
        student: Dict[str, Any],
        resume: Optional[Dict[str, Any]],
        total_attempts: int,
    ) -> float:
        """Compute profile completeness 0.0–1.0."""
        pts = 0.0
        if float(student.get("cgpa", 0) or 0) > 0:
            pts += 0.20
        skills = json.loads(student.get("skills_json", "[]") or "[]")
        if isinstance(skills, list) and len(skills) >= 3:
            pts += 0.20
        if student.get("target_role"):
            pts += 0.15
        if resume and resume.get("file_path"):
            pts += 0.25
        if total_attempts > 0:
            pts += 0.20
        return round(min(1.0, max(0.0, pts)), 2)

    # ── Convenience wrappers ──────────────────────────────────────────────────

    def get_feature_vector(self, student_id: int) -> np.ndarray:
        """Return only the 22-dim normalized SPV vector."""
        v, _, _ = self.assemble(student_id)
        return v

    def get_feature_dict(self, student_id: int) -> Dict[str, Any]:
        """Return SPV as dict with feature names, mask, and completeness."""
        v, mask, comp = self.assemble(student_id)
        feat_map = {name: round(float(v[i]), 6) for i, name in enumerate(SPV_FEATURE_NAMES)}
        return {
            "spv_version": "v1",
            "dimension": 22,
            "features": feat_map,
            "normalized_vector": [round(float(x), 6) for x in v],
            "confidence_mask": mask.tolist(),
            "profile_completeness": comp,
            **feat_map,
        }

    def save_snapshot(
        self,
        student_id: int,
        readiness_prob: Optional[float] = None,
        readiness_tier: Optional[str] = None,
        shap_values: Optional[Dict[str, float]] = None,
        trigger: str = "profile_update",
    ) -> int:
        """Persist a versioned SPV snapshot to spv_snapshots table."""
        v, mask, _ = self.assemble(student_id)
        return db_manager.execute_insert(
            queries.INSERT_SPV_SNAPSHOT,
            (
                student_id, "v1",
                *[round(float(x), 6) for x in v],
                json.dumps(mask.tolist()),
                readiness_prob,
                readiness_tier,
                json.dumps(shap_values or {}),
                trigger,
            ),
            self.db_path,
        )
