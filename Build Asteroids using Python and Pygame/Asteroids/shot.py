from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH, BULLET_COLOR

from pygame import draw, Surface
from typing import override

class Shot(CircleShape):
    """Represents a projectile fired by the player, traveling in a straight
    line across the screen until hitting an asteroid or reaching off-screen.
    """
    def __init__(self, x: float, y: float):
        """Initialize the shot at the specified coordinates with a standard
        bullet radius.
        """
        super().__init__(x, y, SHOT_RADIUS)


    @override
    def draw(self, screen: Surface):
        """Render the bullet as a circle outline onto the target surface."""
        draw.circle(
            screen, BULLET_COLOR, self.position, self.radius, LINE_WIDTH
        )


    @override
    def update(self, Δ: float): # amount to move (Δ in seconds)
        """Update bullet's position based on its velocity & elapsed time.
        Kill it if it flies beyond the visible screen.
        """
        self.position += self.velocity * Δ
        self.check_outside() and self.kill()
