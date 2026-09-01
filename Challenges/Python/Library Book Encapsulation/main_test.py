#!/usr/bin/env python3

from typing import cast

from main import LibraryBook


def reset_library_counters():
    LibraryBook.total_checkouts = 0
    LibraryBook.total_returns = 0


def fmt_actions(actions):
    lines = []
    for a in actions:
        if a[0] == "new":
            _, title, author, total = a
            lines.append(f"  - new: title={title!r}, author={author!r}, total_copies={total}")
        else:
            lines.append(f"  - {a[0]}")
    return "\n".join(lines)


def run_actions(actions):
    book = cast(LibraryBook, None)
    results = []
    for action in actions:
        if action[0] == "new":
            _, title, author, total = action
            book = LibraryBook(title, author, total)
        elif action[0] == "checkout":
            results.append(book.checkout())
        elif action[0] == "return":
            results.append(book.return_copy())
        elif action[0] == "status":
            results.append(book.get_status())
        elif action[0] == "available":
            results.append(book.get_available_copies())
        else:
            raise ValueError(f"unknown action: {action[0]}")
    return results


def test_case(name, actions, expected_results, expected_checkouts, expected_returns):
    reset_library_counters()
    print("---------------------------------")
    print(name)
    print("Input actions:")
    print(fmt_actions(actions))
    print("")

    try:
        actual_results = run_actions(actions)
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    actual_checkouts = LibraryBook.total_checkouts
    actual_returns = LibraryBook.total_returns

    print("Expected results:")
    print(f"  {expected_results}")
    print("Actual results:")
    print(f"  {actual_results}")
    print("")
    print(f"Expected class counters: checkouts={expected_checkouts}, returns={expected_returns}")
    print(f"Actual class counters:   checkouts={actual_checkouts}, returns={actual_returns}")

    if (
        actual_results == expected_results
        and actual_checkouts == expected_checkouts
        and actual_returns == expected_returns
    ):
        print("Pass")
        return True

    print("Fail")
    return False


run_cases = [
    (
        "Run: basic checkout and status",
        [
            ("new", "Dune", "Frank Herbert", 2),
            ("checkout",),
            ("status",),
            ("available",),
        ],
        [True, '"Dune" by Frank Herbert (1/2 available)', 1],
        1,
        0,
    ),
    (
        "Run: checkout fails when no copies left",
        [
            ("new", "The Hobbit", "J.R.R. Tolkien", 1),
            ("checkout",),
            ("checkout",),
            ("status",),
        ],
        [True, False, '"The Hobbit" by J.R.R. Tolkien (0/1 available)'],
        1,
        0,
    ),
    (
        "Run: return increments returns",
        [
            ("new", "Neuromancer", "William Gibson", 1),
            ("checkout",),
            ("return",),
            ("status",),
        ],
        [True, True, '"Neuromancer" by William Gibson (1/1 available)'],
        1,
        1,
    ),
]

submit_cases = run_cases + [
    (
        "Submit: zero-copy book behaves correctly",
        [
            ("new", "Rare Manuscript", "Unknown", 0),
            ("checkout",),
            ("return",),
            ("status",),
        ],
        [False, False, '"Rare Manuscript" by Unknown (0/0 available)'],
        0,
        0,
    ),
    (
        "Submit: multiple checkouts and returns",
        [
            ("new", "Foundation", "Isaac Asimov", 3),
            ("checkout",),
            ("checkout",),
            ("return",),
            ("checkout",),
            ("status",),
        ],
        [True, True, True, True, '"Foundation" by Isaac Asimov (1/3 available)'],
        3,
        1,
    ),
]


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for tc in test_cases:
        correct = test_case(*tc)
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
