class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # loop through find a pair fo reach elemnt where element + pair = 0
        # initializea result list 

        # sort the array [-4, -1, -1, 0, 1, 2]
        # iterate array with pointer i
            # skip over the same number to avoid duplicates
            # calculate the difference 0 - nums[i]  
            # two pointers to determine the if theres a match 
                # skip over the same number to avoid duplicates
                # append it to result list. continue with the two pointer condition

        # return 
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            # opt
            if nums[i] > 0:
                break
            
            diff = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                pairSum = nums[l] + nums[r]

                if pairSum == diff:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif pairSum < diff:
                    l += 1
                else:
                    r -= 1
        
        return res

                

    
        