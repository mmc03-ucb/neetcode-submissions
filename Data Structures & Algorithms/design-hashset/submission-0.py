class Node:
    def __init__(self, key = -1):
        self.key = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.hashVal = 1001
        self.hashset = [Node() for _ in range(self.hashVal)]
    
    def hashedKey(self, k):
        return k % self.hashVal

    def add(self, key: int) -> None:
        hk = self.hashedKey(key)
        curr = self.hashset[hk]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        hk = self.hashedKey(key)
        curr = self.hashset[hk]

        while curr.next and curr.next.key != key:
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next

    def contains(self, key: int) -> bool:
        hk = self.hashedKey(key)
        curr = self.hashset[hk]

        while curr.next and curr.next.key != key:
            curr = curr.next
        
        if curr.next:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)