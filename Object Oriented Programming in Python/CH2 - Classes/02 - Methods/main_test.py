#!/usr/bin/env python3

from main import Wall

TestCase = tuple[int, int, int]

run_cases: list[TestCase] = [
    (10, 5, 20),
    (20, 5, 40),
]

submit_cases: list[TestCase] = run_cases + [
    (320, 5, 640),
    (640, 5, 1280),
]


def test(armor: int, height: int, expected: int) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * armor:  {armor}")
    print(f" * height: {height}")
    print(f"Expected: {expected}")
    wall = Wall()
    wall.armor = armor
    wall.height = height
    wall.fortify()
    result = wall.armor
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
