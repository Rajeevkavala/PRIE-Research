"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module 2: Assessment Intelligence Engine (AIE)
File: modules/assessment_engine.py

Pedagogical Framework:
- Bloom's Revised Taxonomy (Easy: Remember/Understand, Medium: Apply, Hard: Analyze/Evaluate)
- Vygotsky's Zone of Proximal Development (ZPD) with 2-consecutive streak adaptive modulation
- Weighted accuracy score S_assessment:
    S_assessment = sum(w(d_i) * r_i) / sum(w(d_i))
    where w(Easy)=1.0, w(Medium)=1.5, w(Hard)=2.0
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from database.db_manager import execute_insert, execute_query, execute_single
from database import queries

logger = logging.getLogger("PRIE.AssessmentEngine")

DIFFICULTY_WEIGHTS: Dict[str, float] = {
    "Easy": 1.0,
    "Medium": 1.5,
    "Hard": 2.0,
    "easy": 1.0,
    "medium": 1.5,
    "hard": 2.0,
}

DIFFICULTY_TIERS: List[str] = ["Easy", "Medium", "Hard"]


class AssessmentIntelligenceEngine:
    """Delivers adaptive quiz sequencing, real-time difficulty progression,
    and calculates difficulty-weighted mastery scores (S_assessment).
    """

    def __init__(self, db_path: Optional[Union[str, Path]] = None) -> None:
        """Initializes the Assessment Intelligence Engine."""
        self.db_path = db_path
        self.weights = DIFFICULTY_WEIGHTS
        self.tiers = DIFFICULTY_TIERS

    def get_adaptive_question(
        self,
        topic: str,
        current_difficulty: str,
        excluded_ids: Optional[List[int]] = None,
    ) -> Optional[Dict[str, Any]]:
        """Fetches an unused diagnostic question matching topic and targeted difficulty tier.
        Falls back to adjacent tiers within the topic if the targeted tier is exhausted.

        Args:
            topic: Technical discipline (e.g. 'Data Structures', 'DBMS').
            current_difficulty: Difficulty tier ('Easy', 'Medium', 'Hard').
            excluded_ids: List of question IDs already attempted in this session.

        Returns:
            Optional[Dict[str, Any]]: Question record with parsed 'options' list, or None if topic exhausted.
        """
        excluded = list(excluded_ids) if excluded_ids else []
        norm_diff = current_difficulty.capitalize()

        if excluded:
            placeholders = ",".join("?" for _ in excluded)
            query_primary = f"""
                SELECT * FROM question_bank
                WHERE LOWER(topic) = LOWER(?) AND LOWER(difficulty) = LOWER(?)
                  AND question_id NOT IN ({placeholders})
                ORDER BY RANDOM()
                LIMIT 1;
            """
            params_primary = [topic, norm_diff] + excluded
        else:
            query_primary = """
                SELECT * FROM question_bank
                WHERE LOWER(topic) = LOWER(?) AND LOWER(difficulty) = LOWER(?)
                ORDER BY RANDOM()
                LIMIT 1;
            """
            params_primary = [topic, norm_diff]

        row = execute_single(query_primary, tuple(params_primary))

        # Fallback to any difficulty tier in the same topic if current tier is exhausted
        if not row:
            logger.debug(
                "Difficulty tier '%s' exhausted for topic '%s'. Attempting fallback.",
                norm_diff,
                topic,
            )
            if excluded:
                query_fallback = f"""
                    SELECT * FROM question_bank
                    WHERE LOWER(topic) = LOWER(?)
                      AND question_id NOT IN ({placeholders})
                    ORDER BY RANDOM()
                    LIMIT 1;
                """
                params_fallback = [topic] + excluded
            else:
                query_fallback = """
                    SELECT * FROM question_bank
                    WHERE LOWER(topic) = LOWER(?)
                    ORDER BY RANDOM()
                    LIMIT 1;
                """
                params_fallback = [topic]

            row = execute_single(query_fallback, tuple(params_fallback))

        if not row:
            logger.warning("No questions available in question_bank for topic '%s'.", topic)
            return None

        question = dict(row)
        # Parse options JSON into Python list of strings
        if isinstance(question.get("options_json"), str):
            try:
                question["options"] = json.loads(question["options_json"])
            except Exception as e:
                logger.error("Failed to parse options_json for question %s: %s", question.get("question_id"), e)
                question["options"] = []
        elif isinstance(question.get("options_json"), list):
            question["options"] = question["options_json"]
        else:
            question["options"] = []

        return question

    def update_difficulty(
        self,
        current_difficulty: str,
        consecutive_correct: int = 0,
        consecutive_incorrect: int = 0,
        streak: Optional[int] = None,
        is_correct: Optional[bool] = None,
    ) -> Any:
        """Evaluates the 2-consecutive streak difficulty state machine.

        Supports both:
        1. Legacy (consecutive_correct, consecutive_incorrect) -> (new_diff, c_correct, c_incorrect)
        2. Signed streak (streak, is_correct) -> (new_diff, new_streak)

        Args:
            current_difficulty: Current difficulty tier ('Easy', 'Medium', 'Hard').
            consecutive_correct: Count of consecutive correct answers.
            consecutive_incorrect: Count of consecutive incorrect answers.
            streak: Signed streak (+ for correct, - for incorrect).
            is_correct: Boolean indicating if current answer was correct.

        Returns:
            Tuple[str, int, int] or Tuple[str, int] depending on invocation mode.
        """
        curr = current_difficulty.capitalize()
        if curr not in self.tiers:
            curr = "Medium"

        idx = self.tiers.index(curr)

        if streak is not None or is_correct is not None:
            s = streak or 0
            if is_correct:
                s = (s + 1) if s > 0 else 1
                if s >= 2:
                    new_idx = min(idx + 1, len(self.tiers) - 1)
                    return self.tiers[new_idx], 0
                return self.tiers[idx], s
            else:
                s = (s - 1) if s < 0 else -1
                if s <= -2:
                    new_idx = max(idx - 1, 0)
                    return self.tiers[new_idx], 0
                return self.tiers[idx], s

        if consecutive_correct >= 2:
            new_idx = min(idx + 1, len(self.tiers) - 1)
            new_diff = self.tiers[new_idx]
            return new_diff, 0, 0

        if consecutive_incorrect >= 2:
            new_idx = max(idx - 1, 0)
            new_diff = self.tiers[new_idx]
            return new_diff, 0, 0

        return self.tiers[idx], consecutive_correct, consecutive_incorrect

    def compute_session_score(
        self,
        history: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Calculates detailed scoring analytics for an active quiz session.

        Args:
            history: List of question outcome dictionaries containing:
                     'difficulty', 'correct' (bool), and 'question_id'.

        Returns:
            Dict[str, Any]: {
                'raw_score': int,
                'total_questions': int,
                'accuracy_percentage': float,
                'weighted_score': float,
                'max_weighted_score': float,
                'weighted_accuracy': float,
                'difficulty_breakdown': Dict[str, Dict[str, int]]
            }
        """
        if not history:
            return {
                "raw_score": 0,
                "total_questions": 0,
                "accuracy_percentage": 0.0,
                "weighted_score": 0.0,
                "max_weighted_score": 0.0,
                "weighted_accuracy": 0.0,
                "difficulty_breakdown": {t: {"correct": 0, "total": 0} for t in self.tiers},
            }

        raw_score = sum(1 for item in history if item.get("correct"))
        total = len(history)
        weighted_score = 0.0
        max_weighted_score = 0.0
        breakdown = {t: {"correct": 0, "total": 0} for t in self.tiers}

        for item in history:
            diff = str(item.get("difficulty", "Medium")).capitalize()
            w = self.weights.get(diff, 1.5)
            is_correct = bool(item.get("correct"))

            max_weighted_score += w
            if is_correct:
                weighted_score += w
                if diff in breakdown:
                    breakdown[diff]["correct"] += 1

            if diff in breakdown:
                breakdown[diff]["total"] += 1

        weighted_acc = (weighted_score / max_weighted_score) if max_weighted_score > 0 else 0.0
        acc_pct = (raw_score / total * 100.0) if total > 0 else 0.0

        return {
            "raw_score": raw_score,
            "total_questions": total,
            "accuracy_percentage": round(acc_pct, 1),
            "weighted_score": round(weighted_score, 2),
            "max_weighted_score": round(max_weighted_score, 2),
            "weighted_accuracy": round(min(1.0, max(0.0, weighted_acc)), 4),
            "difficulty_breakdown": breakdown,
        }

    def compute_assessment_score(self, student_id: int) -> float:
        """Calculates historical weighted assessment accuracy S_assessment in [0.0, 1.0].

        Formula:
            S_assessment = sum(w(d_i) * r_i) / sum(w(d_i))
            where weights are Easy = 1.0, Medium = 1.5, Hard = 2.0.

        Args:
            student_id: Unique integer identifier of the student.

        Returns:
            float: Weighted accuracy score in [0.0, 1.0].
                   Returns 0.50 uncalibrated prior if student has taken no assessments.
        """
        assessments = execute_query(
            queries.GET_STUDENT_ASSESSMENTS, (student_id,), db_path=self.db_path
        )

        if not assessments:
            return 0.50  # Uncalibrated baseline prior per PRIE specifications

        total_weighted_points = 0.0
        total_weighted_possible = 0.0

        for row_item in assessments:
            a = dict(row_item) if not isinstance(row_item, dict) else row_item
            diff = str(a.get("difficulty", "Medium")).capitalize()
            w = self.weights.get(diff, 1.5)
            score = float(a.get("score", 0))
            total_q = float(a.get("total_questions", 1))

            total_weighted_points += score * w
            total_weighted_possible += total_q * w

        if total_weighted_possible <= 0.0:
            return 0.50

        s_assessment = total_weighted_points / total_weighted_possible
        return float(min(1.0, max(0.0, s_assessment)))

    def record_assessment(
        self,
        student_id: int,
        topic: str,
        difficulty: str,
        score: int,
        total_questions: int,
        time_taken_minutes: float = 0.0,
        question_id: Optional[int] = None,
    ) -> int:
        """Persists a completed assessment attempt to the database and logs a learning event.

        Args:
            student_id: Student ID.
            topic: Assessment topic.
            difficulty: Final difficulty tier reached ('Easy', 'Medium', 'Hard').
            score: Number of questions answered correctly.
            total_questions: Total number of questions in session.
            time_taken_minutes: Elapsed duration in minutes.
            question_id: Optional reference question ID.

        Returns:
            int: Inserted assessment_id.
        """
        norm_diff = difficulty.capitalize()

        assessment_id = execute_insert(
            queries.INSERT_ASSESSMENT,
            (
                student_id,
                question_id,
                topic,
                norm_diff,
                score,
                total_questions,
                round(time_taken_minutes, 2),
            ),
        )

        # Log learning event telemetry for LearningBehaviorAnalyzer
        try:
            event_detail = f"Completed {topic} quiz: {score}/{total_questions} ({norm_diff})"
            payload = json.dumps({
                "assessment_id": assessment_id,
                "topic": topic,
                "difficulty": norm_diff,
                "score": score,
                "total_questions": total_questions,
                "percentage": round((score / total_questions) * 100.0, 1) if total_questions > 0 else 0.0,
                "time_taken_minutes": time_taken_minutes,
            })
            execute_insert(
                queries.INSERT_LEARNING_EVENT,
                (
                    student_id,
                    "quiz_completed",
                    payload,
                    event_detail,
                    int(round(time_taken_minutes)),
                ),
            )
        except Exception as e:
            logger.warning("Failed to log learning event for quiz_completed: %s", e)

        logger.info(
            "Recorded assessment %d for student %d: %s (%d/%d at %s)",
            assessment_id,
            student_id,
            topic,
            score,
            total_questions,
            norm_diff,
        )
        return assessment_id

    def get_topic_summary(self, student_id: int) -> List[Dict[str, Any]]:
        """Retrieves topic-level performance metrics for the student.

        Args:
            student_id: Student ID.

        Returns:
            List[Dict[str, Any]]: Aggregated topic summary metrics.
        """
        rows = execute_query(queries.GET_STUDENT_TOPIC_STATS, (student_id,))
        return [dict(r) for r in rows] if rows else []

    def get_available_topics(self) -> List[str]:
        """Retrieves all distinct topics available in the question bank.

        Returns:
            List[str]: Sorted list of topic names.
        """
        rows = execute_query(queries.GET_DISTINCT_TOPICS)
        if rows:
            return [r["topic"] for r in rows]
        # Fallback default catalog
        return [
            "Data Structures",
            "Algorithms",
            "Database Management Systems",
            "Operating Systems",
            "Computer Networks",
            "Aptitude",
        ]
