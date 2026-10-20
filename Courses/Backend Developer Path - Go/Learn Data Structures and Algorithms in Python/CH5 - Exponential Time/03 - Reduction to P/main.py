from functools import cache

@cache
def fib(n: int) -> int:
    if (n := abs(n)) < 2: return n
    a = b = 1
    for _ in range(n - 2): a, b = b, a + b
    return b
