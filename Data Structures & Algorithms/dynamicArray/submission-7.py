class DynamicArray:
    """
    array of size ap
    ix to keep track of last elem
    s double when ix == s
    increment ix when adding elem
    decrement ix when popping
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [0] * self.cap
        self.ix = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.ix >= self.cap:
            self.resize()
        self.arr[self.ix] = n
        self.ix += 1

    def popback(self) -> int:
        temp = self.arr[self.ix - 1]
        self.ix -= 1
        return temp

    def resize(self) -> None:
        self.cap *= 2
        temp = [0] * self.cap
        for i in range(self.ix):
            temp[i] = self.arr[i]
        
        self.arr = temp

    def getSize(self) -> int:
        return self.ix
    
    def getCapacity(self) -> int:
        return self.cap
