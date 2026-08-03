# pyright: reportMissingTypeArgument = false

from typing import Generic, Iterator, List, Tuple, TypeVar, cast, override
from abc import ABCMeta, abstractmethod
from pygame import sprite, SurfaceType, Vector2

T = TypeVar("T", bound=sprite.Sprite)

class TypedGroup(sprite.Group, Generic[T]):
    @override
    def copy(self) -> "TypedGroup[T]": return super().copy()

    @override
    def sprites(self) -> List[T]: return cast(List[T], super().sprites())

    @override
    def __iter__(self) -> Iterator[T]:
        return cast(Iterator[T], super().__iter__())



class CircleShape(sprite.Sprite, metaclass=ABCMeta):

    containers: Tuple[TypedGroup["CircleShape"], ...] # merely declared

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
