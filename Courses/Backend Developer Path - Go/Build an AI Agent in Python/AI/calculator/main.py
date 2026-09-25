#!/usr/bin/env python3

from sys import argv
from pkg.calculator import evaluate
from pkg.render import format_json_output

def main() -> None:
    if len(argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        exit(1)

    try:
        if ( result := evaluate(expression := ' '.join(argv[1:])) ) is not None:
            print(format_json_output(expression, result))
        else: print("Error: Expression is empty or contains only whitespace.")

    except ValueError as e: print("Error:", e); exit(1)


if __name__ == "__main__": main()
