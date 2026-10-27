#!/usr/bin/env -S python3 -m pytest

import pytest
from main import LinkedList
from node import Node

run_cases = (
    pytest.param(
        ["Major Marquis Warren", "John Ruth"],
        ["John Ruth", "Major Marquis Warren"]
    ),
    pytest.param(
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue"],
        ["Daisy Domergue", "John Ruth", "Major Marquis Warren"]
    )
)

submit_cases = (
    pytest.param(
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
        ["Chris Mannix", "Daisy Domergue", "John Ruth", "Major Marquis Warren"],
        marks=pytest.mark.submit
    ),
    pytest.param(
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
        ],
        [
            "Bob",
            "Chris Mannix",
            "Daisy Domergue",
            "John Ruth",
            "Major Marquis Warren"
        ],
        marks=pytest.mark.submit
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
        [
            "Oswaldo Mobray",
            "Bob",
            "Chris Mannix",
            "Daisy Domergue",
            "John Ruth",
            "Major Marquis Warren",
        ],
        marks=pytest.mark.submit
    )
)

@pytest.mark.parametrize(("inputs", "expected_state"), run_cases + submit_cases)
def test_add_to_head(inputs: list[str], expected_state: list[str]):
    print("\n---------------------------------")

    linked_list = LinkedList()
    for val in inputs: linked_list.add_to_head( Node(val) )
    result = linked_list_to_list(linked_list)

    print(f"Input:  {inputs}")
    print(f"Expect: {expected_state}")
    print(f"Actual: {result}")

    assert result == expected_state


def linked_list_to_list(linked_list: LinkedList):
    return [ node.val for node in linked_list ]
