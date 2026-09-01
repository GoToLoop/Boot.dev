#!/usr/bin/env python3

from main import combine_predicates, build_pipeline


def is_even(n):
    return n % 2 == 0


def is_positive(n):
    return n > 0


def is_negative(n):
    return n < 0


def square(n):
    return n * n


def increment(n):
    return n + 1


def triple(n):
    return n * 3


run_cases = [
    (
        "combine",
        [is_even, is_positive],
        [-2, -1, 0, 1, 2],
        [],
        [False, False, False, False, True],
    ),
    (
        "pipeline",
        [is_even, is_positive],
        [1, 2, 3, 4, -2],
        [square],
        [4, 16],
    ),
]

submit_cases = run_cases + [
    (
        "combine",
        [is_negative],
        [5, 0, -1, -10],
        [],
        [False, False, True, True],
    ),
    (
        "pipeline",
        [],
        [0, -1, 2],
        [increment, triple],
        [3, 0, 9],
    ),
    (
        "pipeline",
        [is_even],
        [2, 4, 5, 7],
        [],
        [2, 4],
    ),
]


def test(mode, predicates, numbers, transforms, expected_output):
    print("---------------------------------")
    if mode == "combine":
        print("Mode: combine_predicates")
        print("Input predicates:", [p.__name__ for p in predicates])
        print("Input values:", numbers)
        combined = combine_predicates(predicates)
        result = []
        for value in numbers:
            result.append(combined(value))
        print("Expected:", expected_output)
        print("Actual:  ", result)
        if result == expected_output:
            return True
        return False

    if mode == "pipeline":
        print("Mode: build_pipeline")
        print("Input predicates:", [p.__name__ for p in predicates])
        print("Input transforms:", [t.__name__ for t in transforms])
        print("Input numbers:", numbers)
        original_copy = list(numbers)
        pipeline = build_pipeline(predicates, transforms)
        result = pipeline(numbers)
        print("Expected:", expected_output)
        print("Actual:  ", result)
        if numbers != original_copy:
            print("FAIL: input list was mutated")
            return False
        if result == expected_output:
            return True
        return False

    print("Unknown mode", mode)
    return False


def main():
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
