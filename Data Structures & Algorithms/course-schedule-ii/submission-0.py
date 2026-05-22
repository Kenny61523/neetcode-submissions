class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses)}
        
        for crs, pre, in prerequisites:
            prereq[crs].append(pre)
        
        visit, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            visit.add(crs)
            res.append(crs)
            cycle.remove(crs)        

        for i in range(numCourses):
            if dfs(i) == False: return []
            print(i)
        
        return res

