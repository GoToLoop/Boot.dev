from random import choice, randint, uniform
from typing import Callable, Final, override

from typedgroup import TypedGroup
from traittypes import Updatable
from constants import *

from asteroid import Asteroid
from pygame import sprite, Vector2

Edge = tuple[Vector2, Callable[[float], Vector2]]
"""Represents a spawn boundary edge, defined by a directional vector and a
function that calculates a position along that edge given a normalized scalar.
"""

class AsteroidField(Updatable):
    """Responsible for periodically generating and spawning new asteroids 
    at random screen edges to continuously populate the game world.
    """
    container: TypedGroup[Updatable] # merely declared, not created yet

    edges: Final[ tuple[Edge, Edge, Edge, Edge] ] = (
        (
            Vector2(1, 0), # east
            lambda y: Vector2(-ASTEROID_MAX_RADIUS, SCREEN_HEIGHT * y),
        ),
        (
            Vector2(-1, 0), # west
            lambda y: Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, SCREEN_HEIGHT * y
            ),
        ),
        (
            Vector2(0, 1), # south
            lambda x: Vector2(SCREEN_WIDTH * x, -ASTEROID_MAX_RADIUS),
        ),
        (
            Vector2(0, -1), # north
            lambda x: Vector2(
                SCREEN_WIDTH * x, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ),
    )
    """Collection of the four screen boundary edges (east, west, south, north) 
    used to randomize where new asteroids enter the playfield.
    """

    def __init__(self):
        """Initialize the asteroid field and register it with its container
        group if specified."""
        if hasattr(self, "container"): super().__init__(self.container)
        else: sprite.Sprite.__init__(self)
        self.spawn_timer = 0.0


    def spawn(self, radius: float, position: Vector2, velocity: Vector2):
        """Instantiate a new asteroid with the given physical properties."""
        Asteroid(position.x, position.y, radius, velocity)


    def gestate(self):
        """Determine a random boundary edge, calculate trajectory parameters, 
        and spawn a new asteroid into the game world.
        """
        self.spawn_timer = 0
        edge = choice(self.edges)

        velocity = edge[0] * randint(40, 100)
        velocity.rotate_ip(randint(-30, 30))

        position = edge[1](uniform(0, 1))
        kind = randint(1, ASTEROID_KINDS)

        self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)


    @override
    def update(self, Δ: float):
        """Accumulate elapsed time and trigger a new asteroid spawn when the
        threshold interval is reached.
        """
        self.spawn_timer += Δ
        self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS and self.gestate()
