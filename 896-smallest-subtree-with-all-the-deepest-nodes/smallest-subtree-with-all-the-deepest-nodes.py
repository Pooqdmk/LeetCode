# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        d = {None: -1}

        def dfs(node, parent = None):
            if not node:
                return 
            
            d[node] = d[parent] + 1
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root)
        mx = max(d.values())
        res = []
        def ans(node):
            if not node or mx == d.get(node):
                return node
            
            left = ans(node.left)
            right = ans(node.right)

            if left and right:
                return node
            
            if left:return left
            if right:return right
            return None
        return ans(root)


            
