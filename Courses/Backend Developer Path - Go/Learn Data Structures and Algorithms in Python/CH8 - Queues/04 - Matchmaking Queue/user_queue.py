# pyright: reportDeprecated = hint

from typing import Iterator, Optional, final, override

@final
class Queue[T=str]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.insert(0, item)

    enqueue = push

    def pop(self) -> Optional[T]:
        return self.items.pop() if self.items else None

    dequeue = pop

    def peek(self) -> Optional[T]:
        return self.items[-1] if self.items else None

    def size(self) -> int:
        return len(self.items)

    def clear(self) -> None:
        self.items.clear()

    def iter(self) -> Iterator[T]:
        return iter(self.items)

    def search_and_remove(self, item: T) -> Optional[T] :
        try: self.items.remove(item) 
        except ValueError: return None
        return item

    @override
    def __repr__(self) -> str:
        return f"[{', '.join(map(str, self.items))}]"
