import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i: i[0])
        squeries = []
        for i in range(len(queries)):
            squeries.append((queries[i], i))
        squeries.sort(key=lambda i: i[0])
        res = [-1] * len(queries)
        i = 0
        minheap = []
        for q, qi in squeries:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minheap, (intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i+= 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if minheap:
                res[qi] = minheap[0][0]
            else: 
                res[qi] = -1
        
        return res
                    

