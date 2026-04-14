class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        d = defaultdict(list)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        for i, j in d.items():
            freq[j].append(i)
        count = 0
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                out.append(n)
                count += 1
                if count >= k:
                    return out