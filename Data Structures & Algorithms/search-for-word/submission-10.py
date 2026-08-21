class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, i):
            if i >= len(word):
                return True
            elif min(r, c) < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            else:
                board[r][c] = "#"
                
                if backtrack(r+1, c, i+1) or backtrack(r-1, c, i +1) or backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1):
                    board[r][c] = word[i]
                    return True
                else:
                    board[r][c] = word[i]
                    return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False