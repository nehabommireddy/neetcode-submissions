class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[0])

        prevEnd = intervals[0][1]
        overlaps = 0

        for i, j in intervals[1::]:
            if i >= prevEnd:
                prevEnd = j
            else:
                prevEnd = min(prevEnd, j)
                overlaps += 1
        
        return overlaps

        