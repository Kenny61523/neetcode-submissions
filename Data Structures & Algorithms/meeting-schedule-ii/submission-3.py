"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals is sorted 
        cur = 0
        res = 0
        # keep track of two states: start[] and end[]

        starts = [x.start for x in intervals]
        starts.sort()
        ends = [x.end for x in intervals]
        ends.sort()
        s, e = 0, 0

        while s < len(intervals):
            # additional meeting rooms
            if starts[s] < ends[e]:
                s += 1
                cur += 1
                res = max(res, cur)

            # meeting has finished - decrement number of active meeting rooms
            else:
                e += 1
                cur -= 1
            
        return res