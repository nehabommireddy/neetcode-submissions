class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        res=0
        def expand(l,r):
            nonlocal res, start
            while l>= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            length = r-l-1
            if length>res:
                res = length
                start = l+1
        for i in range (len(s)):
            expand(i, i)
            expand (i, i+1)
        return s[start:start+res]