#!/usr/bin/env -S python3 -m pytest

import pytest
from main import selection_sort

run_cases = [
    pytest.param([5, 3, 8, 6, 1, 9], [1, 3, 5, 6, 8, 9]),
    pytest.param(
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ),
]

submit_cases = [
    pytest.param(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [15, 12, 8, 7, 5, 3, 1],
        [1, 3, 5, 7, 8, 12, 15],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [10, 5, 3, 7, 2, 8, 1],
        [1, 2, 3, 5, 7, 8, 10],
        marks=pytest.mark.submit,
    ),
    pytest.param([], [], marks=pytest.mark.submit),
    pytest.param([1], [1], marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_selection_sort(input1: list[int], expected_output: list[int]):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expected: {expected_output}")
    result = selection_sort(input1)
    print(f"Actual:   {result}")
    assert result == expected_output
