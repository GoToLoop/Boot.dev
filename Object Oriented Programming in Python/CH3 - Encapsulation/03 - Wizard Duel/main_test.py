#!/usr/bin/env python3

from typing import TypedDict

from main import Wizard


class TestCase(TypedDict):
    wizard_name: str
    wizard_stamina: int
    wizard_intelligence: int
    fireball_damage: int
    potion_mana: int
    expected_health_after: int
    expected_mana_after: int


run_cases: list[TestCase] = [
    {
        "wizard_name": "Merlin",
        "wizard_stamina": 10,
        "wizard_intelligence": 10,
        "fireball_damage": 30,
        "potion_mana": 20,
        "expected_health_after": 980,
        "expected_mana_after": 130,
    },
    {
        "wizard_name": "Morgana",
        "wizard_stamina": 20,
        "wizard_intelligence": 5,
        "fireball_damage": 75,
        "potion_mana": 25,
        "expected_health_after": 1945,
        "expected_mana_after": 80,
    },
]

submit_cases: list[TestCase] = run_cases + [
    {
        "wizard_name": "Madame Mim",
        "wizard_stamina": 100,
        "wizard_intelligence": 500,
        "fireball_damage": 150,
        "potion_mana": 250,
        "expected_health_after": 9950,
        "expected_mana_after": 5750,
    },
]


def test(case: TestCase) -> bool:
    print("---------------------------------")
    print(
        f"Wizard({case['wizard_name']}, {case['wizard_stamina']}, {case['wizard_intelligence']})"
    )
    wizard = Wizard(
        case["wizard_name"], case["wizard_stamina"], case["wizard_intelligence"]
    )
    print(f"  Starting health: {wizard.health}")
    print(f"  Starting mana:   {wizard.mana}")
    print("")

    print(
        f"  Hit by a {case['fireball_damage']}-damage fireball while at {case['wizard_stamina']} stamina..."
    )
    print(
        f"  Drank a {case['potion_mana']}-mana potion while at {case['wizard_intelligence']} intelligence..."
    )
    wizard.get_fireballed(case["fireball_damage"])
    wizard.drink_mana_potion(case["potion_mana"])
    print("")

    print(f"  Expected health: {case['expected_health_after']}")
    print(f"  Actual health:   {wizard.health}")
    print(f"  Expected mana:   {case['expected_mana_after']}")
    print(f"  Actual mana:     {wizard.mana}")
    if wizard.health != case["expected_health_after"]:
        return False
    if wizard.mana != case["expected_mana_after"]:
        return False
    return True


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for case in test_cases:
        correct = test(case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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
