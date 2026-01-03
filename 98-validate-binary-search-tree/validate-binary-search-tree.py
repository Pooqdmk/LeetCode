# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None]
        valid = [True]
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            if prev[0] != None:
                if prev[0] >= node.val:
                    valid[0] = False
            prev[0] = node.val
            if valid[0]:
                dfs(node.right)
        dfs(root)
        return valid[0]

