#!/usr/bin/env -S python3 -m pytest

import pytest
from main import exponential_growth

run_cases = [
    (10, 2, 4, [10, 20, 40, 80, 160]),
    (0, 2, 2, [0, 0, 0]),
    (20, 2, 6, [20, 40, 80, 160, 320, 640, 1280]),
]

submit_cases = [
    pytest.param(30, 3, 3, [30, 90, 270, 810], marks=pytest.mark.submit),
    pytest.param(
        40,
        10,
        10,
        [
            40,
            400,
            4000,
            40000,
            400000,
            4000000,
            40000000,
            400000000,
            4000000000,
            40000000000,
            400000000000,
        ],
        marks=pytest.mark.submit,
    ),
    pytest.param(10, 5, 0, [10], marks=pytest.mark.submit),
    pytest.param(1, 1, 5, [1, 1, 1, 1, 1, 1], marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("n", "factor", "days", "expected"), run_cases + submit_cases
)
def test_exponential_growth(
    n: int, factor: int, days: int, expected: list[int]
):
    print("\n" + "-" * 40)
    print(f"Inputs: \nn: {n}, factor: {factor}, days: {days}")
    print(f"Expected: {expected}")
    result = exponential_growth(n, factor, days)
    print(f"Actual:   {result}")
    assert result == expected
