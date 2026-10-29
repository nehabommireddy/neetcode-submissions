class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(path, i):
            if sum(path) == target:
                res.append(path.copy())
                return
            if i >= len(nums) or sum(path) > target:
                return
            
            path.append(nums[i])
            backtracking(path, i)
            path.remove(nums[i])
            backtracking(path, i+1)
        
        backtracking([],0)

        return res