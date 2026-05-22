class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsToPre = { i:[] for i in range(numCourses)}
        visiting = set()
        visited = set()
        res = []
        # set up
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            res.append(crs)
            visiting.add(crs)
            for pre in crsToPre[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            # construct res
            res.append(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
        
  