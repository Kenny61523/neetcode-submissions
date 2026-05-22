class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n): # tree condensation
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

            
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)

            if n1 == n2:
                return 0
            
            if rank[n2] > rank[n1]:
                par[n1] = par[n2]
                rank[n2] += rank[n1]

            else:
                par[n2] = par[n1]
                rank[n1] += rank[n2]
            return 1

        #perforem union if false then res += 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res