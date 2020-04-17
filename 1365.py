# How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return_nums = [0 for _ in range(len(nums))]
        nums1 = sorted(nums)
        for i in range(len(return_nums)):
            return_nums[i] = nums1.index(nums[i])
        return return_nums
