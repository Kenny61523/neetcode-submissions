import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stack = []

        # sort by distance
        for x, y in points:
            dist = ((x - 0)**2 + (y - 0)**2)
            stack.append([dist, x, y])

        heapq.heapify(stack)
        res = []
        while k > 0:
            d, x, y = heapq.heappop(stack)
            res.append([x, y])
            k -= 1
        
        return res