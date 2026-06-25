class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(0, n+1):
            self.par[i] = i
            self.rank[i] = 0 
        
        self.numComponents = n

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return True
        return False

    def union(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False
        
        if self.rank[px] > self.rank[py]:
            self.par[py] = px
        elif self.rank[py] > self.rank[px]:
            self.par[px] = py
        else:
            self.par[py] = px
            self.rank[px] += 1
        
        self.numComponents -= 1
        return True

    def getNumComponents(self) -> int:
        return self.numComponents

