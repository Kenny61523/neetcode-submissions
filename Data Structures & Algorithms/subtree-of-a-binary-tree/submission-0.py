# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root, sRoot):
            if not root and not sRoot:
                return True
            
            if not root or not sRoot or root.val != sRoot.val:
                return False

            return sameTree(root.left, sRoot.left) and sameTree(root.right, sRoot.right)
        
        def dfs(cur, sRoot):
            if not cur: return False
            if sameTree(cur, sRoot): return True
            return dfs(cur.left, sRoot) or dfs(cur.right, sRoot)
            
        return dfs(root, subRoot)


