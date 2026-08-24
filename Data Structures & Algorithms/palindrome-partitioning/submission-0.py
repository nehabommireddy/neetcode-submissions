class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(word):
            l = 0
            r = len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        res = []
        partitions = []
        def backtracking (i):
            if i >= len(s):
                res.append(partitions[:])
                return
            
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    partitions.append(s[i:j+1])
                    backtracking(j+1)
                    partitions.pop()
        backtracking(0)
        return res