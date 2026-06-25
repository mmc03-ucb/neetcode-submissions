class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        queue = deque()
        visited = set()

        queue.append((0,0))
        visited.add((0,0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == self.rows - 1 and c == self.cols - 1:
                    return length
                
                for r_disp, c_disp in [(0,1), (0,-1), (1, 0), (-1,0)]:
                    r_next = r + r_disp
                    c_next = c + c_disp
                    if (
                        min(r_next, c_next) < 0 or
                        r_next >= self.rows or
                        c_next >= self.cols or
                        (r_next, c_next) in visited or
                        grid[r][c] == 1
                    ):
                        continue
                    else:
                        queue.append((r_next, c_next))
                        visited.add((r_next, c_next))
            length += 1
        return -1