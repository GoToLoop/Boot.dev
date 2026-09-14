#!/usr/bin/env -S python3 -m pytest

from collections.abc import Callable

import pytest
from main import Doctype

run_cases = [
    (lambda: Doctype.PDF, "Doctype.PDF", False),
    (lambda: Doctype.TXT, "Doctype.TXT", False),
    (lambda: Doctype.DOCX, "Doctype.DOCX", False),
    (lambda: Doctype.MD, "Doctype.MD", False),
]

submit_cases = [
    pytest.param(lambda: Doctype.HTML, "Doctype.HTML", False, marks=pytest.mark.submit),
    pytest.param(
        lambda: getattr(Doctype, "Invalid"),
        "Doctype.Invalid",
        True,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("func", "name", "is_err"), run_cases + submit_cases)
def test_doctype_value(func: Callable[[], object], name: str, is_err: bool) -> None:
    print("\n---------------------------------")
    print(f"Checking value: {name}")
    try:
        func()
    except Exception:
        print("...Invalid enum value!")
        assert is_err
    else:
        print("...Valid enum value!")
        assert not is_err
