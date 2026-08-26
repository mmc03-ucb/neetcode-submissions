class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            if board[r][0] == "O":
                board[r][0] = "Z"
                q.append((r, 0))
            if board[r][cols-1] == "O":
                board[r][cols-1] = "Z"
                q.append((r, cols-1))
        
        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "Z"
                q.append((0, c))
            if board[rows - 1][c] == "O":
                board[rows - 1][c] = "Z"
                q.append((rows -1, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in [(0, 1), (1,0), (0, -1), (-1, 0)]:
                    nr, nc = r + x, c + y
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or board[nr][nc] != "O":
                        continue
                    board[nr][nc] = "Z"
                    q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Z":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
