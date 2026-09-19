"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Resume Intelligence Engine (M3) & ATS NLP Pipeline
File: modules/resume_intelligence.py

Implements multi-format document extraction, domain-specific regex NER skill parsing
against 500+ classified technical skills, dense semantic embedding generation via
Sentence Transformers (all-MiniLM-L6-v2), cosine similarity calculation against
benchmark company JDs, and Composite ATS scoring.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Pattern, Set, Tuple, Union

import numpy as np

import config
from database.db_manager import execute_insert, execute_query, execute_single, execute_update
from database.queries import (
    GET_COMPANY_BY_ID,
    GET_LATEST_RESUME,
    GET_STUDENT_BY_ID,
    INSERT_RESUME,
    UPDATE_RESUME_ANALYSIS,
)
from sentence_transformers import SentenceTransformer
from utils.text_processing import (
    build_skill_regex_pattern,
    extract_document_text,
    normalize_technical_text,
)

logger = logging.getLogger("PRIE.ResumeIntelligence")

# Default foundational benchmark skills used for global keyword coverage
DEFAULT_BENCHMARK_SKILLS: List[str] = [
    "Data Structures",
    "Algorithms",
    "Python",
    "Java",
    "C++",
    "SQL",
    "Git",
    "Linux",
    "Operating Systems",
    "Computer Networks",
    "Database Management",
    "System Design",
]


class ResumeScoreResult(tuple):
    """Encapsulates resume score results supporting tuple unpacking, dict indexing, and dot attributes."""

    def __new__(
        cls,
        ats_score: float,
        skills: List[str],
        student_id: Optional[int] = None,
        row: Optional[Any] = None,
    ):
        instance = super().__new__(cls, (ats_score, skills))
        instance.ats_score = ats_score
        instance.skills = skills
        instance.student_id = student_id
        instance._row = dict(row) if row else {}
        return instance

    def __getitem__(self, key: Any) -> Any:
        if isinstance(key, str):
            if key == "ats_score":
                return self.ats_score
            if key in ("skills", "extracted_skills"):
                return self.skills
            if key == "student_id":
                return self.student_id
            if key in self._row:
                return self._row[key]
            raise KeyError(key)
        return super().__getitem__(key)

    def get(self, key: str, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default


class ResumeIntelligenceEngine:
    """Evaluates candidate resumes using dense semantic embeddings and domain NER."""

    _model: Optional[SentenceTransformer] = None
    _jd_embeddings: Optional[np.ndarray] = None
    _jd_metadata: Optional[List[Dict[str, Any]]] = None
    _taxonomy_data: Optional[List[Dict[str, Any]]] = None
    _canonical_to_category: Optional[Dict[str, str]] = None
    _skill_patterns: Optional[Dict[str, Pattern[str]]] = None
    _alias_map: Optional[Dict[str, str]] = None
    _canonical_skills: Optional[List[str]] = None

    def __init__(self, student_id: Optional[int] = None):
        """Initializes the Resume Intelligence Engine for an optional student ID.

        Args:
            student_id: Optional student ID for database-bound evaluations.
        """
        self.student_id = student_id

    @property
    def taxonomy(self) -> Dict[str, str]:
        """Provides access to taxonomy skill-to-category dictionary."""
        self._load_artifacts()
        return self._canonical_to_category or {}

    @property
    def canonical_skills(self) -> List[str]:
        """Provides access to list of all canonical skill names."""
        self._load_artifacts()
        return self._canonical_skills or []

    @property
    def company_jds(self) -> List[Dict[str, Any]]:
        """Provides access to benchmark company JD metadata."""
        self._load_artifacts()
        return self._jd_metadata or []

    @property
    def jd_embeddings(self) -> np.ndarray:
        """Provides access to precomputed JD embeddings matrix."""
        self._load_artifacts()
        return self._jd_embeddings if self._jd_embeddings is not None else np.empty((0, 384))

    @property
    def encoder(self) -> SentenceTransformer:
        """Provides access to SentenceTransformer encoder."""
        self._load_artifacts()
        return self._model  # type: ignore

    @classmethod
    def _load_artifacts(cls) -> None:
        """Loads SentenceTransformer model, JD embeddings, and skill taxonomy singletons."""
        if cls._model is None:
            logger.info(
                "Loading SentenceTransformer model: %s",
                config.SENTENCE_TRANSFORMER_MODEL,
            )
            cls._model = SentenceTransformer(config.SENTENCE_TRANSFORMER_MODEL)

        if cls._jd_embeddings is None:
            if config.JD_EMBEDDINGS_PATH.exists():
                logger.info("Loading precomputed JD embeddings from: %s", config.JD_EMBEDDINGS_PATH)
                cls._jd_embeddings = np.load(str(config.JD_EMBEDDINGS_PATH))
            else:
                logger.warning(
                    "JD embeddings file not found at %s. Initializing fallback mock unit matrix.",
                    config.JD_EMBEDDINGS_PATH,
                )
                cls._jd_embeddings = np.ones((8, 384), dtype=np.float32) / np.sqrt(384)

        if cls._jd_metadata is None:
            if config.JD_METADATA_PATH.exists():
                with open(config.JD_METADATA_PATH, "r", encoding="utf-8") as f:
                    cls._jd_metadata = json.load(f)
            else:
                cls._jd_metadata = []

        if cls._taxonomy_data is None:
            cls._load_taxonomy()

    @classmethod
    def _load_taxonomy(cls) -> None:
        """Loads skill taxonomy, harmonizes synonyms, and compiles regex patterns."""
        cls._canonical_to_category = {}
        cls._alias_map = {}
        cls._skill_patterns = {}
        cls._canonical_skills = []

        if config.SKILL_TAXONOMY_PATH.exists():
            with open(config.SKILL_TAXONOMY_PATH, "r", encoding="utf-8") as f:
                cls._taxonomy_data = json.load(f)
        else:
            cls._taxonomy_data = []

        # Parse taxonomy items
        for item in cls._taxonomy_data:
            raw_canonical = item.get("skill_name", "").strip()
            category = item.get("category", "General")
            if not raw_canonical:
                continue

            # Strip parenthetical annotations: e.g. "Kubernetes (K8s)" -> "Kubernetes"
            base_name = re.sub(r"\(.*?\)", "", raw_canonical).strip()
            clean_canonical = base_name if base_name else raw_canonical

            # Detect common corporate taxonomy compound names
            for suffix in (
                "Containerization",
                "Fundamentals",
                "Basics",
                "Architecture",
                "Development",
                "Programming",
                "Concepts",
            ):
                if clean_canonical.endswith(" " + suffix):
                    candidate_clean = clean_canonical[: -(len(suffix) + 1)].strip()
                    if candidate_clean:
                        clean_canonical = candidate_clean
                        break

            if clean_canonical not in cls._canonical_skills:
                cls._canonical_skills.append(clean_canonical)
            cls._canonical_to_category[clean_canonical] = category
            cls._canonical_to_category[raw_canonical] = category

            # Register canonical lowercased aliases
            cls._alias_map[clean_canonical.lower()] = clean_canonical
            cls._alias_map[raw_canonical.lower()] = clean_canonical

            if base_name.lower() not in cls._alias_map:
                cls._alias_map[base_name.lower()] = clean_canonical

            # Extract terms in parentheses (e.g. "K8s" from "Kubernetes (K8s)")
            for paren in re.findall(r"\((.*?)\)", raw_canonical):
                p_clean = paren.strip().lower()
                if p_clean and p_clean not in cls._alias_map:
                    cls._alias_map[p_clean] = clean_canonical

            # Map all true synonyms to clean canonical skill name
            for synonym in item.get("synonyms", []):
                syn_clean = synonym.strip().lower()
                if syn_clean:
                    cls._alias_map[syn_clean] = clean_canonical

        # Curated technical framework aliases to ensure standard syntax matches
        FRAMEWORK_ALIASES = {
            ".net": (".NET", "Web Development"),
            ".net core": (".NET", "Web Development"),
            "dotnet": (".NET", "Web Development"),
            "dotnet core": (".NET", "Web Development"),
            "asp.net": (".NET", "Web Development"),
            "asp.net core": (".NET", "Web Development"),
            "node.js": ("Node.js", "Web Development"),
            "nodejs": ("Node.js", "Web Development"),
            "react.js": ("React", "Web Development"),
            "react": ("React", "Web Development"),
            "reactjs": ("React", "Web Development"),
            "css": ("CSS", "Web Development"),
            "css3": ("CSS", "Web Development"),
            "html": ("HTML", "Web Development"),
            "html5": ("HTML", "Web Development"),
            "vue": ("Vue.js", "Web Development"),
            "vue.js": ("Vue.js", "Web Development"),
            "angular": ("Angular", "Web Development"),
            "ci/cd": ("CI/CD", "Cloud & DevOps"),
            "ci cd": ("CI/CD", "Cloud & DevOps"),
            "rest api": ("RESTful API", "Web Development"),
            "restful api": ("RESTful API", "Web Development"),
            "machine learning": ("Machine Learning", "Machine Learning & AI"),
            "deep learning": ("Deep Learning", "Machine Learning & AI"),
            "docker": ("Docker", "Cloud & DevOps"),
            "kubernetes": ("Kubernetes", "Cloud & DevOps"),
            "k8s": ("Kubernetes", "Cloud & DevOps"),
            "aws": ("AWS", "Cloud & DevOps"),
            "data structures": ("Data Structures", "Data Structures"),
            "dsa": ("Data Structures", "Data Structures"),
            "algorithms": ("Algorithms", "Algorithms"),
            "system design": ("System Design", "Software Architecture"),
            "cloud computing": ("Cloud Computing", "Cloud & DevOps"),
            "object-oriented programming": ("Object-Oriented Programming", "Programming"),
            "oop": ("Object-Oriented Programming", "Programming"),
        }

        for alias_term, (target_skill, target_cat) in FRAMEWORK_ALIASES.items():
            if target_skill not in cls._canonical_skills:
                cls._canonical_skills.append(target_skill)
            cls._canonical_to_category[target_skill] = target_cat
            cls._alias_map[alias_term] = target_skill

        # Compile regex patterns for all unique alias terms
        for term in cls._alias_map:
            cls._skill_patterns[term] = build_skill_regex_pattern(term)

        logger.debug(
            "Compiled %d regex skill patterns across %d canonical skills.",
            len(cls._skill_patterns),
            len(cls._canonical_skills),
        )

    def extract_text(self, file_path: Union[str, Path]) -> str:
        """Extracts plain text from a resume document (PDF, DOCX, TXT).

        Args:
            file_path: Path to the candidate's resume file.

        Returns:
            str: Raw extracted document text.
        """
        return extract_document_text(file_path)

    def clean_text(self, raw_text: str) -> str:
        """Cleans and normalizes text while preserving programming tokens.

        Args:
            raw_text: Unprocessed document text string.

        Returns:
            str: Normalized technical text string.
        """
        return normalize_technical_text(raw_text)

    def extract_skills(self, text: str) -> List[str]:
        """Extracts technical skills using word-boundary regex taxonomy matching.

        Scans the input text against 500+ pre-compiled skill patterns, preventing
        false-positive substring collisions (e.g. matching 'C' inside 'React').

        Args:
            text: Raw or normalized document text.

        Returns:
            List[str]: Deduplicated, sorted list of canonical skill names.
        """
        self._load_artifacts()
        if not text or not self._skill_patterns or not self._alias_map:
            return []

        matched_canonical: Set[str] = set()

        for term, pattern in self._skill_patterns.items():
            if pattern.search(text):
                canonical = self._alias_map.get(term)
                if canonical:
                    matched_canonical.add(canonical)

        return sorted(list(matched_canonical))

    def extract_skills_by_category(self, text: str) -> Dict[str, List[str]]:
        """Extracts skills and organizes them into domain categories.

        Args:
            text: Raw or normalized document text.

        Returns:
            Dict[str, List[str]]: Category-to-skill-list mapping.
        """
        self._load_artifacts()
        extracted = self.extract_skills(text)
        categorized: Dict[str, List[str]] = {}

        for skill in extracted:
            category = self.taxonomy.get(skill, "General")
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(skill)

        return categorized

    def compute_dense_embedding(self, text: str) -> np.ndarray:
        """Generates a 384-dimensional dense semantic embedding via SBERT.

        The resulting vector is L2-normalized to unit length to enable fast dot-product
        cosine similarity against corporate job description benchmarks.

        Args:
            text: Input resume text string.

        Returns:
            np.ndarray: 1D float32 array of shape (384,) with unit norm.
        """
        self._load_artifacts()
        if not text or not text.strip() or self._model is None:
            return np.zeros(384, dtype=np.float32)

        # Truncate text to 4096 characters to fit within transformer context safely
        truncated_text = text[:4096]
        embedding = self._model.encode(
            truncated_text,
            normalize_embeddings=True,
            show_progress_bar=False,
            device="cpu",
        )
        return np.asarray(embedding, dtype=np.float32)

    def compute_cosine_similarity(
        self,
        resume_embedding: np.ndarray,
        target_company_id: Optional[int] = None,
    ) -> Dict[str, float]:
        """Calculates dot product cosine similarities against precomputed JD embeddings.

        Args:
            resume_embedding: 384-D L2-normalized candidate resume vector.
            target_company_id: Optional target company ID.

        Returns:
            Dict[str, float]: Dictionary mapping company name to cosine similarity in [0.0, 1.0].
        """
        self._load_artifacts()
        if self._jd_embeddings is None or len(self._jd_embeddings) == 0:
            return {}

        if resume_embedding is None or np.all(resume_embedding == 0.0):
            return {
                meta.get("company_name", f"Company_{i+1}"): 0.0
                for i, meta in enumerate(self._jd_metadata or [])
            }

        # Since both resume_embedding and jd_embeddings are L2-normalized,
        # the matrix dot product directly calculates cosine similarity.
        similarities = np.dot(self._jd_embeddings, resume_embedding)
        company_sims: Dict[str, float] = {}

        for idx, sim in enumerate(similarities):
            # Clamp negative similarities to 0.0
            bounded_sim = float(max(0.0, min(1.0, float(sim))))
            comp_name = f"Company_{idx + 1}"
            if self._jd_metadata and idx < len(self._jd_metadata):
                comp_name = self._jd_metadata[idx].get("company_name", comp_name)

            company_sims[comp_name] = round(bounded_sim, 4)

        return company_sims

    def get_target_cosine_similarity(
        self,
        company_sims: Dict[str, float],
        target_company_id: Optional[int] = None,
        target_company_name: Optional[str] = None,
    ) -> float:
        """Extracts the primary cosine similarity for a target company or mean benchmark.

        Args:
            company_sims: Mapping of company name to similarity.
            target_company_id: Optional ID of target company.
            target_company_name: Optional name of target company.

        Returns:
            float: Target cosine similarity in [0.0, 1.0].
        """
        if target_company_name and target_company_name in company_sims:
            return company_sims[target_company_name]

        if target_company_id is not None and self._jd_metadata:
            for meta in self._jd_metadata:
                if meta.get("company_id") == target_company_id:
                    name = meta.get("company_name")
                    if name in company_sims:
                        return company_sims[name]

        if company_sims:
            return round(float(np.mean(list(company_sims.values()))), 4)
        return 0.0

    def compute_keyword_coverage(
        self,
        extracted_skills: List[str],
        target_company: Optional[Union[int, str, List[str]]] = None,
        required_skills: Optional[List[str]] = None,
        return_details: bool = False,
    ) -> Union[float, Tuple[float, List[str], List[str]]]:
        """Calculates keyword coverage ratio against target or benchmark skills.

        Args:
            extracted_skills: List of skills extracted from candidate resume.
            target_company: Optional target company ID, name, or explicit skills list.
            required_skills: Optional explicit list of required skills.
            return_details: If True, returns (coverage, matched, missing).

        Returns:
            Union[float, Tuple[float, List[str], List[str]]]:
                Coverage ratio in [0.0, 1.0], optionally with matched & missing lists.
        """
        self._load_artifacts()
        target_reqs: List[str] = []

        # 1. If explicit required_skills provided
        if required_skills is not None:
            target_reqs = required_skills
        elif isinstance(target_company, list):
            target_reqs = target_company
        elif isinstance(target_company, str):
            # Lookup by company name
            if self._jd_metadata:
                for meta in self._jd_metadata:
                    if meta.get("company_name", "").lower() == target_company.lower():
                        target_reqs = meta.get("required_skills", [])
                        break
        elif isinstance(target_company, int):
            # Lookup by company ID
            if self._jd_metadata:
                for meta in self._jd_metadata:
                    if meta.get("company_id") == target_company:
                        target_reqs = meta.get("required_skills", [])
                        break

            if not target_reqs:
                row = execute_single(GET_COMPANY_BY_ID, (target_company,))
                if row and row["required_skills_json"]:
                    try:
                        parsed = json.loads(row["required_skills_json"])
                        target_reqs = [
                            s["skill"] if isinstance(s, dict) and "skill" in s else str(s)
                            for s in parsed
                        ]
                    except json.JSONDecodeError:
                        target_reqs = []

        # 2. Fallback to foundational benchmark skills if none found
        if not target_reqs:
            target_reqs = DEFAULT_BENCHMARK_SKILLS

        extracted_lower = {s.lower() for s in extracted_skills}
        matched: List[str] = []
        missing: List[str] = []

        for req in target_reqs:
            req_str = req["skill"] if isinstance(req, dict) and "skill" in req else str(req)
            if req_str.lower() in extracted_lower or any(
                req_str.lower() in s.lower() for s in extracted_skills
            ):
                matched.append(req_str)
            else:
                missing.append(req_str)

        coverage = len(matched) / max(len(target_reqs), 1)
        coverage = min(1.0, max(0.0, coverage))
        rounded_coverage = round(coverage, 4)

        if return_details:
            return rounded_coverage, matched, missing
        return rounded_coverage

    def compute_composite_ats_score(
        self,
        cosine_similarity: float = 0.0,
        keyword_coverage: float = 0.0,
        cosine_sim: Optional[float] = None,
    ) -> float:
        """Computes the formal Composite ATS Score on a 0–100 scale.

        Formula:
            ATS Score = 0.60 * (Cosine Similarity * 100) + 0.40 * (Keyword Coverage * 100)

        Args:
            cosine_similarity: Cosine similarity in [0.0, 1.0].
            keyword_coverage: Keyword coverage ratio in [0.0, 1.0].
            cosine_sim: Optional alias for cosine_similarity.

        Returns:
            float: Composite ATS Score in [0.0, 100.0] rounded to 2 decimal places.
        """
        sim = cosine_sim if cosine_sim is not None else cosine_similarity
        ats = (0.60 * (sim * 100.0)) + (0.40 * (keyword_coverage * 100.0))
        clamped = max(0.0, min(100.0, ats))
        return round(clamped, 2)

    def evaluate_text(
        self,
        raw_text: str,
        target_company_id: Optional[int] = None,
        target_company: Optional[Union[str, int]] = None,
    ) -> Dict[str, Any]:
        """Executes full resume intelligence audit on raw document text.

        Args:
            raw_text: Raw resume document text string.
            target_company_id: Optional ID of target company for benchmark matching.
            target_company: Optional name or ID of target company.

        Returns:
            Dict[str, Any]: Comprehensive analysis results including ATS score.
        """
        start_time = time.perf_counter()
        self._load_artifacts()

        # Resolve target company name & ID
        t_id = target_company_id
        t_name: Optional[str] = None
        if target_company is not None:
            if isinstance(target_company, int):
                t_id = target_company
            elif isinstance(target_company, str):
                t_name = target_company
                if self._jd_metadata:
                    for meta in self._jd_metadata:
                        if meta.get("company_name", "").lower() == target_company.lower():
                            t_id = meta.get("company_id")
                            t_name = meta.get("company_name")
                            break

        if not raw_text or not raw_text.strip():
            latency = round(time.perf_counter() - start_time, 4)
            return {
                "overall_ats_score": 0.0,
                "ats_score": 0.0,
                "cosine_similarity": 0.0,
                "keyword_coverage": 0.0,
                "target_company_score": {
                    "company": t_name or "Benchmark Average",
                    "ats_score": 0.0,
                    "cosine_similarity": 0.0,
                    "keyword_coverage": 0.0,
                    "matched_skills": [],
                    "missing_skills": DEFAULT_BENCHMARK_SKILLS,
                },
                "company_scores": {},
                "company_similarities": {},
                "extracted_skills": [],
                "total_skills_count": 0,
                "skills_by_category": {},
                "matched_skills": [],
                "missing_skills": DEFAULT_BENCHMARK_SKILLS,
                "gap_analysis": {
                    "matched_skills": [],
                    "missing_skills": DEFAULT_BENCHMARK_SKILLS,
                    "coverage": 0.0,
                },
                "raw_text_length": 0,
                "latency_seconds": latency,
                "target_company_id": t_id,
            }

        cleaned_text = self.clean_text(raw_text)
        extracted_skills = self.extract_skills(raw_text + " " + cleaned_text)
        skills_by_cat = self.extract_skills_by_category(raw_text + " " + cleaned_text)

        # 1. Semantic Embedding & Cosine Similarity
        resume_emb = self.compute_dense_embedding(cleaned_text)
        company_sims = self.compute_cosine_similarity(resume_emb)
        primary_cosine = self.get_target_cosine_similarity(
            company_sims,
            target_company_id=t_id,
            target_company_name=t_name,
        )

        # 2. Keyword Coverage
        target_target = t_name if t_name else t_id
        cov_res = self.compute_keyword_coverage(
            extracted_skills,
            target_company=target_target,
            return_details=True,
        )
        assert isinstance(cov_res, tuple)
        coverage, matched, missing = cov_res

        # 3. Composite ATS Score
        overall_ats = self.compute_composite_ats_score(primary_cosine, coverage)

        # 4. Detailed Per-Company ATS Breakdown
        company_scores: Dict[str, float] = {}
        for comp_name, sim in company_sims.items():
            comp_cov = self.compute_keyword_coverage(
                extracted_skills,
                target_company=comp_name,
                return_details=False,
            )
            assert isinstance(comp_cov, float)
            company_scores[comp_name] = self.compute_composite_ats_score(sim, comp_cov)

        target_company_score = {
            "company": t_name or "Benchmark Average",
            "ats_score": overall_ats,
            "cosine_similarity": primary_cosine,
            "keyword_coverage": coverage,
            "matched_skills": matched,
            "missing_skills": missing,
        }

        latency = round(time.perf_counter() - start_time, 4)

        return {
            "overall_ats_score": overall_ats,
            "ats_score": overall_ats,
            "cosine_similarity": primary_cosine,
            "keyword_coverage": coverage,
            "target_company_score": target_company_score,
            "company_scores": company_scores,
            "company_similarities": company_sims,
            "extracted_skills": extracted_skills,
            "total_skills_count": len(extracted_skills),
            "skills_by_category": skills_by_cat,
            "matched_skills": matched,
            "missing_skills": missing,
            "gap_analysis": {
                "matched_skills": matched,
                "missing_skills": missing,
                "coverage": coverage,
            },
            "raw_text_length": len(raw_text),
            "latency_seconds": latency,
            "target_company_id": t_id,
        }

    def evaluate_resume(
        self,
        file_path: Union[str, Path],
        target_company_id: Optional[int] = None,
        target_company: Optional[Union[str, int]] = None,
    ) -> Dict[str, Any]:
        """Extracts text from a document file and performs full ATS evaluation.

        Args:
            file_path: Path to the resume file (PDF, DOCX, TXT).
            target_company_id: Optional target company ID.
            target_company: Optional target company name or ID.

        Returns:
            Dict[str, Any]: Analysis results with file metadata attached.
        """
        raw_text = self.extract_text(file_path)
        result = self.evaluate_text(
            raw_text,
            target_company_id=target_company_id,
            target_company=target_company,
        )
        result["file_path"] = str(file_path)
        return result

    def has_resume(
        self,
        student_id: Optional[int] = None,
        db_path: Optional[Union[str, Path]] = None,
    ) -> bool:
        """Checks if the associated student has an uploaded resume in the database.

        Args:
            student_id: Optional explicit student ID.
            db_path: Optional explicit database path.

        Returns:
            bool: True if at least one resume record exists for student_id.
        """
        sid = student_id if student_id is not None else self.student_id
        if sid is None:
            return False

        row = execute_single(GET_LATEST_RESUME, (sid,), db_path=db_path)
        return row is not None

    def get_resume_score(
        self,
        student_id: Optional[int] = None,
        db_path: Optional[Union[str, Path]] = None,
    ) -> Optional[ResumeScoreResult]:
        """Retrieves the latest ATS score and extracted skills for the student.

        Required interface method for PRIEOrchestrator coordination.

        Args:
            student_id: Optional explicit student ID.
            db_path: Optional explicit database path.

        Returns:
            Optional[ResumeScoreResult]: Tuple-like result (ats_score, skills) or None.
        """
        sid = student_id if student_id is not None else self.student_id
        if sid is None:
            return None

        row = execute_single(GET_LATEST_RESUME, (sid,), db_path=db_path)
        if not row:
            return None

        ats_score = float(row["ats_score"] or 0.0)
        try:
            skills = json.loads(row["extracted_skills_json"] or "[]")
        except Exception:
            skills = []

        return ResumeScoreResult(
            ats_score=round(ats_score, 2),
            skills=skills,
            student_id=sid,
            row=row,
        )

    def save_resume_analysis(
        self,
        student_id: Optional[int] = None,
        file_path: Optional[Union[str, Path]] = None,
        analysis: Optional[Dict[str, Any]] = None,
        raw_text: Optional[str] = None,
        evaluation: Optional[Dict[str, Any]] = None,
        file_name: Optional[str] = None,
        file_text: Optional[str] = None,
        db_path: Optional[Union[str, Path]] = None,
    ) -> bool:
        """Persists a new resume record and its analysis into SQLite resumes table.

        Args:
            student_id: ID of the student.
            file_path: File path on disk.
            analysis: Output dictionary from evaluate_resume or evaluate_text.
            raw_text: Optional raw extracted text.
            evaluation: Alias for analysis dictionary.
            file_name: Alias for file_path.
            file_text: Alias for raw_text.
            db_path: Optional explicit database path.

        Returns:
            bool: True upon successful database insertion.
        """
        sid = student_id if student_id is not None else self.student_id
        if sid is None:
            raise ValueError("student_id must be provided to save resume analysis.")

        eval_dict = evaluation or analysis or {}
        path_str = str(file_path or file_name or "resume.pdf")
        text_content = raw_text or file_text or eval_dict.get("raw_text", "")
        skills_json = json.dumps(eval_dict.get("extracted_skills", []))
        ats = eval_dict.get("overall_ats_score", eval_dict.get("ats_score", 0.0))
        cosine = eval_dict.get("cosine_similarity", 0.0)
        coverage = eval_dict.get("keyword_coverage", 0.0)

        target_comp = eval_dict.get("target_company_id", "all")
        jd_hash = hashlib.md5(f"jd_{target_comp}_{ats}".encode("utf-8")).hexdigest()[:16]

        resume_id = execute_insert(
            INSERT_RESUME,
            (
                sid,
                path_str,
                text_content,
                skills_json,
                ats,
                cosine,
                coverage,
                jd_hash,
            ),
            db_path=db_path,
        )
        logger.info(
            "Persisted resume ID %d for student %d (ATS: %.1f).",
            resume_id,
            sid,
            ats,
        )
        return True
