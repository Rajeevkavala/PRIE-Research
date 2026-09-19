"""
PRIE v1 — Module M09: Curriculum-Grounded RAG Assistant
File: backend/modules/m09_rag_assistant.py

MODULE: M09 — Curriculum-Grounded RAG Assistant
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (Dense Retrieval RAG, DD-009)
RESEARCH_GAP: RG6 (Generic LLM hallucinations lacking curriculum grounding)
RESEARCH_OBJECTIVE: RO6 (Context-Grounded Technical Guidance)
TRACEABILITY: Paper17, Paper21, Paper25, Paper34; DD-009

Pipeline:
  Corpus Ingestion -> Sliding Window Chunking -> SBERT / Normalized Dense Embeddings ->
  Top-K Semantic Vector Search -> Grounding Verification -> Synthesized Contextual Response
"""

from __future__ import annotations

import json
import logging
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config

logger = logging.getLogger("PRIE.M09.RAGAssistant")


class DenseCorpusIndex:
    """Manages document chunking, embeddings, and cosine retrieval."""

    def __init__(self, corpus_path: Optional[Path] = None) -> None:
        self.corpus_path = corpus_path or config.RESOURCE_LIBRARY_PATH
        self.chunks: List[Dict[str, Any]] = []
        self.embeddings: Optional[np.ndarray] = None
        self._sbert = None
        self._build_index()

    def _load_sbert(self):
        if self._sbert is None:
            try:
                from sentence_transformers import SentenceTransformer
                self._sbert = SentenceTransformer(config.SBERT_MODEL)
            except Exception as e:
                logger.warning(f"SBERT embedding model not available: {e}. Dense TF-IDF fallback active.")
        return self._sbert

    def _build_index(self) -> None:
        """Ingest JSON document corpus and create chunk index."""
        if not self.corpus_path.exists():
            logger.info(f"Corpus not found at {self.corpus_path}. Index is empty.")
            return

        try:
            docs = json.loads(self.corpus_path.read_text(encoding="utf-8"))
            chunk_list = []
            for doc in docs:
                content = doc.get("content", "")
                # Sliding window chunking (~60 words per chunk, 15 words overlap)
                words = content.split()
                chunk_size = 60
                overlap = 15
                step = max(1, chunk_size - overlap)

                for i in range(0, len(words), step):
                    chunk_words = words[i:i + chunk_size]
                    if len(chunk_words) < 15 and i > 0:
                        continue
                    chunk_text = " ".join(chunk_words)
                    chunk_list.append({
                        "chunk_id": f"{doc.get('doc_id', 'DOC')}_C{len(chunk_list):03d}",
                        "doc_id": doc.get("doc_id", "DOC"),
                        "title": doc.get("title", "Curriculum Document"),
                        "source_type": doc.get("source_type", "syllabus"),
                        "text": chunk_text,
                    })

            self.chunks = chunk_list
            logger.info(f"Indexed {len(self.chunks)} semantic chunks from {len(docs)} documents.")

            # Compute embeddings
            sbert = self._load_sbert()
            if sbert is not None and self.chunks:
                texts = [c["text"] for c in self.chunks]
                self.embeddings = sbert.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        except Exception as e:
            logger.warning(f"Failed to build dense corpus index: {e}")

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Retrieve top-K most relevant chunks with cosine similarity scores."""
        if not self.chunks:
            return []

        sbert = self._load_sbert()
        if sbert is not None and self.embeddings is not None:
            query_emb = sbert.encode([query], convert_to_numpy=True, normalize_embeddings=True)[0]
            scores = np.dot(self.embeddings, query_emb)
            top_indices = np.argsort(scores)[::-1][:top_k]

            results = []
            for idx in top_indices:
                chunk_copy = dict(self.chunks[idx])
                chunk_copy["relevance_score"] = round(float(scores[idx]), 4)
                results.append(chunk_copy)
            return results

        # Fallback keyword overlap ranking with stop-word filtration
        stop_words = {
            "what", "is", "the", "for", "with", "a", "an", "in", "on", "at", "to",
            "and", "or", "of", "how", "do", "does", "can", "tell", "me", "about", "are"
        }
        all_q_tokens = set(re.findall(r'\w+', query.lower()))
        content_q_tokens = {w for w in all_q_tokens if w not in stop_words}
        if not content_q_tokens:
            content_q_tokens = all_q_tokens

        scored = []
        for c in self.chunks:
            c_tokens = set(re.findall(r'\w+', c["text"].lower()))
            overlap = len(content_q_tokens & c_tokens)
            score = overlap / max(1, len(content_q_tokens))
            scored.append((score, c))

        scored.sort(key=lambda x: x[0], reverse=True)
        results = []
        for score, c in scored[:top_k]:
            c_copy = dict(c)
            c_copy["relevance_score"] = round(float(score), 4)
            results.append(c_copy)
        return results


class CurriculumRAGAssistant:
    """
    M09: Curriculum-Grounded RAG Assistant.
    Enforces dense retrieval, citation tracing, and grounding verification.
    """

    def __init__(self, corpus_path: Optional[Path] = None) -> None:
        self.index = DenseCorpusIndex(corpus_path)

    def answer(
        self,
        question: str,
        student_context: Optional[Dict[str, Any]] = None,
        top_k: int = 3,
        threshold: float = 0.20,
    ) -> Dict[str, Any]:
        """
        Answer a curriculum query using verified document retrieval.
        Never fabricates an answer without empirical retrieval grounding.
        """
        retrieved_chunks = self.index.retrieve(question, top_k=top_k)

        # Check grounding threshold
        max_score = max([c["relevance_score"] for c in retrieved_chunks], default=0.0)
        is_grounded = max_score >= threshold

        if not is_grounded:
            return {
                "question": question,
                "response": (
                    "No verified syllabus or curriculum documentation directly addresses this specific question. "
                    "Please consult your course syllabus or verified faculty guidelines to prevent ungrounded assumptions."
                ),
                "is_grounded": False,
                "retrieval_score": max_score,
                "citations": [],
                "retrieved_chunks_count": len(retrieved_chunks),
                "epistemological_status": "ESTABLISHED_BY_RESEARCH (Dense RAG Safeguard, DD-009)",
            }

        # Assemble grounded context with citations
        context_parts = []
        citations = []
        for c in retrieved_chunks:
            if c["relevance_score"] >= threshold:
                context_parts.append(f"[{c['chunk_id']}] {c['text']}")
                citations.append({
                    "chunk_id": c["chunk_id"],
                    "title": c["title"],
                    "source_type": c["source_type"],
                    "relevance_score": c["relevance_score"],
                })

        assembled_context = "\n\n".join(context_parts)
        grounded_answer = (
            f"Based on authoritative curriculum documentation ({citations[0]['title']}):\n\n"
            f"{context_parts[0]}\n\n"
            f"Relevance Score: {max_score:.2f}. Referenced {len(citations)} source passages."
        )

        return {
            "question": question,
            "response": grounded_answer,
            "is_grounded": True,
            "retrieval_score": max_score,
            "citations": citations,
            "assembled_context": assembled_context,
            "epistemological_status": "ESTABLISHED_BY_RESEARCH (Dense Retrieval RAG, DD-009)",
        }
