class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dictionary = {}
        self.head = Node()
        self.tail = Node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return - 1
        nd = self.dictionary[key]
        self.remove(nd)
        self.add(nd)

        return nd.val

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            nd = self.dictionary[key]
            nd.val = value
            self.remove(nd)
            self.add(nd)
        else:
            nd = Node(key, value)
            self.add(nd)
            self.dictionary[key] = nd
            if len(self.dictionary) > self.cap:
                toRemove = self.tail.prev
                self.remove(toRemove)
                del self.dictionary[toRemove.key]
    
    def add(self, nd):
        nxt = self.head.next
        nd.next = nxt
        nd.prev = self.head

        nxt.prev = nd
        self.head.next = nd
    
    def remove(self, nd):
        p = nd.prev
        nxt = nd.next

        p.next = nxt
        nxt.prev = p
            

        
