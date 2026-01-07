# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node, curr):
            if not node:
                return 
            
            curr.append(str(node.val))
            # print(curr)
            if not node.left and not node.right:
                res[0]+=int(''.join(curr))
            dfs(node.left, curr)
            dfs(node.right, curr)
            curr.pop()
        dfs(root,[])
        return res[0]
