class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i,j):
            if j == len(t):
                return 1
            if i >= len(s) or j > len(t):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            val = 0
            if s[i] == t[j]:
                val += dfs(i+1, j+1)

            val += dfs(i+1, j)

            memo[(i,j)] = val
            return memo[(i,j)]
        return dfs(0,0)
            