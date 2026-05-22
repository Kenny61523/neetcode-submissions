class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:        
        res = []
        nums.sort()
        def backtrack (i, cur):
            if i == len(nums):
                res.append(cur[::]) # copy of cur
                return 
            
            # include all nums[i]
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

            # exclude all nums[o]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, cur)
        
        backtrack(0, [])
        return res


        