class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # initialize res
        crsToPre = {i: [] for i in range(numCourses)}
        # create a hash fo prereq to course
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)
        res = []
        visited = set()
        visiting = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crs in visiting:
                return True 
            
            visited.add(crs)
            for pre in crsToPre[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            visiting.add(crs)
            res.append(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res