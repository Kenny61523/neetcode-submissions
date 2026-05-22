from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()        
        res = [intervals[0]]
        leftMin, rightMax = res[0][0], res[0][1]
        
        for i in range(1, len(intervals)):
            if rightMax >= intervals[i][0]:
                # merge intervals
                res.pop()
                leftMin = min(leftMin, intervals[i][0])
                rightMax = max(rightMax, intervals[i][1])
                res.append([leftMin, rightMax])
            else:
                # start a new interval group
                res.append(intervals[i])
                leftMin, rightMax = intervals[i]   # 🔧 reset bounds here
                
        return res
