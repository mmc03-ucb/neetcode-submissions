class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lst = []

    def get(self, i: int) -> int:
        return self.lst[i]

    def set(self, i: int, n: int) -> None:
        if i == 0:
            prefix = [n]
            prefix.extend(self.lst[1:])
            self.lst = prefix
        else:
            prefix = self.lst[0:i]
            prefix.append(n)
            if i + 1 < len(self.lst) - 1:
                prefix.extend(self.lst[i + 1:])
            self.lst = prefix
        if len(self.lst) > self.capacity:
            self.capacity += 1

    def pushback(self, n: int) -> None:
        self.lst.append(n)
        if len(self.lst) > self.capacity:
            self.capacity *= 2

    def popback(self) -> int:
        elem = self.lst[-1]
        self.lst = self.lst[0:-1]
        return elem

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.lst)
    
    def getCapacity(self) -> int:
        return self.capacity