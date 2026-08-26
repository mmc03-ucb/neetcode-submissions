class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if not fresh:
            return 0
        mins = -1
        while rotten:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dispR, dispC in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    nr, nc = r + dispR, c + dispC
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    rotten.append((nr, nc))
                    fresh -= 1
            mins += 1
        
        return mins if not fresh else -1