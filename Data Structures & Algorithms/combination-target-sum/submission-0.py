class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i, path):
            if i == len(nums):
                return
            if sum(path) == target:
                combinations.append(path[:])
                return
            if sum(path) > target:
                return
            
            path.append(nums[i])
            backtrack(i, path)
            path.pop()
            backtrack(i+1, path)
            return
        
        backtrack(0, [])
        return combinations