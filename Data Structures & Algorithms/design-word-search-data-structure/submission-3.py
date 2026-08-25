class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(i, nd):
            if i >= len(word):
                return nd.word
            c = word[i]
            if c == ".":
                for child in nd.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            else:
                if c not in nd.children:
                    return False
                return dfs(i+1, nd.children[c])
        
        for i in range(len(word)):
            c = word[i]
            if c != ".":
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            else:
                return dfs(i, curr)
            
        return curr.word
