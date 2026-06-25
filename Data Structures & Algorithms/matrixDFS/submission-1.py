class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        def dfs(r, c, visit):
            # base case
            if (
                min(r,c) < 0 or
                r == self.rows or
                c == self.cols or
                (r,c) in visit or
                self.grid[r][c] == 1
            ):
                return 0
            
            if r == self.rows - 1 and c == self.cols - 1:
                return 1
            
            visit.add((r,c))

            count = 0
            for disp_r, disp_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                count += dfs(r + disp_r, c + disp_c, visit)
            
            visit.remove((r, c))
            return count
        return dfs(0, 0, set())        
            