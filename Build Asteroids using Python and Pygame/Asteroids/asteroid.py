from circleshape import CircleShape
from typehints import ColorValue

import pygame
from typing import override

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.SurfaceType): ...
        # pygame.draw.polygon(screen, SHIP_COLOR, self.triangle(), LINE_WIDTH)

    
    @override
    def update(self, Δ: float): ... # amount to rotate or move (Δ in seconds)