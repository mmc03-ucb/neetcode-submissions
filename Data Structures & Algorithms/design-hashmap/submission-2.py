class ListNode:
    def __init__(self, k = 0, v = 0):
        self.key = k
        self.val = v
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashVal = 1000
        self.arr = [ListNode() for _ in range(self.hashVal)]
    
    def hashedKey(self, k):
        return k % self.hashVal

    def put(self, key: int, value: int) -> None:
        ix = self.hashedKey(key)
        head = self.arr[ix]
        curr = head

        while curr.next and curr.next.key != key:
            curr = curr.next
        
        if not curr.next:
            curr.next = ListNode(key, value)
        else:
            curr.next.val = value


    def get(self, key: int) -> int:
        ix = self.hashedKey(key)
        head = self.arr[ix]
        curr = head

        while curr.next and curr.next.key != key:
            curr = curr.next
        
        if not curr.next:
            return -1
        else:
            return curr.next.val

    def remove(self, key: int) -> None:
        ix = self.hashedKey(key)
        head = self.arr[ix]
        curr = head

        while curr.next and curr.next.key != key:
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)