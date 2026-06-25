class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # for each rotten orange, make adjacent oranges rotten
        # do this until there are no more rotten oranges or fresh = 0

        # create a count of fresh oranges and add already rotten oranges
        # to queue
        fresh = 0
        queue = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        time = 0
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for r_disp, c_disp in [(0,1), (1,0), (0,-1), (-1,0)]:
                    r_next = r + r_disp
                    c_next = c + c_disp
                    if (
                        min(r_next, c_next) < 0 or
                        r_next == len(grid) or
                        c_next == len(grid[0]) or
                        grid[r_next][c_next] == 0 or
                        grid[r_next][c_next] == 2
                    ):
                        continue
                    else:
                        queue.append((r_next, c_next))
                        grid[r_next][c_next] = 2
                        fresh -= 1
            time += 1
        
        return time if not fresh else -1


