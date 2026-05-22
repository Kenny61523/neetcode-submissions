class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keep track of the maximum jump at eadch point i 
        # bottom up dp 
        # dp = [0] * (len(nums) + 1)
        curPos = len(nums) - 1
        # we dont care about the last element 
        for i in range(len(nums) - 2, -1, -1):
            # when connected 
            if nums[i] + i >= curPos:
                curPos = i
            # not connected

        return curPos == 0