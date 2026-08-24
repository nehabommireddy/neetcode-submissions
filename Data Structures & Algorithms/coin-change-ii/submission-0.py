class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = 0
        memo = {}
        def dfs(i, total):
            if total > amount:
                return 0
            if total == amount:
                return 1
            if i>=len(coins):
                return 0
            if (i, total) in memo:
                return memo[(i,total)]
            memo[(i,total)] = 0
            take = dfs(i, coins[i]+total)
            skip = dfs(i+1, total)
            memo[(i,total)] += take + skip
            return memo[(i,total)]
        return dfs(0, 0)
