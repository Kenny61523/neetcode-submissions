class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones) # pop the smallest val
            s2 = heapq.heappop(stones)
            if s2 - s1 > 0:
                heapq.heappush(stones, s1 - s2)
        
        return abs(stones[0]) if stones else 0
