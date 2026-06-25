class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)
       
        for src, dst, w in edges:
            adjList[src].append([dst, w])
            adjList[dst].append([src, w])
        
        visited = set()
        minHeap = []

        for nod, w in adjList[edges[0][0]]:
            heapq.heappush(minHeap, [w, nod])
        
        visited.add(edges[0][0])
        totalWeight = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            
            totalWeight += w1

            for n2, w2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [w2, n2])
        
        return totalWeight if len(visited) == n else -1