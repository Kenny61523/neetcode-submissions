class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # algo: run to loops forward and backword, for each loop kep multipling current number by the prevous number

        # have an array of 1 (base val for multiplication)
        # have a placeholder val n
        # forward loop starting at i = 1
            # update n by n * nums[i - 1]
            # update nums[i] to nums[i] * n

        # res [1, 1, 2, 8]
            
        # backeward loop ending at j = 1
            # update m by m * nums[j + 1]
            # update the state var m *= nums[j]
            
        # res [48,24, 12,8]

        # return

        #code 
        res = [1] * len(nums)
        n = 1
        for i in range(1,len(nums)):
            n *= nums[i - 1]
            res[i] *= n
            # n *= nums[i]
        print(res) # [1, 1, 2, 8]

        n = 1
        for j in range(len(nums) - 2, -1, -1):
            n *= nums[j + 1]
            res[j] *= n
        

        print(res) 
        return res