from user import User
from typing import Final, Generic, Literal, Protocol, Self, TypeIs, TypeVar

class SupportsComparison(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...
    def __gt__(self, other: Self, /) -> bool: ...


C = TypeVar("C", bound=SupportsComparison, default=User)

class RBNode(Generic[C]):
    def __init__(self, val: C, red: bool = False) -> None:
        self.val: C = val
        self.red: bool = red

        self.parent: RBNode[C] | None = None

        self.left: RBNode[C] | Nil = self
        self.right: RBNode[C] | Nil = self


Nil = RBNode[Literal[False]]
NIL: Nil = RBNode(False)

def is_nil(node: RBNode[C] | Nil) -> TypeIs[Nil]: return node is NIL

class RBTree(Generic[C]):
    nil: Final = NIL

    def __init__(self, root: RBNode[C] | Nil = NIL) -> None:
        self.root: RBNode[C] | Nil = root


    def rotate_left(self, pivot_parent: RBNode[C] | Nil) -> bool:
        if is_nil(pivot_parent) or is_nil(pivot := pivot_parent.right):
            return False

        pivot_parent.right = pivot.left
        if not is_nil(pivot.left): pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent

        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent is pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot

        pivot.left = pivot_parent
        pivot_parent.parent = pivot

        return True


    def rotate_right(self, pivot_parent: RBNode[C] | Nil) -> bool:
        if is_nil(pivot_parent) or is_nil(pivot := pivot_parent.left):
            return False

        pivot_parent.left = pivot.right
        if not is_nil(pivot.right): pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent

        if pivot_parent.parent is None: self.root = pivot
        elif pivot_parent is pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot


        pivot.right = pivot_parent
        pivot_parent.parent = pivot

        return True


    def insert(self, val: C) -> bool:
        new_node = RBNode(val, True)
        new_node.left = new_node.right = NIL

        current = self.root
        parent = None

        while not is_nil(current):
            if val == current.val: return False
            parent = current
            current = val < current.val and current.left or current.right

        if parent is None: self.root = new_node
        elif val < parent.val: parent.left = new_node
        else: parent.right = new_node

        new_node.parent = parent
        return True
