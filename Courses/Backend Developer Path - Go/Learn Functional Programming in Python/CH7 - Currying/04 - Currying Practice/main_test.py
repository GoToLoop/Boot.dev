#!/usr/bin/env -S python3 -m pytest

import pytest
from main import create_markdown_image

run_cases = [
    (
        "seal",
        "https://imgur.com/oglPAXK",
        "this is a seal",
        '![seal](https://imgur.com/oglPAXK "this is a seal")',
    ),
    (
        "cinnamon roll",
        "https://imgur.com/a/0MyOP",
        "this is a cinnamon roll",
        '![cinnamon roll](https://imgur.com/a/0MyOP "this is a cinnamon roll")',
    ),
]

submit_cases = [
    pytest.param(
        "banana",
        "https://imgur.com/nlArAKx",
        None,
        "![banana](https://imgur.com/nlArAKx)",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "not an image",
        "https://en.wikipedia.org/wiki/Variable_(computer_science)",
        "showing escape characters",
        '![not an image](https://en.wikipedia.org/wiki/Variable_%28computer_science%29 "showing escape characters")',
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("alt_text", "url", "title", "expected"), run_cases + submit_cases
)
def test_create_markdown_image(
    alt_text: str, url: str, title: str | None, expected: str
) -> None:
    print("\n---------------------------------")
    print("Inputs:")
    print(f"* Alt Text: {alt_text}")
    print(f"* URL: {url}")
    print(f"* Title: {title}")
    print(f"Expected: {expected}")
    result = create_markdown_image(alt_text)(url)()
    if title:
        result = create_markdown_image(alt_text)(url)(title)
    print(f"Actual:   {result}")
    assert result == expected
