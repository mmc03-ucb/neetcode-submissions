class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []

        def bt(i, curr):
            if i >= len(s):
                palindromes.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                currStr = s[i:j+1]
                if currStr == currStr[::-1]:
                    curr.append(currStr)
                    bt(j+1, curr)
                    curr.pop()
            return
        
        bt(0, [])

        return palindromes