class LinkedList:
    def __init__(self, val = ""):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = LinkedList()
        self.tail = LinkedList()

        self.hp = LinkedList(homepage)
        self.head.next = self.hp
        self.hp.prev = self.head

        self.hp.next = self.tail
        self.tail.prev = self.hp

        self.curr = self.hp

    def visit(self, url: str) -> None:
        p = self.curr
        self.curr = LinkedList(url)

        p.next = self.curr
        self.curr.prev = p

        self.curr.next = self.tail

    def back(self, steps: int) -> str:
        while steps != 0 and self.curr.prev != self.head:
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps != 0 and self.curr.next != self.tail:
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)