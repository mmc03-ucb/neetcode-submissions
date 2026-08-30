class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(nd, i):
            if i >= len(word):
                return nd.word
            elif not nd:
                return False

            c = word[i]

            if c != ".":
                if c not in nd.children:
                    return False
                return dfs(nd.children[c], i + 1)
            else:
                for child in nd.children.values():
                    if dfs(child, i+1):
                        return True
                return False
        
        return dfs(self.root, 0)








