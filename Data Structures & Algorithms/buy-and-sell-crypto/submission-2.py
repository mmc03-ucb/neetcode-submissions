class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        lowest = prices[0]

        for p in prices:
            if p >= lowest:
                profit = p - lowest
                maxProfit = max(profit, maxProfit)
            else:
                lowest = p
        
        return maxProfit