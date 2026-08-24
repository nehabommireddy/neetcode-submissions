class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix)
        row = -1

        while (left < right):
            mid = (left+right)//2

            if (target<=matrix[mid][-1] and target>=matrix[mid][0]):
                row = mid
                break
            elif (target<matrix[mid][0]):
                right = mid
            
            else:
                left = mid+1
        if row == -1:
            return False
        left = 0
        right = len(matrix[row])
        while (left<right):
            mid = (left+right)//2

            if (matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] < target):
                left = mid+1
            else:
                right = mid
        
        return False