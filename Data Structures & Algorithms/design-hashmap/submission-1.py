class node:
    def __init__(self, k = -1, v = -1):
        self.k = k
        self.v = v
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hash = 1000
        self.arr = [node() for _ in range(self.hash)]
    
    def hashedkey(self, key):
        return key % self.hash

    def put(self, key: int, value: int) -> None:
        hk = self.hashedkey(key)
        curr = self.arr[hk]

        while curr and curr.next:
            if curr.next.k == key:
                curr.next.v = value
                return
            curr = curr.next
        
        curr.next = node(key, value)

    def get(self, key: int) -> int:
        hk = self.hashedkey(key)
        curr = self.arr[hk]

        while curr and curr.next:
            if curr.next.k == key:
                return curr.next.v
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        hk = self.hashedkey(key)
        curr = self.arr[hk]

        while curr and curr.next:
            if curr.next.k == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)