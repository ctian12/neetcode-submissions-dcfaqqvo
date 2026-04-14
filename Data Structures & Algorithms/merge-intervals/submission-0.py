class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        out = [intervals[0]]

        for start, end in intervals:
            currEnd = out[-1][1]
            if start <= currEnd:
                out[-1][1] = max(currEnd, end)
            else:
                out.append([start, end])
        
        return out