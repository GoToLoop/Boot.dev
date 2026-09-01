#!/usr/bin/env python3

from main import pair_document_with_format

Unpaired = tuple[list[str], list[str]]
Paired = list[tuple[str, str]]
TestCase = tuple[Unpaired, Paired]

run_cases: list[TestCase] = [
    (
        (["Proposal", "Invoice", "Contract"], ["docx", "pdoof", "txt"]),
        [("Proposal", "docx"), ("Contract", "txt")],
    ),
    (
        (["Presentation", "Summary"], ["pptx", "docx"]),
        [("Presentation", "pptx"), ("Summary", "docx")],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (([], []), []),
    ((["Test", "Example"], ["ppt", "docx"]), [("Test", "ppt"), ("Example", "docx")]),
    (
        (
            ["Python Cheatsheet", "Java Cheatsheet", "Malware", "Golang Cheatsheet"],
            ["pdf", "docx", "trash", "docx"],
        ),
        [
            ("Python Cheatsheet", "pdf"),
            ("Java Cheatsheet", "docx"),
            ("Golang Cheatsheet", "docx"),
        ],
    ),
]


def test(input: Unpaired, expected: Paired) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * doc_names: {input[0]}")
    print(f" * doc_formats: {input[1]}")
    print(f"Expected: {expected}")
    try:
        result: Paired | str = pair_document_with_format(*input)
    except Exception as e:
        result = f"Error: {e}"
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
