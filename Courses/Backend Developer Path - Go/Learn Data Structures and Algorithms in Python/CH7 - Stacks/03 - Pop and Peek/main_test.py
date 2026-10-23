#!/usr/bin/env -S python3 -m pytest

import pytest
from main import Stack

run_cases = [
    (
        [
            ("push", {"name": "Alice", "role": "Developer"}),
            ("push", {"name": "Bob", "role": "Designer"}),
            ("size", None),
            ("peek", None),
            ("pop", None),
            ("size", None),
        ],
        [
            None,
            None,
            2,
            {"name": "Bob", "role": "Designer"},
            {"name": "Bob", "role": "Designer"},
            1,
        ],
    ),
    (
        [
            ("peek", None),
        ],
        [
            None,
        ],
    ),
    (
        [
            ("push", {"name": "Charlie", "company": "TechCorp"}),
            ("push", {"name": "David", "skills": ["Python", "JavaScript"]}),
            ("pop", None),
            ("pop", None),
            ("pop", None),
        ],
        [
            None,
            None,
            {"name": "David", "skills": ["Python", "JavaScript"]},
            {"name": "Charlie", "company": "TechCorp"},
            None,
        ],
    ),
]

submit_cases = [
    pytest.param(
        [
            ("push", {"name": "Eve", "role": "Manager", "years": 5}),
            ("peek", None),
            ("push", {"name": "Frank", "role": "DevOps"}),
            ("size", None),
            ("pop", None),
            ("pop", None),
            ("pop", None),
        ],
        [
            None,
            {"name": "Eve", "role": "Manager", "years": 5},
            None,
            2,
            {"name": "Frank", "role": "DevOps"},
            {"name": "Eve", "role": "Manager", "years": 5},
            None,
        ],
        marks=pytest.mark.submit,
    ),
]


def visualize_stack(stack):
    if not stack:
        return "- (empty)"
    return "\n".join(
        [f"    - {item['name']}: {list(item.values())[1]}" for item in reversed(stack)]
    )


@pytest.mark.parametrize(("operations", "expected_outputs"), run_cases + submit_cases)
def test_stack(operations, expected_outputs):
    print("\n---------------------------------")
    stack = Stack()
    actual_outputs = []

    try:
        for i, (op, value) in enumerate(operations):
            print(f"Operation {i + 1}:")
            if op == "push":
                print(f"  Push: {value}")
                actual_outputs.append(stack.push(value))
            elif op == "pop":
                result = stack.pop()
                print(f"  Pop: {result}")
                actual_outputs.append(result)
            elif op == "peek":
                result = stack.peek()
                print(f"  Peek: {result}")
                actual_outputs.append(result)
            elif op == "size":
                result = stack.size()
                print(f"  Size: {result}")
                actual_outputs.append(result)

            print(f"  Stack:\n{visualize_stack(stack.items)}")
            print()
    except Exception as error:
        print(f"Error: {error}")
        raise

    print(f"Expected outputs: {expected_outputs}")
    print(f"Actual outputs: {actual_outputs}")
    assert actual_outputs == expected_outputs
