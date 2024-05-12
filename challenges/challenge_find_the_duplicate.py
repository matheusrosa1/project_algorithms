def find_duplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if not isinstance(nums[i], int):
            return False
        if nums[i] < 1:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False


nums = [-1, -1]
print(find_duplicate(nums))
