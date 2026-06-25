class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)
        for src, dst in edges:
            adjList[src].append(dst)
        
        def dfs(node, topSort, visited, path):
            if node in path:
                return False
            if node in visited:
                return True
            
            
            path.add(node)
            for nei in adjList[node]:
                if not dfs(nei, topSort, visited, path):
                    return False
            visited.add(node)
            topSort.append(node)
            path.remove(node)
            return True

        topSort = []
        visited = set()
        path = set()

        for node in range(n):  # Ensuring all nodes are considered
            if node not in visited:
                if not dfs(node, topSort, visited, path):
                    return []  # Return empty list if a cycle is detected
        
        topSort.reverse()
        return topSort
        


