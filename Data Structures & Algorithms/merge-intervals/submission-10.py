class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by first number 
        res = []
        intervals.sort()
        cur = intervals[0]
        # sort the i and i - 1 element 
        for i in range(1, len(intervals)):
            # no merge 
            if cur[1] < intervals[i][0]:
                res.append(cur)
                cur = intervals[i]
            # merge 
            else:
                # intervals[i - 1][0] = min(intervals[i - 1][0], intervals[i][0])
                cur[0] = min(cur[0], intervals[i][0])
                cur[1] = max(cur[1], intervals[i][1])
        res.append(cur)
        return res