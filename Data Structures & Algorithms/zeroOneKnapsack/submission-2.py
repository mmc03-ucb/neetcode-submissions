class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # optimized dp
        n, m = len(profit), capacity

        dp = [0] * (m+1)

        # fill first row (first item)
        for c in range(m+1):
            if weight[0] <= c:
                dp[c] = profit[0]
        
        for r in range(1, n):
            curRow = [0] * (m+1)
            for c in range(1, m+1):
                skip = dp[c]
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + dp[c - weight[r]]
                
                curRow[c] = max(include, skip)
            dp = curRow
        
        return dp[m]
