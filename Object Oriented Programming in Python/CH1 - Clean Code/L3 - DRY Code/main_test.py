#!/usr/bin/env python3

from main import Soldier, Result, fight_soldiers, get_soldier_dps

TestCase = Soldier, Soldier, Result

run_cases: list[TestCase] = [
    (
        {"damage": 10, "attacks_per_second": 3},
        {"damage": 20, "attacks_per_second": 1},
        "soldier 1 wins",
    ),
    (
        {"damage": 50, "attacks_per_second": 1},
        {"damage": 50, "attacks_per_second": 2},
        "soldier 2 wins",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        {"damage": 1, "attacks_per_second": 1},
        {"damage": 2, "attacks_per_second": 1},
        "soldier 2 wins",
    ),
    (
        {"damage": 100, "attacks_per_second": 2},
        {"damage": 50, "attacks_per_second": 4},
        "both soldiers die",
    ),
]


def test(soldier_one: Soldier, soldier_two: Soldier, expected: str) -> bool:
    print("---------------------------------")
    print("Soldier one:")
    print(f"  damage: {soldier_one['damage']}")
    print(f"  attacks_per_second: {soldier_one['attacks_per_second']}")
    print("Soldier two:")
    print(f"  damage: {soldier_two['damage']}")
    print(f"  attacks_per_second: {soldier_two['attacks_per_second']}")
    print(f"Expected: {expected}")
    try:
        result = fight_soldiers(soldier_one, soldier_two)
        print(f"Actual:   {result}")
        if result != expected:
            print("Fail")
            return False
        actual_soldier_one_dps = get_soldier_dps(soldier_one)
        actual_soldier_two_dps = get_soldier_dps(soldier_two)
        expected_soldier_one_dps = (
            soldier_one["damage"] * soldier_one["attacks_per_second"]
        )
        expected_soldier_two_dps = (
            soldier_two["damage"] * soldier_two["attacks_per_second"]
        )
        if actual_soldier_one_dps != expected_soldier_one_dps:
            print(f"Expected soldier one dps: {expected_soldier_one_dps}")
            print(f"Actual soldier one dps:   {actual_soldier_one_dps}")
            return False
        if actual_soldier_two_dps != expected_soldier_two_dps:
            print(f"Expected soldier two dps: {expected_soldier_two_dps}")
            print(f"Actual soldier two dps:   {actual_soldier_two_dps}")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Error: {e}")
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
