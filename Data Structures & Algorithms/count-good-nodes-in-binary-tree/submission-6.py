# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur, maxVal):
            if not cur:
                return 0
            
            res = 1 if maxVal <= cur.val else 0
            maxVal = max(maxVal, cur.val)
            res += dfs(cur.left, maxVal)
            res += dfs(cur.right, maxVal)
            return res
        
        return dfs(root, root.val)


