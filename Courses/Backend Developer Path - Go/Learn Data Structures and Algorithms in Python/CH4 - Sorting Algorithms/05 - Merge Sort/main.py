from collections.abc import Sequence

def merge_sort(nums: Sequence[int]) -> list[int]:
    if (size := len(nums)) < 2: return list(nums)
    mid_idx = size >> 1
    return merge( merge_sort(nums[:mid_idx]), merge_sort(nums[mid_idx:]) )


def merge(a: Sequence[int], b: Sequence[int]) -> list[int]:
    merged: list[int] = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged += a[i:]
    merged += b[j:]

    return merged
