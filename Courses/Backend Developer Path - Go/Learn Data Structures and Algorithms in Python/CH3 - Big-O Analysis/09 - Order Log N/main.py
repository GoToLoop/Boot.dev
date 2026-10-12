from collections.abc import Sequence

def binary_search(target: int, arr: Sequence[int]) -> bool:
    low_idx = 0; high_idx = len(arr) - 1

    while low_idx <= high_idx: 
        if (n := arr[mid_idx := low_idx + high_idx >> 1]) == target: return True

        if n < target: low_idx = mid_idx + 1
        else: high_idx = mid_idx - 1

    return False
