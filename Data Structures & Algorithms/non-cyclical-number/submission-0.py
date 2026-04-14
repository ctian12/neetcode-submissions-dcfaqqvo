class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            digits = [int(digit) for digit in str(n)]
            total = 0
            for d in digits:
                total += d ** 2
            n = total
        return False