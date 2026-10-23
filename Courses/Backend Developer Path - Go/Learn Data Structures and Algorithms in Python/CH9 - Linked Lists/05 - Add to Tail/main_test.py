#!/usr/bin/env -S python3 -m pytest

# pyright: reportAny = hint

import pytest
from main import LinkedList
from node import Node

run_cases = [
    pytest.param(["Major Marquis Warren", "John Ruth"]),
    pytest.param(["Major Marquis Warren", "John Ruth", "Daisy Domergue"]),
]

submit_cases = [
    pytest.param(
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
        marks=pytest.mark.submit,
    ),
    pytest.param(
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
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize("inputs", run_cases + submit_cases)
def test_add_to_tail(inputs: list[str]):
    print("\n---------------------------------")

    linked_list = LinkedList()
    for val in inputs: linked_list.add_to_tail( Node(val) )
    actual = linked_list_to_list(linked_list)

    print(f"Expected: {inputs}")
    print(f"Actual  : {actual}")
    assert actual == inputs


def linked_list_to_list(linked_list: LinkedList):
    return [node.val for node in linked_list]
