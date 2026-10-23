#!/usr/bin/env -S python3 -m pytest

import pytest
from itertools import islice
from main import backoff_delays

submit = pytest.mark.submit

run_cases = (
    pytest.param(1, 5, [1, 2, 4, 8, 16]),
    pytest.param(3, 4, [3, 6, 12, 24])
)

submit_cases = (
    pytest.param(2, 8, [2, 4, 8, 16, 32, 64, 128, 256], marks=submit),
    pytest.param(10, 3, [10, 20, 40], marks=submit)
)

@pytest.mark.parametrize(
    ("base", "num_retries", "expected_delays"), run_cases + submit_cases
)
def test_backoff_delays(
    base: int, num_retries: int, expected_delays: list[int]
):
    print("\n---------------------------------")
    print(f"Base delay: {base}")
    print(f"Retries:    {num_retries}")
    print(f"\nExpected: {expected_delays}")

    result = list( islice(backoff_delays(base), num_retries) )

    print(f"Actual:   {result}")
    assert result == expected_delays
