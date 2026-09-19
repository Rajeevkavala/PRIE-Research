"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Personalized Recommendation Engine Module (M9)
File: modules/recommendation_engine.py

Implements Algorithm 5 (Personalized Learning Recommendation Engine):
- Content-based relevance matching against student prioritized skill gaps.
- Applies a 20% score boost (1.20x) when resource format matches student learning style:
  * visual -> video / course
  * reading -> article / documentation
  * practical -> practice_problem / problem_set
- Filters out already-completed recommendations for the student.
- Ranks candidate educational materials descending by relevance score.
- Returns top-N recommendations (default: 5) with personalized explanatory rationales.
- Safely persists recommendations to SQLite recommendations table.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Union

import config
from database import queries
from database.db_manager import (
    execute_insert,
    execute_query,
    execute_single,
    execute_update,
)

logger = logging.getLogger("PRIE.RecommendationEngine")


class RecommendationEngine:
    """Personalized Learning Recommendation Engine (Module M9).

    Ranks educational resources from the catalog by computing content relevance
    against the student's prioritized skill gap vector and boosting scores
    according to their individual learning style preference.
    """

    def __init__(self, student_id: Optional[int] = None) -> None:
        """Initialize the recommendation engine.

        Args:
            student_id: Optional default student identifier.
        """
        self.student_id = student_id
        self._catalog: List[Dict[str, Any]] = self._load_catalog()

    def _load_catalog(self) -> List[Dict[str, Any]]:
        """Load vetted resource catalog from static JSON file."""
        catalog_path: Path = getattr(
            config, "RESOURCE_LIBRARY_PATH", config.DATA_DIR / "resource_library.json"
        )
        if catalog_path.exists():
            try:
                with open(catalog_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
            except Exception as exc:
                logger.warning("Failed to load resource catalog JSON: %s", exc)
        return []

    def _get_student_learning_style(self, student_id: Optional[int]) -> str:
        """Query student's preferred learning style from database, or default.

        Args:
            student_id: Integer student ID.

        Returns:
            str: Learning style ('visual', 'reading', or 'practical').
        """
        if not student_id:
            return "practical"

        try:
            student = execute_single(queries.GET_STUDENT_BY_ID, (student_id,))
            if student and "learning_style" in student.keys() and student["learning_style"]:
                style = str(student["learning_style"]).lower().strip()
                if style in ("visual", "reading", "practical"):
                    return style
        except Exception as exc:
            logger.debug("Could not query student learning style: %s", exc)

        return "practical"

    def _map_style_to_format(self, learning_style: str) -> str:
        """Map learning style string to canonical resource format string."""
        mapping = {
            "visual": "video",
            "reading": "article",
            "practical": "practice_problem",
        }
        return mapping.get(str(learning_style).lower(), "video")

    def _get_completed_resource_identifiers(
        self, student_id: Optional[int]
    ) -> set[str]:
        """Fetch set of URLs and titles already marked completed by this student.

        Args:
            student_id: Integer student ID.

        Returns:
            set[str]: Set of lowercase completed URLs and titles.
        """
        if not student_id:
            return set()

        completed: set[str] = set()
        try:
            query = """
            SELECT title, url FROM recommendations
            WHERE student_id = ? AND is_completed = 1;
            """
            rows = execute_query(query, (student_id,))
            for row in rows:
                if "url" in row.keys() and row["url"]:
                    completed.add(str(row["url"]).strip().lower())
                if "title" in row.keys() and row["title"]:
                    completed.add(str(row["title"]).strip().lower())
        except Exception as exc:
            logger.debug("Could not fetch completed resources: %s", exc)

        return completed

    def _normalize_gap_weights(
        self, priority_gaps: Union[Dict[str, Any], List[Dict[str, Any]], None]
    ) -> Dict[str, float]:
        """Convert input gaps into a normalized dictionary of {skill_name_lower: weight}.

        Args:
            priority_gaps: Dict or List of gap representations.

        Returns:
            Dict[str, float]: Mapping of skill names (lowercase) to importance weights.
        """
        if not priority_gaps:
            return {}

        gap_weights: Dict[str, float] = {}

        if isinstance(priority_gaps, dict):
            for skill, info in priority_gaps.items():
                s_name = str(skill).strip().lower()
                if isinstance(info, dict):
                    gap_val = info.get("gap", 1)
                    if gap_val == 1 or gap_val is True:
                        w = float(info.get("priority", info.get("weight", 0.5)))
                        gap_weights[s_name] = max(gap_weights.get(s_name, 0.0), w)
                elif isinstance(info, (int, float)):
                    if float(info) > 0.0:
                        gap_weights[s_name] = max(gap_weights.get(s_name, 0.0), float(info))

        elif isinstance(priority_gaps, list):
            for item in priority_gaps:
                if isinstance(item, dict):
                    skill = item.get("skill") or item.get("skill_name") or item.get("topic")
                    if skill:
                        s_name = str(skill).strip().lower()
                        gap_val = item.get("gap", 1)
                        if gap_val == 1 or gap_val is True:
                            w = float(item.get("priority", item.get("weight", 0.5)))
                            gap_weights[s_name] = max(gap_weights.get(s_name, 0.0), w)

        return gap_weights

    def generate_recommendations(
        self,
        student_id: Optional[int] = None,
        priority_gaps: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None,
        top_n: int = getattr(config, "RECOMMENDATION_TOP_N", 5),
        persist: bool = True,
    ) -> List[Dict[str, Any]]:
        """Generate personalized resource recommendations using Algorithm 5.

        Args:
            student_id: Target student ID (falls back to self.student_id).
            priority_gaps: Optional explicit priority gaps. If None and student_id
                           is provided, gaps will be derived from StudentProfilingEngine
                           and SkillGapEngine if available.
            top_n: Number of top recommendations to return (default: 5).
            persist: Whether to insert generated recommendations into SQLite.

        Returns:
            List[Dict[str, Any]]: Top-N ranked recommendations with calibrated scores
            and customized explanation rationales.
        """
        effective_student_id = student_id or self.student_id
        learning_style = self._get_student_learning_style(effective_student_id)
        completed_set = self._get_completed_resource_identifiers(effective_student_id)

        # Build gap weights map
        gap_skills = self._normalize_gap_weights(priority_gaps)

        # Fallback: if no gaps provided and student_id is available, attempt to derive
        if not gap_skills and effective_student_id is not None:
            try:
                from modules.skill_gap_engine import SkillGapEngine

                student_row = execute_single(queries.GET_STUDENT_BY_ID, (effective_student_id,))
                if student_row:
                    skills_raw = student_row["skills_json"] if "skills_json" in student_row.keys() else "[]"
                    profile_skills = json.loads(skills_raw) if skills_raw else []
                    target_company_id = student_row["target_company_id"] if "target_company_id" in student_row.keys() else 1
                    sge = SkillGapEngine()
                    _, _, derived_priority_gaps = sge.compute_gap(
                        student_skills=profile_skills,
                        company_id=target_company_id,
                    )
                    gap_skills = self._normalize_gap_weights(derived_priority_gaps)
            except Exception as exc:
                logger.debug("Could not automatically derive student gaps: %s", exc)

        scored_resources: List[Dict[str, Any]] = []

        # Preferred format mapping for 20% boost
        style_formats = {
            "visual": ["video", "course"],
            "reading": ["article", "documentation"],
            "practical": ["practice_problem", "problem_set", "course"],
        }
        preferred_types = style_formats.get(learning_style, ["practice_problem"])
        boost_multiplier = getattr(config, "LEARNING_STYLE_BOOST", 1.20)

        for item in self._catalog:
            item_url = str(item.get("url", "")).strip().lower()
            item_title = str(item.get("title", "")).strip().lower()
            item_topic = str(item.get("topic", "")).strip().lower()
            res_type = str(item.get("resource_type", "")).strip().lower()

            # Skip resources already completed by this student
            if item_url in completed_set or item_title in completed_set:
                continue

            # Compute gap relevance match
            # Check if catalog topic or title matches any gap skill
            matched_gap_weight: Optional[float] = None
            matched_skill_name: Optional[str] = None

            for skill_name, weight in gap_skills.items():
                if (
                    skill_name in item_topic
                    or item_topic in skill_name
                    or skill_name in item_title
                ):
                    if matched_gap_weight is None or weight > matched_gap_weight:
                        matched_gap_weight = weight
                        matched_skill_name = skill_name

            base_catalog_score = float(item.get("relevance_score", 0.85))

            if matched_gap_weight is not None:
                # Direct gap match: combine catalog baseline and gap importance
                base_relevance = 0.60 * matched_gap_weight + 0.40 * base_catalog_score
                is_gap_targeted = True
            else:
                # General foundational recommendation when no specific gap matches
                base_relevance = 0.35 * base_catalog_score
                is_gap_targeted = False

            # Apply 20% learning-style boost for preferred format
            is_boosted = res_type in preferred_types
            style_boost = boost_multiplier if is_boosted else 1.00
            final_score = min(1.00, round(base_relevance * style_boost, 3))

            # Build personalized explanation reason
            if is_gap_targeted and matched_skill_name:
                reason = (
                    f"Targets priority gap in {item.get('topic')} "
                    f"(calibrated for {learning_style} learners)"
                )
            else:
                reason = (
                    f"Recommended core foundation in {item.get('topic')} "
                    f"aligned with your {learning_style} learning preference"
                )

            scored_resources.append(
                {
                    "title": item.get("title", ""),
                    "topic": item.get("topic", "Computer Science"),
                    "resource_type": item.get("resource_type", "article"),
                    "url": item.get("url", ""),
                    "difficulty": item.get("difficulty", "intermediate"),
                    "platform": item.get("platform", "Web"),
                    "relevance_score": final_score,
                    "reason": reason,
                    "is_completed": 0,
                }
            )

        # Sort strictly descending by relevance_score, breaking ties by title
        scored_resources.sort(
            key=lambda x: (x["relevance_score"], x["title"]), reverse=True
        )
        top_recommendations = scored_resources[:top_n]

        # Persist to database if requested
        if persist and effective_student_id is not None and top_recommendations:
            self._persist_recommendations(effective_student_id, top_recommendations)

        return top_recommendations

    def get_recommendations(
        self,
        student_id: Optional[int] = None,
        top_n: int = getattr(config, "RECOMMENDATION_TOP_N", 5),
    ) -> List[Dict[str, Any]]:
        """Orchestrator-friendly alias returning top-N recommendations.

        Args:
            student_id: Optional target student ID.
            top_n: Count of recommendations.

        Returns:
            List[Dict[str, Any]]: Ranked recommendations.
        """
        return self.generate_recommendations(
            student_id=student_id,
            priority_gaps=None,
            top_n=top_n,
            persist=True,
        )

    def _persist_recommendations(
        self, student_id: int, recommendations: List[Dict[str, Any]]
    ) -> None:
        """Persist generated recommendations into SQLite recommendations table.

        Args:
            student_id: Integer student ID.
            recommendations: List of recommendation dicts.
        """
        try:
            for rec in recommendations:
                params = (
                    student_id,
                    rec.get("title", ""),
                    rec.get("topic", ""),
                    rec.get("resource_type", "article"),
                    rec.get("url", ""),
                    rec.get("difficulty", "intermediate"),
                    rec.get("platform", "Web"),
                    rec.get("relevance_score", 0.5),
                    rec.get("reason", ""),
                    0,  # is_completed default 0
                )
                try:
                    execute_insert(queries.INSERT_RECOMMENDATION, params)
                except Exception:
                    execute_query(queries.INSERT_RECOMMENDATION, params)

            logger.info(
                "Persisted %d recommendations to SQLite for student_id=%d",
                len(recommendations),
                student_id,
            )
        except Exception as exc:
            logger.error("Failed to persist recommendations to database: %s", exc)

    def mark_completed(self, rec_id: int, student_id: Optional[int] = None) -> bool:
        """Mark a specific recommendation as completed by the student.

        Args:
            rec_id: Recommendation database ID.
            student_id: Student ID.

        Returns:
            bool: True if successfully marked, False otherwise.
        """
        effective_student_id = student_id or self.student_id
        if effective_student_id is None:
            logger.error("Cannot mark recommendation complete without student_id")
            return False

        try:
            params = (rec_id, effective_student_id)
            try:
                rows_affected = execute_update(queries.MARK_RECOMMENDATION_COMPLETE, params)
            except Exception:
                rows_affected = execute_query(queries.MARK_RECOMMENDATION_COMPLETE, params)

            return True
        except Exception as exc:
            logger.error(
                "Failed to mark recommendation rec_id=%d complete: %s", rec_id, exc
            )
            return False

    def get_student_recommendations(
        self, student_id: int, limit: int = getattr(config, "RECOMMENDATION_TOP_N", 5)
    ) -> List[Dict[str, Any]]:
        """Retrieve stored recommendations for a student from SQLite.

        Args:
            student_id: Integer student ID.
            limit: Maximum count to return.

        Returns:
            List[Dict[str, Any]]: List of persisted recommendation records.
        """
        try:
            rows = execute_query(
                queries.GET_STUDENT_RECOMMENDATIONS, (student_id, limit)
            )
            result: List[Dict[str, Any]] = []
            for r in rows:
                result.append(
                    {
                        "rec_id": r["rec_id"] if "rec_id" in r.keys() else None,
                        "student_id": r["student_id"],
                        "title": r["title"],
                        "topic": r["topic"],
                        "resource_type": r["resource_type"],
                        "url": r["url"],
                        "difficulty": r["difficulty"] if "difficulty" in r.keys() else "intermediate",
                        "platform": r["platform"] if "platform" in r.keys() else "Web",
                        "relevance_score": r["relevance_score"],
                        "reason": r["reason"] if "reason" in r.keys() else "",
                        "is_completed": r["is_completed"] if "is_completed" in r.keys() else 0,
                        "recommended_at": r["recommended_at"] if "recommended_at" in r.keys() else None,
                        "completed_at": r["completed_at"] if "completed_at" in r.keys() else None,
                    }
                )
            return result
        except Exception as exc:
            logger.error("Failed to query student recommendations: %s", exc)
            return []
