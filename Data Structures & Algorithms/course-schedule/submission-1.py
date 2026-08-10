class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        inDeg = defaultdict(int)

        for u,v in prerequisites:
            adjList[u].append(v)
            inDeg[v] += 1
        
        q = deque(i for i in range(numCourses) if inDeg[i] == 0)

        while q:
            c = q.popleft()
            for v in adjList[c]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        
        for v in inDeg.values():
            if v != 0:
                return False
        
        return True