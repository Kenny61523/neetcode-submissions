class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myMap = {}

        for i in nums:
            myMap[i] = myMap.get(i, 0) + 1
            if myMap[i] > 1: return i
            
        