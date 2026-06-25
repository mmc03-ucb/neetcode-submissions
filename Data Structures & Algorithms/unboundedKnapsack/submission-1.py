class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        self.capacity = capacity
        def dp(i, w):
            if i >= len(profit):
                return 0
            
            if w > self.capacity:
                return - 1
            
            exclude = dp(i+1, w)

            include = 0
            if w + weight[i] <= self.capacity:
                include = profit[i] + dp(i, w + weight[i])
            
            return max(include, exclude)
        
        return dp(0, 0)