import heapq
import collections
from typing import List

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return -1  # No edges means no spanning tree

        # Step 1: Create adjacency list
        adjList = collections.defaultdict(list)
        for src, dst, w in edges:
            adjList[src].append((dst, w))
            adjList[dst].append((src, w))

        # Step 2: Start Prim’s Algorithm from node 0
        minHeap = [(0, 0)]  # (weight, node)
        visit = set()
        total_weight = 0

        while minHeap and len(visit) < n:
            wei, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            total_weight += wei

            for nei, nei_w in adjList[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (nei_w, nei))

        # If not all nodes are visited, return -1 (graph is disconnected)
        return total_weight if len(visit) == n else -1
