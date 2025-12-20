# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = [True]
        def check(p,q):
            if not p and not q:
                return
            if (p and not q) or (q and not p):
                same[0] = False
                return 
            if p.val != q.val:
                same[0] = False
                return
            left,right = check(p.left,q.left), check(p.right,q.right)
            
        check(p,q)
        return same[0]

