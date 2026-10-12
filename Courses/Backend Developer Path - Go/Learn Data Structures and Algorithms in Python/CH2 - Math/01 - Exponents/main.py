from collections.abc import Sequence
from typing import cast

def get_estimated_spread(audiences_followers: Sequence[int]) -> float:
    if (num_followers := len(audiences_followers)) == 0: return 0
    spreaders_weight = cast(float, num_followers ** 1.2)
    return sum(audiences_followers) / num_followers * spreaders_weight
