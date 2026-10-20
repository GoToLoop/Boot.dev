#!/usr/bin/env -S python3 -m pytest

import pytest
from main import fib

run_cases = (
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (10, 55),
    (20, 6765),
)

submit_cases = (
    pytest.param(0, 0, marks=pytest.mark.submit),
    pytest.param(40, 10_2334_155, marks=pytest.mark.submit),
    pytest.param(70, 190_392_490_709_135, marks=pytest.mark.submit),
    pytest.param(
        160,
        1_226_132_595_394_188_293_000_174_702_095_995,
        marks=pytest.mark.submit,
    ),
)


@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_fib(input1: int, expected_output: int):
    print("\n---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected:  {expected_output}")
    result = fib(input1)
    print(f"Actual: {result}")
    assert result == expected_output
