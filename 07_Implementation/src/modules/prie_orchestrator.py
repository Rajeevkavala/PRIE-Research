"""ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module: PRIE Orchestrator (M10 - Master Orchestration Engine)
File: modules/prie_orchestrator.py

Governs the master coordination lifecycle across all nine constituent intelligence
engines to produce the unified Composite Placement Readiness Score (PRS),
TreeSHAP explainability attributions, bootstrap confidence intervals, and
adaptive prescriptive roadmaps.

Adheres strictly to:
- Chapter 05: PRIE Framework & Composite PRS Equation
- Chapter 07: Algorithm 7 (PRIE Orchestration Workflow)
- Chapter 09: System Implementation (Section 9.4 Orchestrator)
- Implementation Plan: 08_Integration_Plan.md & 03_Backend_Implementation.md
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

import config
from database import queries
from database.db_manager import execute_insert, execute_query, execute_single
from modules.assessment_engine import AssessmentIntelligenceEngine
from modules.behavior_analyzer import LearningBehaviorAnalyzer
from modules.company_predictor import CompanyReadinessPredictor
from modules.explainability import ExplainabilityModule
from modules.placement_predictor import PlacementReadinessPredictor
from modules.recommendation_engine import RecommendationEngine
from modules.resume_intelligence import ResumeIntelligenceEngine
from modules.roadmap_generator import AdaptiveRoadmapGenerator
from modules.skill_gap_engine import SkillGapEngine
from modules.student_profiling import StudentProfilingEngine

logger = logging.getLogger("PRIE.Orchestrator")


class PRIEOrchestrator:
    """Master orchestration engine governing the lifecycle of PRIE.

    Coordinates the 13-step sequence defined in Algorithm 7 (PDR Chapter 07 & 09) and
    Implementation Plan (08_Integration_Plan.md & 03_Backend_Implementation.md):
        Step 0: Log triggering event to learning_events
        Step 1: Extract 22-D Student Profile Vector (SPV) and completeness
        Step 2: Calculate weighted assessment accuracy S_assessment
        Step 3: Retrieve resume ATS score S_resume and extracted skills
        Step 4: Compute skill gap vector, S_gap, S_skill, and priority gaps
        Step 5: Run XGBoost placement predictor for S_pred, SHAP, and bootstrap CI
        Step 6: Compute behavioral score S_behavior and session consistency C_norm
        Step 7: Evaluate company readiness alignment S_company and gap-to-target
        Step 8: Compute formal 7-component Composite PRS formula
        Step 9: Compute PRS confidence score and map qualitative tier
        Step 10: Persist full telemetry record and TreeSHAP values to prs_history
        Step 11: Conditionally refresh adaptive 8-week roadmap if gap delta > 15%
        Step 12: Generate personalized resource recommendations
        Step 13: Assemble and return comprehensive dashboard payload (< 2000ms)
    """

    def __init__(
        self,
        db_path: Optional[Union[str, Path]] = None,
        weights: Optional[Dict[str, float]] = None,
        gap_delta_threshold: Optional[float] = None,
    ) -> None:
        """Initialize the PRIE Orchestrator with all constituent sub-engines.

        Args:
            db_path: Optional explicit SQLite database path.
            weights: Optional custom dictionary of PRS component weights.
                     Defaults to config.PRS_WEIGHTS.
            gap_delta_threshold: Sensitivity threshold to trigger roadmap re-generation.
                                 Defaults to config.GAP_DELTA_THRESHOLD (0.15).
        """
        self.db_path = Path(db_path) if db_path is not None else config.DATABASE_PATH
        self.weights = dict(weights or config.PRS_WEIGHTS)
        self.gap_delta_threshold = (
            float(gap_delta_threshold)
            if gap_delta_threshold is not None
            else getattr(config, "GAP_DELTA_THRESHOLD", 0.15)
        )

        # Validate weight configuration
        weight_sum = sum(self.weights.values())
        if abs(weight_sum - 1.0) > 1e-6:
            raise ValueError(
                f"Invalid PRS weights: sum must equal 1.00, got {weight_sum:.4f}"
            )

        logger.info(
            "Initializing PRIEOrchestrator (DB=%s, Threshold=%.2f)...",
            self.db_path.name if hasattr(self.db_path, "name") else self.db_path,
            self.gap_delta_threshold,
        )

        # Step 1-9 Sub-engines initialization
        self.profiler = StudentProfilingEngine(db_path=self.db_path)
        self.assessment_engine = AssessmentIntelligenceEngine(db_path=self.db_path)
        self.resume_engine = ResumeIntelligenceEngine(student_id=None)
        self.gap_engine = SkillGapEngine()
        self.predictor = PlacementReadinessPredictor()
        self.company_predictor = CompanyReadinessPredictor()
        self.behavior_analyzer = LearningBehaviorAnalyzer(db_path=self.db_path)
        self.roadmap_generator = AdaptiveRoadmapGenerator(student_id=None)
        self.recommender = RecommendationEngine(student_id=None)
        self.explainer = ExplainabilityModule()

        logger.info("PRIEOrchestrator initialized successfully with all 10 sub-engines.")

    @staticmethod
    def get_readiness_tier(prs_score: float) -> Tuple[str, str]:
        """Categorize a continuous Placement Readiness Score (0-100) into qualitative tiers.

        Adheres to Table 5.14.3 PRS Interpretation Scale:
            0  - 30 : Critical — Not Ready (Immediate intensive intervention required)
            30 - 50 : Low — Significant Gap (Structured daily learning for 6-8 weeks)
            50 - 65 : Moderate — Developing (Targeted gap closure over 4-6 weeks)
            65 - 80 : Good — Near Ready (Fine-tuning resume and interview prep)
            80 - 90 : High — Ready (Mock interviews, company-specific prep)
            90 - 100: Excellent — Placement Ready (Apply to target companies immediately)

        Args:
            prs_score: Clamped float score in [0.0, 100.0].

        Returns:
            Tuple[str, str]: (tier_name, action_recommendation)
        """
        score = float(np.clip(prs_score, 0.0, 100.0))
        if score < 30.0:
            return (
                "Critical",
                "Critical — Not Ready: Immediate intensive intervention required.",
            )
        elif score < 50.0:
            return (
                "Low",
                "Low — Significant Gap: Structured daily learning for 6-8 weeks.",
            )
        elif score < 65.0:
            return (
                "Moderate",
                "Moderate — Developing: Targeted gap closure over 4-6 weeks.",
            )
        elif score < 80.0:
            return (
                "Good",
                "Good — Near Ready: Fine-tuning resume and technical interview prep.",
            )
        elif score < 90.0:
            return (
                "High",
                "High — Ready: Mock interviews and company-specific coding preparation.",
            )
        else:
            return (
                "Excellent",
                "Excellent — Placement Ready: Qualifies for target company campus drives.",
            )

    @staticmethod
    def compute_confidence_score(
        profile_completeness: float,
        has_resume: bool,
        assessment_attempts: int,
        event_count: int,
        s_behavior: float,
    ) -> float:
        """Calculate mathematical PRS Data Confidence Score reflecting telemetry quality.

        Formula (PDR Section 5.14.5 & Chapter 09 line 336):
            Confidence = (0.40 * PCS)
                       + (0.20 * has_resume)
                       + (0.25 * assessment_coverage)
                       + (0.15 * behavior_sufficiency)

        Args:
            profile_completeness: Standardized PCS in [0.0, 1.0].
            has_resume: Boolean indicator if resume is uploaded and parsed.
            assessment_attempts: Total diagnostic quiz sessions completed.
            event_count: Telemetry clickstream events logged in learning_events.
            s_behavior: Behavioral composite score.

        Returns:
            float: Calibrated confidence score in [0.0, 1.0].
        """
        pcs = float(np.clip(profile_completeness, 0.0, 1.0))
        resume_factor = 1.0 if has_resume else 0.0

        # Assessment coverage saturates at 3 completed assessments
        assessment_coverage = float(np.clip(assessment_attempts / 3.0, 0.0, 1.0))

        # Behavior data sufficiency based on telemetry density and velocity
        behavior_sufficiency = float(
            np.clip(max(event_count / 10.0, s_behavior), 0.0, 1.0)
        )

        confidence = (
            (0.40 * pcs)
            + (0.20 * resume_factor)
            + (0.25 * assessment_coverage)
            + (0.15 * behavior_sufficiency)
        )
        return round(float(np.clip(confidence, 0.0, 1.0)), 4)

    def check_gap_delta(
        self, student_id: int, current_gap_score: float
    ) -> Tuple[bool, float]:
        """Determine whether skill gap changed significantly enough to warrant roadmap re-generation.

        Algorithm 7 Step 11:
            GapDeltaSignificant(gap_vector, previous_gaps, threshold=0.15)
            If student has no existing roadmap in SQLite, generation is mandatory.
            If previous PRS record exists, calculates:
                delta = |current_gap_score - previous_gap_score|
            Returns (True, delta) if delta > threshold or initial roadmap needed.

        Args:
            student_id: Integer primary key of student.
            current_gap_score: Current S_gap in [0.0, 1.0].

        Returns:
            Tuple[bool, float]: (needs_refresh, delta_magnitude)
        """
        existing_roadmaps = execute_query(
            queries.GET_STUDENT_ROADMAP, (student_id,), db_path=self.db_path
        )
        if not existing_roadmaps:
            logger.info("Student %d has no existing roadmap. Generation mandatory.", student_id)
            return True, 1.0

        latest_prs_row = execute_single(
            queries.GET_LATEST_PRS, (student_id,), db_path=self.db_path
        )
        if not latest_prs_row:
            logger.info("Student %d has no historical PRS record. Refresh approved.", student_id)
            return True, 1.0

        try:
            prev_s_skill = float(latest_prs_row["s_skill"] or 0.0)
            prev_gap_score = 1.0 - prev_s_skill
            delta = abs(current_gap_score - prev_gap_score)
            needs_refresh = delta > self.gap_delta_threshold
            logger.debug(
                "Student %d gap delta: current=%.4f, prev=%.4f, delta=%.4f, threshold=%.2f, refresh=%s",
                student_id, current_gap_score, prev_gap_score, delta, self.gap_delta_threshold, needs_refresh
            )
            return needs_refresh, round(delta, 4)
        except Exception as exc:
            logger.warning("Error evaluating gap delta for student %d: %s", student_id, exc)
            return True, 1.0

    def run_full_pipeline(
        self,
        student_id: int,
        trigger_event: str = "manual_refresh",
        force_roadmap_refresh: bool = False,
    ) -> Dict[str, Any]:
        """Execute the end-to-end 13-step PRIE coordination workflow.

        Args:
            student_id: Primary key of target student in SQLite students table.
            trigger_event: Semantic trigger origin (e.g., 'manual_refresh',
                           'quiz_completed', 'resume_uploaded', 'profile_updated',
                           'company_target_changed', 'roadmap_task_checked').
            force_roadmap_refresh: Force roadmap regeneration bypassing gap delta check.

        Returns:
            Dict[str, Any]: Standardized complete dashboard execution payload containing:
                - prs: Composite Readiness Score (0-100)
                - readiness_tier: Categorical tier (Critical, Low, Moderate, Good, High, Excellent)
                - readiness_action: Contextual next step recommendation
                - confidence_score: Telemetry sufficiency metric [0.0, 1.0]
                - confidence_interval: 95% bootstrap CI (lower%, upper%)
                - profile_completeness: Standardized PCS score [0.0, 1.0]
                - component_scores: Normalized [0.0, 1.0] scores for all 7 dimensions
                - component_percentages: Formatted [0.0, 100.0]% scores for radar/gauge
                - weights_applied: Dictionary of component weights
                - priority_gaps: Sorted list of missing skills with weights
                - gap_vector: Granular dictionary of all required company skills
                - shap_values: TreeSHAP local attributions per feature
                - explanations: Human-readable diagnostic strengths and drags
                - company_fit: Gap-to-target telemetry against target enterprise
                - roadmap: Active 8-week structured roadmap schedule
                - recommendations: Curated learning resources matching learning style
                - execution_time_ms: Measured pipeline latency in milliseconds (< 2000ms)
                - trigger_event: Trigger identifier string

        Raises:
            ValueError: If student_id does not exist in the database.
        """
        start_time = time.perf_counter()
        logger.info(
            "Starting PRIE Master Pipeline for Student ID: %d [Trigger: %s]...",
            student_id,
            trigger_event,
        )

        # ---------------------------------------------------------------------
        # Pre-check: Verify Student Existence
        # ---------------------------------------------------------------------
        student = execute_single(
            queries.GET_STUDENT_BY_ID, (student_id,), db_path=self.db_path
        )
        if not student:
            raise ValueError(f"Student with ID {student_id} not found in database.")

        # ---------------------------------------------------------------------
        # Step 0: Audit Logging of Triggering Event
        # ---------------------------------------------------------------------
        try:
            event_payload = {
                "student_id": student_id,
                "trigger_event": trigger_event,
                "timestamp": datetime.now().isoformat(),
            }
            execute_insert(
                queries.INSERT_LEARNING_EVENT,
                (
                    student_id,
                    trigger_event,
                    json.dumps(event_payload),
                    f"PRIE Master Pipeline invoked via {trigger_event}",
                    0,
                ),
                db_path=self.db_path,
            )
        except Exception as exc:
            logger.warning("Step 0 (Event Logging) non-fatal warning: %s", exc)

        # ---------------------------------------------------------------------
        # Step 1: Ingest 22-Dimensional Student Profile Vector (SPV)
        # ---------------------------------------------------------------------
        fv, completeness = self.profiler.assemble_feature_vector(student_id)
        logger.debug("Step 1 Complete: SPV assembled (completeness=%.2f)", completeness)

        # ---------------------------------------------------------------------
        # Step 2: Assessment Engine Accuracy Score (S_assessment)
        # ---------------------------------------------------------------------
        s_assessment = float(
            self.assessment_engine.compute_assessment_score(student_id)
        )
        s_assessment = float(np.clip(s_assessment, 0.0, 1.0))
        logger.debug("Step 2 Complete: S_assessment = %.4f", s_assessment)

        # ---------------------------------------------------------------------
        # Step 3: Resume Intelligence Score (S_resume) & Extracted Skills
        # ---------------------------------------------------------------------
        resume_result = self.resume_engine.get_resume_score(
            student_id=student_id, db_path=self.db_path
        )
        has_resume = resume_result is not None

        if has_resume and resume_result:
            s_resume = float(np.clip(resume_result.ats_score / 100.0, 0.0, 1.0))
            extracted_skills = resume_result.skills
            if not extracted_skills:
                extracted_skills = json.loads(student["skills_json"] or "[]")
        else:
            # Fallback per Algorithm 7 Line 17 & Chapter 09 Line 303
            s_resume = 0.0
            extracted_skills = json.loads(student["skills_json"] or "[]")

        logger.debug(
            "Step 3 Complete: has_resume=%s, S_resume=%.4f, skills_count=%d",
            has_resume,
            s_resume,
            len(extracted_skills),
        )

        # ---------------------------------------------------------------------
        # Step 4: Skill Gap Detection (S_gap, S_skill, priority_gaps)
        # ---------------------------------------------------------------------
        target_company_id = int(student["target_company_id"] or 1)
        gap_vector, s_gap, s_skill, priority_gaps = (
            self.gap_engine.evaluate_skill_gaps(
                student_skills=extracted_skills,
                company_id=target_company_id,
            )
        )
        s_gap = float(np.clip(s_gap, 0.0, 1.0))
        s_skill = float(np.clip(s_skill, 0.0, 1.0))
        logger.debug(
            "Step 4 Complete: S_gap=%.4f, S_skill=%.4f, priority_gaps=%d",
            s_gap,
            s_skill,
            len(priority_gaps),
        )

        # ---------------------------------------------------------------------
        # Step 5: Placement Readiness Prediction (S_pred, TreeSHAP, CI)
        # ---------------------------------------------------------------------
        s_pred, shap_dict, (ci_lower, ci_upper) = self.predictor.predict_readiness(fv)
        s_pred = float(np.clip(s_pred, 0.0, 1.0))
        ci_lower = float(np.clip(ci_lower, 0.0, 1.0))
        ci_upper = float(np.clip(ci_upper, 0.0, 1.0))
        logger.debug(
            "Step 5 Complete: S_pred=%.4f, CI=[%.4f, %.4f]",
            s_pred,
            ci_lower,
            ci_upper,
        )

        # ---------------------------------------------------------------------
        # Step 6: Behavioral Analytics (S_behavior, C_norm)
        # ---------------------------------------------------------------------
        s_behavior, c_norm = self.behavior_analyzer.analyze_behavior(student_id)
        s_behavior = float(np.clip(s_behavior, 0.0, 1.0))
        c_norm = float(np.clip(c_norm, 0.0, 1.0))
        logger.debug(
            "Step 6 Complete: S_behavior=%.4f, C_norm=%.4f", s_behavior, c_norm
        )

        # ---------------------------------------------------------------------
        # Step 7: Company Readiness Prediction (S_company, gap_to_target)
        # ---------------------------------------------------------------------
        s_company, gap_to_target = self.company_predictor.evaluate_company_fit(
            student_id=student_id,
            company_id=target_company_id,
            student_skills=extracted_skills,
            current_prs=None,
        )
        s_company = float(np.clip(s_company, 0.0, 1.0))
        logger.debug(
            "Step 7 Complete: S_company=%.4f (target_company_id=%d)",
            s_company,
            target_company_id,
        )

        # ---------------------------------------------------------------------
        # Step 8: Compute Composite Placement Readiness Score (PRS)
        # Formula: PRS = 100 * Σ(w_i * S_i)
        # ---------------------------------------------------------------------
        w = self.weights
        prs_raw = 100.0 * (
            w["w_pred"] * s_pred
            + w["w_skill"] * s_skill
            + w["w_resume"] * s_resume
            + w["w_behavior"] * s_behavior
            + w["w_consistency"] * c_norm
            + w["w_company"] * s_company
            + w["w_assessment"] * s_assessment
        )
        prs = float(np.clip(round(prs_raw, 2), 0.0, 100.0))
        logger.info("Step 8 Complete: Composite PRS = %.2f / 100.0", prs)

        # Re-align company gap-to-target with final calibrated PRS
        try:
            _, gap_to_target = self.company_predictor.evaluate_company_fit(
                student_id=student_id,
                company_id=target_company_id,
                student_skills=extracted_skills,
                current_prs=prs,
            )
        except Exception as exc:
            logger.debug("Minor notice re-evaluating company fit: %s", exc)

        # ---------------------------------------------------------------------
        # Step 9: Interpretation Tier, Confidence Score & Human Explanations
        # ---------------------------------------------------------------------
        tier_name, tier_action = self.get_readiness_tier(prs)

        # Query historical assessment attempts and telemetry volume for confidence
        assessments_history = execute_query(
            queries.GET_STUDENT_ASSESSMENTS, (student_id,), db_path=self.db_path
        )
        events_history = execute_query(
            queries.GET_STUDENT_EVENTS, (student_id, 100), db_path=self.db_path
        )

        confidence = self.compute_confidence_score(
            profile_completeness=completeness,
            has_resume=has_resume,
            assessment_attempts=len(assessments_history),
            event_count=len(events_history),
            s_behavior=s_behavior,
        )

        # Explainability diagnostics
        explanations = self.explainer.generate_diagnostic_summary(shap_dict)
        logger.debug(
            "Step 9 Complete: Tier=%s, Confidence=%.4f", tier_name, confidence
        )

        # ---------------------------------------------------------------------
        # Step 10: Persist Full Telemetry to prs_history
        # ---------------------------------------------------------------------
        prs_history_id = execute_insert(
            queries.INSERT_PRS_RECORD,
            (
                student_id,
                target_company_id,
                prs,
                prs,  # Dual-column synchronization (prs_score and prs_value)
                round(float(s_pred), 4),
                round(float(s_skill), 4),
                round(float(s_resume), 4),
                round(float(s_behavior), 4),
                round(float(c_norm), 4),
                round(float(s_company), 4),
                round(float(s_assessment), 4),
                round(float(confidence), 4),
                round(float(ci_lower), 4),
                round(float(ci_upper), 4),
                json.dumps(shap_dict),
                trigger_event,
            ),
            db_path=self.db_path,
        )
        logger.debug("Step 10 Complete: Inserted prs_history record ID: %d", prs_history_id)

        # ---------------------------------------------------------------------
        # Step 11: Conditional Adaptive Roadmap Refresh (Gap Delta > 15%)
        # ---------------------------------------------------------------------
        needs_refresh, gap_delta = self.check_gap_delta(student_id, s_gap)
        if needs_refresh or force_roadmap_refresh:
            logger.info(
                "Refreshing adaptive roadmap for student %d (gap delta=%.3f > %.2f or forced)",
                student_id,
                gap_delta,
                self.gap_delta_threshold,
            )
            roadmap = self.roadmap_generator.generate_weekly_roadmap(
                student_id=student_id,
                priority_gaps=priority_gaps,
            )
        else:
            logger.info(
                "Retaining existing roadmap for student %d (gap delta=%.3f <= %.2f)",
                student_id,
                gap_delta,
                self.gap_delta_threshold,
            )
            saved_weeks = self.roadmap_generator.get_student_roadmap(student_id)
            if saved_weeks:
                roadmap = {w["week_number"]: w for w in saved_weeks}
            else:
                roadmap = self.roadmap_generator.generate_weekly_roadmap(
                    student_id=student_id,
                    priority_gaps=priority_gaps,
                )

        logger.debug("Step 11 Complete: Roadmap loaded (%d weeks)", len(roadmap))

        # ---------------------------------------------------------------------
        # Step 12: Personalized Learning Resource Recommendations
        # ---------------------------------------------------------------------
        recommendations = self.recommender.generate_recommendations(
            student_id=student_id,
            priority_gaps=priority_gaps,
            top_n=5,
            persist=True,
        )
        logger.debug(
            "Step 12 Complete: Curated %d recommendations", len(recommendations)
        )

        # ---------------------------------------------------------------------
        # Step 13: Assemble and Return Complete Dashboard Payload (< 2000ms)
        # ---------------------------------------------------------------------
        elapsed_ms = round((time.perf_counter() - start_time) * 1000.0, 2)
        logger.info(
            "Step 13 Complete: PRIE Pipeline finished in %.2fms (PRS=%.1f, Tier=%s)",
            elapsed_ms,
            prs,
            tier_name,
        )

        payload: Dict[str, Any] = {
            "student_id": student_id,
            "student_name": student["name"],
            "prs": round(prs, 1),
            "prs_raw": prs,
            "readiness_tier": tier_name,
            "readiness_action": tier_action,
            "confidence_score": round(confidence, 3),
            "confidence_interval": (
                round(ci_lower * 100.0, 1),
                round(ci_upper * 100.0, 1),
            ),
            "ci_raw": (ci_lower, ci_upper),
            "profile_completeness": round(completeness, 3),
            "component_scores": {
                "s_pred": round(float(s_pred), 4),
                "s_skill": round(float(s_skill), 4),
                "s_resume": round(float(s_resume), 4),
                "s_behavior": round(float(s_behavior), 4),
                "c_norm": round(float(c_norm), 4),
                "s_company": round(float(s_company), 4),
                "s_assessment": round(float(s_assessment), 4),
            },
            "component_percentages": {
                "s_pred": round(float(s_pred) * 100.0, 1),
                "s_skill": round(float(s_skill) * 100.0, 1),
                "s_resume": round(float(s_resume) * 100.0, 1),
                "s_behavior": round(float(s_behavior) * 100.0, 1),
                "c_norm": round(float(c_norm) * 100.0, 1),
                "s_company": round(float(s_company) * 100.0, 1),
                "s_assessment": round(float(s_assessment) * 100.0, 1),
            },
            "weights_applied": dict(self.weights),
            "priority_gaps": priority_gaps,
            "gap_vector": gap_vector,
            "gap_score": round(float(s_gap), 4),
            "gap_delta": round(float(gap_delta), 4),
            "roadmap_refreshed": bool(needs_refresh or force_roadmap_refresh),
            "shap_values": shap_dict,
            "explanations": explanations,
            "company_fit": gap_to_target,
            "roadmap": roadmap,
            "recommendations": recommendations,
            "execution_time_ms": elapsed_ms,
            "trigger_event": trigger_event,
            "timestamp": datetime.now().isoformat(),
        }

        return payload
