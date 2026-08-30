# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-INF")

        def dfs(nd):
            if not nd:
                return 0
            
            left = dfs(nd.left)
            right = dfs(nd.right)

            self.maxSum = max(self.maxSum, nd.val, left + nd.val, left + nd.val + right, right + nd.val)

            return max(nd.val, left + nd.val, right + nd.val)
        
        dfs(root)

        return self.maxSum