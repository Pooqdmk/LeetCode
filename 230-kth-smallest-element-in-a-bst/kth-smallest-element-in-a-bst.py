# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        s = [root]
        while s:
            e = s.pop()
            res.append(e.val)
            if e.right:
                s.append(e.right)
            if e.left:
                s.append(e.left)
        res.sort()
        return res[k-1]