# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        dfs through tree:
            if not nd:
                return None
            if nd.val == p or q:
                return nd
            if left and right:
                return nd
            elif left or right:
                return left or right
        """

        def dfs(nd):
            if not nd:
                return None
            
            left = dfs(nd.left)
            right = dfs(nd.right)

            if nd.val == p.val or nd.val == q.val or (left and right):
                return nd
            else:
                return left or right
        
        return dfs(root)









