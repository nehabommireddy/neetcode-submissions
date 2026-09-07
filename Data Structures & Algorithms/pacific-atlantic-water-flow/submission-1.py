class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        res = []
        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r,c))

            if r+1 < rows and heights[r+1][c] >= heights[r][c]:
                dfs(r+1, c, ocean)
            if r-1 >= 0 and heights[r-1][c] >= heights[r][c]:
                dfs(r-1, c, ocean)
            if c+1 < cols and heights[r][c+1] >= heights[r][c]:
                dfs(r, c+1, ocean)
            if c-1 >= 0 and heights[r][c-1] >= heights[r][c]:
                dfs(r, c-1, ocean)
        
        for r in range(rows):
            for c in range(cols):
                if r== 0 or c == 0:
                    dfs(r,c, pacific)
                if r == rows -1 or c == cols - 1:
                    dfs(r,c, atlantic)
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        
        return res
















        """
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs (r,c, visited):
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c+ dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
            
                if (nr, nc) in visited: 
                    continue

                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
      
        for c in range(cols):
            dfs(0, c, pacific)
            
        for r in range(rows):
            dfs(r, 0, pacific)
            
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
            
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
        """



            
