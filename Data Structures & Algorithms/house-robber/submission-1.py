class Solution:
    #base case if len(nums) == 1, return nums[0]
    #if 0, return 0
    # opt[i] = nums[i] + opt(i-2) 
    def rob(self, nums: List[int]) -> int:

        memo = {}
        def dfs(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            keep = nums[i] + dfs(i - 2)
            skip = dfs(i-1)
            memo[i] = max(keep,skip)
            return memo[i]
        
        return dfs(len(nums)-1)