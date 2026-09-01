#!/usr/bin/env python3

from main import Wizard

TestCase = tuple[str, int, int, int, int]

run_cases: list[TestCase] = [
    ("Merlin", 10, 10, 1000, 100),
    ("Morgana", 20, 5, 2000, 50),
]

submit_cases: list[TestCase] = run_cases + [
    ("Arthur", 3, 3, 300, 30),
]


def test(
    wizard_name: str,
    wizard_stamina: int,
    wizard_intelligence: int,
    expected_health: int,
    expected_mana: int,
) -> bool:
    print("---------------------------------")
    print("Creating wizard with:")
    wizard = Wizard(wizard_name, wizard_stamina, wizard_intelligence)
    print(f"  Name: {wizard.name}")
    print(f"  Stamina: {wizard_stamina}")
    print(f"  Intelligence: {wizard_intelligence}")
    print("After initialization:")
    print(f"  Expected mana: {expected_mana}")
    print(f"  Actual mana:   {wizard.mana}")
    print(f"  Expected health: {expected_health}")
    print(f"  Actual health:   {wizard.health}")
    if wizard.mana != expected_mana:
        return False
    if wizard.health != expected_health:
        return False
    is_private = True
    if hasattr(wizard, "stamina"):
        is_private = False
        print("Stamina isn't private!")
    if hasattr(wizard, "intelligence"):
        is_private = False
        print("Intelligence isn't private!")
    try:
        getattr(wizard, "_Wizard__stamina")
        getattr(wizard, "_Wizard__intelligence")
    except AttributeError:
        print("Attributes __stamina and __intelligence must exist!")
        return False

    return is_private


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
