class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        if (r == 0):
            if nums[r] == target: return 0
            else: return -1

        while (l < r):
            if nums[l] == target: return l
            if nums[r] == target: return r
            if nums[l] > target or nums[r] < target:
                break

            difL = target - nums[l]
            difR = nums[r] - target
            
            if difL > difR: l += 1
            else: r -= 1


        return -1




