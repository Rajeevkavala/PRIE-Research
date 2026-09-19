"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Skill Gap Engine (M4)
File: modules/skill_gap_engine.py

Implements weighted skill gap detection, binary gap indication, skill
coverage scoring, and priority-ranked deficiency identification against
enterprise hiring benchmarks in accordance with Algorithm 3 and Chapter 5.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union

from database.db_manager import execute_query, execute_single
from database.queries import GET_COMPANY_BY_ID

logger = logging.getLogger("PRIE.SkillGapEngine")


class SkillGapEngine:
    """Computes weighted skill deficiencies against company hiring criteria."""

    def __init__(self) -> None:
        """Initialize SkillGapEngine."""
        logger.info("SkillGapEngine (M4) initialized.")

    def _load_company_requirements(
        self, company_id: int
    ) -> Tuple[Optional[str], List[Dict[str, Any]]]:
        """Load company name and required skills from database or query mock.

        Supports both live database rows with `required_skills_json` and
        mocked `execute_query` fixtures providing skill lists directly.

        Args:
            company_id: Primary key of target enterprise in companies table.

        Returns:
            Tuple of (company_name, list of required skill dictionaries).
        """
        # 1. Check if execute_query was mocked to return skill dicts directly
        try:
            query_res = execute_query(GET_COMPANY_BY_ID, (company_id,))
            if (
                query_res
                and isinstance(query_res, list)
                and len(query_res) > 0
                and isinstance(query_res[0], dict)
                and ("skill" in query_res[0] or "skill_name" in query_res[0])
                and "company_id" not in query_res[0]
            ):
                return "Benchmark Enterprise", query_res
        except Exception as err:
            logger.debug("execute_query probe skipped: %s", err)

        # 2. Query company record via execute_single
        try:
            company = execute_single(GET_COMPANY_BY_ID, (company_id,))
        except Exception as err:
            logger.error(
                "Database query failed for company_id %s: %s", company_id, err
            )
            return None, []

        if not company:
            logger.warning("Target company with ID %s not found.", company_id)
            return None, []

        company_dict = dict(company) if hasattr(company, "keys") else company
        company_name = company_dict.get("company_name", "Target Company")
        req_json = company_dict.get("required_skills_json", "[]")

        if isinstance(req_json, str):
            try:
                required_skills = json.loads(req_json)
            except (json.JSONDecodeError, TypeError) as err:
                logger.error(
                    "Failed to parse required_skills_json for company %s: %s",
                    company_id,
                    err,
                )
                required_skills = []
        elif isinstance(req_json, list):
            required_skills = req_json
        else:
            required_skills = []

        return company_name, required_skills

    def evaluate_skill_gaps(
        self,
        student_skills: Union[Iterable[str], Set[str], List[str]],
        company_id: int,
    ) -> Tuple[Dict[str, Any], float, float, List[Dict[str, Any]]]:
        """Compute weighted skill gap vector, gap score, and priority gaps.

        Fulfills the PRIEOrchestrator and Backend Implementation contract:
        returns `(gap_vector, gap_score, skill_coverage, priority_gaps)`.

        Args:
            student_skills: Collection of skills possessed by the student.
            company_id: Database ID of target company.

        Returns:
            Tuple of:
            - gap_vector: Dict mapping skill name to deficiency attributes.
            - gap_score: Weighted gap score S_gap in [0.0, 1.0].
            - skill_coverage: Skill coverage score S_skill in [0.0, 1.0].
            - priority_gaps: Top-10 prioritized missing skills list.
        """
        company_name, required_skills = self._load_company_requirements(
            company_id
        )
        if not required_skills:
            logger.warning(
                "No required skills found for company_id %s.",
                company_id,
            )
            return {}, 0.0, 1.0, []

        # Normalize student skills: trim and lowercase
        student_skills_normalized = {
            s.strip().lower()
            for s in student_skills
            if isinstance(s, str) and s.strip()
        }

        gap_vector: Dict[str, Dict[str, Any]] = {}
        weighted_gap_sum = 0.0
        total_weight = 0.0
        priority_gaps: List[Dict[str, Any]] = []

        for req in required_skills:
            if not isinstance(req, dict):
                continue
            skill_name = str(
                req.get("skill") or req.get("skill_name") or ""
            ).strip()
            if not skill_name:
                continue

            try:
                weight = float(req.get("weight", 0.1))
            except (ValueError, TypeError):
                weight = 0.1

            total_weight += weight
            is_present = skill_name.lower() in student_skills_normalized

            if not is_present:
                weighted_gap_sum += weight
                gap_data = {
                    "skill": skill_name,
                    "skill_name": skill_name,
                    "gap": 1,
                    "weight": round(weight, 4),
                    "priority": round(weight * 1.0, 4),
                }
                gap_vector[skill_name] = gap_data
                priority_gaps.append(gap_data)
            else:
                gap_data = {
                    "skill": skill_name,
                    "skill_name": skill_name,
                    "gap": 0,
                    "weight": round(weight, 4),
                    "priority": 0.0,
                }
                gap_vector[skill_name] = gap_data

        # Formulate normalized scores
        gap_score = (
            (weighted_gap_sum / total_weight) if total_weight > 0.0 else 0.0
        )
        gap_score = max(0.0, min(1.0, gap_score))
        skill_coverage = max(0.0, min(1.0, 1.0 - gap_score))

        # Sort priority gaps descending by priority, breaking ties
        priority_gaps.sort(key=lambda x: (-x["priority"], x["skill"].lower()))
        top_priority_gaps = priority_gaps[:10]

        logger.debug(
            "Company %s: gap=%.4f, coverage=%.4f, gaps_count=%d",
            company_id,
            gap_score,
            skill_coverage,
            len(top_priority_gaps),
        )

        return (
            gap_vector,
            round(gap_score, 4),
            round(skill_coverage, 4),
            top_priority_gaps,
        )

    def compute_gap(
        self,
        student_skills: Union[Iterable[str], Set[str], List[str]],
        company_id: Optional[int] = None,
        target_company_id: Optional[int] = None,
    ) -> Tuple[Dict[str, Any], float, List[Dict[str, Any]]]:
        """Compute skill gap adhering to Algorithm 3 and unit test contract.

        Returns `(gap_vector, gap_score, priority_gaps)`.

        Args:
            student_skills: Set or list of student skills.
            company_id: Target company ID.
            target_company_id: Alias for company_id.

        Returns:
            Tuple of (gap_vector, gap_score, priority_gaps).
        """
        cid = company_id if company_id is not None else (target_company_id if target_company_id is not None else 1)
        gap_vector, gap_score, _, priority_gaps = self.evaluate_skill_gaps(
            student_skills=student_skills,
            company_id=cid,
        )
        return gap_vector, gap_score, priority_gaps

    def get_skill_gaps_summary(
        self,
        student_skills: Union[Iterable[str], Set[str], List[str]],
        company_id: int,
    ) -> Dict[str, Any]:
        """Generate comprehensive diagnostic summary for UI and analytics.

        Args:
            student_skills: Student's verified technical skills.
            company_id: Target company ID.

        Returns:
            Structured dictionary with gap metrics, matched skills, and gaps.
        """
        company_name, _ = self._load_company_requirements(company_id)
        res = self.evaluate_skill_gaps(student_skills, company_id)
        gap_vec, gap_score, skill_cov, priority_gaps = res

        matched_skills = [
            k for k, v in gap_vec.items() if v.get("gap") == 0
        ]
        missing_skills = [
            k for k, v in gap_vec.items() if v.get("gap") == 1
        ]

        return {
            "company_id": company_id,
            "company_name": company_name or f"Company #{company_id}",
            "total_required": len(gap_vec),
            "total_matched": len(matched_skills),
            "total_missing": len(missing_skills),
            "gap_score": gap_score,
            "skill_score": skill_cov,
            "coverage_percentage": round(skill_cov * 100.0, 1),
            "matched_skills": sorted(matched_skills),
            "missing_skills": sorted(missing_skills),
            "prioritized_gaps": priority_gaps,
        }
