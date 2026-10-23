# pyright: reportExplicitAny = hint
# pyright: reportAny = hint

from typing import Any

class Stack:
    def __init__(self) -> None: self.items: list[Any] = []
    def push(self, item: Any) -> None: self.items.append(item)
    def size(self) -> int: return len(self.items)
