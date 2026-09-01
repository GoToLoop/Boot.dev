#!/usr/bin/env python3

from main import format_menu

run_cases = [
    ({"Burger": 5, "Fries": 3}, "Burger - $5\nFries - $3"),
    ({}, ""),
    ({"Tea": 2}, "Tea - $2"),
]

submit_cases = run_cases + [
    ({"Soda": 1, "Popcorn": 4, "Candy": 2}, "Soda - $1\nPopcorn - $4\nCandy - $2"),
    ({"Apple": 1, "Banana": 1, "Cherry": 3}, "Apple - $1\nBanana - $1\nCherry - $3"),
    ({"Noodles": 7, "Soup": 5, " Salad": 4, "Dessert": 6}, "Noodles - $7\nSoup - $5\n Salad - $4\nDessert - $6"),
]


def show_menu_input(menu):
    if not menu:
        return "  (empty)"
    lines = []
    for k in menu:
        lines.append(f"  - {k}: {menu[k]}")
    return "\n".join(lines)


def test(input1, expected_output):
    print("---------------------------------")
    print("Input menu:")
    print(show_menu_input(input1))
    print("")
    result = format_menu(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


essage = "============= PASS =============="
failure = "============= FAIL =============="

def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print(essage)
    else:
        print(failure)
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
