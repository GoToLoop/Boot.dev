#!/usr/bin/env -S python3 -m pytest

import pytest
from main import BSTNode
from user import User, get_users

run_cases = (
    pytest.param(4, [User(7), User(0), User(11), User(8)]),
    pytest.param(6, [User(10), User(5), User(0), User(9), User(16), User(17)]),
)

submit_cases = (
    pytest.param(12, [
        User(34), User(22), User(2), User(19), User(17), User(10), User(11),
        User(18), User(30), User(27), User(23), User(33)
    ], marks=pytest.mark.submit),

    pytest.param(0, [], marks=pytest.mark.submit),
)

@pytest.mark.parametrize(("num_characters", "expected"), run_cases+submit_cases)
def test_preorder(num_characters: int, expected: list[User]):
    characters = get_users(num_characters)
    bst = BSTNode()
    for character in characters: bst.insert(character)

    print("\n=====================================")
    print("Tree:")
    print("-------------------------------------")
    print(print_tree(bst))
    print("-------------------------------------\n")
    print(f"Expected: {expected}")

    actual = bst.preorder([])
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
