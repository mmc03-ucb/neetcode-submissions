class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []

        def backtrack(i, curr):
            if i >= len(s):
                palindromes.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                string = s[i: j+1]
                if string == string[::-1]:
                    curr.append(string)
                    backtrack(j+1, curr)
                    curr.pop()
            
            return

        backtrack(0, [])

        return palindromes
