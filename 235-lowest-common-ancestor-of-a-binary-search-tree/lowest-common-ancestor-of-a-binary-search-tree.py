# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [root]

        def dfs(node):
            if not node:
                return 
            res[0] = node
            if p.val < node.val and q.val < node.val:
                dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                dfs(node.right)
            else:
                return 
        dfs(root)
        return res[0]

