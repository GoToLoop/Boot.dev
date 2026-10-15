def quick_sort(nums: list[int], low: int, high: int) -> list[int]:
    if low >= high: return nums
    mid = partition(nums, low, high)
    return quick_sort( quick_sort(nums, low, mid - 1), mid + 1, high )
    

def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low

    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[high] = nums[i]
    nums[i] = pivot

    return i
