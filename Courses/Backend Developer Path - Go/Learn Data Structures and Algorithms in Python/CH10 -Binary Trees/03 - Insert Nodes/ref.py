from main import BSTNode, C
from collections.abc import MutableSequence

def ref_implementation(node: BSTNode[C], val: C):
    """Mock implementation for inserting a comparable user value into the BST.

    Args:
        node: Current node in the Binary Search Tree (BST) being evaluated.
        val: Comparable user object that needs to be inserted into the BST.
    """
    if node.val is None: node.val = val

    elif val < node.val:
        if node.left is None: node.left = BSTNode(val)
        else: ref_implementation(node.left, val)

    elif val > node.val:
        if node.right is None: node.right = BSTNode(val)
        else: ref_implementation(node.right, val)


def ref_inorder(node: BSTNode[C], acc: MutableSequence[C]):
    """Mock implementation for an "in-order" traversal, populating the
    accumulator list with the binary-sorted user values.

    Args:
        node: Current node being visited during the traversal.
        acc: Accumulator list used to collect the user objects in sorted order.

    Returns: Populated accumulator list containing the traversed sorted users.
    """
    if node.val is None: return acc # no value found; end of the BST traversal
    _ = node.left and ref_inorder(node.left, acc) # collect smaller values 1st
    acc.append(node.val) # middle value after left side but before right side
    _ = node.right and ref_inorder(node.right, acc) # get bigger values last
    return acc # all values collected in ascendant order
