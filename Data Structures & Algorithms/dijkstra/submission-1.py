class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        
        for s, d, w in edges:
            adjList[s].append((d, w))
        
        shortest = {}
        minHeap = [(0, src)]

        while minHeap:
            w, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            shortest[node] = w
            for nei, w_nei in adjList[node]:
                if nei not in shortest:
                    heapq.heappush(minHeap, (w + w_nei, nei))
        
        for s in adjList:
            if s not in shortest:
                shortest[s] = -1
        
        return shortest
        

