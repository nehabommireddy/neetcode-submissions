class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 1
        buy = 0
        maxi = 0

        while ( sell < len(prices)):
            if (prices[sell]-prices[buy] > maxi):
                maxi = prices[sell]-prices[buy]
            if (prices[sell] < prices[buy]):
                buy = sell
            sell += 1

        return maxi