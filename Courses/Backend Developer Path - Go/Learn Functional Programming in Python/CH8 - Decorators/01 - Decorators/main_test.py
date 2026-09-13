#!/usr/bin/env -S python3 -m pytest

import pytest
from main import process_doc

Inputs = tuple[str, str]
Output = tuple[str, dict[str, int]]

run_cases = [
    (
        ("Welcome to the jungle", "txt"),
        ("Processing doc: 'Welcome to the jungle'. File Type: txt", {"txt": 1}),
    ),
    (
        ("We've got fun and games", "txt"),
        ("Processing doc: 'We've got fun and games'. File Type: txt", {"txt": 2}),
    ),
    (
        ("We've got *everything* you want honey", "md"),
        (
            "Processing doc: 'We've got *everything* you want honey'. File Type: md",
            {"txt": 2, "md": 1},
        ),
    ),
]

submit_cases = [
    pytest.param(
        ("We are the champions my friends", "docx"),
        (
            "Processing doc: 'We are the champions my friends'. File Type: docx",
            {"txt": 2, "md": 1, "docx": 1},
        ),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("print('hello world')", "py"),
        (
            "Processing doc: 'print('hello world')'. File Type: py",
            {"txt": 2, "md": 1, "docx": 1, "py": 1},
        ),
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("inputs", "expected"), run_cases + submit_cases)
def test_process_doc(inputs: Inputs, expected: Output) -> None:
    print("\n---------------------------------")
    print("Inputs:")
    for value in inputs:
        print(f" * {value}")
    print("Expected:")
    for value in expected:
        print(f" * {value}")
    result = process_doc(*inputs)
    print("Actual:")
    for value in result:
        print(f" * {value}")
    assert result == expected
