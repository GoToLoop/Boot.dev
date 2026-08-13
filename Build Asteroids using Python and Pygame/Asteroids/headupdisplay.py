from pygame import Surface, font
from typing import Final

from constants import FONT_SIZE, FONT_OFFSET, FONT_COLOR
from spritegroups import asteroids, shots

class Hud:
    """Display the current number of asteroids and shots."""

    AST_TXT: Final = "Asteroids: %d"
    SHOTS_TXT: Final = "Shots: %d"

    def __init__(self, font_size: int=FONT_SIZE):
        """Initialize the heads-up display.

        Arg:
            font_size: Size of the font used to display the counters (optional).
        """
        self.font_size: int = font_size
        self.font: font.Font = font.SysFont(None, font_size)


    def render_group_counts(self, surface: Surface):
        """Render asteroid and shot counts onto a display surface.

        The asteroid count is drawn at ``FONT_OFFSET`` from the top-left
        corner. The shot count is drawn below the asteroid count.

        Arg:
            surface: Surface on which the HUD text is rendered.
        """
        txt = Hud.AST_TXT % len(asteroids)
        txt_surface = self.font.render(txt, True, FONT_COLOR)
        surface.blit(txt_surface, (FONT_OFFSET, FONT_OFFSET))

        txt = Hud.SHOTS_TXT % len(shots)
        txt_surface = self.font.render(txt, True, FONT_COLOR)
        surface.blit(txt_surface, (FONT_OFFSET, FONT_OFFSET + self.font_size))
