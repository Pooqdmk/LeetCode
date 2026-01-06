# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        mx = -10**5
        l = 1
        res = -1
        q = deque([root])
        while q:
            n = len(q)
            s = 0
            
            for i in range(n):
                node=q.popleft()
                s+=node.val
                if node.left: q.append(node.left)
                if node.right:q.append(node.right)
                
            if s > mx:
                mx = s
                res = l
            l+=1
        return res

