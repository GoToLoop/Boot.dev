#!/usr/bin/env -S python3 -m pytest

import pytest
from main import BSTNode
from user import get_users

submit = pytest.mark.submit

run_cases = (
    pytest.param(2, 2),
    pytest.param(6, 3),
)

submit_cases = (
    pytest.param(0, 0, marks=submit),
    pytest.param(1, 1, marks=submit),
    pytest.param(16, 7, marks=submit),
)

@pytest.mark.parametrize(("num_users", "expected"), run_cases + submit_cases)
def test_inorder(num_users: int, expected: int):
    if users := get_users(num_users):
        root = BSTNode(users[0])
        for user in users[1:]: root.insert(user)
    else: root = BSTNode()

    print("\n---------------------------------")
    print(f"Users: {[*map(str, users)]}\n")
    print_tree(root)

    print("\nExpecting height:", expected)
    result = root.height()
    print("Actual height:", result)

    assert result == expected


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
