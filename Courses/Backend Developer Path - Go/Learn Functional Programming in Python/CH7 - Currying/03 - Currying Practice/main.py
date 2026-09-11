from collections.abc import Callable
from functools import reduce

def lines_with_sequence(char: str) -> Callable[[int], Callable[[str], int]]:
    def with_char(length: int) -> Callable[[str], int]:
        sequence = char * length

        return lambda doc: reduce(
            lambda count, line: count + (sequence in line),
            doc.split('\n'), 0
        )

    return with_char
