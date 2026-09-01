#!/usr/bin/env python3

from typing import Callable
from collections.abc import Iterable, Sequence

Predicate = Callable[[int], bool]
Predicates = Iterable[Predicate]

Transform = Callable[[int], int]
Transforms = Sequence[Transform]

Pipeline = Callable[[Sequence[int]], list[int]]

def combine_predicates(predicates: Predicates) -> Predicate:
    pass


def build_pipeline(predicates: Predicates, transforms: Transforms) -> Pipeline:
    pass


if __name__ == "__main__":
    pass
