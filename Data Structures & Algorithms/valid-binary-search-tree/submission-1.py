# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def boundsCheck(lo, nd, high):
            if not nd:
                return True
            
            if not lo < nd.val < high:
                return False
            
            return boundsCheck(lo, nd.left, nd.val) and boundsCheck(nd.val, nd.right, high)
        
        return boundsCheck(float("-INF"), root, float("INF"))