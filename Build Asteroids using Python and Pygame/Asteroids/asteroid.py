from circleshape import CircleShape
from logger import log_event

from constants import (
    ASTEROID_COLOR, ASTEROID_MIN_RADIUS, LINE_WIDTH, SIGNUMS, LOGGING,
    ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE, ASTEROID_ACCEL
)

from pygame import draw, Surface, Vector2
from random import uniform
from typing import override

class Asteroid(CircleShape):
    """Represents a destructible asteroid obstacle that moves across the
    playfield and can be rendered onto the screen.
    """
    def __init__(self, x: float, y: float, radius: float, vx: float, vy: float):
        """Initialize an asteroid with position, size, and initial velocity."""
        super().__init__(x, y, radius)
        self.velocity.update(vx, vy)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return

        LOGGING and log_event("asteroid_split")

        x, y = self.position
        vel = Vector2()
        rad = self.radius - ASTEROID_MIN_RADIUS
        θ = uniform(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE)

        for signum in SIGNUMS: # rotate signum range: (1, -1)
            vel.update(self.velocity) # start same vel as destroyed asteroid
            vel.rotate_ip(signum * θ) # rotate 1st clockwise, 2nd anti-clockwise
            vel *= ASTEROID_ACCEL # make new split asteroids faster
            Asteroid(x, y, rad, *vel) # spawn smaller and at same position


    @override
    def draw(self, screen: Surface):
        """Render the asteroid as a circle outline onto the target surface."""
        draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH
        )


    @override
    def update(self, Δ: float): # amount to move (Δ in seconds)
        """Update asteroid's position based on its velocity & elapsed time."""
        self.position += self.velocity * Δ
