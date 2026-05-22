class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                # Skip duplicates: if the current candidate is the same as the previous one,
                # and it's not the first candidate at this level, then skip it.
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        return res
