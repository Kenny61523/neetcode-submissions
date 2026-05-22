class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        res = [1] * len(nums)
        cur = 1
        for i in range(len(nums) - 1):
            cur *= nums[i]
            res[i + 1] *= cur

        cur = 1
        for i in range(len(nums) - 2, -1, -1):
            cur *= nums[i + 1]   
            res[i] *= cur      

        return res
