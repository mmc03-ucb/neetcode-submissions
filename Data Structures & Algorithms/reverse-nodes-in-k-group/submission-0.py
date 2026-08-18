# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        groupPrev = dummy

        curr = head

        def incrementK(nd):
            for _ in range(k):
                nd = nd.next
                if not nd:
                    return None
            
            return nd

        while True:
            kth = incrementK(groupPrev)
            if not kth:
                return dummy.next
            
            groupNext = kth.next
            # groupNext = 4

            prev = groupNext

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # curr = 4, nxt = curr, prev = 3
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp