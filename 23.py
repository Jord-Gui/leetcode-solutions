# Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_duplicate = 0
        duplicate = 1
        if len(nums) < 1:
            return len(nums)
        while duplicate < len(nums):
            if nums[non_duplicate] == nums[duplicate]:
                nums.pop(duplicate)
            else:
                duplicate += 1
                non_duplicate = duplicate - 1
        return len(nums)
