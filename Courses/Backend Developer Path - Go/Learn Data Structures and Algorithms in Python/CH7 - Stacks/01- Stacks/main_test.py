#!/usr/bin/env -S python3 -m pytest

import pytest
from main import Stack

run_cases = [
    (
        [
            ("push", {"name": "Alice", "role": "Developer"}),
            ("push", {"name": "Bob", "title": "CTO"}),
            ("size", None),
        ],
        2,
        "Bob",
    ),
    (
        [
            ("push", {"name": "Charlie", "company": "TechCorp"}),
            ("push", {"name": "Diana", "skills": "Python"}),
            ("push", {"name": "Ethan", "role": "Manager"}),
            ("size", None),
        ],
        3,
        "Ethan",
    ),
]

submit_cases = [
    pytest.param(
        [
            ("size", None),
        ],
        0,
        None,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [
            ("push", {"name": "Frank", "experience": "5 years"}),
            ("push", {"name": "Grace", "education": "MBA"}),
            ("push", {"name": "Henry", "location": "New York"}),
            ("push", {"name": "Ivy", "industry": "Finance"}),
            ("size", None),
        ],
        4,
        "Ivy",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [
            ("push", {"name": "Jack", "connections": 500}),
            ("size", None),
            ("push", {"name": "Kelly", "endorsements": 50}),
            ("size", None),
        ],
        2,
        "Kelly",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("operations", "expected_output", "expected_name_at_top"),
    run_cases + submit_cases,
)
def test_stack(operations, expected_output, expected_name_at_top):
    print("\n---------------------------------")
    stack = Stack()
    result = None
    for op, value in operations:
        if op == "push":
            print(f"Push: {value}")
            stack.push(value)
        elif op == "size":
            result = stack.size()

    print(f"Expecting size: {expected_output}")
    print(f"Actual size: {result}")
    assert result == expected_output

    if len(stack.items) > 0:
        name_at_top = stack.items[-1]["name"]
        print(f"Expecting last added name: {expected_name_at_top}")
        print(f"Actual last added name: {name_at_top}")
        assert name_at_top == expected_name_at_top
