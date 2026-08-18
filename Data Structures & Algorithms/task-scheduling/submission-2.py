class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        ready = []
        waiting = []

        for t, c in count.items():
            heapq.heappush_max(ready, (c, t))
        
        cycle = 0
        while ready or waiting:
            cycle += 1
            # check waiting
            while waiting and waiting[0][0] < cycle:
                _, t, c = heapq.heappop(waiting)
                heapq.heappush_max(ready, (c, t))
            
            if ready:
                c, t = heapq.heappop_max(ready)
                c -= 1
                if c != 0:
                    heapq.heappush(waiting, (cycle + n, t, c))
        
        return cycle
