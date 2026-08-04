from abc import ABCMeta, abstractmethod
from typing import override
from pygame import SurfaceType, sprite

class Updatable(sprite.Sprite, metaclass=ABCMeta):
    """Abstract class for objects that need to be updated each frame/tick."""

    @abstractmethod
    @override
    def update(self, Δ: float) -> None:
        """Update the object's state. ``Δ`` represents delta time in seconds."""
        pass


class Drawable(sprite.Sprite, metaclass=ABCMeta):
    """Abstract class for objects that can be rendered to a screen surface."""

    @abstractmethod
    def draw(self, screen: SurfaceType) -> None:
        """Draw the object onto the given screen surface."""
        pass


class Spritable(Updatable, Drawable, metaclass=ABCMeta):
    """Abstract class for objects that can be both updated & rendered."""
    pass
