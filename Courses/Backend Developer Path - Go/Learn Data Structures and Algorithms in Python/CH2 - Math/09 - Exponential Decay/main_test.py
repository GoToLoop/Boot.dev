#!/usr/bin/env -S python3 -m pytest

import pytest
from main import decayed_followers

run_cases = [
    pytest.param(200, 0.5, 1, 100),
    pytest.param(200, 0.4, 2, 72),
    pytest.param(200, 0.05, 3, 171),
]

submit_cases = [
    pytest.param(1000, 0.005, 2, 990, marks=pytest.mark.submit),
    pytest.param(1000, 0.05, 3, 857, marks=pytest.mark.submit),
    pytest.param(1200, 0.55, 8, 2, marks=pytest.mark.submit),
    pytest.param(1200, 0.09, 16, 265, marks=pytest.mark.submit),
    pytest.param(0, 0.5, 1, 0, marks=pytest.mark.submit),
    pytest.param(100, 0, 5, 100, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_decayed_followers(input1, input2, input3, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * initial_followers: {input1}")
    print(f" * fraction_lost_daily: {input2}")
    print(f" * days: {input3}")
    result = round(decayed_followers(input1, input2, input3))
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
