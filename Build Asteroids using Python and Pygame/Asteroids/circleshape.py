from typedgroup import TypedGroup
from traittypes import Spritable
from typehints import Cardinal
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

from typing import Callable, Final, Self, Tuple
from abc import ABCMeta
from pygame import Vector2

Edge = Callable[ ["CircleShape"], bool ]

class CircleShape(Spritable, metaclass=ABCMeta):
    """An abstract base class for circular game entities that possess position,
    velocity, a radius and insert themselves into typed Pygame group containers.
    """
    containers: Tuple[TypedGroup[Self], ...] # declared but not created yet

    EDGES: Final[ Tuple[Edge, Edge, Edge, Edge] ] = (
        lambda c: c.position.x < -c.radius*2,               # WEST
        lambda c: c.position.x > SCREEN_WIDTH + c.radius*2, # EAST
        lambda c: c.position.y < -c.radius*2,               # NORTH
        lambda c: c.position.y > SCREEN_HEIGHT + c.radius*2 # SOUTH
    )

    def __init__(self, x: float, y: float, radius: float):
        """Initialize a new circular sprite with position and radius.

        Registers the instance in its declared ``containers`` (if any), or
        falls back to a bare ``Spritable`` initialization when no containers
        are defined. Sets initial position, zero velocity, and the given radius.

        Args:
            x (float): Initial x-coordinate for the circle's center.
            y (float): Initial y-coordinate for the circle's center.
            radius (float): Radius of the circle.
        """
        if hasattr(self, "containers"): super().__init__(*self.containers)
        else: Spritable.__init__(self)

        self.position: Vector2 = Vector2(x, y)
        self.velocity: Vector2 = Vector2()
        self.radius: float = abs(radius)


    def init(self,
        x: float, y: float,
        radius: float=0.0,
        vx: float=0.0, vy: float=0.0
    ) -> Self:
        """Reinitialize this circular sprite with new position and radius.
        Defaults to keeping old radius if not given a new one.

        Args:
            x (float): New x-coordinate for the circle's center.
            y (float): New y-coordinate for the circle's center.
            radius (float): New optional radius of the circle.
            vx (float): New x-component of the velocity vector.
            vy (float): New y-component of the velocity vector.

        Returns:
            Self: The re-initialized instance itself, allowing chained calls.
        """
        self.position.update(x, y)
        self.velocity.update(vx, vy)
        if radius: self.radius = abs(radius)

        return self


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


    def check_outside(self) -> Cardinal:
        """Determine whether this circle has crossed the canvas boundary.

        Returns:
            Cardinal: One of the following enum values (0-4):

            - Cardinal.INSIDE → circle is still within the visible screen (0)
            - Cardinal.WEST   → circle fully crossed the west edge        (1)
            - Cardinal.EAST   → circle fully crossed the east edge        (2)
            - Cardinal.NORTH  → circle fully crossed the north edge       (3)
            - Cardinal.SOUTH  → circle fully crossed the south edge       (4)
        """
        for idx, edge_check in enumerate(CircleShape.EDGES, 1):
            if edge_check(self): return Cardinal(idx)
        return Cardinal.INSIDE


    def teleport(self, edge_index: Cardinal):
        """Teleport this circle shape to the opposite side of the canvas."""
        match edge_index:
            case Cardinal.INSIDE: # still inside visible screen
                pass
            case Cardinal.WEST:   # west → move to east
                self.position.x = SCREEN_WIDTH + self.radius
            case Cardinal.EAST:   # east → move to west
                self.position.x = -self.radius
            case Cardinal.NORTH:  # north → move to south
                self.position.y = SCREEN_HEIGHT + self.radius
            case Cardinal.SOUTH:  # south → move to north
                self.position.y = -self.radius
