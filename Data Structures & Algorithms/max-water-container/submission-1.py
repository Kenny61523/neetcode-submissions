class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #initial height

        l, r = 0, len(heights) - 1
        width = r - l
        area = width * min(heights[l], heights[r])
        # for i, h, in enumerate(heights):
        
        while l < r:
            newArea = (r - l) * min(heights[l], heights[r])
            if newArea > area: area = newArea

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return area