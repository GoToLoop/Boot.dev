#!/usr/bin/env python3

from logger import args_logger

def test(*args: object, **kwargs: object) -> None:
    args_logger(*args, **kwargs)
    print("========================================")


def main() -> None:
    print("--- Test 1: Mix of args & kwargs -------")
    test("Good", "riddance", date_str="01/01/2023")

    print("--- Test 2: Only kwargs ----------------")
    test(message="Hello World", to_delete="l")

    print("--- Test 3: Only args ------------------")
    test("two", "star-crossed", "lovers")

    print("--- Test 4: Mix of args & kwargs -------")
    test("hi", True, f_name="Lane", l_name="Wagner", age=28)


if __name__ == "__main__": main()
