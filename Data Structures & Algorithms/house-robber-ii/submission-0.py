class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums):
            memo = {}

            def dfs(i):
                if i < 0:
                    return 0

                if i in memo:
                    return memo[i]

                keep = nums[i] + dfs(i - 2)
                skip = dfs(i - 1)

                memo[i] = max(keep, skip)
                return memo[i]

            return dfs(len(nums) - 1)

        return max(
            rob_linear(nums[:-1]),  # exclude last
            rob_linear(nums[1:])    # exclude first
        )