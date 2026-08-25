# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def boundsCheck(low, nd, high):
            if not nd:
                return True
            
            if not low < nd.val < high:
                return False
            
            return boundsCheck(low, nd.left, nd.val) and boundsCheck(nd.val, nd.right, high)
        
        return boundsCheck(float("-INF"), root, float("INF"))
            
            