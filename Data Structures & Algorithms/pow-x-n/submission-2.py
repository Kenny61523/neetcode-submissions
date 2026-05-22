class Solution:
    def myPow(self, x: float, n: int) -> float:
        # cse n == 0
        if n == 0:
            return 1

        res = x
        i = 1
        
        while i < abs(n - 0):
            res *= x
            i += 1
            print(f"i:{res}")

        # case n < 0
        print(f"res:{res}")
        if n < 0:
            return 1 / res
        else:
            return res