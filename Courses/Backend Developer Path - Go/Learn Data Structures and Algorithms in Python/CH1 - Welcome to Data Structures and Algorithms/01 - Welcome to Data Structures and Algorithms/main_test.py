#!/usr/bin/env -S python3 -m pytest

import pytest
from main import add

run_cases = [
    pytest.param(2, 3, 5),
    pytest.param(100, 250, 350),
]

submit_cases = [
    pytest.param(0, 0, 0, marks=pytest.mark.submit),
    pytest.param(-5, 5, 0, marks=pytest.mark.submit),
    pytest.param(123456, 654321, 777777, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("a", "b", "expected_output"), run_cases+submit_cases)
def test_add(a: int, b: int, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: a={a}, b={b}")
    result = add(a, b)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
