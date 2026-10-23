#!/usr/bin/env -S python3 -m pytest

import pytest
from main import Node

run_cases = [
    pytest.param("Anton Chigurh", ["Llewelyn Moss", "Anton Chigurh"]),
    pytest.param(
        "Carson Wells",
        ["Llewelyn Moss", "Anton Chigurh", "Carson Wells"]
    ),
    pytest.param(
        "Ed Tom Bell",
        ["Llewelyn Moss", "Anton Chigurh", "Carson Wells", "Ed Tom Bell"],
    ),
]

submit_cases = [
    pytest.param(
        "Carla Jean Moss",
        [
            "Llewelyn Moss",
            "Anton Chigurh",
            "Carson Wells",
            "Ed Tom Bell",
            "Carla Jean Moss",
        ],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "Wendell",
        [
            "Llewelyn Moss",
            "Anton Chigurh",
            "Carson Wells",
            "Ed Tom Bell",
            "Carla Jean Moss",
            "Wendell",
        ],
        marks=pytest.mark.submit,
    ),
]

@pytest.fixture(scope="module")
def linked_list(): return Node("Llewelyn Moss")

@pytest.mark.parametrize(("input", "expected_state"), run_cases + submit_cases)
def test_set_next(linked_list: Node, input: str, expected_state: list[str]):
    print("\n---------------------------------")
    print(f"Linked List: {linked_list_to_str(linked_list)}")
    print(f"Set Next: {input}")
    print(f"Expected: {expected_state}")

    node = Node(input)
    last_node = get_last_node(linked_list)
    last_node.set_next(node)

    result = linked_list_to_list(linked_list)
    print(f"Actual: {result}")

    assert result == expected_state


def linked_list_to_list(node: Node):
    result: list[str] = []
    current = node

    while current:
        result.append(current.val)
        current = current.next

    return result


def get_last_node(node: Node):
    current = node
    while hasattr(current, "next") and current.next: current = current.next
    return current


def linked_list_to_str(node: Node):
    current = node
    linked_list_str = ""

    while current and hasattr(current, "val"):
        linked_list_str += current.val + " -> "
        current = current.next

    return linked_list_str
