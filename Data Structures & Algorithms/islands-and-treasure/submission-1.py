from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c= queue.popleft()
            if r+1 < len(grid) and grid[r+1][c] == 2147483647:
                queue.append((r+1,c))
                grid[r+1][c] = 1 + grid[r][c]
            if r-1 >= 0 and grid[r-1][c] == 2147483647:
                queue.append((r-1,c))
                grid[r-1][c] = 1 + grid[r][c]
            if c+1 < len(grid[0]) and grid[r][c+1] == 2147483647:
                queue.append((r,c+1))
                grid[r][c+1] = 1 + grid[r][c]
            if c-1 >= 0 and grid[r][c-1] == 2147483647:
                queue.append((r,c-1))
                grid[r][c-1] = 1 + grid[r][c]
            





























"""


        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = deque()
        for row in range(len(grid)):
            for col in range (len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row,col))
    
        while queue:
            r,c = queue.popleft()
            if r+1<len(grid) and grid[r+1][c] == 2147483647:
                queue.append((r+1,c))
                grid[r+1][c] = grid[r][c]+1
            if r-1>=0 and grid[r-1][c] == 2147483647:
                queue.append((r-1,c))
                grid[r-1][c] = grid[r][c]+1
            if c+1<len(grid[0]) and grid[r][c+1] == 2147483647:
                queue.append((r,c+1))
                grid[r][c+1] = grid[r][c]+1
            if c-1>=0 and grid[r][c-1] == 2147483647:
                queue.append((r,c-1))
                grid[r][c-1] = grid[r][c]+1
        """
                
    