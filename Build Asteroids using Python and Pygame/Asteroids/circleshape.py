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


    def collides_with(self, other: "CircleShape") -> bool:
        """Checks if this shape collides with another circular shape.

        Calculates the squared Euclidean distance between the centers of both
        circles and compares it to the squared sum of their radii for an
        optimized collision check (avoiding expensive square root operations).

        Args:
            other (CircleShape): The other circular shape to check against.

        Returns:
            bool: True if the two circles overlap or touch, False otherwise.
        """
        return self.position.distance_squared_to(other.position) <= (
            self.radius + other.radius) ** 2
