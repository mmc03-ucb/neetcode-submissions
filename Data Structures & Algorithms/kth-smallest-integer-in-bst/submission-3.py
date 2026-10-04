# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        preorder = []

        def dfs(nd):
            if not nd:
                return
            
            dfs(nd.left)
            preorder.append(nd.val)
            dfs(nd.right)

            return
        dfs(root)
        return preorder[k-1]