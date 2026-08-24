class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if (r<0 or r>=len(grid) or c<0 or c>=len(grid[0])):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        max_size = 0
        for row in range (rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_size = max(max_size, dfs(row, col))
        
        return max_size
            
            