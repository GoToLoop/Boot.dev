#!/usr/bin/env python3

from main import BatteringRam, Wall

ExpectedAttributes = dict[str, int]
TestCase = tuple[type[object], ExpectedAttributes]

run_cases: list[TestCase] = [(Wall, {"armor": 10, "height": 5})]

submit_cases: list[TestCase] = run_cases + [
    (BatteringRam, {"damage": 2, "length": 4}),
]


def test(class_type: type[object], expected_attributes: ExpectedAttributes) -> bool:
    print("---------------------------------")
    print(f"Testing class: {class_type.__name__}")
    try:
        instance = class_type()
        passed = True

        for attr_name, expected_value in expected_attributes.items():
            if hasattr(instance, attr_name):
                actual_value = getattr(instance, attr_name)
                print(f"Expected {attr_name}: {expected_value}")
                print(f"Actual {attr_name}:   {actual_value}")
                if actual_value != expected_value:
                    passed = False
            else:
                print(f"Error: {attr_name} attribute not found")
                passed = False

        if passed:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
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
