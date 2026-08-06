from random import choice, randint, uniform
from typing import Callable, Final, Tuple, override

from typedgroup import TypedGroup
from traittypes import Updatable

from asteroid import Asteroid
from pygame import sprite, Vector2

from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED, ASTEROID_DRIFT_ANGLE,
    ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS
)

Edge = Tuple[Tuple[int, int], Callable[ [float], Tuple[float, float] ]]
"""Represents a spawn boundary edge, defined by a directional normalized vector
which moves opposite to the spawning site and a function that calculates a
spawning position along that edge given a normalized scalar.
"""

class AsteroidField(Updatable):
    """Responsible for periodically generating and spawning new asteroids 
    at random screen edges to continuously populate the game world.
    """
    container: TypedGroup[Updatable] # merely declared, not created yet

    EDGES: Final[ Tuple[Edge, Edge, Edge, Edge] ] = (
        (
            (1, 0), # moves east (RIGHT) and spawns at the west boundary edge
            lambda y: (-ASTEROID_MAX_RADIUS, SCREEN_HEIGHT * y),
        ),
        (
            (-1, 0), # moves west (LEFT) and spawns at the east boundary edge
            lambda y: (SCREEN_WIDTH + ASTEROID_MAX_RADIUS, SCREEN_HEIGHT * y),
        ),
        (
            (0, 1), # moves south (DOWN) and spawns at the north boundary edge
            lambda x: (SCREEN_WIDTH * x, -ASTEROID_MAX_RADIUS),
        ),
        (
            (0, -1), # moves north (UP) and spawns at the south boundary edge
            lambda x: (SCREEN_WIDTH * x, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS),
        ),
    )
    """Collection of the four screen boundary edges (east, west, south, north) 
    used to randomize where new asteroids spawn *just outside* the visible 
    viewport, ensuring smooth entry into the playfield.
    """

    def __init__(self):
        """Initialize the asteroid field and register it with its container
        group if specified."""
        if hasattr(self, "container"): super().__init__(self.container)
        else: sprite.Sprite.__init__(self)

        self.spawn_timer: float = 0.0 # start asteroid spawn time counter
        """Elapsed time counter in seconds for next asteroid spawn."""


    def spawn(self, rad: float, px: float, py: float, vx: float, vy: float):
        """Instantiate a new asteroid with the given physical properties."""
        Asteroid(px, py, rad, vx, vy) # auto-inserts itself in pygame groups


    def gestate(self):
        """Determine a random boundary edge, calculate trajectory parameters, 
        and spawn a new asteroid into the game world.
        """
        self.spawn_timer = 0.0 # reset counter for next spawn
        edge = choice(AsteroidField.EDGES) # random spawning edge
    
        vel = Vector2(edge[0]) # opposite moving direction to the spawning edge
        vel *= randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
        vel.rotate_ip(randint(-ASTEROID_DRIFT_ANGLE, ASTEROID_DRIFT_ANGLE))

        pos = edge[1](uniform(0, 1)) # random position along edge’s varying axis
        kind = randint(1, ASTEROID_KINDS) # random starting size multiplier

        self.spawn(kind * ASTEROID_MIN_RADIUS, *pos, *vel)


    @override
    def update(self, Δ: float): # frame's transpired time (Δ in seconds)
        """Accumulate elapsed time and trigger a new asteroid spawn when the
        threshold interval is reached.
        """
        self.spawn_timer += Δ
        self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS and self.gestate()
