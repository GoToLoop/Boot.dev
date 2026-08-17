#!/usr/bin/env python3

from typing import Any

from main import hex_to_rgb

RGB = tuple[int, int, int]
TestCase = tuple[Any, RGB | None] | tuple[Any, RGB | None, str]

run_cases: list[TestCase] = [
    (
        "00FFFF",
        (0, 255, 255),
    ),
    (
        "FFFF00",
        (255, 255, 0),
    ),
    (
        "Hello!",
        None,
        "not a hex color string",
    ),
    (
        "42",
        None,
        "not a hex color string",
    ),
    (
        1_000_000,
        None,
        "not a hex color string",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        "",
        None,
        "not a hex color string",
    ),
    (
        "FF00FF00",
        None,
        "not a hex color string",
    ),
    (
        "FF00FF",
        (255, 0, 255),
    ),
    (
        "000000",
        (0, 0, 0),
    ),
    (
        "FFFFFF",
        (255, 255, 255),
    ),
]


def test(
    input_hex: Any, expected_output: RGB | None, expected_err: str | None = None
) -> bool:
    print("---------------------------------")
    print(f"  Inputs: '{input_hex}'")
    try:
        result = hex_to_rgb(input_hex)
    except Exception as e:
        print(f"Expected Error: {expected_err}")
        print(f"  Actual Error: {str(e)}")
        if str(e) != expected_err:
            print("Fail")
            return False
        print("Pass")
        return True

    if expected_err is not None:
        print(f"Expected Error: {expected_err}")
        print(f"        Actual: {result} (no error thrown)")
        print("Fail")
        return False

    print(f"Expected: {expected_output}")
    print(f"  Actual: {result}")
    if result != expected_output:
        print("Fail")
        return False
    print("Pass")
    return True


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
