#!/usr/bin/env -S python3 -m pytest

import pytest
from main import num_possible_orders

run_cases = [
    pytest.param(2, 2),
    pytest.param(3, 6),
    pytest.param(5, 120),
]

submit_cases = [
    pytest.param(1, 1, marks=pytest.mark.submit),
    pytest.param(6, 720, marks=pytest.mark.submit),
    pytest.param(7, 5040, marks=pytest.mark.submit),
    pytest.param(8, 40320, marks=pytest.mark.submit),
    pytest.param(9, 362880, marks=pytest.mark.submit),
    pytest.param(11, 39916800, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_num_possible_orders(input1: int, expected_output: int):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * num_posts: {input1}")
    result = num_possible_orders(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
