"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        s = 0
        e = 0
        count = 0
        start.sort()
        end.sort()
        max_val = 0
        while s < len(intervals) and e < len(intervals):
            if start[s] < end[e]:
                s+= 1
                count += 1
            else:
                count -= 1
                e += 1
            max_val = max(max_val, count)
        
        return max_val
        