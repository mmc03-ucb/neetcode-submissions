class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        node = Node(value)
        
        curr = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        
        node.prev = curr
        curr.next = node

        self.size += 1

    def appendleft(self, value: int) -> None:
        node = Node(value)

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def pop(self) -> int:
        if self.tail.prev != self.head:
            v = self.tail.prev.val
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return v
        else:
            return -1

    def popleft(self) -> int:
        if self.head.next != self.tail:
            v = self.head.next.val
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return v
        else:
            return -1
        
