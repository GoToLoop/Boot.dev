# pyright: reportMissingTypeArgument = hint

from typing import Generic, Iterator, List, TypeVar, cast, override
from pygame.sprite import Group, Sprite

T = TypeVar("T", bound=Sprite, contravariant=True)

class TypedGroup(Group, Generic[T]):
    """A strongly-typed wrapper around pygame.sprite.Group which enforces type
    safety for its member sprites using a generic contravariant type parameter.
    """
    @override
    def copy(self) -> "TypedGroup[T]": return super().copy()

    @override
    def sprites(self) -> List[T]: return cast(List[T], super().sprites())

    @override
    def __iter__(self) -> Iterator[T]:
        return cast(Iterator[T], super().__iter__())


__all__ = "TypedGroup",
