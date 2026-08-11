# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        dfs with passing down maxVal seen so far in path 
        from root
        """

        def dfs(nd, maxFromRoot):
            if not nd:
                return 0
            
            left = dfs(nd.left, max(maxFromRoot, nd.val))
            right = dfs(nd.right, max(maxFromRoot, nd.val))

            if nd.val >= maxFromRoot:
                return 1 + left + right
            else:
                return left + right
        
        return dfs(root, float("-INF"))