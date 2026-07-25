#!/usr/bin/env python3

from typing import TypedDict

from main import Wizard


class TestCase(TypedDict):
    wizard1_name: str
    wizard1_stamina: int
    wizard1_intelligence: int
    wizard2_name: str
    wizard2_stamina: int
    wizard2_intelligence: int
    fireball_cost: int
    fireball_damage: int
    expect_success: bool
    expected_wizard1_mana_after: int
    expected_wizard2_alive: bool


run_cases: list[TestCase] = [
    {
        "wizard1_name": "Merlin",
        "wizard1_stamina": 10,
        "wizard1_intelligence": 10,
        "wizard2_name": "Morgana",
        "wizard2_stamina": 8,
        "wizard2_intelligence": 8,
        "fireball_cost": 50,
        "fireball_damage": 30,
        "expect_success": True,
        "expected_wizard1_mana_after": 50,
        "expected_wizard2_alive": True,
    },
    {
        "wizard1_name": "Gandalf",
        "wizard1_stamina": 15,
        "wizard1_intelligence": 12,
        "wizard2_name": "Saruman",
        "wizard2_stamina": 10,
        "wizard2_intelligence": 9,
        "fireball_cost": 80,
        "fireball_damage": 50,
        "expect_success": True,
        "expected_wizard1_mana_after": 40,
        "expected_wizard2_alive": True,
    },
]

submit_cases: list[TestCase] = run_cases + [
    {
        "wizard1_name": "Harry",
        "wizard1_stamina": 5,
        "wizard1_intelligence": 1,
        "wizard2_name": "Voldemort",
        "wizard2_stamina": 2,
        "wizard2_intelligence": 15,
        "fireball_cost": 200,
        "fireball_damage": 400,
        "expect_success": False,
        "expected_wizard1_mana_after": 10,
        "expected_wizard2_alive": True,
    },
    {
        "wizard1_name": "Ron",
        "wizard1_stamina": 5,
        "wizard1_intelligence": 7,
        "wizard2_name": "Hermione",
        "wizard2_stamina": 2,
        "wizard2_intelligence": 15,
        "fireball_cost": 70,
        "fireball_damage": 400,
        "expect_success": True,
        "expected_wizard1_mana_after": 0,
        "expected_wizard2_alive": False,
    },
]


def test(case: TestCase) -> bool:
    print("---------------------------------")
    print(
        f"{case['wizard1_name']} (Stamina: {case['wizard1_stamina']}, Intelligence: {case['wizard1_intelligence']})"
    )
    wizard1 = Wizard(
        case["wizard1_name"], case["wizard1_stamina"], case["wizard1_intelligence"]
    )
    print(f"  Starting health: {wizard1.health}")
    print(f"  Starting mana:   {wizard1.mana}")

    wizard2 = Wizard(
        case["wizard2_name"], case["wizard2_stamina"], case["wizard2_intelligence"]
    )
    print(
        f"{case['wizard2_name']} (Stamina: {case['wizard2_stamina']}, Intelligence: {case['wizard2_intelligence']})"
    )
    print(f"  Starting health: {wizard2.health}")
    print(f"  Starting mana:   {wizard2.mana}")
    print("")

    try:
        wizard1.cast_fireball(wizard2, case["fireball_cost"], case["fireball_damage"])
        success = True
        print(f"{case['wizard1_name']} cast fireball at {case['wizard2_name']}...")
        print(f"  Fireball cost:   {case['fireball_cost']}")
        print(f"  Fireball damage: {case['fireball_damage']}")
        print("")
    except Exception as e:
        success = False
        print(f"Exception: {e}")

    wizard1_mana_after = wizard1.mana
    wizard2_alive_after = wizard2.is_alive()

    print(f"Expected cast success: {case['expect_success']}")
    print(f"Actual cast success:   {success}")
    print(
        f"Expected {case['wizard1_name']} mana after: {case['expected_wizard1_mana_after']}"
    )
    print(f"Actual {case['wizard1_name']} mana after:   {wizard1_mana_after}")
    print(
        f"Expected {case['wizard2_name']} alive after: {case['expected_wizard2_alive']}"
    )
    print(f"Actual {case['wizard2_name']} alive after:   {wizard2_alive_after}")

    if success != case["expect_success"]:
        return False
    if wizard1_mana_after != case["expected_wizard1_mana_after"]:
        return False
    if wizard2_alive_after != case["expected_wizard2_alive"]:
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
