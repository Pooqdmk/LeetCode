# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = [None]
        mn = [10**6]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if prev[0] != None:
                mn[0] = min(mn[0], abs(node.val - prev[0]))
            prev[0] = node.val
            dfs(node.right)
        dfs(root)
        return mn[0]
