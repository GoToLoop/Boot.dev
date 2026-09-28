from collections.abc import Collection
from functools import reduce
from sys import maxsize

def get_lowest(a: int, b: int) -> int: return a if a <= b else b

def find_minimum(nums: Collection[int]) -> int | None:
    if not nums: return None
    return reduce(get_lowest, nums, maxsize)
