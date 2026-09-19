"""
PRIE v1 — REST API: Digital Twin & What-If Sensitivity Simulator (M12)
File: backend/api/v1_twin.py
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import numpy as np
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from modules.m06_placement_predictor import PlacementPredictor
from modules.m12_digital_twin import DigitalTwin
from spv_version import SPV_FEATURE_NAMES, IMMUTABLE_FEATURES

router = APIRouter()
predictor = PlacementPredictor()
twin = DigitalTwin(predictor=predictor)


class WhatIfSimulateRequest(BaseModel):
    spv_vector: List[float] = Field(..., description="Canonical 22D normalized SPV vector")
    perturbations: Dict[str, float] = Field(..., description="Feature delta changes (e.g. {'dsa_score': 0.15})")


class SensitivityRequest(BaseModel):
    spv_vector: List[float] = Field(..., description="Canonical 22D normalized SPV vector")
    step_size: float = Field(0.10, ge=0.01, le=0.50)


@router.get("/state/{student_id}", response_model=Dict[str, Any])
async def get_digital_twin_state(student_id: int):
    """Retrieve the active synchronized Digital Twin snapshot state for a student."""
    return twin.get_twin_state(student_id)


@router.post("/simulate", response_model=Dict[str, Any])
async def simulate_what_if_scenario(request: WhatIfSimulateRequest):
    """Execute what-if forward simulation against statistical prediction model."""
    if len(request.spv_vector) != 22:
        raise HTTPException(status_code=400, detail=f"SPV must be exactly 22 dimensions, got {len(request.spv_vector)}")

    # Reject immutable perturbations
    for imm in IMMUTABLE_FEATURES:
        if imm in request.perturbations and abs(request.perturbations[imm]) > 1e-6:
            raise HTTPException(
                status_code=422,
                detail=f"Immutability constraint violated: Feature '{imm}' cannot be modified in What-If simulations."
            )

    try:
        vec = np.array(request.spv_vector, dtype=np.float32)
        res = twin.simulate_what_if(vec, request.perturbations)
        return res
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Simulation failed: {e}")


@router.post("/sensitivity", response_model=List[Dict[str, Any]])
async def compute_sensitivity_matrix(request: SensitivityRequest):
    """Compute marginal responsiveness sensitivity matrix across all actionable features."""
    if len(request.spv_vector) != 22:
        raise HTTPException(status_code=400, detail=f"SPV must be exactly 22 dimensions, got {len(request.spv_vector)}")

    try:
        vec = np.array(request.spv_vector, dtype=np.float32)
        matrix = twin.compute_sensitivity_matrix(vec, step_size=request.step_size)
        return matrix
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sensitivity calculation failed: {e}")
