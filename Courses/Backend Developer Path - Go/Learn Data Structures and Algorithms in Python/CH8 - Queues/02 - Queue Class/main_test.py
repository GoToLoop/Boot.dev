#!/usr/bin/env -S python3 -m pytest

import pytest
from main import Queue

run_cases = [
    (
        [("push", "Rand"), ("push", "Mat"), ("peek", None), ("pop", None)],
        ["Rand", "Rand"],
    ),
    (
        [
            ("push", "Egwene"),
            ("push", "Nynaeve"),
            ("size", None),
            ("pop", None),
            ("size", None),
        ],
        [2, "Egwene", 1],
    ),
    (
        [("push", "Aviendha"), ("pop", None), ("peek", None)],
        ["Aviendha", None],
    ),
]

submit_cases = [
    pytest.param(
        [("pop", None), ("peek", None), ("size", None)],
        [None, None, 0],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [
            ("push", "Perrin"),
            ("push", "Moiraine"),
            ("push", "Lan"),
            ("pop", None),
            ("pop", None),
            ("peek", None),
        ],
        ["Perrin", "Moiraine", "Lan"],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [("push", "Thom"), ("pop", None), ("push", "Loial"), ("peek", None)],
        ["Thom", "Loial"],
        marks=pytest.mark.submit,
    ),
]


def visualize_queue(queue):
    if not queue.items:
        return "Queue is empty"
    return "\n".join([f"- {item}" for item in reversed(queue.items)])


@pytest.mark.parametrize((
    "operations", "expected_outputs"), run_cases + submit_cases
)
def test_queue(operations, expected_outputs):
    print("\n---------------------------------")
    queue = Queue()
    outputs = []
    for op, value in operations:
        if op == "push":
            queue.push(value)
            print(f"Push: {value}")
        elif op == "pop":
            result = queue.pop()
            outputs.append(result)
            print(f"Pop: {result}")
        elif op == "peek":
            result = queue.peek()
            outputs.append(result)
            print(f"Peek: {result}")
        elif op == "size":
            result = queue.size()
            outputs.append(result)
            print(f"Size: {result}")

        print("\nQueue state:")
        print(visualize_queue(queue))
        print()

    print(f"Expected: {expected_outputs}")
    print(f"Actual: {outputs}")
    assert outputs == expected_outputs
