class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            ans = float("inf")
            for coin in coins:
                ans = min(ans, 1 + dfs(amount-coin))
            memo[amount] = ans
            return ans
        res = dfs(amount)
        return res if res != float("inf") else -1
