#!/usr/bin/env -S python3 -m pytest

import pytest
from main import LinkedList
from node import Node

run_cases = (
    pytest.param("John Ruth", ["Major Marquis Warren", "John Ruth"]),
    pytest.param(
        "Daisy Domergue",
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue"]
    ),
    pytest.param(
        "Chris Mannix",
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"]
    )
)

submit_cases = (
    pytest.param(
        "Bob",
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
        ],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "Oswaldo Mobray",
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
        marks=pytest.mark.submit,
    )
)

@pytest.fixture(scope="module")
def linked_list():
    linked_list = LinkedList()
    linked_list.head = Node("Major Marquis Warren")
    return linked_list


@pytest.mark.parametrize(("input", "expected_state"), run_cases + submit_cases)
def test_iteration(
    linked_list: LinkedList, input: str, expected_state: list[str]
):
    print("\n---------------------------------")
    print(f"Linked List: {linked_list}")
    print(f"Set Next: {input}")
    print(f"Expected: {expected_state}")

    node = Node(input)
    last_node = get_last_node(linked_list)
    last_node.set_next(node)

    result = linked_list_to_list(linked_list)

    print(f"Actual: {result}")
    assert result == expected_state


def linked_list_to_list(linked_list: LinkedList):
    return [ node.val for node in linked_list ]


def get_last_node(linked_list: LinkedList):
    if not (current := linked_list.head): raise RuntimeError("Head is invalid!")
    while hasattr(current, "next") and current.next: current = current.next
    return current
