class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = { i: [] for i in range(n)} # [cost, node]

        # create adj list
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        visit = set()
        minHeap = [[0, 0]]
        # Prim's
        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue 
            res += cost
            visit.add(i)

            for cost2, j in adj[i]:
                if j not in visit:
                    heapq.heappush(minHeap, [cost2, j])
        
        return res
