"""ToolBook 8.0 OPTLOADER unpacker package.

Public API:
    is_optloader(data) -> bool
    unpack(data) -> bytes
"""

from .unpack_optloader import is_optloader, unpack

__all__ = ["is_optloader", "unpack"]
__version__ = "1.0.0"
