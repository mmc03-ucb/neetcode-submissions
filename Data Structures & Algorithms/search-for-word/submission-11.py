class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def bt(r, c, i):
            if i >= len(word):
                return True
            
            if min(r,c) < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i]:
                return False
            
            board[r][c] = "#"
            
            left = bt(r, c-1, i+1)
            right = bt(r, c+1, i+1)
            up = bt(r-1, c, i+1)
            down = bt(r+1, c, i+1)

            board[r][c] = word[i]

            return left or right or up or down
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if bt(r, c, 0):
                        return True
        
        return False