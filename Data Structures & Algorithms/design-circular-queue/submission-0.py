class Node:
    def __init__(self, v):
        self.v = v
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        self.k = k
    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        node = Node(value)
        p = self.tail.prev
        p.next = node
        node.prev = p

        node.next = self.tail
        self.tail.prev = node
        self.size += 1
        return True
    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        curr = self.head.next
        nxt = curr.next

        self.head.next = nxt
        nxt.prev = self.head

        self.size -= 1

        return True


    def Front(self) -> int:
        return -1 if self.size == 0 else self.head.next.v

    def Rear(self) -> int:
        return -1 if self.size == 0 else self.tail.prev.v

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()