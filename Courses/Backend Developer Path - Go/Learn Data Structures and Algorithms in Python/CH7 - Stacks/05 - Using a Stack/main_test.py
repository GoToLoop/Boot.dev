#!/usr/bin/env -S python3 -m pytest

import pytest
from main import is_balanced

mark = pytest.mark.submit

run_cases = (
    ("(", False),
    ("()", True),
    ("(())", True),
)

submit_cases = (
    pytest.param("()()", True, marks=mark),
    pytest.param("(()))", False, marks=mark),
    pytest.param("((())())", True, marks=mark),
    pytest.param("(()(()", False, marks=mark),
    pytest.param(")(", False, marks=mark),
    pytest.param(")()(()", False, marks=mark),
    pytest.param("())(()", False, marks=mark),
)

@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_is_balanced(input1: str, expected_output: bool):
    print("\n---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    result = is_balanced(input1)
    print(f"Actual:   {result}")
    assert result == expected_output
