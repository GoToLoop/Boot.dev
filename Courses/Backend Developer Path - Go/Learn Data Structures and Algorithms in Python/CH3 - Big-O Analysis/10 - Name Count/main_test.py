#!/usr/bin/env -S python3 -m pytest

import pytest
from main import count_names

run_cases = [
    pytest.param(
        [["George", "Eva", "George"], ["Diane", "George", "Eva", "Frank"]],
        "George",
        3,
    ),
    pytest.param(
        [
            ["Amy", "Bob", "Candy"],
            ["Diane", "George", "Eva", "Frank"],
            ["Diane", "George"],
            ["George", "name", "George"],
        ],
        "George",
        4,
    ),
]

submit_cases = [
    pytest.param(
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "Hector",
        3,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "George",
        1,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [["Alex", "name", "Chloe"], ["Eric", "name", "Fred"], ["Hector", "name"]],
        "Alex",
        1,
        marks=pytest.mark.submit,
    ),
    pytest.param([], "George", 0, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_count_names(input1: list[list[str]], input2: str, expected_output: int):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * list of lists: {input1}")
    print(f" * target name: {input2}")
    result = count_names(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
