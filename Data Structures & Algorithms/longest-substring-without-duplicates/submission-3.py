class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        left = 0
        right = 1
        
        if (len(s)==0):
            return 0
        length = 1
        
        while (right < len(s)):
            sub = s[left:right]
            while left < right and (s[right] in sub):
                left += 1
                sub = s[left:right]
            right += 1
            length = max(length, right-left)
        
        return length

'''
s="pwwkew"
left = 1
right = 2
sub = "p"
length = 1
'''
