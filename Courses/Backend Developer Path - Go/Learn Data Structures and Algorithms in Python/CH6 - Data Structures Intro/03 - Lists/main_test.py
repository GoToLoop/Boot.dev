#!/usr/bin/env -S python3 -m pytest

import pytest
from main import last_work_experience

run_cases = [
    (["Software Engineer", "Data Analyst", "Project Manager"], "Project Manager"),
    (["Intern", "Junior Developer"], "Junior Developer"),
]

submit_cases = [
    pytest.param([], None, marks=pytest.mark.submit),
    pytest.param(["CEO"], "CEO", marks=pytest.mark.submit),
    pytest.param(
        ["Cashier", "Supervisor", "Manager", "Director"],
        "Director",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_last_work_experience(input1: list[str], expected_output: str):
    print("\n---------------------------------")
    print(f"Input work experiences: {input1}")
    print(f"Expected output: {expected_output}")
    result = last_work_experience(input1)
    print(f"Actual output: {result}")
    assert result == expected_output
