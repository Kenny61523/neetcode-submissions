class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bits operators: ^ XOR & AND | OR >>, << for shift.
        total = len(nums)
        for i in range(len(nums)):
            total += i - nums[i]

        return total


    