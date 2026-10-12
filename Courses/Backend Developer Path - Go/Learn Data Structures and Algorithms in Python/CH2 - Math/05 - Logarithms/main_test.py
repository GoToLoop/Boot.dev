#!/usr/bin/env -S python3 -m pytest

import pytest
from main import get_influencer_score

run_cases = [
    pytest.param(40000, 0.3, 5),
    pytest.param(43000, 0.1, 2),
    pytest.param(100000, 0.6, 10),
]

submit_cases = [
    pytest.param(1, 1, 0, marks=pytest.mark.submit),
    pytest.param(200, 0.8, 6, marks=pytest.mark.submit),
    pytest.param(300000, 0.5, 9, marks=pytest.mark.submit),
    pytest.param(500000, 0.2, 4, marks=pytest.mark.submit),
    pytest.param(750000, 0.7, 14, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_get_influencer_score(input1, input2, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * num_followers: {input1}")
    print(f" * average_engagement_percentage: {input2}")
    result = round(get_influencer_score(input1, input2))
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
