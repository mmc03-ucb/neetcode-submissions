class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        copy_arr = self.arr
        self.capacity *= 2
        self.arr = [None] * self.capacity
        for i in range(self.size):
            self.arr[i] = copy_arr[i]



    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity