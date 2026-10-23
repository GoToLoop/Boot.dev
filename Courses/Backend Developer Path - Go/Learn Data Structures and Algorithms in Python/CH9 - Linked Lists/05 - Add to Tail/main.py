from node import Node
from typing import override

class LinkedList[T=str]:
    def add_to_tail(self, node: "Node[T]"):
        if not (current := self.head): self.head = node

        else:
            for current in self: pass
            current.set_next(node)


    def __init__(self): self.head: "Node[T] | None" = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next


    @override
    def __repr__(self): return " -> ".join( str(node.val) for node in self )
