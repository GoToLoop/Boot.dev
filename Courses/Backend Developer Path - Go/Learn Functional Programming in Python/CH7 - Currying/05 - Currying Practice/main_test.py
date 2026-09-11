#!/usr/bin/env -S python3 -m pytest

import pytest
from main import new_resizer

Size = tuple[int, int]
ResizeCase = tuple[Size, Size]
MinSize = Size | tuple[()]

run_cases = [
    (
        (1920, 1080),
        (800, 600),
        [
            ((2560, 1440), (1920, 1080)),
            ((500, 400), (800, 600)),
            ((1600, 1000), (1600, 1000)),
            ((800, 600), (800, 600)),
            ((1920, 1080), (1920, 1080)),
        ],
        None,
    ),
    (
        (1200, 800),
        (1600, 800),
        [],
        "minimum size cannot exceed maximum size",
    ),
    (
        (1600, 800),
        (1200, 1200),
        [],
        "minimum size cannot exceed maximum size",
    ),
]

submit_cases = [
    pytest.param(
        (1600, 1200),
        (1200, 800),
        [
            ((1601, 799), (1600, 800)),
            ((1199, 1201), (1200, 1200)),
        ],
        None,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        (600, 600),
        (600, 600),
        [
            ((601, 601), (600, 600)),
            ((599, 599), (600, 600)),
        ],
        None,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        (100, 100),
        (),
        [
            ((200, 200), (100, 100)),
            ((0, 0), (0, 0)),
        ],
        None,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("max_size", "min_size", "sizes", "expected_err"), run_cases + submit_cases
)
def test_new_resizer(
    max_size: Size,
    min_size: MinSize,
    sizes: list[ResizeCase],
    expected_err: str | None,
) -> None:
    print("\n---------------------------------")
    print(f"Max Size:  {max_size}")
    if min_size:
        print(f"Min Size:  {min_size}")
    try:
        resize_image = new_resizer(*max_size)(*min_size)
    except Exception as error:
        print(f"Expected Error: {expected_err}")
        print(f"  Actual Error: {error}")
        assert str(error) == expected_err
        return
    if expected_err is not None:
        print(f"Expected Error: {expected_err}")
    assert expected_err is None
    print("Resizing Images...")
    results = []
    expected_sizes = []
    for input_size, expected_size in sizes:
        result = resize_image(*input_size)
        print(f" * Image Size: {input_size}")
        print(f" *   Expected: {expected_size}")
        print(f" *     Actual: {result}")
        results.append(result)
        expected_sizes.append(expected_size)
    assert results == expected_sizes
