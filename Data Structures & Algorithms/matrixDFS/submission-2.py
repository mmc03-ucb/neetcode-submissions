class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r, c, grid, visit):
            R = len(grid)
            C = len(grid[0])
            if min(r,c) < 0 or r == R or c == C or grid[r][c] == 1 or (r, c) in visit:
                return 0
            if r == R - 1 and c == C - 1:
                return 1
            
            visit.add((r,c))
            
            count = 0
            count += dfs(r+1, c, grid, visit)
            count += dfs(r-1, c, grid, visit)
            count += dfs(r, c+1, grid, visit)
            count += dfs(r, c-1, grid, visit)

            visit.remove((r,c))
            return count
        
        return dfs(0, 0, grid, set())