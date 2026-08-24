class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i, j in intervals[1::]:
            last = result[-1][1]

            if (i<=last):
                result[-1][1] = max(last, j)
            else:
                result.append([i,j])

        
        return result
        