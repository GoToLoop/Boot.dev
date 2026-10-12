#!/usr/bin/env -S python3 -m pytest

import pytest
from main import Influencer, vanity_sort

theprimeagen = Influencer(12, 1)
pokimane = Influencer(800, 2)
spambot = Influencer(0, 200)
lane = Influencer(10, 2)
badcop = Influencer(1, 2)

run_cases = [
    pytest.param([badcop, lane], [badcop, lane]),
    pytest.param([lane, badcop, pokimane], [badcop, lane, pokimane]),
    pytest.param([spambot, theprimeagen], [theprimeagen, spambot]),
]

submit_cases = [
    pytest.param([], [], marks=pytest.mark.submit),
    pytest.param([lane], [lane], marks=pytest.mark.submit),
    pytest.param(
        [pokimane, theprimeagen, spambot, badcop, lane],
        [badcop, theprimeagen, lane, pokimane, spambot],
        marks=pytest.mark.submit,
    ),
]

@pytest.mark.parametrize(("input1", "expected_output"), run_cases+submit_cases)
def test_vanity_sort(input1: list[Influencer], expected_output: int):
    print("\n---------------------------------")
    print(f"Input:\n * {input1}")
    print(f"Expected: {expected_output}")
    result = vanity_sort(input1)
    print(f"Actual:   {result}")
    assert result == expected_output
