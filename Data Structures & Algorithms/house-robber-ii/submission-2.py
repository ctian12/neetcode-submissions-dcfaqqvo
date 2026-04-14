class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [-1] * n
        memo2 = [-1] * n

        def dfsSkipLast(i):
            if i >= n - 1:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dfsSkipLast(i + 2), dfsSkipLast(i + 1))
            return memo[i]
        
        def dfsSkipFirst(i):
            if i >= n:
                return 0
            if memo2[i] != -1:
                return memo2[i]
            memo2[i] = max(nums[i] + dfsSkipFirst(i + 2), dfsSkipFirst(i + 1))
            return memo2[i]
        
        return max(dfsSkipLast(0), dfsSkipFirst(1))