class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in cache:
                return cache[n]
            cache[n] = dfs(n-1) + dfs(n-2)

            return cache[n]
        
        return dfs(n)
