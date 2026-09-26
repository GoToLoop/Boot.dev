#!/usr/bin/env python3

from functions.get_files_info import get_files_info

WORKING_FOLDER = "calculator"
RESULT = "Result for '%s' directory:\n%s\n"
FILENAMES = "pkg", "/bin", "../"

def test():
    print( "Result for current dir:\n" + get_files_info(WORKING_FOLDER) + '\n')

    print(*(
        RESULT % (filename, get_files_info(WORKING_FOLDER, filename))
        for filename in FILENAMES
    ), sep='\n')


if __name__ == "__main__": test()
