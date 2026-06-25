class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        node = self.head.next
        while node:
            if i == index:
                return node.val
            node = node.next
            i += 1
        return -1
            
    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        node = self.head
        while i < index and node:
            node = node.next
            i += 1
        
        if node and node.next:
            if node.next == self.tail:
                self.tail = node
            node.next = node.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        node = self.head.next
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr
        
