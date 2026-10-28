#!/usr/bin/env -S python3 -m pytest

import pytest
from collections.abc import Sequence

from main import BSTNode
from user import User, get_users

submit = pytest.mark.submit

run_cases = (
    pytest.param(5, True),
    pytest.param(3, False),
)

submit_cases = (
    pytest.param(1, True, marks=submit),
    pytest.param(21, False, marks=submit),
    pytest.param(17, True, marks=submit),
    pytest.param(7, True, marks=submit),
)

def populate_tree(nodes: Sequence[User]):
    if not nodes: return None
    tree = BSTNode(nodes[0])
    for node in nodes[1:]: tree.insert(node)
    return tree


@pytest.mark.parametrize(("val_to_check", "expected"), run_cases + submit_cases)
def test_node_exists(val_to_check: int, expected: bool):
    print("\n---------------------------------")

    tree = populate_tree(users := get_users(11))
    user_to_find = User(val_to_check)

    print("Tree nodes:")
    for user in users: print(f" * {user}")

    print(f"Searching for: {user_to_find}")
    result = tree and tree.exists(user_to_find)

    print(f"Expected: {expected}")
    print(f"Actual:   {result}")

    assert result == expected
