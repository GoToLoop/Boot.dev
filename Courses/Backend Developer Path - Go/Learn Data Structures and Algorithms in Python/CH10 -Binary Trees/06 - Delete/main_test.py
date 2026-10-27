#!/usr/bin/env -S python3 -m pytest

import pytest
from random import shuffle

from main import BSTNode
from user import User, get_users

# ref module is hidden because it has the solution!
from ref import ref_inorder

run_cases = (
    pytest.param(6, 2, [User(0), User(9), User(16), User(17)]),

    pytest.param(12, 4, [
        User(2), User(10), User(11), User(17), User(22), User(27),
        User(30), User(33),
    ]),
)

submit_cases = (
    pytest.param(24, 6, [
        User(2), User(3), User(9), User(10), User(12), User(16), User(18),
        User(19), User(22), User(23), User(35), User(39), User(45), User(51),
        User(54), User(68), User(69), User(70),
    ], marks=pytest.mark.submit),
)

@pytest.mark.parametrize(
    ("num_users", "num_to_delete", "expected"), run_cases + submit_cases
)
def test_insert_nodes(num_users: int, num_to_delete: int, expected: list[User]):
    users_copy = list(users := get_users(num_users))
    shuffle(users_copy)
    users_to_delete = users_copy[:num_to_delete]

    bst = BSTNode()
    for user in users: bst.insert(user)

    print("\n=====================================")
    print("Tree:")
    print_tree(bst)
    print("-------------------------------------\n")

    actual_bst = BSTNode()
    for user in users: actual_bst.insert(user)

    print("Deleting users: " + str(users_to_delete))
    for user in users_to_delete:
        if ( actual_bst := actual_bst.delete(user) ) is None: break

    print("Actual Tree:")
    print_tree(actual_bst)
    print("-------------------------------------")

    actual: list[User] = []
    _ = actual_bst and ref_inorder(actual_bst, actual)

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")

    assert expected == actual


def print_tree(bst_node: BSTNode | None):
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
