class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxStack = []
        for num in nums:
            maxStack.append(-num)
        
        heapq.heapify(maxStack)

        while k > 0:
            n = heapq.heappop(maxStack)
            k -= 1
        
        return -n