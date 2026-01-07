# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = [0]

        def comp(node):
            if not node:
                return 
            total[0]+=node.val
            comp(node.left)
            comp(node.right)
        comp(root)
        mx = [0]

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            curr = node.val + left + right
            mx[0] = max(mx[0], (total[0]-curr)*curr)
            return curr
        dfs(root)
        return mx[0]%(10**9 + 7)
        