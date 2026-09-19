"""
PRIE v1 — XAI & Prescriptions API Routes
File: backend/api/v1_explain.py
"""

from __future__ import annotations
import sys
from pathlib import Path
from fastapi import APIRouter, HTTPException, Depends

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from api.v1_auth import get_current_student
from modules.m01_spv_aggregator import SPVAggregator
from modules.m04_skill_gap_engine import SkillGapEngine
from modules.m06_placement_predictor import PlacementPredictor
from modules.m07_prescriptive_xai import PrescriptiveXAI
from database import db_manager, queries

router = APIRouter()


@router.post("/prescribe")
def prescribe(student_id: int = Depends(get_current_student)):
    """POST /api/v1/explain/prescribe — M01→M04→M06→M07 pipeline."""
    try:
        agg  = SPVAggregator()
        spv, mask, completeness = agg.assemble(student_id)

        row = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_ID, (student_id,)))
        target_role = (row or {}).get("target_role", "Software Development Engineer")

        # M04: gap analysis
        gap_engine = SkillGapEngine()
        gap_score, deficit_list, deficit_vector = gap_engine.compute_gap(spv, target_role)

        # M06: prediction + SHAP
        pred = PlacementPredictor()
        pred_result = pred.predict(spv, compute_shap=True)

        # M07: explanations + counterfactuals
        xai = PrescriptiveXAI()
        explanation = xai.explain(pred_result.get("shap_values", {}), spv)
        counterfactual = xai.generate_counterfactual(spv, deficit_list)
        narrative = xai.generate_narrative(pred_result, explanation)

        return {
            "prediction":       pred_result,
            "gap_score":        gap_score,
            "deficit_ranking":  deficit_list[:6],
            "explanation":      explanation,
            "counterfactual":   counterfactual,
            "narrative":        narrative,
            "target_role":      target_role,
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
