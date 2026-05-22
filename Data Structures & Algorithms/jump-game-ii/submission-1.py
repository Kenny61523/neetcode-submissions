class Solution:
    def jump(self, nums: List[int]) -> int:
        # sliding window 
        # you want to maximize the window -> minimize the number of jumps
        l = r = 0
        res = 0

        while r < len(nums) - 1:
            # the window size
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        
        return res
