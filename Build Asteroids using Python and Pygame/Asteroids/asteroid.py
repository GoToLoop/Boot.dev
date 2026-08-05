from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_COLOR

from pygame import draw, SurfaceType
from typing import override

class Asteroid(CircleShape):
    """Represents a destructible asteroid obstacle that moves across the
    playfield and can be rendered onto the screen.
    """
    def __init__(self, x: float, y: float, radius: float, vx: float, vy: float):
        """Initialize an asteroid with position, size, and initial velocity."""
        super().__init__(x, y, radius)
        self.velocity.update(vx, vy)


    @override
    def draw(self, screen: SurfaceType):
        """Render the asteroid as a circle outline onto the target surface."""
        draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH
        )


    @override
    def update(self, Δ: float): # amount to move (Δ in seconds)
        """Update asteroid's position based on its velocity & elapsed time."""
        self.position += self.velocity * Δ
