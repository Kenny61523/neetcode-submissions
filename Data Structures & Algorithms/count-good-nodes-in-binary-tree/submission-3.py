# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            # A node is "good" if its value is greater than or equal to the max so far.
            count = 1 if node.val >= max_so_far else 0
            # Update the max_so_far value for the next recursion.
            max_so_far = max(max_so_far, node.val)
            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)
            return count
        
        # Start the recursion with the root's value as the initial maximum.
        return dfs(root, root.val)
