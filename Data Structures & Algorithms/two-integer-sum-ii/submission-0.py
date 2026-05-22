class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = {}
        for i, v in enumerate(numbers):
            diff = target - v
            if diff in prev:
                return [prev[diff], i + 1]
            prev[v] = i + 1
        
        return 