# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set fast pointer n steps ahead of slow
        # edge cases: head, tail, only 1 node
            
        slow, fast = head, head

        while n!= 0:
            fast = fast.next
            n -= 1

        prev = None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if not prev:
            return head.next
        nxt = slow.next
        prev.next = nxt

        return head
