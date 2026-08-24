class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]
        columns = set()
        diagonal = set()
        antidiagonal = set()
        def backtracking(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            for col in range(0, n):
                if col in columns:
                    continue
                if (row-col) in diagonal:
                    continue
                if (row+col) in antidiagonal:
                    continue
                board[row][col] = "Q"

                columns.add(col) 
                diagonal.add(row-col)
                antidiagonal.add(row+col)
                backtracking(row+1)
                board[row][col] = "."
                columns.remove(col)
                diagonal.remove(row-col)
                antidiagonal.remove(row+col)
            
        backtracking(0)
        return result

