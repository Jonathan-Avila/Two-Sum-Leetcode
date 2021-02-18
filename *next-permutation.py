
def nextPermutation(self, nums: List[int], index = -2) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    elif nums == nums.sort():
        nums = nums.reverse()
        return
    else:
        if nums[index:] == nums[index:].sort():
            return nextPermutation(self, nums, index - 1)
        sub_array = nums[index:]
        temp = sub_array[-1]
        for index in range(len(sub_array)-1,-1,-1):
            sub_array[index] = sub_array[index - 1]
        sub_array[0] = temp
        nums[index:] = sub_array
        return
