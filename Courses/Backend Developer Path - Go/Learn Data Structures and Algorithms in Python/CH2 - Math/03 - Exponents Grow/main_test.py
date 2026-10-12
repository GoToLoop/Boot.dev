#!/usr/bin/env -S python3 -m pytest

import pytest
from main import get_follower_prediction

run_cases = [
    pytest.param(10, "fitness", 1, 40),
    pytest.param(10, "fitness", 2, 160),
    pytest.param(12, "cosmetic", 4, 972),
]

submit_cases = [
    pytest.param(15, "business", 4, 240, marks=pytest.mark.submit),
    pytest.param(10, "fitness", 5, 10240, marks=pytest.mark.submit),
    pytest.param(10, "fitness", 6, 40960, marks=pytest.mark.submit),
    pytest.param(10, "fitness", 7, 163840, marks=pytest.mark.submit),
    pytest.param(10, "fitness", 8, 655360, marks=pytest.mark.submit),
    pytest.param(10, "tech", 9, 5120, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("follower_count", "influencer_type", "num_months", "expected"),
    run_cases + submit_cases,
)
def test_get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int, expected: int
) -> None:
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * Follower count: {follower_count}")
    print(f" * Influencer type: {influencer_type}")
    print(f" * Number of months: {num_months}")
    print(f"Expected: {expected}")
    result = get_follower_prediction(follower_count, influencer_type, num_months)
    print(f"Actual:   {result}")
    assert result == expected
