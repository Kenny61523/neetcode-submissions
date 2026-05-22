class Solution:
    def rob(self, nums: List[int]) -> int:

        def robber(nums):
        # start from pos 0 or 1
            rob1, rob2 = 0, 0

            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        # edge 1 you cannot rob1 from the frist and last house
        return max(nums[0], robber(nums[1:]), robber(nums[:-1]))

