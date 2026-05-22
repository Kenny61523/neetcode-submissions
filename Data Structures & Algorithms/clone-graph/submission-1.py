"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # hash old : new
        oldToNew = {}

        def dfs(node):
            # node in hash return node
            if node in oldToNew:
                return oldToNew[node]

            # if node in not hash make copy
            copyNode = Node(node.val)
            oldToNew[node] = copyNode

            for nei in node.neighbors:
                copyNode.neighbors.append(dfs(nei))
            
            return copyNode
        
        return dfs(node) if node else None


            