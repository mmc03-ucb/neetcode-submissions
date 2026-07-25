# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide list into two halves
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half
        prev = None
        curr = slow.next

        # detach from first half
        slow.next = None

        # reverse 2nd half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev is at head of 2nd half reversed

        # merge 2 halves
        first = head
        merged = first
        while first and prev:
            fnext, pnext = first.next, prev.next
            first.next = prev
            prev.next = fnext
            first = fnext
            prev = pnext
        
        
        
            
