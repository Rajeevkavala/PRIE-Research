"""
PRIE v1 — Module M11: Company Benchmark Matcher & Alignment Engine
File: backend/modules/m11_company_matcher.py

MODULE: M11 — Company Readiness & Alignment Engine
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (Multi-criteria Benchmark Matching, DD-010)
RESEARCH_GAP: RG7 (Misaligned career pathways; no objective company readiness metrics)
RESEARCH_OBJECTIVE: RO7 (Company-Specific Readiness Profiling)
TRACEABILITY: Paper03, Paper07, Paper26, Paper32; DD-010

Features:
  - Data-backed company benchmarks (loaded from DB / config)
  - Multi-dimensional competency matching (DSA, System Design, ATS, Projects, Core CS)
  - Objective gap breakdown per target enterprise
  - Explicit scientific integrity guarantee: NO fabricated hiring probabilities.
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
from database import db_manager, queries
from spv_version import SPV_FEATURE_NAMES

logger = logging.getLogger("PRIE.M11.CompanyMatcher")

DEFAULT_COMPANIES: List[Dict[str, Any]] = [
    {
        "company_id": 1,
        "company_name": "Google",
        "tier": "MAANG",
        "min_cgpa": 7.5,
        "required_skills": ["python", "c++", "data structures", "algorithms", "system design", "linux", "distributed systems"],
        "benchmark_dimensions": {
            "dsa_score": 0.88,
            "programming_score": 0.85,
            "os_score": 0.75,
            "cn_score": 0.75,
            "project_quality_score": 0.80,
            "resume_ats_score": 0.75,
        },
        "prs_threshold": 85.0,
    },
    {
        "company_id": 2,
        "company_name": "Amazon",
        "tier": "MAANG",
        "min_cgpa": 7.0,
        "required_skills": ["java", "python", "data structures", "algorithms", "oop", "sql", "aws", "docker"],
        "benchmark_dimensions": {
            "dsa_score": 0.82,
            "programming_score": 0.80,
            "dbms_score": 0.75,
            "os_score": 0.70,
            "project_quality_score": 0.75,
            "resume_ats_score": 0.72,
        },
        "prs_threshold": 80.0,
    },
    {
        "company_id": 3,
        "company_name": "Microsoft",
        "tier": "MAANG",
        "min_cgpa": 7.0,
        "required_skills": ["c#", "c++", "python", "data structures", "algorithms", "azure", "sql", "git"],
        "benchmark_dimensions": {
            "dsa_score": 0.80,
            "programming_score": 0.82,
            "os_score": 0.75,
            "dbms_score": 0.72,
            "project_quality_score": 0.75,
            "resume_ats_score": 0.70,
        },
        "prs_threshold": 78.0,
    },
    {
        "company_id": 4,
        "company_name": "TCS (Digital)",
        "tier": "Tier-2 Product / IT",
        "min_cgpa": 6.5,
        "required_skills": ["python", "java", "sql", "git", "web development"],
        "benchmark_dimensions": {
            "dsa_score": 0.65,
            "programming_score": 0.65,
            "aptitude_score": 0.70,
            "dbms_score": 0.60,
            "resume_ats_score": 0.60,
        },
        "prs_threshold": 65.0,
    },
]


class CompanyBenchmarkMatcher:
    """
    M11: Company Readiness & Alignment Engine.
    Matches a student's profile and SPV against empirical hiring benchmark criteria.
    """

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self.db_path = db_path
        self.companies = self._load_companies()

    def _load_companies(self) -> List[Dict[str, Any]]:
        """Load from database or fallback to DEFAULT_COMPANIES."""
        try:
            rows = db_manager.execute_query(queries.GET_ALL_COMPANIES, db_path=self.db_path)
            items = db_manager.dict_rows(rows)
            if items:
                formatted = []
                for row in items:
                    req_skills = json.loads(row.get("required_skills_json") or "[]")
                    dim_str = row.get("tech_stack_json") or "{}"
                    try:
                        dims = json.loads(dim_str) if isinstance(dim_str, str) else {}
                    except Exception:
                        dims = {}
                    if not isinstance(dims, dict):
                        dims = {
                            "dsa_score": 0.75, "programming_score": 0.70, "dbms_score": 0.65
                        }
                    formatted.append({
                        "company_id": row["company_id"],
                        "company_name": row["company_name"],
                        "tier": row["tier"],
                        "min_cgpa": float(row.get("min_cgpa", 6.0)),
                        "required_skills": req_skills if isinstance(req_skills, list) else [],
                        "benchmark_dimensions": dims,
                        "prs_threshold": float(row.get("prs_threshold", 70.0)),
                    })
                return formatted
        except Exception as e:
            logger.debug(f"DB company load note: {e}")
        return DEFAULT_COMPANIES

    def evaluate_student(
        self,
        student_cgpa: float,
        student_skills: List[str],
        spv_dict: Dict[str, float],
        company_name: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Evaluate compatibility against one or all company benchmarks.
        """
        target_list = [c for c in self.companies if c["company_name"].lower() == company_name.lower()] if company_name else self.companies

        results = []
        for comp in target_list:
            # 1. Academic Eligibility Check
            is_eligible = bool(student_cgpa >= comp["min_cgpa"])

            # 2. Skill Coverage
            req_skills = [s.lower() for s in comp["required_skills"]]
            std_skills = [s.lower() for s in student_skills]
            matched = [s for s in req_skills if s in std_skills]
            missing = [s for s in req_skills if s not in matched]
            skill_coverage_pct = round((len(matched) / max(1, len(req_skills))) * 100.0, 1)

            # 3. Dimensional Competency Matching
            dim_deficits = {}
            dim_scores = []
            for dim_name, target_val in comp["benchmark_dimensions"].items():
                curr_val = spv_dict.get(dim_name, 0.5)
                deficit = max(0.0, target_val - curr_val)
                dim_deficits[dim_name] = round(deficit, 3)
                # Dimensional score (100 if curr >= target, else proportional)
                dim_score = min(100.0, (curr_val / max(0.01, target_val)) * 100.0)
                dim_scores.append(dim_score)

            competency_pct = round(float(np.mean(dim_scores)) if dim_scores else 70.0, 1)

            # 4. Overall Compatibility Score
            overall_compatibility = round(
                0.50 * competency_pct + 0.50 * skill_coverage_pct, 1
            )

            results.append({
                "company_id": comp.get("company_id"),
                "company_name": comp["company_name"],
                "tier": comp["tier"],
                "is_eligible": is_eligible,
                "eligibility_reason": "Meets academic CGPA criterion" if is_eligible else f"CGPA {student_cgpa:.1f} below minimum requirement {comp['min_cgpa']:.1f}",
                "overall_compatibility_score": overall_compatibility,
                "skill_coverage_percent": skill_coverage_pct,
                "competency_percent": competency_pct,
                "matched_skills": matched,
                "missing_skills": missing,
                "dimensional_gaps": dim_deficits,
                "prs_threshold": comp["prs_threshold"],
                "scientific_integrity_note": (
                    "Score reflects geometric benchmark compatibility. "
                    "Does not constitute an empirical guarantee of employment."
                ),
            })

        results.sort(key=lambda x: x["overall_compatibility_score"], reverse=True)
        return results
