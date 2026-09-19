"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Multi-Metric Company Readiness Predictor (M6)
File: modules/company_predictor.py

Evaluates multi-metric candidate alignment (technical skill overlap, CGPA
eligibility, and longitudinal PRS telemetry) against target enterprise hiring
criteria in accordance with Algorithm 6 and Chapter 5 Section 5.9.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union

from database.db_manager import execute_query, execute_single
from database.queries import (
    GET_ALL_COMPANIES,
    GET_COMPANY_BY_ID,
    GET_LATEST_PRS,
    GET_LATEST_RESUME,
    GET_STUDENT_BY_ID,
)

logger = logging.getLogger("PRIE.CompanyPredictor")


class CompanyReadinessPredictor:
    """Computes multi-metric company alignment and gap-to-target telemetry."""

    def __init__(self) -> None:
        """Initialize CompanyReadinessPredictor."""
        logger.info("CompanyReadinessPredictor (M6) initialized.")

    def evaluate_company_fit(
        self,
        student_id: int,
        company_id: int,
        student_skills: Optional[
            Union[Iterable[str], Set[str], List[str]]
        ] = None,
        current_prs: Optional[float] = None,
    ) -> Tuple[float, Dict[str, Any]]:
        """Compute composite company fit score and gap-to-target payload.

        Calculates multi-metric alignment adhering to Algorithm 6:
            S_company = 0.40 * Skill + 0.30 * CGPA + 0.30 * PRS

        Args:
            student_id: Primary key of student in students table.
            company_id: Primary key of target enterprise in companies table.
            student_skills: Optional explicit skill collection.
            current_prs: Optional explicit PRS score overriding DB.

        Returns:
            Tuple of:
            - S_company: Float composite alignment score in [0.0, 1.0].
            - gap_to_target: Structured dictionary containing missing skills,
              CGPA deficit, PRS deficit, and readiness percentage.
        """
        # 1. Fetch Student Profile
        student = None
        try:
            student = execute_single(GET_STUDENT_BY_ID, (student_id,))
        except Exception as err:
            logger.error("Failed to query student %s: %s", student_id, err)

        student_dict: Dict[str, Any] = (
            dict(student)
            if student and hasattr(student, "keys")
            else (student or {})
        )

        try:
            student_cgpa = float(student_dict.get("cgpa", 0.0) or 0.0)
        except (ValueError, TypeError):
            student_cgpa = 0.0

        # Collect student skills
        parsed_student_skills: Set[str] = set()
        if student_skills is not None:
            parsed_student_skills.update(
                s.strip()
                for s in student_skills
                if isinstance(s, str) and s.strip()
            )
        else:
            raw_skills = student_dict.get("skills_json", "[]")
            if isinstance(raw_skills, str):
                try:
                    loaded = json.loads(raw_skills)
                    if isinstance(loaded, list):
                        parsed_student_skills.update(
                            str(s).strip() for s in loaded if s
                        )
                except (json.JSONDecodeError, TypeError):
                    pass
            elif isinstance(raw_skills, list):
                parsed_student_skills.update(
                    str(s).strip() for s in raw_skills if s
                )

            # Check latest resume for additional skills if needed
            try:
                latest_resume = execute_single(
                    GET_LATEST_RESUME, (student_id,)
                )
                if latest_resume and latest_resume["extracted_skills_json"]:
                    res_skills = json.loads(
                        latest_resume["extracted_skills_json"]
                    )
                    if isinstance(res_skills, list):
                        parsed_student_skills.update(
                            str(s).strip() for s in res_skills if s
                        )
            except Exception as err:
                logger.debug(
                    "Resume skills skipped for %s: %s", student_id, err
                )

        # 2. Fetch Current PRS
        if current_prs is not None:
            try:
                prs_score = float(current_prs)
            except (ValueError, TypeError):
                prs_score = 50.0
        else:
            prs_score = 50.0  # Baseline neutral prior
            try:
                latest_prs_rec = execute_single(
                    GET_LATEST_PRS, (student_id,)
                )
                if latest_prs_rec:
                    rec_dict = (
                        dict(latest_prs_rec)
                        if hasattr(latest_prs_rec, "keys")
                        else latest_prs_rec
                    )
                    val = (
                        rec_dict.get("prs_score")
                        or rec_dict.get("prs_value")
                    )
                    if val is not None:
                        prs_score = float(val)
            except Exception as err:
                logger.debug(
                    "Latest PRS failed for student %s: %s", student_id, err
                )

        # 3. Fetch Company Criteria
        company = None
        try:
            company = execute_single(GET_COMPANY_BY_ID, (company_id,))
        except Exception as err:
            logger.error("Failed to query company %s: %s", company_id, err)

        if not company:
            logger.warning(
                "Company %s not found. Returning fallback.", company_id
            )
            fallback_payload = {
                "company_id": company_id,
                "company_name": f"Company #{company_id}",
                "tier": "Unknown",
                "readiness_percentage": 0.0,
                "company_fit_score": 0.0,
                "skill_alignment": 0.0,
                "cgpa_alignment": 0.0,
                "prs_alignment": 0.0,
                "skills_missing": [],
                "skills_matched": [],
                "cgpa_deficit": 0.0,
                "prs_deficit": 0.0,
                "target_cgpa": 0.0,
                "student_cgpa": round(student_cgpa, 2),
                "target_prs": 0.0,
                "student_prs": round(prs_score, 1),
            }
            return 0.0, fallback_payload

        comp_dict: Dict[str, Any] = (
            dict(company) if hasattr(company, "keys") else company
        )
        company_name = comp_dict.get("company_name", "Target Company")
        tier = comp_dict.get("tier", "N/A")

        try:
            min_cgpa = float(comp_dict.get("min_cgpa", 0.0) or 0.0)
        except (ValueError, TypeError):
            min_cgpa = 0.0

        try:
            prs_threshold = float(
                comp_dict.get("prs_threshold", 0.70) or 0.70
            )
        except (ValueError, TypeError):
            prs_threshold = 0.70

        target_prs_points = round(prs_threshold * 100.0, 1)

        req_json = comp_dict.get("required_skills_json", "[]")
        company_skills: List[str] = []
        if isinstance(req_json, str):
            try:
                parsed_reqs = json.loads(req_json)
                if isinstance(parsed_reqs, list):
                    for item in parsed_reqs:
                        if isinstance(item, dict):
                            s = item.get("skill") or item.get("skill_name")
                            if s:
                                company_skills.append(str(s).strip())
                        elif isinstance(item, str) and item.strip():
                            company_skills.append(item.strip())
            except (json.JSONDecodeError, TypeError):
                company_skills = []
        elif isinstance(req_json, list):
            for item in req_json:
                if isinstance(item, dict):
                    s = item.get("skill") or item.get("skill_name")
                    if s:
                        company_skills.append(str(s).strip())
                elif isinstance(item, str) and item.strip():
                    company_skills.append(item.strip())

        # 4. Compute Sub-Alignments

        # A. Skill Alignment
        student_skills_norm = {s.lower() for s in parsed_student_skills}
        matched_skills: List[str] = []
        missing_skills: List[str] = []

        for req_skill in company_skills:
            if req_skill.lower() in student_skills_norm:
                matched_skills.append(req_skill)
            else:
                missing_skills.append(req_skill)

        if len(company_skills) > 0:
            skill_alignment = len(matched_skills) / len(company_skills)
        else:
            skill_alignment = 1.0

        skill_alignment = max(0.0, min(1.0, skill_alignment))

        # B. CGPA Alignment
        if min_cgpa > 0.0:
            cgpa_alignment = min(1.0, student_cgpa / min_cgpa)
            cgpa_deficit = max(0.0, round(min_cgpa - student_cgpa, 2))
        else:
            cgpa_alignment = 1.0
            cgpa_deficit = 0.0

        cgpa_alignment = max(0.0, min(1.0, cgpa_alignment))

        # C. PRS Alignment
        if target_prs_points > 0.0:
            prs_alignment = min(1.0, prs_score / target_prs_points)
            prs_deficit = max(0.0, round(target_prs_points - prs_score, 1))
        else:
            prs_alignment = 1.0
            prs_deficit = 0.0

        prs_alignment = max(0.0, min(1.0, prs_alignment))

        # 5. Composite S_company
        s_company = (
            0.40 * skill_alignment
            + 0.30 * cgpa_alignment
            + 0.30 * prs_alignment
        )
        s_company = max(0.0, min(1.0, s_company))
        readiness_percentage = round(s_company * 100.0, 1)

        gap_to_target = {
            "company_id": company_id,
            "company_name": company_name,
            "tier": tier,
            "readiness_percentage": readiness_percentage,
            "company_fit_score": round(s_company, 4),
            "skill_alignment": round(skill_alignment, 4),
            "cgpa_alignment": round(cgpa_alignment, 4),
            "prs_alignment": round(prs_alignment, 4),
            "skills_missing": sorted(missing_skills),
            "skills_matched": sorted(matched_skills),
            "cgpa_deficit": cgpa_deficit,
            "prs_deficit": prs_deficit,
            "target_cgpa": min_cgpa,
            "student_cgpa": round(student_cgpa, 2),
            "target_prs": target_prs_points,
            "student_prs": round(prs_score, 1),
        }

        logger.debug(
            "Fit student %s vs %s: fit=%.4f (sk=%.3f, cg=%.3f, pr=%.3f)",
            student_id,
            company_name,
            s_company,
            skill_alignment,
            cgpa_alignment,
            prs_alignment,
        )

        return round(s_company, 4), gap_to_target

    def compute_alignment(
        self,
        student_id: int,
        company_id: int,
        student_skills: Optional[
            Union[Iterable[str], Set[str], List[str]]
        ] = None,
        current_prs: Optional[float] = None,
    ) -> Tuple[float, Dict[str, Any]]:
        """Alias for evaluate_company_fit adhering to Algorithm 6 naming."""
        return self.evaluate_company_fit(
            student_id=student_id,
            company_id=company_id,
            student_skills=student_skills,
            current_prs=current_prs,
        )

    def evaluate_all_companies(
        self,
        student_id: int,
        student_skills: Optional[
            Union[Iterable[str], Set[str], List[str]]
        ] = None,
        current_prs: Optional[float] = None,
    ) -> List[Dict[str, Any]]:
        """Evaluate student readiness across all enterprise profiles in the DB.

        Returns list of gap-to-target dictionaries sorted descending by score.

        Args:
            student_id: Student identifier.
            student_skills: Optional skill override.
            current_prs: Optional PRS score override.

        Returns:
            Ranked list of company readiness payloads.
        """
        companies = execute_query(GET_ALL_COMPANIES)
        if not companies:
            logger.warning("No companies found for portfolio evaluation.")
            return []

        results: List[Dict[str, Any]] = []
        for comp in companies:
            comp_id = comp["company_id"]
            _, payload = self.evaluate_company_fit(
                student_id=student_id,
                company_id=comp_id,
                student_skills=student_skills,
                current_prs=current_prs,
            )
            results.append(payload)

        # Sort descending by readiness percentage
        results.sort(key=lambda x: x["readiness_percentage"], reverse=True)
        return results
