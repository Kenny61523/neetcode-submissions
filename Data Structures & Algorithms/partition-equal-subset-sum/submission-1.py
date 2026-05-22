class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0) # base case

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for n in dp:
                nextDP.add(n + nums[i])
                nextDP.add(n)
            dp = nextDP
        
        return True if target in dp else False