#!/usr/bin/env -S python3 -m pytest

import pytest
from main import RBTree, RBNode, Nil, is_nil
from user import get_users

# ref module is hidden because it has the solution!
from ref import ref_implementation, ref_inorder

run_cases = (
    pytest.param(4),
    pytest.param(8),
)

submit_cases = (
    pytest.param(10, marks=pytest.mark.submit),
)

@pytest.mark.parametrize(("num_users"), run_cases + submit_cases)
def test_inorder(num_users: int):
    ref_tree = RBTree()
    for user in ( users := get_users(num_users) ):
        _ = ref_implementation(ref_tree, user)

    print("\n============ NEW TEST ===============")
    actual_tree = RBTree()
    for user in users:
        print(f"Inserting {user} into tree...")
        _ = actual_tree.insert(user)

    print("-------------------------------------")
    print("Expecting Tree:")
    print("-------------------------------------")
    print_tree(ref_tree)

    print("-------------------------------------")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_tree)
    print("-------------------------------------")

    assert ref_inorder(actual_tree.root, []) == ref_inorder(ref_tree.root, [])


def print_tree(node: RBTree | None):
    print('\n'.join( format_tree_string(node and node.root, []) ))


def format_tree_string(
    node: RBNode | Nil | None, lines: list[str], level: int = 0
):
    if node and not is_nil(node) :
        format_tree_string(node.right, lines, level + 1).append(
            4 * level * ' ' + "> " + str(node.val) + ' ' + (
                node.red and "[red]" or "[black]"
            )
        )
        _ = format_tree_string(node.left, lines, level + 1)

    return lines
