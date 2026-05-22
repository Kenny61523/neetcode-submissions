class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if overlapping then merge 

        # English solution 
        # traverse through array (interval has no overlap by defualt)
        
        # soon as you see a inteval start_i < cur_start_i compare the one before to merge 
        # check if the i - 1 and i element needs to be merged -> modify i - 1

        # chekc if the i - 1 and i elemnt needs to be merged. -> modify i - 1 & pop i + 1

        # cosntructin gres version 
        res = []
        for cur in intervals:
            # cur interval is before
            if cur[1] < newInterval[0]:
                res.append(cur)
            # cur is after new inter
            elif cur[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = cur ###
            else:
                newInterval[0] = min(newInterval[0], cur[0])
                newInterval[1] = max(newInterval[1], cur[1])
        res.append(newInterval)
        return res
