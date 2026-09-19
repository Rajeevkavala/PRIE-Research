"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
System Usability Scale (SUS) Evaluation Engine
File: modules/sus_evaluator.py

Implements standardized System Usability Scale (SUS) scoring methodology
per John Brooke (1996) and adjective rating classification per Bangor et al. (2008).
Provides statistical aggregation, task completion metric tracking,
and automated Markdown report generation for user acceptance studies.
"""

from __future__ import annotations

import json
import logging
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

logger = logging.getLogger("PRIE.SUSEvaluator")


class SUSEvaluator:
    """Evaluates System Usability Scale (SUS) study outcomes and usability metrics.

    The System Usability Scale (SUS) is a 10-item Likert questionnaire
    giving a global view of subjective usability assessments (Brooke, 1996).
    """

    DEFAULT_DATA_PATH = Path("data/sus_evaluation_results.json")

    # Question polarities: 1-indexed. Positive = 1, 3, 5, 7, 9; Negative = 2, 4, 6, 8, 10
    ODD_QUESTIONS = (1, 3, 5, 7, 9)
    EVEN_QUESTIONS = (2, 4, 6, 8, 10)

    @staticmethod
    def compute_individual_sus(responses: Dict[Union[int, str], int]) -> float:
        """Computes the standardized SUS score (0 to 100) for an individual participant.

        Mathematical Formulation:
            Odd items (1, 3, 5, 7, 9): contribution = Score - 1
            Even items (2, 4, 6, 8, 10): contribution = 5 - Score
            SUS Score = 2.5 * sum(contributions)

        Args:
            responses: Dictionary mapping question number (1 to 10) to Likert rating (1 to 5).

        Returns:
            float: Calibrated SUS score strictly bounded in [0.0, 100.0].

        Raises:
            ValueError: If fewer than 10 questions provided or ratings outside [1, 5].
        """
        if not responses or len(responses) < 10:
            raise ValueError(f"SUS requires all 10 question responses, got {len(responses) if responses else 0}.")

        contributions: List[float] = []

        for q_id in range(1, 11):
            val = responses.get(q_id)
            if val is None:
                val = responses.get(str(q_id))

            if val is None:
                raise ValueError(f"Missing response for question ID {q_id}")

            try:
                numeric_val = int(val)
            except (ValueError, TypeError) as err:
                raise ValueError(f"Rating for question {q_id} must be an integer: {val}") from err

            if numeric_val < 1 or numeric_val > 5:
                raise ValueError(f"Question {q_id} rating must be between 1 and 5, got {numeric_val}")

            if q_id in SUSEvaluator.ODD_QUESTIONS:
                contributions.append(float(numeric_val - 1))
            else:
                contributions.append(float(5 - numeric_val))

        raw_score = sum(contributions) * 2.5
        clamped_score = max(0.0, min(100.0, float(raw_score)))
        return round(clamped_score, 2)

    @staticmethod
    def classify_adjective_rating(sus_score: float) -> Tuple[str, str]:
        """Maps a numeric SUS score to adjective rating and letter grade.

        Based on empirical benchmarks established by Bangor, Kortum, and Miller (2008):
        - >= 85.0: "Best Imaginable", Grade A+
        - >= 80.0: "Excellent", Grade A
        - >= 70.0: "Good", Grade B
        - >= 50.0: "OK", Grade C/D
        - < 50.0: "Poor / Not Acceptable", Grade F

        Args:
            sus_score: Float SUS score in [0.0, 100.0].

        Returns:
            Tuple[str, str]: (Adjective rating, Letter grade).
        """
        if sus_score >= 85.0:
            return "Best Imaginable", "A+"
        if sus_score >= 80.0:
            return "Excellent", "A"
        if sus_score >= 70.0:
            return "Good", "B"
        if sus_score >= 50.0:
            return "OK", "C/D"
        return "Poor", "F"

    def load_evaluation_data(self, data_path: Optional[Union[str, Path]] = None) -> Dict[str, Any]:
        """Loads the empirical SUS evaluation study data from JSON file.

        Args:
            data_path: Optional path to JSON dataset. Defaults to DEFAULT_DATA_PATH.

        Returns:
            Dict[str, Any]: Parsed JSON dataset dictionary.

        Raises:
            FileNotFoundError: If the evaluation JSON file cannot be found.
        """
        path = Path(data_path) if data_path else self.DEFAULT_DATA_PATH
        if not path.is_absolute():
            path = Path(__file__).resolve().parent.parent / path

        if not path.exists():
            raise FileNotFoundError(f"SUS evaluation dataset not found: {path}")

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception as err:
            logger.error("Failed to load SUS evaluation dataset from %s: %s", path, err)
            raise

    def compute_aggregate_metrics(
        self, study_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Computes cohort-level statistical aggregates for the SUS study.

        Args:
            study_data: Optional loaded study data. If None, loads from DEFAULT_DATA_PATH.

        Returns:
            Dict[str, Any]: Aggregated usability statistics, task metrics, and ratings.
        """
        if study_data is None:
            study_data = self.load_evaluation_data()

        participants: List[Dict[str, Any]] = study_data.get("participants", [])
        if not participants:
            return {
                "cohort_size": 0,
                "mean_sus": 0.0,
                "median_sus": 0.0,
                "std_sus": 0.0,
                "ci_95": (0.0, 0.0),
                "adjective_rating": "N/A",
                "grade": "N/A",
            }

        sus_scores: List[float] = []
        for p in participants:
            # Recompute or use verified score
            if "responses" in p:
                sc = self.compute_individual_sus(p["responses"])
            else:
                sc = float(p.get("sus_score", 0.0))
            sus_scores.append(sc)

        n = len(sus_scores)
        mean_score = sum(sus_scores) / n
        sorted_scores = sorted(sus_scores)
        median_score = (
            sorted_scores[n // 2]
            if n % 2 != 0
            else (sorted_scores[(n // 2) - 1] + sorted_scores[n // 2]) / 2.0
        )

        variance = sum((s - mean_score) ** 2 for s in sus_scores) / (n - 1) if n > 1 else 0.0
        std_score = math.sqrt(variance)

        # 95% Confidence Interval
        margin_of_error = 1.96 * (std_score / math.sqrt(n)) if n > 1 else 0.0
        ci_lower = max(0.0, round(mean_score - margin_of_error, 2))
        ci_upper = min(100.0, round(mean_score + margin_of_error, 2))

        adj_rating, grade = self.classify_adjective_rating(mean_score)

        # Task completion stats
        evaluated_tasks = study_data.get("evaluated_tasks", [])
        task_metrics: List[Dict[str, Any]] = []
        for task in evaluated_tasks:
            task_id = task.get("task_id")
            completion_rate = task.get("completion_rate_pct", 0.0)
            avg_time = task.get("avg_time_min", 0.0)
            satisfaction = task.get("satisfaction_1_to_5", 0.0)
            task_metrics.append({
                "task_id": task_id,
                "name": task.get("name", "Unknown Task"),
                "completion_rate_pct": completion_rate,
                "avg_time_min": avg_time,
                "satisfaction_1_to_5": satisfaction,
            })

        remediations = study_data.get("usability_remediations", [])

        return {
            "cohort_size": n,
            "mean_sus": round(mean_score, 2),
            "median_sus": round(median_score, 2),
            "std_sus": round(std_score, 2),
            "ci_95": (ci_lower, ci_upper),
            "min_sus": min(sus_scores),
            "max_sus": max(sus_scores),
            "adjective_rating": adj_rating,
            "grade": grade,
            "benchmark_exceeded": mean_score >= 80.0,
            "individual_scores": sus_scores,
            "task_metrics": task_metrics,
            "remediations": remediations,
        }

    def generate_markdown_report(self, metrics: Optional[Dict[str, Any]] = None) -> str:
        """Generates a comprehensive Markdown evaluation report from usability metrics.

        Args:
            metrics: Optional computed metrics dictionary. If None, computes automatically.

        Returns:
            str: Markdown formatted report.
        """
        if metrics is None:
            metrics = self.compute_aggregate_metrics()

        ci_low, ci_high = metrics["ci_95"]
        benchmark_badge = "✅ PASSED (>= 80.0)" if metrics["benchmark_exceeded"] else "❌ FAILED"

        lines = [
            "# System Usability Scale (SUS) Evaluation Report",
            "",
            "## 1. Executive Summary",
            "",
            f"- **Cohort Size:** {metrics['cohort_size']} undergraduate engineering students",
            f"- **Mean SUS Score:** **{metrics['mean_sus']:.1f} / 100** ({benchmark_badge})",
            f"- **Adjective Rating:** **{metrics['adjective_rating']}** (Grade **{metrics['grade']}**)",
            f"- **Median SUS Score:** {metrics['median_sus']} / 100",
            f"- **Standard Deviation:** {metrics['std_sus']}",
            f"- **95% Confidence Interval:** [{ci_low}, {ci_high}]",
            f"- **Score Range:** Min {metrics['min_sus']} — Max {metrics['max_sus']}",
            "",
            "---",
            "",
            "## 2. Task Completion & Usability Metrics",
            "",
            "| Task ID | Evaluated Workflow | Completion Rate | Avg Time (min) | User Satisfaction (1-5) |",
            "| :---: | :--- | :---: | :---: | :---: |",
        ]

        for tm in metrics.get("task_metrics", []):
            lines.append(
                f"| **{tm['task_id']}** | {tm['name']} | {tm['completion_rate_pct']:.1f}% | "
                f"{tm['avg_time_min']:.1f} min | {tm['satisfaction_1_to_5']:.1f} / 5.0 |"
            )

        lines.extend([
            "",
            "---",
            "",
            "## 3. Usability Issues Identified & Remediation Status",
            "",
            "| Issue ID | Identified Usability Bottleneck | Severity | Implemented Resolution |",
            "| :---: | :--- | :---: | :--- |",
        ])

        for r in metrics.get("remediations", []):
            lines.append(
                f"| **{r.get('id', 'UR')}** | {r.get('issue', '')} | {r.get('severity', 'Medium')} | "
                f"{r.get('resolution', '')} |"
            )

        lines.append("")
        return "\n".join(lines)
