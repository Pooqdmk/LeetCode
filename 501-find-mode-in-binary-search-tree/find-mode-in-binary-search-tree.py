# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = {}

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            d[node.val] = d.get(node.val,0)+1
            dfs(node.right)

        dfs(root)
        mx = max(d.values())
        l = sorted(d.items(), key = lambda x: x[1])
        res = []

        for k,v in l:
            if v == mx:
                res.append(k)
        return res
        
