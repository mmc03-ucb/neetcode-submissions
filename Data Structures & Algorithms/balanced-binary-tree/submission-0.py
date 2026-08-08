# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(nd):
            if not nd:
                return 0
            
            left = dfs(nd.left)
            right = dfs(nd.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return 1 + max(left, right)
        
        dfs(root)

        return self.balanced