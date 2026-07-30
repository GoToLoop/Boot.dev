#!/usr/bin/env python3

from main import Sword, SwordType

TestCase = tuple[Sword, Sword, str | None, str | None]

run_cases: list[TestCase] = [
    (Sword("bronze"), Sword("bronze"), "iron", None),
    (Sword("bronze"), Sword("iron"), None, "cannot craft"),
]

submit_cases: list[TestCase] = run_cases + [
    (Sword("steel"), Sword("steel"), None, "cannot craft"),
    (Sword("iron"), Sword("iron"), "steel", None),
    (Sword("bronze"), Sword("steel"), None, "cannot craft"),
]


def test(
    sword1: Sword[SwordType],
    sword2: Sword[SwordType],
    expected_result: str | None,
    expected_err: str | None,
) -> bool:
    try:
        print("---------------------------------")
        print(f"{sword1.sword_type} sword + {sword2.sword_type} sword...")
        result = sword1 + sword2

        if expected_err:
            print(f"Expected Exception: {expected_err}")
            print("Actual Exception:    None")
            return False

        print(f"Expected: {expected_result}")
        print(f"Actual:   {result.sword_type}")
        if result.sword_type != expected_result:
            return False

    except Exception as error:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception:   {error}")
        if expected_err != str(error):
            return False

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
