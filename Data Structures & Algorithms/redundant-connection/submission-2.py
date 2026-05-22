class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)] # [0, 1, ... , N]
        rank = [1] * (N + 1) # size of nodes are initially 1 
        
        def find(n): # finds the parent
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]

    
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)

            if n1 == n2:
                return False # could not be merge
            
            if rank[n1] > rank[n2]: #smaller tree is merged to the bigger tree
                par[n2] = par[n1]
                rank[n2] += rank[n1]

            else:
                par[n1] = par[n2]
                rank[n1] += rank[n2]
            return True 
        
        for n1, n2 in edges:
            if union(n1, n2) == False:
                return [n1, n2]
                