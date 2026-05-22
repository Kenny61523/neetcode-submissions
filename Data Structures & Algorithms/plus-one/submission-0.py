from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # take into carry inmind 

        # top bottom approach
        # for i in range(len(digits) - 1, -1, -1):
        #     carry = 0
        #     if digits[i] + 1 == 10:
                
        res = deque()

        def dfs(carry, i):
            if i < 0:
                if carry == 1:
                    res.appendleft(1)
                return res

            curDigit = digits[i] + carry 
            if curDigit == 10:
                carry = 1
                res.appendleft(0)
            else:
                carry = 0
                res.appendleft(curDigit)
            return dfs(carry, i - 1)

        dfs(1, len(digits) - 1)
        return list(res)