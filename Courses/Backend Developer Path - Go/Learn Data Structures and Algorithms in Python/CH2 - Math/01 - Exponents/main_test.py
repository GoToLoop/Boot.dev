#!/usr/bin/env -S python3 -m pytest

import pytest
from main import get_estimated_spread

run_cases = [
    pytest.param([7, 4, 3, 100, 765, 2344, 1, 2, 32], 5056),
    pytest.param([12, 12, 12], 45),
    pytest.param([10, 200, 3000, 5000, 4], 11333),
]

submit_cases = [
    pytest.param([], 0, marks=pytest.mark.submit),
    pytest.param([1, 1, 1], 4, marks=pytest.mark.submit),
    pytest.param([100], 100, marks=pytest.mark.submit),
    pytest.param([50, 60, 70, 80, 90], 483, marks=pytest.mark.submit),
    pytest.param(
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        872,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
        ],
        1912,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_get_estimated_spread(input1: list[int], expected_output: float):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = round(get_estimated_spread(input1))
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
