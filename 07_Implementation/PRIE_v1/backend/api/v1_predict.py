"""
PRIE v1 — Prediction API Routes
File: backend/api/v1_predict.py
"""

from __future__ import annotations
import sys
from pathlib import Path
from fastapi import APIRouter, HTTPException, Depends

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from api.v1_auth import get_current_student
from modules.m01_spv_aggregator import SPVAggregator
from modules.m06_placement_predictor import PlacementPredictor

router = APIRouter()
_predictor = None

def _get_predictor() -> PlacementPredictor:
    global _predictor
    if _predictor is None:
        _predictor = PlacementPredictor()
    return _predictor


@router.post("/readiness")
def predict_readiness(student_id: int = Depends(get_current_student)):
    """POST /api/v1/predict/readiness — M01 → M06 pipeline."""
    try:
        agg  = SPVAggregator()
        spv, mask, completeness = agg.assemble(student_id)
        pred = _get_predictor()
        result = pred.predict(spv, compute_shap=True)

        # Compute PRS
        spv_dict = {name: float(spv[i]) for i, name in enumerate(
            __import__("spv_version").SPV_FEATURE_NAMES
        )}
        spv_dict.update(result)
        prs = pred.compute_prs(spv_dict)

        result["prs_score"]          = prs
        result["profile_completeness"] = completeness
        result["confidence_mask"]    = mask.tolist()
        result["probability"]        = result["readiness_probability"]
        result["confidence_interval"] = [result["ci_lower"], result["ci_upper"]]

        # Save snapshot
        try:
            agg.save_snapshot(
                student_id,
                readiness_prob=result["readiness_probability"],
                readiness_tier=result["readiness_tier"],
                shap_values=result.get("shap_values", {}),
                trigger="prediction_request",
            )
        except Exception:
            pass

        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
