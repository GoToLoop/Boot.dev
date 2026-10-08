#!/usr/bin/env python3

from functions.run_shebang_script import run_shebang_script
from functions.partial import WORK_DIR

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
        OUTPUT % (call, run_shebang_script(WORK_DIR, call[0], *call[1:]))
        for call in PYTHON_CALLS
    ), sep='\n')


if __name__ == "__main__": test()
