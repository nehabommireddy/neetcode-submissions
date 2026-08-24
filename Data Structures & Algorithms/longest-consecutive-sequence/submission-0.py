class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        start = []

        for num in nums:
            s.add(num)

        for num in s:
            if num-1 not in s:
                start.append(num)
        
        sequence = 0
        count = 0
        for i in start:
            while i in s:
                i += 1
                count += 1
            sequence = max (sequence, count) 
            count = 0
        
        return sequence