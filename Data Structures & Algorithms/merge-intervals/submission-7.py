class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # edge case
        if not intervals:
            return []

        # interval 
        intervals.sort(key = lambda i : i[0])        
        res = [intervals[0]]
        leftMin, rightMax = res[0][0],  res[0][1]
        
        # if the array is sorted, then the following logic works (?)
        for i in range(1, len(intervals)):
            # merge into new interval
            if rightMax >= intervals[i][0]:
                res.pop()
                leftMin = min(leftMin, intervals[i][0])
                rightMax = max(rightMax, intervals[i][1])
                res.append([leftMin, rightMax])
            else:
                res.append(intervals[i])
                leftMin, rightMax = intervals[i]
        return res
            
            