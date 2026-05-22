class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # for i, n in enumerate(nums):
        #     if (n == target): 
        #         return i
        index = 0

        for n in range(len(nums)):
            if nums[n] == target: 
                return index
            index += 1

        return -1




