class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        out = []

        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            out.append([x, y])
        
        return out