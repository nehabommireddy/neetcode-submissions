class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0 for _ in range (26)]
        for char in s1:
            freq1[ord(char) - ord('a')] += 1

        freq2 = [0 for _ in range (26)]

        if len(s2) < len(s1):
            return False
        
        left = 0
        right = len(s1)
        while right <= len(s2):
            for i in range (left, right):
                freq2[ord(s2[i]) - ord('a')] += 1
            
            if freq1 == freq2:
                return True
            else: 
                freq2 = [0 for _ in range (26)]
                left += 1
                right += 1
        return False

        
        