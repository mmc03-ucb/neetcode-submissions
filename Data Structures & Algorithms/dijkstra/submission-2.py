class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = collections.defaultdict(list)
        for s, dst, w in edges:
            adjList[s].append((dst, w))
        
        minHeap = [(0, src)]
        distance = {}

        while minHeap:
            w, nd = heapq.heappop(minHeap)
            if nd in distance:
                continue
            distance[nd] = w

            for nei, wei in adjList[nd]:
                if nei not in distance:
                    newWei = w + wei
                    heapq.heappush(minHeap, (newWei, nei))
        
        for i in range(n):
            if i not in distance:
                distance[i] = -1
        
        return distance

                