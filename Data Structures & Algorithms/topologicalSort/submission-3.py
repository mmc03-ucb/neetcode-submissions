class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)
        for s, d in edges:
            adjList[s].append(d)
        
        def dfs(nd, path):
            if nd in path:
                return False
            
            if nd in visited:
                return True

            path.add(nd)
            for nei in adjList[nd]:
                if not dfs(nei, path):
                    return False
            output.append(nd)
            visited.add(nd)
            path.remove(nd)
            return True
        
        visited = set()
        output = []

        for i in range(n):
            if not dfs(i, set()):
                return []
        
        return output[::-1]