class Solution:
    def networkDelayTime(self, times, n, k):
        adj = {}
        for u, v, t in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((v, t))

        heap = [(0, k)]
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            if node in adj:
                for nei, t in adj[node]:
                    if nei not in dist:
                        heapq.heappush(heap, (time + t, nei))

        if len(dist) != n:
            return -1
        return max(dist.values())
