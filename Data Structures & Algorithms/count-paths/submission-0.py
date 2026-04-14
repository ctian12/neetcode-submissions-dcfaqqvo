class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for i in range(m)]

        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 or j == n - 1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dp(i + 1, j) + dp(i, j + 1)
            return memo[i][j]
        
        return dp(0, 0)
