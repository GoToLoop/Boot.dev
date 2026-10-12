# pyright: reportUnusedImport = hint

from math import factorial
from functools import cache, reduce
from operator import mul

@cache
def num_possible_orders(num_posts: int) -> int:
    # return factorial(num_posts)
    # return reduce(mul, range(2, num_posts + 1), 1)
    return num_posts > 1 and num_posts * num_possible_orders(num_posts-1) or 1
