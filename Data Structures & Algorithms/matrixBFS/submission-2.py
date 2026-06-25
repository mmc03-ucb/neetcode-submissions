class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        q = collections.deque()
        visit = set()

        q.append((0,0))
        visit.add((0,0))

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
                
                disp = [[0,1], [0, -1], [1, 0], [-1,0]]
                for rd, cd in disp:
                    r_next = r + rd
                    c_next = c + cd
                    if min(r_next, c_next) < 0 or r_next == R or c_next == C or grid[r_next][c_next] == 1 or (r_next,c_next) in visit:
                        continue
                    else:
                        q.append((r_next, c_next))
                        visit.add((r_next, c_next))
            length += 1
        
        return -1
