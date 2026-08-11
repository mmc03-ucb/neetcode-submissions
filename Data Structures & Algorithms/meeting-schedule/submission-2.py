"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        we need to check if the start time of (i+1) meeting
        coincides with end time of ith meeting
        sort by start time 
        [(0, 15), (20, 25), (13, 17)]
        """
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        end = intervals[0].end

        for i in range(1, len(intervals)):
            start = intervals[i].start
            if start < end:
                return False
            end = intervals[i].end
        
        return True


