class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.exists = False

        def bt(r, c, i):
            if i >= len(word):
                self.exists = True
                return 
            if min(r, c) < 0 or r >= rows or c >= cols or board[r][c] == "#" or board[r][c] != word[i]:
                return
            
            board[r][c] = "#"

            bt(r+1, c, i+1)
            bt(r-1, c, i+1)
            bt(r, c+1, i+1)
            bt(r, c-1, i+1)

            board[r][c] = word[i]
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    bt(r, c, 0)
                    if self.exists:
                        return True
        
        return False

            
            