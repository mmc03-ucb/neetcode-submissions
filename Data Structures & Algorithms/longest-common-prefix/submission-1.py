class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        word = strs[0]
        string = []

        for i in range(len(word)):
            c = word[i]
            for w in strs:
                if i >= len(w) or w[i] != c:
                    return "".join(string)
            string.append(c)
        
        return "".join(string)
                
