"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        # interval?
        intervals.sort(key = lambda i : i.start)
        print(intervals)
        prev = intervals[0]

        for interval in intervals[1:]:
            if prev.end > interval.start:
                return False

            prev = interval

        return True