class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def dp(i, w):
            if i >= len(profit):
                return 0
            
            if (i, w) in cache:
                return cache[(i, w)]

            skip = dp(i+1, w)

            include = 0
            if w - weight[i] >= 0:
                include = profit[i] + dp(i, w - weight[i])
            
            cache[(i, w)] = max(skip, include)
            return cache[(i, w)]
        
        return dp(0, capacity)