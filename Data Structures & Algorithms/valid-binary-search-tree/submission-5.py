# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(lo, nd, hi):
            if not nd:
                return True
            if not lo < nd.val < hi:
                return False
            
            return dfs(lo, nd.left, nd.val) and dfs(nd.val, nd.right, hi)
        
        return dfs(float("-INF"), root, float("INF"))