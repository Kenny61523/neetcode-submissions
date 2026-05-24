class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # initialize res
        crsToPre = {i: [] for i in range(numCourses)}
        # create a hash fo prereq to course
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)
        res = []
        visiting = set()
        visited = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)
            for pre in crsToPre[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res