class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 0, 0

        res = [1] * len(nums)
        cur = 1
        for i in range(1, len(nums)):
            cur *= nums[i - 1]
            res[i] *= cur
        
        print(res)

        cur = 1
        for i in range(len(nums) - 2, -1, -1):
            cur *= nums[i + 1]
            res[i] *= cur
        
        
        return res