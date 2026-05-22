class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (numbers[l] + numbers[r]) != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
        
        return[l + 1, r + 1]

        for i, v in enumerate(numbers):
            diff = target - v
            if diff <= v:
                if numbers[i - 1] == diff: 
                    return [i, i+1]
        
        return 