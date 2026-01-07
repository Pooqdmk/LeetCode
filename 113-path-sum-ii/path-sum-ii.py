# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        curr = []
        res = []
        def dfs(node,s):
            if not node:
                return 0
            s+= node.val
            curr.append(node.val)
            
            if s == targetSum and not node.left and not node.right:
                res.append(curr[:])

            left = dfs(node.left,s)
            right = dfs(node.right,s)

            s -= curr.pop()
        dfs(root,0)
        return res
