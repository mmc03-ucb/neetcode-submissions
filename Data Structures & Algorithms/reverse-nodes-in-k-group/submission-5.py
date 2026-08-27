# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        def incr(nd):
            for _ in range(k):
                if not nd:
                    return None
                nd = nd.next
            
            return nd

        while True:
            kth = incr(groupPrev)
            if not kth:
                break
            
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        
        return dummy.next