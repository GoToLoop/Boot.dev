#!/usr/bin/env python3

import main as main_

TestCase = tuple[str, str, str | None]

run_cases: list[TestCase] = [
    ("Proposal.docx", "pdf", "Proposal.pdf"),
    ("Invoice.txt", "md", "Invoice.md"),
]

submit_cases: list[TestCase] = run_cases + [
    ("Presentation.ppt", "pptx", "Presentation.pptx"),
    ("Intro.pptx", "jpeg", None),
    ("Summary.md", "txt", "Summary.txt"),
    ("Contract.pdf", "pdoof", None),
]


def mutate_globals() -> None:
    setattr(main_, "valid_extensions", ["docx", "txt", "pptx", "ppt", "md"])
    setattr(
        main_,
        "valid_conversions",
        {
            "docx": ["jpeg"],
            "pdf": ["docx", "txt", "md"],
            "txt": ["docx"],
            "ppt": ["pptx", "jpeg"],
            "md": ["png"],
            "jpeg": ["png"],
        },
    )


def test(name: str, ext: str, expected: str | None) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * filename: {name}")
    print(f" * target_format: {ext}")
    print(f"Expected: {expected}")
    result = main_.convert_file_format(name, ext)
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main() -> None:
    passed = 0
    failed = 0
    mutate_globals()
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
