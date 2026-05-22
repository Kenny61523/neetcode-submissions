class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            mask = (n >> i) & 1
            res = res | (mask << (31 - i))
        return res