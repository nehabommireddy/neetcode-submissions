class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range (9)]
        cols = [set() for _ in range (9)]
        squares = [set() for _ in range (9)]

        for i in range (9):
            for j in range (9):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    square = (i//3)*3 + (j//3)

                    if num in rows[i] or num in cols[j] or num in squares[square]:
                        return False
                    else:
                        rows[i].add(num)
                        cols[j].add(num)
                        squares[square].add(num)

        
        return True
