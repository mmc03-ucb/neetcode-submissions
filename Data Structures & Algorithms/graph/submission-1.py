class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList or dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        q = collections.deque()
        visit = set()

        q.append(src)
        visit.add(src)

        while q:
            for i in range(len(q)):
                v = q.popleft()
                if v == dst:
                    return True
                
                for n in self.adjList[v]:
                    if n in visit:
                        continue
                    q.append(n)
                    visit.add(n)
        return False
