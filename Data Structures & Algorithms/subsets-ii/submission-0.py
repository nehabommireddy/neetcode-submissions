class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtracking(i, path):
            if i >= len(nums):
                result.append(path[:])
                return
            
         
            path.append(nums[i])
            backtracking(i+1,path)
            path.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtracking(i+1, path)

            
        
        backtracking(0, [])
        return result

        
        