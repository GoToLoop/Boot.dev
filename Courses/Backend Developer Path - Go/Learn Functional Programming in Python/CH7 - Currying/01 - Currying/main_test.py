#!/usr/bin/env -S python3 -m pytest

import pytest
from main import converted_font_size

run_cases = [
    (12, "txt", 12),
    (16, "md", 32),
]

submit_cases = [
    pytest.param(14, "html", "invalid doc type", marks=pytest.mark.submit),
    pytest.param(0, "txt", 0, marks=pytest.mark.submit),
    pytest.param(50, "md", 100, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("font_size", "doc_type", "expected"), run_cases + submit_cases
)
def test_converted_font_size(
    font_size: int, doc_type: str, expected: int | str
) -> None:
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * font_size: {font_size}")
    print(f" * doc_type: {doc_type}")
    print(f"Expected: {expected}")
    try:
        result = converted_font_size(font_size)(doc_type)
    except Exception as error:
        result = str(error)
    print(f"Actual:   {result}")
    assert result == expected
