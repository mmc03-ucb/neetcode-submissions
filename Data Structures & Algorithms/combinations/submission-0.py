class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def backtrack(i, comb):
            if len(comb) == k:
                combs.append(comb.copy())
                return
            
            if i > n:
                return 
            
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
            backtrack(i+1, comb)

        backtrack(1, [])

        return combs