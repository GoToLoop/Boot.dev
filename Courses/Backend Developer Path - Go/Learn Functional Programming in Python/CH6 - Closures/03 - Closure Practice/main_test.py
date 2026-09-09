#!/usr/bin/env -S python3 -m pytest

import pytest
from main import new_collection

run_cases = [
    (["Dan Evans"], ["Charlie Prince"], ["Dan Evans", "Charlie Prince"]),
    (
        ["Dan Evans", "Ben Wade"],
        ["Alice Evans"],
        ["Dan Evans", "Ben Wade", "Alice Evans"],
    ),
    (
        ["Dan Evans", "Ben Wade", "Alice Evans"],
        ["Doc Potter", "Butterfield"],
        ["Dan Evans", "Ben Wade", "Alice Evans", "Doc Potter", "Butterfield"],
    ),
]

submit_cases = [
    pytest.param(
        ["Dan Evans", "Ben Wade", "Alice Evans"],
        [],
        ["Dan Evans", "Ben Wade", "Alice Evans"],
        marks=pytest.mark.submit,
    ),
    pytest.param([], ["William Evans"], ["William Evans"], marks=pytest.mark.submit),
    pytest.param(
        ["Dan Evans", "Ben Wade"],
        ["Charlie Prince", "Butterfield"],
        ["Dan Evans", "Ben Wade", "Charlie Prince", "Butterfield"],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("initial_docs", "new_docs", "expected"), run_cases + submit_cases
)
def test_new_collection(
    initial_docs: list[str], new_docs: list[str], expected: list[str]
) -> None:
    print("\n---------------------------------")
    print(f"Initial documents: {initial_docs}")
    print(f"Documents to add: {new_docs}")
    print(f"Expected: {expected}")
    copy_of_initial_docs = initial_docs.copy()
    add_doc = new_collection(initial_docs)
    result = initial_docs.copy()
    for doc in new_docs:
        result = add_doc(doc)
    print(f"Actual:   {result}")
    assert copy_of_initial_docs == initial_docs, (
        "You should not modify the initial list"
    )
    assert result == expected, "Unexpected result"
