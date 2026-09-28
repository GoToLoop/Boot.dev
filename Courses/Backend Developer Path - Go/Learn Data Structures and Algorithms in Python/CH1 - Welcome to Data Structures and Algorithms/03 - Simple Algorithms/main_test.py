#!/usr/bin/env -S python3 -m pytest

import pytest
from main import summed

run_cases = [
    pytest.param([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2686826),
    pytest.param([12, 12, 12], 36)
]

submit_cases = [
    pytest.param([10, 200, 3000, 5000, 4], 8214, marks=pytest.mark.submit),
    pytest.param([], 0, marks=pytest.mark.submit),
    pytest.param([1], 1, marks=pytest.mark.submit),
    pytest.param([123456789], 123456789, marks=pytest.mark.submit),
    pytest.param([-1, -2, -3], -6, marks=pytest.mark.submit),
    pytest.param([0, 0, 0, 0, 0], 0, marks=pytest.mark.submit)
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_summed(input1: list[int], expected_output: int):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * nums: {input1}")
    result = summed(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
