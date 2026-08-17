#!/usr/bin/env python3

from main import stylize_title

TestCase = tuple[str, str]

run_cases: list[TestCase] = [
    (
        """The Importance of FP
Learn how functional programming can change the way you think about code.
Benefits include immutability, simplicity, and composability.""",
        "          The Importance of FP          \n"
        "****************************************\n"
        "Learn how functional programming can change the way you think about code.\n"
        "Benefits include immutability, simplicity, and composability.",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        """Short Title
Equally short story""",
        "              Short Title               \n"
        "****************************************\n"
        "Equally short story",
    ),
    (
        """DocToDoc: A Guide
Understanding the art of document conversion.
We write cool functional code to make it happen.""",
        "           DocToDoc: A Guide            \n"
        "****************************************\n"
        "Understanding the art of document conversion.\n"
        "We write cool functional code to make it happen.",
    ),
]


def test(input_doc: str, expected: str) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * document: {input_doc}\n")
    print(f"Expected:\n{expected}\n")
    result = stylize_title(input_doc)
    print(f"Actual:\n{result}\n")
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
