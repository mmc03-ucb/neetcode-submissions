class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dist = 1
        while q:
            for _ in range(len(q)):
                currR, currC = q.popleft()
                for dispR, dispC in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newR, newC = currR + dispR, currC + dispC
                    if min(newR, newC) < 0 or newR >= rows or newC >= cols or grid[newR][newC] != 2147483647:
                        continue
                    grid[newR][newC] = dist
                    q.append((newR, newC))

            dist += 1

        