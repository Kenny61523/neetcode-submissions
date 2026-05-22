class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []

        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return 
            
            # subset to include 
            cur.append(nums[i])
            dfs(i + 1)
            
            # subset to exclude
            cur.pop()
            dfs(i + 1)

        dfs(0)
        return res