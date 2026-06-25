class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # backtracking with memoization
        cache = collections.defaultdict(int)
        return self.dfs(0, profit, weight, capacity, cache)
    def dfs(self, item, profit, weight, cap, cache):
        # end case
        if item == len(profit):
            return 0
        
        if (item, cap) in cache:
            return cache[(item, cap)]
        
        # skip item
        cache[(item, cap)] = self.dfs(item + 1, profit, weight, cap, cache)

        # include item
        newCap = cap - weight[item]
        if newCap >= 0:
            p = profit[item] + self.dfs(item + 1, profit, weight, newCap, cache)
            cache[(item, cap)] = max(cache[(item, cap)], p)
        
        return cache[(item, cap)]

