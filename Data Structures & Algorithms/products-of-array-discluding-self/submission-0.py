class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        sum = 1

        for i in range(len(nums)):
            for index, val in enumerate(nums):
                if index == i: continue
                sum *= val
            res.append(sum)
            sum = 1

        return res