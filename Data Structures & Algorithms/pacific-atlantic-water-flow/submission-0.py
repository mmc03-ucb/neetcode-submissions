from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for r_disp, c_disp in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r_next = r + r_disp
                    c_next = c + c_disp
                    if (
                        r_next < 0 or c_next < 0 or
                        r_next >= len(heights) or c_next >= len(heights[0]) or
                        heights[r_next][c_next] < heights[r][c] or
                        (r_next, c_next) in visited
                    ):
                        continue
                    visited.add((r_next, c_next))
                    q.append((r_next, c_next))
            return visited

        # Pacific side
        pacific_side = [(0, c) for c in range(len(heights[0]))] + [(r, 0) for r in range(len(heights))]
        
        # BFS for Pacific side
        q = deque(pacific_side)
        visited = set(pacific_side)
        pacific_heights = bfs(q, visited)

        # Atlantic side
        atlantic_side = [(r, len(heights[0]) - 1) for r in range(len(heights))] + [(len(heights) - 1, c) for c in range(len(heights[0]))]
        
        q = deque(atlantic_side)
        visited = set(atlantic_side)
        atlantic_heights = bfs(q, visited)

        # Intersection of both
        result = pacific_heights.intersection(atlantic_heights)
        return [list(cell) for cell in result]
