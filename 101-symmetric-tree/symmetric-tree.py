# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        bal = [True]
        def check(a,b):
            if not a and not b:
                return
            
            if (not a and b) or (not b and a):
                bal[0] = False
                return
            
            elif a.val != b.val:
                bal[0] = False
                return
            
            check(a.left, b.right)
            check(a.right,b.left)

        check(root.left,root.right)
        return bal[0]