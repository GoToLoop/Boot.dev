#!/usr/bin/env -S python3 -m pytest

import pytest
from main import does_name_exist

run_cases = [
    pytest.param(100, 100, "bob0 gonzalez0", True),
    pytest.param(500, 500, "maria1 smith1", True),
]

submit_cases = [
    pytest.param(1000, 1000, "bob500 smith1", False, marks=pytest.mark.submit),
    pytest.param(2000, 2000, "bob1999 wagner1998", False, marks=pytest.mark.submit),
    pytest.param(3000, 3000, "sally2999 smith2998", True, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("num_fnames", "num_lnames", "check_name", "expected_output"),
    run_cases + submit_cases,
)
def test_does_name_exist(num_fnames, num_lnames, check_name, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * num first_names: {num_fnames}")
    print(f" * num last_names: {num_lnames}")
    print(f" * looking for name: {check_name}")
    print(f"Expected: {expected_output}")
    fnames = get_first_names(num_fnames)
    lnames = get_last_names(num_lnames)
    result = does_name_exist(fnames, lnames, check_name)
    print(f"Actual:   {result}")
    assert result == expected_output


def get_first_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"bob{i}")
        elif m == 1:
            names.append(f"maria{i}")
        elif m == 2:
            names.append(f"sally{i}")
    return names


def get_last_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"gonzalez{i}")
        elif m == 1:
            names.append(f"smith{i}")
        elif m == 2:
            names.append(f"wagner{i}")
    return names
