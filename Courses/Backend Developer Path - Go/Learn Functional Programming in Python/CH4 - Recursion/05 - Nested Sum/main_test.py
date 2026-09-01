#!/usr/bin/env python3

from main import sum_nested_list

NestedList = list[int | list]
TestCase = tuple[NestedList, int]

run_cases: list[TestCase] = [
    ([1, 2, [3, 4]], 10),
    ([5, [6, 7], [[8, 9], 10]], 45),
]

submit_cases: list[TestCase] = run_cases + [
    ([], 0),
    ([1, [2], [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]], 55),
]


def test(input_list: NestedList, expected: int) -> bool:
    print("---------------------------------")
    print(f"Input list: {input_list}")
    print(f"Expected output: {expected}")
    result = sum_nested_list(input_list)
    print(f"Actual output: {result}")
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
