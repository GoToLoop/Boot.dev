#!/usr/bin/env python3

from functions.run_python_file import run_python_file

WORK_DIR = "calculator"
OUTPUT = "%s output:\n%s\n"

PYTHON_CALLS = (
    ("main.py",),
    ("main.py", "3 + 5"),
    ("tests.py",),
    ("../main.py",),
    ("nonexistent.py",),
    ("lorem.txt",)
)

def test():
    print(*(
        OUTPUT % (call, run_python_file(WORK_DIR, call[0], *call[1:]))
        for call in PYTHON_CALLS
    ), sep='\n')


if __name__ == "__main__": test()
