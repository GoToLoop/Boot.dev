from collections.abc import MutableSequence

def bubble_sort[M: MutableSequence[int]](nums: M) -> M:
    active_length = len(nums)

    while active_length > 1:
        last_swap_index = 0

        for idx in range(1, active_length):
            if nums[idx - 1] > nums[idx]:
                nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
                last_swap_index = idx

        active_length = last_swap_index

    return nums
