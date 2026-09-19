"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Document Text Extraction & Normalization Utilities
File: utils/text_processing.py

Provides robust, multi-format text extraction for PDF and Word DOCX documents,
technical token cleaning preserving programming language syntax (C++, C#, .NET),
and domain-specific regex pattern compilation with strict word boundaries.
"""

from __future__ import annotations

import logging
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Pattern, Set, Union

logger = logging.getLogger("PRIE.TextProcessing")

# Suppress pymupdf deprecation warnings if present
try:
    import pymupdf as fitz  # Standard modern PyMuPDF
except ImportError:
    try:
        import fitz  # Fallback to classic fitz namespace
    except ImportError:
        fitz = None  # type: ignore

try:
    import docx
except ImportError:
    docx = None  # type: ignore

# Technical keywords where special characters must be preserved during normalization
PRESERVED_TOKENS: Dict[str, str] = {
    "c++": "__tokencpp__",
    "c#": "__tokencsharp__",
    ".net": "__tokendotnet__",
    "node.js": "__tokennodejs__",
    "vue.js": "__tokenvuejs__",
    "react.js": "__tokenreactjs__",
    "next.js": "__tokennextjs__",
    "express.js": "__tokenexpressjs__",
    "tcp/ip": "__tokentcpip__",
    "ci/cd": "__tokencicd__",
    "rest/api": "__tokenrestapi__",
}


def extract_text_from_pdf(file_path: Union[str, Path]) -> str:
    """Extracts plain text from a PDF document using PyMuPDF.

    Args:
        file_path: Path to the target PDF file.

    Returns:
        str: Extracted text content across all pages.

    Raises:
        FileNotFoundError: If the PDF file does not exist.
        ValueError: If PyMuPDF is not installed or document cannot be read.
    """
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"PDF document not found: {path}")

    if fitz is None:
        raise ValueError("PyMuPDF / fitz is not installed in the active environment.")

    extracted_pages: List[str] = []
    try:
        doc = fitz.open(str(path))
        for page_idx, page in enumerate(doc):
            page_text = page.get_text()
            if page_text:
                extracted_pages.append(page_text.strip())
        doc.close()
    except Exception as err:
        logger.error("Error extracting text from PDF '%s': %s", path.name, err)
        raise ValueError(f"Failed to read PDF document '{path.name}': {err}") from err

    full_text = "\n\n".join(extracted_pages).strip()
    logger.debug("Extracted %d characters from PDF: %s", len(full_text), path.name)
    return full_text


def extract_text_from_docx(file_path: Union[str, Path]) -> str:
    """Extracts plain text from a DOCX document including tables.

    Args:
        file_path: Path to the target Word document.

    Returns:
        str: Extracted text content from paragraphs and tables.

    Raises:
        FileNotFoundError: If the DOCX file does not exist.
        ValueError: If python-docx is not installed or document cannot be read.
    """
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"DOCX document not found: {path}")

    if docx is None:
        raise ValueError("python-docx is not installed in the active environment.")

    text_parts: List[str] = []
    try:
        doc = docx.Document(str(path))
        # 1. Extract standard paragraphs
        for para in doc.paragraphs:
            stripped = para.text.strip()
            if stripped:
                text_parts.append(stripped)

        # 2. Extract table cells (resumes often use tables for education/skills)
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    cell_text = cell.text.strip()
                    if cell_text and cell_text not in text_parts:
                        text_parts.append(cell_text)
    except Exception as err:
        logger.error("Error extracting text from DOCX '%s': %s", path.name, err)
        raise ValueError(f"Failed to read DOCX document '{path.name}': {err}") from err

    full_text = "\n\n".join(text_parts).strip()
    logger.debug("Extracted %d characters from DOCX: %s", len(full_text), path.name)
    return full_text


def extract_document_text(file_path: Union[str, Path]) -> str:
    """Extracts raw text from a document based on its file extension.

    Supports .pdf, .docx, .doc, and .txt formats with defensive validation.

    Args:
        file_path: Path to the document.

    Returns:
        str: Extracted document text.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file extension is unsupported or file is corrupted.
    """
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"Resume document not found at: {path}")

    suffix = path.suffix.lower()
    if suffix == ".pdf":
        text = extract_text_from_pdf(path)
    elif suffix in (".docx", ".doc"):
        text = extract_text_from_docx(path)
    elif suffix == ".txt":
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
        except UnicodeDecodeError:
            with open(path, "r", encoding="latin-1") as f:
                text = f.read().strip()
    else:
        raise ValueError(
            f"Unsupported resume file format '{suffix}'. "
            "Supported formats: PDF (.pdf), Word (.docx), and Plain Text (.txt)."
        )

    if len(text.strip()) < 10:
        logger.warning(
            "Extracted text from '%s' is suspiciously short (%d chars). "
            "File may be scanned or empty.",
            path.name,
            len(text),
        )

    return text


def normalize_technical_text(text: str) -> str:
    """Cleans and normalizes technical resume text while preserving language syntax.

    Preserves critical programming language identifiers (e.g. C++, C#, .NET, Node.js)
    while removing noisy punctuation, normalizing whitespace, and lowercasing.

    Args:
        text: Raw document text string.

    Returns:
        str: Cleaned, normalized technical text.
    """
    if not text or not isinstance(text, str):
        return ""

    cleaned = text.lower()

    # Step 1: Protect specific technical tokens by replacing with unique placeholders
    token_mapping: Dict[str, str] = {}
    for token, placeholder in PRESERVED_TOKENS.items():
        # Match token when not embedded in other alphabetic characters
        pattern = r"(?<![a-z0-9_])" + re.escape(token) + r"(?![a-z0-9_])"
        if re.search(pattern, cleaned):
            cleaned = re.sub(pattern, placeholder, cleaned)
            token_mapping[placeholder] = token

    # Step 2: Replace bullet points, formatting symbols, and punctuation
    # Allow alphanumeric, whitespace, placeholders, and basic punctuation
    cleaned = re.sub(r"[^\w\s\+\#\.\-/]", " ", cleaned)

    # Step 3: Strip standalone punctuation and trailing periods from sentences
    # e.g., "experience." -> "experience ", but not in "__TOKEN_DOTNET__"
    cleaned = re.sub(r"(?<!\w)\.(?!\w)", " ", cleaned)
    cleaned = re.sub(r"(?<=\w)\.(?=\s|$)", " ", cleaned)

    # Step 4: Restore preserved technical tokens
    for placeholder, original in token_mapping.items():
        cleaned = cleaned.replace(placeholder, original)

    # Step 5: Collapse multiple spaces, tabs, and newlines into single spaces
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    return cleaned


def build_skill_regex_pattern(skill: str) -> Pattern[str]:
    """Compiles a word-boundary regex pattern for exact skill matching.

    Employs boundary assertions that handle non-word character terminals
    like C++, C#, and .NET while preventing false-positive substring collisions
    (e.g., preventing "c" from matching inside "react", "cat", or "css").
    Supports flexible whitespace for multi-word skill phrases.

    Args:
        skill: Canonical skill name or synonym string (e.g. "C++", "Python", "C").

    Returns:
        Pattern[str]: Compiled case-insensitive regex pattern.
    """
    words = skill.strip().lower().split()
    if not words:
        return re.compile(r"$^")  # Matches nothing for empty string

    # Match each word escaped, allowing flexible whitespace (\s+) between words
    escaped_words = [re.escape(w) for w in words]
    escaped = r"\s+".join(escaped_words)

    # (?<![a-zA-Z0-9_]) ensures no preceding alphanumeric/underscore
    # (?![a-zA-Z0-9_]) ensures no following alphanumeric/underscore
    boundary_pattern = r"(?<![a-zA-Z0-9_])" + escaped + r"(?![a-zA-Z0-9_])"
    return re.compile(boundary_pattern, re.IGNORECASE)
