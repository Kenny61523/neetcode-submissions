class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # uniue combination
        res = []
        def dfs(total, cur, i):
            if total > target or i >= len(nums):
                return 
            if total == target:
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(total + nums[i], cur, i)

            cur.pop()
            dfs(total, cur, i + 1)
        
        dfs(0, [], 0)
        return res