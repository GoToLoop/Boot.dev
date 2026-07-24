#!/usr/bin/env python3

from main import Wall

TestCase = tuple[Wall, list[int]]

run_cases: list[TestCase] = [(Wall(), [50, 100, 200])]

submit_cases: list[TestCase] = run_cases + [
    (Wall(), [50, 100, 200, 400, 800, 1600, 3200]),
]


def test(wall: Wall, expected_outputs: list[int]) -> bool:
    print("---------------------------------")
    actual_outputs: list[int] = []
    for _ in expected_outputs:
        cost = wall.get_cost()
        actual_outputs.append(cost)
        print(f"Wall cost: {cost}")
        wall.fortify()
        print("fortifying wall...")
    print(f"Expected: {expected_outputs}")
    print(f"Actual:   {actual_outputs}")

    if actual_outputs == expected_outputs:
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
