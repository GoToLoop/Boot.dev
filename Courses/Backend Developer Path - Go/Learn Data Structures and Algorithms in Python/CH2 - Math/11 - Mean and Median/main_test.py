#!/usr/bin/env -S python3 -m pytest

import pytest
from main import average_followers

run_cases = [
    pytest.param([1], 1),
    pytest.param([1, 2, 3, 4, 5, 6, 7], 4),
    pytest.param([12, 12, 12], 12),
    pytest.param([], None),
]

submit_cases = [
    pytest.param([0], 0, marks=pytest.mark.submit),
    pytest.param([100, 200, 300, 400, 500], 300, marks=pytest.mark.submit),
    pytest.param([5, 10, 200, 3000, 5000], 1643, marks=pytest.mark.submit),
    pytest.param(
        [12_345, 618_222, 58_832_221, 2_180_831_475, 8_663_863_102],
        2_180_831_473,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_average_followers(input1, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * nums: {input1}")
    print(f"Expected: {expected_output}")
    result = average_followers(input1)
    if expected_output is not None and result is not None:
        result = int(result)
    print(f"Actual:   {result}")
    assert result == expected_output
