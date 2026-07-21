"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x : x.start)

        curr = intervals[0]
        for i in range(1,len(intervals)):
            if curr.end <= intervals[i].start:
                curr = intervals[i]
            elif curr.start >= intervals[i].end:
                curr = intervals[i]
            else:
                return False
        return True