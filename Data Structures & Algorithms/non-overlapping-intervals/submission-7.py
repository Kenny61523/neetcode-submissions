class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i:i[0])
        prevEnd = intervals[0][1]
        res = 0

        for left, right in intervals[1:]:
            if left >= prevEnd:
                prevEnd = right
            else:
                res += 1
                prevEnd = min(right, prevEnd)

        return res        