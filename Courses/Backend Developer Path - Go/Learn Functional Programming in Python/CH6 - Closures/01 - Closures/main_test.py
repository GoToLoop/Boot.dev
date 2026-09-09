#!/usr/bin/env -S python3 -m pytest

import pytest
from main import word_count_aggregator

run_cases = [
    (
        [
            "Welcome to the jungle",
            "We've got fun and games",
            "We've got everything you want honey",
        ],
        15,
    )
]

submit_cases = [
    pytest.param(
        [
            "We are the champions my friends",
            "And we'll keep on fighting till the end",
        ],
        14,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [
            "I've got another confession to make",
            "I'm your fool",
            "Everyone's got their chains to break",
            "Holdin' you",
        ],
        17,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_docs", "expected"), run_cases + submit_cases)
def test_word_count_aggregator(input_docs: list[str], expected: int) -> None:
    print("\n---------------------------------")
    print("Input:")
    for doc in input_docs:
        print(f" * {doc}")
    print(f"Expected: {expected}")

    aggregator = word_count_aggregator()

    result = 0
    for input_doc in input_docs:
        result = aggregator(input_doc)

    print(f"Actual:   {result}")
    assert result == expected
