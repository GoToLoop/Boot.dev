#!/usr/bin/env -S python3 -m pytest

import pytest
from typing import Literal

from main import RBTree, RBNode, Nil, is_nil
from user import get_users

# ref module is hidden because it has the solution!
from ref import ref_compare, ref_impl_left, ref_impl_right

NodeNil = RBNode | Nil
Dir = Literal["left", "right"]

run_cases = (
    pytest.param(4),
)

submit_cases = (
    pytest.param(10, marks=pytest.mark.submit),
)

@pytest.mark.parametrize(("num_users"), run_cases + submit_cases)
def test_inorder(num_users: int):
    tree = RBTree()
    ref_tree = RBTree()

    for user in get_users(num_users):
        _ = tree.insert(user)
        _ = ref_tree.insert(user)

    print("\n=====================================")
    print("Starting Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")

    assert rotate_and_compare(
        tree, tree.root, ref_tree, ref_tree.root, "left"
    )

    assert rotate_and_compare(
        tree, tree.root, ref_tree, ref_tree.root, "right"
    )

    assert rotate_and_compare(
        tree, tree.root.right, ref_tree, ref_tree.root.right, "left"
    )

    assert rotate_and_compare(
        tree, tree.root.left, ref_tree, ref_tree.root.left, "right"
    )


def rotate_and_compare(
    tree: RBTree, node: NodeNil, ref_tree: RBTree, ref_node: NodeNil, dir: Dir
):
    print(f"Rotating {dir} at {node.val}...")
    print("-------------------------------------")

    if dir == "left":
        _ = tree.rotate_left(node)
        _ = ref_impl_left(ref_tree, ref_node)
    else:
        _ = tree.rotate_right(node)
        _ = ref_impl_right(ref_tree, ref_node)

    print("Expected Tree:")
    print("-------------------------------------")
    print_tree(ref_tree)
    print("-------------------------------------")

    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")

    return ref_compare(tree.root, ref_tree.root)


def print_tree(node: RBTree):
    print('\n'.join( format_tree_string(node.root, []) ))


def format_tree_string(
    node: NodeNil, lines: list[str], level: int = 0
):
    if node and not is_nil(node) :
        format_tree_string(node.right, lines, level + 1).append(
            4 * level * ' ' + "> " + str(node.val) + ' ' + (
                node.red and "[red]" or "[black]"
            )
        )
        _ = format_tree_string(node.left, lines, level + 1)

    return lines
