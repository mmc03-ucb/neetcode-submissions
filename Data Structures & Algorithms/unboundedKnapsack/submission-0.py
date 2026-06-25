class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def dfs(i, cap):
            if i == len(profit):
                return 0
            
            if (i, cap) in cache:
                return cache[(i, cap)]
            
            # skip
            cache[(i, cap)] = dfs(i+1, cap)

            # include
            remaining = cap - weight[i]

            if remaining >= 0:
                p = profit[i] + dfs(i, remaining)
                cache[(i, cap)] = max(cache[(i, cap)], p)
            
            return cache[(i, cap)]
        
        return dfs(0, capacity)
