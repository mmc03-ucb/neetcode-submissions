"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(nd):
            if not nd:
                return nd

            if nd in oldToNew:
                return oldToNew[nd]
            
            oldToNew[nd] = Node(nd.val)

            for nei in nd.neighbors:
                oldToNew[nd].neighbors.append(dfs(nei))
            
            return oldToNew[nd]
        
        return dfs(node)