# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedL = ListNode()
        dummy = ListNode()
        dummy = sortedL

        while list1 and list2:
            if list1.val <= list2.val:
                sortedL.next = list1
                list1 = list1.next
            else:
                sortedL.next = list2
                list2 = list2.next

            sortedL = sortedL.next
        
        while list1:
            sortedL.next = list1
            break
        
        while list2:
            sortedL.next = list2
            break
        
        return dummy.next