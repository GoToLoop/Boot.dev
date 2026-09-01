#!/usr/bin/env python3

from main import add_prefix

TestCase = tuple[tuple[str, ...], tuple[str, ...]]

run_cases: list[TestCase] = [
    (
        ("hello there", "sonny", "how ya doing"),
        ("0. hello there", "1. sonny", "2. how ya doing"),
    )
]

submit_cases: list[TestCase] = run_cases + [
    (
        ("go", "python", "java", "javascript"),
        ("0. go", "1. python", "2. java", "3. javascript"),
    ),
    (
        ("boots", "everyone else"),
        ("0. boots", "1. everyone else"),
    ),
]


def test(input_docs: tuple[str, ...], expected: tuple[str, ...]) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * documents: {input_docs}")
    print(f"Expected: {expected}")
    documents: tuple[str, ...] = ()
    try:
        for doc in input_docs:
            documents = add_prefix(doc, documents)
    except Exception as e:
        result: tuple[str, ...] | str = f"Error: {e}"
    else:
        result = documents
    print(f"Actual: {result}")
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
