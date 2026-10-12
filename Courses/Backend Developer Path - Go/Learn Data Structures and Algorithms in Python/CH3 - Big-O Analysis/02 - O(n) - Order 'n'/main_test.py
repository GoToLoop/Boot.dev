#!/usr/bin/env -S python3 -m pytest

import pytest
from main import find_max

run_cases = [
    pytest.param([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2343243),
    pytest.param([12, 12, 12], 12),
]

submit_cases = [
    pytest.param([10, 200, 3000, 5000, 4], 5000, marks=pytest.mark.submit),
    pytest.param([0], 0, marks=pytest.mark.submit),
    pytest.param([-1, -2, -3], -1, marks=pytest.mark.submit),
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, marks=pytest.mark.submit),
    pytest.param([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_find_max(input1: list[int], expected_output: int):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * nums: {input1}")
    result = find_max(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
