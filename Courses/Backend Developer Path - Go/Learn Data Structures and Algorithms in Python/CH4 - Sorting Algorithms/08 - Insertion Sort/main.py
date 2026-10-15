def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums
