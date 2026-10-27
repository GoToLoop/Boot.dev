from user import User
from typing import Protocol, Self, TypeVar, Generic

class SupportsComparison(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...
    def __gt__(self, other: Self, /) -> bool: ...


C = TypeVar("C", bound=SupportsComparison, default=User)

class BSTNode(Generic[C]):
    def __init__(self, val: C | None = None):
        self.left: BSTNode[C] | None = None
        self.right: BSTNode[C] | None = None
        self.val: C | None = val


    def get_min_node(self):
        node = self
        while node.left: node = node.left
        return node


    def get_min(self):
        assert ( val := self.get_min_node().val ), "Tree is empty"
        return val


    def get_max_node(self):
        node = self
        while node.right: node = node.right
        return node


    def get_max(self):
        assert ( val := self.get_max_node().val ), "Tree is empty"
        return val


    def insert(self, val: C):
        if self.val is None: self.val = val

        elif val < self.val:
            if self.left is None: self.left = BSTNode(val)
            else: self.left.insert(val)

        elif val > self.val:
            if self.right is None: self.right = BSTNode(val)
            else: self.right.insert(val)
