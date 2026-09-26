#!/usr/bin/env python3

from functions.write_file import write_file

WORKING_FOLDER = "calculator"
FEEDBACK = "'%s' feedback:\n%s\n"

FILE_CONTENTS = (
    ("lorem.txt", "wait, this isn't lorem ipsum"),
    ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("/tmp/temp.txt", "this should not be allowed")
)

def test():
    print(*(
        FEEDBACK % (filename, write_file(WORKING_FOLDER, filename, content))
        for filename, content in FILE_CONTENTS
    ), sep='\n')


if __name__ == "__main__": test()
