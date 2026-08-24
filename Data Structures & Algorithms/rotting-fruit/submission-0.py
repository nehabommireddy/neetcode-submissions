from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh+=1 
        minutes = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                r,c = queue.popleft()
                if r+1 < len(grid) and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    queue.append((r+1, c))
                    fresh -= 1
                if r-1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    queue.append((r-1, c))
                    fresh -= 1
                if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    queue.append((r, c+1))
                    fresh -= 1
                if c-1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    queue.append((r, c-1))
                    fresh -= 1
            minutes += 1
        if fresh > 0:
            return -1
        else:
            return max(minutes,0)
        