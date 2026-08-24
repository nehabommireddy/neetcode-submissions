class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        end = 0
        curr = 0
        result = []
        while curr < len(s):
            end = last[s[curr]]
            length = 0
            while curr <= end:
                end = max(end, last[s[curr]])
                curr += 1
                length += 1

            result.append(length)

        return result
            
        
