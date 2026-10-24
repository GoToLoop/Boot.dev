from typing import Any, override

class Node[T=Any]:
    val: T; next: "Node | None"

    def __init__(self, val: T): self.val = val; self.next = None

    def set_next(self, node: "Node[T] | None"): self.next = node

    @override
    def __repr__(self): return str(self.val)
