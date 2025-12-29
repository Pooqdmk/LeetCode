# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        s = [(root,root.val)]
        cnt = 0
        while s:
            node, mx = s.pop()
            m = mx
            if node.val >= mx:
                cnt+=1
            if node.right:
                mx  = max(mx, node.right.val)
                s.append((node.right, mx))
            if node.left:
                m  = max(m, node.left.val)
                s.append((node.left, m))
        return cnt

            
