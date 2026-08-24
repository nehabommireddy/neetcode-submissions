class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for j in nums:
                if j not in path:
                    path.append(j)
                    backtracking(path)
                    path.pop()
        
        backtracking([])
        return result