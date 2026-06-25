import heapq
from typing import List

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])  # Path compression
        return self.par[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.par[root_x] = root_y
        else:
            self.par[root_x] = root_y
            self.rank[root_y] += 1
        
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for src, dst, w in edges:
            heapq.heappush(minHeap, (w, src, dst))
        
        mst = []
        uf = UnionFind(n)
        weight = 0

        while minHeap and len(mst) < n - 1:
            w, src, dst = heapq.heappop(minHeap)
            if uf.union(src, dst):
                mst.append([src, dst])
                weight += w
        
        return weight if len(mst) == n - 1 else -1  # Return -1 if MST is not possible
