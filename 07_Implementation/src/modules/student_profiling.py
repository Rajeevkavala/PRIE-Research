"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module 1: Student Profiling Engine (SPE)
File: modules/student_profiling.py

Constructs and manages the 22-dimensional Student Profile Vector (SPV), computes
profile completeness scores, encodes categorical academic and career attributes,
and aggregates assessment and resume performance signals.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

from database import queries
from database.db_manager import execute_query, execute_single, execute_update

logger = logging.getLogger("PRIE.StudentProfiling")

# Categorical branch academic encoding mappings
BRANCH_MAP: Dict[str, float] = {
    "computer science": 0.95,
    "computer science & engineering": 0.95,
    "computer science and engineering": 0.95,
    "cse": 0.95,
    "information technology": 0.90,
    "it": 0.90,
    "artificial intelligence": 0.92,
    "ai & ds": 0.92,
    "electronics & communication": 0.75,
    "electronics and communication": 0.75,
    "electronics": 0.75,
    "ece": 0.75,
    "electrical & electronics": 0.65,
    "electrical and electronics": 0.65,
    "electrical": 0.65,
    "eee": 0.65,
    "mechanical": 0.50,
    "mechanical engineering": 0.50,
    "mech": 0.50,
    "civil": 0.45,
    "civil engineering": 0.45,
}

# Categorical target role career encoding mappings
ROLE_MAP: Dict[str, float] = {
    "software development engineer": 0.90,
    "sde": 0.90,
    "software engineer": 0.90,
    "full stack developer": 0.88,
    "backend developer": 0.88,
    "frontend developer": 0.82,
    "data scientist": 0.85,
    "machine learning engineer": 0.88,
    "cloud engineer": 0.80,
    "devops engineer": 0.82,
    "data analyst": 0.75,
    "business analyst": 0.70,
    "qa engineer": 0.65,
    "quality assurance": 0.65,
    "security analyst": 0.78,
}

# Canonical 22-dimensional SPV feature names matching ML pipeline
SPV_FEATURE_NAMES: List[str] = [
    "cgpa",
    "backlogs",
    "internship_months",
    "skill_count",
    "certification_count",
    "project_count",
    "aptitude_score",
    "dsa_score",
    "dbms_score",
    "cn_score",
    "programming_score",
    "resume_ats_score",
    "cosine_similarity",
    "gap_score",
    "consistency_score",
    "has_internship",
    "branch_encoded",
    "target_role_encoded",
    "assessment_attempts",
    "behavior_score",
    "engagement_score",
    "roadmap_completion_rate",
]


class StudentProfilingEngine:
    """Foundational Data Acquisition Engine assembling the 22-D Student Profile Vector (SPV)."""

    def __init__(self, db_path: Optional[Union[str, Path]] = None) -> None:
        """Initialize the Student Profiling Engine.

        Args:
            db_path: Optional explicit database path for isolated environments.
        """
        self.db_path = db_path

    def extract_skills(self, student_id: int) -> List[str]:
        """Extract unique technical skills for a student from their latest resume and profile.

        Args:
            student_id: Primary key of student.

        Returns:
            List[str]: Alphabetically sorted list of verified technical skills.
        """
        skills_set = set()
        # 1. From latest resume if available
        resume_row = execute_single(
            queries.GET_LATEST_RESUME,
            (student_id,),
            db_path=self.db_path,
        )
        if resume_row and resume_row.get("extracted_skills_json"):
            try:
                r_skills = json.loads(resume_row["extracted_skills_json"])
                if isinstance(r_skills, list):
                    skills_set.update(r_skills)
            except Exception:
                pass

        # 2. From student table skills_json
        student_row = execute_single(
            queries.GET_STUDENT_BY_ID,
            (student_id,),
            db_path=self.db_path,
        )
        if student_row and student_row.get("skills_json"):
            try:
                s_skills = json.loads(student_row["skills_json"])
                if isinstance(s_skills, list):
                    skills_set.update(s_skills)
            except Exception:
                pass

        return sorted(list(skills_set))

    def encode_branch(self, branch: Optional[str]) -> float:
        """Encode academic engineering branch into normalized numeric weight.

        Args:
            branch: Academic discipline name string.

        Returns:
            float: Normalized weight in [0.45, 0.95]; defaults to 0.60 for unknown branches.
        """
        if not branch or not isinstance(branch, str):
            return 0.60
        cleaned = branch.strip().lower()
        return BRANCH_MAP.get(cleaned, 0.60)

    def encode_role(self, role: Optional[str]) -> float:
        """Encode target career job profile into normalized numeric weight.

        Args:
            role: Target job title string.

        Returns:
            float: Normalized weight in [0.65, 0.90]; defaults to 0.70 for unlisted roles.
        """
        if not role or not isinstance(role, str):
            return 0.70
        cleaned = role.strip().lower()
        return ROLE_MAP.get(cleaned, 0.70)

    def assemble_feature_vector(self, student_id: int) -> Tuple[np.ndarray, float]:
        """Assemble the complete 22-dimensional Student Profile Vector (SPV).

        Extracts academic credentials, internship history, skill counts, assessment
        topic averages, latest resume ATS scores, and behavioral telemetry priors.

        Args:
            student_id: Primary key of student.

        Returns:
            Tuple[np.ndarray, float]: (feature_vector_22d, completeness_score_0_to_1)

        Raises:
            ValueError: If student record does not exist in database.
        """
        student_row = execute_single(
            queries.GET_STUDENT_BY_ID,
            (student_id,),
            db_path=self.db_path,
        )
        if not student_row:
            raise ValueError(f"Student with ID {student_id} not found in database.")

        student = dict(student_row)
        assessments_rows = execute_query(
            queries.GET_STUDENT_ASSESSMENTS,
            (student_id,),
            db_path=self.db_path,
        )
        assessments = [dict(a) for a in assessments_rows]

        resume_row = execute_single(
            queries.GET_LATEST_RESUME,
            (student_id,),
            db_path=self.db_path,
        )
        resume = dict(resume_row) if resume_row else None

        # 1. Academic & Demographics
        cgpa = float(student.get("cgpa", 0.0) or 0.0)
        backlogs = int(student.get("backlogs", 0) or 0)
        branch_str = str(student.get("branch", ""))
        branch_encoded = self.encode_branch(branch_str)

        # 2. Internships & Experience
        internship_months = int(student.get("internship_months", 0) or 0)
        internship_status = str(student.get("internship_status", "None"))
        has_internship = 1 if (internship_months > 0 or internship_status.lower() in ["completed", "ongoing"]) else 0

        # 3. Skills & Targets
        skills_raw = student.get("skills_json", "[]") or "[]"
        try:
            skills = json.loads(skills_raw)
            if not isinstance(skills, list):
                skills = []
        except Exception:
            skills = []
        skill_count = len(skills)

        target_role = str(student.get("target_role", ""))
        target_role_encoded = self.encode_role(target_role)

        # 4. Project & Certification counts
        certification_count = int(student.get("certification_count", 0) or 0)
        project_count = int(student.get("project_count", 0) or 0)
        # Apply calibrated default priors if unrecorded
        if certification_count == 0:
            certification_count = 1
        if project_count == 0:
            project_count = 2

        # 5. Diagnostic Assessment Performance by Subject Area
        aptitude_scores: List[float] = []
        dsa_scores: List[float] = []
        programming_scores: List[float] = []
        dbms_scores: List[float] = []
        cn_scores: List[float] = []

        for a in assessments:
            topic = str(a.get("topic", "")).lower()
            total_q = int(a.get("total_questions", 1) or 1)
            score = int(a.get("score", 0) or 0)
            percentage = (score / total_q) * 100.0 if total_q > 0 else 0.0

            if "aptitude" in topic:
                aptitude_scores.append(percentage)
            elif any(k in topic for k in ["dsa", "data structure", "algorithm"]):
                dsa_scores.append(percentage)
            elif any(k in topic for k in ["programming", "python", "java", "c++"]):
                programming_scores.append(percentage)
            elif "dbms" in topic or "database" in topic or "sql" in topic:
                dbms_scores.append(percentage)
            elif any(k in topic for k in ["computer network", "networking", "cn"]):
                cn_scores.append(percentage)

        aptitude_score = float(np.mean(aptitude_scores)) if aptitude_scores else 60.0
        dsa_score = float(np.mean(dsa_scores)) if dsa_scores else 50.0
        programming_score = float(np.mean(programming_scores)) if programming_scores else 55.0
        dbms_score = float(np.mean(dbms_scores)) if dbms_scores else 70.0
        cn_score = float(np.mean(cn_scores)) if cn_scores else 65.0
        assessment_attempts = len(assessments)

        # 6. Resume ATS and NLP Embeddings
        resume_ats = float(resume.get("ats_score", 40.0) or 40.0) if resume else 40.0
        cosine_sim = float(resume.get("cosine_similarity", 0.40) or 0.40) if resume else 0.40

        # 7. Behavioral and Alignment Telemetry Priors
        gap_score = 0.35
        consistency_score = 0.60
        behavior_score = 0.65
        engagement_score = 0.70
        roadmap_completion_rate = 0.30

        # Construct exact 22-dimensional feature vector
        features = [
            float(cgpa),
            float(backlogs),
            float(internship_months),
            float(skill_count),
            float(certification_count),
            float(project_count),
            float(aptitude_score),
            float(dsa_score),
            float(dbms_score),
            float(cn_score),
            float(programming_score),
            float(resume_ats),
            float(cosine_sim),
            float(gap_score),
            float(consistency_score),
            float(has_internship),
            float(branch_encoded),
            float(target_role_encoded),
            float(assessment_attempts),
            float(behavior_score),
            float(engagement_score),
            float(roadmap_completion_rate),
        ]

        # Calculate profile completeness score
        completeness = self._calculate_completeness(student, resume, assessments)

        # Persist updated completeness in students table
        try:
            execute_update(
                queries.UPDATE_STUDENT_COMPLETENESS,
                (round(completeness * 100.0, 1), student_id),
                db_path=self.db_path,
            )
        except Exception as exc:
            logger.warning("Could not sync profile_completeness: %s", exc)

        return np.array(features, dtype=np.float32), completeness

    def get_feature_vector(self, student_id: int) -> np.ndarray:
        """Convenience method returning solely the 22-dimensional numpy array.

        Args:
            student_id: Primary key of student.

        Returns:
            np.ndarray: 22-dimensional float32 vector.
        """
        vector, _ = self.assemble_feature_vector(student_id)
        return vector

    def get_feature_dict(self, student_id: int) -> Dict[str, Any]:
        """Assemble feature vector as a dictionary mapped by canonical feature names.

        Args:
            student_id: Primary key of student.

        Returns:
            Dict[str, Any]: Feature names mapped to their respective scalar values.
        """
        vector, completeness = self.assemble_feature_vector(student_id)
        feature_dict = {
            name: float(val) for name, val in zip(SPV_FEATURE_NAMES, vector)
        }
        feature_dict["profile_completeness"] = float(completeness)
        return feature_dict

    def _calculate_completeness(
        self,
        student: Dict[str, Any],
        resume: Optional[Dict[str, Any]],
        assessments: List[Dict[str, Any]],
    ) -> float:
        """Compute the standardized Profile Completeness Score (0.0 to 1.0).

        Scoring Rules:
        - CGPA filled & > 0: +0.20
        - At least 3 skills declared: +0.20
        - Target role and target company specified: +0.15
        - At least one resume uploaded: +0.25
        - At least one diagnostic assessment taken: +0.20
        Total: 1.00 (100%)

        Args:
            student: Student database record.
            resume: Latest resume record or None.
            assessments: List of student assessment records.

        Returns:
            float: Normalized completeness score in [0.0, 1.0].
        """
        points = 0.0

        # CGPA entered
        if float(student.get("cgpa", 0.0) or 0.0) > 0.0:
            points += 0.20

        # Skills list has at least 3 items
        skills_raw = student.get("skills_json", "[]") or "[]"
        try:
            skills = json.loads(skills_raw)
            if isinstance(skills, list) and len(skills) >= 3:
                points += 0.20
        except Exception:
            pass

        # Target role or company
        has_role = bool(student.get("target_role"))
        has_company = bool(student.get("target_company_id"))
        if has_role or has_company:
            points += 0.15

        # Resume present
        if resume is not None and bool(resume.get("file_path")):
            points += 0.25

        # Assessment attempts
        if assessments and len(assessments) > 0:
            points += 0.20

        return round(min(1.0, max(0.0, points)), 2)

    def update_profile(
        self,
        student_id: int,
        profile_data: Dict[str, Any],
    ) -> bool:
        """Update student profile fields and recalculate completeness.

        Args:
            student_id: Primary key of student.
            profile_data: Dictionary containing fields to update.

        Returns:
            bool: True if update succeeded; False otherwise.
        """
        current_row = execute_single(
            queries.GET_STUDENT_BY_ID,
            (student_id,),
            db_path=self.db_path,
        )
        if not current_row:
            return False

        current = dict(current_row)
        name = profile_data.get("name", current.get("name"))
        branch = profile_data.get("branch", current.get("branch"))
        cgpa = profile_data.get("cgpa", current.get("cgpa"))
        backlogs = profile_data.get("backlogs", current.get("backlogs"))
        skills_json = profile_data.get("skills_json", current.get("skills_json"))
        internship_status = profile_data.get("internship_status", current.get("internship_status"))
        internship_months = profile_data.get("internship_months", current.get("internship_months"))
        target_role = profile_data.get("target_role", current.get("target_role"))
        target_company_id = profile_data.get("target_company_id", current.get("target_company_id"))
        learning_style = profile_data.get("learning_style", current.get("learning_style"))
        cert_count = profile_data.get("certification_count", current.get("certification_count", 0))
        proj_count = profile_data.get("project_count", current.get("project_count", 0))

        # Perform update
        rows_affected = execute_update(
            queries.UPDATE_STUDENT_PROFILE,
            (
                name,
                branch,
                cgpa,
                backlogs,
                skills_json,
                internship_status,
                internship_months,
                target_role,
                target_company_id,
                learning_style,
                current.get("profile_completeness", 0.0),
                cert_count,
                proj_count,
                student_id,
            ),
            db_path=self.db_path,
        )

        # Re-assemble to trigger completeness calculation and persistence
        self.assemble_feature_vector(student_id)
        return rows_affected > 0
