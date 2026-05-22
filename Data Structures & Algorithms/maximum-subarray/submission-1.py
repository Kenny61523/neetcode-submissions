class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # take the maximum (greedy) 
        # parse throguh the array 
        # brut force: O()
        # create an arry to keep track of the highest sum upto that point 
        # edge case

        

        prevSum = nums[0]
        curSum = 0
        res = float('-inf')
        # advance by 2
        for n in nums:
            # restart if the curSum becoems negative
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(res, curSum)            

        return res
            