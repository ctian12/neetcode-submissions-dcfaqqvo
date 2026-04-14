class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxDiff = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            maxDiff = max(maxDiff, diff)

            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return maxDiff
