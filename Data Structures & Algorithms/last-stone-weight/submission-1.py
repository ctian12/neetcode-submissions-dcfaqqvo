import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a < b:
                heapq.heappush(stones, a - b)
            elif a > b:
                heapq.heappush(stones, b - a)
        heapq.heappush(stones, 0)
        return abs(stones[0])