class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            memo[amount] = 1 + min(dfs(amount - c) for c in coins)
            return memo[amount]

        

        out = dfs(amount)
        if out == float('inf'):
            out = -1
        return out