class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = prices[i] - buy
            max_profit = max(profit, max_profit)
        
        return max_profit