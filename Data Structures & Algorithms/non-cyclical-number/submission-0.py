class Solution:
    def isHappy(self, n: int) -> bool:
        
        # dfs with a 
        repeats = set()

        def dfs(n):
            curSum = 0
            while n > 0:
                curSum += (n % 10) ** 2
                n //= 10 

            if curSum == 1:
                return True
            if curSum in repeats:
                return False

            repeats.add(curSum)
            return dfs(curSum)
        
        return dfs(n)