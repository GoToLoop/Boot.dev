#!/usr/bin/env -S python3 -m pytest

import pytest
from main import bubble_sort

run_cases = [
    pytest.param([5, 7, 3, 6, 8], [3, 5, 6, 7, 8]),
    pytest.param([2, 1], [1, 2]),
]

submit_cases = [
    pytest.param([], [], marks=pytest.mark.submit),
    pytest.param([1], [1], marks=pytest.mark.submit),
    pytest.param([1, 5, -3, 2, 4], [-3, 1, 2, 4, 5], marks=pytest.mark.submit),
    pytest.param(
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        marks=pytest.mark.submit,
    ),
    pytest.param([1, 3, 2, 5, 4], [1, 2, 3, 4, 5], marks=pytest.mark.submit),
]

@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_bubble_sort(input1: list[int], expected_output: list[int]):
    print("\n---------------------------------")
    print(f"Input:\n * {input1}")
    print(f"Expected: {expected_output}")
    result = bubble_sort(input1)
    print(f"Actual:   {result}")
    assert result == expected_output
