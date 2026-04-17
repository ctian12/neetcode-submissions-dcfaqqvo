class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        l, r = 1, high

        while l < r:
            m = (l + r) // 2
            if self.canEat(piles, m, h):
                r = m
            else:
                l = m + 1
        
        return l

    def canEat(self, piles: List[int], rate: int, h: int) -> bool:
        time = sum(math.ceil(pile / rate) for pile in piles)
        return time <= h
