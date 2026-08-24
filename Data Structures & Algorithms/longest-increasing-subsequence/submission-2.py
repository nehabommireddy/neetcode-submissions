class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, prev):
            if i > len(nums) - 1:
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            notchosen = dfs(i+1, prev)
            chosen = 0
            if prev == -1 or nums[i] > nums[prev]:
                chosen = 1 + dfs(i+1, i)
            
            memo[(i, prev)] = max(chosen, notchosen)
            return max(chosen, notchosen)
        return dfs(0, -1)
