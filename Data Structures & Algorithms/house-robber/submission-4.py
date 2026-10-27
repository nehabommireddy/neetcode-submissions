class Solution:
    
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0 
            
            inc = nums[i] + dp (i+2)
            ninc = dp (i+1)

            memo[i] = max(inc, ninc)
            return memo[i]
        
        return dp(0)
       