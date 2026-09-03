import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = {}
        res = []
        for char in s:
            freq[char] = freq.get(char,0) + 1
        
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        prev = None
        while heap:
            temp = heapq.heappop(heap)
            res.append(temp[1])
            temp = (temp[0]+1 , temp[1])
            if prev and prev[0] != 0:
                heapq.heappush(heap, prev)
            prev = (temp[0], temp[1])
        
        if prev[0] != 0:
            return ""
        else:
            return "".join(res)