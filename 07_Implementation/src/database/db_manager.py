"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Database Connection Manager and Persistence Utilities
File: database/db_manager.py

Implements a thread-safe SQLite connection context manager, transaction boundary
enforcement, parameter validation, and execution helper primitives.
"""

from __future__ import annotations

import logging
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator, List, Optional, Sequence, Tuple, Union
import sqlite3

import config

logger = logging.getLogger("PRIE.Database")


class Row(sqlite3.Row):
    """Subclass of sqlite3.Row that adds dictionary helper methods (get, items, values)."""

    def get(self, key: str, default: Any = None) -> Any:
        """Return the value for key if key is in row column names, else default."""
        return self[key] if key in self.keys() else default

    def items(self) -> List[Tuple[str, Any]]:
        """Return list of (column_name, value) tuples for this row."""
        return [(k, self[k]) for k in self.keys()]

    def values(self) -> List[Any]:
        """Return list of column values for this row."""
        return [self[k] for k in self.keys()]


def get_default_db_path() -> Path:
    """Returns the canonical Path to the SQLite database."""
    return config.DATABASE_PATH


@contextmanager
def get_db_connection(
    db_path: Optional[Union[str, Path]] = None,
) -> Generator[sqlite3.Connection, None, None]:
    """Context manager providing a thread-safe SQLite connection.

    Configures:
    - Write-Ahead Logging (WAL) for high concurrency
    - Foreign key constraint enforcement
    - busy_timeout for lock management
    - sqlite3.Row row factory for dictionary-style attribute access
    - Automatic transaction commit on success or rollback on exception

    Args:
        db_path: Optional explicit file path to database. Defaults to config.DATABASE_PATH.

    Yields:
        sqlite3.Connection: Active database connection.
    """
    target_path = Path(db_path) if db_path is not None else get_default_db_path()

    # Ensure parent directory exists for file databases (skip for in-memory)
    if str(target_path) != ":memory:":
        target_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(
        str(target_path),
        timeout=float(getattr(config, "DB_TIMEOUT", 30)),
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
    )
    conn.row_factory = Row

    # Enforce SQLite operational PRAGMAs
    conn.execute("PRAGMA foreign_keys = ON;")
    if str(target_path) != ":memory:":
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA synchronous = NORMAL;")
    conn.execute("PRAGMA busy_timeout = 30000;")

    try:
        yield conn
        conn.commit()
    except Exception as exc:
        conn.rollback()
        logger.error("Transaction failed, rolled back: %s", exc)
        raise exc
    finally:
        conn.close()


def execute_query(
    query: str,
    params: Sequence[Any] = (),
    db_path: Optional[Union[str, Path]] = None,
) -> List[sqlite3.Row]:
    """Execute a parameterized SELECT query and return all matched rows.

    Args:
        query: Parameterized SQL SELECT string.
        params: Sequence of parameter arguments.
        db_path: Optional explicit database path.

    Returns:
        List of sqlite3.Row instances matching the query.
    """
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()


def execute_single(
    query: str,
    params: Sequence[Any] = (),
    db_path: Optional[Union[str, Path]] = None,
) -> Optional[sqlite3.Row]:
    """Execute a parameterized SELECT query and return the first matching row.

    Args:
        query: Parameterized SQL SELECT string.
        params: Sequence of parameter arguments.
        db_path: Optional explicit database path.

    Returns:
        The first sqlite3.Row instance, or None if no match found.
    """
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()


def execute_insert(
    query: str,
    params: Sequence[Any] = (),
    db_path: Optional[Union[str, Path]] = None,
) -> int:
    """Execute a parameterized INSERT statement and return the inserted row ID.

    Args:
        query: Parameterized SQL INSERT string.
        params: Sequence of parameter arguments.
        db_path: Optional explicit database path.

    Returns:
        int: The integer rowid of the newly inserted record.
    """
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.lastrowid or 0


def execute_update(
    query: str,
    params: Sequence[Any] = (),
    db_path: Optional[Union[str, Path]] = None,
) -> int:
    """Execute a parameterized UPDATE or DELETE statement and return affected row count.

    Args:
        query: Parameterized SQL UPDATE or DELETE string.
        params: Sequence of parameter arguments.
        db_path: Optional explicit database path.

    Returns:
        int: Total count of rows affected by the statement.
    """
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.rowcount


def execute_script(
    script_sql: str,
    db_path: Optional[Union[str, Path]] = None,
) -> None:
    """Execute multi-statement SQL scripts (DDL schemas, bulk migration DDLs).

    Args:
        script_sql: Multi-statement SQL text.
        db_path: Optional explicit database path.
    """
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.executescript(script_sql)


def backup_database(
    destination_path: Union[str, Path],
    source_path: Optional[Union[str, Path]] = None,
) -> None:
    """Execute an online SQLite backup to a target destination file.

    Args:
        destination_path: Path where database backup will be saved.
        source_path: Optional explicit source database path. Defaults to config.DATABASE_PATH.
    """
    dest_path = Path(destination_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    with get_db_connection(source_path) as src_conn:
        dest_conn = sqlite3.connect(str(dest_path))
        try:
            src_conn.backup(dest_conn)
            logger.info("Database backup completed successfully to %s", dest_path)
        finally:
            dest_conn.close()
