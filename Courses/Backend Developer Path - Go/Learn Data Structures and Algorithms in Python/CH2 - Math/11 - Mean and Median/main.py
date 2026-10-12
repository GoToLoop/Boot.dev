from collections.abc import Sequence

def average_followers(nums: Sequence[int]) -> float | None:
    return sum(nums) / len(nums) if nums else None
