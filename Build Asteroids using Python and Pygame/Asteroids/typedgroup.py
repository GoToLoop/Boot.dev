# pyright: reportMissingTypeArgument = hint
# pyright: reportIncompatibleMethodOverride = hint

from traittypes import Drawable
from typing import Generic, Iterator, List, TypeVar, cast, override

from pygame.sprite import Group, Sprite
from pygame.surface import Surface

T = TypeVar("T", bound=Sprite, contravariant=True)
"""Contravariant so a field typed as ``TypedGroup[T]`` can be assigned any
``TypedGroup[U]`` where ``U`` lies between ``Sprite`` and ``T`` in the 
inheritance chain: ``Sprite ⊇ U ⊇ T``.

For example: ``Sprite ⊇ {Updatable, Drawable} ⊇ Spritable``.
"""

class TypedGroup(Group, Generic[T]):
    """A drop-in workaround for the stricter container ``pygame.sprite.Group``.
    The latter only accepts a ``pygame.sprite.Sprite`` derivative as its generic
    type if that also implements the ``_SpriteSupportsGroup`` protocol. Meaning
    it has to provide both ``image`` + ``rect`` properties in addition to the
    vanilla ``pygame.sprite.Sprite`` base type.

    This subclass implementation overrides the ``pygame.sprite.Group``'s
    stricter ``[_TSprite]`` generic type with a more flexible contravariant
    generic type ``[T]`` (where ``T`` is a ``pygame.sprite.Sprite`` subclass).

    Because this new generic type does not require the ``_SpriteSupportsGroup``
    protocol anymore, non-fully compliant ``pygame.sprite.Sprite`` subclasses
    can be used as this container's generic type ``TypedGroup[T]``, allowing it
    to store any ``TypedGroup[U]`` where ``U`` lies between ``Sprite`` and ``T``
    in the inheritance chain: ``Sprite ⊇ U ⊇ T``.
    """
    @override
    def copy(self) -> "TypedGroup[T]": return super().copy()

    @override
    def sprites(self) -> List[T]: return cast(List[T], super().sprites())

    @override
    def draw(self, surface: Surface):
        for sprite in self.sprites():
            if isinstance(sprite, Drawable): sprite.draw(surface)


    @override
    def __iter__(self) -> Iterator[T]:
        return cast(Iterator[T], super().__iter__())


__all__ = "TypedGroup",
