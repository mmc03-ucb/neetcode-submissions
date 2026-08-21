"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)

        heap = []

        for i in intervals:
            s = i.start
            e = i.end
            if not heap or s < heap[0]:
                heapq.heappush(heap, e)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, e)
        
        return len(heap)