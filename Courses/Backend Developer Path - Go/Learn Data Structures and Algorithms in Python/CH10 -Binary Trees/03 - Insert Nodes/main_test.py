#!/usr/bin/env -S python3 -m pytest

import pytest
from main import BSTNode

# ref module is hidden because it has the solution!
from ref import ref_implementation, ref_inorder
from user import get_users

run_cases = (
    pytest.param(3),
    pytest.param(5),
)

submit_cases = (
    pytest.param(10, marks=pytest.mark.submit),
)

@pytest.mark.parametrize("num_users", run_cases + submit_cases)
def test_insert_nodes(num_users: int):
    expected_bst = BSTNode()

    for user in ( users := get_users(num_users) ):
        ref_implementation(expected_bst, user)

    print("\n=====================================")
    print("Expecting Tree:")
    print("-------------------------------------")
    print_tree(expected_bst)
    print("-------------------------------------\n")

    actual_bst = BSTNode()

    for user in users:
        print("Inserting", user, "into tree...")
        actual_bst.insert(user)

    print("\n")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_bst)
    print("-------------------------------------")

    assert ref_inorder(actual_bst, []) == ref_inorder(expected_bst, [])


def print_tree(bst_node: BSTNode):
    print('\n'.join( format_tree_string(bst_node, []) ))


def format_tree_string(
    bst_node: BSTNode | None, lines: list[str], level: int = 0
):
    if bst_node:
        format_tree_string(bst_node.right, lines, level + 1).append(
            4 * level * ' ' + "> " + str(bst_node.val)
        )
        _ = format_tree_string(bst_node.left, lines, level + 1)

    return lines
