class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = res = nums[0]

        for n in nums[1:]:
            tmp = n * curMax
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(curMax, res)
        
        return res