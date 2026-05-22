class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs to do all permutations
        # initialize ressulting list

        # define dfs function 
            # base case is when cnt reahes len(nums) or 
        cur = []
        res = []
        def dfs(cnt):
            if cnt == len(nums):
                res.append(cur.copy())
                return

            # subset to includei
            cur.append(nums[cnt])
            dfs(cnt + 1)

            # subset to go to the next element
            cur.pop()
            dfs(cnt + 1)
    
        dfs(0)
        return res



