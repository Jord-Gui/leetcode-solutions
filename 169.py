# Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        ret_val = None
        for key in count:
            if count[key] > len(nums)//2:
                ret_val = key
        return ret_val