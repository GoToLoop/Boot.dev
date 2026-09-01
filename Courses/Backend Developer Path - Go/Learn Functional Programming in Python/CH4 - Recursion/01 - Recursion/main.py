def factorial_r(x: int) -> int: return x * factorial_r(x - 1) if x > 1 else 1
