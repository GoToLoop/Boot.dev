from user import User
from typing import Protocol, Self, TypeVar, Generic

class SupportsComparison(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...
    def __gt__(self, other: Self, /) -> bool: ...


C = TypeVar("C", bound=SupportsComparison, default=User)

class BSTNode(Generic[C]):
    def __init__(self, val: C | None = None) -> None:
        self.left: BSTNode[C] | None = None
        self.right: BSTNode[C] | None = None
        self.val: C | None = val


    def get_min_node(self) -> "BSTNode[C]":
        node = self
        while node.left: node = node.left
        return node


    def get_min(self) -> C:
        assert ( val := self.get_min_node().val ), "Tree is empty"
        return val


    def get_max_node(self) -> "BSTNode[C]":
        node = self
        while node.right: node = node.right
        return node


    def get_max(self) -> C:
        assert ( val := self.get_max_node().val ), "Tree is empty"
        return val


    def insert(self, val: C) -> None:
        if self.val is None: self.val = val

        elif val < self.val:
            if self.left is None: self.left = BSTNode(val)
            else: self.left.insert(val)

        elif val > self.val:
            if self.right is None: self.right = BSTNode(val)
            else: self.right.insert(val)


    def delete(self, val: C) -> "BSTNode[C] | None":
        if self.val is None: return None

        if val < self.val:
            if self.left: self.left = self.left.delete(val)

        elif val > self.val:
            if self.right: self.right = self.right.delete(val)

        else: # found val in current self node
            if self.right is None: return self.left
            if self.left is None: return self.right

            self.val = self.right.get_min() # Tree has 2 nodes w/ same val!
            self.right = self.right.delete(self.val) # Get rid of 1 of them!

        return self


    def preorder(self, visited: list[C]) -> list[C]:
        if self.val is not None: visited.append(self.val)
        _ = self.left and self.left.preorder(visited)
        _ = self.right and self.right.preorder(visited)
        return visited


    def postorder(self, visited: list[C]) -> list[C]:
        _ = self.left and self.left.postorder(visited)
        _ = self.right and self.right.postorder(visited)
        if self.val is not None: visited.append(self.val)
        return visited
