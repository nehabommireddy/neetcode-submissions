class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs (r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] != "O":
                return
            board[r][c] = "T"
            if r+1 < rows and board[r+1][c] == "O":
                dfs(r+1,c)
            if r-1 >= 0 and board[r-1][c] == "O":
                dfs(r-1,c)
            if c+1 < cols and board[r][c+1] == "O":
                dfs(r,c+1)
            if c-1 >= 0 and board[r][c-1] == "O":
                dfs(r,c-1)
            return

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    if (r == 0 or c== 0 or r==rows-1 or c == cols-1):
                        dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"






















        """rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if board[r][c] != "O":
                return
            board[r][c] = "S"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r, c-1)
        
        for c in range(cols):
            dfs(0,c)

        for c in range(cols):
            dfs(rows-1,c)

        for r in range(1, rows-1):
            dfs(r,0)

        for r in range(1, rows-1):
            dfs(r,cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                    """