from enum import IntEnum, auto
from typing import Literal, Tuple

class Cardinal(IntEnum):
    """Cardinal directions for canvas edges."""
    INSIDE = 0; WEST = auto(); EAST = auto(); NORTH = auto(); SOUTH = auto()

Signum = Literal[1, 0, -1]
"""(positive, zero, negative)"""

Vec = Tuple[float, float]
"""A 2D vector represented as an immutable pair of floats (x, y)."""

Tri = Tuple[Vec, Vec, Vec]
"""A triangle represented as an immutable triple of 2D vertices (v0, v1, v2)."""
