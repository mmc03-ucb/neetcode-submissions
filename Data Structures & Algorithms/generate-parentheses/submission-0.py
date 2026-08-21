class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        at each step
        if 0 < opening bracket remaining <= closing bracket:
            add opening bracket and move to next step
            pop
        if 0 < closing bracket remaining  and cloB > opening bracket:
            add closing bracket and move to next step
            pop
        
        terminate when len(arr) == 2n and opB == cloB == 0
        """

        brackets = []

        def backtrack(bracket, op, clo):
            if len(bracket) == n * 2 and op == clo == 0:
                brackets.append("".join(bracket))
                return
            
            if 0 < op <= clo:
                bracket.append("(")
                backtrack(bracket, op - 1, clo)
                bracket.pop()
            
            if clo > 0 and clo > op:
                bracket.append(")")
                backtrack(bracket, op, clo - 1)
                bracket.pop()
            
        backtrack([], n, n)

        return brackets

