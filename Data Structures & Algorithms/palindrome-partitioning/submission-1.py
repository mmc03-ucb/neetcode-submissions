class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        at each step check if s[i] extends palindrome or not
        if it does extend palindrome
        always append s[i]
        """


        palindromes = []
        substring = []

        def backtrack(i):
            if i == len(s):
                palindromes.append(substring.copy())
                return
            
            for j in range(i, len(s)):
                curr = s[i:j + 1]
                if curr == curr[::-1]:
                    substring.append(curr)
                    backtrack(j+1)
                    substring.pop()
            
        backtrack(0)

        return palindromes
            
            
