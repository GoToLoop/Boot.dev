#!/usr/bin/env -S python3 -m pytest

from random import choice, seed
from time import time

import pytest
from main import LinkedList
from node import Node

run_cases = (
    pytest.param(10, "Patrick Bateman", "Paul Allen"),
    pytest.param(100, "Paul Allen", "Paul Allen"),
    pytest.param(1000, "Paul Allen", "Paul Allen"),
    pytest.param(10000, "Patrick Bateman", "Paul Allen")
)

submit_cases = (
    pytest.param(12000, "Paul Allen", "Paul Allen", marks=pytest.mark.submit),
)

MILLIS = 1500
TIMEOUT = MILLIS / 1000

@pytest.mark.parametrize(
    ("num_items", "first_item", "last_item"), run_cases + submit_cases
)
def test_linked_list_queue(num_items: int, first_item: str, last_item: str):
    print("\n---------------------------------")
    print(f"Adding {num_items} job candidates to a linked list's head")

    linked_list = LinkedList()
    linked_list2 = LinkedList()

    try:
        start = time()
        for item in get_items(num_items):
            linked_list.add_to_head( Node(item) )

        print(f"Adding {num_items} job candidates to a linked list's tail")
        for item in get_items(num_items):
            linked_list2.add_to_tail( Node(item) )
        end = time()

        print("Expecting to complete in less than", MILLIS, "milliseconds")
        assert (delta := end - start) < TIMEOUT, (
            f"Test took too long ({delta * 1000} milliseconds). Speed it up!"
        )
        print("Test completed in less than", MILLIS, "milliseconds!")

        print("\nChecking the first linked list")
        check_links(linked_list, first_item, last_item, num_items)

        print("\nChecking the second linked list")
        check_links(linked_list2, last_item, first_item, num_items)

    finally:
        cleanup_list(linked_list)
        cleanup_list(linked_list2)


OPTIONS = "Patrick Bateman", "Paul Allen", "Evelyn Williams", "Luis Carruthers"

def get_items(num: int):
    seed(1)
    return ( choice(OPTIONS) for _ in range(num) )


def check_links(llist: LinkedList, head: str, tail: str, expected_length: int):
    print(f"Expected Head: {head}")
    print(f"Actual Head: {llist.head}")
    assert llist.head and head == llist.head.val, (
        "The linked list's head node does not have the expected value. "
        "Check if nodes added to the head are set as the new head node"
    )

    print(f"Expected Tail: {tail}")
    print(f"Actual Tail: {llist.tail}")
    assert llist.tail and tail == llist.tail.val, (
        "The linked list's tail node does not have the expected value. "
        "Check if nodes added to the tail are set as the new tail node"
    )

    actual_length = 0
    for _ in llist: actual_length += 1

    print(f"Expected Length: {expected_length}")
    print(f"Actual Length: {actual_length}")

    assert expected_length == actual_length, (
        "The linked list is not the expected length of linked nodes. "
        "Check if added nodes are set as the new head or tail"
    )


def cleanup_list(llist: LinkedList):
    current = llist.head
    while current: current.next, current = None, current.next
    llist.head = llist.tail = None
