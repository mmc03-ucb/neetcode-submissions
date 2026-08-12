class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        we need to track 2 things: count remaining of each task, and cooldown period
        we want to use tasks with higher counts first to reduce idle gaps
        we can use a maxHeap for this
        We also need another heap for cooldown periods
        when a task is allocated, it enters this cooldown heap with (n, count, task)
        at each loop, n -= 1
        when n == 0, add to maxHeap with (count, task)
        TC: nlogk but since k is fixed at 26 it is n
        SC: O(1)
        """
        taskCount = Counter(tasks)
        countHeap = []
        for t, c in taskCount.items():
            heapq.heappush_max(countHeap, (c, t))

        coolDown = []

        cycle = 0

        while countHeap or coolDown:
            cycle += 1
            while coolDown and coolDown[0][0] < cycle:
                _, c, t = heapq.heappop(coolDown)
                heapq.heappush_max(countHeap, (c, t))
            if countHeap:
                c, t = heapq.heappop_max(countHeap)
                c -= 1
                if c > 0:
                    heapq.heappush(coolDown, (cycle + n, c, t))
        
        return cycle

