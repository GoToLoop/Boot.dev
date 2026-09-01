#!/usr/bin/env python3

from main import word_count_memo

Memos = dict[str, int]
Output = tuple[int, Memos]
TestCase = tuple[str, Memos, Output]

run_cases: list[TestCase] = [
    (
        "My hovercraft is full of eels",
        {
            "My hovercraft is full of eels": 6,
            "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
        },
        (
            6,
            {
                "My hovercraft is full of eels": 6,
                "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
            },
        ),
    ),
    (
        "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam",
        {},
        (
            12,
            {
                "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam": 12
            },
        ),
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        "This is an ex-parrot",
        {"This parrot is no more": 5},
        (4, {"This parrot is no more": 5, "This is an ex-parrot": 4}),
    ),
    (
        "This doc should 'incorrectly' have 9999 words to test that the memoization is working",
        {
            "My hovercraft is full of eels": 6,
            "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
        },
        (
            9999,
            {
                "My hovercraft is full of eels": 6,
                "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
            },
        ),
    ),
]


def test(input_doc: str, input_memos: Memos, expected: Output) -> bool:
    print("---------------------------------")
    print(f"Input document:\n  {input_doc}")
    print("Input memos:")
    for key, value in input_memos.items():
        print(f"  {key}: {value}")
    print(f"Expected word count: {expected[0]}")
    print("Expected memos:")
    for key, value in expected[1].items():
        print(f"  {key}: {value}")
    input_memos_copy = input_memos.copy()
    result = word_count_memo(input_doc, input_memos_copy)
    print(f"Actual word count: {result[0]}")
    print("Actual memos:")
    for key, value in result[1].items():
        print(f"  {key}: {value}")

    if input_memos_copy != input_memos:
        print("Mutated input memos\nFail")
        return False
    if input_memos == expected[1] and result[1] != expected[1]:
        print("Expected word count from the input memos\nFail")
        return False
    if result != expected:
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
