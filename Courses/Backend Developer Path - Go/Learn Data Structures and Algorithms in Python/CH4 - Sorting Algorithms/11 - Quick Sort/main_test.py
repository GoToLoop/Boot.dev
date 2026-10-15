#!/usr/bin/env -S python3 -m pytest

import time

import pytest
from main import quick_sort

marks=pytest.mark.submit

run_cases = [
    pytest.param([2, 1, 3], 0, 2, [1, 2, 3]),
    pytest.param([9, 6, 2, 1, 8, 7], 0, 5, [1, 2, 6, 7, 8, 9]),
]

submit_cases = [
    pytest.param([], 0, -1, [], marks=marks),
    pytest.param([1], 0, 0, [1], marks=marks),
    pytest.param([1, 2, 3, 4, 5], 0, 4, [1, 2, 3, 4, 5], marks=marks),
    pytest.param([5, 4, 3, 2, 1], 0, 4, [1, 2, 3, 4, 5], marks=marks),
    pytest.param(
        [0, 1, 6, 4, 7, 3, 2, 8, 5, -9],
        0,
        9,
        [-9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
        marks=marks,
    ),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_quick_sort(
    input1: list[int], input2: int, input3: int, expected_output: list[int]
):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * nums: {input1}")
    print(f" * low: {input2}")
    print(f" * high: {input3}")
    print(f"Expected: {expected_output}")
    start = time.time()
    result = input1.copy()
    _ = quick_sort(result, input2, input3)
    elapsed = time.time() - start
    timeout = 1.00
    if elapsed < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
    print(f"Actual: {result}")
    assert elapsed < timeout
    assert result == expected_output
