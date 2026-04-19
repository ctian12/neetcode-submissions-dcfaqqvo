from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        amount = 0
        for v in freq.values():
            if v == maxFreq:
                amount += 1
        
        out = (maxFreq - 1) * (n + 1)
        out += amount

        out = max(out, len(tasks))

        return out