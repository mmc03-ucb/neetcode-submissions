class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []

        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                output.append(word1[i])
            if i < len(word2):
                output.append(word2[i])
            
            i += 1
        
        return "".join(output)