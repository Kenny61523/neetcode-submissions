class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting 
        nums.sort()
        res = []
        # -4, -1, -1, 0, 1, 2
        for i, n in enumerate(nums):
            # remove duplicates 
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            rem = 0 - n

            l, r = i + 1, len(nums) - 1
            while l < r:
                    
                if nums[l] + nums[r] == rem: 
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r + 1 and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[l] + nums[r] > rem: 
                    r -= 1
                else: 
                    l += 1
                
        return res 