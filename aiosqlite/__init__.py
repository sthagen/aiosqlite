# Copyright 2018 John Reese
# Licensed under the MIT license

"""asyncio bridge to the standard sqlite3 module"""

from sqlite3 import (  # pylint: disable=redefined-builtin
    DatabaseError,
    Error,
    IntegrityError,
    NotSupportedError,
    OperationalError,
    ProgrammingError,
    register_adapter,
    register_converter,
    Row,
    sqlite_version,
    sqlite_version_info,
    Warning,
)

__author__ = "John Reese"
from .__version__ import __version__
from .core import connect, Connection, Cursor

__all__ = [
    "__version__",
    "register_adapter",
    "register_converter",
    "sqlite_version",
    "sqlite_version_info",
    "connect",
    "Connection",
    "Cursor",
    "Row",
    "Warning",
    "Error",
    "DatabaseError",
    "IntegrityError",
    "ProgrammingError",
    "OperationalError",
    "NotSupportedError",
]
