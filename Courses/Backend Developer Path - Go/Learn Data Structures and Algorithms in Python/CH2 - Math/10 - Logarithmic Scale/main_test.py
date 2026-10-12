#!/usr/bin/env -S python3 -m pytest

import pytest
from main import log_scale

run_cases = [
    pytest.param([1, 10, 100, 1000], 10, [0.0, 1.0, 2.0, 3.0]),
    pytest.param([1, 2, 4, 8], 2, [0.0, 1.0, 2.0, 3.0]),
]

submit_cases = [
    pytest.param([2, 4, 8, 16], 2, [1.0, 2.0, 3.0, 4.0], marks=pytest.mark.submit),
    pytest.param([3, 9, 27, 81], 3, [1.0, 2.0, 3.0, 4.0], marks=pytest.mark.submit),
    pytest.param([5, 25, 125, 625], 5, [1.0, 2.0, 3.0, 4.0], marks=pytest.mark.submit),
    pytest.param(
        [10, 100, 1000, 10000],
        10,
        [1.0, 2.0, 3.0, 4.0],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [20, 400, 8000, 160000],
        20,
        [1.0, 2.0, 3.0, 4.0],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("data", "base", "expected_output"), run_cases + submit_cases)
def test_log_scale(data, base, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * data: {data}")
    print(f" * base: {base}")
    print(f"Expected: {expected_output}")
    scaled_data = [round(value, 2) for value in log_scale(data, base)]
    print(f"Actual:   {scaled_data}")
    assert scaled_data == expected_output
