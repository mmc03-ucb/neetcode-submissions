"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        put active meetings in a separate array
        sorted by meeting end times
        if a new meeting start time > earliest end time:
            pop the end time interval
        return len of array
        """

        rooms = []

        intervals.sort(key = lambda x: x.start)

        for i in intervals:
            s = i.start
            e = i.end

            if rooms and s >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        
        return len(rooms)