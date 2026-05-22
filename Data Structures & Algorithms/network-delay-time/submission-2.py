from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, ti in times:
            edges[u].append((v, ti))
        
        minHeap = [(0, k)] # base case (w, n)
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            t = max(t, w1)
            visit.add(n1)
            for n2, w2 in edges[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1