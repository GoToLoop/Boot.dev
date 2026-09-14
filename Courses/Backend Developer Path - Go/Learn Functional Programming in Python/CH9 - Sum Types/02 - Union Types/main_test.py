#!/usr/bin/env -S python3 -m pytest

import pytest
from main import Parsed, ParseError, display_parse_result, parse_document

ExpectedType = type[Parsed] | type[ParseError]

run_cases = [
    (
        "why_fp.txt",
        "Because functions are easier to test",
        Parsed,
        "Parsed why_fp.txt: 36 characters",
    ),
    ("why_fp.md", "", ParseError, "Failed why_fp.md: no content"),
]

submit_cases = [
    pytest.param(
        "functional-patterns.txt",
        "Unions make alternative states explicit",
        Parsed,
        "Parsed functional-patterns.txt: 39 characters",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "empty.md",
        "",
        ParseError,
        "Failed empty.md: no content",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("doc_name", "content", "expected_type", "expected_msg"),
    run_cases + submit_cases,
)
def test_parse_document(
    doc_name: str,
    content: str,
    expected_type: ExpectedType,
    expected_msg: str,
) -> None:
    print("\n---------------------------------")
    print(f"Parsing document: {doc_name}")
    print(f"Content length: {len(content)}")
    result = parse_document(doc_name, content)
    actual_type = type(result)
    print(f"Expected type: {expected_type.__name__}")
    print(f"Actual type: {actual_type.__name__}")
    assert actual_type is expected_type
    if result.doc_name != doc_name:
        print(f"Expected doc_name: {doc_name}")
        print(f"Actual doc_name: {result.doc_name}")
    assert result.doc_name == doc_name
    if isinstance(result, Parsed):
        if result.text != content:
            print(f"Expected text: {content}")
            print(f"Actual text: {result.text}")
        assert result.text == content
    if isinstance(result, ParseError):
        if result.err != "no content":
            print('Expected err: "no content"')
            print(f"Actual err: {result.err}")
        assert result.err == "no content"
    actual_msg = display_parse_result(result)
    print(f"Expected message: {expected_msg}")
    print(f"Actual message: {actual_msg}")
    assert actual_msg == expected_msg
