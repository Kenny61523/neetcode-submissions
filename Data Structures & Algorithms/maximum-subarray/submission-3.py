class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = 0
        res = nums[0]
        for n in nums:
            # reset when cur becomes negative (better to exclude the prev subarray) 
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(res, curSum)

        return res