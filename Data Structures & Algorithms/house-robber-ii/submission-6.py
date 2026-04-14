class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        dp2 = [-1] * n
        dp2[1] = nums[1]
        if len(nums) == 2:
            return max(nums)
        else:
            dp2[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])

        return max(dp[n - 2], dp2[n - 1])