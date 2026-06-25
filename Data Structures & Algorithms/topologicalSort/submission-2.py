class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        
        for src, dst in edges:
            adjList[src].append(dst)

        visit = set()
        path = set()
        topSort = []

        def dfs(nd):
            if nd in path:
                return False
            
            if nd in visit:
                return True
            
            path.add(nd)

            for nei in adjList[nd]:
                if not dfs(nei):
                    return False
            
            path.remove(nd)
            visit.add(nd)
            topSort.append(nd)
            return True
        

        for node in range(n):
            if not dfs(node):
                return []
        topSort.reverse()
        return topSort