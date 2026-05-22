from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return Tue

        adj = { i:[] for i in range(n) }

        # create links for both 
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visiting = set()
        def dfs(cur, prev):
            if cur in visiting:
                return False
            
            visiting.add(cur)

            for nxt in adj[cur]:
                if nxt == prev:
                    continue
                if not dfs(nxt, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visiting) == n


            

            
    