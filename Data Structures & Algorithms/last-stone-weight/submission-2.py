class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = stones
        heapq.heapify_max(h)
        while len(h) > 1:
            a = heapq.heappop_max(h)
            b = heapq.heappop_max(h)
            remaining = abs(a - b)
            if remaining > 0:
                heapq.heappush_max(h, remaining)
        
        if len(h) > 0:
            return h[0]
        else:
            return 0