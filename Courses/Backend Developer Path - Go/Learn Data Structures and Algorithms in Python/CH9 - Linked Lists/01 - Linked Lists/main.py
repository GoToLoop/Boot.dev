# pyright: reportDeprecated = hint

from typing import override, Optional

class Node[T=str]:
    val: T; next: Optional["Node"]

    def __init__(self, val: T) -> None: self.val = val; self.next = None

    def set_next(self, node: "Node") -> None: self.next = node

    @override
    def __repr__(self) -> str: return str(self.val)
