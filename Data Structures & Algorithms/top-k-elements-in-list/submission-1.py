class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        d = defaultdict(list)
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        sorteditems = sorted(d.items(), key=lambda item: item[1])
        for i in range(k):
            out.append(sorteditems[-1][0])
            sorteditems.remove(sorteditems[-1])
        return out