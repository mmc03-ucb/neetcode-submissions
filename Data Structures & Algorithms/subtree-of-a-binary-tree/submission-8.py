# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(nd, subNd):
            if not subNd and not nd:
                return True
            elif not nd or not subNd or nd.val != subNd.val:
                return False
            
            return isSameTree(nd.left, subNd.left) and isSameTree(nd.right, subNd.right)
        
        self.subTree = False

        def dfs(rt):
            if not rt or self.subTree:
                return 
            
            if rt.val == subRoot.val:
                if isSameTree(rt, subRoot):
                    self.subTree = True
                    return
            
            dfs(rt.left)
            dfs(rt.right)
            return

        dfs(root)
        return self.subTree