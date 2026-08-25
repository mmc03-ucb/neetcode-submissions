# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(nd):
            if not nd:
                return
            
            if nd.left:
                dfs(nd.left)
            arr.append(nd.val)
            if nd.right:
                dfs(nd.right)
            
            return
        
        dfs(root)
        return arr[k-1]