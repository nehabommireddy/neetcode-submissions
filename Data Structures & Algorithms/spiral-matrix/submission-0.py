class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        right = cols - 1
        left = 0
        bottom = rows - 1
        res = []
        while top <= bottom and left <= right:
            for c in range(left, right+1):
                res.append(matrix[top][c])
            top += 1
            for c in range (top, bottom+1):
                res.append(matrix[c][right])
            right -= 1

            if top <= bottom:
                for c in range (right, left-1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for c in range (bottom, top-1, -1):
                    res.append(matrix[c][left])
                left += 1
        
        return res

