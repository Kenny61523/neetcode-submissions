class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsToPre = {i : [] for i in range(numCourses)}

        # creae a hash relation 
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)
        
        visiting = set()
        # recursion to check if all pres are valid
        def dfs(crs):
            print(crs)
            if crsToPre[crs] == []:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)
            for pre in crsToPre[crs]:
                if not dfs(pre):
                    return False
            crsToPre[crs] = []
            return True

        # iteration 
        for a in range(numCourses):
            if not dfs(a):
                return False
        
        return True
