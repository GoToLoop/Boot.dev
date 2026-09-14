#!/usr/bin/env -S python3 -m pytest

import pytest
from main import Parsed, ParseError

TestCase = Parsed | ParseError

run_cases = [
    Parsed("why_fp.txt", "Because we're better than everyone else"),
    ParseError("why_fp.docx", "Can't handle weird windows files"),
]

submit_cases = [
    pytest.param(
        Parsed("why_fp.md", "Because we're better than everyone else"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ParseError("why_fp.pdf", "Can't handle weird adobe files"),
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize("obj", run_cases + submit_cases)
def test_sum_type_properties(obj: TestCase) -> None:
    print("\n---------------------------------")
    print(f"Testing properties of {obj.doc_name}...")
    if isinstance(obj, Parsed):
        if not obj.text:
            print("Expecting .text to be non-empty")
        assert obj.text
        if not obj.doc_name:
            print("Expecting .doc_name to be non-empty")
        assert obj.doc_name
    elif isinstance(obj, ParseError):
        if not obj.err:
            print("Expecting .err to be non-empty")
        assert obj.err
        if not obj.doc_name:
            print("Expecting .doc_name to be non-empty")
        assert obj.doc_name
