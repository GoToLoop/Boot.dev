#!/usr/bin/env python3

from main import sort_dates

TestCase = tuple[list[str], list[str]]

run_cases: list[TestCase] = [
    (
        [
            "07-21-2023",
            "12-25-2022",
            "01-01-2023",
            "01-15-2023",
            "10-31-2023",
            "04-10-2023",
        ],
        [
            "12-25-2022",
            "01-01-2023",
            "01-15-2023",
            "04-10-2023",
            "07-21-2023",
            "10-31-2023",
        ],
    ),
    (
        [
            "08-17-2023",
            "11-05-2022",
            "02-28-2023",
            "06-30-2023",
            "09-19-2024",
            "05-22-2023",
        ],
        [
            "11-05-2022",
            "02-28-2023",
            "05-22-2023",
            "06-30-2023",
            "08-17-2023",
            "09-19-2024",
        ],
    ),
    (
        [
            "07-04-2023",
            "12-01-2024",
            "01-20-2023",
            "03-10-2023",
            "10-05-2023",
            "04-25-2023",
        ],
        [
            "01-20-2023",
            "03-10-2023",
            "04-25-2023",
            "07-04-2023",
            "10-05-2023",
            "12-01-2024",
        ],
    ),
    (
        [
            "08-12-2023",
            "11-15-2022",
            "02-10-2023",
            "06-25-2023",
            "09-05-2023",
            "05-05-2023",
        ],
        [
            "11-15-2022",
            "02-10-2023",
            "05-05-2023",
            "06-25-2023",
            "08-12-2023",
            "09-05-2023",
        ],
    ),
    (
        [
            "07-15-2024",
            "12-18-2022",
            "03-30-2023",
            "03-20-2023",
            "10-20-2023",
            "04-05-2023",
        ],
        [
            "12-18-2022",
            "03-20-2023",
            "03-30-2023",
            "04-05-2023",
            "10-20-2023",
            "07-15-2024",
        ],
    ),
]


submit_cases: list[TestCase] = run_cases + [
    (
        [
            "08-22-2023",
            "11-30-2022",
            "02-05-2023",
            "06-10-2023",
            "09-25-2023",
            "05-10-2023",
        ],
        [
            "11-30-2022",
            "02-05-2023",
            "05-10-2023",
            "06-10-2023",
            "08-22-2023",
            "09-25-2023",
        ],
    ),
    (
        [
            "07-10-2024",
            "12-10-2022",
            "01-25-2023",
            "03-05-2023",
            "10-15-2023",
            "04-15-2023",
        ],
        [
            "12-10-2022",
            "01-25-2023",
            "03-05-2023",
            "04-15-2023",
            "10-15-2023",
            "07-10-2024",
        ],
    ),
    (
        [
            "08-02-2023",
            "11-25-2022",
            "02-15-2024",
            "06-05-2023",
            "09-10-2023",
            "05-01-2023",
        ],
        [
            "11-25-2022",
            "05-01-2023",
            "06-05-2023",
            "08-02-2023",
            "09-10-2023",
            "02-15-2024",
        ],
    ),
]


def test(unsorted: list[str], expected: list[str]) -> bool:
    print("---------------------------------")
    print(f"Input: {unsorted}")
    print(f"Expected: {expected}")
    unsorted_copy = unsorted.copy()
    result = sort_dates(unsorted)
    print(f"  Actual: {result}")
    if result != expected:
        print("Fail")
        return False
    if unsorted != unsorted_copy:
        print("Input list was mutated")
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
