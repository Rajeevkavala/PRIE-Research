"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module 10: Explainable AI Diagnostic Module (TreeSHAP Interpretation)

Translates game-theoretic Shapley values into natural-language student diagnostics,
highlighting top positive drivers (strengths) and top negative drags (vulnerabilities)
with actionable guidance.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger("PRIE.Explainability")

# Human-readable labels for 22 SPV features
FEATURE_DISPLAY_NAMES: Dict[str, str] = {
    "cgpa": "Academic CGPA",
    "backlogs": "Active Academic Backlogs",
    "internship_months": "Internship Experience Duration",
    "skill_count": "Verified Skill Count",
    "certification_count": "Professional Certifications",
    "project_count": "Portfolio Technical Projects",
    "aptitude_score": "Quantitative Aptitude Score",
    "dsa_score": "Data Structures & Algorithms (DSA)",
    "dbms_score": "Database Management Systems (DBMS)",
    "cn_score": "Computer Networks (CN)",
    "programming_score": "Core Programming Proficiency",
    "resume_ats_score": "Resume ATS Alignment Score",
    "cosine_similarity": "Job Description Semantic Match",
    "gap_score": "Target Company Skill Gap",
    "consistency_score": "Weekly Learning Consistency",
    "has_internship": "Internship Exposure Indicator",
    "branch_encoded": "Academic Discipline Alignment",
    "target_role_encoded": "Target Role Competency Fit",
    "assessment_attempts": "Assessment Practice Engagement",
    "behavior_score": "Platform Behavioral Score",
    "engagement_score": "Learning Velocity & Engagement",
    "roadmap_completion_rate": "Curated Roadmap Progress",
}

# Actionable domain advice mapped to features
FEATURE_RECOMMENDATIONS: Dict[str, str] = {
    "cgpa": "Focus on high semester exam scores to satisfy corporate minimum GPA cutoffs.",
    "backlogs": "Prioritize clearing outstanding academic arrears before placement drives commence.",
    "internship_months": "Seek summer/winter industrial internships or open-source fellowship contributions.",
    "skill_count": "Expand verified technical competencies aligned with your target company taxonomy.",
    "certification_count": "Pursue industry-recognized certifications (e.g. AWS, Azure, Google Cloud, Meta).",
    "project_count": "Build and deploy production-grade full-stack or systems projects with live GitHub links.",
    "aptitude_score": "Engage daily with quantitative reasoning, logic puzzles, and speed-math drills.",
    "dsa_score": "Solve curated LeetCode/GeeksforGeeks problems focusing on trees, graphs, and dynamic programming.",
    "dbms_score": "Revise SQL queries, ACID properties, indexing mechanisms, and database normalization.",
    "cn_score": "Review OSI model layers, TCP/UDP protocols, routing, and HTTP/HTTPS architecture.",
    "programming_score": "Practice clean OOP concepts, time complexity optimization, and debugging in your primary language.",
    "resume_ats_score": "Refactor your resume layout with standard headings and incorporate target JD keywords.",
    "cosine_similarity": "Tailor your resume project descriptions to mirror role requirements and technologies.",
    "gap_score": "Bridge identified missing mandatory skills using the curated learning roadmap.",
    "consistency_score": "Maintain a regular 5-day active study streak on the platform each week.",
    "has_internship": "Gain practical industry exposure through apprenticeships or mentored virtual internships.",
    "branch_encoded": "Supplement core engineering coursework with specialized CS fundamentals.",
    "target_role_encoded": "Align portfolio projects directly with the expectations of your target job profile.",
    "assessment_attempts": "Attempt adaptive weekly topic quizzes to evaluate conceptual retention.",
    "behavior_score": "Increase active learning session velocity and submission regularity.",
    "engagement_score": "Deepen interaction with recommended coding exercises and interactive modules.",
    "roadmap_completion_rate": "Complete pending weekly milestones in your personalized learning roadmap.",
}


class ExplainabilityModule:
    """Translates raw SHAP feature values into clear, human-readable student diagnostics."""

    def __init__(self) -> None:
        """Initialize ExplainabilityModule."""
        logger.debug("ExplainabilityModule initialized.")

    @staticmethod
    def get_feature_label(feature_name: str) -> str:
        """Return human-readable display label for a feature name."""
        return FEATURE_DISPLAY_NAMES.get(
            feature_name, feature_name.replace("_", " ").title()
        )

    def generate_diagnostic_summary(
        self, shap_values: Dict[str, float]
    ) -> Dict[str, Any]:
        """Generate structured human-readable explanations from SHAP attributions.

        Args:
            shap_values: Dictionary mapping feature name to its SHAP importance value.

        Returns:
            Dict containing:
                top_positive (List[Tuple[str, float]]): Top 3 positive contributors.
                top_negative (List[Tuple[str, float]]): Top 3 negative drags.
                bullet_summary (List[str]): Markdown formatted bullet points.
                key_recommendation (Optional[str]): Actionable advice for top drag.
        """
        if not shap_values:
            return {
                "top_positive": [],
                "top_negative": [],
                "bullet_summary": ["ℹ️ No feature attributions available for this profile."],
                "key_recommendation": None,
            }

        # Sort features by absolute impact magnitude
        sorted_features = sorted(
            shap_values.items(), key=lambda item: abs(item[1]), reverse=True
        )

        positive_drivers: List[Tuple[str, float]] = [
            (k, v) for k, v in sorted_features if v > 0.0
        ][:3]
        negative_drags: List[Tuple[str, float]] = [
            (k, v) for k, v in sorted_features if v < 0.0
        ][:3]

        bullet_summary: List[str] = []

        for feat, val in positive_drivers:
            label = self.get_feature_label(feat)
            bullet_summary.append(
                f"✅ **Strength:** Your {label} positively boosts your placement readiness by +{abs(val):.2f}."
            )

        for feat, val in negative_drags:
            label = self.get_feature_label(feat)
            bullet_summary.append(
                f"⚠️ **Attention Required:** Your {label} is currently lowering your readiness score by -{abs(val):.2f}."
            )

        if not bullet_summary:
            bullet_summary.append("⚖️ **Neutral Profile:** All features are balanced at the baseline.")

        # Derive targeted recommendation from the top negative drag
        key_recommendation: Optional[str] = None
        if negative_drags:
            top_drag_feat = negative_drags[0][0]
            top_drag_label = self.get_feature_label(top_drag_feat)
            advice = FEATURE_RECOMMENDATIONS.get(
                top_drag_feat,
                f"Dedicate targeted effort toward strengthening your {top_drag_label}."
            )
            key_recommendation = f"Priority Action for {top_drag_label}: {advice}"

        return {
            "top_positive": positive_drivers,
            "top_negative": negative_drags,
            "bullet_summary": bullet_summary,
            "key_recommendation": key_recommendation,
        }
