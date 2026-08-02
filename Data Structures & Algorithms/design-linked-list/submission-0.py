class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        while curr and index != 0:
            curr = curr.next
            index -= 1
        
        return curr.val


    def addAtHead(self, val: int) -> None:
        nxt = self.head.next
        nd = ListNode(val)

        self.head.next = nd
        nd.prev = self.head

        nd.next = nxt
        nxt.prev = nd

        self.size += 1

    def addAtTail(self, val: int) -> None:
        last = self.tail.prev
        nd = ListNode(val)

        last.next = nd
        nd.prev = last

        nd.next = self.tail
        self.tail.prev = nd

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        curr = self.head.next
        while curr and index != 0:
            curr = curr.next
            index -= 1
        
        p = curr.prev
        nd = ListNode(val)

        p.next = nd
        nd.prev = p

        nd.next = curr
        curr.prev = nd

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        
        curr = self.head.next

        while curr and index != 0:
            curr = curr.next
            index -= 1
        
        p = curr.prev
        nxt = curr.next

        p.next = nxt
        nxt.prev = p

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)