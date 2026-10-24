from node import Node
from typing import override

class LinkedList[T=str]:
    def add_to_head(self, node: "Node[T]"):
        node.set_next(self.head)
        if not self.head: self.tail = node
        self.head = node


    def add_to_tail(self, node: "Node[T]"):
        if not (self.head and self.tail): self.head = self.tail = node
        else: self.tail.set_next(node); self.tail = node


    head: "Node[T] | None"; tail: "Node[T] | None"

    def __init__(self): self.head = self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next


    @override
    def __repr__(self): return " -> ".join( str(node.val) for node in self )
