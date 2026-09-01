class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        q = deque()

        for t,c in count.items():
            heapq.heappush_max(heap, (c, t))
        
        cycles = 0
        while heap or q:
            cycles += 1
            while q and q[0][1] < cycles:
                t, _ = q.popleft()
                heapq.heappush_max(heap, (count[t], t))
            if heap:
                c, t = heapq.heappop_max(heap)
                count[t] -= 1
                if count[t] != 0:
                    q.append((t, cycles + n))
        
        return cycles
            
            
