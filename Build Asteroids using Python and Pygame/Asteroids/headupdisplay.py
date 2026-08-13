from pygame import Surface, font, time
from typing import Final

from constants import FONT_SIZE, FONT_OFFSET, FONT_COLOR, HUDS
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


    def render_info(self, surface: Surface, clock: time.Clock):
        """Vertically render fps, asteroid & shot counts onto a display surface.

        Args:
            surface: Surface on which the HuD text is rendered.
            clock: Pygame clock used to retrieve the current frame rate.
        """
        infos = clock.get_fps(), len(asteroids), len(shots)

        for idx, hud in enumerate(HUDS):
            txt_surface = self.font.render(hud % infos[idx], True, FONT_COLOR)
            txt_coords = FONT_OFFSET, FONT_OFFSET + self.font_size * idx
            surface.blit(txt_surface, txt_coords)
