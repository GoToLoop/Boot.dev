#!/usr/bin/env -S python3 -m pytest

import pytest
from main import letter_combinations

# input; output length; first 3 output strings; a string that should be present
run_cases: list[tuple[str, int, list[str], str]] = [
    ("", 0, [], ""),
    ("67", 12, ["mp", "mq", "mr"], "op"),
    ("43556", 243, ["gdjjm", "gdjjn", "gdjjo"], "hello"),
    ("2668338", 2187, ["ammtddt", "ammtddu", "ammtddv"], "bootdev"),
]

submit_cases = [
    pytest.param("420", 0, [], "ValueError", marks=pytest.mark.submit),
    pytest.param(
        "7878326",
        3888,
        ["ptptdam", "ptptdan", "ptptdao"],
        "rustfan",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "4568346",
        2187,
        ["gjmtdgm", "gjmtdgn", "gjmtdgo"],
        "ilovego",
        marks=pytest.mark.submit,
    ),
]

@pytest.mark.parametrize(
    ("digits", "expected_length", "expected_initial", "expected_contains"),
    run_cases + submit_cases,
)
def test_letter_combinations(
    digits: str,
    expected_length: int,
    expected_initial: list[str],
    expected_contains: str,
):
    print("\n---------------------------------")
    print(f"Input: '{digits}'")
    try:
        result = letter_combinations(digits)
        print(f"Expected combos: {expected_length}")
        actual_length = len(result)
        print(f"Actual combos:   {actual_length}")
        if expected_length == 0 and actual_length == expected_length:
            assert actual_length == expected_length
            return
        print(f"Expected initial combos: {expected_initial}")
        actual_initial = result[:3]
        print(f"Actual initial combos:   {actual_initial}")
        print(f"Expected to contain: '{expected_contains}'")
        actual_contains = expected_contains in result
        print(f"Actual contains '{expected_contains}'? {actual_contains}")
        assert actual_length == expected_length
        assert actual_initial == expected_initial
        assert actual_contains
    except ValueError as error:
        print(f"Caught ValueError: {error}")
        assert expected_length == 0
        assert expected_contains == "ValueError"
        print("Expected ValueError")
