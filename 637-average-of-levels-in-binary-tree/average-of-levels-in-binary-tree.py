# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque([root])
        res = []
        while q:
            n = len(q)
            l = 0
            for i in range(n):
                node = q.popleft()
                l+=node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(l/n)
        return res
        