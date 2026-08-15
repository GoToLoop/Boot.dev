# pyright: reportCallInDefaultInitializer = hint

from circleshape import CircleShape
from score import score
from logger import log_event

from constants import (
    ASTEROID_MIN_RADIUS, ASTEROID_COLOR, LINE_WIDTH,
    ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE, ASTEROID_ACCEL,
    LOGGING, ASTEROID_WRAP_AROUND, ASTEROID_POINTS
)

from pygame import draw, Surface, Vector2
from random import uniform
from typing import override, Self

class Asteroid(CircleShape):
    """Represents a destructible asteroid obstacle that moves across the
    playfield and can be rendered onto the screen.
    """
    def __init__(self, x: float, y: float, radius: float, vx: float, vy: float):
        """Initialize an asteroid with position, size, and initial velocity."""
        super().__init__(x, y, radius)
        self.velocity.update(vx, vy)


    def increase_score(self) -> Self:
        """Increase the player's score based on the asteroid's size."""
        kind = int(self.radius // ASTEROID_MIN_RADIUS) - 1
        score.current_score += ASTEROID_POINTS[kind]
        return self


    def split(self):
        """Destroy this asteroid and spawn two smaller, faster asteroids.

        If the asteroid is larger than ``ASTEROID_MIN_RADIUS``, two smaller
        asteroids are created at the same position with velocities rotated in
        opposite directions by a random split angle. Asteroids at or below the
        minimum radius are destroyed without spawning new asteroids.
        """
        if self.radius <= ASTEROID_MIN_RADIUS: return self.kill()
        LOGGING and log_event("asteroid_split")

        x, y = self.position
        rad = self.radius - ASTEROID_MIN_RADIUS
        θ = uniform(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE)

        self.init(x, y, rad, *self.gestate(θ)) # respawning using same instance
        Asteroid(x, y, rad, *self.gestate(-θ)) # instantiating for the 2nd split


    def gestate(self, θ: float, _vel: Vector2=Vector2()) -> tuple[float, float]:
        """Compute the velocity components for a child asteroid after a split.

        Starts from this asteroid's current velocity, rotates it by the given
        split angle ``θ``, then scales it by ``ASTEROID_ACCEL`` to make the
        fragment faster.

        The resulting velocity components are returned as a ``(vx, vy)`` tuple.

        Args:
            θ (float): The angle by which to rotate the parent velocity vector
                       for this child asteroid.

            _vel (Vector2): An internal reusable vector to hold the intermediate
                            velocity. This argument is intended for internal
                            reuse and should not be relied upon by callers.

        Returns:
            tuple[float, float]: The new velocity components ``(vx, vy)`` for
                                 the child asteroid.
        """
        _vel.update(self.velocity) # start same vel as destroyed asteroid
        _vel.rotate_ip(θ) # split new angle
        _vel *= ASTEROID_ACCEL # make new split asteroid faster
        return _vel.x, _vel.y


    @override
    def draw(self, screen: Surface):
        """Render the asteroid as a circle outline onto the target surface."""
        draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH
        )


    @override
    def update(self, Δ: float): # amount to move (Δ in seconds)
        """Update asteroid's position based on its velocity & elapsed time.
        Either wrap-around or kill it if it flies beyond the visible screen.
        """
        self.position += self.velocity * Δ
        self.wrap_around_or_kill(ASTEROID_WRAP_AROUND)
