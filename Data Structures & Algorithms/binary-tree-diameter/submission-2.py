# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(nd):
            if not nd:
                return 0
            
            left = dfs(nd.left)
            right = dfs(nd.right)

            d = right + left

            self.diameter = max(self.diameter, d)

            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter