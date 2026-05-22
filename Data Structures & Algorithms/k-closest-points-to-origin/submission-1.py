class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minStack = []

        for point in points:
            dis = point[0] ** 2 + point[1] ** 2
            minStack.append([dis, point[0], point[1]])
        
        heapq.heapify(minStack)
        res = []

        while k > 0:
            dis, x, y = heapq.heappop(minStack)
            res.append([x, y])
            k -= 1
        
        return res

        