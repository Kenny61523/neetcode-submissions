class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges is None: return True
        tree = { t:[] for t in range(n)}

        for child, parent in edges:
            tree[child].append(parent)
            tree[parent].append(child)
        
        visit = set()
        def dfs(cur, prev):
            if cur in visit:
                return False
            visit.add(cur)

            for node in tree[cur]:
                if node == prev: 
                    continue
                if dfs(node, cur) == False:
                    return False
            return True
    
        return dfs(0, -1) and n == len(visit)
        
        
            