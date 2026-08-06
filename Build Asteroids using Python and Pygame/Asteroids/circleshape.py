from typedgroup import TypedGroup
from traittypes import Spritable

from typing import Tuple
from abc import ABCMeta

from pygame import sprite, Vector2

class CircleShape(Spritable, metaclass=ABCMeta):
    """An abstract base class for circular game entities that possess position,
    velocity, a radius and insert themselves into typed Pygame group containers.
    """
    containers: Tuple[TypedGroup["CircleShape"], ...] # declared but not created

    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"): super().__init__(*self.containers)
        else: sprite.Sprite.__init__(self)

        self.position: Vector2 = Vector2(x, y)
        self.velocity: Vector2 = Vector2()
        self.radius: float = radius


    def collides_with(self, other: "CircleShape"):
        return self.position.distance_squared_to(other.position) <= (
            self.radius + other.radius) ** 2
