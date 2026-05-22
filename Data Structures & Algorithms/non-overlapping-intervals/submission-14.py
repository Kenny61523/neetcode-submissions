class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # non overlap
            if prevEnd <= start:
                prevEnd = end

            # overlapping 
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res