#!/usr/bin/env -S python3 -m pytest

import pytest
from main import lines_with_sequence

run_cases = [
    (
        "#",
        3,
        """###
@##
$$$
###""",
        2,
    ),
    (
        "$",
        2,
        """$$$
$
***
@@@
$$
$$$""",
        3,
    ),
]

submit_cases = [
    pytest.param("%", 1, "", 0, marks=pytest.mark.submit),
    pytest.param(
        "*",
        3,
        """***
*
$$$$$$
xxx
****
***
***""",
        4,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        " ",
        1,
        """a a
bbb
 c""",
        2,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("char", "length", "doc", "expected"), run_cases + submit_cases
)
def test_lines_with_sequence(char: str, length: int, doc: str, expected: int) -> None:
    print("\n---------------------------------")
    print(f"Input char: {char}")
    print(f"Input length: {length}")
    print("Input doc:")
    print(doc)
    print(f"Expected: {expected}")
    num_lines = lines_with_sequence(char)(length)(doc)
    print(f"Actual:   {num_lines}")
    assert num_lines == expected
