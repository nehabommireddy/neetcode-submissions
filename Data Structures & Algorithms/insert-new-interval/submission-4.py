class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        for i, j in intervals[1::]:
            last = result[-1][1]
            first = result[-1][0]
            if result[-1][1] >= i:
                result[-1][1] = max(j, last)
                result[-1][0] = min(i, first)
            else:
                result.append([i,j])

        return result