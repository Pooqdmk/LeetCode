# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def dfs(node):
            if not node:
                return (None, 0)
            
            left, l_dis = dfs(node.left)
            right, r_dis = dfs(node.right)

            if l_dis > r_dis:
                return (left, l_dis+1)
            elif r_dis > l_dis:
                return (right, r_dis+1)
            else:
                return (node,l_dis+1)
        return dfs(root)[0]