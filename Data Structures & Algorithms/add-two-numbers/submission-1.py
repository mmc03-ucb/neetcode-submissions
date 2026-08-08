# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        dummy = head
        while l1 or l2 or carry:
            currL1 = l1.val if l1 else 0
            currL2 = l2.val if l2 else 0

            total = currL1 + currL2 + carry
            carry = 0
            
            if total >= 100:
                carry += total // 100
                nd = ListNode(total%100)
            elif total >= 10:
                carry += total // 10
                nd = ListNode(total%10)
            else:
                nd = ListNode(total)
                carry = 0
            
            dummy.next = nd
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next
        