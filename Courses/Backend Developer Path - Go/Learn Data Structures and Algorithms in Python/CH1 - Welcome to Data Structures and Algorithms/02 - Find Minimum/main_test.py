#!/usr/bin/env -S python3 -m pytest

import pytest
from main import find_minimum

run_cases = [
    pytest.param([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 1),
    pytest.param([12, 12, 12], 12),
    pytest.param([10, 200, 3000, 5000, 4], 4)
]

submit_cases = [
    pytest.param([1], 1, marks=pytest.mark.submit),
    pytest.param([1, 2, 3, 4, 5], 1, marks=pytest.mark.submit),
    pytest.param([5, 4, 3, 2, 1], 1, marks=pytest.mark.submit),
    pytest.param([100, 200, 300, 400, 500], 100, marks=pytest.mark.submit),
    pytest.param([500, 400, 300, 200, 100], 100, marks=pytest.mark.submit),
    pytest.param([], None, marks=pytest.mark.submit)
]

@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_find_minimum(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = find_minimum(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
