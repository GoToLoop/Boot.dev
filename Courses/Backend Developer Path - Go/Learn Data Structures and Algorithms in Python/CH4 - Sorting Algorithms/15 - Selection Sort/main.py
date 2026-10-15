def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        low = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[low]: low = j

        nums[i], nums[low] = nums[low], nums[i]

    return nums
