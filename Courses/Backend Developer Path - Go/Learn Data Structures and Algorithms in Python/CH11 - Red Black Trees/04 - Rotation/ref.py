from main import RBTree, RBNode, C, Nil, NIL, is_nil
from collections.abc import MutableSequence

def ref_implementation(tree: RBTree[C], val: C):
    """Inserts a new comparable user value into the Red-Black Tree (RBT).

    The value is placed as a new leaf node at the correct position found 
    via standard BST traversal, extending the tree by one edge.

    Args:
        tree: The Red-Black Tree instance into which the value will be inserted.
        val: The user instance to insert into the tree.

    Returns:
        True if the insertion was successful; False if it was a duplicate.
    """
    node = RBNode(val, True) # new red user leaf node value
    node.left = node.right = NIL # its children starts off as both nil nodes
    current = tree.root # tracks down current parent node within the loop

    while not is_nil(current): # stops when reaching a nil leaf node
        if val == current.val: return False # cancels insertion: duplicate!
        node.parent = current # saves last non-nil current node as parent
        current = val < current.val and current.left or current.right

    if (parent := node.parent) is None: tree.root = node # new node is 1st node
    elif val < parent.val: parent.left = node # attaches new node as left child
    else: parent.right = node # attaches new node as right child via its parent

    return True # new leaf node value insertion successful


def ref_inorder(node: RBNode[C] | Nil, acc: MutableSequence[C]):
    """Performs an in-order traversal of the tree, populating the accumulator
    list with the binary-sorted comparable user values.

    Args:
        node: Current node being visited during the traversal.
        acc: Accumulator list used to collect the user objects in sorted order.

    Returns:
        The populated accumulator list containing the traversed sorted users.
    """
    if is_nil(node): return acc # no value found; end of the BST traversal
    _ = is_nil(node.left) or ref_inorder(node.left, acc) # collect smaller 1st
    acc.append(node.val) # middle value after left side but before right side
    _ = is_nil(node.right) or ref_inorder(node.right, acc) # get bigger last
    return acc # all values collected in ascendant order


def ref_compare(a: RBNode[C] | Nil, b: RBNode[C] | Nil) -> bool:
    """Recursively compares 2 nodes/subtrees for structural and value equality.

    Args:
        a: The first node to compare.
        b: The second node to compare.

    Returns:
        True if both nodes/subtrees are identical in structure, value, and
        color; False otherwise.
    """
    a_nil = is_nil(a)
    b_nil = is_nil(b)

    if a_nil and b_nil: return True
    if a_nil or  b_nil: return False

    return (
        a.val == b.val and a.red is b.red
        and ref_compare(a.left, b.left)
        and ref_compare(a.right, b.right)
    )


def ref_impl_left(tree: RBTree[C], pivot_parent: RBNode[C] | Nil):
    """Performs a left rotation on the Red-Black Tree around pivot_parent.

    Args:
        tree: The Red-Black Tree instance containing the nodes.
        pivot_parent: The node acting as the parent pivot for the left rotation.

    Returns:
        True if the rotation was successful; False if the pivot or its right
        child is Nil.
    """
    if is_nil(pivot_parent) or is_nil(pivot := pivot_parent.right): return False

    pivot_parent.right = pivot.left
    if not is_nil(pivot.left): pivot.left.parent = pivot_parent
    pivot.parent = pivot_parent.parent

    if pivot_parent.parent is None: # its parent is the root node
        tree.root = pivot # so replace it with the pivot node
    elif pivot_parent is pivot_parent.parent.left:
        pivot_parent.parent.left = pivot
    else:
        pivot_parent.parent.right = pivot

    pivot.left = pivot_parent
    pivot_parent.parent = pivot

    return True


def ref_impl_right(tree: RBTree[C], pivot_parent: RBNode[C] | Nil):
    """Performs a right rotation on the Red-Black Tree around pivot_parent.

    Args:
        tree: The Red-Black Tree instance containing the nodes.
        pivot_parent: The node acting as parent pivot for the right rotation.

    Returns:
        True if the rotation was successful; False if the pivot or its left
        child is Nil.
    """
    if is_nil(pivot_parent) or is_nil(pivot := pivot_parent.left): return False

    pivot_parent.left = pivot.right
    if not is_nil(pivot.right): pivot.right.parent = pivot_parent
    pivot.parent = pivot_parent.parent

    if pivot_parent.parent is None: # its parent is the root node
        tree.root = pivot # so replace it with the pivot node
    elif pivot_parent is pivot_parent.parent.right:
        pivot_parent.parent.right = pivot
    else:
        pivot_parent.parent.left = pivot

    pivot.right = pivot_parent
    pivot_parent.parent = pivot

    return True
