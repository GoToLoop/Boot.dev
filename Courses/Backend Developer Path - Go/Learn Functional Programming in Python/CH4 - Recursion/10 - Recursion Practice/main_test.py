#!/usr/bin/env -S python3 -m pytest

import pytest
from main import count_nested_levels

NestedDocs = dict[int, "NestedDocs"]

run_cases = [
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 2, 2),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 9, 4),
]

submit_cases = [
    pytest.param({}, 1, -1, marks=pytest.mark.submit),
    pytest.param(
        {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}},
        5,
        4,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}},
        20,
        -1,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("docs", "target", "expected"), run_cases + submit_cases)
def test_count_nested_levels(docs: NestedDocs, target: int, expected: int) -> None:
    print("\n---------------------------------")
    print(f"Input tree: {docs}")
    print(f"Input document id: {target}")
    print(f"Expected: {expected}")
    result = count_nested_levels(docs, target)
    print(f"Actual:   {result}")
    assert result == expected
