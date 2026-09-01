#!/usr/bin/env python3

from main import Archer

ExpectedResult = list[tuple[int, int] | None]
TestCase = tuple[Archer, Archer, int, ExpectedResult, str | None]

run_cases: list[TestCase] = [
    (
        Archer("Robin", 6, 2),
        Archer("Sheriff", 3, 4),
        1,
        [(5, 1), (2, 3)],
        None,
    ),
    (
        Archer("Friar Tuck", 1, 0),
        Archer("Prince John", 1, 0),
        1,
        [None, None],
        "Friar Tuck can't shoot",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        Archer("Guy of Gisborne", 0, 1),
        Archer("Sheriff", 3, 2),
        1,
        [None, None],
        "Guy of Gisborne is dead",
    ),
    (
        Archer("Little John", 4, 4),
        Archer("Sheriff", 3, 2),
        4,
        [None, None],
        "Sheriff is dead",
    ),
]


def test(
    archer_1: Archer,
    archer_2: Archer,
    rounds: int,
    expected_result: ExpectedResult,
    expected_err: str | None,
) -> bool:
    print("---------------------------------")
    print("Initial Status:")
    archer_1.print_status()
    archer_2.print_status()
    try:
        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num}:")

            # First archer shoots
            print(f"* {archer_1.name}'s turn:")
            archer_1.shoot(archer_2)
            archer_2.print_status()

            # Second archer shoots
            print(f"* {archer_2.name}'s turn:")
            archer_2.shoot(archer_1)
            archer_1.print_status()

        print("\nFinal Status:")
        archer_1.print_status()
        archer_2.print_status()

        # Check for expected error
        if expected_err:
            print(
                f"\nTest Failed: Expected error '{expected_err}' but no exception was raised"
            )
            return False

        # Check results
        _, archer_1_health, archer_1_arrows = archer_1.get_status()
        _, archer_2_health, archer_2_arrows = archer_2.get_status()
        archer_1_expected = expected_result[0]
        archer_2_expected = expected_result[1]
        if archer_1_expected is None or archer_2_expected is None:
            print("\nTest Failed: expected results are missing")
            return False
        archer_1_expected_health, archer_1_expected_arrows = archer_1_expected
        archer_2_expected_health, archer_2_expected_arrows = archer_2_expected
        print("\nResults Check:")
        print(f"Expected {archer_1.name} health: {archer_1_expected_health}")
        print(f"Actual {archer_1.name} health:   {archer_1_health}")
        print(f"Expected {archer_1.name} arrows: {archer_1_expected_arrows}")
        print(f"Actual {archer_1.name} arrows:   {archer_1_arrows}")
        print(f"Expected {archer_2.name} health: {archer_2_expected_health}")
        print(f"Actual {archer_2.name} health:   {archer_2_health}")
        print(f"Expected {archer_2.name} arrows: {archer_2_expected_arrows}")
        print(f"Actual {archer_2.name} arrows:   {archer_2_arrows}")

        if (
            archer_1_health == archer_1_expected_health
            and archer_1_arrows == archer_1_expected_arrows
            and archer_2_health == archer_2_expected_health
            and archer_2_arrows == archer_2_expected_arrows
        ):
            print("Pass")
            return True
        else:
            print("Fail")
            return False

    except Exception as e:
        error_msg = str(e)
        print("")
        print(f"Expected exception: {expected_err}")
        print(f"Actual exception:   {error_msg}")

        if expected_err:
            if error_msg == expected_err:
                print("Pass")
                return True
            else:
                print("Fail")
                return False
        else:
            return False


def main() -> None:
    passed = 0
    failed = 0

    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTEST CASE #{i}")
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    skipped = len(submit_cases) - len(test_cases)
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
