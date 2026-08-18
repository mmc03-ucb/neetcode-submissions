class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.exists = False
        def bt(r, c, i):
            if i >= len(word):
                self.exists = True
                return
            elif min(r, c) < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i] or board[r][c] == "#":
                return
            
            board[r][c] = "#"

            bt(r+1, c, i+1)
            bt(r-1, c, i+1)
            bt(r, c+1, i+1)
            bt(r, c-1, i+1)

            board[r][c] = word[i]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    bt(r, c, 0)
                    if self.exists:
                        return True
        
        return False
