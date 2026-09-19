"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Modules Package Initializer

Contains the 10 core intelligence engines:
- prie_orchestrator
- student_profiling
- assessment_engine
- resume_intelligence
- skill_gap_engine
- placement_predictor
- company_predictor
- behavior_analyzer
- roadmap_generator
- explainability
"""

from modules.student_profiling import (
    BRANCH_MAP,
    ROLE_MAP,
    SPV_FEATURE_NAMES,
    StudentProfilingEngine,
)
from modules.behavior_analyzer import LearningBehaviorAnalyzer
from modules.placement_predictor import PlacementReadinessPredictor
from modules.explainability import ExplainabilityModule
from modules.resume_intelligence import ResumeIntelligenceEngine
from modules.skill_gap_engine import SkillGapEngine
from modules.company_predictor import CompanyReadinessPredictor
from modules.assessment_engine import AssessmentIntelligenceEngine
from modules.mock_interview import MockInterviewEvaluator
from modules.roadmap_generator import AdaptiveRoadmapGenerator
from modules.recommendation_engine import RecommendationEngine
from modules.prie_orchestrator import PRIEOrchestrator
from modules.sus_evaluator import SUSEvaluator

__all__ = [
    "BRANCH_MAP",
    "ROLE_MAP",
    "SPV_FEATURE_NAMES",
    "StudentProfilingEngine",
    "LearningBehaviorAnalyzer",
    "PlacementReadinessPredictor",
    "ExplainabilityModule",
    "ResumeIntelligenceEngine",
    "SkillGapEngine",
    "CompanyReadinessPredictor",
    "AssessmentIntelligenceEngine",
    "MockInterviewEvaluator",
    "AdaptiveRoadmapGenerator",
    "RecommendationEngine",
    "PRIEOrchestrator",
    "SUSEvaluator",
]

