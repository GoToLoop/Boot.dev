#!/usr/bin/env -S python3 -m pytest

import time

import pytest
from main import insertion_sort

run_cases = [
    pytest.param([4, 3, 2, 1], [1, 2, 3, 4]),
    pytest.param([9, 5, -3, 7], [-3, 5, 7, 9]),
]

submit_cases = [
    pytest.param([], [], marks=pytest.mark.submit),
    pytest.param([1], [1], marks=pytest.mark.submit),
    pytest.param([5, 3, 4, 1, 2], [1, 2, 3, 4, 5], marks=pytest.mark.submit),
    pytest.param(
        [0, -2, -5, 3, 2, 1],
        [-5, -2, 0, 1, 2, 3],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        marks=pytest.mark.submit,
    ),
]

@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_insertion_sort(input1: list[int], expected_output: list[int]):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expected: {expected_output}")
    start = time.time()
    result = insertion_sort(input1)
    elapsed = time.time() - start
    timeout = 1.00
    if elapsed < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
    print(f"Actual: {result}")
    assert elapsed < timeout
    assert result == expected_output
