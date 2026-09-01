#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any

import main as student

Command = tuple[str, Callable[..., Any]]
CommandArgs = tuple[Any, ...]
TestCase = tuple[Command, Any, list[CommandArgs], Any]

run_cases: list[TestCase] = [
    (
        ("add_format", student.add_format),
        student.default_formats,
        [("rtf",), ("csv",)],
        ["txt", "md", "html", "rtf", "csv"],
    ),
    (
        ("save_document", student.save_document),
        student.saved_documents,
        [
            ("My_Princess_Diaries.txt", "I can't be a princess!"),
            (
                "The_Devil_Wears_Boots.md",
                "Please, bore someone else with your questions.",
            ),
        ],
        {
            "My_Princess_Diaries.txt": "I can't be a princess!",
            "The_Devil_Wears_Boots.md": "Please, bore someone else with your questions.",
        },
    ),
    (
        ("add_line_break", student.add_line_break),
        "It's not you, it's me.",
        [()],
        "It's not you, it's me.\n\n",
    ),
]


submit_cases: list[TestCase] = run_cases + [
    (
        ("add_format", student.add_format),
        student.default_formats,
        [
            ("doc",),
            ("docx",),
            ("pdf",),
        ],
        ["txt", "md", "html", "doc", "docx", "pdf"],
    ),
    (
        ("save_document", student.save_document),
        student.saved_documents,
        [
            ("Function_Club.txt", "The types you own end up owning you"),
            ("Shrek.doc", "Functions are like onions."),
        ],
        {
            "Function_Club.txt": "The types you own end up owning you",
            "Shrek.doc": "Functions are like onions.",
        },
    ),
    (
        ("add_line_break", student.add_line_break),
        "Go be free.",
        [()],
        "Go be free.\n\n",
    ),
]


def test(
    command: Command, initial: Any, command_calls: list[CommandArgs], expected: Any
) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * new command: {command[0]}")
    print(f" * starting input: {initial}")
    result = initial
    commands = student.default_commands
    initial_copy = initial.copy() if hasattr(initial, "copy") else initial
    default_commands_length = len(student.default_commands)

    # add and test new command
    commands = student.add_custom_command(commands, *command)
    for args in command_calls:
        if len(args) > 0:
            print(f" * input: {args}")
        result = commands[command[0]](result, *args)

    # check result
    print(f"Expected: '{expected}'")
    print(f"Actual:   '{result}'")
    if result == expected:
        # check inputs not mutated
        if initial == initial_copy:
            if len(student.default_commands) == default_commands_length:
                print("Pass")
                return True
            else:
                print("default_commands modified")
        else:
            print("Starting input modified")
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
