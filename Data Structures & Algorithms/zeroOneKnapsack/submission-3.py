class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        self.prof = 0
        n = len(profit)
        def dp(i, p, w):
            if i >= n:
                if w <= capacity:
                    self.prof = max(self.prof, p)
                return
            
            if w > capacity:
                return
            
            # include
            dp(i+1, p + profit[i], w + weight[i])
            # exclude
            dp(i+1, p, w)
        
        dp(0, 0, 0)
        return self.prof
            
