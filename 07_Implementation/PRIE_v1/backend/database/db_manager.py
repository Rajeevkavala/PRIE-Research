"""
PRIE v1 — SQLite Database Manager
File: backend/database/db_manager.py

Implements thread-safe SQLite connection management with WAL mode, foreign key
enforcement, and Row factory for dict-like access.

Traceability: 05_PRIE_Architecture/System_Architecture.md → Layer 5 (SPV-DB)
"""

from __future__ import annotations

import logging
import sqlite3
import threading
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Union

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config

logger = logging.getLogger("PRIE.DBManager")

_local = threading.local()


def _get_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Return a thread-local SQLite connection with WAL mode and row factory."""
    path = db_path or config.DATABASE_PATH
    conn_key = str(path)

    if not hasattr(_local, "connections"):
        _local.connections = {}

    if conn_key not in _local.connections:
        conn = sqlite3.connect(
            str(path),
            timeout=config.DB_TIMEOUT,
            check_same_thread=False,
        )
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA synchronous = NORMAL;")
        _local.connections[conn_key] = conn
        logger.debug(f"Opened SQLite connection: {path}")

    return _local.connections[conn_key]


def initialize_schema(db_path: Optional[Path] = None) -> None:
    """Create all tables from schema.sql if they don't exist."""
    schema_path = Path(__file__).parent / "schema.sql"
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    ddl = schema_path.read_text(encoding="utf-8")
    conn = _get_connection(db_path)
    try:
        conn.executescript(ddl)
        conn.commit()
        logger.info("Database schema initialized successfully.")
    except sqlite3.Error as e:
        logger.error(f"Schema initialization failed: {e}")
        raise


def execute_query(
    sql: str,
    params: Sequence[Any] = (),
    db_path: Optional[Path] = None,
) -> List[sqlite3.Row]:
    """Execute a SELECT query and return all matching rows."""
    conn = _get_connection(db_path)
    try:
        cursor = conn.execute(sql, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        logger.error(f"Query failed: {e} | SQL: {sql[:120]}")
        raise


def execute_single(
    sql: str,
    params: Sequence[Any] = (),
    db_path: Optional[Path] = None,
) -> Optional[sqlite3.Row]:
    """Execute a SELECT query and return the first row or None."""
    conn = _get_connection(db_path)
    try:
        cursor = conn.execute(sql, params)
        return cursor.fetchone()
    except sqlite3.Error as e:
        logger.error(f"Single query failed: {e} | SQL: {sql[:120]}")
        raise


def execute_update(
    sql: str,
    params: Sequence[Any] = (),
    db_path: Optional[Path] = None,
) -> int:
    """Execute an INSERT/UPDATE/DELETE and return rows affected. Auto-commits."""
    conn = _get_connection(db_path)
    try:
        cursor = conn.execute(sql, params)
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error as e:
        conn.rollback()
        logger.error(f"Update failed: {e} | SQL: {sql[:120]}")
        raise


def execute_insert(
    sql: str,
    params: Sequence[Any] = (),
    db_path: Optional[Path] = None,
) -> int:
    """Execute an INSERT and return the lastrowid."""
    conn = _get_connection(db_path)
    try:
        cursor = conn.execute(sql, params)
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        conn.rollback()
        logger.error(f"Insert failed: {e} | SQL: {sql[:120]}")
        raise


def dict_row(row: Optional[sqlite3.Row]) -> Optional[Dict[str, Any]]:
    """Convert a sqlite3.Row to a plain dict, or return None."""
    return dict(row) if row is not None else None


def dict_rows(rows: List[sqlite3.Row]) -> List[Dict[str, Any]]:
    """Convert a list of sqlite3.Row objects to plain dicts."""
    return [dict(r) for r in rows]
