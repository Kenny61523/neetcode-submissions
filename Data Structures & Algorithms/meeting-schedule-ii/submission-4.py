"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Initialize start stack & finish stack 
        start, finish = [], []
        for interval in intervals:
            start.append(interval.start)
            finish.append(interval.end)
        start.sort()
        finish.sort()
        res, cur = 0, 0
        s, f = 0, 0
        while s < len(intervals):
            print(cur)
            if start[s] < finish[f]:
                cur += 1
                s += 1
            else:
                cur -= 1
                f += 1
            res = max(res, cur)
        
        return res
        