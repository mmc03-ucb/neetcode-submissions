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
        if src not in self.adjList or dst not in self.adjList:
            return False
        if dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True
        

    def hasPath(self, src: int, dst: int) -> bool:
        if dst in self.adjList[src]:
            return True
        if not self.adjList[src]:
            return False
        for d in self.adjList[src]:
            if self.hasPath(d, dst):
                return True
        return False
