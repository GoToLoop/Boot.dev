from main import RBTree, RBNode, C, Nil, NIL, is_nil
from collections.abc import MutableSequence

def ref_implementation(tree: RBTree[C], val: C):
    """Inserts a new comparable user value into the Red-Black Tree (BST).

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
