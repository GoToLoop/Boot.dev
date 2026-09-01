#!/usr/bin/env -S python3 -m pytest

import pytest
from main import find_longest_word

run_cases = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    ("Then I die happy", "happy"),
    ("Et tu, Brute?", "Brute?"),
    ("Do not disturb my circles", "disturb"),
]

submit_cases = [
    pytest.param("", "", marks=pytest.mark.submit),
    pytest.param(" ", "", marks=pytest.mark.submit),
    pytest.param(
        "Let us cross over the river and rest under the shade of the trees",
        "cross",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("document", "expected"), run_cases + submit_cases)
def test_find_longest_word(document: str, expected: str) -> None:
    print("\n---------------------------------")
    print(f"Input: '{document}'")
    print(f"Expected: '{expected}'")
    result = find_longest_word(document)
    print(f"Actual:   '{result}'")
    assert result == expected
