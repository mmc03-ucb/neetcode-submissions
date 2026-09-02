class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if not self.heap1 or num <= self.heap1[0]:
            heapq.heappush_max(self.heap1, num)
        else:
            heapq.heappush(self.heap2, num)
        
        if len(self.heap1) - len(self.heap2) > 1:
            heapq.heappush(self.heap2, heapq.heappop_max(self.heap1))
        elif len(self.heap2) - len(self.heap1) > 1:
            heapq.heappush_max(self.heap1, heapq.heappop(self.heap2))

    def findMedian(self) -> float:
        if len(self.heap1) > len(self.heap2):
            return self.heap1[0]
        elif len(self.heap2) > len(self.heap1):
            return self.heap2[0]
        return (self.heap1[0] + self.heap2[0]) / 2
        