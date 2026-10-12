#!/usr/bin/env -S python3 -m pytest

import time

import pytest
from main import binary_search

run_cases = [
    pytest.param(10, [i for i in range(200)], True),
    pytest.param(-1, [i for i in range(20000)], False),
]

submit_cases = [
    pytest.param(15, [], False, marks=pytest.mark.submit),
    pytest.param(0, [0], True, marks=pytest.mark.submit),
    pytest.param(-1, [-2, -1], True, marks=pytest.mark.submit),
    pytest.param(105028, [i for i in range(2000000)], True, marks=pytest.mark.submit),
    pytest.param(
        2000001,
        [i for i in range(2000000)],
        False,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("target", "arr", "expected_output"), run_cases + submit_cases)
def test_binary_search(target: int, arr: list[int], expected_output: int):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * target: {target}")
    print(f" * arr length: {len(arr)} items")
    print(f"Expected:  {expected_output} & completed in less than 50 milliseconds")
    start = time.time()
    result = binary_search(target, arr)
    elapsed = time.time() - start
    timeout = 0.05
    if elapsed < timeout:
        print(f"binary_search completed in less than {timeout * 1000} milliseconds!")
    else:
        print(
            f"binary_search took too long ({elapsed * 1000} milliseconds). Speed it up!"
        )
    print(f"Actual: {result}")
    assert elapsed < timeout
    assert result == expected_output
