from typing import Tuple, override
from abc import ABCMeta, abstractmethod
from pygame import sprite, Vector2, SurfaceType

class CircleShape(sprite.Sprite, metaclass=ABCMeta):

    containers: Tuple[sprite.Group, ...] # declared, but not created yet

    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"): super().__init__(*self.containers)
        else: super().__init__()

        self.position: Vector2 = Vector2(x, y)
        self.velocity: Vector2 = Vector2()
        self.radius: float = radius


    @abstractmethod
    def draw(self, screen: SurfaceType): ...

    @abstractmethod
    @override
    def update(self, Δ: float): ...
