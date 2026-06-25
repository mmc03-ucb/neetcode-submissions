class UnionFind:
    
    def __init__(self, n: int):
        self.par = [i for i in range(n+1)]
        self.rank = [0 for j in range(n+1)]
        self.comps = n

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            p = self.par[self.par[p]]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p, q = self.find(x), self.find(y)
        if p == q:
            return False
        
        if self.rank[p] > self.rank[q]:
            self.par[q] = p
        elif self.rank[q] > self.rank[p]:
            self.par[p] = q
        else:
            self.par[p] = q
            self.rank[q] += 1
        
        self.comps -= 1
        return True

    def getNumComponents(self) -> int:
        return self.comps
