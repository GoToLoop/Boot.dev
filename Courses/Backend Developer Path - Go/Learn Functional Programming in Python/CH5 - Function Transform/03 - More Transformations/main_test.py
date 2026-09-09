#!/usr/bin/env -S python3 -m pytest

from collections.abc import Callable

import pytest
from main import (
    capitalize_content,
    doc_format_checker_and_converter,
    reverse_content,
)

ConversionFunc = Callable[[str], str]

run_cases = [
    (
        "capitalize_content",
        capitalize_content,
        "sample.txt",
        "I really don't feel like screaming today.",
        ["txt", "md", "doc"],
        "I REALLY DON'T FEEL LIKE SCREAMING TODAY.",
    ),
    (
        "reverse_content",
        reverse_content,
        "testing.doc",
        "This is probably how they write in the red room in Twin Peaks...",
        ["txt", "md", "doc"],
        "...skaeP niwT ni moor der eht ni etirw yeht woh ylbaborp si sihT",
    ),
]

submit_cases = [
    pytest.param(
        "capitalize_content",
        capitalize_content,
        "test.docx",
        "Okay actually I do feel like screaming today.",
        ["txt", "md", "doc"],
        "invalid file format",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "reverse_content",
        reverse_content,
        "end.ppt",
        "Cherry pie and coffee anyone?",
        ["txt", "md", "doc"],
        "invalid file format",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "capitalize_content",
        capitalize_content,
        "sample.doc",
        "I really do feel like eating today.",
        ["txt", "md", "doc"],
        "I REALLY DO FEEL LIKE EATING TODAY.",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "reverse_content",
        reverse_content,
        "testing.md",
        "The owls are not what they seem.",
        ["txt", "md", "doc"],
        ".mees yeht tahw ton era slwo ehT",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    (
        "conversion_fn_name",
        "conversion_fn",
        "filename",
        "doc_content",
        "valid_formats",
        "expected",
    ),
    run_cases + submit_cases,
)
def test_doc_format_checker_and_converter(
    conversion_fn_name: str,
    conversion_fn: ConversionFunc,
    filename: str,
    doc_content: str,
    valid_formats: list[str],
    expected: str,
) -> None:
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * conversion_func: {conversion_fn_name}")
    print(f" * filename: {filename}")
    print(f" * doc_content: {doc_content}")
    print(f" * valid_formats: {valid_formats}")
    print(f"Expected: {expected}")
    try:
        result = doc_format_checker_and_converter(conversion_fn, valid_formats)(
            filename, doc_content
        )
    except ValueError as error:
        result = str(error)
    print(f"Actual:   {result}")
    assert result == expected
