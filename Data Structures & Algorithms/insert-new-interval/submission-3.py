class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # keep constructing the new interval 
        res = []
        for i, cur in enumerate(intervals):
            # before 
            if cur[1] < newInterval[0]:
                res.append(cur)
            # after 
            elif newInterval[1] < cur[0]:
                res.append(newInterval)
                return res + intervals[i:]

            # overlapa
            else: 
                newInterval[0] = min(newInterval[0], cur[0])
                newInterval[1] = max(newInterval[1], cur[1])
        res.append(newInterval)
        return res