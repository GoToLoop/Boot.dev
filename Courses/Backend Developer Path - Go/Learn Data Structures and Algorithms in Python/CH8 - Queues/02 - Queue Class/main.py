# pyright: reportExplicitAny = hint
# pyright: reportAny = hint

from typing import Any

class Queue:
    def __init__(self) -> None: self.items: list[Any] = []
    def push(self, item: Any) -> None: self.items.insert(0, item)
    def pop(self) -> Any: return self.items.pop() if self.items else None
    def peek(self) -> Any: return self.items[-1] if self.items else None
    def size(self) -> int: return len(self.items)
