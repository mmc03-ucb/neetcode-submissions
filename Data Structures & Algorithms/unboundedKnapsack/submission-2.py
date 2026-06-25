class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        self.capacity = capacity
        self.cache = {}
        def dp(i, w):
            if i >= len(profit):
                return 0
            
            if w > self.capacity:
                return - 1
            if (i,w) in self.cache:
                return self.cache[(i,w)]

            self.cache[(i,w)] = dp(i+1, w)

            
            if w + weight[i] <= self.capacity:
                self.cache[(i,w)] = max(profit[i] + dp(i, w + weight[i]),self.cache[(i,w)])
            
            return self.cache[(i,w)]
        
        return dp(0, 0)