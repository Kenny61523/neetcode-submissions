class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minV = prices[0]
        for p in prices:
            minV = min(minV, p)
            if p - minV > maxP:
                maxP = p - minV
        
        return maxP
            