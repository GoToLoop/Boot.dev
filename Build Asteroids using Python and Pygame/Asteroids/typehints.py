# pyright: reportMissingModuleSource = hint

from typing import TYPE_CHECKING

if TYPE_CHECKING: from pygame._common import (
    Coordinate, ColorValue, RGBAOutput
)
else: Coordinate = ColorValue = RGBAOutput = None

__all__ = "Coordinate", "ColorValue", "RGBAOutput"
