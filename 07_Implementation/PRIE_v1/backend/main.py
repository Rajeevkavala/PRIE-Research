"""
PRIE v1 — FastAPI Application Entry Point
File: backend/main.py

REST API: /api/v1/...
Traceability: 05_PRIE_Architecture/API_Architecture.md
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config
from database.db_manager import initialize_schema

# Import routers
from api.v1_auth import router as auth_router
from api.v1_profile import router as profile_router
from api.v1_predict import router as predict_router
from api.v1_explain import router as explain_router
from api.v1_roadmap import router as roadmap_router
from api.v1_assessment import router as assessment_router
from api.v1_resume import router as resume_router
from api.v1_interview import router as interview_router
from api.v1_rag import router as rag_router
from api.v1_aqg import router as aqg_router
from api.v1_company import router as company_router
from api.v1_twin import router as twin_router
from api.v1_experiments import router as experiments_router

logger = logging.getLogger("PRIE.Main")

# ── Application ────────────────────────────────────────────────────────────────
app = FastAPI(
    title="PRIE v1 — Placement Readiness Intelligence Engine",
    description=(
        "ScholarCamp AI-Powered Placement Readiness Ecosystem. "
        "PRIE v1 — Phase 07 Implementation. "
        "SPV_VERSION=v1, 22-dimensional feature tensor."
    ),
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# ── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Startup: Initialize database ──────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    logger.info("PRIE v1 starting — initializing database schema...")
    try:
        initialize_schema()
        logger.info("Database ready.")
    except Exception as e:
        logger.error(f"Database init failed: {e}")

# ── Global error handler ──────────────────────────────────────────────────────
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": str(exc)})

# ── Routers ───────────────────────────────────────────────────────────────────
app.include_router(auth_router,        prefix="/api/v1/auth",        tags=["Authentication"])
app.include_router(profile_router,     prefix="/api/v1/profile",     tags=["Student Profile"])
app.include_router(predict_router,     prefix="/api/v1/predict",     tags=["Placement Prediction"])
app.include_router(explain_router,     prefix="/api/v1/explain",     tags=["XAI & Prescriptions"])
app.include_router(roadmap_router,     prefix="/api/v1/roadmap",     tags=["Learning Roadmap"])
app.include_router(assessment_router,  prefix="/api/v1/assessment",  tags=["Adaptive Assessment"])
app.include_router(resume_router,      prefix="/api/v1/resume",      tags=["Resume & ATS"])
app.include_router(interview_router,   prefix="/api/v1/interview",   tags=["Mock Interview"])
app.include_router(rag_router,         prefix="/api/v1/rag",         tags=["Curriculum RAG"])
app.include_router(aqg_router,         prefix="/api/v1/aqg",         tags=["Bloom AQG"])
app.include_router(company_router,     prefix="/api/v1/company",     tags=["Company Matcher"])
app.include_router(twin_router,        prefix="/api/v1/twin",        tags=["Digital Twin"])
app.include_router(experiments_router, prefix="/api/v1/experiments", tags=["Research Experiments"])

from fastapi.staticfiles import StaticFiles

# ── Health endpoint ───────────────────────────────────────────────────────────
@app.get("/api/health", tags=["System"])
async def health():
    return {
        "status":      "healthy",
        "system":      "PRIE v1",
        "spv_version": "v1",
        "dimension":   22,
    }

# ── Static Frontend SPA Mounting ──────────────────────────────────────────────
frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
if frontend_dir.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")
