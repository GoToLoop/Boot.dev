# pyright: reportMissingModuleSource = false

from pygame.colordict import THECOLORS
from pygame._common import ColorValue

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
LINE_WIDTH = 2
FPS = 60

PLAYER_RADIUS = 20
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300
WIDTH_RATIO = 1.5

BG: ColorValue = THECOLORS["black"]
SHIP_COLOR: ColorValue = THECOLORS["white"]
