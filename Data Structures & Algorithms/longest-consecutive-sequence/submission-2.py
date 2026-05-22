class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
        #check is n -1 exists 
            if (n - 1) not in nums:
                length = 0
                while (n + length) in nums:
                    length += 1
                longest = max(length, longest)

        return longest