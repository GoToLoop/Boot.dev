#!/usr/bin/env -S python3 -m pytest

import pytest
from main import DocFormat, convert_format

run_cases = [
    ("# Hello, world!", DocFormat.MD, DocFormat.HTML, "<h1>Hello, world!</h1>"),
    (
        "This is plain text.",
        DocFormat.TXT,
        DocFormat.PDF,
        "[PDF] This is plain text. [PDF]",
    ),
]

submit_cases = [
    pytest.param(
        "<h1>Title</h1>",
        DocFormat.HTML,
        DocFormat.MD,
        "# Title",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "Something wicked",
        DocFormat.TXT,
        None,
        "invalid type",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("content", "from_fmt", "to_fmt", "expected"), run_cases + submit_cases
)
def test_convert_format(
    content: str, from_fmt: DocFormat, to_fmt: DocFormat | None, expected: str
) -> None:
    print("\n---------------------------------")
    print(f"Converting from {from_fmt} to {to_fmt}...")
    print(f"Content: {content}")
    print(f"Expected: {expected}")
    try:
        result = convert_format(content, from_fmt, to_fmt)
    except Exception as error:
        result = str(error)
    print(f"Actual: {result}")
    assert result == expected
