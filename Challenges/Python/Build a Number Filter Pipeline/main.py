#!/usr/bin/env python3

from typing import Callable
from collections.abc import Iterable, Sequence

Predicate = Callable[[int], bool]
Predicates = Iterable[Predicate]

Transform = Callable[[int], int]
Transforms = Sequence[Transform]

Pipeline = Callable[[Sequence[int]], list[int]]

def combine_predicates(predicates: Predicates) -> Predicate:
    return lambda number: all(predicate(number) for predicate in predicates)


def build_pipeline(predicates: Predicates, transforms: Transforms) -> Pipeline:
    unified_check = combine_predicates(predicates)

    def pipeline(nums: Sequence[int]) -> list[int]:
        filtered = filter(unified_check, nums)
        for transform in transforms: filtered = map(transform, filtered)
        return list(filtered)

    return pipeline


if __name__ == "__main__":
    ########################################################################

    def is_even(n: int): return n & 1 == 0
    def is_positive(n: int): return n > 0
    def square(n: int): return n * n
    def triple(n: int): return 3 * n
    def increment(n: int): return n + 1

    ########################################################################

    check = combine_predicates((is_even, is_positive))

    print(check(4))   # True  (even and positive)
    print(check(-2))  # False (even but not positive)
    print(check(3))   # False (positive but not even)

    always_true = combine_predicates([])
    print(always_true(999))  # True

    ########################################################################

    numbers = 1, 2, 3, 4, -2
    pipeline = build_pipeline({ is_even, is_positive }, [square])

    print(pipeline(numbers))
    # [4, 16]
    # Explanation:
    # - `is_even` and `is_positive` keep only 2 and 4
    # - `square` turns 2 -> 4 and 4 -> 16
    # - Result is [4, 16]

    ########################################################################

    numbers = 0, -1, 2
    pipeline = build_pipeline([], (increment, triple))

    print(pipeline(numbers))
    # [3, 0, 9]
    # Explanation:
    # 0   -> (0 + 1) * 3 = 3
    # -1  -> (-1 + 1) * 3 = 0
    # 2   -> (2 + 1) * 3 = 9

    ########################################################################
