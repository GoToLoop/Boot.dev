from math import log
from collections.abc import Iterable

def log_scale(data: Iterable[float], base: float) -> list[float]:
    return [ log(n, base) for n in data ]
