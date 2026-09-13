#!/usr/bin/env -S python3 -m pytest

import pytest
from main import is_palindrome

run_cases = [
    ("aibohphobia", True),
    ("eve", True),
    ("level", True),
    ("", True),
    ("tat", True),
    ("rotator", True),
    ("potato", False),
]

submit_cases = [
    pytest.param("a", True, marks=pytest.mark.submit),
    pytest.param("apple", False, marks=pytest.mark.submit),
    pytest.param("redivider", True, marks=pytest.mark.submit),
    pytest.param("divide", False, marks=pytest.mark.submit),
    pytest.param("kayak", True, marks=pytest.mark.submit),
    pytest.param("river", False, marks=pytest.mark.submit),
    pytest.param("no", False, marks=pytest.mark.submit),
]


def test_is_lru_cache_used() -> None:
    print("\n---------------------------------")
    cache_info = getattr(is_palindrome, "cache_info", None)
    if callable(cache_info):
        print("is_palindrome uses lru_cache")
    else:
        print("is_palindrome does not use lru_cache")
    assert callable(cache_info)


@pytest.mark.parametrize(("input_word", "expected"), run_cases + submit_cases)
def test_is_palindrome(input_word: str, expected: bool) -> None:
    print("\n---------------------------------")
    print(f"Input: '{input_word}'")
    print(f"Expected: {expected}")
    result = is_palindrome(input_word)
    print(f"Actual:   {result}")
    assert result == expected
