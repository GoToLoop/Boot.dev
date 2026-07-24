#!/usr/bin/env python3

from typing import Iterable
from numbers import Complex

from main import destroy_walls_complex

TestCase = list[Complex], list[Complex]

run_cases = (
    ([0, 20, 1 + 30j], [20, 1 + 30j]),
    ([10, 0, 40, -10], [10, 40]),
)

submit_cases: tuple[TestCase] = run_cases + (
    ([], []),
    ([3, 2, 0, 3, 0, 0], [3, 2, 3]),
)


def test(wall_healths: Iterable[Complex], expected: list[Complex]) -> bool:
    print("---------------------------------")
    print(f"Input:    {wall_healths}")
    print(f"Expected: {expected}")
    try:
        result = destroy_walls_complex(wall_healths)
        print(f"Actual:   {result}")
        if str(result) != str(expected):
            return False
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: tuple[TestCase] = submit_cases

if "__RUN__" in globals():
    test_cases = run_cases

main()
