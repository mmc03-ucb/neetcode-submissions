class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inDeg = defaultdict(int)
        order = []

        for u, v in prerequisites:
            adjList[u].append(v)
            inDeg[v] += 1
        
        q = deque(i for i in range(numCourses) if inDeg[i] == 0)

        while q:
            curr = q.popleft()
            order.append(curr)
            for v in adjList[curr]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        
        return order[::-1] if len(order) == numCourses else []