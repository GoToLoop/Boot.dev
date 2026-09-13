#!/usr/bin/env -S python3 -m pytest

from collections.abc import Callable

import pytest
from formatters import concat, format_as_essay

FormatterFunc = Callable[..., str]
Args = tuple[str, ...]
Kwargs = dict[str, str]

run_cases = [
    (
        ("# We like to play it all", "## Welcome to Tally Hall"),
        {},
        concat,
        "concat",
        """  First: We like to play it all
  Second: Welcome to Tally Hall""",
    ),
    (
        (),
        {
            "title": "Why Python is Great",
            "conclusion": "## That's why Python is great!",
            "body": "Maybe it isn't",
        },
        format_as_essay,
        "format_as_essay",
        """  Title: Why Python is Great
  Body: Maybe it isn't
  Conclusion: That's why Python is great!""",
    ),
]

submit_cases = [
    pytest.param(
        ("# Boots' grocery list", "Salmon, gems, arcanum crystals"),
        {"conclusion": "## Don't forget!"},
        format_as_essay,
        "format_as_essay",
        """  Title: Boots' grocery list
  Body: Salmon, gems, arcanum crystals
  Conclusion: Don't forget!""",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("args", "kwargs", "func", "func_name", "expected"), run_cases + submit_cases
)
def test_formatter(
    args: Args,
    kwargs: Kwargs,
    func: FormatterFunc,
    func_name: str,
    expected: str,
) -> None:
    print("\n---------------------------------")
    print(f"Function: {func_name}")
    print("Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f" * {key}: {value}")
    print("Expected:")
    print(expected)
    try:
        result = func(*args, **kwargs)
    except Exception as error:
        result = f"Error: {error}"
    print("Actual:")
    print(result)
    assert result == expected
