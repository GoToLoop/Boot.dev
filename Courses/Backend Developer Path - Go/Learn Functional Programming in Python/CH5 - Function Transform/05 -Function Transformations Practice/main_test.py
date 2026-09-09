#!/usr/bin/env -S python3 -m pytest

from collections.abc import Callable

import pytest
from main import fix_ellipsis, get_filter_cmd, replace_bad, replace_ellipsis

FilterFunc = Callable[[str], str]
FilterArgs = tuple[str, ...]
FilterCase = tuple[FilterArgs, str]

run_cases = [
    (
        "replace_bad",
        replace_bad,
        "replace_ellipsis",
        replace_ellipsis,
        [
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--one",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--two",
                ),
                "I'm bad, and that's good. I will never be good, and that's not bad...",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--three",
                ),
                "I'm good, and that's good. I will never be good, and that's not good...",
            ),
        ],
    ),
]

submit_cases = [
    pytest.param(
        "replace_ellipsis",
        replace_ellipsis,
        "fix_ellipsis",
        fix_ellipsis,
        [
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--one",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--two",
                ),
                "There's no place like home.. but sometimes, it's nice to get away... and explore...",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--three",
                ),
                "There's no place like home... but sometimes, it's nice to get away... and explore.....",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "",
                ),
                "invalid option",
            ),
        ],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("filter_one_name", "filter_one", "filter_two_name", "filter_two", "cases"),
    run_cases + submit_cases,
)
def test_get_filter_cmd(
    filter_one_name: str,
    filter_one: FilterFunc,
    filter_two_name: str,
    filter_two: FilterFunc,
    cases: list[FilterCase],
) -> None:
    print("\n---------------------------------")
    print(f"Input functions: {filter_one_name} and {filter_two_name}")
    filter_cmd = get_filter_cmd(filter_one, filter_two)
    results = []
    expected_results = []
    for args, expected in cases:
        print("Calling filter_cmd with:")
        print(f" * content: {args[0]}")
        if len(args) > 1:
            print(f" * option: {args[1]}")
        else:
            print(" * option: (default)")
        if expected == "invalid option":
            with pytest.raises(Exception) as error:
                filter_cmd(*args)
            result = str(error.value)
        else:
            result = filter_cmd(*args)
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        results.append(result)
        expected_results.append(expected)
    assert results == expected_results
