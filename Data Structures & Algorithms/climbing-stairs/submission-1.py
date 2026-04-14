class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        for i in range(n-1):
            temp = second
            second = first + second
            first = temp
        
        return second