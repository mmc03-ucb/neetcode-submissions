class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        boxCheck = defaultdict(set)

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rowCheck[r]:
                    return False
                rowCheck[r].add(val)

                if val in colCheck[c]:
                    return False
                colCheck[c].add(val)

                box_r = r // 3
                box_c = c // 3

                if val in boxCheck[(box_r, box_c)]:
                    return False
                boxCheck[(box_r, box_c)].add(val)
        
        return True
