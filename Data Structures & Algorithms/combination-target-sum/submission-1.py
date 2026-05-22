class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            
            # break case
            if i >= len(nums) or total > target:
                return

            # keep adding elements
            cur.append(nums[i])
            dfs(i, total + nums[i], cur)
            # advance throuhg the array nums
            cur.pop()
            dfs(i + 1, total, cur)
        
        dfs(0, 0, [])
        return res

