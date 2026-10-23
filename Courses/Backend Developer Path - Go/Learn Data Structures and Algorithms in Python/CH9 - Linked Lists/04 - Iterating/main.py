# pyright: reportExplicitAny = hint

from node import Node
from typing import Any, override

class LinkedList:
    head: "Node[Any] | None"

    def __init__(self): self.head = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next


    @override
    def __repr__(self):
        return " -> ".join( str(node.val) for node in self )
