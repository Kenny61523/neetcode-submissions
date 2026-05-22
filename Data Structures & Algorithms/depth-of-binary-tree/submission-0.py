# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        mySet = set()

        def dfs(val, root):
            if root is None:
                mySet.add(val)
                return 
            dfs(val + 1, root.left)
            dfs(val + 1, root.right)
        
        dfs(0, root)
        return max(mySet) if mySet else 0


