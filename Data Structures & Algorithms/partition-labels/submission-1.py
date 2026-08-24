class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        end = 0
        start = 0
        result = []
        
        for i, char in enumerate(s):
            end = max(end, last[char])

            if end == i:
                result.append(end-start+1)
                start = i+1


        return result
            
        
