import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task,0) + 1
        
        time = 0
        heap = []
        queue = deque()
        for key in hashmap.keys():
            heapq.heappush(heap, -hashmap[key])
        
        while heap or queue:
            time += 1
            if heap:
                count = 1+ heapq.heappop(heap)
                if count != 0:
                    queue.append((time+n, count))
            
            if queue and queue[0][0] == time:
                _, cnt = queue.popleft()
                heapq.heappush(heap, cnt)
        
        return time