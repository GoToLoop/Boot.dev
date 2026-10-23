#!/usr/bin/env -S python3 -m pytest

import pytest
from main import count_marketers

mark = pytest.mark.submit

run_cases = (
    (["developer", "marketer", "designer"], 1),
    (["marketer", "marketer", "developer", "marketer"], 3),
)

submit_cases = (
    pytest.param([], 0, marks=mark),
    pytest.param(["developer", "designer", "product manager"], 0, marks=mark),
    pytest.param(["marketer"], 1, marks=mark),
    pytest.param(["MARKETER", "Marketer", "marketer"], 3, marks=mark),
)

@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_count_marketers(input1: list[str], expected_output: int):
    print("\n---------------------------------")
    print(f"Input job titles: {input1}")
    print(f"Expected: {expected_output}")
    result = count_marketers(input1)
    print(f"Actual:   {result}")
    assert result == expected_output
