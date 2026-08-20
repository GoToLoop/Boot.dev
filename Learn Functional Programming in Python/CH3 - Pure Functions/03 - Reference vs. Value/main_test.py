#!/usr/bin/env python3

from collections.abc import Callable

from main import add_format, remove_format

Formats = dict[str, bool]
Formatter = Callable[[Formats, str], Formats]
TestCase = tuple[Formats, str, Formatter, str, Formats]

run_cases: list[TestCase] = [
    (
        {"docx": True, "pdf": True},
        "add_format",
        add_format,
        "txt",
        {"docx": True, "pdf": True, "txt": True},
    ),
    (
        {"md": True, "txt": False},
        "add_format",
        add_format,
        "ppt",
        {"md": True, "txt": False, "ppt": True},
    ),
    (
        {"md": True, "txt": False},
        "remove_format",
        remove_format,
        "md",
        {"md": False, "txt": False},
    ),
]

submit_cases: list[TestCase] = run_cases + [
    ({}, "add_format", add_format, "docx", {"docx": True}),
    (
        {"docx": True, "pdf": True, "txt": False},
        "remove_format",
        remove_format,
        "pdf",
        {"docx": True, "pdf": False, "txt": False},
    ),
    (
        {"docx": True, "pdf": True, "txt": False},
        "add_format",
        add_format,
        "jpg",
        {"docx": True, "pdf": True, "txt": False, "jpg": True},
    ),
    (
        {"docx": False, "pdf": True, "txt": True},
        "add_format",
        add_format,
        "docx",
        {"docx": True, "pdf": True, "txt": True},
    ),
]


def test(
    default_formats: Formats,
    formatter_name: str,
    formatter: Formatter,
    new_format: str,
    expected: Formats,
) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * default_formats: {default_formats}")
    print(f" * formatter: {formatter_name}")
    print(f" * new_format: {new_format}")
    print(f"Expected: {expected}")
    input1_copy = default_formats.copy()
    result = formatter(default_formats, new_format)
    print(f"Actual:   {result}")
    if result != expected:
        print("Fail")
        return False
    if default_formats != input1_copy:
        print("default_formats was mutated!")
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
