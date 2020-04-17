# Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        else:
            value_dp = [0 for _ in range(size)]
            value_dp[0] = nums[0]
            for i in range(1, size):
                value_dp[i] = max(nums[i], value_dp[i-1] + nums[i])
            return max(value_dp)
