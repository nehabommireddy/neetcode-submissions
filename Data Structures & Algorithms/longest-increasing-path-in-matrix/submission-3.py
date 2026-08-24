import sys
sys.setrecursionlimit(20000)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dfs(r,c):
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]

            left = right = up = down = 1
            if c+1 < len(matrix[0]) and matrix[r][c+1] > matrix[r][c]:
                up = 1+dfs(r, c+1)
            if c-1>=0 and matrix[r][c-1] > matrix[r][c]:
                down = 1+dfs(r, c-1)
            if r+1 < len(matrix) and matrix[r+1][c] > matrix[r][c]:
                left = 1+dfs(r+1, c)
            if r-1>=0 and matrix[r-1][c] > matrix[r][c]:
                right = 1+dfs(r-1, c)
            
            memo[(r,c)] = max(up, down, left, right)
            return memo[(r,c)]
        maxi = 0
        for r in range (len(matrix)):
            for c in range (len(matrix[r])):
                val = dfs(r,c)
                maxi = max(val, maxi)
            
        return maxi