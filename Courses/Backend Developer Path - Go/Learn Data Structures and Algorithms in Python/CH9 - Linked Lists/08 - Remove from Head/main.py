# pyright: reportUnannotatedClassAttribute = hint
# ruff: noqa: E701, E702

from node import Node
from typing import override

class LLQueue[T=str]:
    def remove_from_head(self):
        if not (killed_head := self.head): return None

        self.head = self.head.next
        if not self.head: self.tail = None

        self.size -= 1

        killed_head.set_next(None)
        return killed_head


    dequeue = remove_from_head

    def _add_to_head(self, node: "Node[T]"):
        node.set_next(self.head)
        if not self.head: self.tail = node
        self.head = node
        self.size += 1


    def add_to_tail(self, node: "Node[T]"):
        if not (self.head and self.tail): self.head = self.tail = node
        else: self.tail.set_next(node); self.tail = node
        self.size += 1


    enqueue = add_to_tail

    def _remove_from_tail(self):
        if not ((current := self.head) and self.tail): return None
        if current is (killed_tail := self.tail): return self.remove_from_head()

        while current.next and current.next is not self.tail:
            current = current.next

        self.tail = current
        current.set_next(None)

        self.size -= 1
        return killed_tail


    def clear(self):
        current = self.head
        while current: current.next, current = None, current.next
        self.head = self.tail = None
        self.size = 0


    head: "Node[T] | None"
    tail: "Node[T] | None"
    size: int

    def __init__(self):
        self.head = self.tail = None
        self.size = 0


    def __len__(self): return self.size

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next


    def __contains__(self, item: object):
        return any( node.val == item for node in self )


    @override
    def __repr__(self): return " -> ".join( str(node.val) for node in self )
