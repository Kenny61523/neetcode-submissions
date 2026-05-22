class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bits operators: ^ XOR & AND | OR >>, << for shift.
        total = 0
    
        for i in range(len(nums) + 1):
            total += i

        for i in range(len(nums)):
            total -= nums[i]
        
        return total


    