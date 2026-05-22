class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            hours = 0
            m = l + ((r - l) // 2) # m = 2
            for p in piles:
                hours += math.ceil(p / m)
            
            # print(hours)
            if hours <= h:
                r = m - 1
                res = min(m, res)
            else:
                l = m + 1
        
        return res
            


        

                            
        



