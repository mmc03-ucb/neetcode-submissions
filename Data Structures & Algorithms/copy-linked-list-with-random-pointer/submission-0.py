"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        self.nodes = {}

        def dfs(nd):
            if not nd:
                return None
            
            if nd in self.nodes:
                return self.nodes[nd]
            
            node = Node(nd.val)
            self.nodes[nd] = node

            node.random = dfs(nd.random)
            node.next = dfs(nd.next)

            return self.nodes[nd]
        
        return dfs(head)


