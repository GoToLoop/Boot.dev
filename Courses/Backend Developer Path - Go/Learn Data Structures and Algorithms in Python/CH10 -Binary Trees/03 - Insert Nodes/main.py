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


    def insert(self, val: C):
        if self.val is None: self.val = val

        elif val < self.val:
            if self.left is None: self.left = BSTNode(val)
            else: self.left.insert(val)

        elif val > self.val:
            if self.right is None: self.right = BSTNode(val)
            else: self.right.insert(val)
