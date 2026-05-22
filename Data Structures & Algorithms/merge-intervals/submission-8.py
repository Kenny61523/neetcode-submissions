class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # edge case
        if not intervals:
            return []

        # interval 
        intervals.sort(key = lambda i : i[0])        
        res = [intervals[0]]
        
        # if the array is sorted, then the following logic works (check)
        for left, right in intervals[1:]:
            # merge into new interval
            lastEnd = res[-1][1]
            if lastEnd >= left:
                res[-1][1] = max(lastEnd, right)
            else:
                res.append([left, right])
                
        return res
            
            