class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        rows = [False] * r
        cols = [False] * c

        for i in range (r):
            for j in range (c):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range (r):
            for j in range (c):
                if rows[i] == True or cols[j] == True:
                    matrix[i][j] = 0


        