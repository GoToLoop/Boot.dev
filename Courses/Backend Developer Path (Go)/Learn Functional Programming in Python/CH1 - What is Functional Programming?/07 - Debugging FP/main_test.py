#!/usr/bin/env python3

from main import format_line

TestCase = tuple[str, str]

run_cases: list[TestCase] = [
    (
        "You can't spell America without Erica",
        "YOU CAN'T SPELL AMERICA WITHOUT ERICA...",
    ),
    ("Friends don't lie.", "FRIENDS DON'T LIE..."),
    (" She's our friend and she's crazy!", "SHE'S OUR FRIEND AND SHE'S CRAZY!..."),
]

submit_cases: list[TestCase] = run_cases + [
    (" You're gonna slay 'em dead, Nance. ", "YOU'RE GONNA SLAY 'EM DEAD, NANCE..."),
]


def test(input_line: str, expected_output: str) -> bool:
    print("---------------------------------")
    print(f"Input: {input_line}")
    print(f"Expected: {expected_output}")
    result = format_line(input_line)
    print(f"Actual: {result}")
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
