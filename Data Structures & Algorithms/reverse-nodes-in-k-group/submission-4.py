# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        def incrK(nd):
            for _ in range(k):
                if not nd:
                    return None
                nd = nd.next
            
            return nd
        
        while True:
            kth = incrK(groupPrev)
            if not kth:
                return dummy.next
            
            groupNxt = kth.next

            prev = groupNxt
            curr = groupPrev.next

            while curr != groupNxt:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        
        