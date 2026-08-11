# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        bfs
        insertion order: right first then left
        at each level, first node popped is rightMost
        TC: O(n)
        SC: O(n)
        """

        rsv = []
        if not root:
            return rsv
        q = deque()
        q.append(root)
        level = 0
        while q:
            for _ in range(len(q)):
                nd = q.popleft()
                if len(rsv) == level:
                    rsv.append(nd.val)
                if nd.right:
                    q.append(nd.right)
                if nd.left:
                    q.append(nd.left)
            level += 1
        
        return rsv
