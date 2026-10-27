#!/usr/bin/env -S python3 -m pytest

import pytest
from main import LLQueue
from node import Node

submit = pytest.mark.submit

run_cases = (
    pytest.param(
        ["Rick", "Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        "Rick",
        "Squeaky"
    ),
    pytest.param(
        ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        ["Sharon", "Jay", "Roman", "Squeaky"],
        "Cliff",
        "Squeaky"
    )
)

submit_cases = (
    pytest.param([], [], None, None, marks=submit),
    pytest.param(["Jay"], [], "Jay", None, marks=submit),
    pytest.param(
        ["Roman", "Squeaky"], ["Squeaky"], "Roman", "Squeaky", marks=submit
    ),
    pytest.param(["Squeaky"], [], "Squeaky", None, marks=submit)
)

@pytest.mark.parametrize(
    ("items", "expected_state", "expected_head", "expected_tail"),
    run_cases + submit_cases
)
def test_remove_from_head(
    items: list[str], expected_state: list[str],
    expected_head: str | None, expected_tail: str | None
):
    linked_list = LLQueue()
    for item in items:
        linked_list.add_to_tail( Node(item) )

    print("\n---------------------------------")
    print(f"Linked List Queue: {linked_list}")
    print("Removing Head...\n")

    head = linked_list.remove_from_head()
    tail = linked_list.tail
    result = linked_list_to_list(linked_list)

    print(f"Expected List: {expected_state}")
    print(f"  Actual List: {result}\n")
    assert result == expected_state

    print(f"Expected Removed Head: {expected_head}")
    print(f"  Actual Removed Head: {head}\n")

    if expected_head is None:
        assert head is None
    else:
        assert head is not None
        assert head.val == expected_head

    print(f"Expected Tail: {expected_tail}")
    print(f"  Actual Tail: {tail}\n")

    if expected_tail is None:
        assert tail is None
    else:
        assert tail is not None
        assert tail.val == expected_tail

    if head:
        print("Expected Removed Head's Next Node: None")
        print(f"         Actual Removed Head Next: {head.next}\n")
        assert head.next is None


def linked_list_to_list(linked_list: LLQueue):
    return [ node.val for node in linked_list ]
