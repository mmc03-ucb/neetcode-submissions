class TrieNode:
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
        def dfs(nd, i):
            if i >= len(word):
                return nd.word
            c = word[i]
            if c == ".":
                for child in nd.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else:
                if c not in nd.children:
                    return False
                return dfs(nd.children[c], i + 1)
        
        return dfs(self.root, 0)

