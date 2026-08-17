#!/usr/bin/env python3

from main import Article, Video, build_library_cards

run_cases = [
    ("article", ("Python Tips", "Mia"), "Article: Python Tips by Mia"),
    (
        "helper",
        [("article", "Python Tips", "Mia"), ("video", "Debugging 101", 12)],
        ["Article: Python Tips by Mia", "Video: Debugging 101 (12 min)"],
    ),
]

submit_cases = run_cases + [
    ("helper", [], []),
    ("video", ("CLI Basics", 5), "Video: CLI Basics (5 min)"),
    (
        "helper",
        [("video", "Loops", 7), ("article", "Clean Code", "Ivy"), ("video", "Testing", 9)],
        [
            "Video: Loops (7 min)",
            "Article: Clean Code by Ivy",
            "Video: Testing (9 min)",
        ],
    ),
]


def make_item(kind, value_one, value_two):
    if kind == "article":
        return Article(value_one, value_two)
    return Video(value_one, value_two)



def print_helper_input(items_data):
    if len(items_data) == 0:
        print("Input items: []")
        return
    print("Input items:")
    for item in items_data:
        kind, value_one, value_two = item
        if kind == "article":
            print(f"  - Article(title={value_one}, author={value_two})")
        else:
            print(f"  - Video(title={value_one}, minutes={value_two})")



def test(case_type, input_data, expected_output):
    print("---------------------------------")

    if case_type == "article":
        title, author = input_data
        print(f"Input: Article(title={title}, author={author})")
        result = make_item("article", title, author).card_text()
    elif case_type == "video":
        title, minutes = input_data
        print(f"Input: Video(title={title}, minutes={minutes})")
        result = make_item("video", title, minutes).card_text()
    else:
        print_helper_input(input_data)
        items = []
        for item in input_data:
            kind, value_one, value_two = item
            items.append(make_item(kind, value_one, value_two))
        result = build_library_cards(items)

    print("")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False



def main():
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



test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
