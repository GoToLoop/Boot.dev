#!/usr/bin/env python3

from collections.abc import Callable

def get_logger(format: Callable[[str, str], str]) -> Callable[[str, str], None]:
    return lambda s1, s2: print(format(s1, s2))

# Don't edit below this line

def test(first: str, errors: list[str], formatter: Callable[[str, str], str]):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first: str, second: str) -> str:
    return f"{first}: {second}"


def dash_delimit(first: str, second: str) -> str:
    return f"{first} - {second}"


def main():
    db_errors: list[str] = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors: list[str] = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


if __name__ == "__main__": main()
