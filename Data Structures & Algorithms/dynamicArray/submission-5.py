class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.last = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.last >= self.capacity:
            self.resize()
        self.array[self.last] = n
        self.last += 1
    
    def popback(self) -> int:
        elem = self.array[self.last - 1]
        self.last -= 1
        return elem

    def resize(self) -> None:
        arrayCopy = self.array
        self.capacity *= 2
        self.array = [0] * self.capacity
        for i in range(len(arrayCopy)):
            self.array[i] = arrayCopy[i]

    def getSize(self) -> int:
        return self.last
    
    def getCapacity(self) -> int:
        return self.capacity