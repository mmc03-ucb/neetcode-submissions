from typing import List

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        cache = {}

        def dp(i, w):
            if i >= n:
                return 0  # No more items left
            
            if w > capacity:
                return float('-inf')  # Invalid state

            if (i, w) in cache:
                return cache[(i, w)]
            
            # Exclude current item
            exclude = dp(i + 1, w)
            
            # Include current item (only if within capacity)
            include = 0
            if w + weight[i] <= capacity:
                include = profit[i] + dp(i + 1, w + weight[i])
            
            cache[(i, w)] = max(include, exclude)
            return cache[(i, w)]
        
        return dp(0, 0)
