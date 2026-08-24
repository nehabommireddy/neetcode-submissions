class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0

        def backtracking(i, total):
            nonlocal sum
            if i == len(nums):
                sum += total
                return 
            if i > len(nums):
                return            
            backtracking(i+1, total ^ nums[i])
            backtracking(i+1, total)
            return 

        backtracking(0,0)
        return sum


        