def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        j = i + 1

        while (j := j - 1) and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]

    return nums
