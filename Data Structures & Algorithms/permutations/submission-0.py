class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(path,used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for j in nums:
                if j not in used:
                    path.append(j)
                    used.append(j)
                    backtracking(path, used)
                    path.pop()
                    used.pop()
        
        backtracking([],[])
        return result