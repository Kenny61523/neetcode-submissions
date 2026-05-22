# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            # The current node's value must be between low and high
            if not (low < node.val < high):
                return False
            # Recursively validate the left and right subtrees with updated bounds
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))



        
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         self.minMax = [root.val + 1, root.val - 1]

#         def dfs(cur, left):
#             if not cur:
#                 return True
#             if left:
#                 if not cur.val < self.minMax[0]:
#                     return False
#             else:
#                 if not cur.val > self.minMax[1]:
#                     return False
#             self.parentVal = cur.val
#             print(cur.val)

#             return  (dfs(cur.left, True) and 
#                      dfs(cur.right, False))
        
#         return dfs(root, True)