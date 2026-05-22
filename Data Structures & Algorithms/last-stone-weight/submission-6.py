class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #create mac heapq 
        # for i, n in enumerate(stones):
        #     stones[i] = -n
        stones = [ -n for n in stones]

        heapq.heapify(stones)
        # smallest = heapq.heappop(nums)
        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)

            if a != b:
                heapq.heappush(stones, -(a - b))
            
        return -heapq.heappop(stones) if len(stones) else 0

     