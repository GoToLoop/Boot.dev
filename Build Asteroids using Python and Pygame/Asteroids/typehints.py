# pyright: reportMissingModuleSource = hint

from typing import TYPE_CHECKING

if TYPE_CHECKING: from pygame._common import ColorValue, RGBAOutput
else: ColorValue = RGBAOutput = None

__all__ = "ColorValue", "RGBAOutput"
