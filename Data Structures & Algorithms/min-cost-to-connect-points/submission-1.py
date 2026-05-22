class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # set up dict
        n = len(points)
        adj = { i: [] for i in range(n)} # (cost, node)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        #primes
        minHeap = [(0, 0)]
        res = 0 
        visit = set()

        while len(visit) < n:
            cost, j = heapq.heappop(minHeap)
            if j in visit:
                continue
            res += cost
            visit.add(j)

            for costNei, nei in adj[j]:
                if nei not in visit:
                    heapq.heappush(minHeap, (costNei, nei))
        return res

