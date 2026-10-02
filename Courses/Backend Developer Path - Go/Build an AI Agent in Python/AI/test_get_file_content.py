#!/usr/bin/env python3

from functions.get_file_content import get_file_content, MAX_CHARS
from functions.partial import WORK_DIR

FILENAME = "lorem.txt"
CONTENT = "'%s' content:\n```\n%s\n```\n"
FILENAMES = "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"

def test():
    content = get_file_content(WORK_DIR, FILENAME)
    if truncated := 'truncated' in content: print(content[MAX_CHARS:])

    print(FILENAME, "length:", len(content))
    print(FILENAME, "truncated:", truncated, '\n')

    print(*(
        CONTENT % (filename, get_file_content(WORK_DIR, filename))
        for filename in FILENAMES
    ), sep='\n')


if __name__ == "__main__": test()
