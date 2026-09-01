#!/usr/bin/env python3

from main import factorial_r

TestCase = tuple[int, int]

run_cases: list[TestCase] = [
    (3, 6),
    (5, 120),
    (0, 1),
]

submit_cases: list[TestCase] = run_cases + [
    (1, 1),
    (2, 2),
    (10, 3628800),
]


def test(n: int, expected: int) -> bool:
    print("---------------------------------")
    print(f"Input: {n}")
    print(f"Expected: {expected}")
    result = factorial_r(n)
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


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
