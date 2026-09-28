# pyright: reportUnusedImport = hint

from collections.abc import Iterable
from functools import reduce
from operator import add

def summed(nums: Iterable[int]) -> int:
    # return sum(nums) # shortest
    # return reduce(add, nums, 0) # functional

    # procedural:
    total = 0
    for num in nums: total += num
    return total
