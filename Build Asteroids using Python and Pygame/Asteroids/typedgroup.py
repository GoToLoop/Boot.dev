# pyright: reportMissingTypeArgument = hint

from typing import Generic, Iterator, List, TypeVar, cast, override
from pygame.sprite import Group, Sprite

T = TypeVar("T", bound=Sprite, contravariant=True)
"""Contravariant so a field typed as ``TypedGroup[T]`` can be assigned any
``TypedGroup[U]`` where ``U`` lies between ``Sprite`` and ``T`` in the 
inheritance chain: ``Sprite ⊇ U ⊇ T``.

For example: ``Sprite ⊇ {Updatable, Drawable} ⊇ Spritable``.
"""

class TypedGroup(Group, Generic[T]):
    """A strongly-typed wrapper around ``pygame.sprite.Group`` which enforces
    type safety for its member sprites via a contravariant type parameter.

    This is a workaround for ``pygame.sprite.Group`` being untyped: since it 
    expects objects to match the ``_SpriteSupportsGroup`` protocol (i.e. having 
    ``image`` + ``rect`` attributes), so now it accepts any ``Sprite`` subclass 
    at runtime. ``TypedGroup`` adds static type checking by treating the group 
    as containing only sprites of type ``T`` (where ``T`` is a ``Sprite`` 
    subclass). Type safety is enforced by the type checker, not at runtime; 
    where invoking ``TypedGroup::draw()`` on an incompatible or incomplete 
    sprite can crash the game.
    """
    @override
    def copy(self) -> "TypedGroup[T]": return super().copy()

    @override
    def sprites(self) -> List[T]: return cast(List[T], super().sprites())

    @override
    def __iter__(self) -> Iterator[T]:
        return cast(Iterator[T], super().__iter__())


__all__ = "TypedGroup",
