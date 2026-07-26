# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(nd):
            if not nd:
                return
            
            left = invert(nd.left)
            right = invert(nd.right)

            nd.left = right
            nd.right = left

            return nd

        return invert(root)