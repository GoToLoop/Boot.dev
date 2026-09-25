#!/usr/bin/env python3

from functions.get_files_info import get_files_info

RESULT = "Result for '%s' directory:\n%s\n"

def test():
    print( "Result for current dir:\n" + get_files_info("calculator") + '\n')
    print( RESULT % ("pkg", get_files_info("calculator", "pkg")) )
    print( RESULT % ("/bin", get_files_info("calculator", "/bin")) )
    print( RESULT % ("../", get_files_info("calculator", "../")) )


if __name__ == "__main__": test()
