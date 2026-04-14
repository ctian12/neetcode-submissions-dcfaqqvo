class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        memo = [-1] * len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dp(i + 1), dp(i + 2) + nums[i])
            return memo[i]
        return dp(0)