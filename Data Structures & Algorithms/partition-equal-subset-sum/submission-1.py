class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        sums = 0
        for num in nums:
            sums += num
        half = sums//2
        if sums % 2 != 0:
            return False
        def dfs(i, currsum):
            if i == len(nums) or currsum > half:
                return False
            if currsum == half:
                return True
            if (i, currsum) in memo:
                return memo[(i, currsum)]
            
            skip = dfs(i+1, currsum)
            take = dfs(i+1, currsum+nums[i])
            memo[(i,currsum)] = take or skip
            return memo[(i,currsum)]
        
        return dfs(0, 0)
        