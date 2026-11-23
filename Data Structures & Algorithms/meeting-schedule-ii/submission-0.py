"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        rooms = 0
        maxRooms = 0
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()

        s = e = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                rooms += 1
            elif ends[e] < starts[s]:
                e += 1
                rooms -= 1
            else:
                s += 1
                e += 1
            maxRooms = max(rooms, maxRooms)
            print(rooms)
        
        return maxRooms
