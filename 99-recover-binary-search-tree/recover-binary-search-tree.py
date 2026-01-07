# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            l.append(node.val)
            dfs(node.right)
        dfs(root)
        l.sort()
        i = [0]
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if node.val != l[i[0]]:
                node.val = l[i[0]]
            i[0]+=1
            dfs(node.right)
        dfs(root)