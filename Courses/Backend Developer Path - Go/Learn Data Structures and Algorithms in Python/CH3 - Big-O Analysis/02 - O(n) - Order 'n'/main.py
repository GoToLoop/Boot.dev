from collections.abc import Iterable
from functools import reduce

def get_greatest(a: int, b: int) -> int: return a if a >= b else b

def find_max(nums: Iterable[int]) -> int: return reduce(get_greatest, nums)
