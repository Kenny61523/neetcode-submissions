class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        res = 0 
        cur = 0
        l, r = 0, len(heights) - 1

        while l < r:
            lw = heights[l]
            rw = heights[r]
            
            cur = min(rw, lw) * (r - l)
            res = max(cur, res)
            if lw < rw: 
                l += 1
            else: 
                r -= 1
            
        return res