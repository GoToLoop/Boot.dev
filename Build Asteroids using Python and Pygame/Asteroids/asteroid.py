from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_COLOR

import pygame
from typing import override

class Asteroid(CircleShape):
    """Represents a destructible asteroid obstacle that moves across the
    playfield and can be rendered onto the screen.
    """
    def __init__(self, x: float, y: float, radius: float, vel: pygame.Vector2):
        """Initialize an asteroid with position, size, and initial velocity."""
        super().__init__(x, y, radius)
        self.velocity = vel


    @override
    def draw(self, screen: pygame.SurfaceType):
        """Render the asteroid as a circle outline onto the target surface."""
        pygame.draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH
        )


    @override
    def update(self, Δ: float): # amount to move (Δ in seconds)
        """Update asteroid's position based on its velocity & elapsed time."""
        self.position += self.velocity * Δ
