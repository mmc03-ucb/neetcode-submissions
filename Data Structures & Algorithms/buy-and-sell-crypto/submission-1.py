class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        stack = [prices[0]]

        for p in prices:
            if p >= stack[-1]:
                profit = p - stack[-1]
                maxProfit = max(profit, maxProfit)
            else:
                stack.append(p)
        
        return maxProfit